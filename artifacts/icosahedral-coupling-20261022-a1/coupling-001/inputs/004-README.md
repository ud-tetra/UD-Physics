# Icosahedral central coupling — v1.0

Evidence: **EXACT/CONDITIONAL**, **HYPOTHESIS/DESIGN**, **NUMERICAL**. Base revision: 754d615546612bbae574921120fabc414c0c4089. Continue the [exact icosahedral cone audit](../icosahedral-cone/README.md), preserving its unchanged-generator obstruction.

Three findings are kept distinct: a symmetry obstruction for oriented chain amplitudes; an additional local chain interaction with a chosen orientation; and a separate passive scalar-strain model with a geometric volume readout. No native chain/strain identification is made.

## 1. Sources, objects and locality

Use the audited centre cone with 13 vertices, 42 edges, 50 faces and 20 cells. Integer boundary matrices and exact $\mathbb Q(\sqrt5)$ coordinates are imported from the preserved constructor. Ascending simplex orientations, the real register $\mathbb R^{125}$, and chain metric $H=I$ define $A=\partial^T-\partial$.

Let $e_0$ be the central vertex seed, $Z$ the consistently oriented sum of all cells, and $S=\partial Z$ the exterior surface chain. Then $\|Z\|^2=\|S\|^2=20$ and $AZ=-S,AS=Z$.

For the new chain interaction, “local” means a nonzero matrix entry joins two simplices contained in one closed tetrahedron. It does not mean adjacent grades in the Hasse graph. The scalar mechanical model instead has an explicit central star and ordinary boundary-edge interactions.

The supplied historical ledger v0.39, Q139/Q144–145/Q151–152, keeps physical clock, breathing identification and constitutive selection open. The supplied CRL-2 amendment v1.0 remains a governance proposal, not an extra scientific premise or automatic registry adoption.

## 2. Two exact obstructions under declared hypotheses

First, changing only a differential and its metric adjoint cannot solve the vertex-to-cell problem. If $\partial^2=0$, the metric is block diagonal by degree, and

$$
A=\partial^\dagger-\partial,
\qquad
A^2=-(\partial^\dagger\partial+\partial\partial^\dagger),
$$

then $A^2$ preserves degree. Starting in $C_0$, even powers stay in $C_0$ and odd powers stay in $C_1$. The entire flow stays in $C_0\oplus C_1$. This holds without assuming icosahedral symmetry. A new interaction outside this pure differential/adjoint form, or a different state/readout, is necessary.

Second, let $J$ be spatial inversion acting on oriented simplicial chains. Exact vertex permutation and orientation signs give

$$
Je_0=e_0,\qquad JZ=-Z,\qquad JS=-S.
$$

For any fixed real linear generator $G$ commuting with $J$,

$$
\langle Z,e^{uG}e_0\rangle
=\langle JZ,Je^{uG}e_0\rangle
=-\langle Z,e^{uG}e_0\rangle=0,
$$

and the same holds for $S$. No locality assumption is needed for this obstruction. An inversion-equivariant nonlinear vector field with unique solutions likewise preserves an inversion-even initial state, so it cannot generate these odd components from that state alone.

These are scoped obstructions for the specified transformation law and initial state. A pseudoscalar actuator, orientation parameter, nonsymmetric initial perturbation, or scalar strain state changes the hypotheses.

The executable audit constructs all 120 isometries from images of a fixed ordered face, with 60 proper and 60 improper transformations, and checks the signed chain actions exactly.

## 3. A simplex-local, norm-conserving oriented chain coupling

Propose the additional operator

$$
W=Ze_0^T-e_0Z^T,\qquad A_\eta=A+\eta W,\qquad \eta\in\mathbb R.
$$

Its forty directed nonzero entries connect the central vertex to the twenty incident cells and back. It is skew, so the declared model energy $E_{\rm ch}=E_*\|c\|^2/2$ is conserved. This energy assignment uses the chosen chain metric; no physical energy calibration is implied.

For a signed chain action $R$ induced by a spatial isometry,

$$
RWR^T=\det(R)\,W.
$$

Thus a fixed nonzero $\eta$ preserves the proper rotations and selects an orientation. The full family is covariant if $\eta$ is transformed as a pseudoscalar. This is an added primitive, not a derivation of physical parity violation or geometric chirality.

Write the invariant five-dimensional state as

$$
c=a e_0+bU+jR_{\rm rad}+zZ+sS,
$$

where $U$ sums the twelve outer vertices and $R_{\rm rad}$ sums the twelve outward-oriented radial edges. The coordinate metric is $\operatorname{diag}(1,12,12,20,20)$. Exact full-matrix multiplication verifies

$$
\begin{aligned}
a'&=12j-20\eta z,& b'&=-j,&j'&=-a+b,\\
z'&=\eta a+s,&s'&=-z.
\end{aligned}
$$

The reduced characteristic polynomial is

$$
\lambda(\lambda^2+1)(\lambda^2+13+20\eta^2).
$$

For the unit heart seed, the frequency-one mode remains dark and the active cyclic space has dimension three. With $\Omega^2=13+20\eta^2$,

$$
\begin{aligned}
a(u)&=\frac{1+(\Omega^2-1)\cos(\Omega u)}{\Omega^2},&
b(u)&=\frac{1-\cos(\Omega u)}{\Omega^2},\\
j(u)&=-\frac{\sin(\Omega u)}{\Omega},&
z(u)&=\frac{\eta\sin(\Omega u)}{\Omega},&
s(u)&=-\frac{\eta[1-\cos(\Omega u)]}{\Omega^2}.
\end{aligned}
$$

The twenty oriented cell amplitudes are coherent. Their combined cell/surface share of this model energy is $20(z^2+s^2)$, with exact maximum

$$
\max_u\frac{E_{\rm cells}+E_{\rm surface}}{E_{\rm initial}}
=\frac{20\eta^2}{12+20\eta^2}.
$$

To derive the maximum, set $y=1-\cos(\Omega u)\in[0,2]$. The energy share is $20\eta^2[2y/\Omega^2-(\Omega^2-1)y^2/\Omega^4]$, maximized at $y=\Omega^2/(\Omega^2-1)$.

Illustrative $\eta=1/2$ gives $\Omega^2=18$ and maximum $5/17\approx29.41\%$. This is a model-energy fraction under the declared energy, not an information fraction or physical transfer measurement. It does not supply geometric volume motion by itself.

## 4. A separate passive scalar-strain realization

Now change the state explicitly. Let $\alpha$ be a scalar internal preferred radial strain of the central actuator, not the central point's displacement. Let $q_i$, $i=1,\ldots,12$, be scalar shell strains. Ideal passive radial guides constrain the actual outer positions to

$$
X_i=(1+q_i)r_i,
$$

where the reference rays form the regular icosahedron with edge length $\ell_0$. These scalar strains are permuted without orientation signs under all spatial isometries.

Let $e_{ij}(q)=|X_i-X_j|/\ell_0-1$ for each of the thirty boundary edges. Propose dimensionless model energy

$$
\begin{aligned}
T&=\frac12(\alpha'^2+\sum_iq_i'^2),\\
U&=\frac12\alpha^2+\frac12\sum_iq_i^2
+\frac g2\sum_i(q_i-\alpha)^2
+\frac k2\sum_{\langle ij\rangle}e_{ij}(q)^2,
\qquad g>0,\ k\ge0.
\end{aligned}
$$

All inertia/pinning coefficients have been chosen as one. The last term represents ordinary spatial edge-extension springs, not the earlier protected difference-damping channel. The spoke preferred-length coupling, guides, positive pins and internal actuator are assumed constitutive ingredients. The internal coordinate $\alpha$ is dynamical and receives the spring reaction forces; its preferred-length change is not an externally prescribed control signal.

Use the Euler–Lagrange equations $x''=-\nabla U$ for $x=(\alpha,q)$. The state space has 26 position/velocity coordinates. Every interaction is local to a spoke or boundary edge, the potential is positive definite at equilibrium, and

$$
\frac{d}{du}(T+U)=x'^T(x''+\nabla U)=0.
$$

All 120 spatial symmetries are retained. The invariance follows from permuting identical scalar spoke/pin terms and Euclidean edge lengths. Exact tangent-stiffness checks and nonlinear force checks verify this separately from the oriented chain model.

With $\alpha(0)=1/10$, all $q_i(0)=0$, and all velocities zero, the initial energy at $g=1$ is $13/200$. Since $U\ge\sum_iq_i^2/2$, every $|q_i|\le\sqrt{13/100}<1$ for all unforced times. The positive radial geometry is therefore protected by energy, not only checked during simulation.

## 5. Exact collective manifold and geometric volume readout

For $q_i=b$, every edge length is $\ell_0(1+b)$. Also

$$
\left.\frac{\partial e_{ij}}{\partial q_i}\right|_{q=b\mathbf1}=\frac12.
$$

Each vertex has five edges. The uniform manifold is therefore exactly invariant even for the nonlinear distance-based potential, with equations

$$
\alpha''+(1+12g)\alpha-12gb=0,\qquad
b''+(1+g+5k/2)b-g\alpha=0.
$$

Its mass metric is $\operatorname{diag}(1,12)$; the nonsymmetric equation matrix is self-adjoint in that metric. For the illustrative design $g=1,k=2/5$:

$$
\alpha''+13\alpha-12b=0,\qquad b''+3b-\alpha=0,
\qquad \lambda_\pm=\omega_\pm^2=8\pm\sqrt{37}.
$$

The edge coefficient $2/5$ was selected to make its uniform restoring increment $5k/2$ equal to one. It is a disclosed simplifying design choice, not a measured or source-derived constant. For $\alpha(0)=A_0$, the exact shell strain is

$$
b(u)=\frac{A_0}{2\sqrt{37}}
\left[\cos(\sqrt{8-\sqrt{37}}\,u)-\cos(\sqrt{8+\sqrt{37}}\,u)\right].
$$

In particular $b''(0)=gA_0\ne0$. The decoupled baseline $g=0$ leaves the initially stationary shell stationary.

The volume readout is geometric and exact:

$$
V_C(q)=V_{C,0}\prod_{i\in{\rm outer\ face}(C)}(1+q_i),
\qquad
V_C(b)=V_{C,0}(1+b)^3,
\qquad
\frac{V_{\rm total}}{V_0}=(1+b)^3.
$$

All twenty cells have the same fractional volume change on this manifold. Their reference volume remains $(3+\sqrt5)\ell_0^3/48$ each. The model now supplies an energy-consistent central source and a genuine geometric volume change within the assumed constrained mechanics.

For $A_0=1/10$, $|b|\le1/(10\sqrt{37})\approx0.0164399$. The numerical run over $u=0\ldots100$ observes total fractional volume changes from $-4.8508\%$ to $+5.0133\%$. These sampled extrema are not asserted to be the exact all-time extrema.

## 6. Contrast modes and verification

At equilibrium, ordinary edge extension satisfies $e_{ij}=(q_i+q_j)/2+O(q^2)$, so the shell tangent contribution is the signless vertex Laplacian $k(5I+A_I)/4$, where $A_I$ is the icosahedral vertex adjacency. It responds to common breathing, as ordinary springs should.

For the selected parameters the eleven shell-contrast squared frequencies are

$$
\left(\frac52-\frac{\sqrt5}{10}\right)^{[3]},\quad
\left(\frac{12}{5}\right)^{[5]},\quad
\left(\frac52+\frac{\sqrt5}{10}\right)^{[3]}.
$$

Together with $\lambda_\pm$, all thirteen squared frequencies are positive. An exact integer annihilation/moment certificate on the scaled tangent matrix $10K$ establishes these multiplicities. Angular/shear coordinates are constrained away, so this is not a full three-dimensional material stability theorem.

The computation checks:

- All 120 exact signed chain symmetry actions, inversion parity, forty-entry coupling support and the invariant five-dimensional equations.
- Exact rational weighted-skew and cyclic identities for $\eta=0,1/4,1/2,1$, alongside the general algebraic derivation above.
- Analytic chain trajectories against a matrix exponential; largest observed discrepancy $9.66\times10^{-14}$.
- Full nonlinear 26-state DOP853 integration against the exact two-coordinate collective solution: state discrepancy $4.19\times10^{-11}$.
- Relative model-energy error $1.68\times10^{-10}$; geometric volume discrepancy $1.15\times10^{-11}$.
- Nonuniform potential/force finite-difference check: error $7.63\times10^{-12}$; nonlinear spatial equivariance discrepancy $2.23\times10^{-16}$.

NumPy 2.3.5 and SciPy 1.17.0, float64, $u\in[0,100]$, 4001 samples, DOP853 tolerances relative $10^{-11}$ and absolute $10^{-13}$. These are constructor calculations with distinct exact/numerical methods, not non-constructor review or empirical replication.

An initial matrix-exponential check used an overstrict absolute tolerance $3\times10^{-14}$ and stopped at a discrepancy of order $10^{-13}$. Rechecking in an orthonormal coordinate basis confirmed the same scale. The final numerical tolerance is $10^{-12}$ and the actual error is retained; no exact identity or scientific acceptance criterion was changed.

![Two distinct coupling constructions](../../artifacts/icosahedral-coupling-20261022-a1/coupling-001/files/coupling-comparison.png)

## 7. Reproduction, units and unresolved selection

From repository root, with NumPy, SciPy and Matplotlib installed:

    OPENBLAS_NUM_THREADS=1 python3 experiments/icosahedral-coupling/analyze.py --out /tmp/ud-icosa-coupling
    python3 experiments/icosahedral-coupling/draw.py --data /tmp/ud-icosa-coupling/trajectories.csv --out /tmp/ud-icosa-coupling/coupling-comparison.png
    python3 scripts/validate.py
    python3 -m unittest discover -s tests -v

The [run manifest](../../artifacts/icosahedral-coupling-20261022-a1/coupling-001/manifest.json) captures code, the imported constructor, this report, receipt, data and figure. Reproduce in repository layout because the prior constructor is imported deliberately.

For mechanics, set physical time $t=t_0u$ and energy $E_{\rm phys}=E_*E$. Generalized inertias then scale as $E_*t_0^2$, and actual radial point masses as $E_*t_0^2/R^2$. The scales and apparatus have not been calibrated. The chain energy and mechanical energy belong to different models and are not equated.

The passive scalar model provides prepared finite-energy breathing; it does not provide sustained power, a microscopic UD constitutive source, or an automatic map from $Z/S$ amplitudes to material strain. The full-inversion chain obstruction remains valid under its original hypotheses.

Next discriminant: derive a passive implementation of the scalar preferred-radius coupling and relax the ideal radial-guide assumption, testing angular/shear stability and total-volume coherence under small imperfections.
