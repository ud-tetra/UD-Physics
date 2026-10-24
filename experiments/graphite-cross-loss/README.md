# Passive cross-mode loss bounds for the graphite linewidth transfer

**Status: EXACT / CONDITIONAL operator bound; NUMERICAL replay of an archived conventional model; no measured loss or force.** This audits the diagonal assumption in the [linewidth transfer](../graphite-linewidth-transfer/README.md). The 21.8° and 38.2° paired geometry is inherited from the [graphite hypothesis](../graphite-superlubricity/README.md); the calculation below does not derive friction at those angles or identify a UD-specific material coupling.

## Question and model

How much scalar low-frequency drag is determined by the widths of the two laterally active E-mode pairs if the dissipative bath couples them? Use the stationary conventional KC-plus-1.44 eV plate model already archived at cutoffs 14, 16 and 18 Å. Its lower sheet is fixed, its 14 upper heights use one carbon mass each, and energy is per upper atom. Let `x∈R²` be lateral displacement, `h∈R¹⁴` vertical displacement, `K` the positive height Hessian, `C` the lateral-height coupling, and `D⪰0` a *separately supplied* Rayleigh matrix, with Fourier convention `e^(−iωt)`. The low-frequency Schur drag is `Γ=C K⁻¹ D K⁻¹ Cᵀ`, with scalar `γ=tr(Γ)/2` in meV·ps·Å⁻² per upper atom. A finite closed `D=0` bath gives zero Ohmic drag.

Restrict to the two active, approximately degenerate, real two-dimensional pairs `L` and `H`. In their orthonormal conservative-mode basis write

`D_active = [[d_L I₂, X], [Xᵀ, d_H I₂]]`, `d_L,d_H≥0`.

The diagonal blocks assume equal weak dissipative width within each pair. The off-diagonal real `2×2` block `X` remains unknown; no measured linewidth is inserted. Let `B_i=C_i/κ_i` in the ideal pair-degenerate reduction and `a_i=||B_i||_F²/2`. The archived numerical pair weights are unchanged from the prior linewidth transfer. For weak, resolved power peaks, `d_i≈2πm_eff Δf_i`, with `Δf_i` a *dissipative FWHM* in THz after deconvolution. Here `m_eff=m_C/14≈0.08883659715` meV·ps²·Å⁻² per upper atom, and `c_i=2πm_eff a_i` is a coefficient per THz. The small archived splitting inside each E pair is numerical; the bound can also be formulated without exact degeneracy using the measured Frobenius norms of the respective `CK⁻¹` subblocks.

## Bound and constructive ambiguity

Passivity of `D_active` implies `||X||₂≤√(d_L d_H)` by the Schur complement (also valid at zero diagonal damping by continuity). The cross contribution to `γ` is `tr(B_L X B_Hᵀ)`. Matrix Cauchy–Schwarz therefore gives the **pointwise envelope**

`(√(c_L Δf_L)−√(c_H Δf_H))² ≤ γ ≤ (√(c_L Δf_L)+√(c_H Δf_H))²`.

This is a universal bound for the specified pair norms and passive block structure. It is sharp over compatible two-pair couplings: choose `B_i=√a_i I₂` and `X=ρ√(d_Ld_H)I₂`, `−1≤ρ≤1`. Then `D` has nonnegative eigenvalues and

`γ(ρ)=c_L Δf_L+c_H Δf_H+2ρ√(c_Lc_H Δf_LΔf_H)`.

The three choices `ρ=−1,0,+1` have the **same diagonal pair linewidth parameters** and distinct drags. The archived scalar pair weights alone do not establish that both endpoints are reachable by the archive's unreported full coupling matrices; the envelope is rigorous, and sharpness refers to the compatible model family. If C3 symmetry is imposed exactly on both pairs, each lateral coupling map is a scale times an in-plane rotation, and a symmetry-allowed cross block can align to saturate the envelope. Resolving the actual complex cross response would narrow it.

At the 16 Å reference, the prior diagonal transfer has `c_L=2.7634530847×10⁻⁴` and `c_H=1.8676114422×10⁻⁵` meV·ps·Å⁻² per upper atom per THz. For *equal symbolic widths* `Δf_L=Δf_H=Δf` the numerical coefficient interval is

`γ/Δf ∈ [1.5134043457×10⁻⁴, 4.3870241120×10⁻⁴]` in those units.

The diagonal center is `2.9502142289×10⁻⁴`; cross loss changes it by at most `1.4368098832×10⁻⁴`, or **48.7018830%**. The earlier 93.6696% low-pair share holds for diagonal `D` only; with cross loss, assigning the cross term to one pair has no unique meaning. These numbers are transfer coefficients, not a physical choice of 1 THz width.

At each archived pressure offset a similar envelope is calculable. It does **not** bound the local pressure derivative: even with constant `d_L,d_H`, choose the admissible smooth `ρ(P)=sin(k(P−P₀))`. At `P₀`, the same measured diagonal widths and `ρ(P₀)=0` yield an extra derivative `2k√(c_Lc_H Δf_LΔf_H)`, whose sign and magnitude vary with the unmeasured cross response. Large `k` requires a narrow pressure scale; no such scale is supplied. Thus the prior constant-width `+8.06052×10⁻⁴ MPa⁻¹` logarithmic slope is conditional on no cross loss and cannot be promoted to a load-response prediction. Pointwise 14/16/18 Å replay stability only checks the archived conventional model.

## Measurement gate

Measure the pressure-resolved **complex** dissipative response of both active pairs, including the cross-mode self-energy and its pressure derivative, at a declared contact, temperature and registry. Separately establish a conventional lateral-height baseline, then test any additive UD coupling after baseline subtraction with a signed kinetic force/load trace at the paired angles and comparison angles. The available diagonal widths alone, even if later measured exactly, cannot fix the residual drag or its load slope. Physical UD source, damping, clock map and force readout remain OPEN; independent physics review NOT_RUN; mainline physical promotion 0.

Run `python3 experiments/graphite-cross-loss/replay_cross_loss.py` for the archived pair sums, all three cutoff envelopes, pressure pointwise intervals, and explicit passive extremizers. The immutable [capture](../../artifacts/graphmix-20261023-ebafdc59/exact-001/manifest.json) and [mathematical receipt](../../candidates/graphite-cross-loss/mathematical_receipt.json) specify provenance, conventions, and limitations.
