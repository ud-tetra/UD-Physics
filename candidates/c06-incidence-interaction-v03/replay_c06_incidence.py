"""Exact C06 Gram and AW5 edge-Laplacian replay, using only the standard library."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def multiply(left, right):
    return [[sum(a * b for a, b in zip(row, col)) for col in transpose(right)] for row in left]


def gram(matrix):
    return multiply(transpose(matrix), matrix)


def identity(n, scale=1):
    return [[scale if i == j else 0 for j in range(n)] for i in range(n)]


def incidence(lower, upper):
    matrix = [[0 for _ in upper] for _ in lower]
    indices = {simplex: i for i, simplex in enumerate(lower)}
    for col, simplex in enumerate(upper):
        for k in range(len(simplex)):
            matrix[indices[simplex[:k] + simplex[k + 1:]]][col] = (-1) ** k
    return matrix


def edge_data(cells):
    vertices, edges, faces = [
        sorted({simplex for cell in cells for simplex in combinations(cell, size)})
        for size in (1, 2, 3)
    ]
    b1, b2 = incidence(vertices, edges), incidence(edges, faces)
    assert all(not any(row) for row in multiply(b1, b2))
    div, curl = gram(b1), gram(transpose(b2))
    lap = [[a + b for a, b in zip(dr, cr)] for dr, cr in zip(div, curl)]
    return vertices, edges, faces, b2, lap


def check_flags(edges, faces, b2, lap):
    flags = [(e, f) for e in range(len(edges)) for f in range(len(faces)) if b2[e][f]]
    sampling = [[int(i == e) for i in range(len(edges))] for e, _ in flags]
    assert gram(sampling) == identity(6, 2)
    # Use 2K = F(2I - SS^T) to keep all entries integral.
    duplicate = multiply(sampling, transpose(sampling))
    complement_twice = [[2 * (i == j) - value for j, value in enumerate(row)]
                        for i, row in enumerate(duplicate)]
    face_sum = [[b2[e][f] if f == face else 0 for e, f in flags]
                for face in range(len(faces))]
    assert multiply(face_sum, sampling) == transpose(b2)
    k_twice = multiply(face_sum, complement_twice)
    assert all(not any(row) for row in multiply(k_twice, sampling))
    flag_metric = [[2 * (i == j) + Fraction(value, 4) for j, value in enumerate(row)]
                   for i, row in enumerate(gram(k_twice))]
    assert multiply(transpose(sampling), multiply(flag_metric, sampling)) == lap
    for i, (e, f) in enumerate(flags):
        for j, (e_other, f_other) in enumerate(flags):
            if f == f_other and e != e_other:
                assert flag_metric[i][j] == Fraction(b2[e][f] * b2[e_other][f], 4)


def check_shear():
    # Basis diag(1,-1,0), diag(1,1,-2), and three symmetric off-diagonal pairs.
    diagonals = [(1, -1, 0), (1, 1, -2)]
    pairs = list(combinations(range(3), 2))
    axes = [[q[i] for q in diagonals] + [0] * 3 for i in range(3)]
    edge_readout = [
        [Fraction(q[i] + q[j], 2) for q in diagonals] +
        [sign if (i, j) == pair else 0 for pair in pairs]
        for i, j in pairs for sign in (-1, 1)
    ]
    edge_gram, axis_gram = gram(edge_readout), gram(axes)
    norm = [2, 6, 2, 2, 2]
    assert [Fraction(edge_gram[i][i], norm[i]) for i in range(5)] == [
        Fraction(1, 2), Fraction(1, 2), 1, 1, 1
    ]
    for i in range(5):
        for j in range(5):
            assert 2 * edge_gram[i][j] + axis_gram[i][j] == 2 * norm[i] * (i == j)


def main():
    hub = (0, 1, 2, 3)
    leaves = [tuple(sorted((set(hub) - {i}) | {4 + i})) for i in hub]
    _, edges, faces, b2, lap = edge_data([hub])
    assert lap == identity(6, 4)
    check_flags(edges, faces, b2, lap)
    check_shear()
    filled = edge_data([hub, *leaves])
    hollow = edge_data(leaves)
    assert filled == hollow
    vertices, edges, faces, _, lap = filled
    assert (len(vertices), len(edges), len(faces)) == (8, 18, 16)
    diagonals = Counter(lap[i][i] for i in range(len(edges)))
    assert diagonals == {6: 6, 4: 12}
    missing = 0
    for i, j in combinations(range(len(edges)), 2):
        a, b = set(edges[i]), set(edges[j])
        is_unfilled_wedge = len(a & b) == 1 and tuple(sorted(a | b)) not in faces
        assert abs(lap[i][j]) == int(is_unfilled_wedge)
        missing += int(is_unfilled_wedge)
    assert missing == 24
    assert lap[edges.index((0, 1))][edges.index((0, 5))] == 1
    print(json.dumps({
        "tetrahedron_edge_form": "4I_6",
        "nonunique_flag_metric_within_face_entries": ["-1/4", "1/4"],
        "conditional_equal_unit_gain_shear": "2I_5",
        "aw5_filled_hollow_edge_forms_equal": True,
        "aw5_diagonal_multiplicities": dict(sorted(diagonals.items())),
        "aw5_uncancelled_unordered_wedges": missing,
        "aw5_nonzero_off_diagonal_entries": 2 * missing,
    }, indent=2))


if __name__ == "__main__":
    main()
