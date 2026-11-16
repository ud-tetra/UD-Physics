# AW5 one-leaf refined finite-window certificate

**EXACT / CONDITIONAL** model bounds. **PROBABILISTIC / CONDITIONAL** noise bound. **Physical Promotion = 0.** This is a pre-acquisition model and probe declaration for one explicit carrier. Hardware calibration and independent review remain open. The coarse and refined model residues were already known at declaration. No measured targets or fitted parameters are used.

## Carrier and physical probe map

The refined hollow carrier keeps unrefined leaves 0235, 0136, 0127 and replaces 1234 by 1238, 1248, 1348, 2348. Its graded dimension is 60 with unit simplex inner products. The filled reference is the original 47-coordinate filled AW5. The exterior face coordinates remain the same across both carriers. The one-leaf frozen drive uses the original unweighted exterior sign pattern. In ascending orientation the face order and signs are

| Exterior face | 016 | 017 | 025 | 027 | 035 | 036 | 124 | 127 | 134 | 136 | 234 | 235 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sign | + | − | − | + | + | − | + | − | − | + | + | − |

Divide by √12 to make a unit vector q. For an analog realization use these same signed, normalized face voltages for effective impulse preparation and collocated readout, with the shared time, voltage, reference and gain conventions. All other input components are zero in the model. Compare the refined target with the filled reference using q and with the refined orthogonal control using (e₀₁₆+e₀₁₇)/√2. The latter is orthogonal to the refined harmonic mode because the two faces have equal-magnitude opposite signed coefficients and remain unrefined. The residues of these three arms are 19/80, 0, 0.

Use the original T=32, N=256 midpoint grid and frozen margin 3/64. The damping law is −γP on the twelve exterior faces and the declared hardware tolerance γ≤1/512. The certificate assumes the signed generator and loading of each arm are identified in its own declared basis. The mismatch bounds include gains, offsets, and effective drive.

## Direct bound on midpoint means

The exact replay counts roots of the positive squared-frequency polynomial on [0,1), after factoring off zero roots and possible unit roots. It also verifies the maximum row and column sums of the absolute skew generators. Thus every positive mode satisfies 1≤ω≤8. For midpoint interval Δ=1/8 the mean of a unit cosine is sin(NωΔ)/(2N sin(ωΔ/2)). Here ωΔ/2 is in [1/16,1/2], so the denominator uses the rational sine lower bound s₀=1/16−(1/16)³/6. Nonstationary cosine weights sum to 61/80 for the refined target and 1 for each control, because each readout is normalized and collocated. The resulting worst pairwise loss is (141/80)/(512s₀). This uses the actual discrete grid.

Duhamel and contraction bound the loss from damping between ideal midpoint traces by γT. The mean nominal time is T/2. With jitter j≤1/1024, each ideal damped readout derivative has magnitude ≤9/4, as checked from ||Aq||²+γ². Hence jitter costs ≤(9/2)j per contrast. Dissipative realized generators with induced 2-norm error ≤η=1/4096, drive and sensor error ≤ε=1/512 each, and systematic mean bias ≤β=1/256 per trace cost at most 2(2ε+ε²+β)+η(T+2j).

The original readout noise assumption is independent centered sub-Gaussian samples across the three traces with proxy σ≤1/16 per sample. With N=256, one-sided adverse noise ≤1/32 holds for both comparisons with probability ≥1−2 exp(−16).

| Certificate quantity | Bound |
| --- | ---: |
| Ideal harmonic contrast | 19/80 |
| Midpoint oscillation loss | (141/80)/(512s₀) |
| Exterior damping loss | 1/16 |
| Jitter loss | 9/2048 |
| Mismatch and bias loss | 49169/2097152 |
| Adverse noise allowance | 1/32 |
| Guaranteed measured contrast vs. each control | 978548309/16095641600 |
| Headroom above 3/64 | 224065109/16095641600 |

Thus the lower bound is approximately 0.060796 versus the frozen gate 0.046875. The same union-bound failure probability applies, conditional on the stated assumptions. The earlier −1/320 was a lower bound on the contrast itself from the conservative four-leaf budget. The scoring gate is 3/64, and the older bound leaves a shortfall of 1/20 relative to it. This certificate applies to the stated one-leaf design. The contrast scorer remains synthetic-only.

Replay: `PYTHONDONTWRITEBYTECODE=1 python3 check_refined_window.py` with SymPy 1.14 in this directory.

## Run footer

- **Mission** — Certify the sampled one-leaf AW5 contrast with fixed exterior drives.
- **Done** — Froze the carrier and three probes, replayed the spectral factors and derivative bounds, and evaluated the uncertainty budget.
- **Finding** — Both contrasts clear the 3/64 margin under the declared model and noise assumptions.
- **Bridge value** — The refined test has a quantitative acquisition target for the identified carrier. Measured admission and independent hardware calibration remain open.

## Next step

1. **Priority 92/100** — Generate the three refined model packets through the frozen scorer, then bind the carrier and probe declarations to the independently audited hardware and calibration evidence.
