# Full 3D shell non-affine response: static energy no-go and u≤100 finite pulses

**RESULT: EXACT / CONDITIONAL / FAILED energy-only certificate; NUMERICAL / DEVELOPMENT finite dynamics.**

Session `phasewindow-20261022-gpt6-7c41`; live claim `claims/icosahedral-phasewindow-20261022` remains held; isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Latest inspected integrated main: `a4ae75dd55cd2b691c811c4d6eeae1367fcba015`; original imported primary/port/housing/damping source files are byte-identical to those used for the previous affine certificate. PR #44 Green-bound recovery remains under a separate held claim and was not edited.

## Question

Does the energy inequality alone enforce the proposed condition `||Z||F≤1/40` at original pulse energy? If not, how does the actual full nonlinear three-dimensional icosahedral surrogate behave on representative original-amplitude trajectories through the required time horizon u=100?

The readout is `Z=(I-P0-PV)Y∈R^(12×3)` where `Y_i=X_i-C`, `P0=11^T/12`, `PV=VV^T/(4R²)` and reference shell `V` has `V^T V=4R²I`. Euclidean 3D, reference outer edge length `ell0=1`, continuous dimensionless Newtonian time `u`, uncalibrated materials/energy. `||Z||F` removes translations and reference-affine degrees of freedom; it is not cell volume. All 280 coordinates/560 mechanical phases plus a heat accumulator are simulated without quotient. There are 12 spoke, 30 edge, 150 port and 30 housing positions and 120 current-axis viscous paths. Model constitutive dynamics are assumed as in the source; no physical identification is asserted.

## Exact static obstruction to an energy-only Z bound

Move **one** exterior vertex by `d=(1/25,0,0)`, leaving the other eleven at regular reference positions and the hub at zero. Set the scalar heart coordinate alpha=0, velocities zero, the 150 device coordinates equal to the corresponding port differences `z=G strain`, and the 30 housings at their edge midpoints. All 120 struts remain positive by a coarse triangle-inequality bound.

Because `P0[ii]=1/12`, `PV[ii]=1/4` for every regular vertex, the squared residual is **exactly**

    ||Z||F² = (1/25)² (1-1/12-1/4) = 2/1875 > 1/1600 = (1/40)².

Only one spoke and the five edges incident to the moved vertex change length. Since `R²>(9/10)`, the reverse triangle inequality bounds each spoke strain magnitude by `|d|/R`, every incident edge strain by `|d|`, and other strains by zero. Over **all** allowed spoke g≤21/20 and edge k≤21/50 properties,

    U_primary ≤ 1/2 [(1+21/20)(10/9) + 5(21/50)] (1/25)²
              = 197/56250 < 1/200 < 1360051/20000000 = E_pulse.

Port and housing storage are precisely zero by construction. This is a genuinely 3D static, positive-length **full twelve-vertex network** configuration: **EXACT / FAILED energy-only approach**. It does **not** satisfy the prescribed original-alpha initial preparation, nor establish that the pulse trajectory can reach this low-energy state. It does not contradict the previous exact theorem, which states that a *flattened cell* at low energy needs `||Z||>1/40`; the new witness has no flattened cell. It proves that an invariant region for `||Z||` needs **dynamical information**, not energy alone.

## Model-based numerical tests through u=100

The standalone `nonaffine_audit.py` explicitly reimplements the imported primary elastic forces, 150 reciprocal passive auxiliary-port forces, 30 midpoint mounts, positive masses, current-axis 120 housing loss reactions, spoke/edge friction and Newtonian dynamics. It implements the **canonical source icosahedral vertex and edge ordering** and verifies reference isotropy and the exact projector. This is a constructor reimplementation with source comparisons, not separate empirical replication.

All cases use initial alpha=.1, reference primary/device positions and zero velocity, plus the stated phase when present. Housing energy (if present) equals `Eh=3 Ep/80000` and phase components are normalized in the positive housing mount/kinetic energy metric. Damping nu=.05. The *adverse* case is a fixed seeded (10422) ±5% material, ±1% port ratio and ±10% housing weight scatter, beta=.005 and c_f=0; it is **new** and is **not** claimed to equal any earlier published worst-case coefficient vector. The other cases are uniform properties, beta=.05,c_f=0. Initial housing phase choices: absent; seeded Gaussian direction; or the top right singular vector of the **initial-time linearized 36×180 map from unit phase to projected shell acceleration**. This last choice targets u=0 curvature only, not maximum displacement over u≤100.

DOP853, rtol=2e-9, atol=2e-11, T=100, 1001 sampled times:

| Preparation | Maximum sampled ||Z||F | Worst time | Minimum sampled strut |
|---|---:|---:|---:|
| Uniform, no phase | <6.2e-15 | roundoff | 0.4923411 |
| Uniform, Gaussian phase | 4.1860142e-5 | 1.0 | 0.4921428 |
| Scattered low beta, Gaussian phase | 4.9004399e-4 | 1.5 | 0.4911483 |
| Scattered low beta, top initial-gain phase | 4.9429079e-4 | 1.5 | 0.4915014 |

The initial-gain map's largest singular value is `0.000994018021219` in normalized non-affine-acceleration units; a direct full nonlinear initial-acceleration difference gives `0.000994018022338`, difference `1.12e-12`. Initial energy **includes** the chosen housing phase and nonzero scalar alpha. Max observed energy-plus-heat relative balance residual is `6.64e-10` across these four trajectories. Every listed strut minimum is a **sampled** minimum, not a continuous-time enclosure. Small values of `Z` are not a universal phase-ball guarantee.

The two low-beta cases were additionally computed with DOP853 rtol=3e-11,atol=3e-13 and a doubled 2001-point readout grid. Their maximum sampled `||Z||` changes by `3.8e-12` (Gaussian) and `5.7e-12` (initial-gain). The targeted-phase minimum sampled strut changes due to the finer sampling grid; it is not a nontrivial model instability.

## Independent consistency checks

`verify_audit.py` (another code path, same runtime) checked directional finite differences of total energy against the analytical conservative gradient at perturbed coordinates: absolute error `5.24e-11`. Total spatial force and torque residues across all 13 primary and 30 housing point masses are `2.31e-16` and `1.89e-16`. Energy metric phase normalization, full-12 vertex graph, eight-dimensional projector image, initial-time acceleration singular vector, and exact static witness passed. Source pinning is by Git SHA/blob identifiers listed in `SOURCE_LEDGER.json`; these checks cannot replace execution of original source files and non-constructor independent review.

## Selection, baseline, limits and next discriminant

The threshold 1/40, alpha=.1, original energy ceiling, and performance goal u=100 were exposed. New seeded properties and two phase choices are post-exposure development tests with unquantified selection freedom; do **not** call these independent validation. The null of exact uniform symmetry produces `Z=0`; a permitted static perturbation provides the energy-only counterexample. No freely evolving trajectory was found to exceed 1/40, but four are not exhaustive.

The older exact theorem remains unchanged: cell flattening under the pulse energy ceiling implies `||Z||>1/40`. We have neither an all-180-phase, all-property **dynamic** upper bound on `||Z(u)||` nor a global cell-collapse barrier. No all-time strut-length margin, nonlinear breathing RMS retention, housing ringdown fraction or physical calibration follows from these finite trajectory samples. The 4D branch remains parked. Hardware remains UNSCORED.

**Recommended next discriminant (97/100):** Prove a projected, frame-aware nonlinear Green/variational bound for the 8×3 non-affine response at the low beta,c_f=0 limit, with the full 560-state forcing still included. Test the result against the exact energy-only witness and an optimized phase over the **full time-integrated** Z readout rather than only initial acceleration. Coordinate source/data recovery with PR #44's separate claim without modifying its files. A subsequent validated all-phase `Z≤1/40` theorem combined with the previously proved flattening-implies-Z>1/40 result would certify cell orientation alone—not u100 breathing/ringdown or strut safety.