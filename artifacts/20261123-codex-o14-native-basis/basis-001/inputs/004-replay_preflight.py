"""Exercise the normal CLI on synthetic bundles with controlled native bases."""

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS = ROOT / "experiments"
CHECKER = EXPERIMENTS / "o14-lc-offset-v02" / "validate_offsets.py"
REFERENCE = EXPERIMENTS / "o14-lc-bundle" / "K4_NATIVE_BASIS_U_REFERENCE_v0.1.json"


def main():
    schema = json.loads(CHECKER.with_name("LC_CALIBRATION_BUNDLE_SCHEMA_v0.2.json").read_text())
    fixture = json.loads(REFERENCE.read_text())

    def placeholder(rule):
        if "$ref" in rule:
            return placeholder(schema["$defs"][rule["$ref"].split("/")[-1]])
        if "const" in rule:
            return rule["const"]
        if "enum" in rule:
            return rule["enum"][0]
        if rule["type"] == "object":
            return {key: placeholder(rule["properties"][key]) for key in rule["required"]}
        if rule["type"] == "array":
            return [placeholder(rule["items"]) for _ in range(rule.get("minItems", 1))]
        if rule["type"] == "string":
            return "0" * (40 if rule.get("pattern") == "^[a-f0-9]{40}$" else 64)
        return 1

    bundle = placeholder(schema)
    calibration = bundle["calibration"]
    calibration["input_ids"] = [f"input-{i}" for i in range(14)]
    calibration["readout_to_modal"] = [[0] * 14 for _ in range(14)]
    basis = fixture["modal_to_full_chain_basis"]
    cases = [
        ("exact reference", basis, 0),
        ("alternate orthonormal columns", [row[::-1] for row in basis], 0),
        ("subthreshold Gram defect", [[(1 + 1e-13)*row[0], *row[1:]] for row in basis], 0),
        ("above-threshold Gram defect", [[(1 + 1e-10)*row[0], *row[1:]] for row in basis], 1),
        ("duplicate columns", [[row[1], *row[1:]] for row in basis], 1),
    ]
    nonfinite = deepcopy(basis)
    nonfinite[0][0] = float("nan")
    cases.append(("nonfinite entry", nonfinite, 1))

    with TemporaryDirectory() as directory:
        path = Path(directory) / "bundle.json"
        for label, matrix, expected in cases:
            bundle["native_basis"]["modal_to_full_chain_basis"] = matrix
            path.write_text(json.dumps(bundle) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(path)],
                                    capture_output=True, text=True)
            assert result.returncode == expected, (label, result)
            if expected:
                assert "native-basis Gram" in result.stderr or "||U^T U" in result.stderr, result.stderr
            print(f"PASS: {label}, preflight exit {expected}")


if __name__ == "__main__":
    main()
