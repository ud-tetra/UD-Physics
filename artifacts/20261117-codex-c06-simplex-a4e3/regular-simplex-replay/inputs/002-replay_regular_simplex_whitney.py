"""Replay the regular simplex Whitney mass law with exact barycentric moments."""

from fractions import Fraction as F
from itertools import combinations
import json


def check(dimension, side_squared):
    n = dimension + 1
    edges = list(combinations(range(n), 2))

    def gradient_gram(i, j):
        return (2 / side_squared) * (int(i == j) - F(1, n))

    def moment(i, j):
        return F(1 + (i == j), n * (n + 1))

    cut_mass = 2 / (n * side_squared)
    cycle_mass = 4 / (n * (n + 1) * side_squared)
    gyration_weight = side_squared / (4 * n * (n + 1))
    for i, j in edges:
        for k, l in edges:
            same_edge = int((i, j) == (k, l))
            cut = F(int(j == l) - int(j == k) - int(i == l) + int(i == k), n)
            cycle = same_edge - cut
            curl = 4 * (gradient_gram(i, k) * gradient_gram(j, l)
                        - gradient_gram(i, l) * gradient_gram(j, k))
            mass = (moment(i, k) * gradient_gram(j, l) - moment(i, l) * gradient_gram(j, k)
                    - moment(j, k) * gradient_gram(i, l) + moment(j, l) * gradient_gram(i, k))
            assert curl == (16 / side_squared**2) * cycle
            assert mass == cut_mass * cut + cycle_mass * cycle
            assert mass + F(dimension, 2) * gyration_weight * curl == cut_mass * same_edge
    return {"dimension": dimension, "side_squared": str(side_squared),
            "cut_mass": str(cut_mass), "cycle_mass": str(cycle_mass),
            "added_copies": str(F(dimension, 2))}


if __name__ == "__main__":
    print(json.dumps([check(d, side) for d in range(2, 8) for side in (F(1), F(9, 4))], indent=2))
