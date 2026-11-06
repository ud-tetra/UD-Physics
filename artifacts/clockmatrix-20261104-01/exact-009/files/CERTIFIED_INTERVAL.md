# Explicit local-clock stability interval and readout contract v0.1

**RESULT — EXACT / CONDITIONAL.** For the fixed eta=1 modified Hamiltonian from [LOCAL_STABILIZATION.md](LOCAL_STABILIZATION.md), every coupling `0<mu=lambda I<=2^-30` has bounded linear transverse motion with Euclidean gain at most64 for all native times, for the declared reference phase origin. A separate nonlinear finite observation contract controls phase error below1/1000 rad. This is a conservative analytic certificate, not a maximal stability interval or physical calibration.

## 1. Source and typed contract

Calculation base `ud-tetra/UD-Physics@fdab9d0c5f3f5a629ad00cd6fbaa4a52bbaccddc`; research parent `b04d720d96b1c51842d51066a206e2afa92b1f33`. Same session `clockmatrix-20261104-01`, task `clock-matrix-question-20261104`, held claim `72863501bd80db6aae1fd9b68467de48e92cb42c`. Dependencies: [local stabilization v0.1](LOCAL_STABILIZATION.md) §§1–7 and [transverse-stability v0.1](TRANSVERSE_STABILITY.md) §§1–5. The signed simplex/metric/generator source remains [local-generator v1.0](../qpb1-local-generators/README.md) §§1–4. Historical ledger Q166/Q169/Q170 supplies native incidence dynamics, not the selected quartic, plane or coupling. The source transport/G06 audit preserves physical calibration as OPEN.

C=R^15, ascending simplex basis, unit positive metric, J=A/2. V=h0-perp has dimension14; prepared W=span(v,Jv), v=e_vertex1-e_vertex2 with norm-squared2. Normal N=V intersect W-perp has dimension12, orthogonal projector P. The chosen Hamiltonian is H=||x||^2+lambda(Q+R), eta=1 fixed, lambda>=0. Reference x*(s)=sqrt(I)[v cos(theta)+h sin(theta)], h=Jv, theta=(2+mu)s, mu=lambda I. Initial reference phase theta=0. The stock I=||x*||^2/2 is dimensionless, distinct from O09 lifted-history action. All times below are the continuous native parameter s; physical units/readout calibration are absent.

The linear transverse theorem concerns the variational equation on N. The finite nonlinear theorem concerns actual trajectories in V near the specified reference and uses energy/error gates. Neither asserts nonlinear all-time orbital stability, attraction to W, a selected physical clock or relativity.

## 2. Exact averaged metric and resolvent bounds

Let T be the eta=1 averaged normal generator, extended by zero to the three excluded tangent/harmonic coordinates. Its squared frequencies are a=19/256, b=35/64, c=3/64 with real multiplicities2,4,6. Let K=-JT. The b group has negative K signature and the other groups positive, as previously certified by rational LDL pivots.

Construct the real negative-group projector

    Pi_-=(T^2+aP)(T^2+cP)P / [(a-b)(c-b)],
    R0=P-2Pi_-,
    G0=K R0+(Id-P).

The exact code verifies projector identities, commutation, G0 symmetry, and T^T G0+G0 T=0. It also proves

    (1/64)Id < G0 < 4Id

by strict positivity of the15 exact LDL pivots of each shifted matrix. These include the excluded coordinates via Id-P. Thus T is skew in a positive metric and its Euclidean similarity condition is at most16. Consequently its complex resolvent satisfies

    ||(zId-T)^-1|| <=16 / distance(z,spec T).

On N, R0 is a G0-isometry, so ||R0||<=16. Exact absolute row sums also give ||K||<=29/16<2.

For spectral separation, use circles of radius r=1/8 centered at +-i sqrt(b). The inequalities sqrt(b) in(7/10,3/4), sqrt(a)<3/10 and sqrt(c)<1/4 show every point on those circles is at least r from the spectrum of T; the zero ambient modes are also outside. Each circle selects its signed frequency group and together they select the four-dimensional real negative-signature group. No floating spectral gap estimate is used.

## 3. Full return-map remainder, beyond leading averaging

Set rho=mu/(2+mu). In phase coordinates the transverse equation is

    d xi/dtheta=J_N[Id+rho(B(theta)-Id)]xi.

For this modified quartic, ||B(theta)||<=4 on the unit-action orbit. This follows from the explicit symmetric Hessian row sums: active vertex rows are at most4(cos^2+sin^2), active edge rows at most4, and the added inactive diagonal entries at most1. For example, the vertex inequality follows from u^2+3v^2-3|uv|=(|u|-3|v|/2)^2+3v^2/4>=0. Therefore ||B-Id||<=5.

In the interaction picture exp(-J_N theta), write M_rho=-U_rho(pi). Its Dyson series has coefficient norm bound5rho and first-order integral pi rho T. For alpha=5pi rho<=1/8,

    ||M_rho-Id||<=exp(alpha)-1<=2alpha<=1/4,
    ||M_rho-Id-pi rho T||<=alpha^2,
    ||log(M_rho)-(M_rho-Id)||<=3alpha^2.

The last inequality uses the convergent matrix-log series and its norm-majorizing scalar series. Define L_rho=log(M_rho)/(pi rho), with removable value L_0=T. Then

    ||L_rho-T||<=100pi rho<400rho=:e.

The real logarithm exists in this neighborhood. M_rho is symplectic on N, so L_rho is Hamiltonian and K_rho=-J_N L_rho is symmetric. This is a bound on the actual return map, not a truncated averaging result or a numerical integrator estimate.

## 4. Quantitative invariant metric and explicit coupling interval

The resolvent identity and Neumann series on the two circles above give the perturbed real projector Pi_-(rho), with the same total rank4 and

    delta=||Pi_-(rho)-Pi_-||
         <=4096e/(1-128e)<=8192e, provided128e<1/2.

This coefficient includes both contours: each contributes r(16/r)^2 e/(1-16e/r). Both projectors act on N and vanish on its excluded complement.

Define

    G_rho=K_rho[P-2Pi_-(rho)]+(Id-P).

The signed-pair projector is K_rho-self-adjoint: Pi_-^T K_rho=K_rho Pi_-. This follows by transposing the resolvent identity L_rho^T K_rho=-K_rho L_rho and using the union of the two sign-symmetric contours. The projector also commutes with L_rho. Hence G_rho is symmetric and L_rho^T G_rho+G_rho L_rho=0. These statements hold before assuming the perturbed spectrum is imaginary, so the proof does not use its conclusion as a premise.

Using ||K||<2 and ||R0||<=16,

    ||G_rho-G0||<=e(16+2delta)+4delta <33000e

whenever delta<1 and delta<=8192e. For

    0<mu<=2^-30, rho<=2^-31, e<=400/2^31,

all required scalar hypotheses hold and exact rational arithmetic gives

    33000e <=103125/16777216 <1/128.

Thus

    (1/128)Id <G_rho<5Id.

It follows that the half-return is a G_rho-isometry and its integer powers, positive or negative, have Euclidean gain less than sqrt(640)<32. Within any one half-period, the interaction-picture estimate gives gain <=exp(5pi rho)<2. Periodicity therefore yields the explicit all-native-time normal bound

    ||xi_N(s)||<=64||xi_N(0)||, for all real s,
    0<lambda I<=1/1073741824.

This theorem is for the reference phase origin theta(0)=0. Other origins require the corresponding conjugation/gain accounting. Mu=0 is separately neutral with gain1. The interval is deliberately conservative; it is not evidence that stability ends at2^-30. The much larger sampled points in the preceding report remain numerical findings, including the instability at mu=8.

## 5. Nonlinear finite observation contract for the modified model

The all-time bound above applies to the linear normal equation. To control actual readout errors, use a separate nonlinear estimate with this modified Hamiltonian.

For lambda>=0, H>=||x||^2 and H is conserved. Globally

    ||Hess(Q+R)(x)||<=18||x||^2.

The old Q has bound13||x||^2. Each active edge gains a penalty row bounded by(14/3)||x||^2, while the new inactive rows have bounds at most4||x||^2. The other old rows are smaller; thus the combined largest absolute row sum is less than18||x||^2. Symmetric row sums bound the spectral norm. This derives the modified model's bound rather than importing the old Q's finite-window theorem.

For trajectories x,z with both initial energies <=Ecap, the skew linear term2J(x-z) cancels in the norm derivative, giving

    ||x(s)-z(s)||<=exp(18lambda Ecap |s|)||x(0)-z(0)||.

Use these exact gates:

| Item | Required value or bound |
| --- | --- |
| Reference | I=1, q(0)=1,p(0)=0 |
| Coupling | lambda=mu, 0<mu<=2^-30 |
| Actual initial state | x0 in V, ||x0-z0||<=1/4096 |
| Energy | H(x0)<=33/16; H(z0)=2+mu/2<33/16 |
| Observation horizon | T=1/(128mu), native parameter units |

Then18lambda Ecap T<=297/1024<1/3, and exp(297/1024)<3/2 using exp(t)<1/(1-t) for0<t<1. Uniformly on0<=s<=T,

    ||x(s)-z(s)||<3/8192.

Read out q=v^T x/2,p=h^T x/2 with a continuous phase lift. Their error norm is <=||x-z||/sqrt(2), and the reference radius is1. The inequalities1/sqrt(2)<3/4 and sin(1/1000)>1/1000-(1/1000)^3/6 certify

    |theta_x(s)-theta_z(s)|<1/1000 rad.

No phase-zero crossing occurs under this error bound. At T the candidate reference differs from the lambda=0 reference by mu T=1/128 rad, greater than twice the1/1000-rad tolerance. This is an internal model/null comparison under chosen coefficients, not an observed signal or native physical prediction.

The horizon becomes long in native cycles as mu decreases; the certificate supplies no wall-clock feasibility because physical time calibration is absent. Nonlinear all-time orbital stability and robustness to coefficient noise or detector noise are OPEN. The finite gates include only the state-preparation/energy errors stated above.

## 6. Verification, limits and next step

Run `python3 experiments/clock-matrix-question/certified_interval.py`. Standard-library Fraction arithmetic constructs the exact projectors/metric, verifies both shifted-metric LDL certificates and the invariant identity, and checks every rational scalar margin and nonlinear readout inequality. It imports this task's own `stabilization_exact.py` matrix helpers, captured as an explicit input. No numerical ODE or floating-point eigenvalues establish the certified interval.

The written operator/series/contour and Hamiltonian arguments establish the universal scope; the program checks their finite rational matrices and margins. Independent review NOT_RUN. The chosen plane, eta=1 penalty and lambda remain inverse-designed, physical maps OPEN, physical promotion0. The previous full-S4 and all-active-locality obstructions remain unchanged.

Next: tighten the large resolvent/logarithm bounds or use rigorously enclosed return-map integration to certify a larger finite coupling window, starting with the previously sampled mu=1/64. Preserve exact versus numerical status and expose any failed margin. Do not treat the present conservative endpoint as the true loss-of-stability boundary.
