"""Exact local 1-to-4 ownership obstruction and conditional ancestry receipt."""
from fractions import Fraction as F
from itertools import combinations

from assembled_readout import supports


def ancestry_allocation(old_cells, new_children, unchanged, simplex):
    """Assumed parent shares, evenly divided among descendants containing simplex."""
    old_owners = [c for c in old_cells if simplex <= c]
    assert old_owners
    parent_share = F(1, len(old_owners))
    allocation = {}
    for parent in old_owners:
        descendants = new_children if parent == old_cells[0] else (unchanged,)
        incident = [c for c in descendants if simplex <= c]
        assert incident
        for c in incident:
            allocation[c] = parent_share / len(incident)
    return allocation


if __name__ == "__main__":
    t0 = frozenset((0, 1, 2, 3))
    t1 = frozenset((0, 1, 2, 5))
    old = (t0, t1)
    children = tuple(frozenset((4,)) | frozenset(f)
                     for f in combinations((0, 1, 2, 3), 3))
    new = children + (t1,)
    vertex = frozenset((0,))
    ow = supports(old, {vertex: 1})
    nw = supports(new, {vertex: 1})
    assert (ow[t0], ow[t1]) == (F(1, 2), F(1, 2))
    assert sorted(nw[c] for c in children) == [F(0), F(1, 4), F(1, 4), F(1, 4)]
    assert nw[t1] == F(1, 4)
    assert sum(nw[c] for c in children) == F(3, 4)
    assert sum(ow.values()) == sum(nw.values()) == 1

    allocation = ancestry_allocation(old, children, t1, vertex)
    assert sorted(allocation[c] for c in children if c in allocation) == [F(1, 6)] * 3
    assert allocation[t1] == F(1, 2)
    assert sum(allocation.values()) == 1

    # Source top fundamental chain maps one coefficient to four unit coefficients.
    # An isometric diagonal top weight requires 1/4; old face registers retain 1.
    top_weight, face_weight, incidence = F(1, 4), F(1), F(1)
    skew_defect = incidence * (face_weight - top_weight)
    assert skew_defect == F(3, 4)  # (H A + A^T H)_face,top, up to orientation.
    print("PASS: Q177 parent shares 1/2,1/2 -> 3/4,1/4; ancestry 1/2,1/2; skew defect 3/4")
