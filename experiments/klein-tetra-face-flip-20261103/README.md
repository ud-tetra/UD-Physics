# Klein bottle seam and tetrahedral face-flip audit v0.1

**2026-11-03. UD-Physics Discovery — EXACT finite topological audit / CANDIDATE seam dynamics / physical promotion 0.**

## Question and provenance

Does a tetrahedron's apparent interior/exterior face reversal generate Klein-bottle topology, or is a separate orientation-reversing gluing/transport structure needed? Read-only UD inputs at base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`:

- `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 — oriented filled K4 15D chain complex, signed S4 action, skew incidence generator with **unit Euclidean metric**; this is not a Klein surface or topology-changing law.
- `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` v1.0, **Edgewise sign connection** — an edgewise -1 sign has triangle curvature -1 and is explicitly **not** flat/face-contractible; cannot be imported as a flat Klein orientation character.
- `artifacts/graphpktid-20261024-01/exact-001/inputs/007-04-seam_phase_transport.md` is a placeholder; supplies no recoverable seam dynamics.
- External surface baseline: Klein bottle is the nonorientable genus-two surface with χ=0; square-edge gluing representation, integral H1=Z⊕Z/2Z, H2=0. Standard minimal abstract simplicial triangulation requires 8 vertices; the **two-triangle Δ-complex** below is not such a simplicial triangulation. See [UKY topology notes](https://www.ms.uky.edu/~guillou/S14/651Notes-Week11.pdf) Example 29.2, [MathWorld](https://mathworld.wolfram.com/KleinBottle.html), and [Union mathematical preprint](https://www.math.union.edu/~dpvc/papers/1993-03.KB/vmkb.pdf).

All operators below use Z for chains, F2 for orientation and exact integer O(2) matrices for one example. No material metric, physical clock, energy, mass or quantum mapping is supplied; the seam angle is an independently chosen test value.

## Theorem A — topology cannot be induced by a mere face turn

The unglued K4 boundary ∂Δ³ has `f=(4,6,4)`, χ=2, is orientable, and has H1=0, H2=Z. A Klein bottle has χ=0, is nonorientable, H1=Z⊕Z/2Z and H2=0. Thus no homeomorphism, orientation reversal of a face coordinate chart or topology-preserving Pachner subdivision yields a Klein bottle. Odd S4 permutations reverse simplex orientation **in the chain representation** but do not automatically construct a topologically nonorientable global surface.

A narrower exhaustive test pairs the tetrahedral shell's four WHOLE triangular faces into two identified pairs, choosing any of 3 pair matchings and 6 vertex bijections for each: `3*6*6=108` assignments. The quotient has two representative triangle faces. For a closed surface every quotient edge must be represented by exactly two triangle sides. Exactly **zero of 108** assignments has this necessary incidence pattern; `audit.py` records all seven exact edge-incidence histograms. This does not rule out cuts, finer subdivisions, independent edge-gluing words, new defect cells or more general gluing operations.

## Theorem B — a real Klein double-triangle Δ-complex from edge gluing

Take a square `A=(0,0), B=(1,0), C=(1,1), D=(0,1)`, triangulated along `AC`, with oriented triangle faces `t0=[ABC]` and `t1=[ACD]`. Identify boundary edges `AB=DC` with common arrow and `AD=CB` with opposite spatial traversal, so one opposite pair is flipped. Let oriented quotient edge generators `h=AB=DC`, `v=AD=CB`, and `x=AC`. All square vertices are identified. The quotient chain groups have ranks `C0=1,C1=3,C2=2`, with `∂1=0` and

```
             t0  t1
  h          +1  -1
  v          -1  -1
  x          -1  +1
```

That is `∂2=[[1,-1],[-1,-1],[-1,1]]`. Its rank over Q is 2; its gcd of all rank-two minors is `gcd(2,0,2)=2`, so Smith nonzero invariant factors are (1,2). Hence `H1(K;Z)=Z⊕Z/2Z`, `H2(K;Z)=0`, and χ=1−3+2=0. The sum of both oriented faces has boundary `(0,-2,0)`; a globally compatible signed fundamental 2-chain does not exist over Z. Modulo two the two columns become identical, giving `rank_{F2}∂2=1` and `dim H2(K;F2)=1`. This is an **EXACT** instance of a nonorientable closed surface; the source of the distinction is the gluing.

For the unflipped/toroidal control, choose `∂2^T=[[1,1,-1],[-1,-1,1]]`. The columns cancel and rank_Q=1, leading to H1=Z² and H2=Z. This is a discriminating twist/no-twist null comparison.

## Theorem C — orientation-monodromy and loop dynamics

The orientation line bundle of the Klein surface has a nontrivial class `w1∈H¹(K;F2)`. On the above quotient edge generators, a consistent representative is `w1(h)=1, w1(v)=0, w1(x)=1`. It obeys `w1∂2=0 mod2`. Transport an **oriented frame sign** ε along a discrete edge path γ by
```
epsilon_out = (-1)^(sum_e w1(e)*n_e mod2) epsilon_in.
```
A loop of type h reverses the transported frame sign, while two traversals restore it. This is a Z2 topological holonomy/readout, not a physical oscillation frequency or a global interior/exterior swap.

For an optional O(2) seam phase test, let `F=diag(1,-1)` be reflection and `R(φ)` a planar rotation. Then `F R(φ) F^-1=R(-φ)=R(φ)^-1`. Thus the Klein fundamental-group relation `a b a^-1 b=1` has a flat O(2) representation with `U_a=F,U_b=R(φ)`. The script checks the exact `φ=π/2` matrix. **OPEN:** the rotation angle φ, source-selected packet seam, and dynamical update/coupling. The Z2 monodromy is a discrete *path response*, not a clock, energy flow, stable defect or physical spin.

A nonorientable surface has no globally consistent choice of local 2D orientation. It has no globally defined “inside versus outside” in the sense of a cooriented embedded hypersurface of 3-space. Therefore the strongest UD metaphor is **frame reversal after seam transport**, not literal swapping between a physical interior and exterior.

## Distinction from UD operators / promotion gates

1. Native single-K4 signed boundary maps have `∂²=0` on their own carrier; `S4` odd permutations affect coordinate orientation but do not create Klein w1 by themselves.
2. The flat Klein orientation cocycle requires an **additional identification/seam topology**. It is not the QPB1 sign connection with nonzero triangular curvature; that source explicitly states that face contraction is not invariant. A flat w1 cannot be silently imported as the same edgewise connection.
3. To evolve UD face states across a seam, define a real chain map or twisted local-system transport `U_e`, its domain/codomain, composition, orientation conventions, physical readout and compatible gluing action. Then test `U_{partial f}=I` on every contractible face away from defects and `U_{gamma}=F` on a chosen noncontractible twist loop. If a face has nonflat curvature, label a distinct defect branch and do not confuse it with topology.
4. Nonorientable topology alone cannot select a coupling, growth rate, retention, mass or energy. Physical promotion=0, independent non-constructor proof review NOT_RUN.

## Reproduction and scope

```bash
python3 experiments/klein-tetra-face-flip-20261103/audit.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_klein.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Expected exact output: `results.json`. Target exposure is explicit: Klein surface was the user's requested comparator, and the optional angle π/2 was chosen as an exact integer-matrix fixture; no physically measured values were fitted.

**Decision:** The direct tetrahedron-to-Klein geometry hypothesis fails under topology-preserving operations and under the exhaustive whole-face gluing scheme. The **orientation-double-cover / twisted seam transport** branch survives as a concrete, independently testable mathematical candidate after an explicit NEW gluing topology is supplied. Next discriminant: construct the smallest tetrahedral patch network admitting an actual flat Klein orientation cocycle, with exact signed incidence, then compare local face transport and global twist holonomy and test which channels couple to physical readouts.
