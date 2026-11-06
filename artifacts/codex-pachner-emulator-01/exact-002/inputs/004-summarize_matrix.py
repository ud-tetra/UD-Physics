"""Capture compact, reproducible receipts without duplicating long fractions."""
from hashlib import sha256
import json
import sys

raw = sys.stdin.buffer.read()
d = json.loads(raw)
d["full_output_sha256"] = sha256(raw).hexdigest()
d["sample_count"] = sum(len(row["trace"]) for row in d["cases"])
for row in d["cases"]:
    trace = row.pop("trace")
    row["sample_count"] = len(trace)
    row["trace_sha256"] = sha256(json.dumps(trace, separators=(",", ":")).encode()).hexdigest()
print(json.dumps(d, indent=2))
