#!/usr/bin/env python3
"""Audit the coordinator-supplied frozen writer revision in this reviewer's worktree."""
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WRITER = ROOT / ".tmp" / "writer-frozen"
FROZEN = "846a6a31c3ca87277afa584e6e4d782ef40e9168"
SOURCE = "80b8548edf5b19f876a61c478d3240c91ad0d873"
BASE = "fbf40e3f4daaf3f02af5db35fc1ee82f0da02190"


def main():
    assert subprocess.check_output(["git", "-C", str(WRITER), "rev-parse", "HEAD"], text=True).strip() == FROZEN
    checks = []
    command = [sys.executable, "experiments/clock-map-smoke/clock_map.py", "--fixture", "experiments/clock-map-smoke/fixture.json"]
    p = subprocess.run(command, cwd=WRITER, capture_output=True)
    assert p.returncode == 0, p.stderr
    artifact = WRITER / "artifacts/handoff-writer-20261022-a1/affine-fit-001/files/handoff-writer-20261022-a1-result.json"
    assert p.stdout == artifact.read_bytes()
    output = json.loads(p.stdout)
    assert output["affine"]["offset_ns"] == "1" and output["affine"]["scale_ns_per_tick"] == "2"
    for split in ("training", "evaluation_exposed"):
        assert output["affine"][split]["sse_ns2"] == "0"
    assert output["constant_baseline"]["level_ns"] == "3"
    assert output["constant_baseline"]["training"]["sse_ns2"] == "8"
    assert output["constant_baseline"]["evaluation_exposed"]["sse_ns2"] == "52"
    manifest = json.loads((artifact.parent.parent / "manifest.json").read_text())
    assert manifest["source"] == {"revision": SOURCE, "dirty": False}
    inputs = []
    for entry in manifest["inputs"]:
        path = "experiments/clock-map-smoke/" + entry["name"]
        data = (WRITER / path).read_bytes()
        original = subprocess.check_output(["git", "-C", str(WRITER), "show", SOURCE + ":" + path])
        assert data == original and hashlib.sha256(data).hexdigest() == entry["sha256"] and len(data) == entry["size_bytes"]
        inputs.append({"path": path, "sha256": entry["sha256"], "size_bytes": len(data), "matches_clean_source_commit": True})
    for entry in manifest["files"]:
        data = (artifact.parent.parent / entry["path"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == entry["sha256"] and len(data) == entry["size_bytes"]
    changed = subprocess.check_output(["git", "-C", str(WRITER), "diff", "--name-only", BASE, FROZEN], text=True).splitlines()
    owned = json.loads((WRITER / "tasks/handoff-writer-20261022.json").read_text())["owned_paths"]
    assert all(any(p.startswith(owner + "/") for owner in owned) for p in changed)
    spec = importlib.util.spec_from_file_location("writer_clock_map", WRITER / "experiments/clock-map-smoke/clock_map.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    fixture = json.loads((WRITER / "experiments/clock-map-smoke/fixture.json").read_text())
    probes = []
    for name, change in [("wrong_units", lambda f: f.update(label_unit="s")), ("degenerate_indices", lambda f: f.update(training=[[0,"1"],[0,"3"],[0,"5"]]))]:
        f = copy.deepcopy(fixture); change(f)
        try:
            mod.run(f)
            raise AssertionError("Expected explicit rejection")
        except ValueError as e:
            probes.append({"name": name, "result": "PASS", "response": str(e)})
    perturbed = copy.deepcopy(fixture); perturbed["evaluation_exposed"][0][1] = "8"
    response = mod.run(perturbed)
    assert response["affine"]["offset_ns"] == "1" and response["affine"]["scale_ns_per_tick"] == "2"
    assert response["affine"]["evaluation_exposed"]["sse_ns2"] == "1"
    probes.append({"name": "evaluation_label_perturbation", "result": "PASS", "offset_ns": "1", "scale_ns_per_tick": "2", "evaluation_sse_ns2": "1"})
    for command in ([sys.executable, "scripts/validate.py"], [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]):
        c = subprocess.run(command, cwd=WRITER, text=True, capture_output=True)
        assert c.returncode == 0, c.stderr
        checks.append({"command": command, "exit_code": c.returncode, "stdout": c.stdout, "stderr": c.stderr})
    result = {"review_label": "same-model separate-context LLM review; not independent empirical replication", "frozen_writer_commit": FROZEN, "writer_source_commit": SOURCE, "base_revision": BASE, "reproduction": {"command": p.args, "exit_code": p.returncode, "byte_equal": True, "output_sha256": hashlib.sha256(p.stdout).hexdigest()}, "input_verification": inputs, "scope_changed_paths": changed, "scope_isolated": True, "checks": checks, "counterexample_probes": probes, "model_nonuniqueness": "1+2*n and 1+2*n+n*(n-1)*(n-2)*(n-3)*(n-4) agree at n=0..4 but yield 11 and 131 at n=5; exposed agreement does not identify a native clock law.", "writer_result": output}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
