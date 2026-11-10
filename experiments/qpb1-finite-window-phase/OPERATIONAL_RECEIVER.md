# Operational finite-window interferometer: review and uncertainty contract

**RESULT — EXACT / CONDITIONAL.** An *assumed* coherent phase-reference receiver and a separately calibrated dynamical-phase subtraction extend the previous fixed-window certificate to preparation uncertainty, timing jitter, readout error and independent gain drift. The rational all-box bound is **0.008250275742 radians** (upper enclosure; decimal rounded up), below the *selected* 0.01-radian diagnostic screen, with contrast at least **607251319/612500000 > 0.99**. No implemented optical/material device, physical clock, or empirical uncertainty measurement is claimed.

## Provenance and review classification

Review target: this branch's \`phase-001\` certificate at \`faabd63e9fafc44e824423e85a272d1fca71d750\`; its imported local generator and connection are pinned at integrated revision \`41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb\`. This follow-up uses a **separate algebraic route and a new Python implementation**, but remains **the same assistant's constructor/self-check**, not external independent mathematical review. Other reviewers: **NOT_RUN**. Apparatus and physical tests: **NOT_EXECUTED**. The old \`phase-001\` manifest is immutable and unchanged.

Retain the rank-14 real active carrier with positive Euclidean metric, complex structure J as multiplication by +i, commuting mutually orthogonal sectors P1/P2/P3, and conservative generator \`G=sum gk Kk\`. All time s and T are **dimensionless native** coordinates; physical t=τ0*s is an OPEN map. Frequencies are angular in units 1/native-s. No spacetime metric or measured physical gauge has been selected.

## Receiver hypothesis and missing calibration

For a normalized preparation x and model evolution U(T), assume a coherent reference arm x, a comparison arm U(T)x, balanced recombination and analyzer phase β, all in a common phase frame. The ideal intensity is

\`I(β) = [1 + Re(exp(-iβ)Z)]/2,\quad Z=<x,U(T)x>_C = Σ r_k exp(i2g_kT).\`

Four sampled phases β=0,π/2,π,3π/2 give \`Re Z=I(0)-I(π)\` and \`Im Z=I(π/2)-I(3π/2)\`. Contrast is \`V=|Z|\`. **Raw Arg Z is not the geometric phase.** The readout additionally needs \`D=∫α=2T Σr_k g_k\` and reports \`Φ=Arg Z-D mod 2π\`, provided V>0. The stated phase combines a Pancharatnam overlap with a modeled dynamical correction; a physical mechanism to obtain D in the *same phase gauge* is assumed, not derived. A gauge change at the two endpoints adds the same phase to Arg Z and D; their difference is invariant given a properly transformed reference.

The null baseline is an ordinary two-arm coherent interferometer: these quadratures and their errors require **no special UD mechanism**. An experimental bridge would additionally need physical access to the three sectors, a controlled coupling, a time scale τ0, and a cross-validated D estimator. No ordinary interferometer observation by itself distinguishes the UD generator from a conventional three-frequency complex system.

## Exact analytic bound, including preparation

Expose the previously target-selected reference \`g0=(1,1,3/2), r0=(1/4,1/4,1/2), T0=2π\`, with \`Hol0=-1\`. Assume \`|δgk|≤ε=1/100\` independently, \`|T-T0|≤q=1/100\`, and normalized initial state \`||x-x0||≤ζ=1/2000\`. Because P3 is an orthogonal projection, its probability difference satisfies \`|r3-1/2|≤||x-x0||≤ζ\` (pure-state trace distance bounds any projection readout; equivalently decompose x±x0 along P3).

Writing \`T=T0+u\`, discard baseline angles \`2g0kT0 ∈ 2π Z\`, and set
\`a_k=2g0k u+2δgk(T0+u)\`, \`μ=Σr_k a_k\`. Every \`a_k\` lies in an interval of range at most
\`S=|u|+4ε(T0+|u|) < q+4ε(44/7+q)=2291/8750\`,
where the strict inequality uses \`π<22/7\`. The adjusted angles \`y_k=a_k-μ\` satisfy \`Σr_k y_k=0\` and \`|y_k|≤S\`. Therefore \`Re Σr exp(iy)≥1-S²/2>0\` and \`|Im Σr exp(iy)|≤S³/6\` from the sine Taylor remainder. The continuous-branch finite-path phase drift is bounded by
\`Bφ=S³/[6(1-S²/2)]=12024728171/3881753373750\` radians.

Centering the angle range before taking the complex sum also gives \`V≥cos(S/2)≥1-S²/8=607251319/612500000\`. This establishes nonzero overlap for *all* normalized nonnegative weights and every allowed independent gain/time error, not just a sampled grid. The baseline preparation phase equals \`-2πr3\`, so the deviation from the selected \`-1\` has an additional upper bound \`2πζ < 11/3500\` radians.

## Deterministic readout and calibration budget

Postulate the four-fringe estimator \`|Zhat-Z|≤η=1/1000\` in normalized complex-amplitude units, with a **separate**, same-gauge correction estimate \`|Dhat-D|≤κ=1/1000\` radians. Since \`V≥v\` and \`η<v\`, the angle error from the complex estimator is at most \`η/(v-η)=612500/606638819\` radians. With all perturbations simultaneous,

\`|wrap(Φhat-π)| ≤ 11/3500 + 12024728171/3881753373750 + 612500/606638819 + 1/1000\`
\`= 11101676085864605533/1345612732743408915000 ≈ 0.00825027574110 < 1/100\` radians.

This is a **worst-case deterministic conditional budget**, not a probabilistic confidence interval. The ε, q, ζ, η, κ values and thresholds were selected for this exploratory engineering screen; they are **not measured**. In particular, the ability to achieve a 0.001-radian same-gauge D calibration is a significant unimplemented assumption.

## Alternative construction, checks and boundaries

A separate standard-library implementation reconstructs Z directly as three complex phasors, reconstructs Z through four intensity settings, independently forms D, and checks 243 structured gain/time/preparation tuples with four worst-radius noise directions plus 25,000 seeded additional tuples. All pass within float64 tolerance; these samples check the implementation and do not substitute for the analytic all-box proof. See [standalone audit](operational_audit.py) and [immutable phase-002 artifact](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-002/manifest.json). Reproduce from repository root:

\`python3 experiments/qpb1-finite-window-phase/operational_audit.py --out /tmp/ud-operational-receiver.json\`

Counterexamples/limits: without D subtraction the baseline fringe Arg Z is zero while Hol0 is π, so a raw interferometer does *not* measure the target. If the receiver's phase gauge wanders independently of the D calibration, a 0.001-radian correction error cannot be justified. Outside the certified angle spread the overlap can vanish, making Arg Z unreliable. Unknown clock units, interaction topology, empirical shot noise, loss and material response prevent attributing this generic interferometer model to physical UD processes.

**Discriminant:** require a non-constructor reviewer to check the derivation and reproduce the immutable run; next, specify a realizable phase-reference/correction-calibration pathway and obtain data for its systematic-error floor. No independent prediction or mainline physical promotion.
