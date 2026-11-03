# UD Discovery — Six-channel u100 stability and conditional continuous-time gate (023)

**RESULT — EXACT / CONDITIONAL interpolation lemma; NUMERICAL / DEVELOPMENT late-time adjoint/forward comparison and velocity-channel screen; continuous-time validated gain, nonlinear u100 phase-ball guarantee and physical identification OPEN.**

## Source, ownership, assumptions

- Repo `ud-tetra/UD-Physics`, integrated main checked `59814ea16e94ac4048dc878ef99d23097ca63b9b`, held 3D claim session `phasewindow-20261022-gpt6-7c41`, research head before work `1b630ebd6829a7016d4d4656666a183625020cbb`; isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
- Read-only primary/multiport/housing/mount/geometry mechanical blobs unchanged; PR44 `integration-icosahedral-greenbounds-20261022` is separately held and not modified.
- Fixed **uniform and symmetric** 3D surrogate reference: 280 generalized coordinates, 560 mechanical phases, heart preparation alpha(0)=.1, beta=.005, nu=.05, cf=0, primary g=1 and k=.4, unit gains and housing weights, reference b(0)=c(0)=1, all other initial velocities zero.
- Housing initial phase perturbation uses energy ball `E_h <= 51/20000000` and 180 energy-normalized initial coordinates. This is a target-exposed design allowance and not a physical energy measurement. Time `u` is uncalibrated mechanical time.
- Exact symmetry (checkpoints 019–021): 60 proper A5 rotations; output Z is 24D, injected housing space 180D, first-order gain reconstructible from six selected adjoint output directions along the symmetric moving reference. This is **linearized only**; nonlinear 180-phase remainder OPEN.

## Operator definitions

Let `P = I_12 - 11^T/12 - VV^T/(4R²)` with `R²=(5+sqrt5)/8`. `C` extracts `Z=P (delta X_shell - delta C)` from the 560-state variation; translation subtraction disappears under P. `C_v` extracts `dZ/du` from the velocity components. `B` injects the normalized 180D housing phase ball so each unit vector `a` corresponds to mechanical initial energy `E_h` after scaling by `epsilon=sqrt(2E_h)`.

For the full tangent propagator `Phi(u,0)` along the **moving** symmetric baseline define:

`L_E(u)=epsilon C Phi(u,0) B`, `D_E(u)=epsilon C_v Phi(u,0) B`.

Exact identities on the positive-length baseline: `L_E'(u)=D_E(u)` and `Z_reference(u)=0`. Set `g(u)=||L_E(u)||_2`, `v(u)=||D_E(u)||_2`. The six-seed A5 reduction reconstructs `g(u)` and `v(u)` from two scalar entries and two 2x2 Gram blocks for any *fixed* time. Symmetry does not guarantee numerical accuracy or nonlinear remainder bounds.

## New late-time comparisons — NUMERICAL / DEVELOPMENT

Reproduced the checkpoint-022 six-output adjoint at u100 with DOP853 and independent fresh runs. The opposite-time cross-check uses the independently integrated **forward** tangent for the right singular vector selected from the u100 six-output map. Both use the same sparse Jacobian and symmetric reference implementation, so this is not an independent constitutive-law check or validated computation.

| Run | Nominal solver rtol | Housing contribution at u100 |
|---|---:|---:|
| Six adjoints | 3e-7 | 4.277830011e-6 |
| Six adjoints | 1e-7 | 4.279958539e-6 |
| Forward selected phase | 1e-5 | 4.277828958e-6 |
| Forward selected phase | 1e-6 | 4.280621959e-6 |
| Forward selected phase | 1e-7 | 4.280822724e-6 |

The forward selected-phase scalar at rtol1e-7 differs from the adjoint rtol1e-7 prediction by ~2.019e-4 *relative*, 0.0202%. The maximum observed cross-run spread is of order 0.07%, not a guaranteed error bar. Attempts to use adjoint rtol1e-8 (180s) and forward rtol3e-8 (110s) exceeded runtime limits and are explicitly marked **NOT_COMPLETED**. The difficulty reflects numerical cost/conditioning, not an observed physical failure. The u4 six-output vs separate full-24-output adjoint gain disagrees relatively by 6.02e-8, using the same tangent assembly.

Peak refinement for the six-channel first-order gain: `g(4.04)≈6.638579048e-5` at rtol1e-7, higher than checkpoint-022's coarse grid `g(4)≈6.600275137e-5`. Additional samples at u=3.9,3.95,4.02,4.03,4.05,4.06,4.07,4.1 were recorded. This establishes **only a higher sampled value**, not a global or continuous-time maximum. A partial 0.5-step scan through u9 did not complete the final two targets; it is an incomplete developmental screen.

For all 180 phases, the derivative-output six-channel calculation yielded `v(1)≈0.000313914`, `v(2)≈0.000481874`, `v(4.04)≈0.000600668`, `v(6)≈0.000578604`, `v(10)≈0.000370526`, `v(20)≈0.000243124`, and `v(100)≈0.000042823`. These are sampled numerical values, **not** a continuous derivative bound.

## Theorem 023A — EXACT / CONDITIONAL continuous-time mesh interpolation

Use the mesh `T=(0,1,2,4,6,10,20,40,70,80,90,100)`. Its largest gap is exactly `30`. Suppose the following two additional premises have been **rigorously validated** for this uniform symmetric *linearized* system:

1. At every mesh node, the true complete 180-phase operator norm satisfies `g(t_j) ≤ 1/10000`.
2. For every real `u∈[0,100]`, the true first-order **velocity** operator satisfies `v(u)=||L_E'(u)||_2 ≤ 1/1000`.

At each time choose a nearest node with `|u-t_j|≤15`. Integrating `L_E'` (operator-norm fundamental theorem of calculus) gives

`g(u) ≤ g(t_j) + ∫_{t_j}^u ||L_E'(s)|| ds ≤ 1/10000 + 15/1000 = 151/10000 = 0.0151 < 1/40 = 0.025`.

If an **additional**, fully trajectory-restricted nonlinear remainder bound `sup_{u,a}||R(u,a)||_F < 99/10000` were proved (including safe housing-strut lengths and verified numerical/reference error), then the total non-affine readout of the symmetric pulse would satisfy `||Z_total||_F < 1/40` throughout u100; combined with checkpoint-010's exact flattening-exclusion implication this would establish positive oriented primary cells for the symmetric uniform-property, full-phase preparation. It would not establish housing-strut safety by itself or the breathing/ringdown performance criteria. **None of the three new premises are certified in checkpoint 023.**

### Margin and explicit remaining proof obligation

Node gate `0.0001` exceeds every **numerically evaluated** archived checkpoint-022 node (max `0.0000660028`); derivative gate `0.001` exceeds every sampled derivative (max among our samples `0.000600668`). The checks do not prove either gate. The math works with the sparse irregular original mesh; no claim that the slope remains small between samples is inferred from the samples. A posteriori defect/interval-ODE bounds on the six adjoints and six velocity adjoints, plus full-time baseline integration enclosures, remain necessary. In addition, nonlinear phase-ball and relative housing-to-anchor distance bounds are separately necessary; the exact static counterexamples in checkpoints 017/019 prohibit replacing them by energy monotonicity alone.

## Checks and source capture

- Executed locally: `six_moving_adjoint.py` u100 rtol3e-7 and1e-7; full-24 adjoint at u4; `forward_transpose.py` u100 rtol1e-5,1e-6,1e-7; several six-seed near-peak runs; `velocity_channels.py` at u1,2,4,4.04,6,10,20 and `velocity_only.py` at u100.
- Executed locally: `envelope_gate_023.py` with `fractions.Fraction`; exact inequalities `151/10000<1/40`, nonlinear spare `99/10000`. Numeric archived-node check is labeled NUMERICAL rather than promoted to a proof.
- Independent tangent implementation: `SparseJacobian.apply` vs `SparseJacobian.adjoint` integrates opposite direction, but shares Jacobian source; not an independent reproduction of model physics.
- NOT_COMPLETED: solver rtol1e-8 u100 adjoint, solver rtol3e-8 u100 forward; partial 0.5-step scan beyond u9; continuous-time validated error enclosure; Hessian/full-phase nonlinear u100 proof.
- Archive stores source, code, failed-run notes, source hashes, results and SHA256 manifest; local hash validation is about reproducibility, not certified mathematical inference.

## Next discriminant — Priority 99/100

Compute rigorously verified bounds for `g(t_j)≤1/10000` and `v(u)≤1/1000` using A5 symmetry-adapted validated ODE/adjoint enclosure with residual defects on the positive-length moving baseline. If those pass, attempt `||R||<99/10000` together with a global housing-to-anchor clearance. Do not modify or claim the separate held Green-bound PR44. No native UD law, hardware calibration, physical clock or mainline promotion.