# UD Discovery — exact positive-length convex tube for the original 3D pulse

**RESULT: EXACT / CONDITIONAL.** A full-560-phase domain theorem through \(u=1019/1000\), and explicit current-axis force-Hessian bounds on the convex domain swept by all qualified initial housing phases. **OPEN:** all-time \(u=100\) domain, projected nonlinear remainder, the breathing/ringdown screens, and native physical mapping. The theorem concerns the *unchanged three-dimensional surrogate*; it does not revive the parked 4D model.

## Typed problem and provenance

- Model: 280 generalized coordinates, 280 velocities and a nondecreasing heat ledger, with 12 shell vertices, centre, 30 three-coordinate housing nodes, 150 auxiliary coordinates, scalar heart \(\alpha\), and 120 current-axis viscous paths.
- Space: Euclidean \(\mathbb R^3\), reference unit shell-edge length, regular icosahedron \(R^2=(5+\sqrt5)/8\), internal time \(u\) (not calibrated physical seconds).
- Initial data: \(\alpha(0)=1/10\), primary/auxiliary coordinates at reference, their velocities zero. Arbitrary initial housing positions and velocities (90+90 variables) with additional energy \(E_h\le51/20{,}000{,}000\). This is the previously FIT-expanded housing preparation.
- Continuous qualified box: primary masses and radial stiffnesses in \([19/20,21/20]\), shell edge stiffnesses \([19/50,21/50]\), \(\beta\in[1/200,1/20]\), mean-one housing weights \([9/10,11/10]\), housing frequency 10, \(0\le\nu\le1/20\), nonnegative auxiliary/damping parameters and allowed reciprocal coefficients. The true design window \(\nu\in[1/25,1/20]\) is included.
- Source: versioned read-only integrated main `5fd737fda4dadd6f1cc3d9c3c6c086473b7f72bb` and held branch `ff1d268a0716bd6bcb5297ec7eabf3a90e91fa91`; five mechanical model blobs were verified unchanged versus reference `4aaf0a39d24328e27bc425e333e3612baea888a5`. Claim `icosahedral-phasewindow-20261022`, session `phasewindow-20261022-gpt6-7c41`. PR #44 is separately held and untouched.
- Earlier results imported read-only: prior `relative-tube-006` certified 120 struts and 20 oriented cells through \(u=49/50\); `initial-curvature-017` proved initial nonlinear acceleration remainder \(<9\times10^{-8}\) but also an energy-only global Hessian obstruction.

## Theorem 1 — all initial housing phases: positive-length domain through u=1.019

Define \(T=1019/1000\). For **every** allowed coefficient realization and housing initial phase, the original full nonlinear ODE exists through \(0\le u\le T\) and

\[
\boxed{\text{each of the 120 current-axis struts satisfies }\ell_{ea}(u)>1/2500.}
\]

Every primary spoke and shell edge is also strictly positive. This is a continuation/regularity theorem, **not** a cell-orientation theorem for \(u>49/50\): the mechanical ODE does not have oriented cell volume in a denominator, so temporary cell flattening is not an ODE singularity under the stated law.

### Exact energy, velocity, and oscillator inequalities

Passivity provides \(E(u)\le E_* =1{,}360{,}051/20{,}000{,}000\) on the regular domain. Since \(9/10<R^2<181/200\), shared primary kinetic control gives

\[
\sum_{a=0}^{12}|\dot X_a|^2 <(9/25)^2,\qquad |\dot H_e|<35/4,
\]

and the same initial housing energy bounds the combined oscillator homogeneous displacement/velocity amplitude by \(1/180\) per housing. With \(\eta_e/m_e=\nu/w_e\), the magnitude of the four-anchor viscous acceleration on housing \(e\) is bounded by \(911/450\).

For an endpoint anchor, integrating the *actual moving-midpoint* housing oscillator by parts produces the vector deviation bound (uniformly for all \(u\le T\))

\[
|[H_e(u)-X_i(u)]-[A_e(0)-X_i(0)]|
 < \frac1{180}+\frac9{25}T+\frac{911}{4500}I(T),\quad
I(T)=\int_0^T|\sin(10s)|ds.
\]

For an opposite-face anchor, the same estimate has coefficient \((7/4)(9/25)T\) in the primary-velocity term, but a larger initial reference strut length \(\sqrt3/2>4/5\). A shared primary-velocity norm is used, with no artificial zero-momentum assumption.

### Fully rational sine-kernel enclosure

The lower rational bound \(\pi>333/106\) is verified in the executable by Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\) and alternating rational arctangent partial sums. Also \(\pi<22/7\). Thus \(10T=1019/100\) falls strictly between \(3\pi\) and \(4\pi\). Write \(r=10T-3\pi\), so \(0<r<4057/5300<1\), and use the alternating cosine remainder inequality

\[
0\le1-\cos r\le\frac{r^2}{2}-\frac{r^4}{24}+\frac{r^6}{720}.
\]

The integral \(I(T)=[6+1-\cos r]/10\) is therefore rigorously bounded above by the rational

\[
I_* =\frac{6+(4057/5300)^2/2-(4057/5300)^4/24+(4057/5300)^6/720}{10}
 =\frac{100201575869560039503115249}{159583400128800000000000000}.
\]

For endpoint struts this yields

\[
\ell_{ei}(u) >\frac12-\frac1{180}-\frac9{25}\frac{1019}{1000}-\frac{911}{4500}I_*
=\frac{352344404790340012662008161}{718125300579600000000000000000}
\approx0.0004906447447>\frac1{2500}.
\]

For the two opposite-face anchors, replace \(1/2\) by \(4/5\) and \(9/25\) by \((7/4)(9/25)\); the resulting lower bound is \(\approx0.02536064\), strictly above the endpoint bound. The elastic energy independently gives primary radial strain \(<2/5\) and exterior edge strain \(<3/5\), so no primary member can vanish. Boundness of the remaining coordinates and velocities, together with the length-domain margins, gives ODE continuation through \(T\).

## Theorem 2 — convex interpolation of the entire phase-family geometry

For any primary site pair, shared kinetic control and Cauchy–Schwarz imply

\[
|(X_i(u)-X_j(u))-(X_i(0)-X_j(0))|<\sqrt2\frac9{25}T
 <\frac{27}{50}T=\frac{27513}{50000}.
\]

Since spoke reference lengths are \(R>9/10\) and outer-edge reference lengths are 1, their entire same-time convex interpolants between *any two* admitted trajectories satisfy

\[
\ell_{\rm spoke}>\frac{17487}{50000}>\frac13,
\qquad
\ell_{\rm edge}>\frac{22487}{50000}>\frac25.
\]

The vector error estimates in Theorem 1 also place all housing-to-anchor vectors inside **common convex balls** centred on each nonzero initial strut vector and of radius less than the corresponding initial length minus \(1/2500\). Thus any same-time convex interpolation between admitted state positions retains **all 120 struts \(>1/2500\)**. No linearity of the nonlinear *trajectory* map is presumed. The full geometric spring/damper constitutive vector field is therefore smooth throughout these interpolation segments, uniformly over the qualified phase ball for \(0\le u\le T\).

## Theorem 3 — explicit per-path viscous force Hessian

For one current-axis force \(f(d,w)=\eta P(d)w\), \(P(d)=dd^T/|d|^2\), \(d\in\mathbb R^3\setminus\{0\}\), \(w\in\mathbb R^3\), elementary differentiation of \(n=d/|d|\) gives

\[
\|DP(d)[a]\|_2\le\frac{2|a|}{|d|},\qquad
\|D^2P(d)[a,b]\|_2\le\frac{8|a||b|}{|d|^2}.
\]

On the certified convex tube, \(|d|>1/2500\), \(|w|<911/100\), and \(\eta<1/900\). Hence for any two perturbation pairs \((a_d,a_w)\), \((b_d,b_w)\),

\[
\boxed{
\|D^2f[(a_d,a_w),(b_d,b_w)]\|
\le\frac{4555000}{9}|a_d||b_d|
+\frac{50}{9}(|a_d||b_w|+|b_d||a_w|).
}
\]

A time-slab refinement gives substantially better conditioning before the end of the certified tube:

| Certified interval | Strut lower bound | Per-path \(D_{dd}^2 f\) coefficient | Per-path mixed \(D_{dw}^2f\) coefficient |
|---|---:|---:|---:|
| \(0\le u\le1\) | \(1/125\) | \(22775/18\approx1265.28\) | \(5/18\) |
| \(0\le u\le101/100\) | \(1/250\) | \(45550/9\approx5061.11\) | \(5/9\) |
| \(0\le u\le1019/1000\) | \(1/2500\) | \(4555000/9\approx506111.11\) | \(50/9\) |

Each cutoff is independently verified with exact rational trigonometric bounds in the replay script. The factor-400 increase in the last second-displacement coefficient shows that the crude uniform tube is *badly conditioned* near its proof horizon; it is not evidence of any observed physical instability.

The bound holds throughout every straight interpolation of the permitted state-family *at a fixed time*. Integrating this Hessian on such a segment provides a rigorous quadratic remainder for one **force term**. It is **not** yet a bound on the Hessian of the nonlinear *solution map* and cannot be substituted for the time-varying forced-Green propagator. The coefficient \(4555000/9\approx506{,}111\) is prohibitively conservative near the end of this short tube, despite the tiny observed numerical phase curvature at \(u=4\).

## Checks, selection, and failed extension

- **EXACT:** `strut_tube018.py` uses `fractions.Fraction` exclusively to verify the pi/arctan comparison, sine-kernel integral upper bound, all length and mass inequalities, and the force-Hessian constants. `python3 strut_tube018.py --out result.json` passed locally.
- **NUMERICAL / independent implementation:** `independent_check.py` reconstructs the 13 icosahedral coordinates and 30 edges, all 20 faces and all 120 initial anchor distances exactly with SymPy; checks the sine integral at 70-digit mpmath precision, and tests 30 random normalized second derivatives of \(P(d)\). All passed. These are constructor/cross-checks, not independent formal verification.
- **FIT:** The horizon \(1019/1000\) was selected after inspecting the earlier \(49/50\) estimate and the present sufficient inequality. The coefficient domain, pulse amplitude, housing energy radius, geometry and primary mechanical model are inherited, not newly fitted to measurements. No post-hoc physical-clock calibration.
- **FAILED / OPEN:** The simple finite-horizon bound tends to zero just beyond this time. It neither proves the ODE develops a singularity nor establishes any \(u=100\) dynamics. The old original-pulse orientation certificate remains valid only through \(49/50\); no cell-volume lower bound is claimed between \(49/50\) and \(1019/1000\). A global whole-energy-sublevel Hessian majorant is impossible by the independently proved 017 counterexample; the *trajectory-restricted* Hessian is finite but not sufficient alone for a full nonlinear phase-ball certificate.

**Next discriminant (priority 99/100):** derive time-dependent, projected propagator/Green bounds in this rigorously positive-length domain, then use a nonlinear bootstrap (not an energy-only constant) to extend the domain past \(1019/1000\). Work on PR #44 only with its owner's authorization; preserve the separate branch boundary.