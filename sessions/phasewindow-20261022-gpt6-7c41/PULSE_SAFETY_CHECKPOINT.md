# Continuation checkpoint — exact 3D pulse safety

UTC: 2026-10-22T22:55:00Z
Session: `phasewindow-20261022-gpt6-7c41`; task `icosahedral-phasewindow-20261022`; claim still held by this session.
Integrated source: `ce89a9cd15439463d9a64d983d91c22ea4368726`; isolated branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
No mainline export; Draft PR #45 remains awaiting scientific review.

## MISSION
Test a disjoint, high-value nonlinear all-phase domain theorem without overwriting held Draft PR #44's forced-Green/alignment recovery work.

## NEW RESULT — EXACT / CONDITIONAL
- Same 280-coordinate / 560-phase 3D MountLoss ODE, no fitted constitutive changes. Initial reference primary/auxiliary states, arbitrary housing displacement/velocity phase with `E_h<=3 E_p,ref/80000=51/20000000` (reference energy uses alpha_ref=0.1).
- For **|alpha0|<=1/25**, all existing positive radial, edge, and 120 housing-anchor strut lengths remain positive for every `u>=0`; each strut length is `>ell0/40`; global nonlinear ODE continuation follows.
- For **|alpha0|<=3/100**, additionally every one of the 20 oriented cell volumes retains reference sign, with conservative ratio bounds `((2/125)^(3/2),(248/125)^(3/2))`, and all struts `>2 ell0/15`.
- No full pulse at alpha0=1/10, no 80% RMS breathing, no half-energy deadline or real hardware criterion is certified.
- The original alpha0=.1 energy-sublevel collision witness is preserved, with no claim it is dynamically reached.

## ASSUMPTIONS / TARGET EXPOSURE
Exact energy bound: `E(u)<=34 alpha0²/5+51/20000000`; `k_min=19/50`, `k_h,min>9/50`; same qualified beta, g, weights, cf, Omega bounds. Ratios 1/25 and3/100 deliberately selected as rational sufficient thresholds, not unique or nature-derived constants; source and 80%/50% engineering targets already inspected.

## REPRODUCIBLE CAPTURE
Source: `experiments/icosahedral-phasewindow-20261022/pulse_safety.py`.
Analysis: `experiments/icosahedral-phasewindow-20261022/PULSE_SAFETY.md`.
Results: `experiments/icosahedral-phasewindow-20261022/pulse_safety_results.json`.
Receipt: `sessions/phasewindow-20261022-gpt6-7c41/pulse_safety_receipt.json`.
Immutable v2 run: `artifacts/phasewindow-20261022-gpt6-7c41/pulse-safety-002/manifest.json`.

RUN: `python3 experiments/icosahedral-phasewindow-20261022/pulse_safety.py --out /tmp/pulse-safety.json`.
Executed local byte-identical source (Git blob SHA b3f3138cd5cf3d9009c27e1ccd075ad3c4ec6f9f) with exact Fraction assertions: PASS.
Second longer Fraction checker: PASS; exact SymPy reference Gram eigenvalues: PASS.
Exact input/output digests captured in run manifest. Constructor self-check, not independent validation.
Repository integrity and tests: awaiting PR CI for new head; do not claim scientific certification.

## NEXT
Highest priority: independently review proof and reproduce source/manifest, then tackle missing forced Green, reference-defect, chart, and nonlinear remainder estimates for the original alpha0=.1, u100 energy ball; PR44 ownership remains separate.
