"""Exact endpoint multiplicities under a supplied net Hamming polarity."""

from collections import Counter
from itertools import product
from math import comb


def run():
    states = tuple(product((0, 1), repeat=3))
    grouped = {mu: tuple((a, b) for a in states for b in states
                         if sum(b) - sum(a) == mu) for mu in range(-3, 4)}
    counts = {mu: len(pairs) for mu, pairs in grouped.items()}
    assert counts == {mu: comb(6, 3 + mu) for mu in range(-3, 4)}
    assert sum(counts.values()) == 64
    assert {b for a, b in grouped[0] if a == (1, 0, 0)} == {
        (1, 0, 0), (0, 1, 0), (0, 0, 1)}
    assert {b for a, b in grouped[1] if a == (0, 0, 0)} == {
        (1, 0, 0), (0, 1, 0), (0, 0, 1)}
    multiplicities = Counter(len([b for a, b in grouped[mu] if a == x])
                             for mu in range(-3, 4) for x in states)
    print('mu pair counts:', counts)
    print('per-state candidate multiplicities:', dict(sorted(multiplicities.items())))
    print('witness: 100 with mu=0 has 100,010,001; no unique endpoint')


if __name__ == '__main__':
    run()
