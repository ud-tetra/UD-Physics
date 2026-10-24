# Capture correction — source-frozen-remainder-014

**Integrity failure preserved; metadata-only correction, not a scientific re-run.**

First commit `91878be67c9cb96b7fb01a66b0460f498982e006` placed source-frozen-remainder-014 inputs/outputs with matching captured bytes but declared each input source_location as `isolated local runtime`. GitHub Discovery integrity run `40049284839` failed at `scripts/validate.py` with **Invalid external input source metadata**, before unit tests. This was a schema rule error, not a failed numerical result.

Valid schema2 local external inputs require `source_location: "external"` and `source_path: null`. We corrected only the seven input metadata records and added this disclosure to the summary; all 7 input source bytes and 10 output bytes, SHA256 digests, run ID and calculations remain unchanged. The original invalid version remains recoverable at prior commit `91878be...` and is not treated as a valid immutable capture. This new manifest is the first validator-eligible version.

Validation at the corrected branch head must be checked separately. Neither version certifies numerical integration error or the all-phase nonlinear physical result.
