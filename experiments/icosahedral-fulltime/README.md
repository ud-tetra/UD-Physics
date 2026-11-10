# Full-time 3D icosahedral moving-frame variational analysis — 2026-10-26

**RESULT — NUMERICAL / SAMPLED, COMPLETE EXECUTION:** The frozen 560-dimensional mechanical tangent ODE, with all 180 original housing-phase columns, was integrated from native u=0 to 100 in an isolated GitHub Actions NumPy 2.3.5/SciPy 1.17.0 environment. **EXACT / CONDITIONAL:** a tighter proper-SO3 chart inequality handles reference radius 0.050 and relative displacement radius 0.036. **OPEN:** the true continuous-time nonlinear u100/80%-breathing certificate, full forced Green, uniform flow/remainder and material/source physical identification.

## Frozen provenance and no model changes

Integrated read-only mechanical source \`ud-tetra/UD-Physics@b608e327b9fce95e87172c861985d7e252a8e2aa\`: 280 configuration coordinates, 560 mechanical phase variables plus heat, 13 primary points, 30 housings, 150 auxiliary device degrees and one scalar alpha, with original positive current-axis spring/damping and source housing phase energy Eh=Ep/40000. Use unmodified \`MountLoss.ode\` and \`Linearization.apply\` imported through the existing source \`experiments/icosahedral-pulsetube/jacobian.py\` and \`variational.py\`. The numerical driver \`experiments/icosahedral-fulltime/timeframe_sampler.py\` is **byte-identical** to the source-compatible, previously unexecuted driver from draft [PR #201](https://github.com/ud-tetra/UD-Physics/pull/201); source SHA256 \`cce1ff4fb8ad2d248ab1f28c83743b4955c410bb047bf8a6095e6f08f96936f0\`.

Isolated workflow [run #40373318159](https://github.com/ud-tetra/UD-Physics/actions/runs/40373318159), head \`cea75f2c378c0072826395d3d84613698f6f0f69\`, installed NumPy2.3.5/SciPy1.17.0 into a one-job venv and executed two DOP853 560×180 augmented runs:
- Limiting \`seed10422-0-boundary2\`: source frozen nu=.05, alpha0=.1, fine \`rtol=5e-10\`, tangent atol5e-12, 34,352 RHS evaluations.
- Nominal \`uniform-b0.05-cf0.0\`: same nu/alpha/input family, source original-normal \`rtol=2e-9\`, tangent atol2e-11, 28,892 evaluations.

Each run provided 201 evenly spaced u values with Δu=0.5 and a full 39×180 operator-norm evaluation of both raw and moving-shell-centroid proper-SO3 frame-projected primary tangent. Hub relative-position rotation term is retained. The full numerical JSON sample files are stored in the [GitHub Actions artifact](https://github.com/ud-tetra/UD-Physics/actions/runs/40373318159) (\`icosahedral-fulltime-20261026\`), and were downloaded and SHA256-checked independently in this conversation. Workflow retention is 30 days: do NOT imply the full series are immutable in this Git tree.

## Actual numerical sampled results

| Frozen case | Limiting fine | Nominal normal |
|---|---:|---:|
| Max sampled raw primary position tangent radius | 0.035009719966611536 at u100 | 0.035209379437926326 at u100 |
| Max sampled proper-moving-frame shape tangent radius | **0.0002269454523761407 at u1.0** | **0.00022930815335396365 at u12.5** |
| Max sampled reference displacement from equilibrium | **0.03944037550681534 at u9.0** | **0.046676592620305025 at u64.5** |
| Count of 201 source samples violating older reference d≤0.011 | 145 | 124 |
| DOP853 RHS evaluations | 34352 | 28892 |

Final raw tangent radius matches the **historical immutable source checkpoint** at u100 to absolute 6.94e-18 in each case. Limiting full JSON SHA256 \`d2dc8e35cb8b1f8f54b1acbc168ae93f0a53ce491fd5f193a6ab29f6462be2e2\`; nominal \`be2edff72ba4fa645494b75e078e6d084b69732f330ab4f0ad30f735acccb13a\`; workflow summary \`a9d81fcb925a5af9b039ecf1eb62f4f7d6d1c77e6d814cb400445226fd662ed2\`. The identical summary JSON is captured in the repository's immutable \`fulltime-001\` artifact manifest, but **only** that summary and exact theorem are in the Git tree.

Sampling sensitivity: using every second saved sample (Δu=1) retains the limiting shape maximum but gives nominal shape max 0.0002286184891416114 rather than 0.00022930815335396365, and nominal reference max0.046590265455297576 rather than0.046676592620305025. Thus these are finite sampled extrema, NOT rigorous continuous-time maxima. The comparison is within one computed trajectory; no interval error certification or independent scientific replication.

## Exact tighter moving SO3 chart majorant

The earlier [framechart #187](https://github.com/ud-tetra/UD-Physics/pull/187) used an equilibrium-relative d≤0.036 chart, and [tangent #192](https://github.com/ud-tetra/UD-Physics/pull/192) used a moving chart with reference d≤0.011. Both are too restrictive as uniform assumptions for the present sampled source reference breathing. A **new post-exposure/d=0.05 choice** targets that observed behavior; it is a development design condition and must not be reported as an independently predicted reference bound.

For any time at which the actual reference satisfies \(\|Y_{\rm ref}-Y_{\rm eq}\|_F\le d=1/20=0.05\) and the actual nonlinear primary perturbation satisfies \(\|Y_{\rm actual}-Y_{\rm ref}\|_F\le r=9/250=0.036\), define the shell-centered moving proper-SO3 alignment with \(\Omega\) solving \(G\Omega+\Omega G=2\operatorname{skew}(X_{\rm ref}^\top E_{s,\rm centered})\), \(G=X_{\rm ref}^\top X_{\rm ref}\). Both the shell and reference hub are rotated. The exact chart-remainder proof uses:
- \((5+\sqrt5)/2>18/5\), \(\sqrt{(5+\sqrt5)/2}<191/100\), \(\sqrt{3(5+\sqrt5)/2}<331/100\).
- \(\sqrt{13/12}<25/24\), \(1/\sqrt2<71/100\).
- \(G_{\min}\ge18/5-2(191/100)d-d^2=6813/2000\).
- \(\|\Omega\|_{\rm op}\le t=6958/473125<1\).

Then by the matrix exponential tail and submultiplicativity, uniformly on that primary error ball,
\[
\boxed{\|\mathcal F_{\rm ref}(E)-D\mathcal F_{\rm ref}(0)E\|_F
\le\frac{245802834179}{264666314250000}
\approx0.00092872731<0.001.}
\]
This is a true **EXACT / CONDITIONAL chart theorem**, checked with standard-library exact Fractions in the locally executed \`chart_bound.py\`, source SHA256 \`803e4d09401c350211b8552085001bbc764e11b837631946a80bb26f2e8bc3f5\`, output SHA256 \`68a9b2c9fb690c28224c608b8386b0b0ea86fde777303d7f0d316c9755487214\`. It neither certifies a continuous reference bound nor bounds the actual nonlinear phase perturbation.

The MAX SAMPLED nominal raw tangent radius .0352093794 leaves only .0007906206 margin to the *hypothesized* r=.036 nonlinear relative-domain ball, before any finite-flow remainder/ODE integration error. That narrow margin is why a true nonlinear-flow bound remains the decisive next gate.

## Scientific status, null and open dependencies

The properly aligned 3D geometric response is a generic ordinary unanchored reciprocal spring/dashpot network result; it is **not** a unique UD-to-spacetime bridge, nor an independent material or damping prediction. This branch operates only on the established *hypothetical 3D mechanical model* with source-chosen, uncalibrated parameters.

COM rigid translation was proved exactly over all time in [prior PR #201](https://github.com/ud-tetra/UD-Physics/pull/201); it remains in the 560-state dynamics and positive mechanical energy. Current numerical samples cover the projected initial-phase response \`U(t,0)B\`, but NOT the full forced operator \`U(t,s)\`, a validated whole-time reference enclosure, nonlinear Hessian, finite-amplitude phase-ball flow remainder, positive 120-member strut domain or nonlinear 20-cell oriented-volume determinant. A 201-point time grid with DOP853 tolerance is not a validated interval bound. The existing 80% breathing claim thus remains **OPEN**, not proven.

**Reproducibility:**
- Source sampler: \`python3 experiments/icosahedral-fulltime/timeframe_sampler.py --case seed10422-0-boundary2 --horizon 100 --step .5 --rtol 5e-10 --atol 5e-12 --out limiting.json\`; similarly nominal original tolerance.
- Exact chart: \`python3 experiments/icosahedral-fulltime/chart_bound.py --out chart_bound.json\`.
- [Pinned isolated workflow](../../.github/workflows/icosahedral-fulltime-20261026.yml) and [original run #40373318159](https://github.com/ud-tetra/UD-Physics/actions/runs/40373318159) retain full execution provenance; actions artifact expires after 30 days.
- [Immutable fulltime-001 manifest](../../artifacts/ico-fulltime-20261026-gpt6-a1/fulltime-001/manifest.json) captures inputs with checksums and full summary+theorem bytes. The archived full samples remain outside Git in the workflow artifact.

**NEXT (priority 99/100):** run frozen sample-spacing/integration-tolerance sensitivity and **nonlinear finite-amplitude adverse-phase trajectories** against the sharp ~.00079 domain margin; obtain interval/a-posteriori full-time reference and relative-position bounds, forced Green and Hessian/remainder/length/volume verification before claiming the 80% all-phase nonlinear certificate. External non-constructor mathematical review and physical hardware test remain NOT_RUN / NOT_EXECUTED, and no mainline physical promotion is authorized.
