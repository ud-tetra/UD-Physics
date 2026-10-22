# Fresh-runtime handoff review

RESULT: writer artifact reproduction and reviewer checks PASS at frozen writer
`846a6a31c3ca87277afa584e6e4d782ef40e9168`. This is a same-model,
separate-context LLM review, not independent empirical replication. Integration
and exact-SHA claim release remain coordinator/session-owner actions.

The reviewer booted from verified integrated base
`fbf40e3f4daaf3f02af5db35fc1ee82f0da02190` in its own clone, on branch
`discovery/handoff-reviewer-20261022/handoff-reviewer-20261022-a1`, with claim
`e48cb946c47488062c6a5f7eef1be3529213991d`. Load-order digests, capabilities,
disjoint scopes and observed live refs are in [boot-audit.json](boot-audit.json).
Writer records explicitly retain constructor-only check status until this review.

| Review | Actual result |
| --- | --- |
| Frozen output reproduction | Byte-identical; SHA-256 `9a32fe7b93badd64adfadc67a7a91e6e4dd11dd489dc9fc6be134f263fb8fbd6` |
| Clean source provenance | Script and fixture bytes, hashes and sizes match `80b8548edf5b19f876a61c478d3240c91ad0d873` |
| Exact arithmetic and baseline | Offset 1 ns, scale 2 ns/tick; affine SSE zero; constant 3 ns, training/evaluation SSE 8/52 ns squared |
| Exposure and interpretation | All five labels explicitly exposed; FIT + EXACT, synthetic units, development evaluation, assumptions and non-identifiability disclosed |
| Writer scope | All 10 changed paths inside writer-owned directories; no shared-state/reviewer edits |
| Frozen writer checks | Validator PASS (13 records); all 10 original tooling tests PASS |
| Live claim contention | Competing create-branch rejected with GitHub 422; original writer SHA and claim blob unchanged |
| Adversarial arithmetic | Wrong units and degenerate indices rejected; changing evaluation label 7 to 8 leaves fitted parameters unchanged and yields evaluation SSE 1 |

No blocking writer defect was found. Zero residuals follow the synthetic affine
construction; a polynomial modification can match all five exposed points and
diverge elsewhere. For example, `1+2*n+n*(n-1)*(n-2)*(n-3)*(n-4)` yields 131 at
`n=5`, versus the affine value 11. The writer already discloses this family
non-uniqueness and makes no claim to a physical clock law.

P2 provenance finding: the original validator accepted malformed `run.inputs`
metadata, and capture lost source path mapping for same-named inputs. The
disposable reproducer and immutable original [baseline run](../../artifacts/handoff-reviewer-20261022-a1/baseline-audit-v1/manifest.json)
preserve the actual observations. This finding did not invalidate the writer's
distinct script/fixture hashes, which this reviewer verified manually.

Coordinator amendment `e5c1a4edbb3e3aec62b8c5dde843031c17ae123a` fixes both
observed cases with schema-2 input copies, unique IDs and source paths, plus
metadata, digest and containment validation. Separate amendment checks passed:
validator, all 14 tests, same-name preservation, malformed metadata rejection,
input-tampering rejection and acceptance of frozen writer schema-1 artifacts.
PR #3 head `e576434458fa7252b119c2ff88673a3699ad7342` contains identical tooling
bytes plus an explicit coordinator task/claim expansion to `templates`; the
earlier out-of-scope template edit and correction are disclosed. No blocking
amendment defect was found. Old v1 evidence has not been rewritten.

Acceptance criteria 1–4 were executed and pass within this review's visibility.
Criterion 5 has recorded findings, a tested correction and passing local checks;
final integration checks remain the coordinator's responsibility. Criterion 6
(final PR integrations and releases) remains OPEN here. No full-trial completion
or physical promotion is claimed by this pre-integration report.

Reproduce with the commands and exact revision guards in
[reproduce_writer.py](reproduce_writer.py), [audit_baseline.py](audit_baseline.py),
and [audit_amendment.py](audit_amendment.py). The writer and amendment checkouts
are disposable detached worktrees under the reviewer clone's ignored `.tmp/`.
Read the scripts for their exact `git worktree add --detach` revisions.

MISSION: test whether an explicitly assumed clock-label FIT can be handed off reproducibly.
DONE: reproduced frozen writer bytes and audited boot, ownership, units and provenance.
FINDING: FIT + EXACT arithmetic and protocol checks pass; provenance defects received a tested amendment.
BRIDGE VALUE: reproducible bookkeeping is demonstrated; physical realization remains open.

Next action, priority 100: coordinator integrate this focused review with current
main, rerun integrity checks, then request exact-SHA reviewer claim release.
