# AW5 sampled acquisition sprint

**EXACT / CONDITIONAL** for deterministic bounds. **PROBABILISTIC / CONDITIONAL** for the noise guarantee. Agile hypothesis, target exposure recorded, zero fitted parameters. Physical calibration and independent review remain open. **Physical Promotion = 0.** This work builds on WEAK_DAMPING_WINDOW.md.

Use the aligned hollow, same-pattern filled, and orthogonal-pattern hollow traces, with separate acquisition noise per trace. Set T=32, 0≤γ≤1/512 and N=256 saved midpoint samples per trace. The nominal grid is t_k=(k+1/2)T/N for k=0,…,N−1. Define the statistic as the arithmetic mean of each signed impulse-response trace. Compare the aligned hollow mean separately to each control mean.

## Sampling and time errors

For the ideal collocated response f(t)=qᵀexp(tG)q, contraction gives |f′|≤||Gq|| and |f″|≤||Gᵀq||||Gq||. Both squared norms equal ||Aq||²+γ²||Pq||² because the source is face-only and A changes degree. The exact filled and hollow spectra give ||A||²=5+√5, so the squared norms are less than 29/4 and each first derivative bound is less than 27/10. For sample interval Δ=T/N and timing error at most j per sample, the worst contrast loss is at most (29/48)Δ²+(27/5)j. This follows from the composite midpoint remainder and the mean value bound on each trace. At j≤1/1024 the loss is less than 1/64. Sample times remain nonnegative. This is a sufficient grid for this mean statistic.

## Channel and dynamics mismatch

In the unit simplex norm, let the actual input and readout vectors b and c each deviate from the declared q by at most ε. Let the realized generator G̃ be dissipative in the same norm and satisfy ||G̃−G||≤η. Contraction and Duhamel give pointwise loss at most 2ε+ε²+ηt. Each trace also allows an additive systematic mean bias of magnitude at most β. Comparing two traces on the jittered grid costs at most 2(2ε+ε²+β)+η(T+2j). Use ε≤1/512, η≤1/4096 and β≤1/256. The combined loss is less than 1/32. These are bounds to verify independently against the specified operator, drive, readout, and offset.

## Simultaneous noise guarantee

Assume independent centered sample errors across all three traces and time indices, each with moment generating function bounded by exp(σ²t²/2) for all real t, with σ≤1/16. Each pairwise difference of N-point noise means has variance proxy 2σ²/N. Its probability of reducing the contrast by at least a is at most exp(−Na²/(4σ²)). With a=1/32 the exponent is at least 16. A union bound gives failure probability at most 2 exp(−16) for the two comparisons together. The contrasts share the hollow trace, and the union bound permits this dependence. Temporal drift and correlated errors require a separate bound.

## Joint acquisition specification

| Quantity | Sufficient model-level value |
| --- | --- |
| Window and samples | 32 native time units, 256 midpoint samples per trace |
| Nominal spacing, timing deviation | 1/8, at most 1/1024 |
| Exterior damping | At most 1/512 per trace |
| Drive and sensor vector error | At most 1/512 each |
| Generator mismatch and mean bias | At most 1/4096 and 1/256 per trace |
| Sub-Gaussian readout scale | At most 1/16 |
| Simultaneous contrast lower bound | 3/64 with failure probability at most 2 exp(−16) |

The final bound subtracts the sampling, mismatch, and adverse noise allowances from the continuous-time margin 1/8. It uses the specified impulsive preparation and signed mean. These are sufficient tolerances in native units. Hardware realization, calibrated units, noise independence, and dissipativity still require evidence.

## Run footer

- **Mission** — Convert the finite-window AW5 contrast into a sampled acquisition specification.
- **Done** — Derived independent sampling, mismatch, and noise bounds and checked their joint rational budget.
- **Finding** — The declared tolerances preserve at least 3/64 signed contrast against both controls with failure probability at most 2 exp(−16).
- **Bridge value** — The specification defines which quantities an engineered realization must certify before comparing the three responses.

## Next step

1. **Priority 90/100** — Build a target-blind synthetic intake scorer with separate timing, offset, noise, and operator certificates. Replay passing, failing, and correlated-noise controls before admitting a measured dataset.
