"""Exact Whitney face mass and edge pullback on a regular tetrahedron."""

from fractions import Fraction as F
from itertools import combinations
import json


def main():
    edges = list(combinations(range(4), 2))
    faces = list(combinations(range(4), 3))
    local_edges = list(combinations(range(3), 2))
    # The vertices of the embedded reference triangle are e_i / sqrt(2).
    # Work with covectors in units of sqrt(2) to keep the plane Gram rational.
    gradients = [[F(int(i == j)) - F(1, 3) for j in range(3)] for i in range(3)]
    local = [[F(0) for _ in local_edges] for _ in local_edges]
    for sample in range(3):
        bary = [F(2, 3) if i == sample else F(1, 6) for i in range(3)]
        coframe = [[bary[i] * xj - bary[j] * xi
                    for xi, xj in zip(gradients[i], gradients[j])] for i, j in local_edges]
        for i, left in enumerate(coframe):
            for j, right in enumerate(coframe):
                local[i][j] += F(2, 3) * sum(x * y for x, y in zip(left, right))

    signs = (1, -1, 1)
    assert local == [[F(6 * (i == j) - signs[i] * signs[j], 9)
                      for j in range(3)] for i in range(3)]
    pullback = [[F(0) for _ in edges] for _ in edges]
    curl = [[0 for _ in edges] for _ in edges]
    div = []
    for a, b in edges:
        div.append([int(v == b) - int(v == a) for v in range(4)])
    for face in faces:
        indices = [edges.index((face[i], face[j])) for i, j in local_edges]
        for i, e in enumerate(indices):
            for j, other in enumerate(indices):
                pullback[e][other] += local[i][j]
                curl[e][other] += signs[i] * signs[j]
    for i in range(6):
        for j in range(6):
            assert pullback[i][j] == F(12 * (i == j) - curl[i][j], 9)
            assert curl[i][j] + sum(x * y for x, y in zip(div[i], div[j])) == 4 * (i == j)
            assert sum(curl[i][k] * curl[k][j] for k in range(6)) == 4 * curl[i][j]
    rank = sum(curl[i][i] for i in range(6)) // 4
    assert rank == 3
    print(json.dumps({
        "face_block": [[str(x) for x in row] for row in local],
        "flag_spectrum": {"1/3": 4, "2/3": 8},
        "edge_spectrum": {"4/3": 6 - rank, "8/9": rank},
        "edge_matrix_scalar": False,
    }, indent=2))


if __name__ == "__main__":
    main()
