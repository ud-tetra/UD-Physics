# Contributing

Boot with BOOTLOADER.md. Follow AGENTS.md, claim a task, and use an isolated discovery branch. Include a session handoff, candidate/source provenance, tests actually executed, and captured artifacts in the PR. Keep changes scoped and preserve failed results.

Run:
```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Do not merge stale work over another session. Integrate shared summaries under a separate integration claim. Review and CI validate their declared scope; neither automatically promotes a physical claim.
