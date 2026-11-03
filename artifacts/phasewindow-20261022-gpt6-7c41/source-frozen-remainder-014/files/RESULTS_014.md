# Source-matched projected non-affine remainder audit — run 014

**RESULT — NUMERICAL / DEVELOPMENT; EXACT provenance hash; all-phase nonlinear theorem OPEN.**

## Question

For the original UD passive 3D MountLoss 280-configuration / 560-mechanical-phase surrogate with heart preparation `alpha0=0.1`, how large is the *finite nonlinear* error in the projected 24-dimensional non-affine shell readout after subtracting the moving-reference first derivative for an adverse, already exposed, low-housing-mass / zero-friction parameter set?

## Source, space and readout

The chosen coefficient set is **`edge-p1-b0.005-cf0.0`**, retrieved from integrated `ud-tetra/UD-Physics` at source revision `1e6e0f2abe3fa234919c5a6701547883a807b3e5`, `artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/cases.json` (Git blob `419230bb31596cb75b4de2dddd47b281fa02fa47`). We reconstructed all 13 masses, 12 radial strengths, 30 edge strengths, 150 alternating reciprocal ratios and 30 housing weights; SHA-256 on the original coefficient normalization equals **`8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`**. `frozen_case.json` deliberately uses two-element alternating arrays expanded 75/15 times, so coefficient identity is machine checked on every run. The earlier checkpoint 013's independent scattered case is a different, post-exposure synthetic pattern; its gain may not be called a verification of this source case.

Physical positions are 13 free Cartesian primary points (centre and 12 exterior), 30 finite-inertia housings, 150 device coordinates and scalar alpha. The six rigid spatial directions and all housing velocities are retained. Physical time is independent continuous dimensionless `u`, length `ell0=1`, energy `E*`; no empirical mapping or physical calibration is assumed. Readout `Z(u)=(I-P0-PV)Y(u)` takes the 12 exterior positions in R3 and removes the constant and reference-affine vertex subspaces. It is a **24-dimensional** subspace written in 36 Cartesian components. The prior exact conditional flat-cell theorem states that under total primary energy <= `1360051/20000000`, any flattened cell must satisfy `||Z||_F>1/40`.

The model is the previously audited standalone complete reciprocal force law, with 120 moving-axis strut dampers, parameter `nu=0.05`, `beta=0.005`, `cf=0`; initial heart alpha=.1, primary/devices reference/rest. Added housing energy is **`E_h=2.430311755526067e-6`** (`1.5 Ep/40000` for the frozen case). Initial perturbation direction `a` is normalized using the true housing position/velocity energy metric in R180.

## Calculations actually executed

1. Verified exact source **coefficient SHA-256** in `source_case.py`. `MovingTangent.apply` differentiates all 560 mechanical right-hand-side coordinates, including the derivative of current-axis viscous reactions; directional finite-difference force check discrepancy **`1.2765e-8`**.
2. Attempted complete **180-column** source-matched propagation through `u=100` twice; the compute job timed out **before results**. This failed computational attempt does not negate prior checkpoint 013's 180-column result for another source pattern, and does not supply an all-180 gain for this case.
3. Ran a declared, explicitly *smaller* eight-direction subspace: one initial-acceleration SVD direction and seven frozen RNG seed `20261023` unit-energy directions. Propagated all 560 reference states plus eight 560-component first derivatives over 401 samples in `u∈[0,100]` using DOP853, `rtol=2e-9`, `atol=3e-11`.
4. Selected the direction that maximized **sampled** `||Z_ref(t)+eps W_Z(t)a||` among those eight directions. The selected index is **6**, at `u=4`; maximum projected first-order response **`0.0003726089188233788`**. Source-matched reference pulse has maximum sampled `||Z||=0.000370606147600837`.
5. Integrated the selected phase and its sign reversal at the complete energy budget, and at half the **amplitude** (one quarter housing energy), together with the zero-disturbance reference. The finite replay used DOP853 `rtol=2e-9`, `atol=2e-11` at 401 samples through `u=100`. A full phase means displacement/velocity initial vector `epsilon B a`, with `epsilon=sqrt(2E_h)`. The nonlinear remainder is the *vector* `R(t,a)=Z(t,a)-Z_ref(t)-epsilon W_Z(t)a`.

| Observable (401 sampled times) | Value | Evidence |
| --- | ---: | --- |
| Largest first-order selected among eight directions | 3.726089188e-4 | NUMERICAL |
| Largest finite ||Z|| among reference / selected ± / selected ±half | 3.726090630e-4 | NUMERICAL |
| Max ||R(t, ±a*)|| at full phase | 2.937333690e-9 | NUMERICAL |
| Max ||R(t, ±a*/2)|| at half phase | 7.343383853e-10 | NUMERICAL |
| Half/full remainder ratio | 0.25000169 | NUMERICAL |
| Smallest sampled housing strut length | 0.4914351493 | NUMERICAL |
| Worst relative energy-plus-heat discrepancy | 3.2771e-10 | NUMERICAL |
| Maximum spatial P/L drift | 1.7272e-15 / 8.4545e-15 | NUMERICAL |
| Exact earlier orientation threshold | 0.025 | EXACT / CONDITIONAL |

The ratio `~1/4` is compatible with a leading quadratic Taylor term **along this selected direction**; no global Hessian supremum is inferred from it. The finite error is much smaller than the orientation margin for this one case and phase.

An optional tighter `rtol=3e-11` five-run replay was attempted but exceeded the compute window after the reference and two full-phase signs. Those three completed integrations reported largest finite Z changes below `2e-12` and relative balance errors below `5e-12`; the entire refined five-run remainder and verified integration-error enclosure are **NOT_AVAILABLE**. Solver tolerances and energy balance do not themselves bound true solution error.

## Exact scope and negative results

The previous exact energy-only witness has `||Z||>1/40` for a static admissible 3D configuration at energy far below the heart-pulse budget. This **refutes energy-only control** of the non-affine threshold but is not reachable-trajectory evidence. Our new directional data are not an energy-only theorem and do not contradict the witness. The previous exact `U_primary,lin>=||Z||²/8` controls **equilibrium-linearized housing perturbations**, not the full moving-pulse nonlinear remainder.

No global `u=100` bound follows for all R180 phases from eight test directions, and no continuous property-box or continuous-time numeric/ODE error enclosure is claimed. A moving-pulse full-180 source-matched gain, validated forced Green operator, uniform second-derivative/geometry bounds and positive strut-domain continuation remain OPEN. PR #44 owns related forced-response recovery and was not modified. No independent empirical experiment or material/clock calibration was executed.

## Reproduction and checkpoint

From a directory with `frozen_case.json`, `source_case.py`, `nonaffine_audit.py`, `projected_tangent.py`, `finite_check.py`, `run014_small.py`, `replay014.py`, run:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 source_case.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 run014_small.py --out stage --T 100 --samples 401 --tangent-only
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 replay014.py --input stage --out stage --rtol 2e-9
```

`stage1_summary.json`, `summary.json`, full sampled CSV and selected phase are in the capture; the full stage1 binary `tangent_cache.npz` is preserved in the **local ZIP**, and is deterministically regenerated by the first command before finite replay. Source SHA and output bytes are preserved with a schema-2 immutable manifest. Constructor checking and repeated same-runtime computations are not independent replication.

**NEXT (priority 98/100):** seek a time-dependent *full-180* source-case projected gain via scalable adjoint/block computation and validate the forced nonlinear remainder over an invariant domain. Separate initial housing perturbation energy, baseline pulse, and genuinely unused validation data. Do not claim u100 all-phase safety before both linear gain and uniform nonlinear remainder are bounded.
