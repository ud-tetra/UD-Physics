# Moving-pulse sensitivity and nonlinear tube attempt v1.0

**EXACT / CONDITIONAL / NUMERICAL / OPEN.** Base378ecad7c8d8fc96c4d8abf55cd0ca5330ea5adc; [protocol](PROTOCOL.md), [results](RESULTS.md), [tube theorem](TUBE_THEOREM.md), [candidate and receipt](../../candidates/icosahedral-pulsetube/candidate.json). The [parent mechanics](../icosahedral-mountloss/README.md), [joint window](../icosahedral-jointwindow/README.md) and [earlier nonlinear domain proof](../icosahedral-nonlineartube/README.md) keep their original scopes.

## 1. Objects, model and exposure

No constitutive law or engineering budget changes. There are280 configuration coordinates q=(alpha,13 primary positions,150 device coordinates,30 housing positions),560 mechanical phase variables and a separate heat accumulator. The reference geometry is over Q(sqrt5); evolution is real, with internal units ell0,E_*,u=t/t0, all uncalibrated. No modular clock, prime-factor mechanism, native UD generator or physical identification is inferred.

The two exposed property sets are seed10422-0-boundary2 and uniform-b0.05-cf0.0, both atnu=.05. Each has beta=.05; the first is the prior limiting breathing case withc_f=.001 and specified material/transmission/housing scatter, the second is nominal withc_f=0. These two choices do not cover the continuous parameter box ornu interval. Full coefficients are the frozen cases.json at the base revision.

The reference pulse has alpha=.1, primary points at reference/rest, z=zdot=0, housings at their mount midpoints/rest. Additional initial housing energy is E_h<=E_p/40000, where E_p=(1+sum g_i)/200. All180 housing displacement/velocity phase coordinates are retained. Total spatial momentum, angular momentum and housing kinetic energy are retained, including any rigid motion excited by a phase.

## 2. Complete analytic Jacobian

Write the mechanical ODE as q'=v, Mv'=-grad U(q)-D(q)v. With constant positive M,

\[
 Df(q,v)=\begin{pmatrix}0&I\\-M^{-1}K(q,v)&-M^{-1}C(q)\end{pmatrix},
 \quad K=U_{qq}+\partial_q[D(q)v],\quad C=D(q).
\]

K includes a generally nonsymmetric position derivative of damping; it is not simply the instantaneous conservative Hessian. `jacobian.py` builds all reciprocal blocks and all mount/anchor reactions, with no state quotient.

For one central viscous path, let d be the endpoint difference, ell=|d|,n=d/ell,w the relative velocity and c its constant loss coefficient. Its force gradient is c n(n·w), its velocity derivative is c nn^T and its position derivative is exactly

\[
 \frac{c}{\ell}\left[(n\cdot w)I+n w^T-2(n\cdot w)nn^T\right].
\]

The matrix is applied with equal/opposite endpoint blocks. This includes the120 moving housing struts and the equivalent primary friction pairs. Conservative derivatives include transverse geometric prestress, the150 reciprocal device cross blocks, alpha/spoke cross terms and the constant midpoint-mount Hessian. Device damping remains in C.

Verification uses two representations: central finite differences of the original nonlinear ODE at rest and displaced/moving states, plus comparison with the pre-existing equilibrium mass-normalized K,C assembly. Tangent total P,L invariants are monitored along the pulse. These are constructor checks; they are not independent peer review or empirical replication.

## 3. Tangent propagation along the nonlinear pulse

Let ybar(t) be the zero-extra-housing-energy nonlinear pulse. The full180-column initial-space derivative solves

\[
 W'=Df(\bar y(t))W,\qquad W(0)=B.
\]

B has housing displacement entries1/(Omega sqrt(m_h)) and velocity entries1/sqrt(m_h), so B^T diag(K_ref,M)B=I. An initial phase a with||a||_2<=1 has perturbation epsilon Ba,epsilon=sqrt(2E_h). W therefore describes the first derivative of the nonlinear flow at the moving pulse. It differs from an equilibrium propagator.

Let vbar(t)=mean_k(V_k/Vref)-1 and h(t)=D(mean normalized volume)(ybar(t)) W(t). For the reference-plus-first-order signal, the RMS squared is

\[
 R_{\rm first}(a)^2=R_p^2+2\varepsilon c^Ta+\varepsilon^2a^TQa,
 \quad Q=\frac1T\int_0^T h^Th\,dt,
 \quad c=\frac1T\int_0^T h^T\bar v\,dt.
\]

This is a convex energy-ball trust-region problem. The minimizing phase satisfies

\[
 (\varepsilon^2Q+\lambda I)a=-\varepsilon c,
 \quad\lambda\ge0,\quad\|a\|\le1,\quad\lambda(\|a\|-1)=0.
\]

Convexity makes these KKT conditions sufficient: the quadratic difference about a stationary candidate is a nonnegative Q term plus the constraint multiplier term, which is nonnegative on the unit ball. The executed cases have a boundary minimizer. A scalar root finds lambda; phase norm and KKT residual are checked. The Gram is a positive sum of outer products; tiny floating negative eigenvalues are clipped only within the declared numerical tolerance. A stable BLAS norm avoids overflow in the nearzero-multiplier bracket.

The alternative triangle bound R_first>=R_p-epsilon sqrt(lambda_max(Q)) is also recorded. It is more conservative because it ignores the perturbation's correlation with the pulse. No housing-ringdown phase is substituted for the breathing objective.

For a strut at a sampled time, ellhat-epsilon||D ell W|| is its scalar first-order lower envelope. The stronger geometric interpretation uses the linearized relative-position map L_e: ellhat-epsilon||L_e||_2 is a lower bound for the distance in the *affine tangent prediction*. Neither quantity bounds the true finite-amplitude nonlinear flow without its remainder.

## 4. Finite preparations and error checks

The optimized adverse phase, its negative and half its amplitude (quarter housing energy) are run through the original nonlinear ODE for each property set. A zero-extra-housing-energy run separately checks the augmented reference integration. These are seven finite preparations, not a nonlinear optimization over the entire ball. Phases were frozen from the normal tangent campaign before the finer repeat.

The finer campaign reduces tangent tolerances and output spacing. Compare tangent matrices/readout rows at matching times separately from RMS quadrature changes. The primary readout uses actual oriented determinants. Mean-volume residuals of the adverse finite phases are compared with the tangent prediction on the same time grid. Observed quarter-energy residual ratios near1/4 support directional second-order behavior; they do not bound the Hessian uniformly.

## 5. Why a frame-aware readout bound is needed

An ambient primary-position radius also counts global translation and rotation, although they leave all cell volumes unchanged. The first fine-run raw radius makes the conservative determinant-remainder budget fail even before adding a nonlinear flow remainder. That failed sufficient bound is preserved.

The subsequent diagnostic projects the primary tangent positions normal to their instantaneous six-dimensional rigid tangent space. It is the derivative of proper Procrustes alignment to the reference. The mean volume gradient annihilates those rigid directions; the trust-region problem is unchanged. Alignment affects only the readout analysis: the full560-state dynamics, all initial housing phases, momentum and kinetic energy remain in the calculation.

An additional post-exposure finite phase maximizes final raw primary displacement using its leading tangent singular vector. Its raw versus aligned shape motion tests whether the failed ambient bound is charging frame motion to the readout. This is one targeted diagnostic, not a new blind test or a uniform chart bound. The geometric derivative and finite proper-motion invariance are checked separately in `alignment.py`.

## 6. What is still needed for a nonlinear certificate

[TUBE_THEOREM.md](TUBE_THEOREM.md) proves an exact a posteriori implication: a positive full-state norm, validated housing-to-state gain A, reference/initial-defect contribution beta, integrated nonlinear coefficient C and domain radius r with A+beta+Cr²<r certify all phases through T. Projected Green operators and the exact cubic determinant remainder then bound volume. A proper alignment chart can improve the readout radius only after including its nonlinear chart remainder.

The current180-column W supplies only U(t,0)B. It does not supply the full forced Green operator U(t,s), a uniform nonlinear Hessian bound, numerical-reference defect or validated continuous-time extrema. Solver tolerances, energy balance, KKT residuals and finite amplitude scaling are insufficient substitutes. `certificate_audit.json` leaves those slots explicitly unverified. The requested u100 finite-energy-ball conclusion therefore remains **OPEN**.

## 7. Reproduction and selected capture

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/verify.py --out /tmp/pulsetube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/variational.py --out /tmp/pulsetube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/variational.py --out /tmp/pulsetube --which fine
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/adverse_checks.py --out /tmp/pulsetube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/alignment.py --out /tmp/pulsetube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/variational.py --out /tmp/pulsetube --which objective
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/rigid_diagnostic.py --out /tmp/pulsetube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-pulsetube/finalize.py --out /tmp/pulsetube
```

Use one or two CPU workers as available; no LLM delegation occurred. The normal executed source and later diagnostic amendments are captured. Selected output summaries/traces and compact phase/Gram/final-tangent checkpoints are archived; bulky full augmented-response intermediates are reproducible from the captured code and exact coefficient inputs. Their digests are recorded without claiming they were archived. No source input or prior immutable run is modified.

The earlier exact housing-only global geometry theorem and full-pulse initialu1/20 theorem are preserved. Native constitutive/clock selection and physical testing remain OPEN/UNSCORED; mainline promotion0.
