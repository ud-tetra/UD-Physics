# Sphere information inversion — Discovery journal

**2026-11-20T03:09:32+00:00** · task `sphere-inversion-20261119-6b72` · claim `claims/sphere-inversion-20261119-6b72` held `1a3ba3c0918a0e5b74afac19293f9869cc506e7e` · base `03722496f5b00e8f3f01b2400e4015eb65fdebc4`.

- Read BOOTLOADER v1.1, Discovery v1.2, AGENTS, mathematical method, CURRENT, CONCURRENCY v2.0, ARTIFACTS.
- Declared `K=boundary Delta3` separately from interior `Delta3` and `boundary Delta4`.
- Confirmed `S2` Betti `(1,0,1)` and exact signed complement identities.
- Discovered key distinction: ambient inversion is identity on a sphere, whereas the supplied regular-tetra primal-dual geometric map gives antipodal readout.
- Replayed with symbolic SymPy and independent standard-library Fractions; both PASS.
- Conventional tetra dual baseline reproduces the identities; no UD-specific physical signal.
- No code/experiment data fitted to physical targets. Metric and readout explicitly supplied, not derived.
- NOT_RUN: repository validate.py and unit tests without local full checkout; independent reviewer not assigned.
- Handoff: target-blind source-derived information inversion and geometry readout required. Physical Promotion 0.
