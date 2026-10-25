# Stationary packet variance source on graphite quotients

**EXACT equilibrium and finite-carrier algebra / CONDITIONAL constitutive defect; physical graphite source OPEN.** The [reciprocity note](../graphite-packet-reciprocity/README.md) showed that a time-reversal-even edge weight such as `w_e=⟨y_e²⟩` could enter a reciprocal cross-Hessian, but isotropic quadratic equilibrium cancels its mean harmonic port. This calculation asks what a minimal stationary, symmetry-compatible anisotropy would require. The paired friction angles and load trend were already known; no material or angle parameter is fitted.

## A fixed contact gate does not change the canonical covariance

For any fixed diagonal contact mask `H`, the full 0/1/2 native generator `A_H` is real skew in the unit chain metric and conserves `||q||²`, `q=(x,y,z)`. Under the **declared** native energy `E_n=E0 ||q||²/2` at inverse temperature `β`, the isotropic Gaussian density `ρ(q)∝exp(-β E_n)` is stationary under the closed flow: energy and phase-space volume are preserved. Its edge covariance is `⟨y_e y_f⟩=θ δ_ef`, `θ=(β E0)^-1`. Therefore

`⟨S(y²)⟩=θ M^T B1^T=0`, because `B1 M=0`.

This remains true for a fixed one-edge Q167-style contact mask **in this specified canonical ensemble**. The mask changes the trajectories and can change a particular prepared orbit's time averages; it does not, by itself, prescribe a new equilibrium distribution or a material stiffness. The current [UD local-source selection v0.1](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/docs/UD_Local_Source_Selection_v0.1.md) declares a localized gate on a 600-cell and does not specify graphite edge covariance, thermal energy, atom registration or loss. The supplied ledger v0.39(2) Q166/Q167/Q170 likewise gives support-current and masked-contact identities without a graphite equilibrium variance law.

## One local C3-symmetric constitutive defect

As a separate **hypothesis**, replace the native energy by

`E_Q=E0 (||x||²+ y^T Q y+||z||²)/2`, `Q=I+α P_O`, `α>-1`,

where `P_O` projects onto the three bond registers incident to the labeled A0 vertex. The equal three-edge choice preserves the local C3 rotation; selecting A0 and a physical registry is externally supplied. At zero interface displacement, the canonical covariance is `⟨yy^T⟩=θ Q^-1`, so the three selected edges have `w_O=θ/(1+α)` and every other edge has `w_0=θ`. Let

`δ=w_O-w_0=-θ α/(1+α)`.

Uniform `w_0` cancels. The previously proposed material port becomes

`⟨C_a⟩=λ δ T^T S(χ_O) R_h`, `S(χ_O)=M^T P_O B1^T`,

where `T` registers physical lateral axes, `R_h` registers material height/site coordinates, and `λ` has units meV Å^-2 per upper atom. Those maps and `E0` remain independent assumptions. In the earlier direct harmonic output basis, `sqrt(N) S(χ_O)` has a zero A0 column, the three B-neighbor columns `[(1,1),(-1,1),(0,-2)]`, and all other columns zero. It has rank two and squared Frobenius norm `8` in that **declared direct coordinate metric**, for each `N=7,13,19`. Thus `||S(χ_O)||_F²=8/N`. The `1/N` here is a report normalization, not a predicted friction ratio or contact-area law. In a common `sqrt(N)` report the local source is identical across the three quotients and does not select the paired angles.

The changed energy requires changed reciprocal dynamics. With the same constant skew Poisson structure, `dq/dt=(E0 τ)^-1 A_H ∇_q E_Q=(1/τ) A_H diag(I,Q,I)q`; it conserves `E_Q` because `A_H` is skew. Keeping the former `qdot=A_H q/τ` while assigning `E_Q` as its conserved energy would generally fail. The candidate remains time-reversal even under `diag(I,-I,I)`. The [exact replay](verify_variance.py) checks the incidence, rank, norm, canonical covariance, fixed-mask stationarity and energy balance on all three quotients.

## Load and bath implications

For pressure `p`, at fixed model structure `δ(p)=-θ(p) α(p)/(1+α(p))`, hence

`δ′=-θ′ α/(1+α)-θ α′/(1+α)²`.

Pressure can also change `λ,T,R_h,K,D`, contact and temperature. Neither weak load response nor a friction coefficient follows from the three-edge geometry. If the bath is locally passive, the earlier `Γ=C K^-1 D K^-1 C^T` applies only after its stationary, low-frequency conditions and material registration are independently established; conventional and added sources have signed interference terms. Equilibrium `⟨C_a⟩=0` in the isotropic case does not prove `⟨C_a L C_a^T⟩=0` for fluctuating coupling.

This exercise identifies the *minimum extra input* for this family: a source law or independent measurement for `α(p)` and the selected registry, physical `T,R_h,λ,E0,τ`, and complex material loss. Inferring `α` from the same friction angles would be a fit. An independently sourced `α` must forecast a signed force/load residual after a separately fixed full conventional 2D PES/contact/loss baseline, with N13/N19 and nearby-angle controls. Until then this is a local counterexample and no seven-cell preference, not a UD friction prediction. Independent physics review NOT_RUN; physical promotion 0. See the [receipt](../../candidates/graphite-equilibrium-variance/mathematical_receipt.json) and [capture](../../artifacts/graphvar-20261024-01/exact-001/manifest.json).
