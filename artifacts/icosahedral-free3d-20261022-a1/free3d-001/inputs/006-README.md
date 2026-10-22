# Icosahedral breathing without radial guides — v1.0

Evidence: **EXACT/CONDITIONAL**, **NUMERICAL**, **HYPOTHESIS/DESIGN**. Base revision: fbf35ff97a148b42dc57322c71bd905aec2adff5. Continue the [passive scalar-strain candidate](../icosahedral-coupling/README.md). Its oriented-chain obstruction remains a separate result; this mechanical model is not a native chain-amplitude identification.

## 1. Release both shell and centre coordinates

Let $C\in\mathbb R^3$ be the central point, $X_i\in\mathbb R^3$ the twelve shell points, and $\alpha\in\mathbb R$ the central internal preferred-radius coordinate. There are 40 configuration coordinates and 80 phase variables. All thirteen points can translate and rotate; no radial guides or fixed spatial anchor remain.

Use the regular icosahedral reference rays $r_i$, edge length $\ell_0=1$, and radius $R^2=(5+\sqrt5)/8$. Define

$$
s_i=\frac{|X_i-C|}{R}-1,\qquad
e_{ij}=\frac{|X_i-X_j|}{\ell_0}-1.
$$

The declared model energy is

$$
\begin{aligned}
T&=\frac12\alpha'^2+\frac1{2R^2}
\left(m_C|C'|^2+\sum_i m_i|X_i'|^2\right),\\
U&=\frac12\alpha^2+\frac12\sum_i s_i^2
+\frac12\sum_i g_i(s_i-\alpha)^2
+\frac12\sum_{\langle ij\rangle}k_{ij}e_{ij}^2.
\end{aligned}
$$

The default is $m_C=m_i=g_i=1$, $k_{ij}=2/5$. The internal coordinate has unit inertia. These are illustrative inherited coefficients; the edge value was chosen in the preceding work for a simple uniform restoring increment, not measured or independently predicted.

Euler–Lagrange dynamics are $M x''=-\nabla U$, with constant positive $M=\operatorname{diag}(1,m_C/R^2,m_C/R^2,m_C/R^2,\ldots)$ in the order $(\alpha,C,X_1,\ldots,X_{12})$.

Every potential term acts on the central internal coordinate, one centre-to-shell distance, or one actual shell edge. Central and shell reaction forces are both included. This is a local positive-energy mechanical construction with a scalar preferred-radius element; the microscopic/material origin of that element remains assumed.

## 2. Conservation, exact rigidity and equilibrium stability

Energy, linear momentum, and angular momentum are conserved:

$$
E'=0,\quad
P=\frac1{R^2}\left(m_CC'+\sum_i m_iX_i'\right),\quad
L=\frac1{R^2}\left(m_CC\times C'+\sum_i m_iX_i\times X_i'\right).
$$

Length potentials are invariant under simultaneous Euclidean motions, and $\alpha$ is a scalar. All proper/improper icosahedral permutations are also symmetries for the identical default properties. Label-dependent positive properties can break icosahedral permutation symmetry while preserving Euclidean invariance.

At the reference equilibrium $\alpha=0,C=0,X_i=r_i$, every spring extension vanishes. The quadratic energy is a positive weighted sum of squares of linearized constraints. A sufficient independent constraint set consists of one internal pin, twelve radial distances and thirty shell-edge lengths.

Exact row reduction over $\mathbb Q(\sqrt5)$ gives:

| Calculation | Exact result |
| --- | --- |
| Shell edge-rigidity rank | 30 |
| Full 43-row constraint rank in 40 coordinates | 34 |
| Kernel dimension | 6 |
| Kernel | Three translations and three rotations |
| Restoring directions | 34 = two collective + 32 shape directions |

The twelve extra preferred-radius spring rows are linear combinations of the internal-pin/radial rows, so they do not change this rank. The six Euclidean null vectors are checked exactly and are independent. There are no additional infinitesimal angular/shear mechanisms.

Consequently, for arbitrary strictly positive point masses, spokes and edge stiffnesses in this model, the stress-free reference equilibrium has a positive Hessian on the complement of rigid motions. The positive energy gives **local orbital Lyapunov stability modulo translations and rotations**: a sufficiently small rest-state perturbation stays close to the equilibrium orbit. This is not a global rigidity theorem or an all-time stability theorem for a nonzero breathing orbit.

For the default parameters, numerical mass-normalized eigenvalues give six zeros and 34 positives, with smallest positive squared frequency approximately $0.3618034$.

## 3. The exact breathing manifold survives

With equal properties, the unconstrained system has the exact invariant solution

$$
C=0,\qquad X_i=(1+b)r_i.
$$

The net force on the free centre vanishes by the icosahedral sum of rays. The shell forces are radial on this manifold without imposed guides. The collective mass matrix remains $\operatorname{diag}(1,12)$ and the equations are unchanged:

$$
\alpha''+13\alpha-12b=0,\qquad
b''+3b-\alpha=0,\qquad
\omega_\pm^2=8\pm\sqrt{37}.
$$

For $\alpha(0)=A_0$ and all other strains/velocities initially zero, let $\lambda_\pm=8\pm\sqrt{37}$. Then

$$
\begin{aligned}
b(u)&=\frac{A_0}{2\sqrt{37}}
\left[\cos(\sqrt{\lambda_-}u)-\cos(\sqrt{\lambda_+}u)\right],\\
\alpha(u)&=\frac{A_0}{2\sqrt{37}}
\left[(3-\lambda_-)\cos(\sqrt{\lambda_-}u)
+(\lambda_+-3)\cos(\sqrt{\lambda_+}u)\right].
\end{aligned}
$$

Because the weights in $\alpha$ are nonnegative and sum to one, $|\alpha|\le |A_0|$; also $|b|\le |A_0|/\sqrt{37}$.

The full 80-state nonlinear integration at $A_0=1/10$ agrees with this solution to $9.06\times10^{-10}$ over $u=0\ldots100$. Its nonuniform cell-volume signal is approximately $10^{-13}$, consistent with exact symmetric coherence.

## 4. An exact all-phase instantaneous stiffness certificate

Equilibrium stability alone does not test the moving state. Let $K_0$ be the physical-coordinate equilibrium Hessian. Define positive semidefinite matrices $T_r,T_e$ by the transverse Hessians of the radial and edge distances at the reference configuration. If $D_{iC}$ maps a displacement to $\delta X_i-\delta C$, and $D_{ij}$ to $\delta X_i-\delta X_j$, then

$$
T_r=\sum_i D_{iC}^T\frac{I-n_in_i^T}{R^2}D_{iC},\qquad
T_e=\sum_{\langle ij\rangle}k_{ij}D_{ij}^T
\frac{I-n_{ij}n_{ij}^T}{\ell_0^2}D_{ij}.
$$

On the symmetric breathing motion, with default $g=1$ and $k=2/5$, the exact Hessian is

$$
K(u)=K_0+\frac{2b-\alpha}{1+b}T_r+\frac{b}{1+b}T_e.
$$

The terms involving transverse projectors include spring prestress; omitting them would miss angular effects. The formula is separately checked by finite differences of the nonlinear forces at nonzero strains.

For $|A_0|\le1/10$, $\sqrt{37}>6$ gives $|b|<1/60$, $|\alpha|\le1/10$, hence

$$
\frac{2b-\alpha}{1+b}\ge-\frac8{59},\qquad
\frac{b}{1+b}\ge-\frac1{59}.
$$

Let $P_{\rm rig}$ be the mass-orthogonal projector onto the six reference rigid motions. Exact translation/rotation mass Grams are $(13/R^2)I_3$ and $8I_3$, with zero cross block. The executable certificate proves the matrix

$$
K_0-\frac8{59}T_r-\frac1{59}T_e+MP_{\rm rig}-\frac1{10}M
$$

is positive definite by exact $\mathbb Q(\sqrt5)$ LDL factorization: all forty pivots are positive, and the factorization is reconstructed entry by entry. Therefore every displacement mass-orthogonal to rigid motions satisfies, throughout this entire symmetric family,

$$
\delta x^T K(u)\delta x\ge\frac1{10}\delta x^TM\delta x.
$$

The bound $1/10$ is a conservative computational certificate chosen after inspecting the numerical comparison gap, not an independent prediction or physical threshold. The certificate and exact pivots are preserved.

Thus no instantaneous nonrigid buckling occurs along this family. **Positive time-dependent stiffness does not by itself establish bounded parametric evolution.** Rigid rotations can also have nonzero instantaneous Hessian curvature away from equilibrium, even though a rotated full trajectory is equivalent; they are removed from this shape test.

## 5. Finite-time transverse dynamics

The two collective and six rigid directions span a fixed invariant subspace along the homothetic solution. Exact rigid identities and the collective equations establish this; numerical excluded-to-shape leakage is below $2.80\times10^{-15}$. Their mass-orthogonal complement has 32 coordinates, including angular/shear motion and relative centre motion.

For a mass-normalized orthonormal basis $Q$ of this complement, integrate

$$
\eta''+H_T(u)\eta=0,\qquad H_T=Q^TM^{-1/2}K(u)M^{-1/2}Q.
$$

Set $H_{\rm ref}=Q^TM^{-1/2}K_0M^{-1/2}Q$ and use the reference energy-amplitude norm

$$
\|w\|^2=\eta^TH_{\rm ref}\eta+\|\eta'\|^2.
$$

Here the reference matrix is the stress-free equilibrium stiffness, not the prestressed initial breathing Hessian. The zero-amplitude evolution preserves this norm. A propagated operator's largest singular value measures the greatest amplification of this reference amplitude over the chosen interval.

| Endpoint $u$ | Largest reference-energy amplitude gain |
| --- | --- |
| 20 | 1.2811 |
| 50 | 1.0994 |
| 100 | 1.1124 |
| 200 | 1.1922 |
| 400 | 1.2670 |

These are five endpoint observations, not an asserted bound at every intervening time. The gain at 400 corresponds to about $1.61$ in reference perturbation-energy ratio, not creation of total model energy. There is no sustained growth trend across these samples, but they do not prove all-time stability or rule out slower instability.

The breathing contains two incommensurate frequencies, so no single-period Floquet claim is made. The relative symplectic residual at the five endpoints is at most $1.41\times10^{-9}$.

## 6. Nonlinear imperfections and two distinct volume readouts

For a cell with outer face $(i,j,k)$, use its consistent orientation sign $\sigma_C$:

$$
V_C=\frac{\sigma_C}{6}
\det(X_i-C,X_j-C,X_k-C).
$$

The total $\sum_C V_C$ is exactly independent of the chosen interior cone centre $C$ for a fixed closed oriented shell: its centre-dependent edge terms cancel. Thus centre motion can repartition cell volumes without changing total volume.

For fractional volume signals $y_C=V_C/V_{C,0}-1$, define

$$
L_V=\sqrt{\frac{\int\|P_{20}y\|^2du}{\int\|y\|^2du}},\qquad
R_V=\frac{\operatorname{RMS}(\bar y)_{\rm probe}}
{\operatorname{RMS}(\bar y)_{\rm symmetric}}.
$$

These are signal-amplitude ratios, not energy fractions. Repeat the partition using the geometric mean of shell vertices as cone centre to separate shell deformation from hub-relative repartition. Its signal denominator differs, so the two leakage ratios are not additive components.

Sixteen seeded property probes vary 55 quantities independently within the indicated tolerance: thirteen point masses, twelve spoke coefficients and thirty edge stiffnesses. Eight probes per tolerance, seed 9023, all start with the same $\alpha_0=1/10$ and zero velocities. They are exploratory points, not all corners, statistical confidence intervals or extrema over the continuous parameter box.

| Property tolerance | Maximum moving-hub $L_V$ | Maximum shell-centre $L_V$ | Minimum mean-volume RMS retained | Maximum fitted shell-shape error |
| --- | --- | --- | --- | --- |
| $\pm1\%$ | 3.11% | 1.66% | 99.61% | 0.0614% |
| $\pm5\%$ | 18.62% | 8.84% | 97.83% | 0.2875% |

Extrema can occur in different probes. The last column is the RMS positional residual after fitting a translation, proper rotation and uniform scale, divided by the reference RMS radius. It is not a fraction of energy or the oscillatory volume signal.

There are also three target-informed initial-shape probes: take the leading right singular vector of the exposed $u=100$ variational propagator, with reference amplitude $10^{-6},10^{-5},10^{-4}$. Remove total linear/angular momentum from the perturbed initial state. The observed moving-hub $L_V$ is respectively $0.00109\%,0.01090\%,0.10902\%$, with mean-volume RMS essentially unchanged. This is an adversarial design check using exposed calculations, not an independent prediction test.

All sampled cell volumes remain positive; the smallest observed ratio is above 0.9385. Supporting-halfspace checks at every tenth output sample retain a convex shell to numerical precision. Exact independence of total volume from the cone centre is numerically cross-checked to the declared tolerance.

No global no-inversion or no-self-intersection claim follows from energy alone. The inherited positive radial and edge energies do prevent adjacent length collapse at the declared energy/property ranges, but a cell determinant needs its own geometric check.

![Free3D mode and imperfection summary](../../artifacts/icosahedral-free3d-20261022-a1/free3d-001/files/free3d-summary.png)

## 7. Numerical checks and reproduction

- Full nonlinear dynamics: DOP853, relative tolerance $10^{-10}$, absolute $10^{-12}$, $u=0\ldots100$, 2001 output samples. Largest baseline relative energy error $6.07\times10^{-9}$.
- Variational dynamics: 64 phase coordinates, DOP853 tolerances $2\times10^{-10}$ and $2\times10^{-12}$, through $u=400$. Symplectic checks use the transformed phase-space form.
- The largest moving-hub leakage probe at each property tolerance is repeated with 4001 outputs and nonlinear tolerances $2\times10^{-12}$ and $2\times10^{-14}$. Leakage changes by at most $6.90\times10^{-7}$; refined energy errors are below $9.51\times10^{-11}$.
- Independent force differentiation checks the equilibrium Hessian and the prestressed Hessian; the latter maximum discrepancy is $3.90\times10^{-10}$.
- Exact rank, null vectors, rigid mass Grams, LDL pivots and factorization reconstruction use $\mathbb Q(\sqrt5)$, not floating-point rank thresholds.

All work is constructor verification, with exact algebra and distinct numerical methods. It is not non-constructor peer review, empirical replication, or a physical bridge test. NumPy/SciPy versions and run parameters are in the captured summary.

From repository root, with NumPy, SciPy and Matplotlib installed:

    OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-free3d/analyze.py --out /tmp/ud-free3d
    OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-free3d/certificate.py --out /tmp/ud-free3d
    python3 experiments/icosahedral-free3d/draw.py --summary /tmp/ud-free3d/summary.json --out /tmp/ud-free3d/free3d-summary.png
    python3 scripts/validate.py
    python3 -m unittest discover -s tests -v

The [manifest](../../artifacts/icosahedral-free3d-20261022-a1/free3d-001/manifest.json) captures the new code, imported exact constructor, this report, mathematical receipt, data, exact stiffness certificate and figure. The augmented exact rigid check initially encountered an integer/field coercion programming error; it was corrected before the successful final certificate run.

Physical time/energy scales remain $t_0,E_*$, with $u=t/t_0$ and point masses $E_*t_0^2m_i/R^2$. The central scalar element and its parameters remain constitutive assumptions. The supplied historical ledger v0.39 Q139/Q144–145/Q151–152 leaves their native UD selection open; the supplied governance amendment is a proposal, not evidence for these mechanics.

Next discriminant: derive a robust amplitude/damping operating envelope using realizable passive spoke/edge losses, explicitly measuring the cost to common breathing as well as suppression of shape and hub-relative motion.
