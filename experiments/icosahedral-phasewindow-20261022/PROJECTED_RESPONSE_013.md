# Moving-pulse projected non-affine tangent audit — calculation 013

**RESULT: NUMERICAL / DEVELOPMENT / OPEN.** This is not a nonlinear all-initial-phase (u=100) theorem.

## Question and provenance

Can the original 3D passive icosahedral α0=1/10 heart pulse amplify housing-phase disturbances into a non-affine shell response (Z=(I-P_0-P_V)Y), where (P_0=11^T/12), (P_V=XX^T/(4R^2)), (R^2=(5+sqrt(5))/8), and (Z) has 24 independent output coordinates? The previously proved exact **equilibrium-linearized** inequality ‖Z_housing,lin(u)‖_F<0.004517 at all times does not apply to nonlinear moving-pulse differences. This experiment directly measures a moving-pulse first derivative in one qualified case.

Verified integrated read-only main: `41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb`. Verified original mechanical source blob IDs (unchanged): `experiments/icosahedral-cone/analyze.py` `da375361c20c089409e84197c720026aadc93c9e`; `free3d/model.py` `c480411dea76a32b0703651744fd66549fc7df4e`; `multiport/network.py` `010629e4239c012048ff3cf49196099e3502eb4f`; `tolerances/hardware.py` `663ee8cd3a059920e3463fd33307d4908f6743d2`; `mountloss/mountloss.py` `aa4ad28348e22733340aad0cde6ae33a633f0b75`; `damping/damping.py` `fbb81690ce70f2ec5b5602f2f7d467bdebd40c27`.

The code is a **standalone constructor reimplementation**, imported from previous nonaffine-011/012 local captures and independently differentiated by a direct analytic Jacobian-vector map. Mechanics and positive energy/damping law are unchanged: 280 configurations/560 mechanical phase coordinates, 13 free 3D primary points, 150 auxiliary coordinates, 30 housings, and 120 current-axis reciprocal viscous struts. Spatial P, L and rigid kinetic energy are retained. Physical ℓ0,E_*,t0 are uncalibrated; no dimensional/spacetime interpretation.

## Exposed fixed case and first-derivative computation

- One deterministic *new* scattered-property case (seed 10422): primary mass, spoke and edge stiffness scatter ±5%; 150 reciprocal-gain scatter ±1%; housing weight scatter ±10%, mean 1. β=0.005, c_f=0, ν=0.05. This is **not** the previously frozen `edge-p1-b0.005-cf0.0` coefficients, and no continuous property-box result is asserted.
- Initial α=0.1, other primary/device positions reference/rest. Housing phase energy `E_h=0.00000241875=(3/2)E_p/40000`; all 180 initial housing displacement/velocity directions are represented by B with energy-orthonormal phase coordinates.
- Integrate full nonlinear reference y_ref'(u)=F(y_ref) and all 180 tangent columns W'=DF(y_ref(u))W, W(0)=B. Analytic DF includes radial/edge spring prestress, auxiliary transmission, moving-housing mount reactions, all current-axis damping geometry, masses, and the heart-to-spoke cross terms.
- At each sampled time (u), form `A(u)=P_Z W_q(u)` with 36 rows (rank at most 24), and compute `sqrt(2 E_h) sigma_max(A)`. This is the maximum **first-order** housing-phase contribution at that time; the sampled combined triangle proxy is `||Z_ref||+sqrt(2 E_h) sigma_max(A)`.
- Select the right singular phase at the largest sampled proxy (post-selection), then run full nonlinear dynamics for that phase and its negative without updating coefficients.

## NUMERICAL results

| Evidence | Observation |
| --- | ---: |
| Full moving-reference/tangent integration | `u=0..100`, 401 time samples |
| Largest sampled first-order proxy (full window) | `0.000538024543824654` at `u=1.5` |
| Reference non-affine norm at that time | `0.000488730537455646` |
| Worst housing first-order contribution at that time | `0.0000492940063690084` |
| Fine `u=0..3`, 601-sample peak | `0.000538309299170763` at `u=1.49` |
| Fine peak / prior `1/40=0.025` threshold | `0.02153237196683052` |
| Coarse vs fine at exactly `u=1.5` | `4.94e-13` absolute proxy difference |
| Analytic JVP vs central finite differences | `<1.3e-8` max absolute (sampled random directions) |
| Original nonlinear zero/+/- phase max `||Z||` over sampled `u<=100` | `0.000503529930740667` |
| Worst selected-phase centered finite difference vs tangent gain | `5.4105e-9` relative |
| Sampled minimum of all struts across those three trajectories | `>0.49159` |
| Max energy+heat normalized balance error | `5.94e-11` |
| Max total spatial P/L drift | `<1.7e-15/<8.7e-16` |

Solver full tangent DOP853 rtol `2e-8`, atol `5e-11`; localized refinement rtol `5e-10`, atol `5e-12`. Finite nonlinearity ± trajectories rtol `3e-10` and atol `3e-12`. These are numerical consistency checks, not validated integration/continuous-time enclosures.

The measured first-order proxy is well below `1/40` *for this sampled case*. This does **not** imply all-phase **finite-amplitude nonlinear** safety: the entire nonlinear flow remainder, full coefficient-box coverage, and continuous-time supremum remain unbounded.

## Reproducibility and status

The immediately downloadable chat archive `UD_3D_projected_response_013_20261023.zip` contains an **actual local immutable-style capture** `projected-response-013/` with 3 full executable source inputs, 11 result/protocol outputs, CSV time series, chosen 180-vector phase (JSON), mathematical receipt, and SHA256 manifest. Its hashes were checked locally. **This archive has not been copied into GitHub's `artifacts/` tree**; the research branch receives this scoped report/receipt/checkpoint, so do not claim repository capture of its executable input/output files.

The source code and numerical integrations were executed locally with Python 3.13, NumPy 2.3.5, SciPy 1.17.0. Repository validator/unittests for this head remain NOT_RUN locally; query PR CI separately. Non-constructor independent mathematical review and hardware experiment NOT_EXECUTED.

The earlier exact low-energy static 3D witness with `||Z||>1/40` continues to defeat any *energy-only* nonlinear global-Z certificate. The stationary linear coercivity theorem remains exact in its **stationary linear** scope. PR44's separately claimed forced-Green recovery task remains held and untouched.

**Next discriminant (priority 98/100):** Establish a validated projected nonlinear difference remainder with full forced Green, state-norm, time/geometry bounds and coefficient-box coverage, beginning with the real frozen low-beta/cf0 case, while preserving the exact 1/40 cell-orientation implication and previously known failures.
