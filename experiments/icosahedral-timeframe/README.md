# Exact full-time Galilean block of the 3D icosahedral Green operator

**RESULT — EXACT / CONDITIONAL** global translation subsystem for all 0<=u<=100 and the entire frozen 180-dimensional housing-phase energy ball. **NUMERICAL** full 180-column archived endpoint crosscheck. **OPEN** full time-dependent 560x180 shape/rotation integration, nonlinear forced Green, flow remainder, and all-phase u100 certificate.

## Source and constraints

Read-only mechanical source \`ud-tetra/UD-Physics@447ee4df3b9bc3e71bdfee3e29f7ee9379410df7\`, particularly \`experiments/icosahedral-mountloss/mountloss.py\`, \`experiments/icosahedral-tolerances/hardware.py\`, \`experiments/icosahedral-pulsetube/variational.py\`, and the original \`compact_checkpoints.npz\` archive. Original 280 configurations, 560 mechanical phase variables, 13 primary point masses, 30 housing point masses, 150 device coordinates, alpha, reciprocal internal forces/dashpots and housing phase energy \`E_h=E_p/40000\` are retained. Unmerged prior PRs #187 and #192 are cited read-only, not integrated task dependencies. No material law, damping, source, geometry or target changed.

## Exact full-time subspace and norm obstruction

The source is unanchored and all spatial spring/viscous reactions are internal equal-and-opposite functions of relative positions/velocities. Therefore for the mass-weighted center of mass of all 43 point masses, exactly \`M Rcm''=0\` on every interval where the nonlinear dynamics exist. Comparing any two source solutions:
\[
\delta R_{\rm cm}(u)=\delta R_{\rm cm}(0)+u\,\delta V_{\rm cm}(0).
\]
The 3 spatial Galilean translation blocks of the full state variational propagator are each \`S(Delta)=[[1,Delta],[0,1]]\`, and its exact ordinary Euclidean 2-norm is \`(|Delta|+sqrt(Delta²+4))/2\`. At Delta=100 the full 560-state propagator's operator norm is **at least** \`50+sqrt(2501)≈100.009999\` when equal native position and velocity Euclidean weights are used. This prevents a blanket contractive positive full-state **raw** norm claim. For other positive norms, explicit equivalence factors are required. It does NOT mean mechanical/shape instability, because translation is a free rigid symmetry.

## Sharp all-phase center-of-mass response and archive crosscheck

The frozen initial housing energy ellipse is \`(1/2) sum_j m_hj[Omega²|deltaHj|²+|deltaVj|²]<=E_h\`, Omega=10, primary initial errors zero. The exact all-phase bound, sharp by aligned Cauchy extremizers, is
\[
\sup_{\rm housing\,phase}|\delta R_{\rm cm}(u)|=
\frac{\sqrt{2E_h M_h}}{M}\sqrt{u^2+\Omega^{-2}}\quad(u>=0).
\]
It is valid at every u, and monotone through u100. The source uses \`m_i=m_i^(source)/R²\` and \`m_hj=.4 beta w_j/R²\` with beta=.05 and \`R²=(5+sqrt5)/8\`. Applying the **existing** limiting/nominal masses and energies yields at u100:

| Readout | Limiting | Nominal |
|---|---:|---:|
| Total point mass | 15.1759533484 | 15.0357902024 |
| Total housing mass | .6633436854 | .6633436854 |
| Exact all-phase center-of-mass displacement bound | .00966081790 | .00976528539 |
| Uniform translation contribution to 13-point Frobenius radius | .03483257430 | .03520923719 |
| Archived raw primary tangent operator norm | .03500971997 | .03520937944 |
| Primary residual after removing **only** global CM translation | .03150001927 | .03156386903 |
| Proper moving-SO3 aligned primary shape tangent | .00009867394 | .00016894761 |

**Do not subtract or interpret these operator norms as scalar components of the same maximizing phase.** After CM subtraction the large residual indicates rotational and other rigid-frame effects remain; proper orientation-alignment is essential. None of the above is a measured physical response or a nonlinear flow bound.

The new \`tests/test_icosahedral_timeframe_20261025.py\` ran on [GitHub Actions 40216245891](https://github.com/ud-tetra/UD-Physics/actions/runs/40216245891) using the read-only archived 560x180 final tangent. It verifies **all 3x180** mass-weighted COM derivative columns against the exact initial housing injection formula: max absolute discrepancies 1.15e-11 limiting and 1.72e-11 nominal, with source solver numerical error. The original archive is unchanged; 560 dynamical variables and all 180 input directions are retained.

## Execution limitations, reproducibility and next step

The initial [runner capability test](https://github.com/ud-tetra/UD-Physics/actions/runs/40215676829) establishes that default GitHub CI Python3.12 lacks **NumPy and SciPy**. The local Python container has NumPy and SciPy, but lacks a complete authenticated repo/archived binary download due DNS restrictions. Thus the original 560x180 **time-dependent augmented DOP853 integration was NOT_EXECUTED** in this run. The source-compatible \`timeframe_sampler.py\` was syntax-checked locally and committed as a clearly **UNEXECUTED** numerical workload that invokes the original source m.ode/Jacobian and samples a moving-reference frame along u in a complete SciPy/NumPy repo. Its outputs, if executed later, would be sampled NUMERICAL development data, not interval-certified Green or nonlinear all-phase results.

Executed locally:
\`python3 experiments/icosahedral-timeframe/rigid_green.py --out /tmp/rigid_green.json\`
The exact source (SHA256 \`904ab54b485e95661c23723e5405aece99874409095080100426444573a27f36\`) and **full locally executed result** (SHA256 \`d719e9868ca641d365fbfd031f589b422c626412d3f4235ad6ab5bf24d408efe\`) are captured under [immutable timeframe-001](../../artifacts/ico-timeframe-20261025-gpt6-a1/timeframe-001/manifest.json). They were compared byte-for-byte through Git blob SHA1, not merely copied from summary text.

**Conventional null:** Every ordinary unanchored reciprocal spring/dashpot point-mass model has the same center-of-mass shear. The exact result advances mechanical robustness bookkeeping but does **not** select UD-specific damping/strength, spacetime geometry, SI time/length, or physical charge. No independent peer review/hardware experiment.

**NEXT (priority 99/100):** run the unchanged 560x180 variational ODE on a SciPy-capable full checkout with the provided sampler, record full-time moving-frame shape/rotation and reference signals, then certify forced \`U(t,s)\` over the relevant force range, nonlinear Hessian/flow, reference defect, continuous strut-domain and oriented-volume readout. Keep rigid CM energy and position in a positive block norm; do not claim u100 nonlinear all-phase 80% breathing until every premise closes.
