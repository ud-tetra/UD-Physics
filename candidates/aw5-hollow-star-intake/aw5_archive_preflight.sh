#!/usr/bin/env bash
# Compare raw AW5 exports with a previously authenticated SHA-256 manifest.
set -euo pipefail

exec python3 - "$@" <<'PY'
import argparse
from collections import Counter
from contextlib import ExitStack
import csv
import hashlib
import io
import json
import os
import re
from pathlib import Path
import stat
import tarfile
import zipfile


def load_manifest(path):
    entries = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64}) [ *](.+)", line)
        if match is None:
            raise ValueError(f"Invalid SHA-256 manifest line {line_number}")
        checksum, name = match.groups()
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or relative.name in ("", "."):
            raise ValueError(f"Archive name must be relative to the raw directory, line {line_number}")
        if relative in entries:
            raise ValueError(f"Duplicate archive name on line {line_number}: {name}")
        entries[relative] = checksum.lower()
    if not entries:
        raise ValueError("The expected digest manifest is empty")
    return entries


def file_state(stream):
    info = os.fstat(stream.fileno())
    if not stat.S_ISREG(info.st_mode):
        raise ValueError("Expected a regular archive file")
    return info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns


def csv_preflight(stream):
    sample = stream.read(65536)
    # A prefix can end partway through a row or UTF-8 character.
    if len(sample) == 65536:
        sample = sample[:sample.rfind(b"\n")+1]
    if b"\x00" in sample:
        raise ValueError("CSV prefix contains NUL bytes")
    text = sample.decode("utf-8-sig")
    for delimiter in (",", ";", "\t"):
        rows = csv.reader(io.StringIO(text), delimiter=delimiter)
        widths = Counter(len(row) for row in rows if len(row) >= 2)
        if any(count >= 2 for count in widths.values()):
            return {"format": "delimited text", "candidate_delimiter": delimiter}
    raise ValueError("CSV prefix lacks two consistently delimited records")


def format_preflight(stream, path):
    stream.seek(0)
    name = path.name.lower()
    if name.endswith(".zip"):
        with zipfile.ZipFile(stream) as archive:
            count = sum(not item.is_dir() for item in archive.infolist())
        kind = "zip"
    elif name.endswith((".tar.gz", ".tgz")):
        if stream.read(2) != b"\x1f\x8b":
            raise ValueError("Expected a gzip header")
        stream.seek(0)
        with tarfile.open(fileobj=stream, mode="r|gz") as archive:
            count = sum(item.isfile() for item in archive)
        kind = "gzip tar"
    elif name.endswith(".csv"):
        return csv_preflight(stream)
    else:
        raise ValueError("Expected a .csv, .zip, .tar.gz or .tgz archive")
    if count == 0:
        raise ValueError("Archive contains no file members")
    return {"format": kind, "file_members": count}


def report(result, exit_code):
    print(json.dumps(result, indent=2))
    return exit_code


def main():
    parser = argparse.ArgumentParser(
        prog="aw5_archive_preflight.sh",
        description="Verify a raw archive batch before format inspection. "
                    "Supply the custodian's independently authenticated manifest."
    )
    parser.add_argument("expected_manifest", type=Path, help="GNU sha256sum-style manifest")
    parser.add_argument("raw_directory", type=Path, help="Directory containing the manifest's raw files")
    args = parser.parse_args()
    try:
        root = args.raw_directory.resolve(strict=True)
        if not root.is_dir():
            raise ValueError("Raw directory must be a directory")
        expected = load_manifest(args.expected_manifest)
    except (OSError, UnicodeError, ValueError) as exc:
        return report({"status": "INVALID_INPUT", "error": str(exc)}, 2)

    records = []
    with ExitStack() as sources:
        verified = []
        for relative, checksum in expected.items():
            item = {"file": str(relative), "expected_sha256": checksum}
            records.append(item)
            try:
                resolved = (root / relative).resolve(strict=True)
                if not resolved.is_relative_to(root) or not resolved.is_file():
                    raise ValueError("Archive must resolve to a regular file inside the raw directory")
                stream = sources.enter_context(resolved.open("rb"))
                state = file_state(stream)
                observed = hashlib.file_digest(stream, "sha256").hexdigest()
                item["observed_sha256"] = observed
                if file_state(stream) != state:
                    raise ValueError("Archive changed during hashing")
                if observed != checksum:
                    raise ValueError("SHA-256 mismatch")
                item["digest"] = "MATCH"
                verified.append((relative, stream, state, item))
            except (OSError, ValueError) as exc:
                item.update(digest="FAIL", error=str(exc))
        if len(verified) != len(expected):
            return report({"status": "DIGEST_FAILED", "format_preflight": "SKIPPED", "files": records}, 1)

        format_failed = False
        for relative, stream, state, item in verified:
            try:
                if file_state(stream) != state:
                    raise ValueError("Archive changed before format inspection")
                details = format_preflight(stream, relative)
                if file_state(stream) != state:
                    raise ValueError("Archive changed during format inspection")
                item.update(format_preflight="PASS", **details)
            except (OSError, ValueError, EOFError, csv.Error, tarfile.TarError, zipfile.BadZipFile) as exc:
                item.update(format_preflight="FAIL", error=str(exc))
                format_failed = True
    return report({"status": "FORMAT_FAILED" if format_failed else "PASS_PREFLIGHT",
                   "files": records}, int(format_failed))


if __name__ == "__main__":
    raise SystemExit(main())
PY
