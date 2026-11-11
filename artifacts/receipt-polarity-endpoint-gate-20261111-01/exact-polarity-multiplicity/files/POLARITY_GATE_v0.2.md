# Receipt-index polarity and endpoint selector gate v0.2

2026-11-11; `receipt-polarity-endpoint-gate-20261111-01`; base `ud-tetra/UD-Physics@022b1bac56a76b2c2862e81fba5d003fa37596e8`; [issue #357](https://github.com/ud-tetra/UD-Physics/issues/357). **EXACT / CONDITIONAL combinatorics; NO-GO scoped; physical promotion 0.** No Gibson or empirical target enters the calculation.

## Typed source and assumptions

The recovered UD provenance ledger **v0.85** (`experiments/action-normalization-audit/sources/ledger_v0.85.json`, SHA-256 `8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec`), Q194–Q195 defines `μ_Θ=dim L^-−dim L^+` as a *conditional* net Hamming budget. Q198 declares the receipt-index operator `(θ̄^-,L^-,L^+,T,W^B2)→θ^+ or HOLD/INFEASIBLE`; Q205/Q208 quarantine the obligation saturation and endpoint predictor; Q210 blocks constructing their semantics from closed-carrier variables alone. [Temporal receipt audit](../history-source-update/README.md) v0.1 explains those input and lineage limits. The [v0.1 orbit result](README.md) proves the pure-relabeling relation without asserting physical transitions.

Set `Θ={0,1}³`, and assume only that the net budget `μ=|θ^+|−|θ^-|` is supplied and the endpoint lies in `Θ`. This is a **necessary budget filter**, not the full Q198 operator and not a sourced admissibility predicate. Domain is `(θ^-,μ)∈Θ×{-3,…,3}`; codomain is a *set* of candidate `θ^+∈Θ`, possibly empty. No physical tick, energy unit, stochastic choice, environment coupling or change-of-carrier metric is assumed. A separate HOLD state is an operator outcome, not another endpoint in `Θ`.

## Exact count and obstruction

For initial weight `k`, the endpoint multiplicity is `C(3,k+μ)` if `0≤k+μ≤3`, and zero otherwise. Summing over `C(3,k)` initial states and applying Vandermonde gives `N_μ=Σ_k C(3,k)C(3,k+μ)=C(6,3+μ)`. Hence the ordered-pair counts for `μ=-3,-2,-1,0,1,2,3` are respectively `1,6,15,20,15,6,1`, summing to 64. The `μ=0` relation is exactly the 20 equal-weight pairs of the v0.1 relabeling calculation; this equality of endpoint sets does not equate a receipt with a relabeling event.

**NO-GO / exact hypotheses:** net polarity and initial parity alone do not define a single-valued autonomous endpoint map on all feasible inputs. Witness `θ^-=100, μ=0` admits `100,010,001`; `θ^-=000, μ=1` admits `100,010,001`. Any deterministic choice or HOLD/rejection among these requires additional specified input or constitutive rule. Q198 may select once its full `L^±,T,W` inputs and source semantics are supplied; this result does not disprove its conditional operator, nor assert all counted pairs are physically admissible. Adding a one-bit-flip restriction or tie breaker changes the branch and needs its own source.

[Exact replay](polarity_gate.py) enumerates all 64 ordered pairs, checks the binomial identity and both three-way witnesses. **AUTO_LOCK** only the scoped count and non-uniqueness. **OPEN_GATED:** construction of the obligation spaces and continuation from pre-event local state, conflict resolution, conservation including environment, clock, and independent held-out event test. **AUTO_FREEZE** a claim that the net index by itself supplies a complete physical event selector. Physical promotion remains 0.
