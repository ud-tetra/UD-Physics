"""Exact conditional ancestry contact for local 1-to-4 refinement histories."""
from fractions import Fraction as F
from itertools import combinations


VERTEX = 0


def refine(weights, cell, center):
    """Split the selected parent's current vertex share among incident children."""
    assert cell in weights and center not in set().union(*weights)
    out = dict(weights)
    inherited = out.pop(cell)
    children = tuple(frozenset((center,)) | frozenset(face)
                     for face in combinations(sorted(cell), 3))
    incident = tuple(c for c in children if VERTEX in c)
    assert len(incident) == 3
    for c in children:
        assert c not in out
        out[c] = inherited / 3 if c in incident else F(0)
    assert sum(out.values()) == sum(weights.values())
    return out, children


def cell(*vertices):
    return frozenset(vertices)


if __name__ == "__main__":
    old0, old1 = cell(0, 1, 2, 3), cell(0, 1, 2, 5)
    start = {old0: F(1, 2), old1: F(1, 2)}
    first, children = refine(start, old0, 4)
    a, b = cell(0, 1, 2, 4), cell(0, 1, 3, 4)
    assert a in children and b in children

    ab, _ = refine(first, a, 6)
    ab, _ = refine(ab, b, 7)
    ba, _ = refine(first, b, 7)
    ba, _ = refine(ba, a, 6)
    assert ab == ba  # Disjoint child events commute, including zero-stock cells.
    assert sum(ab.values()) == 1
    assert sorted(v for c, v in ab.items() if VERTEX in c and c != old1) == [F(1, 18)] * 6 + [F(1, 6)]
    assert ab[old1] == F(1, 2)

    nested, _ = refine(first, a, 6)
    leaves = [c for c in nested if VERTEX in c and c != old1]
    assert len(leaves) == 5
    assert sorted(nested[c] for c in leaves) == [F(1, 18)] * 3 + [F(1, 6)] * 2
    global_parent = {c: F(1, 10) for c in leaves}
    assert sum(global_parent.values()) == F(1, 2)
    assert any(nested[c] != global_parent[c] for c in leaves)
    assert F(1, len(leaves) + 1) == F(1, 6)  # New-carrier Q177 shares, including old1.
    print("PASS: commuting disjoint diamond; nested recursive, global-parent, Q177 allocations distinct")
