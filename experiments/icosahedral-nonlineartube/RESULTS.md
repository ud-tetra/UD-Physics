# Nonlinear energy-domain results v1.0

**EXACT / CONDITIONAL:** for every housing-only phase with E_h<=E_p/40000, across the entire qualified property box, all120 struts remain >987/2000=0.4935 and every oriented cell volume stays in(39/40,41/40) of reference for all future time. The solution exists globally. This strengthens the earlier initial-domain result for this preparation only. See [proof](README.md), [receipt](../../candidates/icosahedral-nonlineartube/mathematical_receipt.json).

**EXACT / CONDITIONAL:** full alpha=.1 pulse plus any allowed housing phase is safe throughu=1/20, with struts>1/40 and cell-volume ratios in(.729,1.331). This is an initial tube, not a u100 certificate.

**FAILED certificate extension:** full-pulse energy alone cannot prove all-time positive strut lengths. A lower-beta reference-geometry housing at one endpoint costs only1/(40R²)=.027639320225..., below the nominal pulse energy. Arbitrarily short positive struts also lie below that energy. This is a sublevel obstruction, not a dynamically reachable counterexample.

## Fresh numerical constructor checks

Four exposed housing-only phases, two pulse phases and one finer-tolerance repeat were executed overu0..100; 7/7records pass their numerical/domain checks. The following extrema are sampled, not interval-certified.

| Preparation | nu | E(100)/E(0) | Sampled strut minimum | Sampled cell-volume range |
| --- | --- | --- | --- | --- |
| housing-only edge-p1-b0.005-cf0.0 | 0.04 | 0.305752991 | 0.499708923 | 0.999998799–1.000001203 |
| housing-only edge-p1-b0.005-cf0.0 | 0.05 | 0.239927288 | 0.499724433 | 0.999998448–1.000001552 |
| housing-only uniform-b0.05-cf0.0 | 0.04 | 0.440064550 | 0.499962604 | 0.999775390–1.000225546 |
| housing-only uniform-b0.05-cf0.0 | 0.05 | 0.359171337 | 0.499962662 | 0.999775746–1.000223644 |
| pulse seed10422-0-boundary2 | 0.05 | 0.909301261 | 0.492313907 | 0.955083246–1.046739270 |
| pulse seed10422-0-boundary2 (fine) | 0.05 | 0.909301261 | 0.492313907 | 0.955083246–1.046739270 |
| pulse uniform-b0.05-cf0.0 | 0.05 | 0.948052534 | 0.492295076 | 0.954478599–1.047368862 |

The worst previously exposed breathing preparation retains0.872563910933575 of its frozen nonlinear baseline; its tolerance repeat changes that ratio by1.61e-14. The nominal full-housing-phase pulse retains0.899062529050692 against its separately stated exact undamped/no-housing collective baseline. These results do not optimize over nonlinear phases and do not certify the full ball.

Maximum relative E+heat error is2.986e-9 (housing-only energy is only about1.6e-6); maximum total spatial P,L drifts are below1.20e-15 and5.72e-16. Actual small initial angular momentum is retained. No rigid kinetic energy is discarded.

## Reproducibility and corrections

[Immutable run](../../artifacts/icosahedral-nonlineartube-20261022-a1/nonlineartube-001/manifest.json) captures proofs, exact checks, complete coefficient/phase inputs, source code, per-preparation hashes, output summaries and trajectories sampled every.5u. Full readout extrema used4001points(.025u). NumPy/SciPy versions and solver tolerances are in checks.json. DOP853 errors are checked by balance and tolerance repeat, not bounded through verified integration.

Two implementation errors were corrected and disclosed: Q5 comparisons require exact sign-of-difference; the frozen baseline dictionary has no nominal entry. The nominal comparison therefore uses the exact original collective solution with its own numerical RMS. The complete ODE campaign was rerun after the correction. No model, budget, target or phase was changed. See implementation_corrections.json and [protocol](PROTOCOL.md).

The housing-only nonlinear half-energy-at100 theorem remains OPEN. The full-pulse u100 all-phase length/volume/breathing tube remains OPEN and requires a trajectory-dependent invariant or validated relative-energy/variational argument. Hardware UNSCORED; native law/time selection OPEN; mainline promotion0.
