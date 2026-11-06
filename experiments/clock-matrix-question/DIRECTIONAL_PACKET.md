# Directional packet and moving phase readout v0.1

**NUMERICAL / CONDITIONAL.** A positive-frequency scalar packet on the existing periodic carrier moves and preserves a readable carrier phase over the sampled native times. The phase belongs to the propagation mode. A separately evolving carried clock remains open.

## Model and readouts

Discovery parent 3a492e1cd28a791170a5c7b60e270bb63b7d41a1. Use the [macrocell dispersion audit](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/Docs/UD%20cubic%20macrocell%20metric%20and%20propagation%20audit.md), Periodic scalar propagation, and the [BCC observation audit](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/Docs/UD%20BCC%20observation%20clock%20and%20causality%20audit.md), Vertex observation. Compare the reflection-symmetric launch in [Periodic clock v0.1](PERIODIC_CLOCK.md).

Use cubic periodic grids of odd side 65 and 97, the same unit-incidence scalar symbol, complex vertex amplitude u and its gradient-edge quadrature. With Fourier convention exp(i k·r), supply vertex amplitude a(k) and velocity quadrature −iω(k)a(k), then evolve u_hat(k,s)=a(k)exp(−iωs), ω²=2Σ_d(1−cos(k·d)) over the seven nonzero binary d. Complex amplitudes encode two real solutions. For A=d−dᵀ the compatible edge amplitude is −i B₁* a/ω, well-defined on the spectral support. This realizes the source scalar lane on the torus. Time is dimensionless and displacement is in translation coordinates. No fitted rate law or separate clock coupling enters.

Choose k₀=±(π/3,0,0), Gaussian spectral amplitude of width 9/50 or 3/25, multiplied by a raised cosine taper between radii 9/20 and 13/20 about k₀. These are design choices. For the independent position readout, take the centered-chart centroid X of |u|² and the fraction inside Euclidean coordinate radius 12 about X. This is vertex signal stock, distinct from total chain stock and physical distance. Compare X(s) with s times the spectral mean of ∇ω weighted by |a|². On the infinite lattice for this tapered amplitude the mean formula follows from the Fourier position operator i∂k. On the finite torus it is a diagnostic against boundary and discretization effects, not an exact equality for the chart centroid.

For the phase port use W=exp(−|r−X|²/72), Z=Σ W u exp[−ik₀·(r−X)]. Report coherence |Z|/Σ W|u| and the principal phase residual relative to −ω(k₀)s+k₀·X. The latter compares to an already specified dispersion model and reports only the sampled phase modulo 2π. Coherence measures phase alignment after removing the spatial carrier, not clock accuracy.

## Results and controls

Sample native times 0, 4, 8, 12. At s=12 on the 97³ grid:

| Spectral width | Centroid | Signal inside radius 12 | Phase coherence | Phase residual (rad) |
| --- | --- | ---: | ---: | ---: |
| 9/50 | (20.41371, 10.02249, 10.02249) | 0.94891 | 0.97287 | −0.15699 |
| 3/25 | (20.62244, 10.22782, 10.22782) | 0.73979 | 0.99733 | −0.10025 |

The centroid residual versus spectral prediction is below 0.00014 at all four sampled times on the larger grid. The smaller grid differs from its prediction by about 0.091 at s=12, consistent with wraparound in the centered chart. On 65³, reversing k₀ reverses the centroid and leaves the phase residual unchanged to the tested numerical tolerance. An initial even-grid check failed a strict inversion assertion because the chosen centered coordinate chart has an unmatched endpoint. Odd grids make the chart reflection symmetric. The two grid sizes are finite checks, not a convergence proof.

Bandwidth changes the phase residual and the localization fraction with the same generator and carrier. This is an ordinary dispersive phase effect in a constructed packet. The directional branch passes the transport and readable carrier-phase tests at these checkpoints. It supplies no independent internal clock and no physical time-dilation comparison. Next isolate an internal phase in a separate port and compare a stationary reference at matched preparation. Physical promotion 0. Non-constructor review NOT_RUN.

Replay with Python 3 and NumPy: `python3 experiments/clock-matrix-question/directional_packet.py`. The committed JSON records the 16 observations.
