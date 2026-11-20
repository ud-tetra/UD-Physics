# Discovery v0.1.1 pre-integration metadata schema erratum

**Date:** 2026-11-19 (local) / 2026-11-20 UTC.
**Original commit:** `804b41e7a125f94e7b7d1581bbde330a7402ba9f`; original run metadata remains in immutable Git history.
**Scope:** repository metadata vocabulary only; **no mathematics, programs, source inputs, SHA256 file entries, source snapshots or output files changed.**

The initial draft run manifest was created using descriptive author labels that are not accepted by the repository's canonical `scripts/discovery.py` and `scripts/validate.py` enums. This is a pre-merge, explicitly documented correction rather than a silent replacement.

- `tasks/sphere-inversion-20261119-6b72.json`: status `handoff` -> `active`, because the task is still held and its PR awaits integration.
- `candidates/sphere-information-inversion-6b72/candidate.json`: evidence `[EXACT_CONDITIONAL,NO_GO_SCOPED,OPEN]` -> standard `[EXACT,CONDITIONAL,OPEN]`. The scientific scoping remains in the report and candidate result.
- `artifacts/20261119-gpt6-sphere-6b72/exact-duality-001/manifest.json`: evidence `EXACT_CONDITIONAL` -> `CONDITIONAL`.
- Same manifest input: `source_location=local_selected_source_reference_metadata_NOT_REMOTE_SOURCE_BYTES, source_path=SOURCE_ANCHORS.json` -> `source_location=external, source_path=null` per v2 schema. The input is a separately authored local source-*reference* register, not a byte-for-byte copy of remote GitHub source files. SHA256 `f0d69bfc3a4b9f5c5ccc1a51428f3edb2a21d31d99b872a5b1d083eb3b797ecb` and byte count 1152 are unchanged.

**Version-control limitation:** This pre-integration edit updates three metadata blobs already present in the first unmerged commit; the original bytes remain retrievable in the prior commit. This is an explicit exception to the ordinary immutable finalized-run convention to correct invalid schema before acceptance. No force push, deletion, or claimed historical validator success.

**Verification:** exact-byte output and code checks completed on prior commit. Repository-wide `scripts/validate.py` and unit suite remain NOT_RUN without a fresh checkout; this erratum checks declared fields against source validator logic but does not represent a full validator execution. No nonconstructor review. Physical Promotion = 0.
