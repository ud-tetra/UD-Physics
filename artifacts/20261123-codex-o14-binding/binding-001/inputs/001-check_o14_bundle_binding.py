"""Check internal metadata binding for a canonical filled-K4 O14 v0.2 bundle."""

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "experiments/o14-lc-offset-v02/LC_CALIBRATION_BUNDLE_SCHEMA_v0.2.json"
SIMPLICES = [list(s) for size in range(1, 5) for s in combinations("0123", size)]


def check_binding(bundle):
    """Check declared row and column correspondence after schema validation."""
    basis = bundle["native_basis"]
    calibration = bundle["calibration"]
    simplices = basis["simplices"]
    simplex_ids = [row["id"] for row in simplices]
    if len(set(simplex_ids)) != len(simplex_ids):
        raise ValueError("native_basis.simplices IDs must be unique")
    declared = [(row["ordered_vertices"], row["degree"]) for row in simplices]
    expected = [(vertices, len(vertices) - 1) for vertices in SIMPLICES]
    if declared != expected:
        raise ValueError("native_basis.simplices must use ascending vertices and degree-then-lexicographic row order")

    pairs = basis["modal_pairs"]
    mode_ids = [pair["mode_id"] for pair in pairs]
    if len(set(mode_ids)) != len(mode_ids):
        raise ValueError("native_basis.modal_pairs mode IDs must be unique")
    if mode_ids != [mode["mode_id"] for mode in calibration["modes"]]:
        raise ValueError("native_basis.modal_pairs mode IDs must match calibration.modes in order")

    column_ids = [pair[key] for pair in pairs for key in ("u_id", "v_id")]
    if len(set(column_ids)) != len(column_ids):
        raise ValueError("native_basis.modal_pairs quadrature IDs must be unique")
    if column_ids != calibration["output_ids"]:
        raise ValueError("calibration.output_ids must match the ordered (u_id, v_id) basis columns")

    for selector, degree in (("vertex_selector", 0), ("edge_selector", 1)):
        selected_rows = [i for i, row in enumerate(simplices) if row["degree"] == degree]
        expected_selector = [
            [int(column == i) for column in range(len(simplices))] for i in selected_rows
        ]
        if basis[selector] != expected_selector:
            raise ValueError(f"native_basis.{selector} must select its simplex rows in declared order")


def reject_nonfinite(token):
    raise ValueError(f"Nonfinite JSON number: {token}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    try:
        bundle = json.loads(args.bundle.read_text(), parse_float=Fraction,
                            parse_constant=reject_nonfinite)
        Draft202012Validator(json.loads(SCHEMA.read_text())).validate(bundle)
        check_binding(bundle)
    except ValidationError as error:
        parser.exit(1, f"{error.json_path}: {error.message}\n")
    except (ValueError, OSError, OverflowError) as error:
        parser.exit(1, f"{error}\n")
    print("PASS: canonical simplex and selector rows, ordered modal and output IDs")


if __name__ == "__main__":
    main()
