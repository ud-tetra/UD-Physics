#!/usr/bin/env python3
"""Verify the preserved UD graphite and octahedral development captures.

The original capture manifests retain paths relative to ud-tetra/UD; this
checker resolves those paths under the Discovery run's files/ directory.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(root):
    captures = sorted((root / "captures").iterdir())
    files_checked = 0
    for capture in captures:
        manifest = json.loads((capture / "MANIFEST.json").read_text())
        assert manifest["capture_id"] == capture.name
        for entry in manifest["files"]:
            path = root / entry["path"]
            assert path.is_file() and path.stat().st_size == entry["size_bytes"]
            assert sha256(path) == entry["sha256"], path
            files_checked += 1
        event = root / "events" / (capture.name + ".json")
        assert event.is_file(), event
        json.loads(event.read_text())
    run = json.loads((root.parent / "manifest.json").read_text())
    assert len(run["files"]) == len([p for p in root.rglob("*") if p.is_file()])
    for entry in run["files"]:
        path = root.parent / entry["path"]
        assert path.is_file() and path.stat().st_size == entry["size_bytes"]
        assert sha256(path) == entry["sha256"], path
    print(f"PASS: {len(captures)} captures, {files_checked} original payloads, "
          f"{len(captures)} events, {len(run['files'])} imported files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path, help="Discovery run directory containing manifest.json")
    verify(parser.parse_args().run.resolve() / "files")
