# Prepared-plane local clock interaction v0.1

**RESULT — EXACT / CONDITIONAL.** A nearest-incidence quartic can preserve the specified two-dimensional clock plane and produce a nonzero action-dependent rate with zero transverse leakage on that plane. A positive 13-monomial construction is given below. Full signed S4 invariance prevents this nonzero pure rate law on this particular plane; the construction is deliberately anisotropic. A single coefficient error produces explicit transverse leakage. No native plane/interaction selection or physical clock law is established.

## 1. Sources, state and changed premise

Integrated source `ud-tetra/UD-Physics@698d6d66147131d43e364a1736ca07ad0f3fa9d4`; research parent `d58e99b268fdc5a54e366abb9d874a0f637e8cad`. Resume session `clockmatrix-20261104-01`, held task claim `72863501bd80db6aae1fd9b68467de48e92cb42c`. Main changes since the preceding calculation only close G05/G06 claims; operator/clock sources are unchanged. Retain [local-generator v1.0](../qpb1-local-generators/README.md) §§1–4; [all-preparation quartic v0.1](LOCAL_QUARTIC.md) §§1–6 and [common-rate v0.1](COMMON_RATE.md) §§1–4. Historical supplied ledger v0.39(2) Q166/Q169/Q170 supplies incidence generators/currents, not a quartic coefficient or plane selector. The prior no-go remains intact: this branch changes the preparation domain to one specified plane and allows anisotropic interactions.

Work over Q for exact matrices and polynomial coefficients, R for states and evolution. Single filled tetrahedron, degree-ordered ascending simplex basis, C=R^15, Hmetric=I. Set A=d-d^T, J=A/2, V=h0-perp where h0 has entries1/2 on vertices and0 otherwise; dim V=14. Fixed continuous dimensionless parameter s, no external drive or boundary flux. Poisson evolution x'=J grad H(x), H=||x||^2+lambda Q(x). No physical time/action/energy maps supplied. Define

    v=e_vertex1-e_vertex2, h=Jv,
    ||v||^2=||h||^2=2, v^T h=0,
    Jv=h, Jh=-v, W=span(v,h), x=qv+ph.

Only the edge entries of h are nonzero:

| Edge register | 01 | 02 | 03 | 12 | 13 | 23 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| h component | -1/2 | 1/2 | 0 | 1 | 1/2 | -1/2 |

On W the formal quadratic stock is I=||x||^2/2=q^2+p^2. Readouts q=v^T x/2,p=h^T x/2, signed phase theta=atan2(p,q), unwrapped for rate comparison. The plane and interaction coefficients are question-informed inverse choices, not source-selected preparations. lambda is free.

## 2. Explicit nearest-incidence positive quartic

Write vertex amplitudes as u_i and edge amplitudes as z_ij. All unlisted monomials have zero coefficient. Choose

    Q=(u_1^4+u_2^4+z_12^4)/4
      +z_01^4+z_02^4+z_13^4+z_23^4
      +(u_1^2(z_01^2+z_13^2)+u_2^2(z_02^2+z_23^2))/2
      +z_12^2(u_1^2+u_2^2)/4.

Every mixed monomial uses a vertex and an incident edge; all coefficients are positive and Q>=0. This is a 13-term witness, not a minimal-support proof. For lambda>=0, H>=||x||^2, so every fixed-energy trajectory is bounded and the polynomial dynamics is globally defined in s. This guarantees existence/boundedness, not orbital stability of W. Negative lambda reverses the shift but loses this global coercivity; a bounded-domain or stabilizing hypothesis is then required.

## 3. Exact invariance and clock rate

Substitute u_1=q,u_2=-q and z=p h_edge. Direct differentiation gives

    grad Q(qv+ph)=(q^2+p^2)(qv+ph)=I x.

All other gradient components vanish. Thus, for every q,p, not just grid samples,

    x'=(2+lambda I)Jx,
    q'=-(2+lambda I)p, p'=(2+lambda I)q,
    I'=0, theta'=Omega=2+lambda I.

Q|W=I^2/2 and H|W=2I+lambda I^2/2. For I>0 and Omega>0 the native period is 2pi/Omega. The coefficient identity is cubic, so verifying all coefficients proves the all-plane identity. The nonlinear shift is ordinary amplitude-dependent conservative oscillator behavior within this declared model. It does not supply a universal time-dilation effect. At I=0 no clock phase is defined.

The nearest-incidence coefficient space has99 monomials, including odd pair powers; the even-power subfamily has15+28=43. Requiring J grad Q|W=I Jx gives60 exact cubic coefficient equations (15 output registers x4 monomials q^3,q^2p,qp^2,p^3). In the even family the constraint rank is13 and the affine unit-shift solution dimension30; in the full family the rank is30 and affine solution dimension69. These homogeneous quartic free directions have zero Hamiltonian vector field and zero quartic value on W, but can change the off-plane dynamics. Allowing arbitrary lambda adds one further dimension. The displayed witness sets elimination free coordinates to zero; positivity and sparsity were then checked, not imposed by a physical source.

## 4. Full signed tetrahedral symmetry obstruction

**NO-GO — EXACT / CONDITIONAL.** Within the same unary/nearest-incidence quartic family, full signed S4 invariance is incompatible with a nonzero pure rate shift lambda I on this particular W.

At q=0,x=p h, only edge amplitudes are nonzero. All edges have the same pure-fourth-power coefficient beta under signed S4 (fourth powers remove orientation signs and S4 is transitive on edges). No nearest-incidence mixed term contributes to an edge gradient here: its neighboring vertex/face amplitude is zero. Therefore

    (grad Q)_edge e=4 beta p^3 h_e^3.

The required vector-field identity implies P grad Q=I x, for unit shift, or lambda I x for arbitrary shift, where P projects onto V. P leaves edge coordinates unchanged. It would require 4 beta h_e^2=lambda on every nonzero edge component. But h_12^2=1 while h_01^2=1/4. Hence 4beta=lambda and beta=lambda, forcing beta=lambda=0. Odd pair terms cannot evade this argument. This proves the symmetry obstruction without relying on the solver.

The code independently forms the signed S4 Reynolds projection of all99 monomials. Its ambient invariant energy dimension is13; its plane-constraint image has rank6, and the target is outside that image. It verifies the orientation signs for each transformed simplex by inversion parity. This is a second constructor corroboration of the proof, not nonconstructor review. A different plane, a source-selected broken-symmetry state or a dynamically adaptive interaction changes the assumptions.

## 5. Leakage and finite-time preparation control

For the exact coefficients, W is invariant and transverse leakage is identically zero. This is a statement about exact preparation and exact coefficients, not robustness to errors.

Let P_W=(vv^T+hh^T)/2. Add one allowed local coefficient error

    delta H=epsilon u_1^2 z_01^2.

At q=p=1, the exact instantaneous transverse derivative satisfies

    ||(I-P_W)delta x'||^2=(15/16)epsilon^2.

The code evaluates the ambient gradient and projection directly. Thus a perturbed trajectory starting on W has squared distance to W

    distance(x(s),W)^2=(15/16)epsilon^2 s^2+O(s^3)

at that initial point, for fixed epsilon. This establishes coefficient sensitivity, not instability under every possible perturbation. At q=p=a the displayed derivative norm-squared scales as a^6. The proof uses only the initial derivative; it does not assert a global extrapolation.

For initial-state error with the exact lambda>=0 Hamiltonian, a conservative finite-time bound is available. The displayed Q has pure-power coefficient sum19/4 and mixed-power sum5/2. On ||x||<=R, termwise Hessian bounds give

    ||Hess Q|| <= [12*(19/4)+6*(5/2)]R^2=72R^2.

For the mixed term b x_i^2 x_j^2 one can use the tighter4bR^2 bound, so6bR^2 is safe. Since ||J||=1 on V, F=J grad H is Lipschitz on that ball with L<=2+72lambda R^2. Compare a perturbed initial state x0 in V with z0=P_W x0. Choose R^2=max(H(x0),H(z0)); conservation and H>=||x||^2 bound both complete trajectories in that ball. Gronwall then gives

    distance(x(s),W) <= ||x(s)-z(s)|| <= exp[(2+72lambda R^2)|s|] ||x0-z0||.

For an allowed distance tolerance delta on |s|<=T, the sufficient initialization tolerance is delta*exp[-(2+72lambda R^2)T]. This coarse analytic guarantee does not establish transverse Floquet stability or an experimentally useful tolerance. The periodic transverse variational problem remains OPEN.

## 6. Disposition and next discriminant

**EXACT conditional construction:** a local anisotropic Hamiltonian supports one prepared amplitude-dependent clock with zero exact leakage. **EXACT scoped no-go:** full signed S4 symmetry blocks the same law on the selected plane. The previous all-active-state nearest-incidence no-go remains PARKED with its original reopening conditions; this new restricted-plane branch is ACTIVE, candidate only.

**OPEN_GATED:** native plane preparation, anisotropic contact/coefficient selection, lambda, transverse stability and error budget, physical stock/time/readout maps, an independent comparison and independent review. A selected local oscillator is not a physical identification. No empirical dataset or fit, no mainline registry promotion; physical promotion0.

Next: derive the transverse periodic linearization about W, classify stable/unstable perturbations as a function of lambda I, and quantify a finite observation interval for the phase readout. Selection of W and its interaction must remain explicit even if stability passes.

## 7. Reproduction

Run `python3 experiments/clock-matrix-question/prepared_plane.py`. Standard-library Fraction arithmetic reconstructs the tetrahedron and solves both complete cubic coefficient systems, checks signed S4 projection and infeasibility, evaluates the explicit ambient gradient on25 rational plane points and computes the coefficient-error leakage15/16 exactly. Written gradient/symmetry arguments establish the universal statements. Code, results and receipt are preserved under exact-006. No imported program is executed. Independent review NOT_RUN.
