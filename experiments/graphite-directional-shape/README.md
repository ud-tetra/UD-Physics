# An amplitude-free direction and load test for a graphite passive control

**EXACT / CONDITIONAL within the equal three-mode passive model; EMPIRICAL comparison OPEN; UD residual OPEN.** This note extends the [two-dimensional first-star control](../graphite-2d-relaxation/README.md) used in [graphite paper v2](../graphite-manuscript-v2/README.md). It does not add a material law or claim a new measurement.

## Typed model and readout

Take the published rigid first-star potential of [Lebedeva *et al.*, arXiv:2511.01338v1, Eq. (2)](https://arxiv.org/html/2511.01338v1), with three equal-length reciprocal axes, `g_N=4π√N/(√3 a)`. Give each Fourier component the **assumed** identical independent Debye coordinate of the prior control, with stiffness `κ>0`, loss `η>0`, coupling `λ`, and relaxation time `τ=η/κ`. Let `C=λ² U₁,N² η/(2κ²)>0`, `v>0`, and `x=(g_N v τ)²≥0`. All energies and dissipated powers below are **per participating upper atom** at fixed contact, after steady phase/cycle averaging. Orient `φ=0` along one reciprocal vector and `φ=30°` relative to it. The squared direction cosines are respectively `(1,1/4,1/4)` and `(3/4,3/4,0)`.

For the velocity-odd dissipative power `P_φ=−F_d·v`, the exact normalized functions are

`f₀(x)=P₀/(C g_N² v²)=1/(1+x)+2/(4+x)` and

`f₃₀(x)=P₃₀/(C g_N² v²)=6/(4+3x)`.

The unknown amplitude `C`, contact atom count, and the PES coefficient cancel **only if the same participating contact and force readout apply to both directions at fixed pressure and speed**. The resulting ratio is

`R(x)=P₀/P₃₀=(x+2)(3x+4)/[2(x+1)(x+4)] = 1+x²/[2(x+1)(x+4)]`.

The same ratio applies to positive tangential dissipative force magnitudes `P/v` at equal speed. The identity `R′(x)=x(5x+8)/[2(x+1)²(x+4)²]>0` for `x>0` gives `1<R<3/2`, with endpoints `R(0)=1` and `lim_(x→∞)R=3/2`. In particular `R(1/4)=171/170`, `R(1)=21/20=1.05`, and `R(4)=6/5=1.20`. The small-speed excess is `R−1=x²/8+O(x³)`, or order `v⁴` in the ratio, consistent with a sixfold term of order `v⁶` in dissipated power. At zero coupling or loss (`C=0`) the observed power ratio is `0/0` and is not defined; the formula is a limiting **model shape**, not a zero-loss observable.

For a measured ratio `1<r<3/2`, the unique positive `x` solves `(3−2r)x²−10(r−1)x−8(r−1)=0`; the restricted model then infers `τ=√x/(g_N v)`. At `x=1`, `∂lnτ/∂r=100/13≈7.69` at fixed `g_N,v`. An illustrative absolute ratio error of `0.01` therefore linearizes to about `7.7%` relative uncertainty in `τ`, **before** contact, axis, background and model errors. This is a design sensitivity, not an achieved measurement precision.

## Pressure and cross-index restrictions

Define `K(x)=∂_(ln x) ln R=x²(5x+8)/[(x+1)(x+4)(3x²+10x+8)]`. At fixed speed,

`∂_P ln R=2K(x)[∂_P ln g_N+∂_P ln τ]`.

With fixed lattice scale and fixed index, `∂_P ln g_N=0`. At `x=1`, the logarithmic sensitivity to `τ` is exactly `2K(1)=13/105`. Thus the direction ratio can vary with pressure even when an overall drag amplitude has a small measured load slope because source, coupling, stiffness and loss contributions cancel there. Conversely, a flat measured ratio near `x≈1` constrains `∂_P ln τ` within this null if contact/readout and axis registration are controlled. The formula does **not** determine that derivative without measurements.

If the relaxation time `τ`, the contact geometry and star-axis conventions transfer unchanged between `N=7` and `N=13`, then `g_N²∝N` implies the amplitude-free horizontal collapse

`R₁₃(v)=R₇(√(13/7) v)`.

The published [Chen *et al.* PRL abstract](https://doi.org/10.1103/ly48-b4l2) reports that other commensurate patterns were below detection, so this cross-index test requires a sensitive force or local-loss readout. It is not already verified by the available friction peaks.

## Measurement and interpretation

Measure the dissipative tangential response at matched positive and negative velocities along directions separated by `30°` relative to the registered PES first-star axes, at the **same** contact area, pressure, speed and temperature. Subtract the apparatus and conservative registry contributions using a predeclared estimator. A velocity sweep then fits one time scale `τ` through `R((g_Nvτ)²)` without fitting the force amplitude; use distinct speeds and pressures as held-out checks. The inferred `τ` should be compared with an independent complex-response linewidth, and the source/contact assumptions should be tested. The `N=13` collapse is an additional challenge when its signal becomes detectable.

Edges, defects, direction-dependent contact, phonon-mode mixing, unequal relaxation times, nonlinear stick-slip and finite-window phase averaging can break this simple conventional null. Failure would reject one or more of its stated assumptions, **not establish UD**. Success would narrow the conventional baseline but likewise would not identify UD. An additive UD residual still needs independently sourced `S(w),R,K,D_h`, a contact map and a signed held-out force/load forecast. This null has no physical promotion or independent physics review.

Run `python3 experiments/graphite-directional-shape/replay_directional_shape.py`. The script checks the rational identities with exact integer polynomial arithmetic and exact sample fractions. See [receipt](../../candidates/graphite-directional-shape/mathematical_receipt.json) and [immutable capture](../../artifacts/graphshape-20261024-01/exact-002/manifest.json).
