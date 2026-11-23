"""Check a filled-K4 basis in ascending simplex and signed (u, v) order."""

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import sqrt
from pathlib import Path

SIMPLICES = tuple(s for size in range(1, 5) for s in combinations(range(4), size))
TOLERANCE = Fraction("1e-12")


def basis_defects_squared(basis):
    """Return exact squared Frobenius defects for Gram, kernel and generator."""
    if len(basis) != 15 or any(len(row) != 14 for row in basis):
        raise ValueError("Expected a 15-by-14 basis")
    if not all(type(value) in (int, float, Fraction) for row in basis for value in row):
        raise ValueError("Basis entries must be numbers")
    rows = [[Fraction(value) for value in row] for row in basis]
    columns = list(zip(*rows))
    index = {simplex: i for i, simplex in enumerate(SIMPLICES)}
    au = [[Fraction(0) for _ in columns] for _ in SIMPLICES]
    for j, simplex in enumerate(SIMPLICES):
        if len(simplex) == 1:
            continue
        for k in range(len(simplex)):
            i = index[simplex[:k] + simplex[k + 1:]]
            sign = (-1) ** k
            for c in range(len(columns)):
                au[i][c] += sign * rows[j][c]
                au[j][c] -= sign * rows[i][c]

    gram = sum(
        (sum(x * y for x, y in zip(u, v)) - (i == j)) ** 2
        for i, u in enumerate(columns) for j, v in enumerate(columns)
    )
    kernel = sum((sum(column[:4]) / 2) ** 2 for column in columns)
    signed = 0
    for i, u in enumerate(columns):
        partner = i + 1 if i % 2 == 0 else i - 1
        for j, av in enumerate(zip(*au)):
            expected = 0
            if j == partner:
                expected = -2 if i % 2 == 0 else 2
            signed += (sum(x * y for x, y in zip(u, av)) - expected) ** 2
    return gram, kernel, signed


def reject_nonfinite(token):
    raise ValueError(f"Nonfinite JSON number: {token}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=Path, help="Reference fixture or O14 bundle JSON")
    args = parser.parse_args()
    try:
        record = json.loads(args.basis.read_text(), parse_float=Fraction,
                            parse_constant=reject_nonfinite)
        native = record.get("native_basis", record)
        labels = native["simplices"]
        if "native_basis" in record:
            expected = [([str(v) for v in s], len(s) - 1) for s in SIMPLICES]
            declared = [(s["ordered_vertices"], s["degree"]) for s in labels]
        else:
            expected = [list(s) for s in SIMPLICES]
            declared = labels
        if declared != expected:
            raise ValueError("Expected canonical ascending simplex row order on vertices 0–3")
        defects = basis_defects_squared(native["modal_to_full_chain_basis"])
    except (OSError, AttributeError, KeyError, TypeError, ValueError, OverflowError) as error:
        parser.exit(1, f"Invalid basis input: {error}\n")

    passed = True
    for label, squared in zip(("Gram", "harmonic overlap", "signed generator"), defects):
        valid = squared < TOLERANCE ** 2
        passed &= valid
        try:
            display = f"{sqrt(float(squared)):.8g}"
        except OverflowError:
            display = "too large to display as a float"
        print(f"{'PASS' if valid else 'FAIL'} {label}: {display}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
