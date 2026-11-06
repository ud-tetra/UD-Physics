"""Exact Q169/Q178 universal cell-stock checks on small pure complexes."""

from fractions import Fraction
from itertools import combinations


def complex_matrices(tetrahedra):
    simplices = sorted(
        {face for top in tetrahedra for degree in range(1, 5)
         for face in combinations(top, degree)}, key=lambda x: (len(x), x)
    )
    index = {simplex: i for i, simplex in enumerate(simplices)}
    n = len(simplices)
    a = [[0] * n for _ in simplices]
    for simplex in simplices:
        if len(simplex) == 1:
            continue
        j = index[simplex]
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k + 1:]
            i = index[face]
            a[i][j] = (-1) ** k
            a[j][i] = -a[i][j]
    weights = []
    for top in tetrahedra:
        weights.append([Fraction(int(set(s).issubset(top)),
                                 sum(set(s).issubset(t) for t in tetrahedra))
                        for s in simplices])
    return simplices, a, weights


def commutator(a, weights, coefficients):
    w = [sum(x * row[i] for x, row in zip(coefficients, weights))
         for i in range(len(a))]
    return [[a[i][j] * (w[i] - w[j]) for j in range(len(a))]
            for i in range(len(a))]


def run():
    simplices, a, weights = complex_matrices(((0, 1, 2, 3), (0, 1, 2, 4)))
    same = commutator(a, weights, (1, 1))
    assert all(not x for row in same for x in row)
    unequal = commutator(a, weights, (1, 0))
    witness = next((simplices[i], simplices[j], 2 * unequal[i][j])
                   for i in range(len(a)) for j in range(i + 1, len(a))
                   if unequal[i][j])
    assert witness[2] != 0
    # Any lambda=(u,v) gives u*C(1,0)+v*C(0,1); C(1,1)=0.
    assert any(x for row in unequal for x in row)  # constraint rank one
    disjoint, a2, w2 = complex_matrices(((0, 1, 2, 3), (4, 5, 6, 7)))
    assert all(not x for row in commutator(a2, w2, (1, 0)) for x in row)
    print(f"shared-face: {len(simplices)} registers; constraint rank 1; "
          f"derivative witness {witness}; equal weights conserved")
    print(f"disconnected: {len(disjoint)} registers; independent component stock conserved")


if __name__ == "__main__":
    run()
