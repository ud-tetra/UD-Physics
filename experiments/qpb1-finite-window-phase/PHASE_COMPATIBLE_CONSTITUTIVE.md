# Phase-008 — Constitutive constraints from retained J-phase symmetry

**RESULT — EXACT / CONDITIONAL:** Fully onsite-separable differentiable energy functions invariant under the original continuous J-rotation are restricted to a common quadratic energy, provided all site derivatives vanish at zero and the original connected 15-register incidence graph is retained. A hidden-sector star quartic preserves J and signed S4 but is an additional HYPOTHESIS, and its coefficient is not independently selected. A matched conventional Hamiltonian is dynamically equivalent: physical attribution FAILED.

## Versioned inputs and typed conventions

Integrated source: experiments/qpb1-local-generators/README.md at revision 41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb (matrix A, projectors, full signed S4, and coefficient freedom). Direct predecessor: experiments/qpb1-finite-window-phase/CONSTITUTIVE_SOURCE_AUDIT.md at revision 5e5f64a5bb4f84f3ab5ec6ae627f6d5d300c2381. Inspected read-only sources at integrated revision 4aaf0a39d24328e27bc425e333e3612baea888a5: experiments/qpb1-unit-preparation/README.md, experiments/qpb1-source-reservoir/README.md, experiments/qpb1-charge-field/README.md and experiments/qpb1-impedance-selection/README.md. Their scope does not select a physical nonlinearity or the quartic coefficient used here. This is a bounded source review, not an absence theorem for unread UD records.

The carrier is R^15 of oriented simplex chains, with ranks (4,6,4,1), ascending face signs, positive Euclidean metric, K_k=D_k-D_k^T, A=sum K_k, J=A/2, P_k=-K_k²/4. Original J²=-(P1+P2+P3). Native time s has no physical calibration. Exact matrices and coefficients use Q; the analytic no-go concerns C1 functions on real states. No map from a simplex coordinate to a physical field/port is given.

## Exact onsite no-go

Suppose H_on(x)=sum_i h_i(x_i), every h_i is C1 with h_i'(0)=0, and H_on(exp(theta J)x)=H_on(x) for all real theta,x. Differentiating at theta=0 gives sum_i h_i'(x_i)(Jx)_i=0.

For any adjacent simplex pair i,j with J_ij nonzero, choose x=u e_i+v e_j. All other h'_k(0)=0, leaving J_ij[h'_i(u)v-h'_j(v)u]=0 for every real u,v. For nonzero u,v, h'_i(u)/u=h'_j(v)/v must be the same constant. The Hasse adjacency graph of all 15 simplex registers is connected; hence the constant c is shared by every site and every nonzero argument. Continuity and integration yield exactly

H_on(x)=c ||x||² / 2 + constant.

Thus no genuine onsite-separable nonlinear potential survives this *energy-invariance* condition. This does not classify all vector fields commuting with J, nor coupled energies, nonzero-gradient offsets, non-smooth laws, dissipative sources, alternative metrics or enlarged carriers. It is not a statement about physical locality.

## Minimal J-compatible star-coupled alternative

Let r3(x)=||P3 x||². Explicit new constitutive HYPOTHESIS:

H_lambda(x)=||x||²/2 + lambda*r3(x)²/4,
x'=A grad H_lambda=Ax+lambda*r3 K3x.

For lambda>=0 the added energy is positive; the Poisson tensor A is constant skew. Since P3 commutes with A,J and the signed S4 representation, r1,r2,r3, total norm and H_lambda are conserved, and the flow is J-equivariant. For each fixed preparation, the active angular rates are

omega1=omega2=2; omega3=2(1+lambda*r3).

The hidden projector acts on top cell and alternating four-face plane; its face-to-face block has six off-diagonal couplings. Although the instantaneous K3 operator has incidence support, r3 depends jointly on that star's coordinates. It is not independent onsite energy or a purely endpoint-pair constitutive law.

For previously exposed r3=1/2, imposing the previously exposed gain g3=3/2 demands lambda=1. This is **FIT by target backsolving** and may not be called a source prediction. More general invariant energies F(r1,r2,r3) retain adjustable coefficients, so symmetry neither fixes this functional form nor lambda. lambda=0 returns the native unweighted source. This alternative repairs phase equivariance broken in phase-007, but it does **not** inherit older linear independent-gain robustness bounds, since preparation uncertainty now affects r3 and hence g3.

## Strongest conventional baseline, limitations and discriminant

A conventional nonlinear Hamiltonian using exactly the same Poisson A and scalar H_lambda has identical trajectories, ports and conservation laws for every initial state. Even observing omega3 varying linearly with r3 would support only the stipulated constitutive family against a fixed linear baseline; it would not uniquely identify UD.

An independently specified lambda, measured state-population scale, time map and physically fixed port map are missing. No empirical dataset, physical preparation, photon reference or outside mathematical review was supplied. Candidate is EXACT/CONDITIONAL mathematics, FIT/HYPOTHESIS constitutive interpretation and FAILED unique attribution. Do not promote to mainline or reinterpret historical source status.

## Reproduction

Run: python3 experiments/qpb1-finite-window-phase/sector_law_audit.py --out /tmp/ud-qpb-phase008.json

The standard-library Q arithmetic constructor checks connected 15-register adjacency, hidden rank2 and six face-pair couplings, 24 signed S4 actions, 72 rational state fixtures, 288 J-rotation identities, and exact sector/norm/energy rate balances. The full onsite assertion is the preceding general C1 proof, not an inference from fixtures. Immutable [phase-008 run](../../artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-008/manifest.json) preserves executable input/output SHA-256 bytes; phase-001 through phase-007 runs remain unchanged.

**NEXT (priority 99/100):** obtain an independently versioned source law selecting the functional form and lambda, or park unique UD attribution in this phase-compatible 15D family. A held-out preparation-rate test must include a parameter-budgeted conventional nonlinear control and cannot recycle the exposed g3=3/2 anchor.
