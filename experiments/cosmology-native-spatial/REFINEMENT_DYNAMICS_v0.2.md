# Intrinsic filtration refinement and Q169 dynamics v0.2

Session `cosmology-native-filtration-dynamics-20261106-01`, base `ud-tetra/UD-Physics@5c5c85245fb0306574513c471b2e8e75f597a0b5`. **EXACT conditional / NO-GO scoped** for unqualified refinement invariance; physical promotion 0. Extends [v0.1](README.md) without changing its relabeling theorem.

## Source and typed setup

Use the fixed-complex Q165/Q169/Q177–Q179 definitions in `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, and `experiments/pachner-state-transport/README.md` v0.1 §1→4, which fixes old lower-grade simplices and sends one old top cell to the signed sum of four children. The candidate observable is v0.1 cell support `s_τ=Σ_(σ⊆τ)c_σ²/n₃(σ)` and its face-dual-graph sublevel component count `β₀(u)`. Parameter `t` below is formal native flow; `u` has squared-amplitude stock units, not a physical intensity.

## Exact refinement counterexample with conserved total stock

Let old `K=0123`, new `K'` be its centroid 1→4 subdivision with new vertex 4, children `0124,0134,0234,1234` (up to orientation). Set only old vertex `0` amplitude to 1. The source chain map fixes that vertex. In old `K`, its ownership count `n₃(0)=1`, hence `s=(1)`. In `K'`, vertex 0 belongs to exactly three children, so their supports are `1/3` each and the fourth child's support is 0. The total remains exactly 1 on both carriers. Yet `β₀^old(0)=0` and `β₀^new(0)=1`, since the zero-support child activates at threshold 0. At `u=1/3`, all four children activate as a face-adjacent clique, giving one component.

**NO-GO under this readout and transport:** conservation of Q165/Q178 total stock and boundary-compatible 1→4 vertex transport do not imply filtration invariance. This is a counterexample for the chosen sublevel dual-graph observable, not a theorem against all possible refinement-invariant observables. The old top-unit transport provides a separate contrast: signed four-child top amplitudes have squared stock total `1→4` under the unchanged unit metric, as already recorded in the source Pachner audit. A changed intercomplex metric/contact is a distinct unselected branch; the v2.1 `H_t` family does not automatically provide Q177 cellwise ownership in that metric.

## Exact small-time native dynamics

On any fixed pure tetrahedral complex `K`, put amplitudes only on top cells at `t=0`: `a_τ=c_τ(0)`, all lower grades zero. With ascending oriented boundary matrix `D₃`, Q169 `A=D−Dᵀ` implies `c₂'(0)=D₃a`, `c₃'(0)=0`, `c₃''(0)=−D₃ᵀD₃a`. Therefore

`s_τ(t)=a_τ²+t²[−a_τ(D₃ᵀD₃a)_τ+Σ_(f⊂τ)(D₃a)_f²/n₃(f)]+O(t⁴)`.

The squared face amplitude is owned equally by all incident top cells. Summing the bracket over `τ` gives `−||D₃a||²+||D₃a||²=0`, consistent with Q165 global conservation. Parity of the graded source flow makes the cell-support expansion even in `t` for this preparation.

For the v0.1 face-chain `0123,0124,0145` with top amplitudes `(1,3,2)`, native initial supports are `(1,9,4)` and the exact `t²` coefficients are `(4,−13/2,5/2)`. At threshold `u=4`, the two separated low-stock cells are active at `t=0` (`β₀=2`), but the third-cell support rises above 4 for all sufficiently small nonzero `t`, leaving `β₀=1`. At `u=5` the initial positive stock gaps ensure the same two components persist for a sufficiently small interval by continuity. Thus the filtration is locally stable away from crossing values but not dynamically constant at a threshold crossing. Neither conclusion selects a preferred cluster, a growth law or a physical clock.

**Disposition:** the v0.1 relabeling-invariant native observable remains a **CANDIDATE**. **AUTO_FREEZE** any unqualified claim of 1→4 refinement invariance or dynamical persistence from Q165 conservation alone, while retaining the narrower exact fixed-carrier expansion and counterexample. No physical nebular readout or astronomical scoring is authorized by this result; promotion 0.

Replay `python3 experiments/cosmology-native-spatial/filtration_dynamics.py`; exact `Fraction` checks cover source vertex ownership, both total-stock controls, face-adjacency `β₀`, and Q169 second-order coefficients. A source-selected cross-refinement stock/contact transport and physical projection are reopening dependencies.
