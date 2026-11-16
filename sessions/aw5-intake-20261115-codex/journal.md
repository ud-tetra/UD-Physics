# AW5 offline intake

Base 2ab32f5f28d0461dc4d35a389e814e8415cb58e8. Held task claim 0041ecff29188c08099a53723e713552f6b8e3e9.

Intake checkpoint covers topology and dynamics controls for the flux, routing and damping hypotheses. Independent review OPEN.

Next: Test zero-frequency face-readout residue against filled and orthogonal-sensor controls.

## AW5 governed continuation

Agile hypothesis, target exposure recorded, no physical promotion.

## Run footer

- **Mission** — Determine whether a face-only source and readout distinguish a hollow star from its filled control.
- **Done** — Derived the zero-frequency residue and replayed exact filled, hollow, orthogonal and damped controls.
- **Finding** — The matched exterior readout has hollow residue 1/4. The filled and orthogonal controls give zero, and positive exterior damping removes the pole at the origin.
- **Bridge value** — The result specifies a model-level discriminator. A calibrated face readout and physical mapping remain open.

## Next step

1. **Priority 90/100** — Derive the weak-damping pole location and residue, then obtain a finite observation-time contrast bound. This tests whether the exact undamped discriminator survives finite bandwidth and damping.

## AW5 weak-damping continuation

- **Mission** — Determine whether the hollow-star impulse signature remains distinguishable over a finite window under exterior damping.
- **Done** — Derived the pole displacement and residue order, and bounded the signed time-average against each control.
- **Finding** — The pole moves initially at slope −1/4 with respect to damping. The controlled contrast is at least 1/8 for T = 32 and γ ≤ 1/512.
- **Bridge value** — The result supplies a finite-duration mathematical test with explicit nuisance bounds. Instrument response and calibrated mapping remain open.

## Next step

1. **Priority 90/100** — Derive a contrast guarantee with discrete sampling, independent readout noise, and bounded channel mismatch. This converts the continuous-time prediction into a testable acquisition specification.

## AW5 sampled acquisition sprint

- **Mission** — Convert the finite-window AW5 contrast into a sampled acquisition specification.
- **Done** — Derived independent sampling, mismatch, and noise bounds and checked their joint rational budget.
- **Finding** — The declared tolerances preserve at least 3/64 signed contrast against both controls with failure probability at most 2 exp(−16).
- **Bridge value** — The specification defines which quantities an engineered realization must certify before comparing the three responses.

## Next step

1. **Priority 90/100** — Build a target-blind synthetic intake scorer with separate timing, offset, noise, and operator certificates. Replay passing, failing, and correlated-noise controls before admitting a measured dataset.

## AW5 blind intake replay

- **Mission** — Freeze and exercise blind intake before measured trace admission.
- **Done** — Implemented exact rational scoring, commitment-checked role reveal, two-control adjudication, and synthetic gate replay.
- **Finding** — Equality at 3/64 passes, a single shortfall fails, and correlation, certificate violations, altered scores, or an altered reveal are inadmissible.
- **Bridge value** — The intake separates acquisition eligibility from observed agreement. Physical validation and independent review remain open.

## Next step

1. **Priority 90/100** — Replay model-generated signed impulse traces through the same frozen scorer, then specify independently auditable certificate provenance for timing, operators, and noise.

## AW5 model intake replay

- **Mission** — Check the frozen evaluator using signed responses from the AW5 operators.
- **Done** — Scored six traces across two damping cases and specified auditable certificate inputs.
- **Finding** — Both simulated packets passed against both controls. No measured packet was admitted.
- **Bridge value** — The model and scorer now connect through a reproducible pipeline. Instrumentation and independent review remain open.

## Next step

1. **Priority 90/100** — Identify a realizable signed-coupling platform and test whether independent operator, timing, and noise certificates can meet the native acquisition budgets.

## AW5 signed-coupling feasibility

UD mathematical capture and scorer provenance integrated at c48ffb8b2f9c82b33bcd25fc24755d16c0053424.

- **Mission** — Compare physical platforms against the frozen AW5 acquisition limits.
- **Done** — Screened photonics, superconducting circuits, and active analog circuits and calculated a candidate bench budget.
- **Finding** — Analog is the first prototype candidate. The induced-norm generator certificate is the hardest gate in this desk screen.
- **Bridge value** — The design supports a calibrated classical emulator test. No platform has certified AW5 compliance.

## Next step

1. **Priority 90/100** — Specify the two-state signed pair, then test whether a basis-injection calibration with explicit uncertainty can establish the generator and timing budgets before full-carrier replication.

## AW5 signed pair and WBS receipt

Mainline merge verified at c48ffb8b2f9c82b33bcd25fc24755d16c0053424. WBS v2.7 entry pending a path to the existing master manifest.

- **Mission** — Specify the signed pair and an uncertainty-aware calibration before AW5 replication.
- **Done** — Derived the circuit polarity, basis-injection identification and explicit operator certificate gates.
- **Finding** — Coefficient certification requires a tighter endpoint budget than the scorer's timing tolerance alone supplies.
- **Bridge value** — An auditable calibration candidate is available. Hardware evidence and independent review remain open.

## Next step

1. **Priority 92/100** — Bench the signed pair with the proposed timing loopback and held-out preparations, then evaluate the uncertainty certificate before scaling.

## AW5 bench pair intake and WBS update

Prepared the v2.7 WBS manifest from the supplied master text with the verified UD #516 merge c48ffb8b2f9c82b33bcd25fc24755d16c0053424 and the pending Discovery calibration gate. The supplied offline path was unavailable in this runtime.

- **Mission** — Prepare the formal intake for timing-loopback and signed basis-injection records.
- **Done** — Implemented a machine-readable gate receipt and replayed nominal, timing, held-out, missing-evidence and rank-deficient fixtures.
- **Finding** — The prototype distinguishes independently scoped gate shortfalls from unscorable input.
- **Bridge value** — Bench packets can now be reduced consistently once the underlying measurements and certificates are supplied.

## Next step

1. **Priority 92/100** — Acquire the timing-loopback and paired basis shots with held-out mixed inputs. Audit their certificate sources, then run the unchanged unit-cell intake.

## AW5 heat trace and retriangulation

- **Mission** — Test a topology-preserving control against the cavity heat-trace identity.
- **Done** — Replayed signed incidence, local and exterior boundary preservation, exact face spectra and nullities.
- **Finding** — Hub removal changes the long-time face trace by one. The filled bistellar move changes the finite-time trace and preserves the limiting count.
- **Bridge value** — The controls isolate harmonic count from triangulation-dependent spectral response. The bench gate remains open.

## Next step

1. **Priority 90/100** — Test a boundary-fixed refinement of the hollow star and quantify how the exterior readout residue changes at fixed b₂.

## AW5 exterior residue under refinement

- **Mission** — Test exterior residue at fixed cavity homology.
- **Done** — Replayed five refinement counts and recorded the [AW5 supplement](https://github.com/ud-tetra/UD/blob/b378ede7269c2a793f90e0692b517a2fd4237ee2/captures/2026-11-16T011802Z-codex-aw5-refine-1dd290/REVISED_MANUSCRIPT_REPRODUCIBILITY_SUPPLEMENT_AW5.md).
- **Finding** — Boundary-fixed refinement preserves b2=1 but moves the original exterior residue from 1/4 to 19/80; best aligned residue is 91/380 after one leaf.
- **Bridge value** — The original AW5 amplitude applies to the frozen triangulation and metric. Physical Promotion = 0.

Next: Derive a metric-aware refinement and readout-transfer rule, or exhibit an obstruction.
