# Prepared-clock transverse stability and finite readout window v0.1

**RESULT — EXACT / CONDITIONAL.** The positive13-term local clock from [PREPARED_PLANE.md](PREPARED_PLANE.md) is transversely unstable for sufficiently weak positive coupling. The leading native growth exponent is `3mu/8+O(mu^2)`, mu=lambda I. **NUMERICAL:** every positive point in the stated finite grid has a return multiplier outside the unit circle. **EXACT / CONDITIONAL:** despite this long-time failure, a one-cycle nonlinear readout window with explicit initialization and energy gates has phase error below1/1000 rad. The particular13-term law is PARKED as a robust clock mechanism, not discarded as an invariant-orbit construction.

## 1. Source and state contract

Integrated base `ud-tetra/UD-Physics@dca1009ae232fe3d392d815eb3525aaf97d39dba`; research parent `8e94fd49ded70a00eb4986177d3463860d295960`. Same session/task/held claim `clockmatrix-20261104-01` / `clock-matrix-question-20261104` / `72863501bd80db6aae1fd9b68467de48e92cb42c`. Inspected and merged the new G05/Q136/G06 anchor audit; it adds no clock unit or quartic selection and changes no operator dependency. Sources are [prepared-plane v0.1](PREPARED_PLANE.md) §§1–5, [local quartic v0.1](LOCAL_QUARTIC.md) §§1–6, and [local-generator v1.0](../qpb1-local-generators/README.md) §§1–4. Historical supplied ledger Q166/Q169/Q170 governs native incidence stocks/generator, not this interaction. No physical measurement or external empirical target used.

Retain C=R^15, ascending simplicial basis, unit positive metric; J=A/2, active V=h0-perp, dim14. Prepared W=span(v,h), v=e_vertex1-e_vertex2, h=Jv, normsquared2. Its normal space N=V intersect W-perp has dimension12. Write orthogonal projector P_N=I-h0 h0^T-(vv^T+hh^T)/2. The Hamiltonian is H=||x||^2+lambda Q with the explicit13-term Q fixed, lambda>=0. Native continuous parameter s, no boundary drive/loss. Coefficients and stock I dimensionless; no physical clock/energy/action map.

Reference solution x*(s)=sqrt(I)[v cos(theta)+h sin(theta)], theta=(2+mu)s, mu=lambda I, I>0. This orbit is exactly invariant. Tangent phase/amplitude perturbations must not be confused with transverse N perturbations; changing I changes frequency and can cause tangent phase drift even if N errors were stable.

## 2. Exact transverse equation

The variational equation is

    xi'=J[2Id+lambda Hess Q(x*(s))]xi.

Differentiating gradQ|W=I x shows HessQ maps W into W. Symmetry of HessQ and J-invariance of W,V imply the transverse N block is invariant in the linearization; there is no first-order tangent-to-normal forcing. The harmonic direction is excluded. On N introduce rho=mu/(2+mu), 0<=rho<1, and theta as independent variable:

    d eta/dtheta=J_N[(1-rho)Id+rho B_N(theta)]eta,
    B(theta)=Bc cos^2(theta)+Bs sin^2(theta)+Bx cos(theta)sin(theta).

Here Bc=HessQ(v), Bs=HessQ(h), Bx=HessQ(v+h)-Bc-Bs, projected onto N. B has period pi in theta, half the clock orbit. A half-orbit return map suffices; full-orbit multipliers are its squares.

For a direct exact matrix recipe, HessQ(qv+ph) is nonzero only on vertices1,2 and edges01,02,12,13,23. Both vertex diagonal entries are3q^2+p^2; each of those five edge diagonal entries isq^2+3p^2. Off-diagonal vertex/edge entries are qp times

| Pair | vertex1-edge01 | vertex1-edge12 | vertex1-edge13 | vertex2-edge02 | vertex2-edge12 | vertex2-edge23 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| sign | -1 | +1 | +1 | -1 | -1 | +1 |

All unlisted entries vanish. This reproduces the Hessian by differentiating the original Q in the numerical program, while the exact program constructs the displayed matrix independently.

## 3. Exact weak-positive-coupling instability

Let U_rho(pi) be the transverse half-return matrix. At rho=0 it is -Id_N. Pass to the interaction picture with exp(J_N theta). Exact trigonometric averages give

    U_rho(pi)=-[Id_N+pi rho T_N+O(rho^2)],
    T=P_N{[J(3Bc+Bs)+(Bc+3Bs)J+J Bx J+Bx]/8-J}P_N.

The coefficient follows from averages cos^4=sin^4=3/8, cos^2 sin^2=1/8 and odd mixed averages0 on[0,pi]. It is not a numerical fit. Exact rational ranks and a polynomial annihilator prove

    spec(T|N)={+3/8,-3/8,(+1/4)^3,(-1/4)^3,(+i)^2,(-i)^2}.

On the full15-dimensional matrix there are three additional zero directions: two tangent and one harmonic, all excluded from N. The exact annihilator is t(t^2-9/64)(t^2-1/16)(t^2+1). Kernel dimensions1,1,3,3,4 for the nonzero factors account for all12 transverse coordinates. In particular +3/8 is simple. Ordinary finite-matrix analytic perturbation then yields a real multiplier branch

    m_+(rho)=-[1+(3pi/8)rho+O(rho^2)],

so |m_+|>1 for all sufficiently small positive rho. The equivalent native growth exponent is

    log|m_+| / [pi/(2+mu)] = 3mu/8+O(mu^2).

This establishes linear instability and, by the expanding transverse multiplier of the smooth Poincare map, nonlinear orbital instability of the periodic orbit in that sufficiently-small-positive parameter regime. It gives no explicit numerical endpoint for that regime. It does not prove instability at every positive coupling, nor classify negative coupling, modified Q, restricted perturbations or noise-stabilized/open systems. At lambda=0 the native linear motion is orthogonal and transverse errors are neutral.

## 4. Numerical finite-grid corroboration

Own classical RK4 integrates the12x12 fundamental matrix over theta in[0,pi], using2048 steps and then4096 steps. Matrix eigenvalues use NumPy2.3.5 float64. The orthonormal N basis is computed from P_N. No program from another task or deposit is executed.

| mu | Largest half-return multiplier modulus, numerical |
| ---: | ---: |
| 0 | 1.0000000000 |
| 1/64 | 1.0091872708 |
| 1/16 | 1.0365475823 |
| 1/4 | 1.1428672333 |
| 1 | 1.5168317464 |
| 2 | 1.9019588697 |
| 4 | 2.4124166095 |
| 8 | 2.9403327974 |
| 16 | 3.3666974065 |
| 64 | 3.8161540838 |

The maximum2048/4096 step-doubling difference in matrix2-norm is2.85e-12; maximum symplectic residual is1.93e-14. These are convergence/structure diagnostics, not rigorous error enclosures or proof for the continuum of mu. Eigenvector condition numbers are retained in the result file. The finite grid is target-informed mathematical exploration, not empirical evidence. All nine positive grid values show growth comfortably above numerical discrepancies.

An exploratory attempt to use an unavailable symbolic package failed with ModuleNotFoundError before the exact computation; the final certificate instead uses standalone Fraction rank arithmetic and requires no such package. No failed computation is presented as a completed symbolic proof.

## 5. Exact nonlinear finite observation window

A controlled short readout does not require all-time orbital stability. For the fixed positive Q, H>=||x||^2 and energy is conserved. A sharper global Hessian bound than the previous72 is

    ||HessQ(x)|| <=13||x||^2.

Proof by symmetric row sums: each active vertex row is bounded by(11/2)||x||^2, each outer-edge row by13||x||^2, and the central-edge row by4||x||^2; all other rows vanish. These follow from2|ab|<=a^2+b^2 applied to the explicit Hessian. The spectral norm of a symmetric matrix is at most its largest absolute row sum.

Compare exact trajectories x(s) and reference z(s) from z0 in W. If both initial energies are <=R^2, both trajectories stay in the radiusR ball for all time. In the error e=x-z the linear term2Je has zero contribution to d||e||^2/ds because J is skew. The nonlinear mean-value/Hessian bound therefore gives

    ||e(s)|| <= exp(13lambda R^2 |s|)||e(0)||.

This is a nonlinear finite-time guarantee, not merely a linearized estimate. Set the following exact, illustrative gates:

| Quantity | Gate |
| --- | --- |
| Reference | I=1, q(0)=1,p(0)=0 |
| Coupling | lambda=1/64, hence Omega=129/64 |
| Initial active state | x0 in V, ||x0-z0||<=1/4096 |
| Energy | H(x0)<=33/16 and H(z0)=257/128<33/16 |
| Observation interval | 0<=s<=T=128pi/129, one reference cycle |

Then13lambda R^2 T<=143pi/344 and exp(143pi/344)<4. The exact code checks the latter using pi<22/7 and a rational Taylor-series upper bound for exp(4/3)<4. Consequently

    ||x(s)-z(s)||<1/1024, distance(x(s),W)<1/1024

over the whole interval. Read out q=v^T x/2,p=h^T x/2. Their two-coordinate error is <=||e||/sqrt(2); the reference radius is1. The phase lift can be chosen continuously, and

    |theta_x(s)-theta_z(s)|<=asin[1/(1024sqrt(2))]<1/1000 rad.

The final inequality follows from1/sqrt(2)<3/4 and sin(1/1000)>1/1000-(1/1000)^3/6, checked in exact rational arithmetic. The phase readout remains nonzero, so no hidden zero-amplitude phase exclusion occurs. These are exact gates in formal state/parameter units; apparatus preparation, measurement noise and physical time calibration are not supplied.

For comparison at the same T, a perfectly prepared lambda=0 reference accumulates phase2T. The candidate-reference difference is2pi/129, larger than the stipulated1/1000-rad model error. This is a model-to-model discriminant under chosen lambda and preparation, not an independent native prediction or observed time-dilation signal.

## 6. Disposition and next step

**PARKED:** the specific13-term Q as a long-time robust clock, because weak-positive-coupling transverse instability is proved. Preserve its valid invariant plane and finite observation-window theorem. Full signedS4 selection remains obstructed on this plane; native preparation, coefficient selection, physical map and independent review remain OPEN. Physical promotion0; no registry export or empirical claim.

The even local family has30 homogeneous coefficient directions with zero vector field on W. Some can alter transverse Hessians without changing the exact clock law; therefore this witness's instability is not an all-local-quartic no-go. Next test whether those directions admit a positive local modification that removes transverse hyperbolicity while retaining gradQ|W=Ix. Treat any choice as inverse design until an independent source selects it. Do not repeat a coupling scan of this fixed Q without a new discriminant.

## 7. Reproduction

Run `python3 experiments/clock-matrix-question/transverse_exact.py` for rational eigenspace/annihilator and observation-window certificates, and `python3 experiments/clock-matrix-question/transverse_stability.py` for the numerical grid and convergence diagnostics. The exact certificate is standard-library only; the numerical program requires NumPy, version recorded. Both programs are newly authored for this task. Evidence labels are EXACT/CONDITIONAL for the proofs and finite gates, NUMERICAL for the grid. Independent review NOT_RUN.
