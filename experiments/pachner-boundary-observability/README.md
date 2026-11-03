# Fixed-shell Pachner moves and boundary observability v0.1

**2026-11-03. Development — no registry entry.** EXACT for the declared finite simplicial complexes and unit-chain-metric operator; CANDIDATE as a physical payload bridge. This addresses the hidden-degree/uniqueness objection without identifying native response with a Standard Model charge. The [existing four-cell analysis v1.0](../four-cell-tetrahedron/README.md), integrated base `046bfb6cc3d69122cd30028d1fbb4ff8b42a40d9`, already establishes that the 1→4 split preserves the shell but changes the full unit-metric generator. The supplied [UD coefficient provenance ledger v0.39(2)](../../artifacts/action-normalization-20261022-a1/exact-001/inputs/011-20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md), SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q166/Q167, provides adjacent-chain current and a masked contact identity; it does not select this boundary port or a particle charge. The supplied *CRL-2 Subdivision and Anti-Erosion Rules v1.0*, SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4`, is a **governance proposal**, not an accepted physical theorem. The [designated project site](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) lists Papers I–III 1.1.1 / IV 0.1 and physical promotion 0 on 2026-11-03.

## Question and typed construction

Does keeping the *outer shell* fixed force all internal retriangulations to have identical boundary-accessible dynamics? Take a finite simplicial 3-ball `K` with oriented chain maps `B_k:C_k(K;Z)→C_(k−1)(K;Z)` and `B₁B₂=B₂B₃=0`. Snap every vertex to the exact integer coordinates below, fixing the boundary vertices and their triangles throughout each move. The combinatorial boundary and shell coordinates are one type of datum. The interior chain dimensions, unit-edge graph operator, and response to a boundary excitation are different typed data.

Use the **declared** unit edge metric, not a physical conductance inferred from geometry. Define `L_K=B₁B₁ᵀ:C₀(K;Q)→C₀(K;Q)`. The dimensionless native 0↔1 incidence system `x'=-B₁y, y'=B₁ᵀx` gives `x''=-L_K x`. For boundary vertices `b` and internal vertices `i`, prescribe `x_b=φ`, solve `L_ii x_i=-L_ib φ`, and read the generalized static boundary response

`f_b=Λ_K φ`, `Λ_K=L_bb−L_bi L_ii⁻¹ L_ib`.

This is also the Hessian of the minimized quadratic `E_K(φ)=min_(x_i) (1/2)∑_(edges ab)(x_a−x_b)²=(1/2)φᵀΛ_K φ`. Its boundary response units are **native**, and its chosen hold/drive is an assumed port. It supplies no electrical charge, meV, newton, second, or Standard Model prediction. In the cases below `L_ii` is invertible whenever there are internal vertices.

## Exact snapped moves and response

| Move | Boundary coordinates fixed | `f=(V,E,F,T)` before → after | Automorphisms preserving complex and snapped distances | Probe `φ` | `Λφ` eigenvalue before → after |
| --- | --- | --- | ---: | --- | ---: |
| 1→4 | tetrahedron corners `(1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1)`; new centroid `(0,0,0)` | `(4,6,4,1)→(5,10,10,4)` | 24 (`S₄`) | `(1,−1,0,0)` | `4→5` |
| 2→3 | equator `(1,−1,0),(0,1,−1),(−1,0,1)`; apices `(1,1,1),(−1,−1,−1)` | `(5,9,7,2)→(5,10,9,3)` | 12 (`S₃×C₂`) | `(0,0,0,1,−1)` | `3→5` |

For 1→4 the exact outer boundary remains the four original triangles, the oriented boundary 2-chain is identical, and total Euclidean volume is `8/3` before and after; each of four children has volume `2/3`. The boundary graph is `K₄` with `Λ_old=4I−J`. Four unit radial edges to the new internal centroid yield

`Λ_new=(5I−J)−(1/4)J=(5/4)(4I−J)`.

Here `J=11ᵀ` on four boundary vertices. Thus the constant mode is in the kernel of both, while the three-dimensional nonconstant `S₄` representation shifts `4→5`. For the displayed probe, minimized native energy changes `4→5`. The preserved automorphism does **not** fix the response coefficient.

For 2→3, the two initial tetrahedra are `[0,1,2,3]` and `[0,1,2,4]`. They share the equatorial face. The three final tetrahedra are `[0,1,3,4]`, `[1,2,3,4]`, `[0,2,3,4]`, sharing the new apex edge `(3,4)`. Their six outer triangles and oriented boundary chain agree exactly. Total Euclidean volume is `3` on each side (initial two volumes `3/2` each; final three volumes `1` each). All five vertices lie on the outer boundary; the new edge is internal to the 3-ball and is absent from its 2-dimensional boundary complex. With `v=e₃−e₄`,

`Λ_new−Λ_old=v vᵀ`.

The apex-odd one-dimensional representation has eigenvalue `3→5`; the displayed probe's minimized energy changes `3→5`. The other three nonconstant modes have eigenvalue `5` both before and after, and the constant mode has eigenvalue `0`. Thus a boundary measurement restricted to those unchanged modes would miss this move even though a different boundary mode detects it.

Both complexes on either side have Betti vector `(1,0,0,0)` over `Q`; their boundary homology and Euler characteristic cannot serve as the discriminating payload. The complete exact chain ranks, boundary faces, response matrices and probes are in [`results.json`](results.json). The [replay](audit.py) checks boundary compositions, oriented shell equality, volumes, automorphism groups, response covariance and both probe shifts.

Repeated 1→4 moves give an unbounded **countable family of finite triangulations** with the same outer shell and face vector `(4+k,6+4k,4+6k,1+3k)` after `k≥0` insertions. This establishes growth of chain-state descriptions, not an infinite-dimensional state space at any one finite `k`, and not equality of every observable across the family.

**EXACT / observer-dependent hidden sector.** The dimension of `ker B₁` rises `3→6` in 1→4 and `5→6` in 2→3. Because `H₁=0`, each edge-cycle state is a face boundary: `ker B₁=im B₂`. Under the unmasked full 0/1/2 incidence evolution `x'=-B₁y, y'=B₁ᵀx−B₂z, z'=B₂ᵀy`, initial `x=0`, `y∈im B₂` stays in the edge/face sector and produces `x(s)=0` at every vertex for all dimensionless `s`. A vertex-only observer cannot detect these states in that linear dynamics; an edge/face readout or a declared coupling is needed. This is an exact scoped unobservable subspace, not evidence for a new electric charge. It coexists with the distinguishable vertex-driven response above.

## General visibility theorem and failure cases

**DERIVED / fixed positive unit weights.** A 1→4 move keeps every old graph edge and adds four unit edges from a new vertex `c` to the four vertices of the subdivided tetrahedron. For any fixed boundary `φ`,

`E_new(φ) ≥ E_old(φ)`.

Equality holds exactly when the unique old harmonic extension takes one common value at those four tetrahedron vertices: the new star can then have zero energy by setting `x_c` to that value. A 2→3 move keeps old graph edges and adds one edge between opposite vertices `p,q`; equality holds exactly when the old harmonic extension has `x_p=x_q`. These statements follow by minimizing a nonnegative added sum of squares; they are conditional on connected positive-weight graph energy and an unchanged boundary port. In matrix form `Λ_new−Λ_old⪰0`; its kernel is precisely the boundary excitations satisfying the stated equal-potential condition. Reverse 4→1 and 3→2 moves reverse the inequality. A constant boundary excitation is always invisible to this port. No general one-to-one reconstruction of an arbitrary interior follows.

**OPEN / physical function.** A fixed shell determines shell-derived numbers by definition; it does not establish that every internal state gives the same *measured* Standard Model constants. Conversely, two distinct interiors need not represent distinct physical states: they may be gauge-related under a specified equivalence, or inaccessible to a specified observer. To decide, a proposed UD model must declare (i) admissible moves and their state map, (ii) whether a move is gauge or dynamical, (iii) boundary preparation/readout and equivalence criterion, (iv) the conserved payload, if any, and (v) a calibrated physical bridge. A putative electron carrier needs a sourced charge operator and conservation law; a graph response eigenvalue alone is neither charge nor mass.

For a dynamical port, the corresponding *candidate* transfer matrix is `Z_K(ω)=L_bb−ω²I−L_bi(L_ii−ω²I)⁻¹L_ib` away from internal Dirichlet poles, with unit vertex inertia and dimensionless `ω`. It can distinguish resonances but has no physical clock or laboratory coupling. A boundary-fixing gauge equivalence would need to preserve the complete chosen transfer and state readout, not just the shell numbers. Finite static `Λ` alone can remain noninjective under unspecified weights or hidden sectors; this calculation does not prove predictive uniqueness.

At `ω²=1`, the exact replay checks the same chosen nonconstant modes shift `3→4` for 1→4 and `2→4` for 2→3 in `Z_K(ω)`. These are response coefficients in native dimensionless frequency, not matched to spectroscopy. The zero-frequency and finite-frequency checks use one frozen operator and one fixed choice of boundary probe, with no target-dependent parameter adjustment.

## Falsification path

Freeze a single move rule, unit/constitutive metric, initial state, boundary port, observer and equivalence rule **before** comparing targets. Test at least the two symmetry channels above and a null constant channel. If physical measurements with an independently calibrated coupling show no response where the model predicts a detectable difference, that proposed bridge fails; if all allowed interiors project identically under every declared port, either identify a gauge quotient or admit an unobservable sector. Do not select a different port after seeing a target and call it an independent prediction. The supplied *Gap 2 Final Status* is a historical working document about a separate cosmology simulation, not evidence for this Pachner bridge.

**Disposition:** AUTO_LOCK only these scoped finite complex, shell, symmetry, and conditional unit-metric response identities after exact replay. AUTO_FREEZE any claim that a Pachner move changes electron charge, forces Standard Model numbers, or explains cosmology from this calculation. Physical promotion 0; independent non-constructor review NOT_RUN. Next dependency: a source-selected local weight and move law, followed by a registered physical boundary probe with units, calibration, uncertainty and a conventional baseline.
