# Frozen one-leaf AW5 synthetic trace replay

**NUMERICAL / SYNTHETIC.** The frozen scorer evaluates the 12-decimal serialized samples using exact rational arithmetic. **Physical Promotion = 0.** No measured trace, injected noise, or calibration error is included.

## Freeze and replay

1. The model, face signs, probe normalization, window and controls are pinned by the [one-leaf certificate](../REFINED_WINDOW_CERTIFICATE.md) at c26feb7e1c93b3eb54d3d055df7a1fab3d6243cf. One packet contains the 60-coordinate refined target, 47-coordinate filled control and 60-coordinate refined orthogonal control. All traces use 256 midpoint samples over 32 native units, with exterior damping γ=1/512. The incremental matrix exponential was checked against the direct exponential at the first, middle and last samples of each trace.
2. The scorer file was checked byte-for-byte against the pinned v1 blob. The role-free [packet](blind-packet.json), [manifest](freeze.json), and [blind scores](blind-scores.json) were committed at [526cc9873d6984fea9280ace81f505faa7020c2a](https://github.com/ud-tetra/UD-Physics/commit/526cc9873d6984fea9280ace81f505faa7020c2a). The role reveal was held outside that commit. The verifier checked the raw packet, canonical packet, all three canonical envelope hashes, committed role hash and scores against the published bytes before adjudication.
3. The unchanged scorer then consumed the [reveal](reveal.json), verified its commitment, and returned [PASS](verdict.json) at 3/64.

| Comparison | Exact scored gap | Approximate gap |
| --- | ---: | ---: |
| Refined target vs. filled | 147799803523/640000000000 | 0.230937193005 |
| Refined target vs. refined orthogonal | 3881205912749/16000000000000 | 0.242575369547 |

The constructor generated the roles and traces. The staged record verifies packet integrity and that the scorer reduced opaque traces before receiving the role map. Independent experimental custody remains open. The certificate's bound is 2 exp(−16), approximately 2.25×10⁻⁷, for the joint adverse-noise event under its model. This deterministic replay verifies scoring behavior.

From the candidate directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 refined_trace_freeze.py one-leaf-replay-v1
PYTHONDONTWRITEBYTECODE=1 python3 intake_score.py one-leaf-replay-v1/blind-packet.json \
  --scores one-leaf-replay-v1/blind-scores.json --reveal one-leaf-replay-v1/reveal.json
```

## Run footer

- **Mission** — Exercise the frozen scorer on the specified one-leaf carrier with both controls.
- **Done** — Generated and froze signed model traces, verified the published digests before reveal, and replayed adjudication.
- **Finding** — Both gaps clear 3/64 with γ=1/512 on the declared synthetic packet.
- **Bridge value** — The refined model and acquisition scorer now connect end to end. Calibration, measured admission, and independent custody remain open.

## Next step

1. **Priority 92/100** — Bind the declared carrier and probe map to independently calibrated hardware records, beginning with the signed-pair bench packet and timing loopback.
