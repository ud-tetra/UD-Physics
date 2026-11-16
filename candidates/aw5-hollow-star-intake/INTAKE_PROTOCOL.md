# AW5 blind intake and adjudication v1

**SYNTHETIC PIPELINE REPLAY.** Agile physical hypothesis. Physical Promotion = 0.

Before acquisition, the custodian freezes protocol AW5-ACQUISITION-v1, the three role assignments and a SHA-256 commitment to the canonical JSON reveal. Use an independently generated random nonce of at least 128 bits encoded as 32 hex characters for a non-fixture reveal. Keep the role map and nonce separate from the blinded packet. The packet has opaque trace IDs and contains 256 timestamps and signed observations per trace. Use exact rational strings or integer JSON numbers. The runnable replay fixture constructs every packet field and the reveal.

The scoring operator runs `python3 intake_score.py packet.json > scores.json` and records the blind scores and packet digest before reveal. Upon receipt of the reveal, run `python3 intake_score.py packet.json --scores scores.json --reveal reveal.json`. The reveal is a JSON object with keys nonce and roles. Canonicalization uses Python json.dumps with sorted keys and compact separators, followed by SHA-256 of the UTF-8 bytes. Independent custody and an external timestamped audit record establish the chronology. The local tool verifies content consistency and the commitment.

The scorer checks count and timestamp tolerances, declared timing-independent noise conditions, dissipativity and rational certificate limits. A syntactically valid declaration is a fixture input. Measured evidence requires independently supported certificates and acquisition provenance. This version gates measured inputs out.

After reveal, each control gap must be at least 3/64. PASS means the two observed contrasts meet the frozen model compatibility margin. FAIL means an admissible packet misses one or both contrasts. INADMISSIBLE means the declared acquisition conditions or custody checks failed. The alternative-side probability bound in the sampled acquisition note is conditional on its model and does not specify a physical false-positive rate.

Replay with `PYTHONDONTWRITEBYTECODE=1 python3 replay_intake.py`. The flat fixtures exercise the software gates and threshold arithmetic. An explicitly declared correlation is rejected. Unknown or undeclared correlation cannot be inferred from these fixtures.

## Run footer

- **Mission** — Freeze and exercise blind intake before measured trace admission.
- **Done** — Implemented exact rational scoring, commitment-checked role reveal, two-control adjudication, and synthetic gate replay.
- **Finding** — Equality at 3/64 passes, a single shortfall fails, and correlation, certificate violations, altered scores, or an altered reveal are inadmissible.
- **Bridge value** — The intake separates acquisition eligibility from observed agreement. Physical validation and independent review remain open.

## Next step

1. **Priority 90/100** — Replay model-generated signed impulse traces through the same frozen scorer, then specify independently auditable certificate provenance for timing, operators, and noise.
