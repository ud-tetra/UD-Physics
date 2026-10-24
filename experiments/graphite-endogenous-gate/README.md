# Equivariant contact triggers and gate-transition stock

**EXACT finite-carrier obstruction / CONDITIONAL trigger / graphite friction OPEN.** This follows the [one-edge gate replay](../graphite-native-gate-dynamics/README.md), which imposed a selected closure. The supplied *UD coefficient provenance ledger v0.39(2)* Q166/Q167/Q170 (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) supplies local signed support continuity and a binary masked contact identity, but leaves the gate-transition rule open. The known 21.8°/38.2° angles and weak load trend are exposed targets; neither sets the trigger below.

## Symmetry obstruction

Use the prior N=7,13,19 periodic honeycomb 0/1/2 chain carrier, unit metric and dimensionless model parameter `s`:

`ẋ=−B₁H(c)y`, `ẏ=H(c)B₁ᵀx−B₂z`, `ż=B₂ᵀy`, with `c=(x,y,z)` and binary diagonal `H`.

Let `R` be the exact 120° chain permutation of the previous replay, and suppose a deterministic contact law obeys `H(Rc)=R₁H(c)R₁⁻¹`. Its vector field is equivariant: `F(Rc)=R F(c)`. If the update has a unique state trajectory, or a hybrid switching rule resolves simultaneous events equivariantly, the `R`-fixed initial state stays `R`-fixed. The edge stock injection `J_e=2h_e y_e(B₁ᵀx)_e` rotates with the state. The two constant-direction harmonic coordinates have no `R`-fixed vector; therefore **`P_N(s)=√N MᵀJ(s)=0` at all times for each N**. This statement applies to *any* such deterministic equivariant local rule, including memory or hysteresis whose complete initial state and update are themselves equivariant. It is a conditional no-go for this seed and readout, not an all-UD or all-friction no-go.

An asymmetric packet, registry, sliding direction, boundary/contact field, or stochastic realization can break the premise. A stochastic law may produce a nonzero individual realization while its symmetric ensemble mean remains zero. Such input must be specified and independently constrained; it cannot be hidden in a tie-break that singles out edge `(0,0)`.

## Explicit threshold witness and its failure

As a proposed, **not ledger-derived**, local readiness define `u_e(c)=((B₁ᵀx)_e)²+y_e²` and `h_e(c)=1` if `u_e<τ`, `0` otherwise. It is invariant to reversing the oriented edge basis (`y_e` and `B₁ᵀx` both change sign), and is `C₃` equivariant. At `x(0)=e_A0`, `y(0)=z(0)=0`, precisely three incident edges, `(t,0)` for `t=0,1,2`, have `u=1`; all others have `u=0`. For `τ=1/2`, the complete three-edge orbit closes and the packet is stationary because `H B₁ᵀx=0`. For `τ=3/2`, every contact stays open initially and the free flow is symmetric. Subsequent equivariant switches preserve symmetry. Both have `P_N=0` for N=7,13,19. Thus this simple endogenous readiness rule cannot reproduce the previously imposed one-edge response or select seven cells. The threshold values are illustrative counterexamples, not fits or physical material parameters.

## Transition receipt and full-chain scope

For a fixed binary mask, the full generator remains skew and preserves `S=||x||²+||y||²+||z||²`. Q167's masked `||x||²+||Hy||²` belongs to its 0↔1 lane. If we extend its *classification stock* to the full replay as `S̃_H=||x||²+||Hy||²+||z||²`, the unchanged face coupling gives the exact identity

`dS̃_H/ds=2 yᵀ(I−H)B₂z` **between switches**, while `dS/ds=0`.

At an instantaneous mask update `H⁻→H⁺` with continuous `c`, the exact reclassification is `ΔS̃=Σ_e(h_e⁺−h_e⁻)y_e²`, whereas `ΔS=0`. For example, at `x=e_A0`, `y_(t,0)=1` for all three directions and all other amplitudes zero, lowering the declared threshold from `5/2` to `3/2` closes that orbit and changes `S̃` by `−3`, without changing `S`. This **does not** measure gate work or physical dissipation. It prevents treating masked-stock disappearance as lost energy. If the mask jumps at a nonzero edge amplitude, `J` also changes instantaneously; no intrinsic switching time or energetic actuator is supplied. With `B₂=0` in the restricted 0/1 lane, the between-switch masked-stock derivative vanishes as in Q167's scope.

The [exact integer/Fraction replay](replay_trigger.py) checks the three-edge threshold orbit, the frozen seed, full-generator commutation on every chain basis vector for both fixed masks, equivariance at a non-invariant test state, full norm continuity, the masked-stock derivative, and the `−3` transition on N=7,13,19. See the [mathematical receipt](../../candidates/graphite-endogenous-gate/mathematical_receipt.json) and [immutable capture](../../artifacts/graphendog-20261024-01/exact-001/manifest.json).

## Next discriminant

Specify a *physical* symmetry-breaking preparation or boundary input before choosing the gate and an independently constrained material energy/time/force and complex-loss map. A registered sliding direction is a candidate input, but it would normally activate counterparts at all three quotients; seven-cell selection would still require a measured or independently derived quotient-dependent material response. No friction residual or load slope has been predicted. Independent physics review NOT_RUN; physical promotion 0.
