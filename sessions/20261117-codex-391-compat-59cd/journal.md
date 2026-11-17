# Session 20261117-codex-391-compat-59cd

Boot attempt: 2026-11-17T01:09:59.356033+00:00

Runtime: Codex GitHub connector and isolated local worktree

Task: discovery-391-metadata-compat

Goal: Restore Discovery validation for the integrated #391 archive

Ownership: UNCLAIMED until remote claim acquisition succeeds.

## 2026-11-17T01:09:59.500508+00:00

Checkpoint (handoff): Path-scoped compatibility preserves #391 source bytes and hash checking.

Next: Review compatibility change and rerun Discovery CI on main.

## 2026-11-17T01:10:21.671925+00:00

Full validation passes. Normalizing the four archived labels exposes a dotted run ID and an uncaptured predecessor reference; the exact path and value exceptions preserve the original records and digests. Physical Promotion = 0.
