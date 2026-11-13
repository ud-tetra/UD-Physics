# Tracked clock window and phasor error budget v0.1

**NUMERICAL / CONDITIONAL.** Increasing the radius from 3 to 12 raises the smaller captured stock fraction about 69-fold while preserving the ideal phase split. The radius-12 detector still captures a small fraction of each packet.

## Aperture sweep

Discovery parent db3e2918d165b497fe27fc76648fac6cf2c030b4. Keep the passive site-clock dynamics, equal-frequency preparations, spectral centroid tracks, and stock-weighted phasor of [Tracked current clock v0.1](TRACKED_CURRENT_CLOCK.md). Use hard spherical windows of Euclidean coordinate radius 3, 6, and 12. Integrate clocks at the union of sites sampled by the largest window. Compare Gauss order 8 and trapezoid step 1/4 with order 12 and step 1/8. The default radius-three replay is byte-identical after the window parameterization. No dynamics, coupling, or metric was refitted.

Finer replay at native time 12:

| Radius | Axis captured fraction | Diagonal captured fraction | Phase split (rad) | Common additive error / total stock |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 1.20021×10⁻⁶ | 3.15076×10⁻⁷ | 0.01177997 | 9.27895×10⁻¹⁰ |
| 6 | 9.48535×10⁻⁶ | 2.73032×10⁻⁶ | 0.01177997 | 8.04077×10⁻⁹ |
| 12 | 7.47294×10⁻⁵ | 2.16073×10⁻⁵ | 0.01177997 | 6.36332×10⁻⁸ |

Ideal phase contrast is unity to displayed precision throughout. The numbers are numerical estimates. The two joint refinements agree at displayed precision but do not certify a continuum or temporal integration error.

## Deterministic noise contract

Let U=ΣWρ exp(iφ) be the unnormalized complex readout, S=ΣWρ its window stock, and N the total stock of that launch. Contrast C=|U|/S. Suppose the measured complex readout is U+e. Hold detector position and window fixed and include numerator readout errors in e. For |e|<|U| the disk about U has angular half-width arcsin(|e|/|U|), by the tangent construction. If the noiseless phase gap is Δ∈(0,π/2), require each channel's error magnitude to be at most |U|sin(Δ/4). Then each phase changes by at most Δ/4 and at least Δ/2 of the gap survives. This is an exact conditional bound for the specified error model. It is a sufficient budget with a half-gap reserve, not the sign-only threshold or a probability-of-detection estimate.

The common budget expressed relative to each launch's total stock is min(C_A S_A/N_A, C_D S_D/N_D)sin(Δ/4). Radius 12 admits about 6.36×10⁻⁸ of total stock per channel, or a common budget of about 0.2945% of each channel's captured stock. The normalized readout phase does not depend on a positive real denominator. Tracking errors, calibration, correlated quadrature noise, and actual gain mapping are outside this contract. No instrument performance is inferred.

Replay with `OPENBLAS_NUM_THREADS=1 python3 experiments/clock-matrix-question/window_noise.py`. Physical promotion 0. Independent review NOT_RUN.
