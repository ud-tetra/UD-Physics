"""Presence gate for a prospective certificate; never certifies scientific truth."""
import json
from pathlib import Path
import sys


def main(path):
    x = json.loads(Path(path).read_text())
    required = [k for k in x if k not in ("schema_version", "status", "native_carrier", "physical_model", "physical_promotion")]
    missing = [k for k in required if x[k] is None]
    result = {"status": "BLOCKED_MISSING_INPUTS" if missing else "PRESENCE_ONLY_REVIEW_REQUIRED",
              "missing": missing, "count": len(missing),
              "scientific_calibration_verified": False, "empirical_score": "UNSCORED", "physical_promotion": 0}
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main(sys.argv[1])
