# Klein–K4 finite face-patch transport and independent double-cover audit v0.2

**2026-11-04 / UD-Physics Discovery / EXACT-CONDITIONAL topology and transport, SOURCE-GATED dynamics / physical promotion 0.** This is a scoped continuation of the HELD task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`. Original source base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; [v0.1 result](README.md). Sources: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 (native filled-K4 signed incidence and S4), `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` v1.0 (nonflat edgewise sign warning). Seam source placeholder remains unusable. New topology is a **candidate assumption**.

## 1. Two tetrahedral face patches and a NEW seam

Take adjacent *face patches* [012] and [023] from one K4 shell. Their union is a quadrilateral with diagonal [02]. Cut away the other two tetrahedral faces [013] and [123]. Keep the two oriented triangles, then impose new boundary-edge identifications:
```
[01] ~ [32] -> h,  [03] ~ [21] -> v,  [02] -> x .
```
The one-vertex three-edge two-face quotient is a Klein **Delta-complex**, with
```
             [012]  [023]
h              1     -1
v             -1     -1
x             -1      1
```
so B1=0 and B2 has Smith factors 1,2. Integral H1=Z⊕Z/2, H2=0; Euler characteristic 0. This **does not** arise by a local face flip or Pachner move in the unchanged tetrahedral sphere (Euler 2). It is not a closed three-dimensional tetrahedral bulk; there is no claim that the 3-cell survives its altered face identification as a 3-manifold.

## 2. First workload — exact orientation double cover

Duplicate the two triangles, giving the four labeled faces (t0,0),(t0,1),(t1,0),(t1,1). Match each paired base edge across the two sheets so the lifted quotient is consistently orientable. If the two base triangle sides use the same orientation, the sheet changes; for opposite side orientations it does not. Identify their oriented vertices and edges by union-find.

The resulting finite CW/Delta-complex has
```
C0=Z², C1=Z^6, C2=Z^4,
B1 = [-1  1  0  0  1 -1;
       1 -1  0  0 -1  1],

B2 = [ 1  0 -1  0;
       0  1  0 -1;
       1  0  0  1;
       0  1  1  0;
       1  0 -1  0;
       0  1  0 -1].
```
Exactly B1*B2=0, rank(B1)=1, rank(B2)=3; the Smith nonzero factors of B2 are (1,1,1), and the gcd of rank-three minors of its representation in the graph-cycle lattice is 1. Hence H1=Z² without torsion, H2=Z, and chi=2−6+4=0; the connected, orientable surface is a torus. The fundamental oriented 2-chain has coefficient pattern (-1,+1,-1,+1), a nonzero kernel vector of B2.

The base orientation cocycle w1=(1,0,1) on (h,v,x) is nontrivial over F2 because base B1=0 and w1 is not zero, while w1 B2=0 mod2. Its cover pullback to the six lifted edges is (1,1,0,0,1,1), which equals B1^T*(0,1) mod2; **the global orientation obstruction becomes a mere local frame choice on the cover**.

## 3. Independent workload — different CW presentation

A separate checker does **not use** the two-triangle incidence construction. Start from the Klein group presentation `<h,v | h v h^-1 v>` and orientation character h→sheet switch, v→same sheet. The Schreier two-sheet CW complex has two vertices, four directed 1-cells (h0,h1,v0,v1), and two 2-cells. Its boundary maps are
```
B1_CW = [-1  1  0  0;
          1 -1  0  0],
B2_CW = [0  0;
         0  0;
         1  1;
         1  1].
```
Ranks (1,1), chain composition zero, primitive 2-cell relation, and 2-cell kernel rank 1 prove H1=Z² and H2=Z. The base one-cell presentation has boundary 2v, so H1=Z⊕Z/2. Thus **different chain decompositions reproduce the same integral homology**, independently supporting the double-cover interpretation. Both checks were produced within this research session; they are different algorithms, **not** non-constructor review.

## 4. Flat local transport versus global orientation reversal

Define an exact sample O(2) representation
```
U_h=F=diag(1,-1),  U_v=R=[[0,-1],[1,0]],  U_x=R F .
```
The two *oriented triangle boundary words* are h v^-1 x^-1 and h^-1 v^-1 x. Exactly
```
F R^-1 (R F)^-1=I,
F^-1 R^-1 (R F)=I.
```
Both contractible faces are **flat**, yet the noncontractible loop h has det(U_h)=-1 and h² has +1. Under local frame gauge changes the based closed-loop matrix conjugates; determinant is unchanged. Hence this is a **gauge-invariant topological orientation readout** for this declared gluing, not a mere local choice of sign. The specific quarter rotation R is a matrix fixture; replace it by any R(phi) and flatness remains, so topology alone does not fix phi.

Controls: on the original uncut K4 sphere, all loops are contractible, so a flat orientation character has trivial holonomy. On the orientable torus control, the orientation character is zero, and a flat O(2) holonomy can be chosen entirely in SO(2), with no forced reflection. The QPB1 loop-history source's edgewise -1 on *every* edge has nontrivial elementary triangle curvature and must **not** be conflated with this flat global w1.

## 5. What the proposed dynamics means—and what remains OPEN

A *path transport step* sends a local frame psi to U_e psi; after a twist loop its orientation is reversed. This is path/holonomy kinematics, not a native time-evolution generator, a face material turnover, physical inside/outside exchange, retained burden or an emergent particle. The candidate supplies **no new physical coupling**, SI units, preparation or dynamical readout on the 15D K4 carrier. To promote it as native UD, source or derive (i) the additional edge-pair seam gluing, (ii) a typed incidence-preserving map from K4 packet carriers to the twisted patch local system, (iii) a local update/clock and current conservation, and (iv) an independently discriminating physical measurement.

## 6. Reproducibility and evidence status

```bash
python3 experiments/klein-tetra-face-flip-20261103/cover_audit_v02.py
python3 experiments/klein-tetra-face-flip-20261103/independent_cw_v02.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_cover_v02.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Expected machine-readable outputs are `cover_results_v02.json` and `independent_cw_results_v02.json`. The scripts use SymPy exact integer matrices and Smith normal form; no floating-point computation. Equivalent local programs passed both exact audits and four unit tests. Repository integrity CI checks repository structure; it is not a scientific replication. The orientation seam hypothesis is **target exposed** (user proposed Klein-bottle mechanism); flatness, torsion, and twist results are mathematical consequences under that explicit topology. No physical target was used for calibration.

**Disposition:** EXACT/CONDITIONAL finite face-patch quotient, integer homology and loop holonomy; CANDIDATE new UD seam operator; OPEN source-selected seam, bulk 3D gluing, dynamical generator, persistence, and physical correspondence. No mainline promotion or mutation of the accepted coefficient ledger.
