# 3D icosahedral reference: exact center-of-mass block and projected tangent-stiffness gate

**RESULT — EXACT / CONDITIONAL:** The frozen unconstrained 43-point-mass mechanics has a mass-orthogonal six-coordinate global center-of-mass position/velocity block that decouples from all internal relative coordinates. **NUMERICAL:** An actual original 560-state DOP853 reference and source analytic Jacobian show extremely small CM coupling and *negative symmetric internal stiffness at the initial pulse state*. The source tangent position matrix becomes nonsymmetric under velocity-dependent damping along the moving reference. **FAILED:** A directly positive unshifted instantaneous stiffness-energy norm is unavailable for this source trajectory. **OPEN:** a uniformly positive alternative block norm, certified time-dependent stability Green, verified residual integral, true reference sample error below 0.01031, and full all-180 housing-phase nonlinear u100 mechanical certificate.

## Sources, objects and firewall

Integrated baseline \`ud-tetra/UD-Physics@6d5462c51e5a966066197bb56f33022ecd3a56aa\`: original \`experiments/icosahedral-pulsetube/jacobian.py\`, \`icosahedral-mountloss/mountloss.py\`, \`icosahedral-tolerances/hardware.py\`, and pulse \`variational.py\` checked blob-identical to earlier source cba74cc20ba323599339f88830bd0cc97fc9a6da. The 280-dimensional configuration has alpha, 13 primary 3D points, 150 device internal coordinates, and 30 housing 3D points, plus velocities and separate heat. Its full mechanical linearization is
\[
(q',v')=(v,-M^{-1}(K(u)q+C(u)v)),
\]
where M is positive diagonal. **K here is the effective linearized force-position matrix**, not generally the conservative Hessian: source \`Linearization.matrices(y)\` adds \(\partial_q[D(q)v]\) from position-dependent damping. The source internal pairwise forces sum to zero and are translation-invariant. Source cases \`seed10422-0-boundary2\` and \`uniform-b0.05-cf0.0\` are frozen (nu=.05, alpha0=.1, no new material/source parameter fits).

Read-only predecessor [PR #220](https://github.com/ud-tetra/UD-Physics/pull/220) narrowed the reference error requirement to a validated sampled global position error \(\delta_{\rm num}<0.010310941\). [PR #226](https://github.com/ud-tetra/UD-Physics/pull/226) showed that the raw 560-state equal q/v Euclidean scalar Gronwall gives exponential rigid-shear overestimation and cannot usefully certify it. This is a separate isolated branch, not a mainline or prior PR writeback.

## Exact invariant projector and separate rigid Green

Let \(T\in\mathbb R^{280\times3}\) represent identical Cartesian translation of all 43 spatial point masses, with zero on alpha and 150 auxiliary coordinates. Let \(M\succ0\) be the unchanged source diagonal configuration inertia matrix, \(M_{\rm total}=T^\top MT\) (equal to a scalar times \(I_3\)). Define
\[
P=I_{280}-T(T^\top MT)^{-1}T^\top M,\qquad
\Pi=\mathrm{diag}(P,P).
\]
Then \(P^2=P\), \(PT=0\), \(T^\top MP=0\), and \(\Pi\) is an orthogonal projector in the block kinetic mass metric \(\mathrm{diag}(M,M)\), even though P is not Euclidean-symmetric.

For the original internal-source model the exact identities
\[
KT=CT=0,\qquad T^\top K=T^\top C=0
\]
follow from translation invariance and balanced internal forces (the nonconservative damping-position derivative also has these symmetries). Hence \(\Pi J(u)=J(u)\Pi\) for every source reference state in its domain. The 6D center-of-mass sector has exact Green
\[
U_{\rm cm}(u,s)=\begin{pmatrix}I_3&(u-s)I_3\\0&I_3\end{pmatrix}
\]
and should be retained explicitly in the full state, including its kinetic momentum. The relative state evolves under a separate 554-dimensional projected Jacobian. This decomposition is **EXACT / CONDITIONAL on the unchanged free mechanics**, not an appeal to rigid-state deletion or an empirical result.

For a differentiable approximate reference p with residual \(r=p'-f(p)\), the projected perturbation equations formally separate into the CM shear with mass-projected residual \(r_{\rm cm}\), and a relative equation containing the projected residual, tangent Green and nonlinear remainder. The CM block error can be bounded with a polynomial-in-u convolution; the internal part still needs a verified force-range stability Green, Hessian/tube and residual enclosure. This algebra alone **does not** prove \(\delta_{\rm num}<0.01031\).

## Actually executed stiffness and damping diagnostics

[Isolated pinned NumPy/SciPy workflow #40717553809](https://github.com/ud-tetra/UD-Physics/actions/runs/40717553809) actually executed original frozen MountLoss references with DOP853 strict rtol5e−12/atol5e−15, and at each u=0,1,9.2,12.5,64.5,100 built exact-source \(K(u),C(u)\) through \`Linearization.matrices(y)\`. It formed mass-normalized \(M^{-1/2}KM^{-1/2}\) and \(M^{-1/2}CM^{-1/2}\), verified translation coupling, and examined the eigenvalues of the **symmetric part of K** on CM-free configurations (translation eigenvalues shifted away only to report internal minima).

| u | Limiting internal symmetric K minimum | Nominal internal symmetric K minimum |
|---|---:|---:|
| 0 | **−0.0962369393** | **−0.0965115462** |
| 1 | +0.0925546781 | +0.0935566669 |
| 9.2 | +0.1198168484 | +0.1226902912 |
| 12.5 | +0.0964303673 | +0.1017913084 |
| 64.5 | +0.0889944380 | +0.1158268186 |
| 100 | +0.0964511550 | +0.0738846483 |

The unshifted internal symmetric K is already indefinite at u=0. **This is a sampled numerical source diagnostic (not a certified eigenvalue enclosure) and does not imply actual dynamic instability.** The source initial velocity-dependent damping position derivative is zero to numerical tolerance, so initial K is nearly symmetric; the negative eigenvalue is not a floating artifact of the skew damping tangent. Nonnegative *nonlinear mechanical potential energy* does not imply its second derivative is nonnegative at every off-equilibrium pulse configuration.

At moving times, \(\|M^{-1/2}(K-K^\top)M^{-1/2}\|_F\) reaches about **0.00184** among the twelve sampled source states; K therefore cannot be treated as a symmetric conservative Hessian in general. The mass-normalized damping C is symmetric to \(\approx10^{-17}\) and its smallest eigenvalues are numerically zero, consistent with positive semidefinite relative viscous damping. All translation-leakage diagnostics from both K and C are below \(4.3\times10^{-14}\). These are NUMERICAL corroborations, not independent exact machine proofs or uniform time enclosures.

An illustrative **FIT / HYPOTHESIS** shifted internal quadratic form uses \(\mathrm{sym}(K)+\kappa MP\) with \(\kappa=0.11\), chosen *after* viewing the most negative sampled value ≈−0.09651. It would have a positive sampled mass-normalized minimum ≈0.01348845 at u0, with larger margins at the other sampled times. This does **NOT** prove all-time positivity, nor make \(\kappa\) a physical spring law. Its stability derivative contains nontrivial terms.

## Required shifted-energy calculation and failure of premature stability promotion

For the homogeneous linear relative dynamics \(q'=v,\ Mv'=-Kq-Cv\), with source \(K=K_{\rm sym}+K_{\rm skew}\) and time-dependent \(K_{\rm sym}\), define the tentative block norm energy
\[
\mathcal E_\kappa=\frac12 v^\top Mv
+\frac12 q^\top(K_{\rm sym}+\kappa MP)q
\quad (Pq=q,\ Pv=v).
\]
Only if the quadratic form is *uniformly positive* along the entire reference and within a declared error tube does it define a positive norm. Its exact derivative for homogeneous relative perturbations is
\[
\boxed{\mathcal E_\kappa'
=-v^\top Cv+v^\top(\kappa MP-K_{\rm skew})q
+\frac12 q^\top\dot K_{\rm sym}q.}
\]
For an external/projected residual forcing term g in the momentum equation add \(v^\top g\). This explicitly exposes three terms a stability estimate must bound: artificial shift, nonsymmetric tangent, and time-dependent symmetric stiffness. The present six-time spectra do not bound any of them uniformly, nor establish a certified fundamental matrix/Green gain. No claim of dissipation-based contraction or physical stability is made from the sampled positive C alone.

## Reproducibility and scientific status

Executable source: \`python3 experiments/icosahedral-projected-stability/projected_stability.py --out stability.json\`. The first isolated workflow [#40717152362](https://github.com/ud-tetra/UD-Physics/actions/runs/40717152362) FAILED because an initial constructor erroneously assumed that K was symmetric. The corrected version **preserves that failure in Git history**, removes the unjustified assertion and records the actual nonsymmetric tangent. Executed final workflow [#40717553809](https://github.com/ud-tetra/UD-Physics/actions/runs/40717553809) PASS.

Immutable [projected-001](../../artifacts/ico-projstable-20261028-gpt6-a1/projected-001/manifest.json) captures full source SHA256 \`fb51d73c10efe1d129d6b35153a7b26841fa6a22055c0481717a4a53f825bc19\` (4800 bytes) and the complete full 14343-byte output SHA256 \`1cfd06eb21f89e895ef31cc5a0c98d95a0f842c55b81e56b119df62ee0d152c9\`, verified against downloaded GitHub Actions artifact. No source mechanical laws, previous integrated results, or unrelated tasks are edited.

**Disposition:** EXACT/CONDITIONAL CM/internal invariant block established; NUMERICAL sampled internal K/C spectrum and antisymmetry quantified; FAILED direct unshifted positive stiffness-energy route; OPEN verified time-continuous positive shifted block norm and projected Green, interval step residual plus bootstrap, sampled true reference numerical error δ_num<0.01031, actual all180 housing phase nonlinear radius r=.036, 120 positive struts, 20 positive oriented volumes, and source u100 80% breathing. Ordinary unanchored reciprocal 3D spring/dashpot mechanics is the matched conventional null. External non-constructor review and physical experiment NOT_RUN, physical UD spacetime correspondence NOT_ESTABLISHED, and no mainline writeback.

**NEXT, priority 99/100:** derive a verified CM-exact/internal projected stability bound using a positive **shifted** mass-normalized norm with explicit \(\dot K_{\rm sym},K_{\rm skew}\) and \(\kappa\) terms, or a more efficient Lyapunov metric; obtain all-time spectral/derivative enclosures and source dense residual interval bounds, then attempt \(\delta_{\rm num}<0.01031\) without discarding rigid mechanical energy. Distinctly, all-phase nonlinear housing response remains a later gate.
