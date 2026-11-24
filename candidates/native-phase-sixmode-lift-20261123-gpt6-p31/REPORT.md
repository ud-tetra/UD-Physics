# Signed-S4 six-mode native-phase lift to octahedral daughter top cells — v0.1

**EXACT / CONDITIONAL; NO-GO_SCOPED locality; OPEN constitutive source. Physical Promotion = 0.**

## Provenance
1. UD-Physics draft PR #473 head `361aa2df2cc510e90a9b6e39825e63656127cdb0`, `sessions/20261123-explorer-whitney-7d2a/TWO_SHEET_v0.2.md`, blob `517ce03ea3635fbd34e43062c399c54cdf9e3e8e`: two separate source-tagged Whitney sheets, each containing 8 shared core tetra of volume 1/6 and 4 private cells of volume 1/3, with metric H=diag(6I8,3I4); candidate scalar exchange only.
2. UD-Physics integrated main `ea93a86305925aced4ad9aa43b8bc7979f5b0f15`, `candidates/aw5-gap4-native-holonomy/AW5_STRUCTURAL_EXCLUSIVITY_AND_GAP4_DRAFT.md` §2, blob `5c088ce09f6aaf02217c3dc84af808e38bff7da1`: exact filled K4 native phase on 6D edge-cycle/face sector. Signed simplex permutation representation.
3. UD draft PR #611 head `ed7e860a0912d9480a19707be42771f155d0dee0`, report §§2–5: canonical octahedral fan is externally prescribed; 117D incidence generator fails inherited 30→117 transfer intertwining.

## Typed objects
Native `C(K4;R)=R15`, graded dimensions (4,6,4,1), lex oriented simplices, metric I15; signed S4 action R(g); boundary ∂ and generator A=∂ᵀ−∂; J=A/2. Define outward face chains `F_i=(-1)^i[0123\\{i}]`, `z_i=∂F_i∈C1`, `y_i=Jz_i∈C2`. Let Z,Y be 15×4 matrices. `Q=I4−11ᵀ/4`, then `ZᵀZ=YᵀY=4Q`, `ZᵀY=0`, `JZ=Y`, `JY=−Z`; native W=im(Z)⊕im(Y) has dimension 6 and `P_W=(ZZᵀ+YYᵀ)/4`.

Target daughter top cochains `R12` (not old chain amplitudes): core positive octant orbit four, core negative octant orbit four, four private caps, metric `H=diag(6I8,3I4)`. The two four-orbit pairing is prescribed by the supplied Euclidean octahedral geometry and is NOT a native pre-event contact selector.

## Exact algebra
Let `α=√(2/3)` fixed by Whitney metric, and define `Φ=(α/4)[Zᵀ;Yᵀ;0_(4×15)] : R15→R12`. Define daughter phases:
- strictly matched-cell local `J_local=[[0,−I4,0],[I4,0,0],[0,0,0]]` (rank 8);
- native-supported `J_W=[[0,−Q,0],[Q,0,0],[0,0,0]]` (rank 6).

Exact symbolic checks:
`ΦᵀHΦ=P_W`, `Φ J = J_local Φ = J_W Φ`; all 24 signed S4 permutations satisfy `R_d(g)Φ=ΦR(g)`, with `R_d(g)=diag(sgn(g)P_g,sgn(g)P_g,sgn(g)P_g)`. Both J operators are H-skew; `rank(J_local−J_W)=2`. The 2 extra modes are uniform octant-orbit combinations: `J_W` annihilates them. No new daughter coordinates are needed to realize *six-mode* phase.

For two independently tagged sheets, define `B=[[0,J_W],[J_W,0]]` and `H2=diag(H,H)`. Then `BᵀH2+H2B=0`, `SBS=B` for ordinary sheet swap S, and rank(B)=12. These are conditional after the geometry and two-sheet carrier are supplied.

## NO-GO and missing source
- **NO-GO_SCOPED locality:** If a phase operator must mix only individually matched core-cell pairs with the same nonzero local coefficient, S4 symmetry forces a rank-8 action; it cannot act only on the six-dimensional native W image. `J_W` subtracts 4-cell means via Q and therefore mixes amplitudes across a core orbit (not strictly diagonal in the cell basis).
- **NO-GO_SCOPED activation:** The pure native tetrahedron top-grade state `e_top∈C3` satisfies `Φe_top=0`. Thus this native phase lift does not by itself activate the initially uniform top Whitney excitation used in PR #473. An independent source-derived grade-mixing/preparation operator would be needed.
- **OPEN:** pre-event face-flag selection and two-carrier connection, full 117D generator compatibility, post-event complement dynamics, native phase transport of top stock, contact selection, clock, physical measurement. The underlying geometric orbit pairing is prescribed, not native. Rotated contact not tested.
- **Verification:** local `python verify.py` exact SymPy replay passed. Repository CI and independent non-constructor review NOT_RUN. No frozen claims altered; Physical Promotion = 0.

**Local immutable scratch package** `UD_NATIVE_PHASE_SIX_MODE_LIFT_v0.1.zip`, SHA-256 `d232c8ae42c1987dad1335be21e809119c4b6f332fe79c67f4069131c3ece071`. This GitHub capture is a parallel versioned text publication, not byte-identical to that local ZIP.
