# Symmetric native packet and one-edge gate on graphite quotients

**EXACT finite-carrier dynamics / CONDITIONAL interface identification; graphite friction OPEN.** This extends the [native support-current identity](../graphite-native-support-current/README.md) from an arbitrary prepared edge amplitude to an explicit finite evolution. The reported 21.8°/38.2° friction peaks were known before the calculation; no friction or angle coefficient is fitted. The supplied *UD coefficient provenance ledger v0.39(2)* (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) Q166/Q167/Q170 supplies signed support continuity and a conditional masked contact lane. This calculation **declares** the packet seed, which contact closes, and that it stays closed during the Taylor window. It does not derive the gate trigger or a physical update time.

## Carrier, clock and readout

For each periodic honeycomb torus with `(m,n)=(2,1),(3,1),(3,2)` and `N=m²+mn+n²=7,13,19`, take `x∈C₀=R^(2N)`, `y∈C₁=R^(3N)`, `z∈C₂=R^N` in the unit simplex metric. `B₁` is the A-to-B edge boundary and `B₂` the oriented hexagonal face boundary of the earlier [quotient replay](../graphite-quotient-contrast/README.md). The **native model parameter** `s` is dimensionless. A diagonal contact mask `H=diag(h_e)` has `h_e=1` everywhere in the free model. In the gate model, only `h_{e(0,0)}=0`, closing **both endpoint contacts of that one edge register**. The face coupling stays unchanged:

`ẋ=−B₁ H y`, `ẏ=H B₁ᵀx−B₂z`, `ż=B₂ᵀy`.

This block generator is skew and conserves `||x||²+||y||²+||z||²`. The masked `B₁H` need not satisfy `(B₁H)B₂=0`; it is an interaction mask, **not** a replacement simplicial boundary. Start from the same labeled seed `x(0)=e_{A0}`, `y(0)=z(0)=0` in all three quotients. The 0↔1 lane's edge-register stock injection is `J_e(s)=2h_e y_e(s)(B₁ᵀx(s))_e`. Retain the original ungated harmonic columns `M`, each a constant bond-direction vector divided by `√N`. Report `P_N(s)=√N MᵀJ(s)` in the fixed integer basis `h₁=(1,−1,0)`, `h₂=(1,1,−2)`. This is a **native stock-flow projection**, not a physical force or a Q24 material coefficient.

## Exact free-flow symmetry

The torus presentations have a 120° automorphism about `A0`. With `s₁=m+n`, choose `q` satisfying `q s₁≡−m`, `q n≡−s₁`, `q³≡1 (mod N)`; the exact choices are `q=4,9,7` for N=7,13,19. It sends `A_r→A_{qr}`, `B_r→B_{qr−s₁}`, edge `(t,r)→(t+1 mod 3,qr)`, and face `r→qr−m`. The replay checks, on every chain basis vector, that this permutation commutes with the **unmasked** full 0/1/2 generator. The seed is invariant. The two-dimensional harmonic readout has no C3-fixed vector, so

`P_N^free(s)=(0,0)` **for every s**, not only to the finite Taylor order checked by the program.

The one-edge closure breaks this symmetry by a supplied choice. It cannot arise from the free linear evolution of this symmetric seed alone. Q167 specifies a lawful masked contact *once the mask is given*; it does not select this graphite edge or its duration.

## Exact gated Taylor response

The exact integer derivative recurrence for the full `C₀⊕C₁⊕C₂` system, followed by binomial product derivatives for `J`, gives the following coefficients. Both components of `P_N(s)` equal the displayed value. No floating-point reconstruction is used.

| Term | N=7 | N=13 | N=19 |
| --- | ---: | ---: | ---: |
| `s¹` | `−2` | `−2` | `−2` |
| `s³` | `13/3` | `13/3` | `13/3` |
| `s⁵` | `−187/60` | `−187/60` | `−187/60` |
| `s⁷` | `43/35` | `253/210` | `253/210` |
| `s⁹` | `−19751/60480` | `−18527/60480` | `−1591/5184` |

Thus the **first quotient-dependent Taylor term in this specified common gate experiment** is order `s⁷`, with `P₇−P₁₃=(1/42,1/42)s⁷+O(s⁹)`. N=13 and N=19 first separate at `s⁹`, with `P₁₃−P₁₉=(13/22680,13/22680)s⁹+O(s¹¹)`. The replay calculates through `s¹⁷`, checks skewness and the exact C3 action, and verifies the stated differences. The first three nonzero terms are identical across all three quotients; the gate immediately activates **all** of them. The seventh-order difference has no supplied physical clock, speed, force or detector normalization and does not establish a seven-cell friction preference. Its sign is a signed native projection, not a positive drag ranking.

## What this changes for the UD hypothesis

This is a target-blind, native **preparation-and-evolution candidate** with an explicit gate choice. It tightens the original question: symmetric free dynamics cannot generate the harmonic readout from this seed, while a single chosen contact breaks C3 and produces a response across multiple moiré quotients before topology differentiates them. The first quotient-specific coefficient is a possible *internal* discriminator only if a separate physical map identifies the prepared interface, the gate clock and the stock-flow projection with a material response. The gate trigger, source localization, persistence after gate restoration, physical edge stiffness, complex bath damping, pressure response and signed kinetic force remain OPEN. A finite closed skew system alone supplies no irreversible Ohmic friction. Independent physics review NOT_RUN; physical promotion 0.

Run `python3 experiments/graphite-native-gate-dynamics/replay_gate.py`; see the [mathematical receipt](../../candidates/graphite-native-gate-dynamics/mathematical_receipt.json) and [immutable capture](../../artifacts/graphgate-20261024-01/exact-001/manifest.json).
