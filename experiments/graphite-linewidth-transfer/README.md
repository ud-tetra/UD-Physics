# From material mode linewidths to a conditional graphite drag coefficient

**Status: CONDITIONAL / NUMERICAL replay of an archived conventional KC-plus-plate model; measured linewidths OPEN; UD-specific damping OPEN.** This follows the [four-site source test](../graphite-source-constraints/README.md) and the [passive-port attribution limit](../graphite-port-attribution/README.md). The paired friction angles and weak load response were known before this calculation and are not fitted here.

## Typed low-frequency reduction

In the archived stationary 14-height model, `x∈R²` is the lateral displacement in Å, `h∈R¹⁴` contains upper-site vertical heights in Å, and the **energy is per upper atom** in meV. The clamped lateral-height coupling `C` and positive height stiffness `K` are conventional KC-plus-plate quantities at the chosen stationary registry. The illustrative plate stiffness is 1.44 eV, the lower sheet is rigid, and each upper site is assigned one 12C mass. In these per-atom coordinates `m_eff=m_C/14≈0.08883659715 meV ps² Å⁻²`. The archive's 16 Å cutoff has two laterally active E-mode pairs near 9.3709 and 25.5937 THz. These are model frequencies, not measured graphite phonons.

The **closed finite harmonic** bath has reversible poles and exactly zero low-frequency Ohmic drag in this model. To make a conditional *open* model, assume that an independently measured, dissipative Rayleigh matrix `D` is diagonal in the archived conservative normal-mode basis. With Fourier convention `e^(−iωt)`, a mode has denominator `κ_j−m_eff ω²−iω d_j`, where `d_j≥0` has units meV ps Å⁻² per upper atom. Eliminating the heights yields

`Γ_add = C K⁻¹ D K⁻¹ Cᵀ`, and `γ_scalar = (1/2) tr Γ_add = Σ_j a_j d_j`,

where `a_j=||C v_j||²/(2κ_j²)` is the **archived conventional** modal weight. The formula is a low-frequency damping coefficient for a specified moving-coordinate model, not yet the measured kinetic friction force. A purely numerical broadening of finite lines must not be inserted as `d_j`.

For a resolved weakly damped spectral peak, define `Δf_j` as the **dissipative power-spectrum full width at half maximum** in cycles/ps (THz), after deconvolving finite observation time and instrumental broadening. Then `d_j≈2π m_eff Δf_j`. This is the high-Q linewidth approximation; a broad or overlapping pair requires fitting the full retarded response rather than reading off a peak width. Assuming equal widths within each E pair, `Δf_L` and `Δf_H`, the archived 16 Å model gives the ready-to-calibrate equation

`γ_scalar ≈ (2.7634530847×10⁻⁴ Δf_L + 1.8676114422×10⁻⁵ Δf_H) meV ps Å⁻² per upper atom`,

with each `Δf` entered numerically in THz. Both coefficients are positive. The 14 and 18 Å archive cutoffs change the first coefficient by less than `5×10⁻¹⁰` and the second by less than `1×10⁻¹⁰` in these units; this is only a cutoff sensitivity check within the same material model. Under equal `d_j`, the low pair supplies 93.6696% of this conditional drag; the high pair supplies equal drag only if its linewidth is about 14.797 times the low-pair width. The low pair supplies 0.152474 of the total 0.229339 meV Å⁻² per-atom **static softening** at this model reference, so static and dissipative modal shares differ.

The [passive cross-mode loss audit](../graphite-cross-loss/README.md) quantifies the scope of the diagonal assumption: with equal symbolic widths, an unknown positive semidefinite off-diagonal loss block permits a pointwise interval ±48.70% around this diagonal estimate. The 93.6696% share is a diagonal-only decomposition; pair widths by themselves do not determine the cross contribution or its pressure derivative.

## Load derivative and measurement gate

The archived ±2.5 MPa stationary pressure sweep supplies `a_L(P),a_H(P)`, but assumed **constant, unmeasured** Rayleigh loss. Differentiating the calibrated mode law gives

`γ_scalar′(P)=2π m_eff [a_L′ Δf_L+a_H′ Δf_H+a_L Δf_L′+a_H Δf_H′]`,

provided the masses and pair identification are unchanged. At the 16 Å reference, the coefficients of the first two terms are `2.22384339×10⁻⁷ Δf_L + 1.54184042×10⁻⁸ Δf_H` in meV ps Å⁻² per atom per MPa, with widths in THz. **Linewidth derivatives are independently required.** If both widths are equal and constant, the conditional logarithmic drag slope is `+8.06052×10⁻⁴ MPa⁻¹`. A common linewidth fractional slope of approximately `−8.06052×10⁻⁴ MPa⁻¹` cancels that *drag* slope locally. This is a model cancellation condition, not a prediction that measured friction is load independent.

Measure or calculate complex mode response near both pairs at the reference and at pressure offsets, with the same contact and temperature preparation. Report fitted pole positions, dissipative widths, uncertainty and cross-mode self-energy. If `D` mixes the two E copies, four linewidths alone do **not** determine `C K⁻¹ D K⁻¹ Cᵀ`; measure the off-diagonal loss response. Independently register the four-site source map and subtract a frozen conventional coupling before assigning any added contribution to the UD candidate. A distinct UD damping prediction requires its own independently fixed `C_add`, material bath law, physical clock and sliding-force estimator. This conventional linewidth transfer is a calibrated null control, not a UD-specific residual.

`python3 experiments/graphite-linewidth-transfer/replay_linewidth_transfer.py` checks the modal-weight sums, `a_j=||Cv_j||²/(2κ_j²)`, mass/frequency conversion, pressure-sweep decomposition and 14/16/18 Å sensitivity. [Captured output](../../artifacts/graphline-20261023-80beee09/exact-001/files/linewidth-transfer.json) and [calculation receipt](../../candidates/graphite-linewidth-transfer/mathematical_receipt.json) retain its exact inputs and conventions. No new KC simulation, phonon measurement or force trace was produced; independent physics review and mainline physical promotion remain OPEN and zero, respectively.
