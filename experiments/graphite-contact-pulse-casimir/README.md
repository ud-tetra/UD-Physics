# Contact-pulse preparation and harmonic-charge material port v0.1

**Date:** 2026-11-02. **EXACT/CONDITIONAL** native pulse and reciprocal energy algebra; contact selection, physical clock, material coefficients and graphite force **OPEN**. The observed 21.8°/38.2° pair was exposed before this calculation. No angle, force or load value was fitted. Physical promotion 0; independent physics review NOT_RUN.

## Carrier, state and pulse

Import the periodic honeycomb chain quotient and its `HARMONIC` rows from [graphite packet reciprocity](https://github.com/ud-tetra/UD-Physics/blob/1993cadecaae3a5fe98773abca5cc399d2e22df4/experiments/graphite-packet-reciprocity/README.md) and [prepared harmonic source](https://github.com/ud-tetra/UD-Physics/blob/1993cadecaae3a5fe98773abca5cc399d2e22df4/experiments/graphite-harmonic-preparation/README.md). For `(m,n)=(2,1),(3,1),(3,2)`, set `N=m²+mn+n²=7,13,19`. Orient edge class `t` as `A_r→B_(r-s_t)`, `s=(0,m+n,n)`. Write `U:R²→R^(3N)` for the *unnormalized* harmonic embedding with class rows `u₀=(1,1),u₁=(-1,1),u₂=(0,-2)`. In the unit chain metric, `B₁U=0`, `B₂ᵀU=0`, and `G=UᵀU=N diag(2,6)`. The harmonic coordinate is `a(q)=G⁻¹Uᵀy∈R²`, for `q=(x,y,z)∈R^(2N)⊕R^(3N)⊕R^N`. All are native dimensionless spaces and the parameter `s` below is not physical time.

The supplied *UD coefficient provenance ledger v0.39(2)* (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`), Q22–Q26, keeps the current seam-pairing source zero and the Q24 edge/route source conditional. The pulse model below does not amend or identify those objects with graphite material stiffness.

For a fixed binary contact mask `P` on edge registers, use the already declared Q167-style **interaction** generator

`x'=-B₁Py,  y'=P B₁ᵀx-B₂z,  z'=B₂ᵀy`.

It is skew in the unit chain metric and preserves `||q||²`; `B₁P` is *not* a replacement simplicial boundary. Start at the labeled local seed `q(0)=(e_A0,0,0)`. For one **externally chosen** incident edge `e*=(t,0)`, close that edge only: `P=I-E_(e*)` for `0≤s≤ε`, then reopen with `P=I`. The pulse duration `ε>0`, distinguished vertex, and orientation choice are inputs; no native readiness law selects them.

## Exact transfer and a finite nonzero interval

During the pulse, `a'=G⁻¹UᵀP B₁ᵀx`. At the initial state `UᵀB₁ᵀe_A0=0`, while `(B₁ᵀe_A0)_(e*)=-1`. Consequently

`a'(0)=G⁻¹u_t=(u_(t,1)/(2N),u_(t,2)/(6N))`.

For `t=0,1,2` these are respectively `(1/(2N),1/(6N))`, `(-1/(2N),1/(6N))`, and `(0,-1/(3N))`. The pulse generator anticommutes with the 0/1/2 grading, so `a(s)` is odd for the stated zero-edge/face seed. Hence

`a(ε)=ε G⁻¹u_t+O(ε³)`, and `||U a(ε)||²=(2/(3N)) ε²+O(ε⁴)`.

The leading harmonic stock coefficient is the same for the three edge classes, and nonzero at all three indices. The exact integer/Fraction replay gives the cubic coefficient `-(1/3)G⁻¹u_t` on each of the nine `(N,t)` cases; later quotient-dependent coefficients do not supply a seven-cell selector.

This is more than a formal infinitesimal claim. Each `B₁` row has three edges and column two vertices, so `||B₁||₂≤√6`; each `B₂` row has two incident faces and column six edges, so `||B₂||₂≤√12`. Thus `||A_P||₂≤√6+√12<6`. Also `||G⁻¹Uᵀ||₂=1/√(2N)` and `||G⁻¹u_t||₂≥1/(3N)`. The odd Taylor tail after the linear term satisfies

`||a(ε)-εG⁻¹u_t||₂ ≤ 36 e^(6ε) ε³/√(2N) < 72 ε³/√(2N)` for `0<ε≤1/100`, since `e^(3/50)≤50/47<2`. Its ratio to the leading lower bound is below `216√(19/2)/10000<1/2` for the listed `N`. Therefore **`||a(ε)||₂≥ε/(6N)>0` for every listed quotient and all `0<ε≤1/100`**. The interval is in native parameter units; it does not set a physical preparation time.

The state is continuous when `P` reopens. Both fixed generators are skew, so total native norm is conserved on each side and has no jump. A masked *classification* stock may jump because the mask changed; this is not heat or actuator work. The contact pulse creates a harmonic component together with other, generally oscillatory edge components. It does not produce the pure state `y=Ua` by itself.

## Persistence and reciprocal conditional material completion

After reopening, the free native generator has the exact invariant `Uᵀy`: `Uᵀ(B₁ᵀx-B₂z)=0`. Stronger: in a reciprocal Hamiltonian completion `qdot=(E₀τ)⁻¹ A∇_q E` with the **same unmasked skew** `A`, `a(q)` is a Casimir for *any differentiable energy* `E`, because `Uᵀ` annihilates the edge row of `A`. A material interaction may change the nonharmonic motion while the pulse-created harmonic charge persists. An open-system source acting directly on that charge, a changed Poisson operator, or another contact mask falls outside this theorem.

For a stable local material reference, take lateral displacement `u∈R²` and height/mode displacement `h∈R^r` in Å; energy is per upper atom in meV. Let `P_h=UG⁻¹Uᵀ` be the unit-metric projector onto the native harmonic edge space, `w_h=(P_h y)^{◦2}=(Ua)^{◦2}`, and `S_h=Uᵀ diag(w_h)B₁ᵀ`. The [previous exact port calculation](https://github.com/ud-tetra/UD-Physics/blob/1993cadecaae3a5fe98773abca5cc399d2e22df4/experiments/graphite-harmonic-preparation/README.md) gives `S_h=v(a)l_siteᵀ`, `v=(4a₁a₂,2(a₁²-3a₂²))`, `l_siteᵀ=[-1_Nᵀ,1_Nᵀ]`. The projected weight is an **assumed nonlocal coarse readout**, not Q25's current canonical local edge law. It is stationary after reopening because `a` is conserved; the full `y_e²` generally is not.

Assume independent dimensionless registrations `T:R²_cart→R²_native`, `R_h:R^r→R^(2N)_site` and a dimensional `λ` in meV Å⁻² per upper atom. Define `C_a=λ TᵀS_hR_h=λ (Tᵀv) lᵀ`, `lᵀ=l_siteᵀR_h`. This is a **candidate** reciprocal cross-Hessian. With `K=Kᵀ≻0` (meV Å⁻²), physical mode mass `M_h≻0`, and separately measured or sourced Rayleigh loss `D_h=D_hᵀ⪰0` (meV ps Å⁻²), one local energy and material equation are

`E=E₀||q||²/2 +uᵀK₀u/2 +uᵀ(C₀+C_a(a))h+hᵀKh/2 +hdotᵀM_h hdot/2`,

`M_h hddot+D_h hdot+K h=-(C₀+C_a)ᵀu`, `F_reaction=-∂_u E`.

With the stated skew packet evolution, controlled `u(t)`, and fixed matrices, `dE/dt=-F_reaction·udot-hdotᵀD_h hdot`. Because `a` is a Casimir, the `a`-dependent energy gradient lies in the kernel of `A`; the material term need not alter the packet equation to satisfy this exact power identity. Here physical time `t=τs` is an assumed clock, not supplied by UD. The polynomial energy is local about a stable reference only; `K₀−(C₀+C_a)K⁻¹(C₀+C_a)ᵀ` must also satisfy the chosen stability criterion. `E₀,τ,T,R_h,λ,K,D_h,M_h,C₀`, pressure dependence and contact participation are **not** fixed by this calculation.

For a specified stationary, low-frequency material bath let `L=K⁻¹D_hK⁻¹`. The conditional added *self-loss* is exactly

`Γ_self=C_aLC_aᵀ = λ²(lᵀL l)(Tᵀv)(Tᵀv)ᵀ ⪰0`, `rank Γ_self≤1`.

The total conventional-subtracted drag includes cross terms `C₀LC_aᵀ+C_aLC₀ᵀ` and may have either signed component. The self-loss is not the measured friction force; no signed force vector or load slope follows without a calibrated sliding estimator and `C,K,D` at load offsets. Nothing in this source derives the external pulse, physical loss, or the observed angle pair. The invariant harmonic charge persists, but a friction signal requires a dissipative material channel.

## Verification and disposition

Run `python3 experiments/graphite-contact-pulse-casimir/replay_contact_pulse.py` (SHA-256 `6d4f98a4506d468dc5e830e4ab543f7be7f7546ed503fd04efa16105752316c1`). It checks exact coefficients, equal leading stock, the combinatorial degree bounds, the squared Taylor-ratio inequality, and post-reopening harmonic conservation on `N=7,13,19` for every incident edge class. The analytic norm/tail argument independently verifies nonzero preparation throughout the declared interval. The source paper's [publisher abstract](https://journals.aps.org/prl/abstract/10.1103/ly48-b4l2) is only a target-exposure record, not input data to this construction.

**Decision:** AUTO_LOCK the scoped transfer, nonzero interval, Casimir persistence and conditional power/rank identities. The contact-selection rule, pulse duration, nonlocal projected weight, material map and bath remain CANDIDATE/OPEN. There is no seven-cell selection or physical promotion. Reopen only with a sourced contact selector and physical material measurements or independently derived parameters, followed by a genuinely held-out signed force comparison.
