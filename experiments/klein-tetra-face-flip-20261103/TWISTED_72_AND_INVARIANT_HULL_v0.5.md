# Klein–K4 v0.5 — complete 72-tetrahedron twisted boundary, rational comparison map and invariant packet hull

**2026-11-04. Discovery / EXACT-CONDITIONAL / NONCANONICAL MAP / PHYSICAL PROMOTION 0.** Task `klein-tetra-face-flip-20261103`, same session `ktff-20261103-01`, live HELD claim `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, isolated branch and draft PR #301. Source base originally `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; reread main at `fbb21d58a7662b737e4a2fb5276fefedc547412b`. Mainline export, physical measurement and claim release remain unauthorized.

## 1. Typed source objects

- Read-only UD source `experiments/qpb1-local-generators/README.md` v1.0 §§1–3: signed filled-K4 integral chain, 15 coordinate real unit-metric skew generator `A_K=d_K-d_Kᵀ`, full signed S4 action; `A_K³+4A_K=0`.
- `experiments/klein-tetra-face-flip-20261103/THREED_KLEIN_PACKET_SEAM_v0.4.md` (own Discovery) supplies the **assumed** nonorientable 3-manifold `M=Klein×I` with 72 labeled barycentric tetrahedra, ordinary f=(18,102,156,72), integral B²=0 and signed S4 extension ambiguity. The new Klein gluing is not a native K4 Pachner move.
- Distinguish: integral **twisted local-system simplicial chains** `C_*(M;Z_rho)`; rational extension for harmonic comparison; minimal cellular `C_*(K;Z_rho)⊗C_*(I)`; formal 60D `C_*(K;Z_rho)⊗C_*(Delta³)`; and original 15D K4 dynamics. These are not interchangeable.

## 2. The complete twisted boundary, not just a coarse CW proxy

Let `rho(h)=-1,rho(v)=+1,rho(x)=-1` be the flat orientation character on the base two-face Klein quotient. Duplicate **every barycentric simplex** of the 72-tetrahedron K×I assembly into sheets 0/1, then on the three glued rectangular prism sides identify sheet labels with flips `(1,0,1)`. This produces the 2-fold orientable cover, with

```
degree k             0    1    2    3
cover cells         36  204  312  144
anti-invariant      18  102  156   72
```

For each deck-paired k-simplex choose `[s,0]-[s,1]` as anti-invariant generator. The full integer twisted boundary `B_k^rho` is obtained by taking signed faces upstairs and projecting to these oriented anti-invariants. The implementation `twisted_72_boundary_v05.py` generates **every entry** of matrices sized `18×102,102×156,156×72`. Exact checks:

```
B1^rho B2^rho=0, B2^rho B3^rho=0;
rank_Q B1^rho,B2^rho,B3^rho = (18,83,72);
Betti_Q = (0,1,1,0).
```

An **independent integer Smith-form reduction of B1** finds invariant factors `(1 repeated 17 times,2)`, hence `H0(M;Zrho)=Z/2Z`. The full integral H1 and H2 Smith quotients are NOT independently recomputed from the 72D matrices; the known cellular product topology gives H1=Z,H2=Z. Do not treat rational Betti counts as integral torsion certificates.

The sheet-anti-invariant construction enforces the twist on *all* 72 tetrahedra, not an arbitrary hand-placed edge sign. It remains conditional on the originally assumed Klein×I gluing.

## 3. An explicit, but non-geometric, rational simplicial-to-cellular chain map

Let `B_s` be the new exact twisted simplicial boundary and `B_c` the previously constructed twisted **cellular** boundary of K×I. In real/rational unit-coordinate metrics, both chain complexes have one harmonic class in degrees 1 and 2 and none in 0 and 3. Choose nonzero exact harmonic vectors `h_k∈ker B_{s,k}∩ker B_{s,k+1}ᵀ` and `t_k∈ker B_{c,k}∩ker B_{c,k+1}ᵀ`. Define

```
Phi_0=0, Phi_3=0,
Phi_k = t_k h_k^T / (h_k^T h_k), k=1,2.
```

This is an **explicit rational matrix formula for every simplicial basis vector**, with exactly computed source harmonic norms `h1²=160,h2²=84` and cellular target norms `t1²=t2²=2`. Exact code checks `B_c Phi=Phi B_s` in all three degrees and `Phi_k h_k=t_k` for k=1,2. The resulting map has graded ranks `(0,1,1,0)`, and its composite with the previous integral cellular-to-60D inclusion is also a rational chain map with ranks `(0,1,1,0)`. It induces an isomorphism on **rational H1 and H2**.

**OPEN / IMPORTANT LIMITATION:** This is a chosen *global harmonic matching* under unit-coordinate metrics, not the natural local barycentric-subdivision-to-cellular retraction, not an integral homotopy equivalence and not a certificate that Z/2 torsion in H0 survives. A canonical, local, integral subdivision chain map remains the next topological gate. A rational map of ranks (0,1,1,0) is not allowed to silently replace it.

## 4. Dynamically closed 5D source-native K4 carrier

The previous even-S4 seam-compatible interval chain embedding F has rank3 and Gram `FᵀF=2I3`, but leaks out of its image under the unmodified K4 skew generator A_K. Define the minimal A-invariant Krylov hull

```
H = span_Q{im F, A_K im F, A_K² im F}.
```

Since `A_K³=-4A_K`, this span is invariant. Exact rank is **5**; it is the unique minimal linear invariant subspace containing im F. Define its unit-metric orthogonal projector `P_H=H(HᵀH)^{-1}Hᵀ`. Then

```
P_H A_K=A_K P_H, (I-P_H)A_K H=0.
```

The hull contains one harmonic mode and four active real modes (two source-native 2-rate oscillators). The even seam permutation `p=(3,2,1,0)` fixes this hull pointwise: `R_K(p)x=x` for all x∈H. Therefore the **chosen** combined orientation seam `U_tw=-R_K(p)` restricts to `-I5`; the orientable no-twist control `U_0=R_K(p)` restricts to `+I5`. For every nonzero x in H, using **the declared source unit metric**,

```
<x,U_tw x> = -||x||²,       <x,U_0 x> = +||x||².
```

This is a parameter-free **mathematical framed correlation** given the unit metric and selected even extension, not an identified laboratory observable. No inserted seam phase angle or empirical normalization is needed for this exact contrast, but a **physical orientation reference/preparation and coupling to measurement remain OPEN**. The even S4 completion and initial hull admission are additional choices; the odd S4 extension is not ruled out globally, only excluded under the earlier rank2 fixed-space requirement. The hull closure does not prove attraction, cluster selection or retained matter.

## 5. Dynamics, locality and scope

Source evolution on the 5D hull is a well-defined restriction `x'=A_K|_H x`, with prescribed initial `x(0)∈H`, conserved source norm and unchanged K4 unit metric. The 72-tet *full* twisted simplicial evolution or full 60D versus 72D metric intertwiner is **not proved**. The rational harmonic comparison is nonlocal by construction; no physical spatial range or clock is derived. Any finite packet network with a source-selected seam and operational reference remains OPEN.

## 6. Reproduction

```bash
python3 experiments/klein-tetra-face-flip-20261103/twisted_72_boundary_v05.py
python3 experiments/klein-tetra-face-flip-20261103/rational_comparison_v05.py
python3 experiments/klein-tetra-face-flip-20261103/invariant_hull_v05.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_v05.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Expected exact results in three corresponding JSON files; typed mathematical receipt `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.5.json`. Local same-constructor exact calculations PASS; repository CI only checks records/tooling; external non-constructor proof review NOT_RUN. No physical target fit or experimental evidence; physical promotion remains 0.

**Disposition:** Exact finite twisted 72-simplex boundary and exact 5D invariant native K4 subspace **within the assumed topology and even seam branch**. Rational H1/H2 comparison exists but cannot be promoted to an integral geometric cellular retraction. Physical orientation readout remains source-blocked. Next best discriminant: construct the *integral cellular subdivision map and chain homotopy* preserving Z2 torsion, then seek a source-selected packet seam and operational framed reference.
