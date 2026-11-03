# Capture correction — source-frozen-remainder-014

**Integrity failure preserved; metadata-only correction, not a scientific re-run.**

First commit `91878be67c9cb96b7fb01a66b0460f498982e006` placed source-frozen-remainder-014 inputs/outputs with matching captured bytes but declared each input source_location as `isolated local runtime`. GitHub Discovery integrity run `40049284839` failed at `scripts/validate.py` with **Invalid external input source metadata**, before unit tests. This was a schema rule error, not a failed numerical result.

Valid schema2 local external inputs require `source_location: "external"` and `source_path: null`. We corrected only the seven input metadata records and added this disclosure to the summary; all 7 input source bytes and 10 output bytes, SHA256 digests, run ID and calculations remain unchanged. The original invalid version remains recoverable at prior commit `91878be...` and is not treated as a valid immutable capture. This new manifest is the first validator-eligible version.

Validation at the corrected branch head must be checked separately. Neither version certifies numerical integration error or the all-phase nonlinear physical result.

## Second integrity correction (CSV byte transfer)

Run `40049376931` at head `330bf5a...` reached manifest file integrity but failed `SHA-256 mismatch: files/selected_remainder_trace.csv`. The transfer bundle was constructed with Python `Path.read_text()`, which converted 402 original CRLF line endings to LF. The original CSV in the captured local ZIP had 65,606 bytes; the initially published GitHub LF copy had 65,204. All numerical CSV values were unchanged but the file bytes disagreed with the manifest SHA-256.

This correction restores **exactly 402 CRLF line endings** to GitHub file content without changing CSV values, the capture manifest, input bytes, or scientific results. The full sequence of invalid/failed capture attempts remains in Git history. Check final CI status independently.
