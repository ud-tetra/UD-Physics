# Two-dimensional first-star passive control for graphite

**EXACT / CONDITIONAL conventional null; source-rounded contrast; UD residual OPEN.** This lifts the [one-dimensional passive control](../graphite-relaxation-null/README.md) to the published first spatial Fourier star. It supplies a direction-resolved force law under a deliberately simple loss model, so a proposed UD contribution has a concrete conventional comparison. It does not turn a DFT static PES into measured kinetic friction.

## Published PES and typed model

Lebedeva *et al.*, [arXiv:2511.01338v1](https://arxiv.org/html/2511.01338v1), Eq. (2), write the two-dimensional PES per upper atom as `U₁[2 cos(k_y y)cos(k_x x)+cos(2k_y y)]`. The three equal-length reciprocal vectors can be chosen `g₁=(k_x,k_y)`, `g₂=(−k_x,k_y)`, `g₃=(0,2k_y)`, with `k_x=√3 k_y`, `|g_j|=g_N=4π√N/(√3 a)` and `N=m²+mn+n²`. A global rotation of all vectors changes only the reference direction. Their Table 4 gives **rigid** first-star coefficients `U₁,7=+0.0793` and `U₁,13=−0.00598 µeV/atom`. The opposite signs indicate different PES types; the simple quadratic loss below depends on their squares. These are DFT-derived values, not the Chen *et al.* kinetic force traces. The source reports 2.0% and 3.3% RMS fitting deviations relative to PES corrugation, which are not error bars on the coefficients.

Take three independent dimensionless internal coordinates `q_j`, each with identical stiffness `κ>0`, Rayleigh loss `η≥0`, and real coupling `λ` to its own Fourier component. At fixed pressure, assume energy per upper atom

`E(r,q)=U₀(r)+Σ_j [κ q_j²/2−λ U₁ q_j cos(g_j·r)]`, `η q̇_j=−∂_(q_j)E`, `r(t)=r₀+v t`.

`U₀` is the rigid conservative PES and `τ=η/κ`. Use physical time, length, and energy per participating upper atom as in the preceding scalar control. This is an **assumed conventional bath**, not a UD-sourced current, mode, clock, or graphite damping measurement. It has three independent loss coordinates with identical parameters and no mode mixing. If one uses an already relaxed PES for `U₀`, its relaxation contribution must not be counted again. A fixed contact and prescribed steady translation omit stick-slip, defects, edges, thermal activation and apparatus compliance.

## Exact velocity-odd drag and passivity

For each `ω_j=g_j·v`, the steady coordinate is `q_j=(λU₁/κ)[cos(φ_j)+ω_jτ sin(φ_j)]/[1+(ω_jτ)²]`, `φ_j=g_j·r(t)`. The **dissipative, phase-averaged** force is

`F_d(v)=−C Σ_j g_j(g_j·v)/[1+τ²(g_j·v)²]`, `C=λ²U₁²τ/(2κ)=λ²U₁²η/(2κ²)≥0`.

Consequently `−F_d·v=C Σ_j (g_j·v)²/[1+τ²(g_j·v)²]≥0`. If `g_j·v=0`, that mode contributes no dissipated power; a fixed initial transverse registry can retain a **conservative transverse force** omitted from `F_d`. The dissipative force formula is exact for independent modes after phase/cycle averaging, or after averaging initial registry for stationary modes. It is not a complete total-force trajectory. The conservative `U₀` contributes zero *work per period* on a closed periodic sliding path; for a nonclosing irrational direction, use spatial phase/long-time averaging with the relevant conditions.

At low speed, the first-star dyad identity is `Σ_j g_j g_jᵀ=(3g_N²/2) I₂`. Hence the viscous tensor is isotropic:

`Γ_N^0=(3λ²η U₁,N² g_N²/(4κ²)) I₂`.

This result holds for the stated **equal independent loss channels**. C3/C6 symmetry also constrains a linear, symmetry-preserving rank-two dissipative tensor to be isotropic, but its scalar coefficient is not generally this one if the bath mixes modes.

## Directional onset and exact replay

Let `φ` be the velocity direction relative to a first-star reciprocal-vector axis, `z=g_N|v|τ`, and `P_d=−F_d·v`. Character sums over the three axes give the exact low-`z` series

`P_d/(C g_N² |v|²)=3/2−(9/8)z²+[15/16+(3/32)cos(6φ)]z⁴+O(z⁶)`.

The first directional term is of order `|v|⁶` in dissipated **power**, equivalently order `|v|⁵` in dissipative **force**. The direction-sensitive tangential force begins `F_φ=(3/32)C g_N² |v| z⁴ sin(6φ)+O(|v|z⁶)`. A low-speed direction-dependent linear drag within a truly C3-preserving contact would therefore falsify this equal-star null or its symmetry assumptions; it would not, by itself, identify UD.

Run `python3 experiments/graphite-2d-relaxation/replay_two_dimensional.py`. Exact rational squared direction cosines give moments `(3/2,9/8,33/32)` along a wavevector and `(3/2,9/8,27/32)` at 30°. At `z=1`, normalized dissipated powers are `9/10` and `6/7` respectively. The check also constructs the isotropic dyad without floating rounding. [Immutable capture](../../artifacts/graph2d-20261024-c829/exact-001/manifest.json) and [mathematical receipt](../../candidates/graphite-2d-relaxation/mathematical_receipt.json).

## Source-rounded angle contrast and load response

If `λ,η,κ`, per-atom contact transfer and the low-speed regime are the **same** for N=7 and N=13, then Table 4 and `g_N²∝N` yield

`Γ_7^0/Γ_13^0=(0.0793/0.00598)²(7/13)=651175/6877≈94.688818`.

This is a **conditional ratio of this model's per-atom low-speed viscous coefficients**, calculated from rounded DFT first-star coefficients. It is not a measured kinetic ratio, bound, UD contribution or prediction for an AFM contact. It differs sharply from the preceding **4.33** scalar-cut surrogate, which equated the coupling's gradient amplitude to the rigid minimum-energy-path ideal shear strength. The first-star mode coupling uses the three full Fourier gradients instead; the two transfer assumptions are inequivalent, especially because the `(2,1)` and `(3,1)` PESs have opposite types. The fact that two plausible conventional transfers give different ratios is an **identifiability warning**, not evidence favoring one.

For positive nonzero coefficients at fixed N, the low-speed logarithmic load slope is `∂_P ln γ_N^0 = 2∂_P ln|U₁,N| +2∂_P ln|λ| + ∂_P ln η −2∂_P ln κ +2∂_P ln g_N`. The last term is zero if the lattice scale is fixed under pressure. No source supplies these derivatives for the specific contact. At finite velocity, the response depends on `g_N|v|τ` and slide direction, so even a shared bath does not preserve the 94.69 ratio. A near-zero measured load slope constrains the full combination; it cannot be inferred from PES amplitude alone.

## Gate to a UD paper claim

The primary PRL [public abstract](https://doi.org/10.1103/ly48-b4l2) reports detectable peaks at 21.8°/38.2°, weak load dependence, and other commensurate patterns below detection. It does not provide the force curves or threshold in this access path. The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` Q22 leaves nonuniform stiffness unsourced; Q77–Q84 phase kernels do not identify the three graphite loss channels. Before assigning a residual to UD, freeze a contact-resolved two-dimensional conventional PES and measured complex loss matrix, include mode mixing and load derivatives, and forecast the same signed force observable at the paired angles and controls. A separately specified UD response must improve a held-out comparison. Independent physics review NOT_RUN; physical promotion 0.
