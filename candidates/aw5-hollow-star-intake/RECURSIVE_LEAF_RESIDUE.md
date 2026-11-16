# AW5 uniform recursive leaf subdivision

**EXACT / CONDITIONAL. Physical Promotion = 0.** Use the same twelve exterior faces, ascending simplex orientations, signed incidence and unit simplex metric. Start at depth zero with one tetrahedron per leaf. At each depth, stellarly subdivide every current tetrahedron inside the leaf once, fixing its boundary. The four leaf depths may differ. The cavity remains b₂=1. No fit or physical map enters.

## Exact four-terminal reduction

With coherently oriented top cells, the squared chain norm of z−B₃x is a sum of (x_i−x_j)² over internal faces and (z_f−x_i)² over boundary faces. Here z is the cavity shell and z_f gives its signed boundary-face data in the coherent boundary coordinates. The minimization is therefore a unit-resistor network on the dual graph with four terminal loads per original leaf. The residual h=z−B₃x at the minimum is the harmonic representative. The terminal currents are the four oriented boundary coefficients of h.

At depth d, symmetry forces the four-terminal response to be α_d(4I−J). This is electrically equivalent at its ports to a star with four identical arms of resistance R_d=1/(4α_d). Depth zero has R₀=1. Each terminal has a physical unit-resistance edge in series with its internal network. Removing those edges leaves an equivalent star with arms R_d−1, with zero arms at depth zero understood as a common junction. In the next subdivision use four such stripped networks. Connect the pair of corresponding inner ports for each neighboring child through the single unit edge of the shared face. Put back one unit edge at each exterior terminal. The resulting equivalent network has R_d from each exterior terminal to its child center and 2R_d−1 on each edge of the complete graph of child centers. On its zero-sum subspace the center admittance is 4/(2R_d−1), so the terminal differential resistance is

```text
R_(d+1) = R_d + (2R_d−1)/4
R_d     = (1+(3/2)^d)/2
α_d     = 1/[2(1+(3/2)^d)].
```

The cavity terminal coefficient magnitude in each leaf is 3α_d and the three exterior magnitudes are α_d, with the original orientation signs. For depths d_i, the harmonic norm squared is zᵀh=3 Σ_i α_(d_i). The original signed exterior drive has twelve coefficients of magnitude 1/√12, so its normalized stationary residue is (Σ_i α_(d_i))/4. The best aligned unit exterior drive has residue (Σ_i α_(d_i)²)/(Σ_i α_(d_i)). With equal depths both reduce to α_d. The degree-2 heat trace still tends to one, while α_d→0 with depth.

| Uniform depth | Stationary residue |
| ---: | ---: |
| 0 | 1/4 |
| 1 | 1/5 |
| 2 | 2/13 |
| 3 | 4/35 |
| 4 | 8/97 |
| 5 | 16/275 |
| 6 | 32/793 |

Depth six is the first equal depth where the **ideal stationary residue** falls below 3/64. This establishes a vanishing-amplitude result at fixed topology and fixed probes. The stationary value does not determine the recorded 32-unit finite-window verdict. Positive modes can contribute on that window and damping changes the late-time response. The split-metric theorem concerns different metric and readout choices.

Replay with `python3 check_recursive_leaf_residue.py`. Exact Schur complements verify depths 0–3 against the induction formula. The separately derived [finite-window certificate](REFINEMENT_SWEEP_WINDOW_CERTIFICATE.md) covers the 16 first-level subsets and uniform depths two and three.

## Run footer

- **Mission** — Determine whether the exterior harmonic signal has a depth-independent floor under unit weights.
- **Done** — Reduced each refined leaf to a symmetric four-terminal network and verified the recursion with exact incidence-based Schur complements.
- **Finding** — The residue can approach zero at fixed b₂=1. The ideal stationary residue first falls below 3/64 at uniform depth six.
- **Bridge value** — This gives a mathematical limit on extrapolating the first-level acquisition result to deeper carriers.

## Next step

1. **Priority 92/100** — Extend the four-terminal reduction to frequency-dependent response and use it to certify the original midpoint window at depth two and beyond.
