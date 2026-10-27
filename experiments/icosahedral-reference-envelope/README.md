# Continuous-time primary reference radius: energy-velocity intersample lemma

**RESULT — EXACT / CONDITIONAL analytical interpolation; NUMERICAL 2,001-point frozen reference sampling; OPEN validated numerical error and full 180-phase nonlinear tube.** The original 560-state 3D icosahedral mechanical dynamics, masses, 120 housing struts, 20 oriented volumes, dampers, heat, and source parameters are unchanged.

## Mission, typed source and evidence

Question: can the entire unforced breathing-reference displacement from the equilibrium primary geometry remain below **d=0.070 for every native time u in [0,100]**, as needed by the revised moving SO3 chart in the earlier separate [nonlinear radial PR #219](https://github.com/ud-tetra/UD-Physics/pull/219)? The source is the integrated 3D code at \`ud-tetra/UD-Physics@cba74cc20ba323599339f88830bd0cc97fc9a6da\`, with original \`experiments/icosahedral-pulsetube/jacobian.py\`, \`variational.py\`, \`icosahedral-mountloss/mountloss.py\` and \`icosahedral-tolerances/hardware.py\`. Prior PR #219's eight selected nonlinear housing-phase results and d=.070 chart theorem are read-only and are **not** integrated dependencies. No rewrite of other 3D, 4D, QPB, quantum or circuit tasks occurred.

The two frozen cases are \`seed10422-0-boundary2\` and \`uniform-b0.05-cf0.0\` with nu=.05, source initial alpha=.1, 13 primary spatial masses \(m_i>0\), 30 housing masses, and unforced reference \`yref(0)=MountLoss.initial_augmented(.1)\`. Their native reference initial total mechanical energy \(E_0\) is the source actuator energy \(E_p=(1+\sum g_i)(.1)^2/2\). Native mechanical time u=t/t0, lengths ell0 and energy E* remain **uncalibrated** physical parameters, not SI predictions.

## Exact conditional energy-speed lemma

The imported mechanical energy is the sum of nonnegative strain/port/mount potentials, kinetic terms and positive housing energy. Dissipative forces use relative velocities and transfer nonnegative work into the heat accumulator. For any true source reference solution in the positive member-length domain with no external work,
\[
0\le E_{\rm mech}(u)\le E_0,\qquad
\tfrac12m_{\min}\|\dot Y_{\rm primary}(u)\|_F^2
\le \tfrac12\sum_{i=1}^{13}m_i|\dot y_i(u)|^2
\le E_{\rm mech}(u),
\]
where \(m_{\min}=\min_i m_i\). Therefore a **uniform speed bound valid at every time**, including between numerical output samples, follows:
\[
\boxed{\|\dot Y_{\rm primary}(u)\|_F\le V_{\max}:=
\sqrt{2E_0/m_{\min}}.}
\]
Let \(0=u_0<\cdots<u_N=100\) be a uniform mesh with \(\Delta u\). For each u choose the closest mesh endpoint \(|u-u_j|\le\Delta u/2\), integrate speed, and use the triangle inequality. If \(Y^{\rm num}_j\) approximates the **true primary reference position** at u_j with uniform numerical position error at most \(\delta_{\rm num}\), then
\[
\boxed{
\sup_{u\in[0,100]}\|Y_{\rm ref}(u)-Y_0\|_F
\le D_{\rm sampled}+\frac{\Delta u}{2}V_{\max}+\delta_{\rm num},\quad
D_{\rm sampled}:=\max_j\|Y^{\rm num}_j-Y_0\|_F.}
\]
This is an **EXACT / CONDITIONAL** theorem, requiring source energy positivity, true reference existence, correct mesh and a **separately certified** global sample error \(\delta_{\rm num}\). Its continuous-time component is proved by analysis, not extrapolation of the sample curve. Merely setting \(\delta_{\rm num}=0\) because SciPy solves accurately is **not permitted**.

## Actual execution and numerical budget

The isolated [GitHub Actions run #40569925956](https://github.com/ud-tetra/UD-Physics/actions/runs/40569925956), head \`efb1fd11cf097382b682ad1bbd116ae6e9139b79\`, installed pinned NumPy2.3.5/SciPy1.17.0 and executed original \`MountLoss.ode\` for both frozen reference cases with two solver tolerances, DOP853 \`rtol=2e-11 atol=2e-14\` and \`rtol=5e-12 atol=5e-15\`. Exactly **2,001** samples u0..100 at \(\Delta u=0.05\) were evaluated in each tolerance run. No housing input directions were added because this test targets the **reference trajectory only**. The same source energy \(E_p\), primary masses and dissipative heat law were used.

| Native quantity | Limiting frozen case | Nominal frozen case |
|---|---:|---:|
| \(E_0\) | 0.06480831348069511 | 0.06500000000000003 |
| Minimum primary mass \(m_{\min}\) | 1.0629793373048022 | 1.105572809000084 |
| Analytic speed cap \(V_{\max}\) | 0.34919494364153736 | 0.34290830353663304 |
| Max sampled reference displacement \(D_{\rm sampled}\) | 0.05039240841022644 at u9.25 | 0.05111635138364076 at u9.20 |
| Conservative intersample allowance \(\Delta u V_{\max}/2\) | 0.008729873591038434 | 0.008572707588415826 |
| Conditional bound if sampled states were exact | **0.059122282001264875** | **0.05968905897205659** |
| **Allowed verified sample numerical error \(\delta_{\rm num}\) before d=.070 fails** | **0.01087771799873513** | **0.010310941027943417** |
| Difference between two DOP853 position arrays | 1.1144678127869183e−12 | 1.2101084363643354e−12 |
| Strict-tolerance RHS evaluations | 49,493 | 53,345 |

The source reference peak u9.20 in the nominal case is marginally larger than the earlier 0.25-grid u9.25 peak. A 0.25-grid speed-based upper bound is about .094, too loose for d=.07. A 0.05-grid speed-based upper bound leaves a positive **global numerical-error budget of at least .01031**. The two-tolerance solver agreement is a reproducibility/sensitivity indication **only**: it does not establish \(\delta_{\rm num}\le 1.21\times10^{-12}\) or prove any other global numerical error bound.

Thus the source reference side of the revised SO3 chart condition is **CONDITIONALLY CERTIFIABLE** given a validated numerical reference position error smaller than the explicit budget. **It has not yet been certified.** This narrower dependency may be substantially easier than bounding the full nonlinear 180-phase housing ball, but solving it does not establish the latter.

## Null baseline, other missing prerequisites, next discriminant

Energy-to-speed interpolation is standard continuous-time mechanics and applies equally to an ordinary reciprocal local 3D spring/dashpot model with the same masses and energy law. It cannot distinguish UD from classical mechanics, derive physical time/length scales, establish a local spacetime metric or certify an independent empirical result.

The complete nonlinear source robustness theorem still needs an independently validated sample error \(\delta_{\rm num}\), the **full180-dimensional finite-amplitude nonlinear relative primary radius r=.036**, the forcing-projected 560-state full Green \(U(u,s)\), source Hessian/nonlinear flow remainder, 120 strictly positive housing strut domains and 20 oriented cell volume bounds, and the u100 80% breathing retention criterion. Eight selected numerical housing directions from PR #219 are **not** a full ball enclosure.

**Highest-value next action (priority 99/100):** obtain an a posteriori validated global ODE error \(\delta_{\rm num}<0.01031\) for the unforced reference samples using source Jacobian, reconstructed dense-output residual, a verified Lipschitz/variational Green bound and appropriate interval/matrix precision; freeze the reference proof. Independently pursue the much more difficult forcing-range projected Green and nonlinear phase-ball remainder, without claiming closure from finite trajectories.

## Reproduce and artifact status

Complete numerical checkout command:
\`OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-reference-envelope/reference_envelope.py --step .05 --out envelope.json\`

Actual GitHub workflow uses the pinned numerical venv and publishes a full \`envelope.json\` in Actions artifact id **12765172127** with 30-day retention. The file was downloaded and SHA-256 verified against the workflow's printed checksum. An identical full JSON output and executed original program are captured under immutable [reference-001](../../artifacts/ico-ref-envelope-20261027-gpt6-a1/reference-001/manifest.json). Source SHA256 \`408f6aeba43ca08df22a2d288b65def8d4206e5b84d01ffd085b227c8f1cd6f5\` (4,230 bytes); result SHA256 \`13f126c8a2ea8aab5ba47c4923b70d74929b06f9522f32e897cf8eb871e57040\` (2,992 bytes).

Independent scientific reviewer NOT_RUN, physical hardware/experiment NOT_EXECUTED, no mainline writeback or physical promotion. The result is an exact mathematical intersample lemma plus numerical frozen-reference data, NOT a finished u100 nonlinear certificate.
