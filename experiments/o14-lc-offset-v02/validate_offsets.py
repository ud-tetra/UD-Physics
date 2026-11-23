"""Check O14 v0.2 offsets, input-axis dimensions and native-basis orthonormality."""

import argparse
import json
from math import fsum, hypot, isfinite
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError


SCHEMA = Path(__file__).with_name("LC_CALIBRATION_BUNDLE_SCHEMA_v0.2.json")


def check_dimensions(calibration):
    input_count = len(calibration["input_ids"])
    expected_offset = input_count if calibration["offset_space"] == "channel" else 14
    if len(calibration["offset"]) != expected_offset:
        raise ValueError(f"Expected {expected_offset} {calibration['offset_space']} offsets")
    for row in calibration["readout_to_modal"]:
        if len(row) != input_count:
            raise ValueError(f"Each readout_to_modal row must have {input_count} input columns")


ORTHONORMALITY_TOLERANCE = 1e-12


def check_basis_orthonormality(basis):
    """Check the Gram matrix of the 15-by-14 basis after schema validation."""
    try:
        if not all(isfinite(value) for row in basis for value in row):
            raise ValueError("Native basis must contain only finite numbers")
        columns = list(zip(*basis))
        defect = hypot(*(
            fsum(x * y for x, y in zip(left, right)) - (i == j)
            for i, left in enumerate(columns)
            for j, right in enumerate(columns)
        ))
    except (OverflowError, ValueError) as error:
        raise ValueError(f"Cannot evaluate finite native-basis Gram matrix: {error}") from error
    if not defect < ORTHONORMALITY_TOLERANCE:
        raise ValueError(
            f"Native basis must satisfy ||U^T U - I||_F < {ORTHONORMALITY_TOLERANCE:g}"
            f" (got {defect:.6g})"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA.read_text())
    try:
        bundle = json.loads(args.bundle.read_text())
        Draft202012Validator(schema).validate(bundle)
        check_dimensions(bundle["calibration"])
        check_basis_orthonormality(bundle["native_basis"]["modal_to_full_chain_basis"])
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    except ValidationError as error:
        parser.exit(1, f"{error.json_path}: {error.message}\n")
    print("PASS: schema, offset dimensions and native-basis orthonormality")


if __name__ == "__main__":
    main()
