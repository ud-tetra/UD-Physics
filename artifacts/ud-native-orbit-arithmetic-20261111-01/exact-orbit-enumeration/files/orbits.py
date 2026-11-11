"""Target-blind exact K4 opposite-edge parity orbit enumeration."""

from itertools import combinations, permutations, product
from math import comb


VERTICES = tuple(range(4))
MATCHINGS = tuple(dict.fromkeys(
    frozenset((frozenset(e), frozenset(set(VERTICES) - set(e))))
    for e in combinations(VERTICES, 2)
))
THETA = tuple(product((0, 1), repeat=3))


def parity(p):
    return sum(p[i] > p[j] for i in VERTICES for j in VERTICES if i < j) % 2


def pair_map(p):
    return tuple(MATCHINGS.index(frozenset(
        frozenset(p[v] for v in edge) for edge in m)) for m in MATCHINGS)


def act(p, x):
    q = pair_map(p)
    return tuple(x[q.index(i)] for i in range(3))


def run():
    assert len(MATCHINGS) == 3 and len(THETA) == 8
    s4 = tuple(permutations(VERTICES))
    a4 = tuple(p for p in s4 if parity(p) == 0)
    assert len(s4) == 24 and len(a4) == 12
    for name, group in (("S4", s4), ("A4", a4)):
        relation = {(x, act(p, x)) for x in THETA for p in group}
        expected = {(x, y) for x in THETA for y in THETA
                    if sum(x) == sum(y)}
        assert relation == expected
        orbit_sizes = tuple(sorted({len({act(p, x) for p in group})
                                    for x in THETA if sum(x) == k})[0]
                            for k in range(4))
        assert orbit_sizes == (1, 3, 3, 1)
        assert len(relation) == sum(comb(3, k)**2 for k in range(4)) == 20
        print(f"{name}: {len(group)} permutations, 8 fiber states, "
              f"orbit sizes {orbit_sizes}, {len(relation)}/64 related ordered pairs")
    assert len({pair_map(p) for p in s4}) == 6
    assert len({pair_map(p) for p in a4}) == 3
    print("negative control: (000, 001) is not a relabeling pair")
    assert not any(act(p, (0, 0, 0)) == (0, 0, 1) for p in s4)


if __name__ == "__main__":
    run()
