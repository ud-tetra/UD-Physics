# Handoff checkpoint — nonlinear dimensional discrimination

Time (UTC): 2026-10-22T21:23:08.775683+00:00
Session: `icosa4dvol-20261022-gpt6-c7d2`; claim ref `refs/heads/claims/icosahedral-4d-volume-20261022` held at `23b04a0533df0bd6b26f0c7fc9f94a6864400cea` before run; isolated branch remains the PR #39 branch.
Original integrated base `92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`; source prior run retained; this is new run `nonlinear-003`, not a modification of earlier immutable artifacts.

EXACT/CONDITIONAL: 4D apex radial length is identical to ordinary 3D planar guided-carriage spring length for every `(s,z)`, making complete reduced nonlinear Lagrangian, damping and shell-volume readout identical. Distinct physical localization is not established. Numerical static third-order force response: -0.2927050983 f + 1.1542424192 f² - 10.4233658800 f³. Negative-height/positive-height fold concerns are distinct from physical time. Positive-height static branch has a fold at -0.05258752206 in the nominal units. Numerical pulses (6 signed amplitudes) and finite-time free-mode frequency checks (4 amplitudes) match 3D analogue to numerical tolerance. Simpler 3D linear null differs nonlinear; it cannot identify dimension.

Target exposure: equal-edge target selected earlier; 3D comparator built deliberately to match it, not independent prediction. `a=k_r=k_e=m_s=m_a=1`, damping `0.06M`, pulse shapes and amplitudes illustratively chosen, no physical fit. Exact proofs only inside declared toy model. 

Run reproduce with `python3 nonlinear_audit.py`. Requirements sympy 1.14.0, numpy 2.3.5, scipy 1.17.0. Source/input hash and outputs in `artifacts/icosa4dvol-20261022-gpt6-c7d2/nonlinear-003/manifest.json`. Script self-assertions and py_compile PASS; repo validation/test suite NOT_RUN; no independent empirical replication. No mainline export or `state/CURRENT.md` edits.

Next: examine admissible local-isotropic reciprocal 3D networks and full unconstrained shell/apex sectors, report discriminating observables or document a revised no-go. Priority 97/100. Claim remains HELD; PR #39 remains DRAFT until integrity review.

CORRECTION: invalid `nonlinear-002` attempt missing `source_path` metadata (GitHub Actions 39857539810 FAILED); its files were withdrawn from the PR tree but retained in Git history. `nonlinear-003` re-captures unchanged code/data with valid repository `source_path`. New CI must validate this head; no physical verification.


CI UPDATE: Corrected `nonlinear-003` passed Discovery integrity at head `0c0505f990cf4488a672f9d9d25cf61a032adc3e`, run `39858108061`: `scripts/validate.py` PASS 85 records and `unittest discover` PASS 16 tests. Integrity checks cannot prove a physical 4D identification. Review status DRAFT / held claim; no mainline export.
