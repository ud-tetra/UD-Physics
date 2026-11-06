"""Check completeness and score the measured loopback arithmetic only."""
from dataclasses import fields
from fractions import Fraction
import json
from pathlib import Path
import sys

from bench_reference import ChannelBounds, evaluate


def score(record):
    required = ("capture_manifest", "calibration_receipt", "operating_envelope",
                "phasor_unit", "time_unit", "gap_floor_rad", "target_rad")
    channels = record.get("channels", {})
    bound_names = [field.name for field in fields(ChannelBounds)]
    missing = [name for name in required if not record.get(name)]
    for label in ("axis", "diagonal"):
        row = channels.get(label, {})
        missing.extend(f"{label}.{name}" for name in bound_names if row.get(name) is None)
    if missing:
        return {"status": "UNSCORED", "missing": missing}

    def fraction(value):
        if not isinstance(value, str):
            raise ValueError("Enter exact decimal or rational strings")
        return Fraction(value)

    bounds = [ChannelBounds(**{name: fraction(channels[label][name]) for name in bound_names})
              for label in ("axis", "diagonal")]
    result = evaluate(fraction(record["gap_floor_rad"]), fraction(record["target_rad"]), bounds)
    return {"status": "ARITHMETIC_ONLY", **result}


if __name__ == "__main__":
    print(json.dumps(score(json.loads(Path(sys.argv[1]).read_text())), indent=2))
