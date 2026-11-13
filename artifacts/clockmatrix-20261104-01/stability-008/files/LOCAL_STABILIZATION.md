# Positive local penalties and weak-coupling transverse stabilization v0.1

**RESULT — EXACT / CONDITIONAL.** A positive14-term nearest-incidence penalty leaves the selected clock orbit and its rate `Omega=2+lambda I` unchanged, but changes its transverse linearization. At penalty strength eta=1, the modified orbit has bounded transverse linear motion for every sufficiently small positive mu=lambda I. The endpoint of that interval is not yet certified. **NUMERICAL:** eta=1 removes growth at the disclosed points up to mu=4 but growth returns at mu=8. Nonlinear orbital stability and native parameter selection remain OPEN.

## 1. Source boundary and retained objects

Integrated base `ud-tetra/UD-Physics@51bd7252473ecbbe3c4f5cb83011e45b5eeace09`; research parent `b65135ce434564c221d5991d5283b6a63aa328a7`. Same session `clockmatrix-20261104-01`, task `clock-matrix-question-20261104`, held claim `72863501bd80db6aae1fd9b68467de48e92cb42c`; no new main changes at resume. Retain [prepared-plane v0.1](PREPARED_PLANE.md) §§1–6 and [transverse-stability v0.1](TRANSVERSE_STABILITY.md) §§1–6. The latter instability result remains valid for its unchanged original13-term Q. Historical ledger Q166/Q169/Q170 and the [local-generator source](../qpb1-local-generators/README.md), §§1–4, supply the fixed carrier and incidence dynamics, not the penalty or coefficient selection.

C=R^15, ascending tetrahedral simplex basis, unit positive metric, J=A/2. V=h0-perp, dim14; W=span(v,h), v=e_vertex1-e_vertex2, h=Jv, normsquared2. Normal N=V intersect W-perp, dim12. Clock x=qv+ph, I=q^2+p^2. Evolution uses native dimensionless s and H_eta=||x||^2+lambda Q_eta. All stocks, energy, lambda and eta formal dimensionless; physical time/action/energy maps OPEN. Lambda>=0,eta>=0 in the positive family. No drive, damping, bath or boundary flux; this mechanism changes conservative stiffness and is not attraction to W.

## 2. Exhaustive even null directions and chosen penalty

The43 even nearest-incidence quartics split into13 terms supported wholly on active registers and30 with at least one inactive register. The13-term active coefficient system is nonsingular for the prescribed plane rate; its coefficients are exactly the previous Q. Each other even monomial has zero value and zero gradient on W. Of those30, eight are inactive fourth powers, eight use two inactive registers, and14 use an inactive register paired with an active edge. Only the latter14 change the transverse Hessian on W. This is why a positive penalty can preserve the clock law while modifying linear stability; no interaction is sourced by the null-space count alone.

Let E*={01,02,12,13,23} be the active edges, and S={vertex0,vertex3,face012,face013,face023,face123}. For each inactive register sigma in S define

    w_sigma=sum_(e in E*,e~sigma) h_e^2,
    R(x)=sum_(sigma in S) [x_sigma^2/(2w_sigma)] sum_(e in E*,e~sigma) z_e^2,
    Q_eta=Q+eta R.

The weights are w=1/2 at vertices0,3 and faces013,023, and w=3/2 at faces012,123. Thus all14 coefficients are positive, equal to1 or1/3. The code lists every oriented register pair and coefficient. Each pair is one Hasse incidence. No global stock readout or spatially nonlocal term is used in this energy functional. This locality is on chain registers, not a physical propagation cone.

On x=qv+ph, all x_sigma vanish, so

    R|W=0, gradR|W=0, HessR|W=p^2 D6,

where D6 is the diagonal projector onto the six listed inactive registers. Therefore the original exact plane and rate persist for every eta:

    x'=(2+lambda I)Jx on W, I'=0.

For eta>=0, R>=0; with lambda>=0, H_eta>=||x||^2. Conservation of H_eta gives global existence and bounded energy sublevels, which do not by themselves establish stability of W. The interaction still selects the same anisotropic plane and does not evade the full-S4 obstruction on that plane.

## 3. Search and selection disclosure

The explored one-parameter family is newly imposed. A coarse numerical search used eta in{0,1/4,1/2,1,2,4,8,16,32,64}, mu in{1/16,1,4}, and1024 RK4 steps over the half-return phase interval[0,pi]. Eta=1 was the first value in that ordered list with no numerical transverse growth at those three points; eta=2 also passed. Larger penalties sometimes destabilize the clock again. Eta=1 was selected from this exposed mathematical search, not from a native variational principle or a held-out experiment. This is inverse design; no empirical parameter fit or physical prediction is claimed.

A subsequent exact certificate establishes weak-coupling linear stability for eta=1 independently of the grid values. A further10-point mu grid refines the numerical characterization of that selected candidate. These computations remain constructor checks, not nonconstructor review or independent data.

## 4. Exact leading transverse spectrum and signatures

Use theta=(2+mu)s, rho=mu/(2+mu). The transverse equation from the previous report remains

    d xi/dtheta=J_N[(1-rho)Id+rho B_eta(theta)]xi,

with only Bs changed to Bs+eta D6 before projection. Half-return U_rho(pi)=-[Id+pi rho T_eta+O(rho^2)]. The same exact trigonometric average yields

    T_eta=P_N{[J(3Bc+Bs_eta)+(Bc+3Bs_eta)J+J Bx J+Bx]/8-J}P_N.

At eta=1, standalone Fraction algebra proves the full15-dimensional annihilator

    t(t^2+19/256)(t^2+35/64)(t^2+3/64).

The three zero coordinates are tangent/harmonic and excluded from N. Put K=-J T_1; K is symmetric. Exact bases of ker(T_1^2+nu^2 Id) and exact LDL pivots of K restricted to those bases give:

| Frequency squared nu^2 | Real normal dimension | Sign of K on that subspace | Exact LDL pivots |
| --- | ---: | --- | --- |
| 19/256 | 2 | Positive | 19/4,1/4 |
| 35/64 | 4 | Negative | -5/8,-7/2,-7/2,-5/8 |
| 3/64 | 6 | Positive | 3/8,5/24,1/5,15/16,9/10,1/2 |

All12 normal dimensions are accounted for; the factors are distinct and have no repeated roots. Thus the leading normal frequencies are sqrt(19)/16, sqrt(35)/8 and sqrt(3)/8, with complex eigenvalue multiplicities1,2,3 for each signed pair. These frequencies belong to the scaled averaged transverse generator, not to additional measured clock species or physical particles.

Definiteness within each separated frequency group is the signature condition used below. It is distinct from positive definiteness on the whole normal space: K is indefinite globally. The explicit rational pivots allow the condition to be checked without a floating eigenvalue-sign decision.

## 5. Proof of actual weak-coupling linear stability

The leading imaginary eigenvalues alone would be insufficient. Here the definite subspace signatures close the additional step.

For rho near0, M_rho=-U_rho(pi) is a real symplectic matrix near identity. Its local matrix logarithm exists analytically. Define

    L_rho=log(M_rho)/(pi rho), L_0=T_1|N.

The removable value at rho=0 is the exact leading generator. The symplectic identity implies L_rho is Hamiltonian; therefore K_rho=-J_N L_rho is symmetric and tends to K|N. The three real spectral subspaces associated with the separated conjugate frequency groups persist continuously for sufficiently small rho, by their isolating spectral projectors. K_rho restricted to each remains definite with its original sign, since its limiting restriction is definite. No group meets zero or another group for sufficiently small rho.

The Hamiltonian identity gives L_rho^T K_rho+K_rho L_rho=0. On each invariant subspace, multiply K_rho by its definite sign to obtain a positive metric. L_rho is skew-adjoint in that metric, so it has semisimple imaginary eigenvalues and bounded linear motion there. This follows directly by conjugating with a square root of that positive metric to a real skew matrix. Combining the three subspaces proves that every transverse multiplier of U_rho(pi)=-exp(pi rho L_rho) has unit modulus and is semisimple. Periodic bounded intra-period evolution then gives bounded transverse linear perturbations for each fixed sufficiently small positive rho.

This proves an existential positive stability interval and an open coefficient neighborhood around eta=1 in the same weak-coupling setting. It does not supply a numerical interval endpoint, a uniform gain bound as parameters approach a collision, nonlinear orbital stability, control of all tangent phase drift, or native coefficient selection. Opposite signature groups make later collisions a relevant risk; the finite-coupling numerical counterexample below is retained.

## 6. Finite-coupling numerical results and counterexample

The selected eta=1 candidate was replayed with2048 and4096 own-RK4 steps per half orbit, using the prior task's own differentiation and Floquet routines. NumPy2.3.5 float64 supplies eigenvalues. Largest multiplier moduli:

| mu | Original Q | Modified Q+R |
| ---: | ---: | ---: |
| 1/64 | 1.0091872708 | 1.0000000000 |
| 1/16 | 1.0365475823 | 1.0000000000 |
| 1/4 | 1.1428672333 | 1.0000000000 |
| 1 | 1.5168317464 | 1.0000000000 |
| 2 | 1.9019588697 | 1.0000000000 |
| 4 | 2.4124166095 | 1.0000000000 |
| 8 | 2.9403327974 | 1.1329632575 |
| 16 | 3.3666974065 | 1.2722152247 |
| 64 | 3.8161540838 | 1.3945281965 |

Mu=0 is neutral in both models. The modified results at positive mu<=4 in this grid differ from unit modulus by at most3e-15, while the largest step-doubling matrix difference across all10 points is1.21e-12 and the largest symplectic residual is9.45e-15. Eigenvector condition numbers are retained. These diagnostics are not rigorous enclosures and do not prove stability throughout[0,4] or locate the first loss of stability between4 and8. The original column is read from its preserved preceding result; no original instability result is overwritten.

The strong-coupling failure demonstrates that removing weak growth does not produce an all-parameter robust clock. The next discriminant is a certified finite coupling interval and its error-growth bound, not a larger undirected scan.

## 7. Disposition and reproduction

**EXACT / CONDITIONAL:** the14 positive local penalties preserve the plane and rate, and eta=1 removes the previous weak-positive transverse hyperbolicity with bounded linear normal motion. **NUMERICAL:** finite tested low/moderate couplings pass the multiplier test, higher tested couplings fail. **OPEN:** nonlinear orbital stability, an explicit certified finite-mu range, transient/initialization tolerances for the modified model, native preparation and coefficients, physical calibration and independent review. The original13-term robust-clock branch stays PARKED; this modified branch is ACTIVE as an inverse-designed candidate. Physical promotion0; no registry or physical-identification claim.

Run `python3 experiments/clock-matrix-question/stabilization_exact.py` for exact pair weights, normal spectrum and signature pivots. Run `python3 experiments/clock-matrix-question/local_stabilization.py` for the30-case exploratory grid and10-case selected-candidate refinement. It imports only this task's own `transverse_stability.py` implementation, captured as an explicit dependency; no external deposit or author program is executed. The exact certificate is standard-library only; the numerical calculation requires NumPy. Inputs/results/receipt are preserved in stability-008. Independent review NOT_RUN.
