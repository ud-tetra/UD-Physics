# v0.3.3 — source/run capture completeness

This is an **append-only replacement run** for the earlier incomplete `source-contrast-v0.3`. The original files and manifest remain in Git history.

The full v0.3 source and original execution files are now on the GitHub development branch with verified matching Git blob hashes against local originals: `REPORT.md`, `verify.py`, `replay_stdlib.py`, `results.json`, `run.log`, `replay.log`; four March source inputs and predecessor report v0.2 are also copied in `inputs/`.

Run `cd artifacts/20261115-chatgpt-constitutive-b7cf/source-contrast-full-v0.3.3; python3 files/verify.py; python3 files/replay_stdlib.py` (requires SymPy only for `verify.py`). The scripts passed locally; **a fresh-branch checkout replay and repository CI remain NOT_RUN**, as does a non-constructor review. Byte equality is source integrity, not a mathematical proof certification or physical bridge.

Source-derived admissibility alone still leaves free `q,κ` and event clock. The conditional negative result remains unchanged. Physical Promotion=0.
