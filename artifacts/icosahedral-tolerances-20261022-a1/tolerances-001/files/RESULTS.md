# Joint tolerance results — v1.0

**RESULT —20/20 declared in-budget preparations retain useful breathing;54 additional housing modes obstruct full mechanical relaxation.** Exact module and symmetric frequency bounds have narrower hypotheses than the finite joint campaign. Physical tests remain unperformed.

## Proposed engineering budget

| Parameter | Declared value/range |
| --- | --- |
| Reciprocal ratio error | Within±1% on each of150 branches |
| Total housing mass | At most5% of nominal original shell mass |
| Input-port viscosity parameter c_f | At most0.001;each port has c_f/10 |
| Housing mount frequency | UniformOmega_h10 |
| Housing mass weights | Within±10% of mean;total mass preserved |
| Primary masses,spoke couplings,edge springs | Within±5% in sampled realizations |
| Preparation | alpha=.1,reference geometry,zero other states |
| Window | Dimensionlessu0..100 |

Twelve boundary probes combine3 exposed property sets with4 ratio/housing patterns. Eight new seeded interior probes sample the same declared ranges. All remain development data. Device parameters(mu,kappa,gamma)=(2,50,5) were unchanged. The mass and stiffness weights are correlated to preserve mount frequency;independent component/mount-frequency tolerances remain OPEN. The single c_f is shared across ports within each trajectory;spatial friction scatter was not sampled.

| In-budget outcome | Observed result |
| --- | ---: |
| Passed80%RMS/5%mismatch/50%shape screen | 20/20 |
| Minimum mean-volume RMS retained | 92.311% |
| Maximum hub-relative volume mismatch | 0.73757% |
| Maximum shell-centroid volume mismatch | 0.66957% |
| Residual shell-shape RMS,range | 4.475–10.183% |
| Maximum housing lag / reference edge | 0.002266 |

RMS/shape ratios use the matching **original undamped,no-housing** preparation,so they include housing and friction costs. Stored baselines are used for the3 exposed sets;fresh undamped baselines were computed for the8 new sets. These finite observations do not certify every point in the parameter box.

## Challenges outside the proposed budget

Each challenge changes the named factor from a declared boundary preparation. Passing one challenge does not expand the budget.

| Changed factor | Breathing RMS retained | Hub-volume mismatch | Screen |
| --- | ---: | ---: | --- |
| Ratio errors3% | 87.93% | 0.864% | PASS,finite case |
| Housing mass20% | 83.56% | 0.697% | PASS,finite case |
| c_f=.02 | 69.54% | 0.744% | FAILED breathing retention |
| Mount frequency4 | 83.49% | 0.658% | PASS,finite case |

The friction challenge keeps volume mismatch small while exhausting the useful common signal. Coherence and retained amplitude require separate readouts.

## Exact narrower certificates

- Bare-module common/differential dissipative impedance ratio is at most0.0701321% overomega1..4 under the declaredratio/friction bounds andnominal device values. Normalized cross-impedance is at most2/199. These are impedance bounds,not assembly volume bounds.
- Ideal uniformly loaded conservative collective frequencies shift downward by at most2.136% forbeta<=5% andOmega_h>=10. The sampled defaultbeta5% case shifts the two low frequencies by1.639% and0.179%. Friction andnonuniform loading are separate questions.
- Positive housing storage preserves the earlier primary member positive-length certificate atA0=.1 in the stated g,k ranges. It does not prove all-time cell orientation or coherence.

## Negative housing-mode result

The added midpoint mounts are conservative. The unsigned12-by30 endpoint incidence has rank12,so there are18 reaction-cancelling housing patterns per spatial axis:54 undamped modes. A four-edge alternating pattern at amplitude1e-4 was checked exactly and simulated in the full560-phase model,withpositive device/input losses andalpha0.

Primary/relative coordinates change by at most1.22e-17;housing motion matches the undamped harmonic orbit within5.96e-14. Relative housing-energy variation is1.22e-9,and dissipated fraction is below3.14e-27. Full mechanical asymptotic relaxation is therefore FAILED for this housing model. The20 budget probes initialize those modes at zero anddo not test their decay. The[addendum](MOUNT_MODE_ADDENDUM.md) preserves proof,scope and reopening conditions.

## Verification and next physical test

- Four full560-phase symmetric trajectories agree with the exact3-coordinate loaded subsystem within5.76e-10.
- Independent mount energy-gradient error3.74e-12;net mount force/torque residuals2.51e-17 /1.62e-17. Input-friction power assembly agrees within3.39e-21.
- Maximum E+D relative residual4.78e-9 over the24 joint/challenge plus4 symmetry trajectories. Total primary-plus-housing P/L drift stays below1.61e-15 /1.14e-14. Primary momentum alone exchanges with the housings.
- Worst in-budget volume mismatch changes by1.70e-8 under refinement;refined energy-balance residual1.02e-12.
- Minimum sampled cell volume is0.95312 of reference;sampled supporting halfspaces pass. No all-time orientation theorem follows.

![Joint probes,module bound and housing counterexample](../../artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files/tolerance-summary.png)

[MODULE_TEST.md](MODULE_TEST.md) now gives calibration,common/differential forcing,uncertainty gates and a separate housing-only ringdown test. StatusUNSCORED/NOT_EXECUTED. Full relaxation requires an explicit passive mount-loss mechanism,with all reactions and its breathing cost quantified. Actual gearing,routing,travel limits and casing modes outside the midpoint-mount model remain untested. No physical correspondence or native-law promotion was established.
