# Checkpoint — original amplitude relative short tube u<=49/50

**STATUS:** HANDOFF / EXACT / CONDITIONAL / FIT; not an independent experiment, not mainline export, not merged.

- **Verified current main:** `127c5fb995cdd218fecc479bccec8ed7a2c2bad0` (read-only), source files `mountloss.py`, `hardware.py`, `free3d/model.py`, `multiport/network.py` verified identical to prior imported version.
- **Active session:** `phasewindow-20261022-gpt6-7c41`; claim `refs/heads/claims/icosahedral-phasewindow-20261022` belongs to this session and is held; claim origin `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`.
- **Research branch:** `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41` (separate from integrated state).
- **Competing task:** separate PR44 `integration-icosahedral-greenbounds-20261022` is held by another session. No edits to its paths, and no imported recovery gaps silently closed.

## Completed exact conditional result

For original full560-state nonlinear 3D MountLoss, alpha0=1/10, initial primary/devices at reference/rest, all 180 housing initial displacement/velocity phases with Eh<=51/20000000 and the original continuous qualified coefficient box, the solution exists through u=49/50. Every one of 120 housing struts remains >3853/281250 reference shell lengths, primary members remain positive, and all 20 oriented cell ratios lie in ((1/500)^3,(999/500)^3). Spatial rigid kinetic energy remains included. These are conservative geometric protections, not volume RMS or shape-coherence gates.

The calculation refines the previous u=9/10 theorem using R²<181/200 in common velocity norm, combined housing initial oscillator energy, and the finite sine integral `∫_0^(49/50)|sin 10t|dt<79/125`. Its rational horizon was selected after previous bounds and target exposure (FIT). No constitutive modification or new physical calibration occurred.

## Evidence and capture

- [Proof](../../experiments/icosahedral-phasewindow-20261022/TUBE098.md)
- [Exact checker](../../experiments/icosahedral-phasewindow-20261022/tube098.py)
- [Separate same-runtime check](../../experiments/icosahedral-phasewindow-20261022/tube098_check.py)
- [Typed receipt](tube098_receipt.json)
- [Immutable run manifest](../../artifacts/phasewindow-20261022-gpt6-7c41/relative-tube-006/manifest.json)
- Captured 3 inputs including previous exact proof, plus source-check result and written proof, each with SHA256 and verified blob identity.
- Same-runtime Python Fraction and SymPy checks: PASS; quadrature is a diagnostic only. Independent mathematical reproduction: NOT_RUN. Hardware/physical testing: UNSCORED.

## Failure and next step

The same bound at u=1 yields squared cell-relative operator bound 648/625>1; this **sufficient certificate fails**, not the nonlinear dynamics. In particular, it does not show cell collapse or violate earlier safety claims. Full nonlinear u=100 all-180-phase breathing>=80%, hub mismatch<=5%, and housing-energy remaining<=50% remain **OPEN**.

Next highest-value action: independently verify this exact proof and recover PR44 forced-response source/Green/alignment evidence; close a full positive-norm nonlinear tube to the original 100-unit horizon without changing physical targets, else preserve failed certificate attempts and check cross-path ownership. Keep this claim held until reviewed/integrated or explicitly abandoned.
