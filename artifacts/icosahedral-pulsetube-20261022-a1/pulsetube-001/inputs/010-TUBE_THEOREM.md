# Conditional a posteriori nonlinear tube criterion v1.0

This is an exact implication with explicit hypotheses. The current numerical campaign does **not** verify all its hypotheses. It cannot be cited as a closed u100 finite-energy-ball theorem.

## 1. Full state, reference defect and Green operator

Let y'=f(y) be the unchanged560-state mechanical ODE on the positive member/strut length domain D. Heat can be reconstructed by integrating nonnegative loss; it does not feed the mechanical ODE. No spatial rigid coordinates or kinetic energy are discarded.

Choose a piecewise C1 reference path yhat:[0,T]->D. It may be a numerical interpolant: it need not be an exact solution. Its defect is

\[
 d(t)=\widehat y'(t)-f(\widehat y(t)),\qquad
 J(t)=Df(\widehat y(t)),\qquad
 \partial_t U(t,s)=J(t)U(t,s),\quad U(s,s)=I.
\]

The family of norms ||.||_t must be continuous in t, uniformly equivalent on[0,T] to a fixed Euclidean norm, and positive definite on all560 coordinates, with explicitly compatible induced operator norms. A semidefinite stiffness norm that discards rigid velocities is inadmissible here. For a full housing initial phase a in R180, ||a||_2<=1, write

\[
 y(0)-\widehat y(0)=\varepsilon Ba+e_0,
 \qquad \varepsilon=\sqrt{2E_h}.
\]

The injection B has displacement housing block1/(Omega sqrt(m_h)) and velocity block1/sqrt(m_h); it satisfies B^T diag(K_ref,M)B=I. The latter identity normalizes the initial housing energy and is not substituted for the required positive state norm at future times.

Assume, for every t and every ||e||_t<=r, that the segment yhat(t)+theta e,theta in[0,1], lies in D and

\[
 \|f(\widehat y+e)-f(\widehat y)-J(t)e\|_t
 \le\tfrac12 H(t)\|e\|_t^2.
\]

Supply **validated upper bounds**, in these same norms, for

\[
 A\ge\varepsilon\sup_{0\le t\le T}\|U(t,0)B\|_{2\to t},
\]

\[
 \beta\ge\sup_t\left\|U(t,0)e_0-\int_0^tU(t,s)d(s)\,ds\right\|_t,
 \qquad
 C\ge\tfrac12\sup_t\int_0^t\|U(t,s)\|_{s\to t}H(s)\,ds.
\]

These are distinct objects. The computed180-column U(t,0)B does **not** supply the full560-dimensional forced Green operator U(t,s). Numerical local-error tolerances, balance residuals, output quadrature refinements and trajectory samples do **not** supply beta or a uniform H.

## 2. The radii inequality and continuation proof

If a radius r satisfies

\[
 \boxed{A+\beta+Cr^2<r}
\]

and the entire closed r tube remains in D with a positive member/strut length margin, then every initial phase in the allowed ball exists through T and satisfies ||y(t)-yhat(t)||_t<r.

**Proof.** Taylor's formula with integral remainder and variation of constants give, up to the first exit from the tube,

\[
 e(t)=U(t,0)(\varepsilon Ba+e_0)-\int_0^tU(t,s)d(s)\,ds
       +\int_0^tU(t,s)R(s,e(s))\,ds.
\]

The assumed bounds make its norm at most A+beta+Cr²<r. It cannot attain the tube boundary. At t=0 this also gives a strict initial margin. On finite intervals the reference tube is bounded and its positive length margin excludes the singularities of f; the standard local ODE continuation argument extends the solution to T. This reasoning is uniform in a. For C>0, the polynomial has a usable negative interval only if4C(A+beta)<1; a rational trial radius can be checked directly without approximating a quadratic root. If C=0, choose r>A+beta.

The nonlinear flow remainder beyond the first derivative is bounded by

\[
 \sup_t\|e(t)-\varepsilon U(t,0)Ba\|_t\le\beta+Cr^2.
\]

The strict radius condition must be recomputed if the model, parameter set, reference path, norm, initial space or energy budget changes. A failed scalar majorant is a failure of that sufficient certificate, not a dynamical counterexample.

## 3. Primary/output bounds can use projected Green operators

To avoid charging a large housing velocity against a primary volume readout, also bound the primary-position projection Pi_p of the flow remainder:

\[
 r_{p,2}\ge\sup_t\|\Pi_p(e(t)-\varepsilon U(t,0)Ba)\|_2
 \le\beta_p+C_pr^2.
\]

Here beta_p,C_p are defined by the preceding expressions with Pi_p U in place of U. The total primary position difference then has radius

\[
 r_p\ge\varepsilon\sup_t\|\Pi_pU(t,0)B\|_2+r_{p,2}.
\]

For each reference cell matrix Ahat_k, assume sigma_min(Ahat_k)>=s_*>0 and |Vhat_k/Vref|<=v_*. The map from the13 primary point displacements to three hub-relative cell columns has Euclidean operator norm2 (the three-leaf star incidence has largest singular value2). Thus ||Delta A_k||_2<=2r_p. With z=2r_p/s_*, determinant expansion yields the exact volume Taylor remainder bound

\[
 \left|\frac{V_k-\widehat V_k-DV_k(\widehat y)\Pi_pe}{V_{k,\rm ref}}\right|
 \le v_*\left(3z^2+z^3\right).
\]

Indeed det(I+E)=1+trE+sum of three principal2x2 minors+detE. Each minor has magnitude<=||E||_2² and |detE|<=||E||_2³. No linear volume readout is silently substituted for the geometric determinant.

If L_m bounds the norm of the mean normalized volume gradient along yhat, and R_first,min bounds the RMS of the reference-plus-linearized signal for every initial phase, the full nonlinear signal satisfies

\[
 R_{\rm nonlinear}\ge R_{\rm first,min}-L_m r_{p,2}
                        -v_*\left[3(2r_p/s_*)^2+(2r_p/s_*)^3\right].
\]

R_first,min itself must be enclosed, including quadrature and derivative-flow errors. A numerical trust-region minimum alone is insufficient.

### Proper-frame alignment alternative

Raw primary positions include translation and rotation, while the volume is invariant under their finite proper action. A smooth proper Procrustes alignment chart chi_t can align primary coordinates to the reference before evaluating the same determinant. Its derivative at the reference is the orthogonal projection normal to the instantaneous six-dimensional rigid tangent space. Thus the first-order mean-volume row is unchanged, but a smaller aligned shape radius can replace the ambient position radius.

This substitution needs its own remainder bound. For example, if the alignment chart satisfies ||D²chi_t||<=H_chi uniformly on the tube, its deviation from its linear projection contributes at most H_chi r²/2. The aligned-flow remainder must include that term in addition to the appropriately projected forced Green and reference-defect terms. The chart must remain smooth and unique on the tube. Sampled projection singular values alone do not establish any of these properties or bounds.

The full ODE, positive state norm, spatial momentum and all housing kinetic energy remain intact. Removing frame motion from an invariant geometric readout does not authorize deleting its mechanical energy. The initial180-coordinate energy ball is unchanged.

## 4. Strut and orientation domain closure

If the tube bounds each housing-position error by r_H and each primary-point error by r_X, then exactly

\[
 |H_e-X_a|\ge|\widehat H_e-\widehat X_a|-r_H-r_X.
\]

For a raw Euclidean full-state radius r one can conservatively use r_H+r_X<=sqrt2 r. Better block projection bounds are permitted if explicitly verified. The reference minimum must hold continuously, not only at sampled times. Likewise, 2r_p<s_* ensures each cell remains invertible and preserves its initial orientation. This does not by itself establish convexity or global absence of self-intersections.

## 5. Current evidence boundary

The campaign supplies an analytic full-state Jacobian, numerical U(t,0)B at two fixed property sets, numerical readout Grams, finite adverse-phase checks and an exact conditional certificate structure. It does not yet enclose the forced Green operator, a uniform nonlinear remainder over the tube, a reference defect, or continuous-time numerical errors. Therefore the requested finite-energy-ball u100 conclusion remains **OPEN**. The older exact housing-only theorem and full-pulse initialu1/20 theorem retain their scopes.
