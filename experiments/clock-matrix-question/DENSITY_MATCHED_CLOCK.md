# Local density matching for the polynomial clock v0.1

**NUMERICAL / CONDITIONAL.** Matching local stock histories with a single amplitude adjustment restores faster-packet phase ordering for the tested pair.

Discovery parent a9e36e8e2f7314bdc5a7c41b85d586ac9a6487fe. Retain [Polynomial clock v0.1](POLYNOMIAL_CLOCK.md) and the equal-frequency charts from [Isospectral clock](ISOSPECTRAL_CLOCK.md). Hold the coupling and linear dispersion fixed. At native time 12, center equal radius-12 lattice masks on each rounded predicted centroid, (9,4,4) and (10,10,10). Pair sites by their integer offsets from these centers. Compare the full histories of those fixed sites from time zero to 12, since the terminal detector reads fixed-site clocks. The rounded centers permit exact pairing of sites and differ slightly from the previous fractional-center masks.

Choose one positive diagonal stock multiplier by minimizing squared stock mismatch over all sampled site-time pairs. The closed-form multiplier is the inner product of the stock arrays divided by the squared norm of the diagonal array. This uses stock data only. Scaling the initial diagonal amplitude by the square root of the multiplier leaves the normalized frequency distribution and trajectory unchanged, but changes the total launch stock. This is a numerical preparation fit, not a held-out test or an exact density match.

At quadrature order 12 and time step 1/8, the stock multiplier is 3.44550855. The relative L2 mismatch is 0.09682% and the maximum pointwise mismatch relative to axis stock is 0.49376% on the sampled histories. The equal-total-stock split is −0.01066648 rad (diagonal minus axis). After matching it is +0.01256919 rad. Order 8 and step 1/4 reproduce the sign and differ by approximately 1.21×10⁻⁹ rad in the matched split.

As a readout-only counterfactual, replace the diagonal stock history and terminal weights with the exact axis arrays while retaining the diagonal normalized current-squared rate. This gives +0.01256924 rad, within 5.3×10⁻⁸ rad of the amplitude-adjusted result. The substitution is not a propagated packet. It separates the numerical effect of residual stock mismatch from the normalized current contribution for this pair. A different shape can change that normalized current contribution, and these runs do not establish a universal speed law. No hardware data or physical calibration. Physical promotion 0.

Replay with `OPENBLAS_NUM_THREADS=1 python3 experiments/clock-matrix-question/density_matched_clock.py`.
