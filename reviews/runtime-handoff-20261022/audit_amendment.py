#!/usr/bin/env python3
"""Check the coordinator amendment without changing original v1 evidence."""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH = ROOT / ".tmp" / "coordinator-patch"
REVISION = "e5c1a4edbb3e3aec62b8c5dde843031c17ae123a"
sys.path.insert(0, str(PATCH / "scripts"))
from discovery import Store
from validate import validate


def main():
    assert subprocess.check_output(["git", "-C", str(PATCH), "rev-parse", "HEAD"], text=True).strip() == REVISION
    results = {"amendment_revision": REVISION, "checks": [], "probes": [], "original_evidence": "baseline-audit-v1 remains immutable; these are new checks on the amendment"}
    for command in ([sys.executable, "scripts/validate.py"], [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]):
        p = subprocess.run(command, cwd=PATCH, capture_output=True, text=True)
        assert p.returncode == 0, p.stderr
        results["checks"].append({"command": command, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr})
    legacy_errors = validate(ROOT / ".tmp" / "writer-frozen")[1]
    assert not legacy_errors, legacy_errors
    results["legacy_frozen_writer_validation_errors"] = legacy_errors
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp); store = Store(root)
        store.bootstrap("reviewer amendment probe", "probe", "Verify amended provenance", "probe-session")
        inputs = [root / "a/input.json", root / "b/input.json"]
        for i,p in enumerate(inputs):
            p.parent.mkdir(); p.write_text(str(i))
        output = root / "output.json"; output.write_text("3")
        folder = store.capture("probe-session", "probe", "OPEN", "input ambiguity probe", "NOT_EXECUTED", inputs, [output])
        path = folder / "manifest.json"; manifest = json.loads(path.read_text())
        assert manifest["schema_version"] == 2
        assert [x["source_path"] for x in manifest["inputs"]] == ["a/input.json", "b/input.json"]
        assert len({x["input_id"] for x in manifest["inputs"]}) == 2
        assert not validate(root)[1]
        results["probes"].append({"name": "same_named_inputs", "result": "PASS", "manifest_inputs": manifest["inputs"]})
        bad = copy.deepcopy(manifest); bad["inputs"] = "not an array"; path.write_text(json.dumps(bad))
        errors = validate(root)[1]; assert any("inputs must be an array" in x for x in errors)
        results["probes"].append({"name": "malformed_metadata", "result": "PASS", "errors": errors})
        path.write_text(json.dumps(manifest)); (folder / manifest["inputs"][0]["path"]).write_text("tampered")
        errors = validate(root)[1]; assert any("digest/size mismatch" in x for x in errors)
        results["probes"].append({"name": "input_tampering", "result": "PASS", "errors": errors})
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
