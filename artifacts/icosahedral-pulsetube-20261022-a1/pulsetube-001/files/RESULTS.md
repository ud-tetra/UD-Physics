# Moving-pulse results v1.0

**RESULT: u100 nonlinear phase-ball guarantee remains OPEN.** The analytic derivative, moving-pulse first-order phase optimization, exact conditional tube criterion and diagnostic evidence are complete. The missing validated Green/remainder/reference-error bounds are explicit in [theorem](TUBE_THEOREM.md) and the captured certificate_audit.json. See [method and scope](README.md), [protocol](PROTOCOL.md), [receipt](../../candidates/icosahedral-pulsetube/mathematical_receipt.json).

## Moving-pulse sensitivity

Full560-state mechanics and all180 initial housing phase coordinates are retained. Two exposed parameter sets are evaluated atnu=.05, with the inherited housing energy E_h=E_p/40000. The first-order minimum optimizes breathing RMS, rather than housing ringdown energy.

| Fixed property set atnu=.05 | Reference breathing | First-order energy-ball minimum | Direct adverse finite phase |
| --- | --- | --- | --- |
| seed10422-0-boundary2 | 87.256496% | 87.220846% | 87.220741% |
| uniform-b0.05-cf0.0 | 89.909764% | 89.869982% | 89.867174% |

These first-order values use floating tangent propagation and time quadrature, so they are not strict finite-amplitude bounds. For the limiting case, the finer first-order minimum is87.2207615%; the direct finite phase uses the earlier frozen optimizer and4001-point readout, giving87.2207408%. This is lower than the previous tested ringdown-phase result87.2563911%, by0.03565percentage points. The previous64-record campaign remains unchanged; this is a new exposed finite preparation, not a claimed nonlinear worst-case optimum.

The fine sampled affine-tangent strut-distance margin is0.4881907; it applies to the affine prediction, not the true nonlinear ball. Fine sampled first-order cell volumes range0.9549882–1.0468211. The two sets do not establish continuous uncertainty-box ornu-interval coverage.

## Numerical checks

- Analytic Jacobian versus original nonlinear ODE: twelve directional checks, minimum-step-selection errors<=1.30e-9. Independent existing equilibrium K/C representation changes<=4.27e-14/1.39e-17. Initial housing energy Gram identity error<=2.23e-16.
- Seven finite preparations: adverse phase, negative phase and quarter energy for both sets, plus a zero-disturbance reference check. All retain>80% breathing and positive sampled strut/cell volumes. The original5%mismatch/50%shape screens were not recomputed and are not claimed here.
- Adverse-phase mean-volume Taylor residual RMS<=3.392e-10; quarter-energy/full-energy residual ratios0.25138 and0.25133. This is directional scaling, not a uniform nonlinear remainder bound.
- Matched-time refinement: mean-volume derivative change<=5.58e-10, final tangent entry change<=2.55e-7, reference-state entry change<=1.76e-9. RMS changes2.061e-8 include the changed quadrature. Tangent P/L invariant errors<=8.66e-12/6.72e-12; mechanical rigid motion and its energy were retained.
- A standalone reference integration differs from the augmented tangent reference by<=2.23e-9 in full state and1.18e-11 in mean-volume RMS residual. Balance and tolerance checks remain numerical consistency checks, not verified integration error bounds.

## Failed ambient readout budget and frame-aware diagnostic

The raw all-phase tangent primary-position radius is0.03500972. Its conservative determinant remainder bound0.0328188 exceeds the available RMS margin0.00176402 even with zero nonlinear flow error. This sufficient readout bound fails.

Proper-frame alignment reduces the numerical primary shape tangent radius to0.0002420865. The corresponding geometric determinant remainder is1.5187e-6, leaving a sampled-design allowance of0.001767605 for the aligned primary flow remainder. This is a target for future validated analysis, not an achieved bound. Alignment-chart nonlinear terms must also be included.

A separate post-exposure finite diagnostic maximizes raw final primary displacement. It produces raw motion0.03500979, but aligned shape motion stays below4.5762e-5; final aligned shape motion is6.0296e-7 and its final first-order flow remainder1.6538e-9. The phase has nonzero total momentum/angular momentum, which the original ODE conserves. This demonstrates why a raw-position radius spends most of its budget on frame motion. It does not certify the remaining directions.

## Exact conditional progress and archival scope

The exact tube implication is A+beta+C*r²<r with a positive full-state norm and continuous domain margin. The theorem includes initial/reference defects, full forced Green operator, nonlinear Taylor remainder, projected readout bounds, an exact cubic determinant remainder and a proper-alignment alternative. Only U(t,0)B is currently computed; the forced U(t,s), uniform nonlinear/chart remainders and continuous numerical-error bounds remain unverified. No scalar radii test is reported as passed.

[Immutable run](../../artifacts/icosahedral-pulsetube-20261022-a1/pulsetube-001/manifest.json) captures source/coefficients, selected reports/traces, phase/Gram/final-tangent checkpoints and missing-bound audit with SHA256 digests. Large full augmented-response intermediates are reproducible and their digests are recorded, but they are not claimed to be archived. Initial normal source, stable-norm correction and later diagnostic additions are disclosed; no model, energy, pass threshold or original adverse phase was retuned.

Next discriminant: enclose the forced Green response and nonlinear alignment/flow remainder for the limiting case in a positive full-state/block norm. A validated aligned primary remainder below1/1000 is a conservative design goal inside the observed numerical allowance, subject to full reference/quad/domain error accounting. The inherited80% threshold is unchanged.

The earlier exact housing-only global domain/volume theorem and full-pulse u1/20 theorem remain valid in their stated scopes. This work supplies no native constitutive/time identification or physical validation; hardware UNSCORED and mainline promotion0.
