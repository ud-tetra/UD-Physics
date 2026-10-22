# Nonlinear housing-energy domain and volume bounds v1.0

**EXACT / CONDITIONAL**, with separate **NUMERICAL** constructor checks. Base `ef5e2d8f9e0cc5354086a2a3373f6c07600f6dcd`; unchanged [joint-window law and budget](../icosahedral-jointwindow/README.md), [protocol](PROTOCOL.md), [results](RESULTS.md), [candidate and receipt](../../candidates/icosahedral-nonlineartube/candidate.json).

## 1. The two preparations have different energy budgets

The real mechanical state has 280 configuration coordinates, 560 phase variables and one heat accumulator: scalar alpha, 13 primary points X, 150 device coordinates z and 30 housings H. Each housing is spring-mounted to A_e=(X_i+X_j)/2 and has four current-axis viscous paths to i,j and the two opposite vertices of the adjacent faces. All reactions and masses remain included. Length, energy and continuous time u use uncalibrated ell0,E_*,t0 units. Reference geometry lies in Q(sqrt5), R²=(5+sqrt5)/8. No modular register is involved.

The qualified box is beta in[1/200,1/20], Omega=10, housing weights w in[9/10,11/10] of mean1, primary masses/g in[19/20,21/20], k in[19/50,21/50], reciprocal gains in[.99,1.01], c_f in[0,.001]. Nonnegative loss, including nu>=0, suffices for the proofs below. The selected joint-window nu[.04,.05] is a subset.

Keep these preparations separate:

| Preparation | Initial primary/device state | Total initial mechanical energy |
| --- | --- | --- |
| Housing-only ringdown | alpha=0, primary at reference/rest, z=zdot=0 | E_h<=E_p/40000<=17/10^7 |
| Heart pulse plus housings | alpha=1/10, same primary/device state | E_p+E_h<=680017/10^7 |

Here E_p=(1+sum g_i)/200 is the *reference* pulse energy even when the actual preparation has alpha=0. Every housing displacement/velocity combination in its energy ball is allowed, including nonzero total spatial P,L. No equilibrium rigid kinetic energy is discarded.

The parent identity E'=-P_loss<=0 holds on the positive-length domain. For each current primary spoke s_i=|X_i-C|/R-1 and shell edge e_ij=|X_i-X_j|-1, positive storage gives

\[
 \tfrac12\left(\sum s_i^2+k_{\min}\sum e_{ij}^2\right)\le E,
 \qquad \tfrac12 k_{h,e}|H_e-A_e|^2\le E.
\]

Since R²<1, each housing inertia is >9/5000 and its mount stiffness is >9/50. These are conservative exact lower bounds, not fitted coefficients.

## 2. Housing-only: all-phase, all-time positive strut lengths

Set E<=17/10^7. Exact fraction comparisons in `bounds.py` imply

\[
 |s_i|<\sigma=1/500,\quad |e_{ij}|<\epsilon=3/1000,
 \quad |H_e-A_e|<\delta=1/200.
\]

For either endpoint anchor a=i,j,

\[
 |H_e-X_a|\ge\tfrac12|X_i-X_j|-\delta
 >\frac{1-\epsilon}{2}-\delta=\frac{987}{2000}.
\]

For an opposite anchor k, the triangle ijk is a boundary face. The exact median identity gives

\[
 |X_k-A_e|^2=\frac{|X_k-X_i|^2+|X_k-X_j|^2}{2}
             -\frac{|X_i-X_j|^2}{4}
 >(1-\epsilon)^2-\frac{(1+\epsilon)^2}{4}>\left(\frac45\right)^2.
\]

Thus its strut length is >4/5-delta=159/200. **All120 struts therefore stay >987/2000=0.4935 ell0, for every phase and every future time**, throughout the qualified property box. Primary spoke/edge lengths also stay strictly positive.

This closes the continuation argument: on any finite time interval, positive kinetic energy bounds all velocities, positions remain finite, alpha is bounded by its positive storage, strains are bounded, and z is bounded through z-Gy storage. The vector field is smooth away from zero member/strut lengths, which have the uniform positive margins above. The solution therefore extends for all u>=0. The proof permits rigid translation/rotation and nonzero conserved momenta; it does not need a rigid quotient.

This is nonlinear domain safety, **not** a nonlinear half-energy-at100 theorem. It does not establish a decay rate or attraction for nu=0.

## 3. Housing-only: every oriented cell volume stays within2.5%

For one cell, let A=[X_a-C,X_b-C,X_c-C] and G=A^T A. At reference,

\[
 G_0=\tfrac12 I+(R^2-\tfrac12)\mathbf1\mathbf1^T,
 \qquad \lambda_{\min}(G_0)=\tfrac12.
\]

The squared radial length changes are t_i=R²(2s_i+s_i²); the three squared edge changes are u_ij=2e_ij+e_ij². Let U have off-diagonal entries u_ij and diagonal0. Then

\[
 \Delta G=\tfrac12(t\mathbf1^T+\mathbf1t^T-U),\qquad
 \|\Delta G\|_F\le\sqrt3\,\|t\|_2+\frac{\|u\|_2}{\sqrt2}.
\]

The same energy budget constrains both sets of strains. Weighted Cauchy–Schwarz gives

\[
 \|\Delta G\|_F^2
 <2E\left[3(2+\sigma)^2+\frac{(2+\epsilon)^2}{2k_{\min}}\right]
 \le\frac{5588859701}{95000000000000}<\frac1{125^2}.
\]

Consequently ||G_0^(-1/2) DeltaG G_0^(-1/2)||_2<2/125. Its eigenvalues lie between -2/125 and2/125, so

\[
 (123/125)^{3/2}<\sqrt{\det G/\det G_0}<(127/125)^{3/2}.
\]

The determinant cannot vanish, so the initial orientation is preserved. Squaring positive quantities verifies the slightly looser rational bound

\[
 \boxed{\frac{39}{40}<\frac{V_k(u)}{V_{k,\rm ref}}<\frac{41}{40}}
 \quad\text{for every cell and all }u\ge0.
\]

The mean normalized volume obeys the same bound. This is absolute deviation from reference volume; it is not the prior pulse-relative mismatch or RMS-retention observable. Housing-only mean signal can vanish, making a signal-relative ratio unsuitable. Positive cell volumes alone are not claimed to prove convexity or global absence of self-intersections.

## 4. Full pulse: exact short-time tube, long-time energy obstruction

For the full pulse E<=680017/10^7, kinetic energy gives every housing speed <9 and every primary point speed <2/5. The earlier exact initial strut bound is >99/200. Hence on the initial existence interval,

\[
 \ell_{ea}(u)>99/200-(47/5)u\ge1/40,
 \qquad0\le u\le1/20.
\]

This uniform margin proves continuation through u=1/20 for every allowed phase and all qualified properties. The prior total-energy spoke/edge bounds (>5R/8,>2/5) remain applicable.

On this interval each relative spoke column changes by less than(4/5)u. Therefore ||A-A_0||_F<(7/5)u and sigma_min(A_0)=1/sqrt2>7/10. The relative matrix perturbation has norm <2u<=1/10. Singular-value/determinant bounds and continuous orientation give

\[
 \frac{729}{1000}<\frac{V_k(u)}{V_{k,\rm ref}}<\frac{1331}{1000},
 \qquad0\le u\le1/20.
\]

These deliberately conservative bounds certify an initial tube, far short of u=100. They do not certify the80% breathing or5% mismatch screens.

**FAILED method extension:** total energy alone cannot certify a positive strut lower bound on the entire full-pulse energy sublevel. Choose nominal primary properties, beta=1/200,w=1,alpha=z=0, reference primary positions and zero velocities. Move one housing to one of its edge endpoints; all others stay at their midpoints. Its only storage is

\[
 U_{\rm witness}=\frac{k_h}{8}=\frac1{40R^2}<\frac1{36}<\frac{13}{200}=E_{p,\rm nominal}.
\]

The energy extends continuously to this singular position; arbitrarily short positive struts have energy below the pulse budget. A continuous configuration path can first reduce alpha and then move the housing while staying below that energy. **Neither this path nor this state is asserted to be dynamically reachable from the allowed preparation.** The obstruction applies to a certificate using only the unrestricted total-energy sublevel. It does not refute true long-time safety or a trajectory-dependent invariant/tube.

## 5. Reproduction and limits

```bash
python3 experiments/icosahedral-nonlineartube/bounds.py --out /tmp/nonlineartube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-nonlineartube/geometry_check.py --out /tmp/nonlineartube
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-nonlineartube/check.py --out /tmp/nonlineartube
```

The exact proof uses inequalities and reproducible rational/algebraic checks. The ODE checks use floating DOP853 and sampled readouts with a tolerance refinement; they are not verified interval integration. No phase search or parameter retuning is performed. Native constitutive selection, physical scales, routing/strut masses and experimental validation remain OPEN/UNSCORED. Mainline promotion remains0.

Next discriminant: a trajectory-dependent relative-energy/variational tube around the nonlinear pulse, retaining all180 housing phase coordinates and reaction forces, starting with the exposed worst breathing preparation. Any u=100 bound must close its own positive-length domain and bound numerical integration error.
