# Passive housing loss — development protocol v1.0

Base: `83349b741cf262b2a264949f6338140d691373e6`. Declared before the new numerical campaign. All prior results and the 80% breathing / 5% hub-volume mismatch / 50% residual shape screen are exposed development targets. No independent prediction or physical test is claimed.

Keep the finite 280-coordinate Hardware model, device `(mu,kappa,gamma)=(2,50,5)`, its conservative midpoint mounts and its full reactions. For each shell edge housing, add four massless central axial dashpots to the two edge endpoints and the opposite vertices of the two adjoining boundary faces: 120 added links, no additional storage/state. This is an engineered idealization; routing, collisions and finite damper/anchor masses are not modeled.

Each link has positive coefficient `eta=nu*(2 beta/(5 R²))`, fixed within a trajectory. Its force is minus the gradient in velocities of `eta*[n·(V_h-v_a)]²/2`, with current unit direction from anchor to housing. Apply equal opposite central point forces. Zero length is excluded explicitly. Length/energy/time units remain the parent's uncalibrated ell0/E_*/t0.

First audit exact anchor geometry, directions, force/torque/power, stiffness and loss assembly. Prove local detection of the previous 54-dimensional hidden housing sector. Check whether any new undamped equilibrium eigenmode remains; a local result is not a finite-amplitude global theorem.

## Frozen development scan

Scan `nu = [0,.005,.01,.02,.05,.1,.2,.5,1]` at nominal primary properties, beta=.05, Omega=10, c_f=.001, unit housing weights, ideal ratios. For each value:

1. Calculate the maximum final total mechanical energy fraction at u=100 over all initial displacement/velocity phases of the previous 54-dimensional mass-weighted hidden housing space, using the full equilibrium linear propagator. Both position and velocity preparations are included (108-dimensional initial phase space); total rigid momenta are zero. This is a numerical worst-direction linear calculation.
2. Integrate the full nonlinear alpha=.1 / other-strains-zero preparation over u=0..100 (2001 samples), and compare mean volume RMS to the original undamped/no-housing symmetric model.

Select the smallest positive scanned nu with worst housing energy fraction<=.5 and nominal breathing retention>=.8. If none qualifies, record the joint screen FAILED; select the smallest nu meeting the housing gate solely to expose its breathing cost. If no scanned value meets the housing gate, record that failure and stop selection. Never silently adjust gates, add scan points, or call an outcome-blind test.

## Joint and verification runs

Once selected, freeze nu. Reuse the exact 24 probes and 11 original baselines from `artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files/{probes,baselines}.json`; do not regenerate or retune them. They include 20 in-budget and four challenge cases. Report each inherited screen and conservation/energy/length checks, including failures. Add the old four-cycle housing perturbation (alpha=0, amplitude1e-4), a worst-direction linear housing perturbation at small finite amplitude, a full-vs-reduced symmetric comparison, and tighter/sample-doubled reruns of the worst budget mismatch/retention cases (deduplicate if same case). A simultaneous pulse plus nonzero housing perturbation in the worst budget case is a separate development challenge, not one of the original 20.

Use float64 DOP853 rtol=1e-10/atol=1e-12 for pulses; tighter checks rtol=2e-12/atol=2e-14. Tiny ringdown runs use atol=1e-15. Preserve code, input bytes, scan tables, selected value, full readouts, exact certificate, reduced comparison, failures and refinement. Matrix-exponential/SVD calculations are numerical; exact identities use Q(sqrt5)/fractions. One runtime constructs and checks this work; there is no separate-context review or empirical replication.

## Post-selection scope audit (explicit amendment)

After nu=.02 was selected and joint readouts were observed, add three numerical matrix checks for the local proof's c_f=0 scope: nominal beta=.05, scattered primary/housing properties from frozen case1 at beta=.05, and nominal primary/housing weights at beta=.005. These are post-selection development checks, not extra candidates in the strength scan and not independent predictions. Report the worst old-hidden-sector energy as well as the slowest nonrigid pole. A local decay pass does not automatically pass the nominal half-energy-at100 target. `postcheck.py` compares the saved worst nonlinear housing ringdown to the linear prediction, verifies frozen input bytes, and relabels primary-only momentum readouts in the seeded challenge; it changes no trajectories or design choice.
