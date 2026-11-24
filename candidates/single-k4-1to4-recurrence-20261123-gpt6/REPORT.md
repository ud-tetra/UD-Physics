# K4 recurrence by a single interior 1→4 Pachner move — exact addendum v0.1

**2026-11-23 / EXACT-CONDITIONAL / OPEN constitutive source / Physical Promotion = 0.**

## Source hierarchy (UD-Physics main `ea93a86305925aced4ad9aa43b8bc7979f5b0f15`)
- `experiments/four-cell-tetrahedron/README.md` v1.0, blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`: 1→4 kinematics, recursive f-vectors, relative-chain duality and old/new generator spectra.
- `experiments/pachner-boundary-observability/README.md` v0.1, blob `a7aa4a19f4da25ff94783053542c33f9aef188dc`: fixed-shell boundary response 4→5 with unit radial edges.
- `experiments/pachner-state-transport/README.md` v0.1, blob `0523255744e43cb3849730eb44d5faed5a505077`: exact graded chain transfer, support and native generator mismatch.
- UD #611 at `ed7e860a0912d9480a19707be42771f155d0dee0` concerns a **different** two-packet octahedral overlapping union, not a prerequisite for 1→4.

## Typed geometry
Old `K=[0123]`, vertices `(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)`. Prescribe new interior vertex `4=(0,0,0)` and new 3-simplices `[0124],[0134],[0234],[1234]`. Exterior shell fixed. Old f-vector `(4,6,4,1)`, dimension `15`; new `(5,10,10,4)`, dimension `29`; total Euclidean volume `8/3`, daughter volume `2/3`. All chain grades are oriented ascending simplices over Z/Q; no physical units or clock.

## Exact transport and Whitney distinction
Set `T_k=identity-on-old-simplex` for `k≤2`; the old top tetra maps to the signed sum of four child tetrahedra `T3[0123]=−[1234]+[0234]−[0134]+[0124]`. All three signed chain-map identities `B'_k T_k=T_(k−1) B_k` and 24 signed S4 equivariance identities pass exactly. The **unit coefficient** metric gives `T3ᵀT3=4` and `TᵀT=diag(I14,4)`; this is not norm-isometric for the native full 15D chain amplitudes.

The independent **integrated top-COCHAIN** prolongation for the uniform continuous 3-form is `P3=T3/4`. With Whitney top-cochain H_old=`[1/(8/3)]=[3/8]`, H_new=`diag(1/(2/3))=(3/2)I4`, we get `P3ᵀ H_new P3=3/8` **exactly**. This same-domain cochain statement does not supply a full-chain norm isometry, nor an event trigger.

## Exact dynamical and observability controls
Under inherited unit-metric `A=Bᵀ−B`, old characteristic polynomial `λ(λ²+4)^7`; new `λ(λ²+1)(λ²+5)^13`. Thus the full post-event system has active frequencies `1` and `√5`; topological recurrence does not imply dynamic return or unit generator intertwining.

For a unit-weight edge-incidence boundary port `Λ=L_bb−L_biL_ii^−1L_ib`, old `Λ=4I4−11ᵀ`, new `Λ=(5/4)(4I4−11ᵀ)`. Hence nonconstant boundary eigenvalue `4→5`; constant mode unchanged. After *prescribing* the new connectivity and starting with amplitude 1 on old vertex 0, centre vertex 4 has `c4(0)=0,c4'(0)=0,c4''(0)=1`; this is induced response after insertion, **not** an endogenous birth law.

If every tetra splits at each generation, `N_t(n)=4^n`; `f_n=((4^n+11)/3,(4^(n+1)+14)/3,2·4^n+2,4^n)`. Child tetrahedra are not Euclidean-regular/similar to the parent.

## Governance
**EXACT/CONDITIONAL:** One K4 can topologically recur by 1→4 without coupling or gluing a second source packet; exact shell continuity and uniform Whitney top-cochain norm hold.
**NO-GO_SCOPED:** inherited unit-chain norm is not preserved by the signed integral subdivision transfer; inherited full unit incidence generator differs.
**OPEN:** native source and admissibility of new vertex, vertex position, pre-event trigger, evolving lineage, post-event metric/couplings, full state transfer conservation, physical time and measurement; Physical Promotion=0. An event-count convention does not supply a physical clock.

An independent exact SymPy full-grade replay (constructor) passed locally; local immutable scratch ZIP `UD_SINGLE_PACKET_1TO4_RECURSION_v0.1.zip`, SHA-256 `69f8dd00dbfa998eaf6287092f4f04bf843e3cdd6a6245c2f810b308b5493fe8`. This GitHub report is a separately authored capture; do not claim byte identity. Full repo CI and independent review NOT_RUN.
