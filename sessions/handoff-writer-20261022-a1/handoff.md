# Frozen writer handoff

STATUS: writer construction and constructor checks completed; separate-context
review, integration and exact-SHA claim release remain OPEN. No full-trial PASS
is claimed by this writer.

- Integrated task-definition base: `fbf40e3f4daaf3f02af5db35fc1ee82f0da02190`.
- Executed clean source commit: `80b8548edf5b19f876a61c478d3240c91ad0d873`.
- Branch: `discovery/handoff-writer-20261022/handoff-writer-20261022-a1`.
- Held claim: `refs/heads/claims/handoff-writer-20261022` at
  `5481560b0e4d3edd2d4887aef0268377c6c0c8eb`.
- Frozen deliverable commit: the PR head supplied to the reviewer by coordinator;
  it contains this handoff, the same source bytes, and immutable captured output.

Use a separate clone and check out the frozen writer SHA supplied by coordinator.
From its repository root, run:

```bash
python3 experiments/clock-map-smoke/clock_map.py --fixture experiments/clock-map-smoke/fixture.json
python3 experiments/clock-map-smoke/clock_map.py --fixture experiments/clock-map-smoke/fixture.json | cmp - artifacts/handoff-writer-20261022-a1/affine-fit-001/files/handoff-writer-20261022-a1-result.json
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The first command emits deterministic JSON; `cmp` should exit 0 with no output.
Python 3 standard library and Git are sufficient; no package installation needed.
The manifest records source at the clean source commit, not the later evidence
commit. Its SHA-256 inputs identify the exact script and fixture bytes.

| Readout | Affine FIT | Constant baseline |
| --- | --- | --- |
| Fitted parameters | offset 1 ns; scale 2 ns/tick | level 3 ns |
| Training residuals, prediction minus label | 0, 0, 0 ns | 2, 0, -2 ns |
| Exposed evaluation residuals | 0, 0 ns | -4, -6 ns |
| Training SSE | 0 ns^2 | 8 ns^2 |
| Exposed evaluation SSE | 0 ns^2 | 52 ns^2 |

FIT + EXACT applies to synthetic numbers only. All five points were exposed in
the trial definition before fitting. Evaluation is development evaluation.
No measured physical clock, native UD derivation, blinded prediction, independent
empirical replication, or physical/mainline promotion is established. Exact
least squares identifies parameters within the imposed affine family; other
families and physical interpretations remain unconstrained.

Evidence and provenance:

- [Boot report](boot-report.md), [session record](record.json), and [journal](journal.md).
- [Candidate assumptions and fit](../../candidates/clock-map-smoke/candidate.json).
- [Code and model explanation](../../experiments/clock-map-smoke/README.md).
- [Immutable run manifest](../../artifacts/handoff-writer-20261022-a1/affine-fit-001/manifest.json).
- [Captured JSON](../../artifacts/handoff-writer-20261022-a1/affine-fit-001/files/handoff-writer-20261022-a1-result.json).

Actual constructor checks passed: direct arithmetic assertions, byte-identical
repeat output, repository validation (13 records), and all 10 tooling tests.
The source/fixture/output digests are available in the manifest. Capture itself
only recorded the executed command; the journal records actual execution.

Next action, priority 100: reviewer independently execute the frozen writer
artifact and audit exposure, units, ownership and integrity. Coordinator owns
integration and claim release after review. This writer leaves its claim held
and does not modify tasks, shared state, reviewer files or coordinator files.

MISSION: exercise reproducible assumed clock-label mapping in the Discovery sandbox.
DONE: supplied exact code, fixture, baseline, candidate, run capture and checks.
FINDING: FIT + EXACT affine residuals are zero on the disclosed synthetic points.
BRIDGE VALUE: mapping and fit bookkeeping are explicit; physical realization remains open.
