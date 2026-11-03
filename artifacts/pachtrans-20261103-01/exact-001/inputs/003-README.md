# Boundary-fixed Pachner state transport and weight obstruction v0.1

**2026-11-03 — development, no registry entry.** This extends [fixed-shell observability v0.1](../pachner-boundary-observability/README.md) at integrated base `2207611450df9106adccaf8189a50734fef5a46b`. The supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165/Q166/Q169 and Q174–Q179, is read-only source. Q165 is fixed-complex quadratic support; Q169 is the unit-metric global chain generator; Q174/Q175 already distinguish the full 2↔3 spectra. Q177's `1/n₃(σ)` apportions a simplex stock among cells, **not** an edge conductance or a move probability. No source item selects a Pachner event, its physical rate, or a cross-move energy reservoir. Physical promotion 0.

## Objects and exact questions

Use the two snapped 3-balls and ascending oriented simplices of the prior [exact-coordinate replay](../pachner-boundary-observability/audit.py): `K₁→K₄` for a 1→4 center split of a tetrahedron, and `K₂→K₃` for a 2→3 flip of a triangular bipyramid. The source and target complexes have identical oriented outer shell and coordinates. Coefficients are `Z` unless an explicit rational extension is declared. Let `B_k^old/new:C_k→C_(k−1)` be the signed simplicial boundaries, and `F_old`, `F_new` the geometric oriented sums of all top tetrahedra, representing the positive relative fundamental class in `H₃(K,∂K;Z)≅Z`.

Ask for a boundary-fixed graded transport `M_k:C_k(K_old;R)→C_k(K_new;R)` with

`B_k^new M_k=M_(k−1) B_k^old`, `M_k|_(boundary)=I`, and `M₃ F_old=F_new`.

Test equivariance for every exact-coordinate simplicial automorphism: `S₄` (24 elements) on 1→4 and `S₃×C₂` (12 elements) on 2→3. These are chain and topological requirements, **not** an energy or physical-charge law. The declared unit metric `||c||²=Σ_k||c_k||²` and skew generator `A=B−Bᵀ` are checked separately. No target number is fitted.

## 1→4: integral chain transport, metric mismatch

The old boundary vertices, edges and faces remain target simplices, so set `M₀=M₁=M₂=I` on them. Send the single old oriented tetrahedron to the signed sum of its four new tetrahedra. This **integral** map commutes with every boundary and all 24 `S₄` automorphisms. It sends the relative fundamental class with degree `+1`.

For a unit top-cell amplitude, however, `||F_old||²=1` while `||F_new||²=4`. The chain map therefore cannot also be an isometry in the declared unit cell metric. The full block transport does not intertwine the unit-metric skew generator (`A_new M≠M A_old`; exact replay finds 22 nonzero mismatch entries in the fixed ascending bases). A state update that conserves Q165 stock across this move needs a specified rescaling, source/sink, reservoir, or a changed metric. Rescaling the top map by `1/2` would preserve this top norm but violate degree-one boundary transport.

## 2→3: equivariant rational map and integral obstruction

Let `U,D` be the positively oriented old upper and lower tetrahedra, and `F_new` the positive sum of the three new tetrahedra. Keep old vertices, edges and six boundary faces fixed. The full `S₃` equator rotations force the image of each top cell in the orientation-covariant subspace of the three new top cells to be a multiple of `F_new`. Exchanging the apices forces the two multiples to agree. Degree `+1` on `F_old=U+D` then fixes both at **`1/2`**:

`M₃(U)=F_new/2`, `M₃(D)=F_new/2`.

The old internal equatorial face maps to the unique half-weighted boundary cap difference required by `B₃^new M₃=M₂ B₃^old` and `B₂^new M₂=M₁ B₂^old`. The [exact matrices](results.json) verify these equations and all 12 automorphisms. **NO-GO:** no `Z`-linear, full-`S₃×C₂`-equivariant degree-one map with these fixed-boundary and local top-cell conditions exists: the forced half coefficients are not integers. Choosing an upper apex gives an integral chain map with `U→F_new,D→0`; it commutes with only the six apex-preserving symmetries. This is a distinct symmetry-broken branch, not a counterexample to the scoped no-go.

The rational equivariant map sends the **integral total fundamental chain** to another integral chain: `M₃(U+D)=F_new`. Because the map on individual cells uses halves, this is not an induced `Z`-chain map or a claimed integral homology isomorphism; it is degree `+1` over `Q` with an integral value on this generator. It does not preserve the unit top-cell stock: `||F_old||²=2`, `||F_new||²=3`. Its full generator intertwining fails (44 nonzero mismatch entries in the fixed bases). Q177/Q178 do not cure this: every top tetrahedron has cell-incidence count `n₃(τ)=1`, so the top-stock totals are still 2 and 3 for these fundamental chains. Homology preservation, simplex stock conservation, and physical charge are different typed claims.

## Positive new-edge weight and gauge test

Keep all old graph edges at unit weight and add equal radial weight `g>0` on the four center edges in 1→4, or weight `g>0` on the new apex edge in 2→3. These are **assumed constitutive weights**, not Q177 ownership factors. For the same boundary displacement port as the prior audit, exact Schur reduction gives

`Λ_(1→4)(g)−Λ_old=(g/4)(4I−J)`,

`Λ_(2→3)(g)−Λ_old=g(e₃−e₄)(e₃−e₄)ᵀ`.

Thus no **strictly positive** added-edge weight preserves the full static boundary response when old weights, shell and port are held fixed. At `g=0` the operator difference vanishes, but the new center in 1→4 is disconnected and its internal Dirichlet matrix is singular; the formula is the `g↓0` limit, not a positive connected carrier. The exact replay checks `g=1,2,3` for 1→4 and `g=0,1,2` for 2→3; the formulas hold symbolically for every rational/real `g>0` by star elimination and a rank-one edge update. Constant boundary potential remains a null excitation. A gauge interpretation must supply a compensating metric/weight, altered observer, or state equivalence; it cannot be inferred from shell identity alone.

## What is conserved, and what is open

| Typed payload | 1→4 | 2→3 | Status |
| --- | --- | --- | --- |
| Oriented outer boundary chain and exact shell coordinates | Preserved | Preserved | EXACT |
| Relative fundamental class, degree `+1` | Integral map | Total class integral via rational cell map | EXACT / stated maps |
| Unit top-cell quadratic stock across the move | `1→4` | `2→3` | **Not conserved** under these maps |
| Unit-metric generator and full boundary response | Changed | Changed | EXACT under declared metric/port |
| Electron charge, mass, physical energy, event time | No defined map | No defined map | OPEN |

**Disposition:** The source-bound chain and symmetry requirements determine an exact transport for 1→4 and a symmetry-forced rational transport for 2→3, but they do not select a local *dynamical event* or physical weight. AUTO_LOCK the scoped chain-map and positive-weight no-go statements after exact replay. AUTO_FREEZE a claim that the preserved relative orientation class is electric charge or that its stock jump is heat. Independent non-constructor review NOT_RUN. Next dependency: a source-selected state update with a cross-move support/reservoir receipt, plus an independently defined edge/face or boundary observable. Only then can a physical charge or force bridge be preregistered against measurements.

Run `python3 experiments/pachner-state-transport/audit.py`. It imports the preceding exact-coordinate chain builder, verifies every chain equation and automorphism over `Fraction`, tests the integral apex-anchored alternative, counts the generator mismatch and checks rational positive-edge responses. The [result record](results.json) contains all matrices, symmetry counts and stock values; see the mathematical receipt and immutable run manifest for source hashes and limitations.
