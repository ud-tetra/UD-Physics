# Same-spectrum shape control for the polynomial clock v0.1

**NUMERICAL / CONDITIONAL.** A spectral phase chirp changes the tracked clock phase at fixed central mode and group velocity. The change survives a density-only preparation fit and a common-density readout control.

Discovery parent 5344e640a819a2288f10e68daf55e0626f67f890. Retain [Local density matching v0.1](DENSITY_MATCHED_CLOCK.md), its fixed-site clock histories, terminal radius-12 axis window and unchirped axis baseline. In the same axis spectral chart multiply the initial spectrum by exp(i c p²) with c=−2 or +2 and p the existing standardized frequency-chart coordinate. These are fixed exploratory shape choices. The phase factor changes the coherent packet while preserving squared spectral amplitude. Thus its normalized frequency law, central group velocity, and spectral-mean centroid velocity agree exactly with the baseline under linear evolution. This does not assume identical centroids at launch. The terminal windows retain the same fixed lattice sites for all controls.

Apply a single stock multiplier per chirped preparation by least squares on the site-time density arrays only. No phase is used to fit it. The multiplier changes total launch stock and preserves normalized spectral weights. On the finer order-12, step-1/8 replay at native time 12:

| Chirp | Relative L2 density mismatch | Maximum pointwise mismatch | Fitted phase change (rad) | Common-density phase change (rad) |
| ---: | ---: | ---: | ---: | ---: |
| −2 | 0.01327% | 0.06149% | −6.73508×10⁻⁷ | −6.67047×10⁻⁷ |
| +2 | 0.00543% | 0.03354% | +7.61763×10⁻⁷ | +7.65656×10⁻⁷ |

The common-density control substitutes the baseline density history and terminal weights while retaining the chirped normalized local current. It is an algebraic diagnostic, not a separately evolved packet. The two resolutions agree within 4.1×10⁻⁹ rad for the fitted changes and 1.8×10⁻¹⁰ rad for the common-density changes. These checks do not certify a numerical error bound. The observed phase sensitivity to coherent shape persists after controlling for sampled density and centroid velocity. This is a numerical counterexample to interpreting the tested rule as a function of centroid speed and stock history alone, with the exact-stock substitution scoped to the diagnostic. Physical promotion 0. Independent review NOT_RUN.

Replay with `OPENBLAS_NUM_THREADS=1 python3 experiments/clock-matrix-question/shape_matched_clock.py`.
