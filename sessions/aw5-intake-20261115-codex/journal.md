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

## AW5 metric transfer and bench scope

- **Mission** — Separate exact metric/readout transfer from physical acceptance of parasitic refinements.
- **Done** — Replayed the split and Whitney metrics and audited both scorer entry points.
- **Finding** — Matched transfer preserves the mathematical response. The ideal 1/5 floor cannot be used as a finite-window bench tolerance.
- **Bridge value** — The audit specifies the scope evidence needed to compare a refined hardware carrier.

## Next step

1. **Priority 92/100** — Freeze an identified refined carrier and derive a finite-window guarantee using its actual damping, readout transfer and controls.

## AW5 one-leaf acquisition certificate

- **Mission** — Certify the sampled one-leaf AW5 contrast with fixed exterior drives.
- **Done** — Froze the carrier and three probes, replayed the spectral factors and derivative bounds, and evaluated the uncertainty budget.
- **Finding** — Both contrasts clear the 3/64 margin under the declared model and noise assumptions.
- **Bridge value** — The refined test has a quantitative acquisition target for the identified carrier. Measured admission and independent hardware calibration remain open.

## Next step

1. **Priority 92/100** — Generate the three refined model packets through the frozen scorer, then bind the carrier and probe declarations to the independently audited hardware and calibration evidence.

## AW5 one-leaf committed replay

- **Mission** — Exercise the frozen scorer on the specified one-leaf carrier with both controls.
- **Done** — Generated and froze signed model traces, verified the published digests before reveal, and replayed adjudication.
- **Finding** — Both gaps clear 3/64 with γ=1/512 on the declared synthetic packet.
- **Bridge value** — The refined model and acquisition scorer now connect end to end. Calibration, measured admission, and independent custody remain open.

## Next step

1. **Priority 92/100** — Bind the declared carrier and probe map to independently calibrated hardware records, beginning with the signed-pair bench packet and timing loopback.

## AW5 raw archive preflight

Archived the verified shell script and linked it from the bench intake. The raw archive and independently authenticated digest remain pending. Physical Promotion = 0.

## AW5 exact timing boundary

The pinned preflight-era unit-cell CLI rounded a decimal just above 1/1024 ms into the passing boundary. Decimal JSON timing inputs now feed an exact rational maximum and uncertainty sum. Eight CLI cases passed, including positive and negative deviations, sums at and above the gate, and a decimal beyond floating-point resolution. The measured archive and custody evidence remain pending. Physical Promotion = 0.

## 2026-11-16T19:49:02.408531+00:00

## 2026-11-16T19:51:58.928782+00:00

Captured artifacts/aw5-intake-20261115-codex/aw5-refinement-depth-20261116 (EXACT): Exact AW5 stationary depth law and conditional sampled clearance through depth three. Physical Promotion = 0.

## AW5 refinement-depth continuation

- **Mission** — Determine the range of the original AW5 acquisition window under refinement.
- **Done** — Verified the [finite-window certificate](../../candidates/aw5-hollow-star-intake/REFINEMENT_SWEEP_WINDOW_CERTIFICATE.md) and [recursive residue law](../../candidates/aw5-hollow-star-intake/RECURSIVE_LEAF_RESIDUE.md). See the [mathematical receipt](../../candidates/aw5-hollow-star-intake/refinement_depth_receipt.json) and [captured replay](../../artifacts/aw5-intake-20261115-codex/aw5-refinement-depth-20261116/manifest.json).
- **Finding** — First-level subsets guarantee contrast >= 7/100. Uniform depth 3 clears 3/64 with direct damped enclosure. Static residue equals 1/[2(1+(3/2)^d)] and tends to zero.
- **Bridge value** — The declared finite-window margin survives refinements through the verified scopes. Hardware evidence remains open. Physical Promotion = 0.

Next: Derive frequency-dependent four-terminal reduction or an equivalent certified method for depth four and beyond.

## 2026-11-16T20:39:26.500526+00:00

Captured artifacts/aw5-intake-20261115-codex/aw5-dynamic-dtn-depth6 (NUMERICAL): Exact recursive Schur reduction and conditional midpoint bounds through depth six. Physical Promotion = 0.

## AW5 recursive boundary response

Four-face terminal response exists after shared graded assembly; the recursive 14-coordinate leaf ports and final 16-face AW5 resolvent certify the original gate at uniform depths 4–6. Depth-six margin is 0.000240.

[Derivation](../../candidates/aw5-hollow-star-intake/RECURSIVE_FREQUENCY_RESPONSE.md) · [Receipt](../../candidates/aw5-hollow-star-intake/recursive_dtn_receipt.json) · [Captured replay](../../artifacts/aw5-intake-20261115-codex/aw5-dynamic-dtn-depth6/manifest.json).

Next: Tighten the depth-six numerical enclosure and test whether depth seven clears the fixed gate. Physical Promotion = 0.
