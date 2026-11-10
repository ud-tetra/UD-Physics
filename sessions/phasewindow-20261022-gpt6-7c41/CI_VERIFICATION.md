# GitHub Actions integrity verification

Repository: ud-tetra/UD-Physics
PR: https://github.com/ud-tetra/UD-Physics/pull/45 (draft, unmerged)
Observed PR head: `66f5f3624842a59b8940302d5bac1f99cadbebe9`.
Workflow: Discovery integrity, run `39865810320`, job `120127591105`.
Status: completed; conclusion: **success**.

Retrieved actual job log shows:
- `python3 scripts/validate.py`: `PASS: 90 records; manifest digests and local documentation links valid.`
- `python3 -m unittest discover -s tests -v`: `Ran 16 tests in 0.552s`, `OK`.

Scope limits:
- CI ran against GitHub PR merge ref based on verified main `ce89a9cd15439463d9a64d983d91c22ea4368726`.
- These are repository integrity/tooling tests, **not** independent verification of the mathematical theorem or empirical bridge.
- The numerical reanalysis's `replay.py` is **NOT_RUN** in that CI, and no full-560 nonlinear new integration is claimed.
- This follow-up CI evidence record is itself a new documentation commit; separately verify CI at its final head before review.

The source SHA-256 checks and direct connector reanalysis have their own source provenance in `phasewindow-001`.
