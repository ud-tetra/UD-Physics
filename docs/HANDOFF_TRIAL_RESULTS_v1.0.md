# Fresh-runtime handoff results v1.0

**Result: PASS for the declared writer/reviewer scope.** Two fresh same-model LLM contexts used separate clones, branches, sessions and task claims through one GitHub account. This is an operational workflow test, not cross-provider authentication validation or empirical physics replication.

| Acceptance criterion | Result | Evidence |
| --- | --- | --- |
| Verified load order and capabilities | PASS | Writer/reviewer boot reports at base fbf40e3f4daaf3f02af5db35fc1ee82f0da02190 |
| Isolated ownership | PASS | Disjoint owned paths and separate live claims; writer changed only 10 allowed files |
| Frozen artifact reproduced | PASS | Writer 846a6a31 output byte-identical in reviewer; SHA-256 9a32fe7b93badd64adfadc67a7a91e6e4dd11dd489dc9fc6be134f263fb8fbd6 |
| Competing claim rejected | PASS | Live GitHub 422 Reference already exists; owner unchanged |
| Review/fixes/checks | PASS | Input-provenance and connector-lifecycle fixes reviewed; all 16 tooling tests passed |
| Integrated lifecycle | PASS | PRs 1–6 integrated; writer/reviewer released audit markers verified |

## Discovery demonstration

The assumed affine map has fitted offset 1 ns and scale 2 ns/tick. The constant baseline is 3 ns; training and evaluation squared-error sums are 8 ns² and 52 ns² respectively, while affine residuals vanish. All synthetic labels were exposed in the plan. This is FIT plus exact rational arithmetic under declared assumptions; it establishes no measured clock, native UD time law, or spacetime correspondence.

## Defects found and amendments

The reviewer showed legacy run.inputs could be malformed without validation and same-named inputs lost path mapping. Run schema 2 now preserves explicit input copies, IDs, source-relative paths and digests; copied-byte tampering and ambiguous legacy names are checked. Existing schema 1 records remain preserved with their input-byte limitations.

The live writer could not delete a claim because authenticated Git push was unavailable and the connector lacked delete. Claim protocol 2 uses child released markers and exact-SHA updates, followed by guarded reacquisition. The failed v1 deletion remains recorded; no physical deletion is claimed. Separate probes verified stale/wrong-owner/double release rejection and single-winner reacquisition. Both live runtime releases succeeded.

The coordinator also recorded and corrected an unintegrated template scope mismatch through an explicit task/claim amendment before integration. Original audit runs, failed-attempt records, source snapshots and frozen writer artifacts remain intact.

## Entry points and verification

- [Writer handoff](../sessions/handoff-writer-20261022-a1/handoff.md)
- [Reviewer report](../reviews/runtime-handoff-20261022/review.md)
- [Reviewer lifecycle evidence](../reviews/runtime-handoff-20261022/lifecycle.json)
- [Synthetic example](../experiments/clock-map-smoke/README.md)
- [Trial acceptance and coordinator closure](../sessions/handoff-integrator-20261022-a1/acceptance.json)
- [Integrated verification manifest](../artifacts/handoff-integrator-20261022-a1/integrated-verification-v1/manifest.json)
- [Current concurrency protocol](CONCURRENCY.md)

Local integrated validation and all 16 tooling tests passed at 90e9d0048826219485454d71c00aed7b536da279. The newest GitHub Actions runs were queued at the last observation; no remote pass is inferred from a queued status. Server-enforced main protection remains disabled. Final coordinator ownership closure is recorded separately in the linked session acceptance record after this milestone integrates.
