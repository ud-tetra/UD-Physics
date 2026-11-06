"""Exact source 1-to-4 and Q169 Taylor controls for cell-support filtration."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations

from assembled_readout import supports, beta0


def boundary_top(cell):
    v = sorted(cell)
    return [(frozenset(v[:i] + v[i + 1:]), (-1) ** i) for i in range(4)]


def second_order_cell_support(cells, top_amplitudes):
    """Coefficient of s_tau(t)-s_tau(0) at t^2 for dc/dt=(D-D^T)c."""
    face_first = defaultdict(int)
    owners = defaultdict(set)
    for cell in cells:
        for face, sign in boundary_top(cell):
            face_first[face] += sign * top_amplitudes[cell]
            owners[face].add(cell)
    top_second = {cell: -sum(sign * face_first[face]
                             for face, sign in boundary_top(cell)) for cell in cells}
    coeff = {cell: -top_amplitudes[cell] * (-top_second[cell])
             + sum((F(face_first[face] ** 2, len(owners[face]))
                    for face, _ in boundary_top(cell)), F(0))
             for cell in cells}
    assert sum(coeff.values()) == 0
    return coeff


if __name__ == "__main__":
    old = (frozenset((0, 1, 2, 3)),)
    refined = tuple(frozenset((4,)) | frozenset(face)
                    for face in combinations((0, 1, 2, 3), 3))
    # Source chain map fixes vertex 0. Source Q177 reassigns its one unit stock.
    ow = supports(old, {frozenset((0,)): 1})
    nw = supports(refined, {frozenset((0,)): 1})
    assert sorted(ow.values()) == [F(1)]
    assert sorted(nw.values()) == [F(0), F(1, 3), F(1, 3), F(1, 3)]
    assert sum(ow.values()) == sum(nw.values()) == 1
    assert beta0(old, ow, F(0)) == 0
    assert beta0(refined, nw, F(0)) == 1
    # Top fundamental chain is also source transported, but unit support is not.
    assert sum(supports(old, {old[0]: 1}).values()) == 1
    assert sum(supports(refined, {c: 1 for c in refined}).values()) == 4

    chain = tuple(map(frozenset, ((0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 4, 5))))
    amps = {chain[0]: 1, chain[1]: 3, chain[2]: 2}
    coeff = second_order_cell_support(chain, amps)
    assert sum(coeff.values()) == 0
    assert any(v != 0 for v in coeff.values())
    print("Q169 cell-support t^2 coefficients:", tuple(coeff[c] for c in chain))
    print("PASS: source vertex refinement changes beta0 with conserved stock; Q169 redistributes support")
