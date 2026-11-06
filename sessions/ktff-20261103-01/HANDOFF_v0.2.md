# Klein–K4 Discovery handoff v0.2 — finite seam and independent double cover

**Task** `klein-tetra-face-flip-20261103`; **session** `ktff-20261103-01`; **claim** `refs/heads/claims/klein-tetra-face-flip-20261103` HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`; PR #301 draft. Original verified source revision `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, main has advanced. No shared state/CURRENT change, merge, claim release or mainline export. Physical promotion 0.

## Source and purpose

- Imported original K4 signed chain operator: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3.
- Imported warning: `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` v1.0, edgewise sign connection is nonflat on triangles and must not be silently identified with a flat orientation line.
- Earlier claimed result `experiments/klein-tetra-face-flip-20261103/README.md` v0.1, exact tetrahedral-shell χ=2 vs Klein χ=0, 108 whole-face pairing no-go, two-face patch quotient.
- User proposed Klein face flipping before study; seam gluing and quarter-turn sample phase chosen as model inputs. No empirical target exposed or fitted.

## Result and two independent algorithms

The two triangular face patches [012] and [023] from K4 become a **two-dimensional** Klein Delta-complex only after excising the other two faces and adding edge identifications [01]~[32] and [03]~[21]. This is neither the unchanged K4 shell nor a closed 3D packet-gluing theorem.

Base B2=[[1,-1],[-1,-1],[-1,1]], Smith (1,2), H1=Z⊕Z/2, H2=0.

**Algorithm A:** Duplicate each triangle with orientation sheets 0,1; pair oriented sides with a sheet switch precisely for same-sign appearances, identify vertices with disjoint-set union and construct signed B1 (2x6), B2 (6x4). Exact: B1 B2=0, ranks (1,3), Smith B2 nonzero (1,1,1), gcd rank3 cycle-lattice minors=1, H1=Z², H2=Z. Orientation cocycle w1=(1,0,1) on base is nontrivial and pulls back to B1^T*(0,1) mod2: globally twisted downstairs, frame-trivial upstairs.

**Algorithm B:** Start independently from group <h,v | h v h^-1 v>, with h switching orientation sheets and v preserving them. Construct 2-vertex,4-edge,2-face Schreier cellular cover; B1 rank1,B2 rank1 and primitive relation v0+v1. H1=Z²,H2=Z, matching Algorithm A despite different CW decomposition. Neither algorithm provides non-constructor review; mathematical independence is by representation/method, not investigators.

**Transport:** U_h=F reflection, U_v=R quarter turn, U_x=R F; face words h v^-1 x^-1 and h^-1 v^-1 x have exact identity holonomies. det(U_h)=-1 around global twist h; two traversals +1. Closed-loop det invariant under local frame conjugation. R angle free; no physical time, energy, matter retention, or full 15D K4 dynamics source.

## Reproduce

```bash
python3 experiments/klein-tetra-face-flip-20261103/cover_audit_v02.py
python3 experiments/klein-tetra-face-flip-20261103/independent_cw_v02.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_cover_v02.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Files: `experiments/klein-tetra-face-flip-20261103/DOUBLE_COVER_AND_TRANSPORT_v0.2.md`, `cover_audit_v02.py`, `cover_results_v02.json`, `independent_cw_v02.py`, `independent_cw_results_v02.json`, `test_cover_v02.py`; typed receipt `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.2.json`; this handoff and session journal. Local equivalent exact algorithms PASS, four local unit tests PASS. GitHub CI integrity status must be checked for exact head; no claim of external scientific replication.

## Priority and stopping condition

The physical claim is **OPEN**. Before any dynamics interpretation derive a real K4 packet adjacency, seam topology and an incidence-compatible map of the signed native 15D carrier into a twisted local system; specify evolution clock, readout and conservation. If no such mechanism is source-selected, park the Klein correspondence as a mathematical topology candidate. A surface frame flip alone does not create inside/outside motion, gauge forces, fermions or a particle mechanism.

No release of claim or mainline merge.
