# Tetrahedral charge/field-energy candidate — v1.0

**HYPOTHESIS / EXACT CONDITIONAL.** A concrete noncompact quadratic gauge-field model is added on tetrahedral edge cochains. Its equations, symmetry, conserved charge, energy and coefficient freedom are derived below. The electrical identification and action-unit lift are new premises. The frequency2 subfamily is an explicitly inverse-designed analogue normalization, not an independent prediction of its absolute rate. Physical score **UNSCORED**, promotion **0**.

## 1. Question, baseline and source boundary

Can an explicit S4-invariant electrical energy candidate supply the constitutive factor left open by the [impedance audit](../qpb1-impedance-selection/README.md)? We construct a minimal finite model and test coefficient selection, rather than identify support current with electric current by notation.

Discovery base `bbf7b9ec09a86378f6503c16460771a033e48593`. Retained inputs are the filled tetrahedron's oriented boundary maps and the typed native action-unit definition O10/O15. The [source manifest](SOURCES.json) pins these inputs, current C06/O14/Q282–Q288 status and the preceding audit. No registry status is changed. The uploaded historical ledger/governance bytes still match the read-only imports; the unavailable Genesis PNG was not used.

The conventional baseline is discrete variational electromagnetism: Stern, Tong, Desbrun and Marsden, [arXiv:0707.4470v3](https://arxiv.org/html/0707.4470v3), §§2.1,2.6–2.7,5.2–5.4. That primary work separates constitutive/Hodge maps from incidence identities and relates gauge symmetry to preservation of a Gauss constraint. It supplies mathematical comparison, not evidence for UD. Our finite matrices and hypotheses are independently specified and checked here. This candidate's field observables are also available to ordinary linear gauge/LC models; no uniquely UD experimental discriminator is established.

## 2. Typed carrier and added hypotheses

Let K be one filled tetrahedron, with ascending vertex orientation and lexicographic simplex order. Over R, use B1:R6->R4, B2:R4->R6 and B3:R->R4, with the Euclidean chain/cochain identification. The exact identities are

\[
 B_1B_2=0,\quad B_2B_3=0,\quad
 P_L=\frac14 B_1^TB_1,\quad P_T=\frac14 B_2B_2^T,
 \quad P_L+P_T=I_6.
\]

Both projectors have rank3. L denotes the gradient/longitudinal edge sector; T the cycle/transverse sector. These are not physical spacetime indices. The factors4 follow from the exact tetrahedral matrices, not a fitted constant.

**New model:** canonical configuration a in R6 and momentum p in R6, with canonical one-form p^T da. Define face field b=B2^T a and vertex charge rho=B1 p. They are initially dimensionless. The identification of a as a flux potential and p as electric-displacement flux is a Discovery hypothesis. They are not the original simplex-register amplitudes or the PSR support current.

For positive dimensionless parameters u_L,u_T,v, set

\[
 U=u_LP_L+u_TP_T,\qquad
 \boxed{H=\frac12p^TUp+\frac v2\|B_2^Ta\|^2.}
\]

This energy is nonnegative on the12-dimensional phase space, with only configuration gauge directions flat. At fixed rho, quotienting the three gauge directions and fixing the three corresponding momentum values leaves a6-dimensional radiative phase space with positive quadratic energy above its electrostatic minimum. This is three canonical oscillators, whereas the retained UD active chain carrier is R14; no full-carrier equivalence is asserted.

The family is restricted to homogeneous quadratic, S4-invariant energies, no electric/magnetic mixed term, and invariance under the time reversal `(a(s),p(s))->(-a(-s),p(-s))`. Those are assumptions, not forced native field laws. Compact U(1), matter fields, charge quantization, dissipative media, spatial embedding and a continuum limit are not supplied.

## 3. Symmetry determines a family, not its coefficients

S4 acts on every oriented simplex by its signed permutation representation; a and p carry the same edge action. Bk intertwines the adjacent actions. Hence PL,PT and H are invariant under all24 permutations, including orientation reversals.

A complete finite classification is available here: Reynolds-average each of the21 symmetric6-by-6 matrix basis elements over all24 edge actions. Their span has exact rank2 and is already spanned by PL,PT. Thus **every symmetric S4-invariant electric quadratic form on this edge representation** is u_L PL+u_T PT. Positivity requires u_L,u_T>0. The analogous gauge-invariant configuration form annihilates im(B1^T), leaving one coefficient on PT, written4v PT. Time reversal removes the mixed a,p form.

This proves the stated quadratic-family classification, not uniqueness across nonlinear energies or other carriers. The symmetric edge commutant dimension2 is not the full original UD chain commutant dimension13.

The model remains local on vertex/face incidence neighborhoods:

\[
 \tfrac12p^TUp=
 \tfrac{u_T}{2}\|p\|^2+\tfrac{u_L-u_T}{8}\|B_1p\|^2.
\]

The second expression may have a negative displayed difference coefficient when u_L<u_T, but its projector form is positive. Distinct edge momenta interact only when those edges share a vertex. The **stronger** requirement of completely independent identical edge electric energies forces u_L=u_T; S4 symmetry and incidence locality alone do not.

## 4. Variational dynamics, gauge and charge

At a fixed zero-sum charge profile rho_bar, introduce a vertex multiplier psi and the proposed native-unit action

\[
 S=\mathcal A_0\int
 [p^Ta'-H-\psi^T(B_1p-\bar\rho)]\,ds.
\]

The use of the source symbol A0 as this new field model's action prefactor is an explicit unit-lift premise. Variation gives

\[
 a'=Up+B_1^T\psi,\quad
 p'=-vB_2B_2^Ta,\quad B_1p=\bar\rho.
\]

Therefore rho'=0 and B3^T b=0. In temporal gauge psi=0, H'=0 directly; the same conservation follows in any gauge because its extra power is proportional to B1 p'=0. Gauge transformations are `a->a+B1^T chi`, `psi->psi+chi'`. The action changes only by the endpoint term A0*[chi^T rho_bar] when rho_bar is fixed; endpoint-vanishing transformations preserve it.

Gauge symmetry preserves an imposed Gauss constraint; it does not choose the initial charge or prove an electric interpretation. Since 1^T B1=0, this closed model has zero total vertex charge. A lone added electron requires a compensating charge, boundary flux or reservoir absent from this model. No charged particle production, moving matter source or single-electron preparation is derived.

For zero-sum rho, the minimum-energy momentum is p_L=B1^T rho/4; its electrostatic energy is

\[
 H_C=\frac{u_L}{8}\|\rho\|^2.
\]

Longitudinal configuration drift in temporal gauge is gauge, not a fourth radiative mode. The arbitrary constant-charge sector can be held in the gauge a_L=0 using psi=-u_L rho/4.

## 5. Exact radiative spectrum and addressed port

Set a_T=PT a,p_T=PT p. Then

\[
 a_T'=u_Tp_T,\qquad p_T'=-4v a_T,
 \qquad \nu^2=4u_Tv.
\]

There are exactly three identical positive-frequency modes, `nu=2 sqrt(u_T v)`, on the reduced space. This degeneracy is a symmetry/geometry consequence within this model; absolute frequency and the constitutive ratio remain free.

For an explicit unit cycle use edge order `(01,02,03,12,13,23)` and

\[
 w=(1/2,0,-1/2,1/2,0,1/2),\quad
 \|w\|=1,\quad B_1w=0.
\]

The subspace a=alpha w,p=beta w is invariant and has canonical one-form beta d alpha and

\[
 H_w=\tfrac{u_T}{2}\beta^2+2v\alpha^2.
\]

An external mode drive adds `-f(s) alpha` to the Hamiltonian: beta'=-4v alpha+f, alpha'=u_T beta. The field energy obeys H_w'=f alpha'. The drive is divergence-free because B1w=0; it excites a field mode, not net vertex charge. This is a specified source port, not an autonomous native source law.

## 6. Conditional physical dictionary and impedance

Add a charge unit q0>0 and physical clock t=tau0*s. Define edge flux potential and canonical displacement charge by

\[
 \Phi=(\mathcal A_0/q_0)a,\qquad Q=q_0p,
 \qquad E=(\mathcal A_0/\tau_0)H.
\]

Then Q^T dPhi=A0 p^T da exactly. The electric effort is
`V_edge=(A0/(tau0 q0)) Up`, and equals `Phi_dot-B1^T phi_scalar` with `phi_scalar=(A0/(tau0 q0))psi`. It is not generally Phi_dot outside temporal gauge.

On the addressed transverse mode, Phi_mode=(A0/q0)alpha and Q_mode=q0 beta give

\[
 C_{\rm eff}=\frac{\tau_0q_0^2}{\mathcal A_0u_T},\qquad
 L_{\rm eff}=\frac{\mathcal A_0\tau_0}{4vq_0^2},
\]
\[
 \boxed{\omega=\frac{2\sqrt{u_Tv}}{\tau_0}},\qquad
 \boxed{Z_{\rm mode}=\frac{\mathcal A_0}{q_0^2}
 \underbrace{\frac12\sqrt{u_T/v}}_{\lambda_{\rm mode}}.}
\]

These are reduced oscillator parameters. They are not a fabricated circuit topology, full nonsingular edge inductance matrix or measured material constants. The factor1/2 in lambda comes from the curl eigenvalue4; it is not an identification with hbar. Modal charge Q_mode is a signed weighted projection of displacement fluxes. It is not an electron-count observable, even if its unit is chosen to be q0.

## 7. Frequency matching and native support do not remove the freedom

Matching the retained native frequency2 imposes u_T v=1. Even with the stronger edge-diagonal assumption, the positive family

\[
 u_L=u_T=s,\quad v=1/s,\quad s>0
\]

preserves gauge symmetry, S4, positivity, charge conservation and frequency2, while lambda_mode=s/2 ranges over all positive values. This is a general counterfamily; the six rational cases merely check it.

The native oscillator comparison also exposes the preparation issue. For any mode let lambda=(1/2)sqrt(u_T/v), and define

\[
 X=\alpha/\sqrt\lambda,\quad Y=-\sqrt\lambda\,\beta,
 \quad N=X^2+Y^2=\alpha^2/\lambda+\lambda\beta^2.
\]

Then `(X',Y')=nu*(-Y,X)` when undriven, `H_w=(nu/2)N`, and beta d alpha equals `(X dY-Y dX)/2` up to an exact differential. One positive winding has loop action pi*A0*N. At nu2 these agree with the retained **one-plane** native oscillator formulas under the declared map, not with the entire UD carrier.

The preparation alpha0=0,beta0=1 has N=lambda, not automatically1. If Q_mode=e, then `N=lambda(e/q0)^2` and `A_map=e^2 Z_mode=A0*N`. Setting q0=e does not fix N. Declaring the native unit preparation instead requires beta=1/sqrt(lambda), an additional physical preparation law.

## 8. A dimensionless prediction and its additional hypothesis

Compare two precisely specified initial fields, both with a=0:

- Static vertex dipole rho=(1,-1,0,0), with p=B1^T rho/4: `H_C=u_L/4`.
- Neutral face-cycle excitation p=B2 e_face: three signed unit edge entries, `H_F=3u_T/2`.

Their energy ratio is

\[
 \frac{E_C}{E_F}=\frac{u_L}{6u_T}.
\]

Under **independent equal edge electric terms** u_L=u_T, it is1/6, without selecting u_T,v,A0,q0 or tau0. The denominator6 is `3 edge terms * (1/2)` divided into the dipole's `(1/4)` energy; it is not a fitted physical constant. The preparations have different charge profiles and must be established by the declared canonical map before physical comparison. S4 alone allows the ratio to vary: the exact control u_L=3,u_T=v=1 retains frequency2 and lambda1/2 but gives ratio1/2. Ordinary tetrahedral gauge/circuit models share the conditional1/6 prediction.

## 9. Canonical duality has a scale too

On each neutral transverse mode the canonical exchange

\[
 D_\sigma:(\alpha,\beta)\mapsto(\sigma\beta,-\alpha/\sigma)
\]

is symplectic for every sigma>0. It preserves H_w iff u_T=4v sigma^2. Together with nu2, this yields `u_T=2sigma,v=1/(2sigma),lambda=sigma`. Thus the existence of a duality does not select impedance either. The special unscaled exchange sigma1 gives lambda1 only after its relative coordinate normalization has been chosen. This is mode canonical exchange, not a proof of spacetime electromagnetic duality or a symmetry of arbitrary charged matter sectors.

## 10. Decision, limits and reproduction

**ACTIVE conditional field candidate:** a positive reduced energy, variational evolution, conserved Gauss charge, all24 S4 checks, complete symmetric edge-form classification, explicit modal port and conditional energy ratio are now supplied. **OPEN:** native selection of the added electric/field variables, u_L/u_T, u_T/v, q0, physical action/clock anchors and source preparation. The role as an automatic universal impedance/action selector is unsupported under the present assumptions.

A useful next discriminant is the exact integral cycle/cut lattice and its dual pairing: determine whether an independently justified lattice condition could restrict D_sigma, or whether it merely chooses the missing relative charge/flux units. Any compactness or quantization requirement would be a new hypothesis and must disclose its action normalization. No quantum commutator or hbar value was used here.

Run at the repository root:

```bash
python3 experiments/qpb1-charge-field/audit.py --out /tmp/qpb1-charge-field-output
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The audit constructs the oriented boundaries, verifies24 permutations, computes the complete invariant symmetric-form dimension, and checks10 Hamiltonians,30 rational states,6 fixed-frequency impedance examples,one longitudinal-coefficient counterexample and5 canonical-duality examples. General positive-parameter claims are proved above; finite fixtures are scoped constructor checks, not independent review or experiment.

See [the coefficient/preparation contract](COEFFICIENT_CONTRACT.md), [mathematical receipt](../../sessions/qpb1-charge-field-20261022-a1/mathematical_receipt.json), and [immutable run](../../artifacts/qpb1-charge-field-20261022-a1/exact-001/manifest.json).
