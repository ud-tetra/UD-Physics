# Three-dimensional Klein–K4 prism gluing and packet bridge v0.4

**2026-11-04 | UD-Physics Discovery | EXACT/CONDITIONAL finite topology and chain algebra / OPEN source selection | physical promotion 0.**

## Typed scope and original source

Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, HELD claim `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, existing isolated branch and draft PR #301. Original task base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; latest examined main `fbb21d58a7662b737e4a2fb5276fefedc547412b`. No mainline ledger update or physical promotion.

Source-native mathematical pieces are `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 (signed filled-K4 chain, unit-metric skew generator, signed S4 representation) and `experiments/pachner-state-transport/README.md` v0.1 (chain maps need not be isometries or intertwine unit generators). The earlier local Klein model is `experiments/klein-tetra-face-flip-20261103/{README.md,DOUBLE_COVER_AND_TRANSPORT_v0.2.md,TWISTED_K4_PACKET_CHAIN_v0.3.md}`. The existing seam-phase snapshot in the repository is a placeholder; it supplies **no** physical topology selector. All new 3D seam identifications below are explicit CANDIDATE inputs.

## 1. Actual tetrahedral assembly: a nonorientable three-manifold

Let K be the two-triangle Klein Delta-complex built from the *cut* K4 face patch `[012]∪[023]` by new base-edge identifications `[01]~[32]`, `[03]~[21]`, and shared diagonal `[02]` with itself. Its construction is not the unchanged K4 sphere and does not preserve the original filled tetrahedron.

Build M=K×I. It has **two triangular prism three-cells** (one for each base triangle), three rectangle-side gluing pairs, and two Klein boundary components. A triangular prism has 6 vertices,9 edges,5 faces,1 bulk cell. Its barycentric subdivision contains 36 tetrahedra corresponding to incidence flags vertex⊂edge⊂face⊂prism. Glue corresponding barycentric side flags under the three rectangular-face identifications. This yields **72 distinct tetrahedral Δ-cells**, not 72 globally unique four-vertex sets; duplicate vertex sets must remain distinct labeled Δ-simplices because K has quotient identifications.

EXACT quotient audit (`bulk_prism_v04.py`) yields

```
(V,E,F,T)=(18,102,156,72),  Euler=0.
132 interior triangular face classes, each incident to 2 tetrahedra;
24 boundary triangle classes, each incident to 1 tetrahedron;
each boundary component has (V,E,F)=(6,18,12), Euler=0.
```

With oriented barycentric flag bases, the integer boundary matrices have shapes B1:18×102, B2:102×156, B3:156×72 and exactly B1B2=B2B3=0. Exact rational ranks `(17,84,72)` give ordinary real Betti vector `(1,1,0,0)`, consistent with K×I. This is a valid finite nonorientable 3D Δ-complex. A Klein bottle cannot be the *only boundary* of an orientable 3-manifold; here the bulk itself is nonorientable with two Klein boundary components. No oriented 3D volume, Euclidean embedding, or physical interior/exterior swap is implied.

## 2. Explicit cellular chain map into the earlier 60D twisted carrier

The cellular 3D bulk is `C_*(K;Z_rho)⊗C_*(I;Z)`, where `rho(h)=-1, rho(v)=+1` is the orientation local coefficient. The earlier 60D target is `C_*(K;Z_rho)⊗C_*(Delta³;Z)`.

Define the **integer degree-preserving interval inclusion** `f:C_*(I;Z)→C_*(Delta³;Z)` by `f(v0)=[0]`, `f(v1)=[1]`, `f(e)=[01]`; `∂_K4 f(e)=[1]-[0]=f∂_I(e)`. Therefore

```
M = id_(C(K;rho)) tensor f
d_60 M = M d_(K×I,rho).
```

An explicit exact matrix replay (`bulk_bridge_v04.py`) verifies all graded blocks:
```
degree         0    1    2    3
domain         2    5    4    1
target         4   14   20   15
rank(M)        2    5    4    1
```
All maps are injective and commute with boundary. Holonomy rho(h)=-1 acts on both coefficient factors and therefore commutes with M. **This is a chain map of the 3D cellular product**, not a verified 72-tetrahedron simplicial-to-cellular chain matrix. The latter would require explicit subdivision collapse/Alexander–Whitney coordinates; it remains OPEN. A chain map is not automatically an isometry or an intertwiner of unit-metric skew generators.

## 3. Native K4 full-chain transport and the extension ambiguity

The same directed edge seam `[01]→[32]` can be extended to the full K4 vertex set in **two** distinct S4 permutations:
```
p_odd  =(3,2,0,1)     signed top-cell character = -1;
p_even =(3,2,1,0)     signed top-cell character = +1.
```

Let R_K(p) be the actual **signed simplicial chain action** on the K4 15D carrier (not a scalar stand-in). For both extensions, `R_K(p) d_K=d_K R_K(p)`, `R_K(p) A_K=A_K R_K(p)`, `R_K(p)^T R_K(p)=I`, all verified exactly. Set a candidate combined seam transport `U_h=rho(h) R_K(p)=-R_K(p)` and `U_v=I`. Both satisfy the Klein relator and commute with the unmodified native K4 generator. However on the tetrahedral top cell, the combined sign is **+1** for odd p and **-1** for even p. Even the native top-cell sign is thus **not uniquely selected by the directed edge face map**. The extra seam orientation character rho remains fixed at -1 in either branch. A different full-packet completion is a distinct source-selection assumption, not gauge equivalence automatically.

The scalar choice `U_h=-I15` of v0.3 is the special trivial K4 relabeling. More general compatible signed S4 transports can change packet-mode information while preserving norm. No prescribed S4 completion or physical measurement is sourced.

## 4. Observable and null comparison

The *topological* closed-loop orientation character `rho(h)=-1` is invariant under local frame convention, while `rho(h)=+1` in the untwisted null. It survives the cellular chain map, since `M(-z)=-M(z)`. This is an **orientation-sensitive framed path observable**, not a native mass/energy observable. The source-native squared norm is insensitive: `||U_h x||²=||x||²` for both K4 completions and null.

For packet top-cell sign readout, the two equally compatible completions give opposite results. Therefore **NO SOURCE-SELECTED UNIQUE PACKET TOP-CELL OBSERVABLE** follows from seam edge gluing plus the original K4 incidence generator. There is no introduced phase angle or fitted numeric normalization: ρ takes values in {±1}, and S4 actions use exact signs. Distinguish this from whether an actual apparatus can access a relative orientation frame or whether the sign is physically gauge: no operational preparation/reference or bridge has been supplied.

## 5. Failure cases and promotion boundary

- The 72 tetrahedra form K×I with **new quotient gluing**. They do not reconstruct the original solid tetrahedron, a 3D orientable cosmos, or the 15D source carrier as a native physical 3D packet network.
- Integral chain nilpotency does not fix a metric, energy, clock, coupling, top-cell S4 extension, action, or physical observer.
- The 60D target is a formal graded CW tensor carrier with degree through five, not physical spacetime dimension five.
- The complete 72-tetrahedron twisted local-coefficient boundary and 72-simplex-to-cellular chain-map matrices are **not executed** in this audit. The 72-simplex ordinary boundary and cellular twisted bridge are two complementary, separately verified results.
- The source `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` reports a different, locally nonflat edge-sign connection. It is not the flat Klein rho.
- If no independent orientation reference survives physical gauge quotient, the topological sign may be unobservable. Physical promotion stays zero.

## Reproduce

```bash
python3 experiments/klein-tetra-face-flip-20261103/bulk_prism_v04.py
python3 experiments/klein-tetra-face-flip-20261103/bulk_bridge_v04.py
python3 experiments/klein-tetra-face-flip-20261103/full_chain_seam_v04.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Local exact code on these objects passed full quotient f-vector, side-face multiplicity, boundary-components, nilpotency, rational chain ranks, graded cellular intertwining, and both signed S4 completions. GitHub CI and external non-constructor review are separate and must be reported under their actual commits.

**Decision:** CONDITIONAL mathematical 3D realization **exists** as a new nonorientable prism quotient; cellular incidence bridge into the twisted model **exists**; nontrivial topological rho survives. **OPEN / NO-GO under available source** for a unique full-packet completion and physical readout without new assumptions. Next: construct the full 72-tet local-coefficient subdivision chain map and source an operational framed observable and geometry-selection law.

## Coefficient-domain limitation

The 72-tetrahedron ordinary simplicial boundary uses a constant integral coefficient system. The cellular Klein bridge instead uses the nontrivial orientation character rho(h)=-1. A fiberwise constant map from the former to the latter that respects h transport must obey f(n)=-f(n), hence f=0 over the integers. This is a scoped NO-GO for a nonzero monodromy-equivariant map between these particular coefficient systems. An appropriate 72-cell bridge must first equip its source chains with the same pulled-back orientation local system and explicitly build the twisted simplicial boundary. The present ordinary 72-tet nilpotency and twisted cellular chain map are separate exact certificates; they are not yet their composition.
