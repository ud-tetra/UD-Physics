# Polynomial current clock on matched packets v0.1

**NUMERICAL / CONDITIONAL.** The tracked split survives with the continuous polynomial rate, but reverses sign relative to the normalized rate on these matched packets.

Discovery parent 9ee6da4a50e8518658c6617defd5b501c501d98d. Use [Matched packets v0.1](ISOSPECTRAL_CLOCK.md), [Local current clock v0.1](LOCAL_CURRENT_CLOCK.md), and [Tracked phase v0.1](TRACKED_CURRENT_CLOCK.md). Use the same linear scalar evolution, stock/current assignment, metric G, passive fixed-site clocks and radius-12 moving readout. Replace the excess phase rate by ||j||_G²/128. Choose common unit-amplitude total stock 10^8 in dimensionless model stock units for both packets. This arbitrary normalization makes phase differences readable numerically and does not fit a measured quantity. It changes neither the spectral match nor the trajectories. The coupling and stock convention set the reported phase scale.

**EXACT.** Linear propagation makes density and current scale as amplitude squared. Thus each accumulated site phase scales exactly as amplitude to the fourth power. The normalized window weights are invariant under the same scaling. Writing q=a^4, its phasor is therefore the window expectation of exp(i q phi) with unit-amplitude site phases phi. For a finite window, near q=0 the local phase branch is q times the window mean of phi plus O(q³), by Taylor expansion and conjugation symmetry. Fourth-power scaling of the circular readout is a small-phase result and need not hold at large phase spread.

**NUMERICAL.** The finer order-12, step-1/8 replay at native time 12 gives:

| Amplitude | Diagonal minus axis (rad) |
| ---: | ---: |
| 1/4 | −0.00004166978 |
| 1/2 | −0.00066671651 |
| 1 | −0.01066746423 |
| 2 | −0.17067942769 |

The split divided by a^4 varies by less than 6×10⁻¹³ rad across the finer sweep. The two refinement runs differ in that coefficient by about 1.1×10⁻⁹ rad. The minimum final contrast exceeds 0.9999999. Equal total stock does not fix local stock. At s=12 the diagonal window collects about 2.16×10⁻⁵ of its launch stock against 7.47×10⁻⁵ for the axis window. The measured site phase integrates current squared, including its local density-squared factor, over the full history. The reversed ordering rules out inferring a universal speed ordering from this pair under this rule. Independent review NOT_RUN. Physical promotion 0.

Replay with `OPENBLAS_NUM_THREADS=1 python3 experiments/clock-matrix-question/polynomial_clock.py`.
