#!/usr/bin/env python3
"""Audit v2 release migration using only a disposable local bare remote."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH = ROOT / ".tmp" / "release-v2"
REVISION = "35df2b76b2018ef320e5181f143da513b6d83632"
sys.path.insert(0, str(PATCH / "scripts"))
from discovery import claim_commit, claim_payload, git, publish_claim, release_claim, remote_claim


def rejected(operation):
    try:
        operation()
    except RuntimeError as error:
        return str(error)
    raise AssertionError("Operation unexpectedly succeeded")


def main():
    assert subprocess.check_output(["git", "-C", str(PATCH), "rev-parse", "HEAD"], text=True).strip() == REVISION
    result = {"revision": REVISION, "scope": "Disposable local bare remote migration probes; no live release attempted", "checks": []}
    for command in ([sys.executable, "scripts/validate.py"], [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]):
        p = subprocess.run(command, cwd=PATCH, text=True, capture_output=True)
        assert p.returncode == 0, p.stderr
        result["checks"].append({"command": command, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr})
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp); remote = root / "remote.git"; client = root / "client"
        subprocess.run(["git", "init", "--bare", "--initial-branch=main", str(remote)], check=True, capture_output=True)
        subprocess.run(["git", "clone", str(remote), str(client)], check=True, capture_output=True)
        legacy = {"record_type": "claim", "schema_version": 1, "task": "probe-task", "session": "legacy-owner", "created_at": "synthetic", "base_revision": "synthetic", "owned_paths": ["probe-owned"]}
        first = claim_commit(client, legacy)
        git(client, "push", "origin", first + ":refs/heads/claims/probe-task")
        other = dict(legacy, session="new-owner")
        held_rejection = rejected(lambda: publish_claim(client, other))
        owner_rejection = rejected(lambda: release_claim(client, "probe-task", first, "wrong-owner"))
        assert remote_claim(client, "probe-task") == first
        marker = release_claim(client, "probe-task", first, "legacy-owner")
        released = claim_payload(client, "probe-task", marker)
        assert released["status"] == "released" and released["protocol_version"] == 2
        assert released["released_from_sha"] == first and released["owned_paths"] == legacy["owned_paths"]
        assert git(client, "rev-parse", marker + "^") == first
        double_rejection = rejected(lambda: release_claim(client, "probe-task", marker, "legacy-owner"))
        second = publish_claim(client, other)
        held = claim_payload(client, "probe-task", second)
        assert held["status"] == "held" and held["session"] == "new-owner" and held["previous_claim_sha"] == marker
        assert git(client, "rev-parse", second + "^") == marker
        stale_rejection = rejected(lambda: release_claim(client, "probe-task", first, "legacy-owner"))
        assert remote_claim(client, "probe-task") == second
        result["migration_probe"] = {"legacy_claim_sha": first, "released_marker_sha": marker, "reacquired_claim_sha": second, "held_rejection": held_rejection, "wrong_owner_rejection": owner_rejection, "double_release_rejection": double_rejection, "stale_release_rejection": stale_rejection, "parent_chain_preserved": True, "new_owner_unchanged_after_stale_release": True, "result": "PASS"}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
