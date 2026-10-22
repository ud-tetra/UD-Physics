# Running documentation and artifact capture

## Repository layout

| Path | Contents and ownership |
| --- | --- |
| tasks/<task>.json | Scope, dependencies, owned paths; task owner |
| sessions/<session>/record.json | Runtime, task, base revision, claim, status and next action |
| sessions/<session>/journal.md | Concise running notes and corrections; one owner |
| candidates/<candidate>/candidate.json | Hypothesis, map, assumptions, fits, targets and result |
| artifacts/<session>/<run>/manifest.json | Immutable run metadata and file digests |
| artifacts/<session>/<run>/files/ | Intentionally captured outputs |
| sources/imports/<snapshot>/ | Read-only source snapshots with provenance |
| state/CURRENT.md | Integrated milestone summary; integrator only |

Capture useful reasoning, decisions, and reproducible evidence. Do not save hidden reasoning traces, credentials, personal data, full private chats, or automatic environment dumps. Selected public research notes and user-authorized source files are appropriate.

## Commands

```bash
python3 scripts/discovery.py note --session SESSION --text "FIT: selected the exponent using the exposed target; next test is sensitivity."
python3 scripts/discovery.py new-candidate --session SESSION --id CANDIDATE --question "What is the residual response?"
python3 scripts/discovery.py capture --session SESSION --run RUN --evidence NUMERICAL --summary "Toy-model spectrum" --command "python3 analysis.py" --input analysis.py --artifact results.json
python3 scripts/discovery.py checkpoint --session SESSION --status handoff --finding "Conditional result; calibration remains fitted." --next "Compare a held-out regime."
python3 scripts/validate.py
```

Commands record work; capture does not execute or validate the supplied command. Include the actual executed command and its result in your journal. A manifest digest checks bytes, not scientific correctness. Input file hashes identify source bytes; changed inputs require a new run. Keep source/input code in the repository or intentionally capture a copy when needed for reproduction.

Run directories are immutable after capture. Use a new run ID for corrections and record which earlier run it supersedes. Validation rejects modified captured outputs. No binary artifacts, private conversation archives, or bulk source collections are imported automatically.

Keep normal Git files small (prefer below 10 MiB per file). Use release assets or another explicitly configured large-file destination for larger research outputs, with a durable link, digest, and provenance manifest; GitHub Actions artifacts alone are not permanent archival storage.

## Manual/connector capture

Use templates/session.json, templates/candidate.json, and templates/run_manifest.json. Generate SHA-256 values with a capable runtime; leave unavailable verification as NOT_RUN in the session. Do not substitute a Git object SHA for a SHA-256 file digest. A partial draft manifest belongs in the session directory until complete; put only valid finalized runs under artifacts/.

At milestones, include links to the candidate, code, run, limitations, and next discriminant in the session handoff and PR. CURRENT.md links integrated milestones rather than every note.
