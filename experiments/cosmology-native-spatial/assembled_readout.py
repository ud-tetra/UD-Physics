"""Exact assembled-tetra cell-support filtration; no physical embedding."""
from itertools import combinations, permutations
from fractions import Fraction


def supports(cells, amplitudes):
    """Q177/Q178 ownership of squared simplex amplitudes by incident top cells."""
    cells = tuple(frozenset(c) for c in cells)
    assert all(len(c) == 4 for c in cells) and len(set(cells)) == len(cells)
    owners = {}
    for c in cells:
        for k in range(1, 5):
            for face in combinations(sorted(c), k):
                owners.setdefault(frozenset(face), set()).add(c)
    assert set(amplitudes).issubset(owners)
    return {c: sum((Fraction(v * v, len(owners[s]))
                    for s, v in amplitudes.items() if c in owners[s]), Fraction(0))
            for c in cells}


def beta0(cells, weights, threshold, shared=3):
    selected = {c for c in cells if weights[c] <= threshold}
    count = 0
    while selected:
        count += 1
        frontier = [selected.pop()]
        while frontier:
            c = frontier.pop()
            neighbors = {d for d in selected if len(c & d) >= shared}
            selected -= neighbors
            frontier.extend(neighbors)
    return count


if __name__ == "__main__":
    raw = ((0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 4, 5))
    cells = tuple(frozenset(c) for c in raw)
    amps = {cells[0]: 1, cells[1]: 3, cells[2]: 2}
    w = supports(cells, amps)
    assert [w[c] for c in cells] == [1, 9, 4]
    assert [beta0(cells, w, t) for t in (0, 1, 4, 9)] == [0, 1, 2, 1]
    assert beta0(cells, w, 4, shared=2) == 1  # Changed adjacency convention.

    for p in permutations(range(6)):
        tr = lambda c: frozenset(p[v] for v in c)
        moved = tuple(tr(c) for c in cells)
        mw = supports(moved, {tr(c): v for c, v in amps.items()})
        assert [beta0(moved, mw, t) for t in (0, 1, 4, 9)] == [0, 1, 2, 1]
        assert sorted(mw.values()) == sorted(w.values())

    old = (frozenset((0, 1, 2, 3)),)
    new = tuple(frozenset((4,)) | frozenset(f) for f in combinations((0, 1, 2, 3), 3))
    assert sum(supports(old, {old[0]: 1}).values()) == 1
    assert sum(supports(new, {c: 1 for c in new}).values()) == 4
    print("PASS: 720 relabelings, filtration, adjacency and 1-to-4 stock control")
