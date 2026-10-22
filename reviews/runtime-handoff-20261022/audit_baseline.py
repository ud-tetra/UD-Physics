#!/usr/bin/env python3
"""Reproduce reviewer baseline checks and narrowly scoped provenance probes."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from discovery import Store
from validate import validate


def main():
    results = {"base_revision": "fbf40e3f4daaf3f02af5db35fc1ee82f0da02190", "checks": [], "probes": []}
    for command in ([sys.executable, "scripts/validate.py"], [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]):
        p = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        results["checks"].append({"command": command, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr})
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = Store(root)
        store.bootstrap("reviewer probe", "probe", "Provenance input validation", "probe-session")
        first, second, output = root / "a" / "input.json", root / "b" / "input.json", root / "output.json"
        first.parent.mkdir(); second.parent.mkdir()
        first.write_text('{"input": 1}\n'); second.write_text('{"input": 2}\n'); output.write_text('{"result": 3}\n')
        folder = store.capture("probe-session", "probe", "OPEN", "Probe only", "NOT_EXECUTED", [first, second], [output])
        manifest_path = folder / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        results["probes"].append({"name": "duplicate_input_basenames", "inputs": manifest["inputs"], "validation_errors": validate(root)[1], "observed": "Distinct inputs have identical manifest names; hashes distinguish bytes but source paths are absent."})
        manifest["inputs"] = "invalid metadata replacing the input array"
        manifest_path.write_text(json.dumps(manifest))
        results["probes"].append({"name": "malformed_input_metadata", "validation_errors": validate(root)[1], "observed": "Validator accepts a run whose inputs value is a string rather than an input record list."})
    print(json.dumps(results, indent=2))
    return int(any(check["exit_code"] for check in results["checks"]))


if __name__ == "__main__":
    raise SystemExit(main())
