# Handoff — Klein bottle / K4 seam orientation v0.1

**Status:** EXACT topological no-go plus CONDITIONAL orientation transport / candidate Klein seam only. **Physical promotion 0.** Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`; HELD claim `claims/klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`; verified base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. No shared CURRENT or mainline export.

## Source and provenance

Read BOOTLOADER v1.1, AGENTS, Discovery v1.2, UD Mathematical Method v1.0, CURRENT, CONCURRENCY v2.0, ARTIFACTS at verified base. Native signed K4 incidence and S4 action: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3. `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` v1.0 says edge sign connection has non-flat triangle holonomy and is not face contraction invariant. Historical seam snapshot artifact is a placeholder and provides no source derivation. External topology control: MathWorld Klein Bottle and standard square-edge topology notes. User request exposed Klein interpretation before analysis; no physical target fitted.

## Exact findings

1. K4 tetra shell is oriented S2 with f=(4,6,4), χ=2, H1(Z)=0, H2(Z)=Z. Cannot become Klein (χ=0, H1(Z)=Z⊕Z/2, H2(Z)=0) by continuous face flip or topology-preserving Pachner move.
2. Exhaustively evaluated all 3*6*6=108 full triangular face-pair bijection quotients of K4 shell; ZERO have each quotient edge represented twice by the two quotient triangle faces. This is a necessary closed-2-manifold criterion, not a universal no-go for subdivided/cut/seam quotient mechanisms.
3. Independently constructed Klein from square with diagonal into two triangles as a **Delta-complex**: B2=[[1,-1],[-1,-1],[-1,1]], Smith invariants (1,2), H1=Z⊕Z/2, H2=0. Untwisted torus control has H1=Z², H2=Z. This is not an ordinary four-face tetrahedron or 8-vertex standard simplicial triangulation.
4. Orientation cocycle w1=(1,0,1) on (h,v,x) annihilates B2 mod2. Twist loop reverses a local oriented frame; twice returns it. Exact flat O2 test: F=diag(1,-1), R=quarter turn, FRF^-1=R^-1. Angle choice NOT determined; transport sign is a path observable, not time, stock or particle spin.
5. A local signed S4 chart flip or a locally nonflat triangle holonomy does not establish a global Klein orientation class. A new topology/gluing or an orientation-twisted local system must be declared before transplant to UD transport.

## Reproduce

```bash
python3 experiments/klein-tetra-face-flip-20261103/audit.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_klein.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Records: `experiments/klein-tetra-face-flip-20261103/{README.md,audit.py,results.json,test_klein.py}`; `candidates/klein-tetra-face-flip-20261103/{candidate.json,mathematical_receipt.json}`; session record/journal and this handoff. Exact local constructor equivalent audit PASS on 108 matchings and integral ranks/minors; separate four test checks on formulas PASS locally. Repository CI must be tied to exact commit. Non-constructor review NOT_RUN. Local full-run script and exact output available as independently downloadable artifacts, but do not conflate local byte hashes with GitHub-committed script byte hashes.

## Next discriminant

Create a *minimal finite tetrahedral patch gluing* that genuinely carries a flat nontrivial w1 and a signed incidence-compatible transport along adjacent face seams. Require U_boundary-face=I on all contractible loops and an orientation-reversing U_twist on a noncontractible loop; construct orientable double cover and compare with no-twist control. Test whether a proposed native action/stock readout can sense the flip. No physical promotion without independently calibrated bridge.
