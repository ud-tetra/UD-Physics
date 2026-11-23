"""Check O14 v0.2 offset-space and input-axis dimensions."""

import argparse
import json
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA.read_text())
    try:
        bundle = json.loads(args.bundle.read_text())
        Draft202012Validator(schema).validate(bundle)
        check_dimensions(bundle["calibration"])
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    except ValidationError as error:
        parser.exit(1, f"{error.json_path}: {error.message}\n")
    print("PASS: schema and offset dimensions")


if __name__ == "__main__":
    main()
