# Two tetrahedral clocks and a declared bridge v0.1

**EXACT / CONDITIONAL —** One incidence-local bridge leaves two explicitly prepared local clocks at equal frequency 2, while changing other modes. This construction supplies no differential clock-rate law. It exposes preparation-dependent spectral effects instead of a universal rate change. No physical time-dilation claim follows.

## Objects, source and assumptions

Resume base: UD-Physics `08e1aa8e71843c4fa8e5d88842d8dddad41bfa0a`; prior analysis commit `25f856b8527014fe81d7d2d5fc1482a273363186`. Import only the finite incidence evolution convention from [local-generator audit v1.0](../qpb1-local-generators/README.md), §1, and historical [ledger Q169/Q170](../../sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md). Q169 supplies a rule on a specified complex; it does not select the complex, a bridge or its physical weight. The unavailable attached carrier_definition.md is not used.

Choose filled tetrahedra L=[0,1,2,3] and R=[4,5,6,7], joined only by edge [0,4]. This is a declared new carrier, not a derived interaction. Its face counts are (8,13,8,2), so the real chain state has dimension 31. Coefficients of boundary matrices are rational, orientations are ascending, metric H=I, and the retained closed law is z'=Az with A=d-d^T, d^2=0. No sources or spatial boundary loss. Parameter s is continuous and dimensionless; no modulus, physical length or physical time map is supplied.

For a sensitivity family multiply only the bridge boundary column by rational w. Because that bridge belongs to no face, d^2=0 is preserved. The vertex Laplacian bridge conductance is w^2, not w. The physical meaning of changing w remains OPEN. No w is fitted to a clock ratio.

## Independently prepared local phase planes

Let v_L=e_1-e_2 and v_R=e_5-e_6 on the vertex registers, zero elsewhere. Define h_i=A v_i/2. For every w,

    A v_i=2 h_i,   A h_i=-2 v_i,
    ||v_i||^2=||h_i||^2=2,   <v_i,h_i>=0.

The two phase planes are mutually orthogonal and invariant. The bridge coordinate of both h_i is zero. An arbitrary preparation z(0)=q_L v_L+p_L h_L+q_R v_R+p_R h_R therefore has independently selectable amplitudes/phases. Readouts q_i=<v_i,z>/2 and p_i=<h_i,z>/2 obey q_i'=-2p_i, p_i'=2q_i. For nonzero amplitude, phi_i=atan2(p_i,q_i) unwrapped has phi_i'=2. Hence dphi_L/dphi_R=1 and equal native periods pi. These are formal state/readout preparations; no laboratory independence is claimed.

**Proof.** Each v_i has zero amplitude at the bridge endpoint and zero sum within its tetrahedron, so B1 B1^T v_i=4v_i irrespective of w. Boundary nilpotence removes the face component of A^2 v_i, giving A^2v_i=-4v_i. Skewness gives the phase-plane norms and conservation. Disjoint tetrahedral supports and zero bridge components give orthogonality. This proves persistence for all s, beyond a finite replay.

## Coupling does change other modes

The exact vertex-Laplacian characteristic polynomial is

    det(lambda I-L0)=lambda (lambda-4)^5 [lambda^2-(4+2w^2)lambda+2w^2].

Four leaf-difference modes have eigenvalue 4. The remaining subspace is constant separately on each three-leaf group, with distinguished bridge vertices. Its exchange-even quotient has eigenvalues 0,4; the exchange-odd quotient matrix is [[3+2w^2,-3],[-1,1]], giving the remaining quadratic. At w=0 the spectrum is two copies of the isolated tetrahedral vertex spectrum. At w=1 the two affected squared frequencies are 3±sqrt(7), both positive; the associated oscillation frequencies are sqrt(3±sqrt(7)). The protected clocks above still have frequency 2.

Thus one common scalar cannot turn every old active vertex mode into the joined spectrum. The bridge can produce hybridized, readout-dependent normal modes, even when selected clock preparations see no change. Choosing only the slower new mode after inspecting the spectrum would be target-informed mode selection, not a universal clock law.

This is a failure of this minimal bridge as a differential-dilation mechanism; it is not a no-go for all UD couplings. Neither norm conservation nor matrix locality specifies motion, gravitational potential, observer comparison, delay correction or a Lorentzian metric. A new interaction or preparation law must state what changes and which clock species should share its rate.

## Replay, status and next discriminant

Run `python3 experiments/clock-matrix-question/two_clock.py`. Fraction arithmetic checks w=0,1/2,1,2, the full 31-coordinate d^2/skew identities, both clock-plane identities and exact vertex characteristic polynomials. The analytic decomposition proves the family statements. No eigensolver, decimal fit or empirical target is used. Independent review NOT_RUN; physical promotion 0.

Recommended next test: classify allowed inter-carrier couplings that shift all declared active clock modes by one common factor while retaining the specified preparation/readout. Ask whether a source-selected interaction fixes that factor. The present result prevents calling arbitrary spectral slowing a physical dilation mechanism.
