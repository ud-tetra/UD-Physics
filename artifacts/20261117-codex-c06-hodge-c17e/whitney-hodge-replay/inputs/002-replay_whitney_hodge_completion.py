"""Reproduce the tetrahedral boundary Whitney Hodge correction exactly."""

from fractions import Fraction as F
from itertools import combinations
import json


def product(left, right):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*right)] for row in left]


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


def combine(left, right, coefficient=1):
    return [[a + coefficient * b for a, b in zip(row, other)]
            for row, other in zip(left, right)]


def main():
    edges = list(combinations(range(4), 2))
    faces = list(combinations(range(4), 3))
    d0 = [[int(v == j) - int(v == i) for v in range(4)] for i, j in edges]
    d1 = []
    m0 = [[F(0) for _ in range(4)] for _ in range(4)]
    m1 = [[F(0) for _ in edges] for _ in edges]
    for face in faces:
        boundary = {face[:k] + face[k + 1:]: (-1) ** k for k in range(3)}
        d1.append([boundary.get(e, 0) for e in edges])
        for a in face:
            for b in face:
                m0[a][b] += F(1 + (a == b), 12)
        for e, sign in boundary.items():
            for other, other_sign in boundary.items():
                m1[edges.index(e)][edges.index(other)] += F(6 * (e == other) - sign * other_sign, 9)
    m0_inv = [[3 * (i == j) - F(1, 2) for j in range(4)] for i in range(4)]
    assert product(m0, m0_inv) == [[int(i == j) for j in range(4)] for i in range(4)]
    assert all(not any(row) for row in product(d1, d0))
    m1d0 = product(m1, d0)
    down = product(product(m1d0, m0_inv), transpose(m1d0))
    m2 = [[F(16, 3) * (i == j) for j in range(4)] for i in range(4)]
    up = product(product(transpose(d1), m2), d1)
    cuts = product(d0, transpose(d0))
    cycles = product(transpose(d1), d1)
    assert product(m1, d0) == [[F(4, 3) * x for x in row] for row in d0]
    assert product(m1, transpose(d1)) == [[F(8, 9) * x for x in row] for row in transpose(d1)]
    assert down == [[F(16, 3) * x for x in row] for row in cuts]
    assert up == [[F(16, 3) * x for x in row] for row in cycles]
    total = combine(down, up)
    assert total == [[F(64, 3) * (i == j) for j in range(6)] for i in range(6)]
    assert combine(m1, up, F(1, 48)) == [[F(4, 3) * (i == j) for j in range(6)] for i in range(6)]
    with_full_energy = combine(m1, total)
    assert all(with_full_energy[i][j] == m1[i][j] for i in range(6) for j in range(6) if i != j)
    print(json.dumps({
        "cut_mass": "4/3", "cycle_mass": "8/9", "required_cycle_increment": "4/9",
        "down_energy": "(64/3) P_cut", "up_energy": "(64/3) P_cycle",
        "full_energy": "(64/3) I_6", "selected_up_weight": "1/48",
        "augmented_mass": "(4/3) I_6"
    }, indent=2))


if __name__ == "__main__":
    main()
