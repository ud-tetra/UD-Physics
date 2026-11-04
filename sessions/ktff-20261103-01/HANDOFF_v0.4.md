# Klein–K4 three-dimensional seam handoff v0.4

**Task:** klein-tetra-face-flip-20261103; **session:** ktff-20261103-01. **Claim:** `refs/heads/claims/klein-tetra-face-flip-20261103` HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated Discovery branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, PR #301 draft. Original verified task base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, latest main examined `fbb21d58a7662b737e4a2fb5276fefedc547412b`. No shared mainline update, merge or claim release. Physical promotion 0.

## Answer to scientific question

A Klein-type connection is useful to UD as a topology-sensitive **orientation transport** and path comparison observable. It separates a closed loop returning to its packet address from a loop returning its oriented frame unchanged. Two traversals of the twist loop restore the orientation sign. This mathematical behavior is *not* irreversible energy transfer, an automatically selected particle identity or a physical clock. Exact isospectrality of the earlier 60D twisted/untwisted models rules out assuming an ungraded spectral signal from the twist alone.

## New 3D geometric construction, with declared assumption

Two adjacent K4 triangular face patches [012] and [023] form a 2D square after cutting off the other tetrahedral faces. Add Klein edge identifications [01]~[32], [03]~[21], shared diagonal [02], then form K×I. This is a true **nonorientable compact 3-manifold** with two Klein boundary components but NOT the original filled K4 tetrahedron or a topology-preserving local Pachner move. Two triangular prisms ×36 barycentric flag tetrahedra/prism produce a finite 72-tetrahedron labelled Delta-complex.

Exact quotient f-vector (18,102,156,72); internal triangle pairs132, boundary triangles24. Each boundary component has (6,18,12). The full ordinary integral signed boundary ∂ satisfies ∂₁∂₂=∂₂∂₃=0 and ranks over Q (17,84,72); ordinary real Betti (1,1,0,0). Euler 0. An additional direct tetrahedron-orientation-consistency test reaches all72 tetra and finds contradictions, confirming nonorientability.

## Typed chain bridge

CW cellular model with pulled-back Klein orientation character `rho(h)=-1,rho(v)=+1`: `C(K;Zrho)⊗C(I;Z)` with dimensions by degree (2,5,4,1). The prior 60D model is `C(K;Zrho)⊗C(K4;Z)` with graded dims (4,14,20,15,6,1). Exact integral map `M=id⊗f`, `f(v0)=[0],f(v1)=[1],f([v0v1])=[01]`, commutes with signed boundary in degrees0..3 and has injective ranks (2,5,4,1). Twist character rho(h) is preserved. This is a genuine **3D cellular chain-map certificate**, but an explicit **72 tetrahedral simplex-to-twisted-cellular** matrix remains NOT_RUN. The ordinary 72-tet chains have trivial coefficients; a natural nonzero constant-fiber map to nontrivial Zrho is impossible without first twisting the source local system (f=-f over Z implies f=0). A chain map need not intertwine skew generators or preserve the chosen unit norms.

## Source-compatible packet transport and observable failure

Source `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 supplies signed S4 K4 chain actions and the native generator. Directed seam [01]→[32] has two full vertex-permutation extensions: (3,2,0,1) odd and (3,2,1,0) even. Both induced signed 15D chain matrices commute with native d_K and A_K and preserve unit norm. Combined with rho(h)=-1, their top-cell signs are respectively +1 and -1. Thus the gluing cannot source-select a unique packet top-cell orientation observable. A **topological** framed seam-loop sign rho(h)=-1 is well-defined and differs from untwisted rho(h)=+1, but an operational physical readout requires an independent orientation reference and a source-selected vertex-map completion; source-native norm/support is blind to the distinction. No fitted phase or physical normalization was used.

## Reproduce and checks

```bash
python3 experiments/klein-tetra-face-flip-20261103/bulk_prism_v04.py
python3 experiments/klein-tetra-face-flip-20261103/bulk_bridge_v04.py
python3 experiments/klein-tetra-face-flip-20261103/full_chain_seam_v04.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_bulk_v04.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Versioned proof `experiments/klein-tetra-face-flip-20261103/THREED_KLEIN_PACKET_SEAM_v0.4.md`; three exact scripts and corresponding results, four-test suite, `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.4.json`; session journal/checkpoint and this handoff.

Local **equivalent** exact programs PASS the 72-tet quotient, all signed boundary compositions and ranks, boundary connectivity, CW 3D-to-60D chain map, and two S4 operators. Four local tests are constructor-produced, not external review. A local SHA-256-verified reproducibility ZIP is available with source files distinct in bytes from GitHub equivalents; do not misrepresent its hashes as GitHub input hashes. Repository CI status must be checked on final SHA and distinguished from mathematical validation.

## Next discriminant

Build the **pulled-back twisted local-coefficient** 72-tet signed boundary and its explicit subdivision-to-cellular chain-map matrix; then derive an admitted framed measurement/readout from UD source rather than attaching one by choice. If no source-selected orientation reference or seam-selection rule exists, keep the 3D result as a conditional mathematical model. All physical bridges OPEN, physical promotion 0.

## Exact full K4 transport amendment in the same v0.4 session

Additional source-native signed-S4 tests establish that the original cellular map choosing K4 edge [01] is equivariant only under scalar orientation monodromy rho(h)=-1; after selecting a nontrivial K4 vertex extension of the h seam, the original map does **not** commute with full packet transport.

For **even** extension p=(3,2,1,0), a different integer chain inclusion *is* equivariant: f0(v0)=K4 vertex0+vertex3, f0(v1)=vertex1+vertex2, f1(e)=edge02−edge13. It satisfies d_K4 f1=f0 d_I and R_K(p) f=f, with injective ranks (2,1). Its unit-cell Gram matrices are (2I2,[2]), so it is not an isometry. For odd extension p=(3,2,0,1), the K4 vertex fixed subspace has rank 1; no rank2 injective degree-zero map into that invariant subspace exists under the same scalar rho action. See `experiments/klein-tetra-face-flip-20261103/packet_intertwiner_v04.py` and `packet_intertwiner_results_v04.json`. This is a stronger **scoped source-selection obstruction**: an integral compatible full-packet bridge exists in one deliberately chosen branch, but the seam does not force that branch or its native normalization.

Ordinary (trivial-coefficient) 72-tetrahedron chains cannot be naturally identified with twisted-coefficient 3D CW chains by a nonzero monodromy-equivariant constant-fiber map: h forces f=-f over Z. The explicit 72-simplicial **twisted** subdivision map remains OPEN. GitHub CI and non-constructor review statuses are tracked separately. Local standalone calculation/outputs and SHA-256 manifest are packaged in `KLEIN_3D_TETRA_SEAM_v0.4.zip` (equivalent implementations, not byte-identical to committed files).
