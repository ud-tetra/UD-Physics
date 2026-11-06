# Q169 filtration stability bound v0.3

2026-11-06; session `filtration-stability-bound-20261106-01`; base `ud-tetra/UD-Physics@bdaf1e051a94910f98e445d5ead51ba0591afcb5`. **EXACT / CONDITIONAL**, physical promotion 0. Source: supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165, Q169, Q177–Q179; [native filtration v0.1](README.md) and [dynamics v0.2](REFINEMENT_DYNAMICS_v0.2.md). This quantifies the qualitative continuity statement in v0.2, without altering its exact crossing counterexample.

## Typed statement

On a finite pure fixed tetrahedral complex `K`, let `c(t)∈R^Σ` solve `c'=Ac`, `A=D−Dᵀ` with the unchanged unit coefficient metric and arbitrary initial `c(0)`. Let `S=Σ_σ c_σ(0)²`, a conserved native squared-amplitude stock. Let `d=max_σ #{η:A_ση≠0}` be the maximum incidence-graph degree, a dimensionless integer. Let `s_τ(t)=Σ_{σ⊆τ}c_σ(t)²/n₃(σ)` and `G_t[u]` be the face-dual graph induced by cells with `s_τ(t)≤u`. Its component count is `β₀(t,u)`. The generator parameter `t` is not calibrated physical time; `u` and `S` have squared-amplitude units.

**THEOREM — EXACT / CONDITIONAL.** For every cell and all native times `t,t₀`, `|s_τ(t)−s_τ(t₀)|≤ε`, where `ε=2dS|t−t₀|`. Thus the sublevel graphs obey nested induced inclusions `G_t[u−ε]⊆G_t₀[u]⊆G_t[u+ε]` on the same fixed dual graph, and symmetrically with `t,t₀` swapped. These inclusions give a uniform `ε` interleaving of the component filtrations. They do **not** assert pointwise equality of `β₀(t,u)` near a crossing. If `δ=min_τ|s_τ(t₀)−u|>0`, then for `2dS|t−t₀|<δ`, the active cells and `β₀(t,u)` are exactly unchanged. If `dS=0`, all supports are constant and the conclusion holds for every time.

## Proof, control and decision

The ownership matrix `W_τ=diag(1_{σ⊆τ}/n₃(σ))` has operator norm at most one. Skewness conserves `||c||²=S`. The absolute derivative `|s_τ'|=|2cᵀW_τAc|≤2||c||||Ac||≤2||A||₂ S≤2dS`: the last inequality follows from row and column absolute sums at most `d` for the symmetric incidence support of `A`. Integrate over the interval; each vertex weight of the fixed dual graph moves by at most `ε`, yielding the two graph inclusions and the threshold-margin statement. No graph topology changes under fixed `K`.

For the v0.2 three-cell face chain and top amplitudes `(1,3,2)`, `S=14`, `d=6` in the [exact check](filtration_stability.py). At `u=5`, initial supports `(1,9,4)` give `δ=1`, hence `β₀(t,5)=2` whenever `|t|<1/168`. This is a conservative sufficient interval, not a measured persistence time. At `u=4`, `δ=0`; v0.2 derives third-cell quadratic coefficient `5/2>0` and immediate loss of one active cell for sufficiently small nonzero `t`, so an unconditional pointwise-persistence claim is **NO-GO** for this readout and preparation. The bound concerns stability of a candidate mathematical observable, not growth preference, cluster formation, physical length, nebular intensity or astronomical dynamics.

**AUTO_LOCK** the uniform bound and graph-filtration interleaving under the stated fixed-carrier assumptions. **OPEN_GATED:** any physical clock, calibrated readout, carrier-change rule and test against independent sky data. Since the exact bound follows from general finite-dimensional skew flow and maximum degree, it does not by itself favor UD over another incidence dynamics.
