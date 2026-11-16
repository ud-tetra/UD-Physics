"""Check the exact recursive AW5 leaf admittance against small signed-dual systems."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations

from sympy import Matrix, Rational, eye, ones, zeros


def cells_at_depth(depth):
    cells = [(0,1,2,3)]
    next_vertex = 4
    for _ in range(depth):
        children = []
        for cell in cells:
            children.extend(face+(next_vertex,) for face in combinations(cell,3))
            next_vertex += 1
        cells = children
    return cells


def terminal_response(cells):
    owners = defaultdict(list)
    for i, cell in enumerate(cells):
        for face in combinations(cell,3):
            owners[face].append(i)
    exterior = sorted(face for face, indices in owners.items() if len(indices)==1)
    assert exterior == list(combinations(range(4),3))
    # In a coherent orientation the square of each interior face flux is
    # (x_i-x_j)^2. Every child tetrahedron contributes four incident faces.
    gram = 4*eye(len(cells))
    ports = zeros(len(cells),4)
    for indices in owners.values():
        assert len(indices) in (1,2)
        if len(indices)==2:
            i,j = indices
            gram[i,j] -= 1
            gram[j,i] -= 1
    for k, face in enumerate(exterior):
        ports[owners[face][0],k] = 1
    return eye(4)-ports.T*gram.inv(method="DM")*ports


def residue(depth):
    return 1/(2*(1+Q(3,2)**depth))


def main():
    for depth in range(4):
        cells = cells_at_depth(depth)
        alpha = residue(depth)
        assert terminal_response(cells) == Rational(alpha.numerator,alpha.denominator)*(4*eye(4)-ones(4))
        print(f"depth {depth}: {len(cells)} cells per leaf, exact exterior response coefficient {alpha}")
    assert residue(5) >= Q(3,64) > residue(6)
    # Independently iterate the resistance recursion.
    resistance = Q(0)
    for depth in range(7):
        assert residue(depth) == 1/(4*(1+resistance))
        resistance += (2*resistance+1)/4
    print(f"depth 5 static residue {residue(5)}; depth 6 static residue {residue(6)}")
    print("PASS: closed form and four-terminal reduction")


if __name__ == "__main__":
    main()
