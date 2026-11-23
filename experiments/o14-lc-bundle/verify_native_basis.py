"""Build or verify the exact reference basis for the filled tetrahedron."""

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


REFERENCE = Path(__file__).with_name("K4_NATIVE_BASIS_U_REFERENCE_v0.1.json")


def reference():
    simplices = [s for size in range(1, 5) for s in combinations(range(4), size)]
    index = {simplex: i for i, simplex in enumerate(simplices)}
    n = len(simplices)
    boundary = [[0] * n for _ in simplices]
    for j, simplex in enumerate(simplices):
        if len(simplex) == 1:
            continue
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k + 1:]
            boundary[index[face]][j] = (-1) ** k
    assert all(sum(boundary[i][k] * boundary[k][j] for k in range(n)) == 0
               for i in range(n) for j in range(n))

    a = [[boundary[i][j] - boundary[j][i] for j in range(n)] for i in range(n)]
    seeds = [j for j, simplex in enumerate(simplices) if len(simplex) % 2 == 0]
    columns = []
    for seed in seeds:
        columns.append([int(i == seed) for i in range(n)])
        columns.append([Fraction(a[i][seed], 2) for i in range(n)])

    for i, col in enumerate(columns):
        for j, other in enumerate(columns):
            assert sum(x*y for x, y in zip(col, other)) == int(i == j)
    for i in range(n):
        for j in range(n):
            assert sum(col[i] * col[j] for col in columns) == (
                int(i == j) - (Fraction(1, 4) if i < 4 and j < 4 else 0)
            )
    for j in range(0, len(columns), 2):
        for row, u, v in zip(a, columns[j], columns[j+1]):
            assert sum(x*y for x, y in zip(row, columns[j])) == 2*v
            assert sum(x*y for x, y in zip(row, columns[j+1])) == -2*u

    return {
        "reference_version": "0.1",
        "carrier": "filled K4 on vertices 0, 1, 2, 3",
        "metric": "Euclidean coefficient inner product",
        "orientation": "ascending vertices, rows sorted by degree then lexicographically",
        "column_convention": "ordered pairs (e_j, A e_j / 2) for lexicographic edges then tetrahedron",
        "physical_promotion": 0,
        "simplices": [list(simplex) for simplex in simplices],
        "seed_simplices": [list(simplices[j]) for j in seeds],
        "modal_to_full_chain_basis": [
            [int(x) if x == int(x) else float(x) for x in row]
            for row in zip(*columns)
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the reproducible JSON reference")
    args = parser.parse_args()
    fixture = reference()
    if args.write:
        REFERENCE.write_text(json.dumps(fixture, indent=2) + "\n")
    elif json.loads(REFERENCE.read_text()) != fixture:
        parser.exit(1, "Reference fixture differs from exact reconstruction\n")
    print("PASS: exact K4 boundary, 14 orthonormal columns, harmonic complement, seven rotation blocks")


if __name__ == "__main__":
    main()
