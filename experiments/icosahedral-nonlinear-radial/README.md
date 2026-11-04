# Nonlinear radial stress and moving-frame domain audit — 3D icosahedral passive mechanics

**RESULT — NUMERICAL / SELECTED PHASES:** The original source 560-dimensional nonlinear mechanical ODE, including all 13 primary points, 30 housing points, 150 internal devices, rigid momenta and heat, was executed for eight source-energy-ball finite housing-phase preparations and their frozen reference trajectories through native u=100. At 401 sampled time points all eight selected relative-primary displacement traces satisfy r=0.036, with positive housing strut lengths and oriented cell volumes. **FAILED prior d=0.05 moving-frame antecedent:** denser reference sampling finds peaks above 0.05 in BOTH source cases. **EXACT / CONDITIONAL chart repair:** changing the *assumed* reference radius to d=0.07 gives alignment chart remainder <0.001 if the actual nonlinear relative radius remains ≤0.036 and the reference radius ≤0.07 continuously. **OPEN:** the whole 180-dimensional housing energy ball, validated continuous-time maxima, full forced Green/Hessian/remainder, 80% breathing certificate, material measurements, and unique UD mechanism.

## Firewalled read-only source and test choices

Integrated source: \`ud-tetra/UD-Physics@360b72d751934eed428df9b7f89358d9260bbcad\`, full source \`experiments/icosahedral-pulsetube/\`, \`icosahedral-mountloss/\`, frozen numerical checkpoint \`compact_checkpoints.npz\` from the integrated \`pulsetube-001\`. The \`jacobian.py\`, \`variational.py\`, \`mountloss.py\` and compressed checkpoint SHA1 blobs were **verified identical** between original \`447ee4df3b9bc3e71bdfee3e29f7ee9379410df7\` and current base. Earlier draft PR #206 provided a frozen full 560×180 tangent source run with sampled maximal aligned sensitivities around .000229 and reference .04668 on Δu=.5. Those are read-only. No direct changes to prior 3D source, mainline, 4D, QPB, JJ or quantum branch.

This test targets the *most dangerous raw endpoint primary displacement* and is therefore **target-exposed exploratory testing**, not heldout validation. For each source case, load its 560×180 final tangent W(100) and 560×180 initial housing injection B from the read-only checkpoint. Obtain a unit housing phase v from the leading right singular vector of W(100)[1:40,:]; select a deterministic overall sign. Initialize the unchanged mechanical ODE with \`y0[:560] += a sqrt(2Eh) Bv\` for amplitudes \`a=-1,-0.5,+0.5,+1\`, with \`Eh=Ep/40000\` and frozen alpha0=.1, nu=.05, beta=.05, source case coefficients. Integrate a separate reference yref from unchanged initial y0 using the SAME solver accuracy.

DOP853 in isolated CI [run #40554459813](https://github.com/ud-tetra/UD-Physics/actions/runs/40554459813) with pinned NumPy2.3.5/SciPy1.17.0, rtol2e-11, atol2e-14 and 401 samples spaced Δu=.25 over u0..100; original \`MountLoss.ode\` is called directly with no new forces. Compute raw relative primary Frobenius norm \`||Yprimary−Yref_primary||F\`, proper shell-centered moving-SO3 aligned shape and its geometric Taylor remainder, 120 housing strut minimum lengths, oriented cell volumes and energy plus heat balance.

## Actual selected nonlinear numerical results

| Quantity | Limiting source | Nominal source |
| --- | ---: | ---: |
| Max sampled full-amplitude actual primary-relative norm (+ sign) | **0.03500979202** | **0.03520937944** |
| Max sampled moving-SO3 aligned shape norm (+ sign) | 0.00004868981 | 0.00004990125 |
| Max sampled pure frame-chart Taylor remainder (+ sign) | 0.00001030822 | approximately 3.15×10^-16 |
| Max sampled actual source reference displacement from equilibrium | **0.05039240841 at u=9.25** | **0.05109022585 at u=9.25** |
| Min sampled 120-housing strut length (+ sign) | 0.49232941123 | 0.49230213342 |
| Min sampled oriented cell volume (+ sign) | 0.95507671682 | 0.95456068797 |
| Full-amplitude endpoint raw nonlinear flow remainder (+ sign) | 0.00001030811 | approximately 1.14×10^-11 |

All four amplitudes of each case stayed inside r=.036 on the 401 reported sample points; every sampled strut remained of positive length and orientation/volume remained positive. Source energy-plus-heat relative discrepancies were at most about 3.1×10^-12. These facts concern eight **selected finite nonlinear trajectories**, not all allowed 180-dimensional phase preparations or a mathematically certified time interval.

In the limiting case, the endpoint raw nonlinear flow remainder scales approximately quadratically from .5 to full amplitude, ~2.577×10^-6 versus ~1.031×10^-5; this is a **directional** numerical check, not a bound on the full Hessian. The nominal source is exceptionally symmetric, giving near-floating-roundoff raw flow and geometric frame remainders for this selected phase. The moving aligned maximum for these selected raw-adverse phases is smaller than the previous ~.000229 all-direction **linear** moving operator maximum because the phase directions optimize different objectives. Do NOT compare operator maxima as if a single phase attains them all.

## Exact failure mode of the earlier reference radius and sampling sensitivity

The previously exposed draft PR #206 sampled its reference trajectory at Δu=.5 and reported worst-case peaks .0394404 (limiting) and .0466766 (nominal), both below the post-exposure chart criterion d=.05. The **same frozen source** at tighter DOP853 tolerance and Δu=.25 records reference displacement peaks .0503924 and .0510902, both at native u=9.25. Taking every second time sample of these *same new curves* reproduces the previously reported Δu=.5 peak values to ~1e-11. Thus the discrepancy is **temporal aliasing of a high-frequency reference pulse**, not a newly selected material law, a damping-parameter change or a switch of phase norm.

This is a **NUMERICAL counterexample to using d=.05 as an all-time reference enclosure**. It is not a logical counterexample to that theorem, which is conditional on d=.05, nor a rigorous statement about the exact continuous-time maximum without validated integration. In particular a typical source DOP853 local tolerance is not a certified global interval error.

## Revised EXACT/CONDITIONAL proper moving SO3 chart

The source unit-edge regular icosahedral shell X0 satisfies \`X0^TX0=((5+sqrt5)/2)I\`. Define moving reference Yref, its shell-centered Xref and reference hub offset; for actual primary error E=Yactual−Yref, subtract the E shell centroid from all 13 rows. Define skew Omega by
\[
G\Omega+\Omega G=2\operatorname{skew}(X_{\rm ref}^\top E_{s,\rm centered}),\quad
G=X_{\rm ref}^\top X_{\rm ref},\qquad R=\exp(-\Omega)\in SO(3).
\]
The chart rotates both primary shell and hub, is orientation-preserving, and changes **only** the geometric readout; all 560 full mechanical coordinates and kinetic energies remain intact.

The fully executed [exact Fraction chart proof](chart_bound_d007.py) chooses **POST-EXPOSURE** \(d=7/100=0.070\), retains \(r=9/250=0.036\), and derives conservative rational constants \(\sqrt{c_0}<191/100\), \(\|X_0\|_F<331/100\), \(\sqrt{13/12}<25/24\), \(1/\sqrt2<71/100\). With \(\|Y_{\rm ref}-Y_0\|_F\le d\), \(G_{\min}\ge33277/10000\), \(\|\Omega\|_{\rm op}\le63261/4159625\), the matrix exponential Taylor estimate gives
\[
\boxed{\|\mathcal F_{\rm ref}(E)-D\mathcal F_{\rm ref}(0)E\|_F
 \le \frac{26619144063633}{27262940965600000}
 \approx0.0009763856400<0.001.}
\]
This holds for *all* 13-primary directions satisfying **both** actual radii hypotheses, not merely the eight sampled tests. It does **not** validate the source u0..100 nonlinear radius hypotheses: the observed .05109 peak motivates d=.070, and r=.036 has only ~.00079062 margin in the nominal selected phase, before untested directions, between-time peaks and numerical/flow errors.

The usual ordinary free 3D spring-dashpot model has the identical local source and SO3 alignment theorem. No uniquely UD-spacetime geometry, stress law, physical material calibration, time/length scale or independent experimental forecast is established.

## Reproduction / provenance / status

\`python3 experiments/icosahedral-nonlinear-radial/nonlinear_radial.py --case limiting --out limiting.json\`, similarly nominal. Executes the original MountLoss ODE, selects the top final raw housing tangent singular direction from the immutable original archive, uses ±1 and ±.5 amplitudes, 401 source sample points, and preserves complete JSON traces in [GitHub Actions artifact #12757520135](https://github.com/ud-tetra/UD-Physics/actions/runs/40554459813), with 30-day retention. The full output ZIP was downloaded and SHA256-verified within this conversation. Hashes: source \`6627a81b15fc715c43fb8f9bea13b34e9165848cecea2a892ca027c40c5a1728\`, limiting \`55a34f1535e0ac43ddf2dc09cf00a8df68a659394e6af20ca18a5316fa7cce23\`, nominal \`c4a19adb12a7b9e16333a7dd3b3619348a1233e7aa0fd2f19e9f03a2b593198b\`, summary \`343b1325d9bb318dd50a30f1917480940d498726315ae897636785e95a58b07a\`.

The exact updated chart proof was executed locally: source SHA256 \`17980dc96d0e7a996c237d914b51d9a3594656bab40ea5c4791483d516f2ac4a\`, result SHA256 \`369feb80ea6fbb27638d2893b46fad57938a5342dfcbef962d099fa68aeb177a\`. Source code/result, actual CI summary and schema-v2 manifest are committed immutably in [radial-001](../../artifacts/ico-radial-20261027-gpt6-a1/radial-001/manifest.json); **the full 401-point traces are retained only in the expiring Actions artifact**, not claimed immutable Git payload.

**Scientific status:** NUMERICAL selected-phase stress test COMPLETE, prior d=.05 source use **FAILED** at sampled reference times, revised d=.070 SO3 **EXACT / CONDITIONAL** chart theorem PASS, full nonlinear all-phase u100 80% breathing and strut/volume domain certification **OPEN**. Independent non-constructor scientific review and physical experiment NOT_RUN. No mainline promotion.

**NEXT highest-value action (priority 99/100):** construct validated continuous-time reference + projected forced Green/Hessian error bounds on the full 560-state dynamics, and test the *actual full 180D phase ball* against the r=.036 margin with an independently certified nonlinear remainder. Numerical tolerance and sample-spacing repeats are useful supporting checks, but no number of selected phases alone proves the all-phase certificate.
