# Symmetry channels 020 — source-verified Discovery checkpoint

**EXACT / CONDITIONAL** for exactly uniform 3D icosahedral parameters and the globally safe moving symmetric baseline of checkpoint 019. **NUMERICAL / constructor checks** at initial time. **OPEN** for the full nonlinear u100 180-phase ball.

- Source: integrated read-only main `407fe6da298ea3362886075fdd696bf1dfefd2fb`; model/network/damping/hardware/mountloss/cone source blobs SHA-identical to prior baselines.
- Claim: `icosahedral-phasewindow-20261022` held by `phasewindow-20261022-gpt6-7c41`; branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
- Exact group enumeration: 60 proper A5 rotations in Q(sqrt5); classes 1,15,20,12,12; all 12 reference vertices and 30 edges verified. Algebraic source: `experiments/icosahedral-phasewindow-20261022/a5_exact_rotations020.py`.
- Exact character result: `Z24=3+3prime+2*4+2*5`; `H180=2*1+10*3+10*3prime+12*4+14*5`. All-time *linear* response output Gram: two scalar gains and two real PSD 2x2 matrices; source `experiments/icosahedral-phasewindow-20261022/a5_exact_channels020.py`.
- Exact symmetry-permitted nonlinear Hessian map dimension `6516`; nonlinear remainder not bounded by symmetry.
- Constructed full560-state signed-auxiliary A5 covariance check, all 60 rotations, max absolute residual `2.89e-14` (NUMERICAL). Uniform initial acceleration full180 map max intertwinement error `4.07e-20` with top singular response `0.0009605640670680957` at u=0 only (NUMERICAL). Not a u100 propagator bound.
- Corrected first benchmark attempt: isotypic projector rank checked on raw 36 shell components instead of after the rank24 nonaffine projection. Final output ranks 0,3,3,8,10 are reproduced.
- Complete local ZIP `UD_3D_A5_Symmetry_Channels_020_20261024.zip`, SHA256 `7fe3152a50cb91c837bacdeb695828ecc9a0abbe3fe0bbb3d6533ef69109d02e`. Four scripts replayed byte-identically from a fresh ZIP extraction, with schema2 manifest, four outputs, receipt and source ledger. Full ZIP **not** represented as a complete repository artifact tree.
- Detailed theorem and all limitations: `experiments/icosahedral-phasewindow-20261022/SYMMETRY_CHANNELS_020.md`.
- Next priority 99/100: construct six symmetry-adapted adjoint seeds and validate the resulting linear u100 block gain; then bound nonlinear housing-relative deformation and its domain. Scattered coefficients destroy A5 and need separate perturbation treatment. PR #44 untouched.

No mainline writeback, physical identification, material certification or full nonlinear u100 claim.
