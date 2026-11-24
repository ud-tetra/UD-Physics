# Interior-vertex birth and repeated Whitney recurrence v0.1

**2026-11-23 | EXACT/CONDITIONAL; NO-GO_SCOPED; OPEN_EVENT_SOURCE. Physical Promotion = 0.**

## Pinned provenance and typed model
- UD-Physics main `ea93a86305925aced4ad9aa43b8bc7979f5b0f15`: `experiments/four-cell-tetrahedron/README.md` v1.0 blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`, `experiments/pachner-boundary-observability/README.md` v0.1 blob `a7aa4a19f4da25ff94783053542c33f9aef188dc`, and `experiments/pachner-state-transport/README.md` v0.1 blob `0523255744e43cb3849730eb44d5faed5a505077`.
- Predecessor [draft PR #476](https://github.com/ud-tetra/UD-Physics/pull/476) at `bd78ee5723f84c02dfe2e0c5d8d965ff68c8113f`.
- UD main `2e47d8718742cdd56ed81c41941b1cc3d42ad74b`, ledger v0.85 Git blob `93e2ca31eba625989087275a71c4857848e321c6`, Q165/Q169/Q177–Q179/Q200/Q210. Fixed-complex stock and generator are not an event-birth law.
- Old tetra `[0123]` with vertices `(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)`. New centroid `4=(0,0,0)`. The 1→4 move sends `[0123]` to `[0124],[0134],[0234],[1234]`, a *single-carrier* subdivision, not a two-packet union.
- Coefficients real/rational, lexicographic simplices; dimensionless Euclidean coordinates and barycentric finite elements. Geometric grade-k Whitney masses scale as length^(3−2k) if physical length is introduced; any direct cross-grade physical stock needs a separate normalization/unit map. Formal evolution parameter only, not physical time.

## Birth/admission gate (OPEN)
The mathematical move is `K'=4*boundary(K)`, f-vectors `(4,6,4,1)→(5,10,10,4)`, dimensions 15→29, preserving shell and total volume 8/3. It is authorized as a *candidate operation*, not caused by the old 15D fixed-complex incidence generator: an operator on C(K) does not itself specify a new vertex and new complex. A centroid is unique under full Euclidean regular tetrahedral S4 symmetry **given an insertion**, but does not select when to insert or what initializes born modes. No threshold, contact flag, physical clock or reserve was invented. Existing Pachner records likewise distinguish prescribed maps from source-derived trigger. Physical Promotion 0.

## Parent-to-child chain and Whitney cochain transport
Let `T_k` be signed **integral chain** subdivision: old boundary simplices remain, old top tetra maps to the signed four-cell sum. `B'_k T_k=T_(k−1) B_k`; `T3ᵀ T3=4`, so Q165 *unit coefficient chain stock* is not isometric.

Let `P_k:C^k(K)→C^k(K')` instead integrate parent Whitney forms over new k-simplices. In exact affine barycentric coordinates, its coefficient is `P_k[s,t]=det([lambda_j(v)]_{v in s,j in t})`, with k=0 evaluation. `P_0` restricts to identity on old vertices and gives `(1/4,1/4,1/4,1/4)` at the center; signed `P3=(1,-1,1,-1)ᵀ/4`.

**EXACT checks:** `d' P=P d` at all grades, `P_kᵀ M'_k P_k=M_k` for k=0,1,2,3, with `M_k` actual positive definite exact Whitney mass matrices `∑∫<w_i,w_j>dV`; the script directly integrates barycentric affine polynomial products using `∫lambda_i lambda_j=V(1+delta_ij)/20`. Grade dimensions old `4,6,4,1`, new `5,10,10,4`. Original top mass `3/8`, new `(3/2)I4`; exact pullback `3/8`. A noncentroid vertex `(1/2,1/4,1/8)` (barycentric `(15,9,5,3)/32`) also passes **all four Whitney isometry checks**, so this is true same-domain refinement, not centroid-specific.

**Exactly 14 additional cochain coordinates** exist but an isometric prolongation maps the old 15D state into a 15D subspace of 29D; it neither generates independent born amplitudes nor chooses a birth trigger.

## Dynamics and repeat-refinement counterexample
Define cochain `d=Bᵀ` and a **different, geometric-metric** skew Hodge–Dirac `A_M=d−M⁻¹dᵀM`, `M=diag(M0,...,M3)`. On each fixed complex `A_MᵀM+MA_M=0`. This is NOT the inherited Q169 Euclidean-coefficient `A_unit=d−dᵀ`: the choice of Whitney metric changes the model.

- **Centroid 0→1:** exact `A'_M P=P A_M` (rank-zero residual), so the 15D prolongation image remains invariant under this conditional first-level Whitney flow. The inherited *unit* generator gives residual rank **7**, 28 nonzero entries, squared Frobenius norm **15/4** under cochain P.
- **Noncentroid 0→1:** all-grade Whitney mass pullback remains exact, while weighted `A'_M P−P A_M` residual has rank **4**, 80 nonzero entries. Isometry does not entail intertwining.
- **Centroid all-cell recursion 1→2:** split each of the four level-1 tetra at its centroid, giving f-vector `(9,26,34,16)` and dimension **85**. All-grade cochain differential and Whitney metric identities pass again. Yet the (invertibly mass-premultiplied) Hodge–Dirac intertwining defect has rank **13**, 306 nonzero entries. Thus first-level intertwining is not an automatically recursive identity. All coordinates of the second-level centers are exact rationals. A preliminary use of floating-point division was caught and corrected before the recorded exact result.

The first centroid step generates no complement amplitude from an initial prolonged state under its particular Whitney generator; the second step can mix internal complementary modes. This is an exact conditional model finding, not a physical particle or wave prediction.

**Recursion counts:** after splitting every tetra at every generation, `N_t(n)=4^n`, `N_v(n)=(4^n+11)/3`, fixed exterior boundary; graded Whitney embeddings compose isometrically. Child tetrahedra are not regular/similar and no mesh-shape-independent physics is inferred.

## Evidence and release boundary
Local SymPy exact scripts: `verify.py` (cochain/chain, unit generator), `whitney_allgrades.py` (all grades), `weighted_generator.py` (centroid), `weighted_noncentroid.py`, `level2.py`. Actual local package `UD_PACHNER_VERTEX_BIRTH_WHITNEY_RECURSION_v0.1.zip` SHA256 `386873e43b7d042bf8c746520fffbd5fddc6f97cf794f0b50073775d6c56ecc1`. This repo report is a parallel publication, not byte-identical to ZIP. Local constructor replay PASS. Published-file standalone replay and full repo validation/CI/non-constructor review NOT_RUN. No accepted mainline theorem/metric/event law or physical correspondence.

**Next gate:** pre-event intrinsic birth predicate with lawful new-vertex state source; repeated-grade stock and generator update with S4 and mesh perturbation controls; held-out boundary observable null. Keep physical promotion 0.
