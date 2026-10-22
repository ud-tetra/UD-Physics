# UD Discovery: 4D apex to 3D icosahedral shell-volume response

STATUS: EXACT / CONDITIONAL / NUMERICAL; branch-only hypothesis; not physical validation.

Session `icosa4dvol-20261022-gpt6-c7d2`; source main `92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`; task `icosahedral-4d-volume-20261022`; claim `23b04a0533df0bd6b26f0c7fc9f94a6864400cea`.

## Question

Does a fourth Euclidean coordinate of the icosahedral apex induce 3D shell breathing in an explicit passive model? Is its response distinguishable from a comparable 3D mechanical model?

## Typed model, assumptions and source exposure

A regular icosahedron has 12 vertices \(x_i^0\in\mathbb R^3\), 30 edges, circumradius \(a\rho\), with \(\rho^2=(5+\sqrt5)/8\). Shell positions are \((s x_i^0,0)\in\mathbb R^4\); the apex is \((0,0,0,az)\). Shell motion is homothetic for the two-coordinate response. The full 40-DOF check allows independent shell xyz displacements and apex xyz/z displacements while constraining the shell to the hyperplane w=0. Euclidean signature ++++; physical time is an **independent** Newtonian evolution parameter. The 4D elevation \(\eta=\sqrt{(3-\sqrt5)/8}=1/(2\varphi)\) comes from the previously exposed target that radial and exterior edges have equal length a.

Assumed forces: 12 independent radial extension springs stiffness \(k_r>0\) with rest length a; 30 exterior-edge springs stiffness \(k_e>0\) with rest length a. Each shell vertex mass \(m_s>0\); apex mass \(m_a>0\). No separate UD-native constitutive law is asserted. The parameters \(a=k_r=k_e=m_s=m_a=1\) and viscous \(C=0.06 M\) are illustrative **choices**, not physical fits. No empirical target was optimized; source-selected equal-edge criterion remains disclosed. No formula search beyond specified models.

Use dimensionless configurations \(q=(s,z)\). Energy and kinetic form:

\[
U(q)=a^2[6k_r(\sqrt{\rho^2s^2+z^2}-1)^2+15k_e(s-1)^2],\quad
T=(a^2/2)(12m_s\rho^2\dot s^2+m_a\dot z^2).
\]

For physical generalized force \(F_z\) conjugate to dimensionless z (units of energy), the equation is \(a^2 M\ddot q+a^2\nabla_q(U/a^2)+ C_{phys}\dot q=(0,F_z)\). Set a=1 for the numerical ODE, with its time unit \(\sqrt{m_a/k_r}\) when masses and stiffness are calibrated. The 3D shell-volume readout is \(V_3=(5(3+\sqrt5)/12)a^3s^3\).

## EXACT / CONDITIONAL results

At \(q_*=(1,\eta)\), the dimensionless Hessian and mass metric are

\[
K=\begin{pmatrix}12k_r\rho^4+30k_e &12k_r\rho^2\eta\\12k_r\rho^2\eta&12k_r\eta^2\end{pmatrix},\qquad
M=\operatorname{diag}(12m_s\rho^2,m_a).
\]

\(\det K=360k_rk_e\eta^2>0\), and \(K_{zz}=12k_r\eta^2>0\), giving stable uniform breathing/apex directions for positive spring constants. The **static** generalized force-to-volume law is

\[
\frac{\delta V_3}{V_3}=-\frac{\rho^2}{10k_e\eta}\frac{F_z}{a^2}+O(F_z^2).
\]

Small-signal dynamic transfer for \(f_z=F_z/a^2\), with \(\lambda=\omega^2\), is \(\delta V_3/V_3=-3K_{sz} f_z/\det(K-\omega^2 M)\) (undamped and away from resonances). In the example, eigenfrequencies are **0.886724725** and **2.007002196** in normalized angular-frequency units; static gain **-0.292705098312**.

## Full-coordinate rigidity (40 DOF)

Release the uniform shell restriction: 12 independent vertices in 3D (36), apex xyz (3), apex fourth coordinate (1). At the rest-length equilibrium, construct the **42-by-40 spring-length Jacobian J** (30 shell edges and 12 radial connections), and \(H=J^TJ\) for equal unit spring stiffnesses. Numerical singular-value rank = **34**, nullity **6**, smallest positive singular value **0.886724725**. Six explicitly verified null vectors are common xyz translations and 3D rigid rotations; the two-mode sector has invariance residual 4.441e-16.

An EXACT structural argument for rank34 uses the infinitesimal rigidity of the strictly convex triangulated icosahedral shell (Dehn's theorem, reference below): shell-edge J rank30, leaving six rigid motions. Factoring out these rigid motions and fixing shell motion, the 12 radial rows constrain the 4 centre components through [\(-x_i,\eta\)]; \(\sum_i x_i=0\), \(\sum_i x_ix_i^T=4\rho^2 I\), \(\eta\ne0\), hence this 12-by-4 block has rank4. Thus full rank 30+4=34. This is linear local stability **modulo six rigid motions** for the specific spring constraints, not a global nonlinear rigidity or 4D spacetime statement.

Rigidity reference: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F29517D8BDA42813D2E31CEE827B1CC8/S0008414X00026274a.pdf/infinitesimal-rigidity-of-convex-polyhedra-through-the-second-derivative-of-the-hilberteinstein-functional.pdf (Theorem 3.4, Legendre–Cauchy–Dehn).

## NUMERICAL pulse experiment and baseline

Force pulses \(f_z(t)=A\exp[-(t-8)^2/(2(1.5)^2)]\) with A=0.01,0.02,0.08, and \(C=0.06 M\). Solve in dimensionless time 0–70 with DOP853, rtol=1e-11, atol=1e-13. Peak fractional shell-volume changes:

| Amplitude | 4D apex + shell | 3D axial-centre + shell |
|---:|---:|---:|
| 0.01 | 0.509109% | 0.000452% |
| 0.02 | 0.995215% | 0.001807% |
| 0.08 | 3.523392% | 0.028919% |

At A doubled from 0.01 to 0.02, the first peak ratio is 1.954819 versus 4.000056 for the 3D axial-centre baseline: leading linear vs quadratic dependence, as predicted by symmetry. The 3D null must first relax its shell to \(s_0=1.013672463777\) and has **exactly zero linear shell-volume response** to axial apex forcing because shell symmetry makes its cross-Hessian vanish. Each model is compared relative to its own equilibrium shell volume.

**NON-IDENTIFIABILITY:** a different, conventional **3D two-coordinate internal lever** with linear energy \(U_{null}=15k_e x^2+6k_r(\rho^2x+\eta y)^2\) and the same generalized mass/damping has exactly the same K and full linear transfer. Therefore the nonzero 4D response is **not an independent discriminator against all 3D physics**. The 3D axial-center null only tests a particular geometrically symmetric alternative.

## Reproduction and checks

Run `python3 audit.py` with Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0. The script asserts exact icosahedral vertex/edge/face counts, exact symbolic Hessian, determinant, isotropy and symmetric transfer, direct vertex-spring energy matching the reduced law, finite-difference gradients, generalized eigenpairs, 40-coordinate Jacobian rank and six rigid directions, invariant reduction, and numerical pulse energy balance. Residuals are recorded in `results.json`. Time series are in `pulse_series.csv`.

Code self-checks are constructor checks, not independent experiment or external replication. Repository `scripts/validate.py` and full test suite: NOT_RUN in the connector-only checkout; a local isolated script ran successfully instead. No experimental measurements, no trained fit, no material prototype. Exact equal-edge geometry and assumed 4D inertia are not derived by native UD dynamics.

## Failure, limits, next discriminant

- **FAILED as unique 4D signal:** the 3D lever null exactly reproduces the entire linear two-port force-to-volume transfer. A quantitative physical bridge needs some discriminatory nonlinearity, symmetry/selection law, or externally restricted mechanism.
- External shell restricted to w=0; 4D shell rotations/tilts and extra material degrees of freedom are not included.
- With positive damping, numerical dynamics dissipate energy, but finite pulses cannot certify uniform robustness.
- Infinite linear undamped response at resonance is a mathematical idealization, not a bounded driven response.
- **Next priority 96/100:** contrast measured nonlinearity, resonances and mode selection of the 4D spring realization against an equally flexible 3D linkage null, while checking whether any native UD rule constrains the realizable coupling.