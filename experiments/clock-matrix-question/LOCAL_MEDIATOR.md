# Local reciprocal mediator gate v0.1

**RESULT — EXACT / CONDITIONAL.** A declared stable harmonic mediator produces reciprocal clock shifts, but its eliminated quadratic action interaction is negative semidefinite: a nonzero mutual shift necessarily brings self shifts. A pure nonzero action product needs added counterterms or changed assumptions. One register contact cannot give a uniform rate on the entire 14-dimensional active tetrahedral clock space. No mediator or coefficient is native-selected by the inspected sources.

## 1. Source boundary and typed objects

Integrated UD-Physics revision `e400dfb715262a44b3bbb2e929c7b438028af67e`; previous research head `0d82f009d4a492b1b4ab884465c5dc759538670d`. Retain [COMMON_RATE.md](COMMON_RATE.md) §§1–4 and [local-generator classification v1.0](../qpb1-local-generators/README.md) §§1–4. Historical supplied coefficient ledger v0.39(2), Q166/Q169/Q170, supplies skew support dynamics and incidence-cut stock balances, not a constitutive clock mediator. Supplied master_action.md and packet_field_equation.md contain placeholders only. Supplied CRL2 proposal v1.0 §§2,4,5 is governance, not a mediator law. The designated portal inspected 2026-11-05 advertises Papers I–III 1.1.1 / IV 0.1, review pending, physical promotion 0; no new coupling imported from its homepage.

Clock states x,y lie in V=im P subset R^15, dim V=14, P=I-hh^T, where h has entries 1/2 on the four vertices and zero otherwise. Positive Euclidean metric, ascending simplex orientations, J=A/2 restricted to V, J^2=-I. Define I_L=x^T x/2 and I_R=y^T y/2. All quantities below are dimensionless formal Hamiltonian variables; I is quadratic stock, not calibrated physical action. Native evolution parameter s is continuous. Poisson tensor diag(J,J,J_m), J_m=[[0,I],[-I,0]], with mediator (q,p) in R^m x R^m and q'=partial_p H. No external drive, damping or boundary flux. Fixed phase-plane readouts are those of COMMON_RATE.md.

## 2. Passive mediator and exact prepared reduction

**HYPOTHESIS:** declare K=K^T positive definite, two real port vectors c_L,c_R and

    H=2(I_L+I_R)+(p^T p+q^T K q)/2+q^T(c_L I_L+c_R I_R).

Then

    x'=(2+c_L^T q)Jx, y'=(2+c_R^T q)Jy,
    q'=p, p'=-Kq-c_L I_L-c_R I_R.

Both actions are exactly conserved, and the full H is conserved. Every phase plane within each copy has one instantaneous rate, even during mediator transients. Let C=[c_L,c_R], i=(I_L,I_R)^T. The static point is q*=-K^-1 C i, p*=0. It is an invariant preparation manifold because i is conserved. Completing the square gives

    H=2(I_L+I_R)+p^T p/2+(q-q*)^T K(q-q*)/2 - i^T S i/2,
    S=C^T K^-1 C.

On that prepared manifold, H_eff=2(I_L+I_R)-i^T S i/2 and Omega=2(1,1)^T-S i. This is an exact conditional reduction, not generic instantaneous equilibration. Generic q(0),p(0) retains undamped oscillatory memory; stability does not imply convergence. At q(0)=p(0)=0, the initial rate is 2 at both clocks, and

    Omega_L''(0)=-c_L^T C i,

rather than an already present constant reduced shift. Dynamic locality therefore remains distinct from static elimination. Negative quartic terms make this Hamiltonian globally unbounded below when actions can grow; actions are constants of motion, so a fixed-action orbit is bounded in q,p. A bounded action domain with positive clock rates, or an explicitly supplied stabilizing Hamiltonian, is required for a physical candidate. Counterterms below can repair this but are extra hypotheses.

## 3. No pure mutual term from this passive mediator alone

S is a Gram matrix in the positive K^-1 metric. Therefore

    S_LL>=0, S_RR>=0, S_LR^2<=S_LL S_RR.

In H_eff the mutual coefficient is g=-S_LR and the self coefficients are -S_LL/2 and -S_RR/2. If both self shifts vanish, c_L=c_R=0 and g=0; in fact either zero self coefficient forces g=0. Thus a nonzero pure g I_L I_R from COMMON_RATE.md cannot arise from this mediator alone. This also holds for a sum of positive harmonic mediators, since sums of Gram matrices remain positive semidefinite. It does not cover nonlinear mediators, indefinite stiffness, non-equilibrium driving, delayed/non-Hamiltonian reductions or pre-existing action counterterms.

Adding H_ct=(S_LL I_L^2+S_RR I_R^2)/2 cancels the self terms on the prepared manifold and leaves exactly 2(I_L+I_R)+g I_L I_R. This is a constructive but inverse-designed cancellation; it does not explain why UD supplies those terms. The full added terms are positive quartic stock terms; for g>=0 the completed Hamiltonian is bounded below on nonnegative actions. For g<0 retain an action bound or further stabilization. The coefficient g still depends on K and both ports, all newly assumed. Rescaling both ports by a multiplies g by a^2 without changing interaction topology or reciprocity, establishing nonselection within this model family.

## 4. Explicit two-site spatially local mediator candidate

Take mediator sites L,R with local pinning k>0, nearest-site spring t>=0:

    K=[[k+t,-t],[-t,k+t]],
    K^-1=[[k+t,t],[t,k+t]]/[k(k+2t)],
    c_L=(a,0)^T, c_R=(0,b)^T.

Then

    S_LL=a^2(k+t)/[k(k+2t)],
    S_RR=b^2(k+t)/[k(k+2t)],
    g=-ab t/[k(k+2t)].

The mediator's Hamiltonian is nearest-site local and reciprocal. Opposite port signs give positive g; equal signs give negative g. t=0 removes the cross shift while leaving self shifts. k=0 has a zero mode and falls outside positive-definite elimination. With k=t=a=1,b=-1: S=[[2/3,-1/3],[-1/3,2/3]], g=1/3. This is an illustration with chosen rational parameters, not a selected UD constant.

Crucial locality boundary: a q_L I_L couples a site to the sum of all 15 clock-register squares. It is local between declared whole-clock nodes, but is collective within each tetrahedron. It is not an incidence-local realization on the native chain registers and establishes no relativistic finite-speed cone. Eliminating mediator variables produces a nonlocal-in-time response for generic preparations, not an instantaneous physical signal law.

## 5. Register-local contact gate

For a diagonal clock potential D(v)=diag(v_1,...,v_15), let the added Hamiltonian be x^T D(v)x/2. Its active generator is J D(v)x, since J annihilates h. A uniform additional rate r on every active state is equivalent to

    P D(v) P = r P.

Necessity: multiply J D(v)x=rJx by -J on V. For each of the eleven nonvertex coordinate vectors, which lie in V, obtain v_j=r. For vertex pairs x=e_i-e_j, the quadratic identity gives v_i+v_j=2r; all six pairs among four vertices imply all v_i=r. Sufficiency is immediate. Thus all fifteen register potentials must be equal in this diagonal class. Source S4 symmetry alone cannot equate different chain degrees.

More generally, a symmetric contact Hessian B of rank m<14 cannot satisfy PBP=rP with r!=0: rank(PBP)<=m<14. One port proportional to u u^T therefore fails for all-state clock isotropy, even though it may shift a selected prepared phase plane. This rank gate concerns clock Hessians, not mediator count: one collective radial port already acts with Hessian proportional to the identity and has full active rank. Multiple engineered contacts or restrictions on preparations change the question.

## 6. Discriminant and source disposition

The passive-mediated family predicts preparation slopes

    M_ij=partial_(I_j) Omega_i=-S_ij,
    M_LL<=0, M_RR<=0, M_LR=M_RL,
    M_LR^2<=M_LL M_RR.

The uncancelled pure action-product model instead has zero diagonal slopes and nonzero cross slopes, violating this passive-only bound. Separately varying both prepared stocks could distinguish them after independent readout/unit calibration; this is a proposed test, not an apparatus dataset analysis. With added counterterms the passive-only inequality no longer applies to the total slopes.

**OPEN_GATED:** native K, ports, contact support, isotropy enforcement, preparation/relaxation law, stabilization/counterterms, coefficient selection, physical time/stock/energy maps and independent evidence. Inspected sources permit neither assigning a numerical g nor identifying a gravitational lapse. Native unit incidence remains the baseline with no such mediator. This closes a conditional implementation calculation, not a mainline physical gap. Independent review NOT_RUN; physical promotion 0.

## 7. Reproduction

Run `python3 experiments/clock-matrix-question/local_mediator.py`. Standard-library Fraction arithmetic checks 54 two-site parameter fixtures, Gram and reciprocal identities, exact equilibrium/rate derivatives, zero-spring and free-start controls, and the rank of all 15 projected diagonal contact operators. Written arguments give the general conclusions; fixture checks do not substitute for proof. The code is newly authored here; no imported program is executed.
