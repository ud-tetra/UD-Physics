# UD Discovery — exact rotational channel reduction around the symmetric moving 3D pulse

**RESULT — EXACT / CONDITIONAL for uniform mechanical coefficients; NUMERICAL / CONSTRUCTOR checks; nonlinear u100 full-phase safety remains OPEN.**

**Question.** Can the all-180-dimensional initial housing-phase propagator around the exact symmetric moving baseline be reduced by an actual symmetry of the *unchanged* passive 560-state force law? Does the same symmetry alone control its second-order nonlinear remainder?

**Source and isolation.** Read-only source from `ud-tetra/UD-Physics`, main `407fe6da298ea3362886075fdd696bf1dfefd2fb` at verification, with 3D `model.py`, `network.py`, `damping.py`, `hardware.py`, `mountloss.py`, and `analyze.py` blobs unchanged from the established source baseline. Task `icosahedral-phasewindow-20261022`, claim held by `phasewindow-20261022-gpt6-7c41`; separate forced-Green PR #44 held by another owner, untouched. The benchmark 019 supplies the exact all-time symmetric reference domain: shell scale `37/40 < b < 43/40`, 120 housing struts `>37/80`, for uniform parameters and radial-symmetric housing preparation. Current run does **not** prove nearby perturbed trajectories remain in that domain.

## Model, metric and group

Take Euclidean \(\mathbb R^3\) with regular icosahedral reference exterior-edge length one, 12 shell vectors \(v_i\), \(R^2=(5+\sqrt5)/8\), and all 30 shell edges. Time \(u\) is the uncalibrated internal mechanical evolution parameter; scalar heart \(\alpha\) is a coordinate, not time. Use **uniform** primary masses, spoke/edge stiffnesses, reciprocal gains exactly 1, housing weights exactly 1, and uniform positive \(\beta\), \(\nu\), \(c_f\). The model includes 13 primary site positions, 150 auxiliary signed scalar link coordinates, 30 housing 3-vectors, 280 velocities, and heat ledger; all 120 current-axis viscous paths are kept.

The 60 proper icosahedral rotations form \(A_5\). Each acts by a permutation of the shell vertices together with the corresponding proper \(3\times3\) rotation \(R_g\). Housing vectors follow the 30-edge permutation and rotate by \(R_g\); each of the 150 oriented auxiliary difference coordinates follows an appropriate **signed permutation** (sign flips when its canonical pair orientation reverses). This signed rule is essential: an unsigned permutation does not preserve the source transmission rows. The scalar heart and accumulated heat remain invariant.

The elastic potential, axial primary damping, reciprocal auxiliary transmission/damping, housing mount energy, and central moving-axis viscous law are equivariant under this action. Thus the complete nonlinear mechanical force and dissipation law are equivariant wherever primary/strut lengths are positive. The full symmetry-fixed manifold is the 019 exact moving baseline. Differentiating equivariance along it shows the **full 560-phase moving tangent propagator** commutes with \(A_5\) for all times on the baseline.

For shell-relative displacements \(Y\in\mathbb R^{12\times3}\), let

\[
P_0=\frac{11^T}{12},\quad P_V=\frac{VV^T}{4R^2},\quad P=I-P_0-P_V,\quad Z=PY.
\]

Here \(V\) has rows \(v_i\), \(P\) is the exactly orthogonal rank-eight non-affine vertex projector, and \(Z\) has **24 independent real components**. The housing initial phase \(h=(\delta H,\delta\dot H)\in\mathbb R^{180}\) uses the original positive housing mount/kinetic energy metric; uniform masses and weights make the corresponding normalized rotation action orthogonal.

## Theorem A — exact \(A_5\) representation decomposition

The five conjugacy classes are indexed as \(1,2,3,5a,5b\) with sizes \(1,15,20,12,12\). Exact enumeration of the 120 integer graph automorphisms and the 60 determinant-\(+1\) \(\mathbb Q(\sqrt5)\) isometries gives:

| Rotation class | Size | Fixed vertices | Fixed edges | Physical \(\mathrm{tr}\,R_g\) |
|---|---:|---:|---:|---|
| identity | 1 | 12 | 30 | 3 |
| order 2 | 15 | 0 | 2 | −1 |
| order 3 | 20 | 0 | 0 | 0 |
| order 5a | 12 | 2 | 0 | \(\varphi\) |
| order 5b | 12 | 2 | 0 | \(1-\varphi\) |

Because \(P_V\) is the reference 3D-rotation copy inside the 12-vertex permutation representation, the projected vertex character is

\[
\mathrm{tr}(P\Pi_g)=\#\operatorname{Fix}_{vertices}(g)-1-\mathrm{tr}(R_g).
\]

The 24D non-affine output and 90D housing-position characters are therefore exactly

\[
\chi_Z=(24,0,0,-1,-1),\qquad\chi_{H,90}=(90,-2,0,0,0).
\]

Each initial housing phase includes both position and velocity, so \(\chi_{H,180}=2\chi_{H,90}\). Exact character inner products against the five real irreducible characters of \(A_5\) yield:

\[
\boxed{Z\ \cong\ \mathbf3\oplus\mathbf{3'}\oplus2\mathbf4\oplus2\mathbf5,}
\]
\[
\boxed{H_{180}\ \cong\ 2\mathbf1\oplus10\mathbf3\oplus10\mathbf{3'}\oplus12\mathbf4\oplus14\mathbf5.}
\]

All multiplicities are nonnegative exact integers and the dimensions sum to 24 and 180 respectively. No hidden `A5` singlet occurs in the non-affine output; the **two symmetric housing-phase singlets have identically zero first-order non-affine response for all time** (and, by theorem 019, stay exactly non-affine-zero when initiated purely in the symmetric family).

## Theorem B — exact all-time algebraic reduction of moving *linear* gain

Let \(\Phi(u,0)\) be the full 560D mechanical tangent evolution along the 019 symmetric moving solution; it need not be self-adjoint or time-independent. Let \(B\) inject energy-normalized 180D initial housing phases into the tangent state, and \(C\) extract the 24D output \(Z\). Define

\[
L(u)=C\Phi(u,0)B:\mathbb R^{180}\longrightarrow\mathbb R^{24}.
\]

Every factor is an intertwiner. Hence the symmetric positive-semidefinite output Gram \(K(u)=L(u)L(u)^T\) commutes with the output representation. All irreducible characters are of real type. Schur's lemma forces, in a **fixed orthonormal representation basis**,

\[
K(u)= k_3(u)I_3\oplus k_{3'}(u)I_3
 \oplus\bigl(B_4(u)\otimes I_4\bigr)
 \oplus\bigl(B_5(u)\otimes I_5\bigr),
\]

where \(k_3,k_{3'}\ge0\) and \(B_4,B_5\in\mathbb S_+^2\). Thus **exactly**, for every time where the symmetric baseline exists,

\[
\boxed{\|L(u)\|_2^2
=\max\bigl\{k_3(u),k_{3'}(u),\lambda_{\max}(B_4(u)),\lambda_{\max}(B_5(u))\bigr\}.}
\]

This replaces a generic 24x24 symmetric eigenproblem with **two real scalars and two 2x2 symmetric blocks**. The sectors have eigenvalue multiplicities 3,3,4,4,5,5. It does **not** replace propagator integration or its validation by algebra alone, and these time-dependent coefficients have not been bounded through `u=100` in this run.

### Constructor check — full 180-phase initial acceleration

At symmetric reference equilibrium with \(\beta=.005,\nu=.05,c_f=0\) and \(E_h=51/20000000\), an energy-normalized analytic 36x180 matrix mapping initial housing phases to projected primary acceleration has rank24 and largest singular value `0.0009605640670680957` in the source's dimensionless acceleration units. It commutes/intertwines all 60 proper rotations to maximum floating entry error `4.07e-20`; its Gram commutator error is below `1.1e-21`. Central character projectors recover the expected non-affine ranks `0,3,3,8,10` and the expected 3/3/4/4/5/5 eigenvalue degeneracies. **NUMERICAL constructor check at u=0 only**, not the moving u100 gain.

The separate full 560-state nonlinear test at one safely perturbed asymmetric state evaluated every one of the 60 rotations, including signed auxiliary transformation. Its maximum componentwise force-equivariance error was below `2.9e-14`; energy, heat power, projected readout and housing norm also transform correctly to floating precision. This independently checks the *implementation* of the exact covariance premise, not the future dynamics.

## Theorem C — nonlinear second order does not decouple into six scalar tests

The nonlinear displacement Hessian at a symmetric trajectory is an equivariant symmetric bilinear map

\[
D^2 Z(u):\operatorname{Sym}^2(H_{180})\longrightarrow Z.
\]

Its *allowed* linear space of equivariant bilinear maps is large. The symmetric-square character follows from

\[
\chi_{\operatorname{Sym}^2H}(g)=\tfrac12(\chi_H(g)^2+\chi_H(g^2))
=(16290,98,0,0,0).
\]

The character inner product gives **exactly**

\[
\boxed{\dim\operatorname{Hom}_{A_5}(\operatorname{Sym}^2H_{180},Z)=6516.}
\]

This is the dimension of *symmetry-permitted* quadratic maps, not a count of independently adjustable physical parameters or proof that all modes are excited. Unlike the linear sector result, it shows that symmetry **alone** cannot bound or eliminate the nonlinear remainder. In particular the previously measured mixed position/velocity nullspace curvature in checkpoint 016 is compatible with these selection rules.

## What remains open and highest-value follow-up

- **OPEN** validated continuous-time values/enclosures for \(k_3(u),k_{3'}(u),B_4(u),B_5(u)\) on \(0\le u\le100\), even in this uniform moving baseline. A block-adjoint scheme requires at most six correctly aligned output seeds per time step, once verified isotypic bases are constructed; this is a *computational strategy*, not an already executed six-propagator result.
- **OPEN** full 180D nonlinear housing perturbation relative to the moving symmetric baseline. Bilinear and higher interactions between symmetry channels are allowed; a uniform Hessian/positive-strut bootstrap is still needed.
- **OPEN** scattered-property regime: it breaks the \(A_5\) symmetry, so block reduction does not carry over unchanged. A parameter-deviation perturbation estimate would have to justify any transfer.
- **OPEN** nonlinear u100 strut domain, cell orientation, breathing RMS, hub mismatch, housing ringdown and physical UD identification/calibration. The full-time symmetric **reference** domain in checkpoint 019 is not the full phase ball.
- **FIT / DEVELOPMENT:** Housing energy, nu/beta and readout threshold were already exposed. The irreducible decomposition is not fitted to these targets. The symmetry-reduced *target* was selected after seeing numerical full-phase computation costs; no independent prediction is claimed.

**Recommended next discriminant, priority 99/100:** Construct the six compatible symmetry-adapted adjoint seed channels and verify their reconstructed full-180 gain against the existing 24-output numerical reference. Then enclose their continuous-time gain and establish a **separate** housing-relative nonlinear remainder/bootstrap. Preserve the rank-four and low-energy strut counterexamples as negative controls and do not edit PR #44's held recovery files.