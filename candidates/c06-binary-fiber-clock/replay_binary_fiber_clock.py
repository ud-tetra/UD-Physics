"""Exact permutation, receipt, transfer, and edge overlap checks."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json


def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def permute(x, permutation):
    return tuple(x[i] for i in permutation)


def parity(x):
    return sum(x) % 2


def main():
    states = tuple(product((0, 1), repeat=3))
    relabelings = tuple(permutations(range(3)))
    index = {x: i for i, x in enumerate(states)}
    action = [tuple(index[permute(x, p)] for x in states) for p in relabelings]

    fixed = [x for x in states if all(x == permute(x, p) for p in relabelings)]
    assert fixed == [(0, 0, 0), (1, 1, 1)]
    invariant_linear = [a for a in states if a != (0, 0, 0) and
                        all(permute(a, p) == a for p in relabelings)]
    assert invariant_linear == [(1, 1, 1)]
    receipt_checks = 0
    for x, mask, p in product(states, states, relabelings):
        assert parity(xor(permute(x, p), mask)) == (parity(x) ^ parity(mask))
        receipt_checks += 1

    equivariant = [f for f in permutations(range(8))
                   if all(f[a[i]] == a[f[i]] for a in action for i in range(8))]
    assert len(equivariant) == 4
    assert all(f[f[i]] == i for f in equivariant for i in range(8))
    for f in equivariant:
        assert f[0] in (0, 7) and f[7] in (0, 7)
    translations = [mask for mask in states if
                    tuple(index[xor(x, mask)] for x in states) in equivariant]
    assert translations == fixed

    edges = tuple(combinations(range(4), 2))
    signs = [[int(v == b) - int(v == a) for a, b in edges] for v in range(4)]
    overlaps = [F(0), F(0)]
    for i, e in enumerate(edges):
        for j, h in enumerate(edges):
            cut = F(sum(row[i] * row[j] for row in signs), 4)
            cycle = int(i == j) - cut
            if not set(e) & set(h):
                assert cut == cycle == 0
            plus = F(int(i == j) + int(not set(e) & set(h)), 2)
            overlaps[0] += plus * cut
            overlaps[1] += plus * cycle
    assert overlaps == [F(3, 2), F(3, 2)]

    ratios = [1 / f for f in (F(1, 2), F(1, 4))]
    assert ratios == [2, 4]
    print(json.dumps({"fixed_states": fixed, "equivariant_bijections": len(equivariant),
                      "receipt_checks": receipt_checks, "record_gain_witnesses": list(map(str, ratios)),
                      "hodge_overlaps": list(map(str, overlaps))}, indent=2))


if __name__ == "__main__":
    main()
