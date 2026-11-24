# Exact active shared-face sector on two glued tetrahedra v0.1

**EXACT / CONDITIONAL / NO-GO_SCOPED. Physical Promotion = 0.**

## Source pins and scope
UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`; `experiments/four-cell-tetrahedron/README.md` v1.0 Git blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e` and `experiments/pachner-boundary-observability/README.md` v0.1 blob `a7aa4a19f4da25ff94783053542c33f9aef188dc`. Related distinct *sixteen-cell* development: draft PR #480 at head `6c40e9e1ea3ee7fc658189146ab82f01ebcc1340`. The present 2-tetra construction is a controlled face-sharing complex, not a sourced gluing/birth event.

## Typed model
Let K be union of [0123] and [0124] glued on the face [012], oriented ascending. The four real chain grades are (5,9,7,2), 23D total; declare unit simplex coefficient metric and the signed integer boundary D, skew generator A=Dᵀ−D and formal parameter s. No physical time, energy, metric or apparatus is identified.

## Exact spectral and interface result
`rank(B1,B2,B3)=(4,5,2)`, `B1 B2 = B2 B3=0`,
`χ_A(z)=z(z²+3)^4(z²+5)^7`. On the two top coordinates `B3ᵀB3=[[4,1],[1,4]]`, eigenvalues 3,5.

Let `v=e_[012]` be the unit *shared interior triangular face*, and `u=Av`. Exact signed incidences give
`u=−e_[01]+e_[02]−e_[12]−e_[0123]−e_[0124]`,
`u⊥v`, `||u||²=5`, `Au=−5v`.
Thus the rank-two orthogonal projector `P=vvᵀ+uuᵀ/5` obeys `P²=P` and `[P,A]=0`. This is an *active* invariant sector, not an all-coordinate freeze.

Starting with `x(0)=v`, exact solution
`x(s)=cos(√5s)v+(sin(√5s)/√5)u`. Total unit coefficient stock remains 1. Partition: shared face `cos²(√5s)`, three shared-face edges `(3/5)sin²(√5s)`, and two adjacent top tetrahedra `(2/5)sin²(√5s)`. All six exterior *triangular faces* remain identically zero.

With initial top amplitude 1 on [0123] and all other states zero, [0124] top amplitude is `(cos(√5s)−cos(√3s))/2=−s²/2+O(s⁴)`; this is reciprocal incidence mixing *after* gluing has been imposed.

All 12 signed simplicial automorphisms of the two-tetra face-glued complex (six S3 shared-vertex relabelings and optional apex swap) preserve A and P.

## Carefully scoped limitations
This sector is local to the shared face-star but its edges [01],[02],[12] are also outer-boundary edges. Therefore the mode is visible to a boundary-edge sensor; it is not a wholly hidden or physically localized defect. A boundary **triangle** detector has zero direct readout of this sector, but not every boundary port does. A fixed 2-plane under a skew generator does not establish an emergent physical particle, persistent protected excitation under arbitrary perturbation, or intrinsic 1→4 event admission.

**OPEN:** native gluing authorization, source-derived persistent invariant under realistic perturbations, nonlinear coupling, changed geometric metrics, the independently reported three-stage 29→85 discharge, unlimited recurrence, physical correspondence. The missing 23-entry spectral catalogue and nuclear/particle bridges remain blocked.

## Reproduction
Local independent-from-source exact SymPy replay `python verify.py` passes 23D incidence, spectrum, invariant projector, all 12 automorphisms, stock allocation and the reciprocal top initial-state Taylor control. The complete local ZIP `UD_FACE_GLUED_INTERFACE_INVARIANT_v0.1.zip` has SHA256 `84d7c3ed6814ba83cb2e94dc6577f5c2d29962414c4bd61570d6a54d03533254`; this GitHub report is a separate typed capture. Local constructor PASS. GitHub fresh-checkout verifier, CI and non-constructor review PENDING. Physical Promotion = 0.
