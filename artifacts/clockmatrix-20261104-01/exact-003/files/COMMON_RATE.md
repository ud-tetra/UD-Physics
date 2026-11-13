# Common-rate couplings: classification and reciprocal alternative v0.1

**RESULT — EXACT / CONDITIONAL.** In the source-classified linear tetrahedral family, every active oriented clock mode has the same positive rate factor precisely when g1=g2=g3=r>0. A direct linear interaction cannot also leave independently prepared local clock sectors autonomous for every preparation. A posited nonlinear action-action Hamiltonian evades that obstruction and gives uniform within-clock rates, but its coefficient and physical implementation are not selected by the inspected UD sources.

## 1. Objects and source boundary

Resume integrated base: UD-Physics `e400dfb715262a44b3bbb2e929c7b438028af67e`; research parent `8dbaccece8728927ab52d5aefd058c60e0427516`. Import [local-generator audit v1.0](../qpb1-local-generators/README.md), §§1–4, and historical [ledger Q169/Q170](../../sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md). The attached carrier_definition.md and packet_modulation_layer.md are available in this resume but contain only placeholder text; no constitutive law is imported from them.

C=direct sum C_k(Delta3;R), dimension 15; exact matrices over Q, states over R, ascending simplex orientations, H=I. Let D_k be embedded boundaries, K_k=D_k-D_k^T, A=sum K_k, P_k=-K_k^2/4 and P=sum P_k. The imported classification concerns real linear time-independent S4-equivariant skew generators and gives G=sum g_k K_k. The active state space is im P of dimension 14, excluding the static harmonic vertex mode. Parameter s is dimensionless and continuous; SI time map OPEN. Incidence locality is not a physical causal cone.

## 2. Linear common-clock criterion

K_i K_j=0 for i!=j; the P_k are orthogonal projectors of ranks (6,6,2). On P_k the oriented phase rate is 2g_k. Therefore, for every active initial state and fixed signed phase readout,

    G|im P = r A|im P  iff  g1=g2=g3=r.

Proof: restrict the equality to each nonzero P_k. K_k is invertible there, so (g_k-r)K_k=0 forces g_k=r. The converse follows by summation. Positive r preserves the declared clock orientation. Equal magnitudes |g_k|=r alone permit orientation reversals and are insufficient. A preparation confined to one sector cannot test the other gains.

Source scope: unit incidence fixes g_k=1 in the declared native parameter. Symmetry, locality, skew conservation and weighted-boundary nilpotence admit other gain triples; they do not select a state-dependent common r or an SI conversion. Equality of gains is an additional restriction within this broader family, not a derived physical lapse law.

## 3. Autonomous linear clocks versus interaction

Take two fixed positive-metric clock sectors, whitened to Euclidean coordinates, with skew generators A_L,A_R and independent arbitrary initial states. If a linear skew generator has blocks [[B_L,C],[-C^T,B_R]], requiring the local readouts to obey x_L'=r_L A_L x_L and x_R'=r_R A_R x_R for **all** independent preparations forces

    C=0,  B_L=r_L A_L,  B_R=r_R A_R.

This follows at the initial derivative by varying the other preparation independently. It is a scoped obstruction to exact, preparation-independent autonomous local clocks with a nonzero direct linear mixing block. A coupled collective-mode readout changes the premise.

The same obstruction appears with hidden linear memory initially zero. Write G=[[B,C],[-C^T,E]]. Exact projected evolution x(s)=exp(Bs)x(0) for every x(0), with memory(0)=0, requires second derivatives to agree. Yet (G^2)_xx=B^2-C C^T. Thus C C^T=0, hence C=0 in a positive metric. An indefinite metric, restricted preparation, time-dependent actuation, nonlinear coupling or a weaker approximate/readout contract is outside this theorem. No all-UD or all-physics no-go is claimed.

## 4. Reciprocal nonlinear candidate

**HYPOTHESIS + EXACT CONDITIONAL.** Use two copies x,y in im P, with J=A/2 so J^2=-I on each active copy. All amplitudes, actions, g and F in this model are dimensionless; no physical energy or action unit is assigned. Declare the Poisson tensor diag(J,J) and actions I_L=||x||^2/2, I_R=||y||^2/2. For a C2 Hamiltonian F(I_L,I_R),

    x'=Omega_L Jx, y'=Omega_R Jy,
    Omega_L=partial F/partial I_L, Omega_R=partial F/partial I_R.

Both actions and F are conserved, so their rates remain constant along each orbit. Every active phase plane in one copy shares its Omega. Conversely, on the active copies, a Hamiltonian gradient yielding this separate radial phase evolution must be radial in x and y; connected spheres then imply F depends only on the two actions. A prescribed pair of smooth action-dependent rates admits such an F on a simply connected action domain only when partial_IR Omega_L=partial_IL Omega_R (and conversely by integrating the closed one-form). This is reciprocal consistency, not an arbitrary independent assignment of clock rates.

An economical quartic cross-coupling is

    F=2(I_L+I_R)+g I_L I_R,
    Omega_L=2+g I_R, Omega_R=2+g I_L,
    Omega_L/Omega_R=(2+g I_R)/(2+g I_L).

The polynomial family is restricted here to baseline 2 on each isolated clock, no added self-action terms, and degree at most two in the actions. Under these restrictions the bilinear action product is the only polynomial cross term (up to g and an irrelevant constant). Nonnegative g guarantees positive rates for all nonnegative actions; negative g needs a bounded domain. The model exchanges no action between clocks and produces neither phase locking nor relaxation. It provides mutual state-dependent frequency shifts under a declared Hamiltonian.

If one further demands Omega_L=Omega_R for all independent actions, the radial family reduces to F=f(I_L+I_R)+constant locally on a connected action domain. It then supplies one common global rate rather than differential slowing. Unequal actions in the action-product candidate give different rates, so it is not a universal external-environment clock law.

The radial construction imposes stronger active-sector isotropy than the source's S4 classification. I_L I_R multiplies whole-carrier stock sums; no incidence-local material interaction or field mediator is derived. g, the action/energy units and the independently calibrated time/readout map are OPEN. Nonlinear reciprocity repairs a mathematical coupling obstruction but does not identify relativity, gravity or motion dependence. Measuring g from the same comparison and calling the ratio a prediction would be FIT; any empirical forecast needs independent calibration or a source-selected g.

## 5. Checks and disposition

Run `python3 experiments/clock-matrix-question/common_rate.py`. Exact Fraction arithmetic reconstructs the tetrahedron, checks projector identities and ranks, tests all 64 triples from {-1,0,1,2}^3, verifies an explicit positive-metric memory curvature control, and checks four nonlinear coupling cases. Written proofs establish the general statements; finite cases are constructor controls. No empirical dataset, rational reconstruction or parameter fitting. Independent review NOT_RUN; physical promotion 0.

The next discriminant is a source/implementation question: can an explicit local mediator produce one common within-clock factor while retaining reciprocal balances, and does it select g independently of the measured rate? The direct unit-edge bridge remains a valid negative control; the new radial coupling remains a candidate.
