# Original-amplitude all-phase 3D pulse safety: relative-response improvement

**RESULT: EXACT / CONDITIONAL.** For the *unchanged* UD Discovery 280-coordinate/560-mechanical-phase MountLoss surrogate, initial scalar heart pulse \(\alpha_0=1/10\), and arbitrary allowed initial 180-coordinate housing displacement/velocity phase with \(E_h\le51/20{,}000{,}000\), the entire mechanical trajectory exists to **\(u=9/10\)**, every one of its 120 moving-axis housing struts is longer than **\(11/1250\)** unit shell-edge lengths, and all 20 oriented cell volumes remain positive with ratios strictly between **\(27/10^6\)** and **\(7{,}645{,}373/10^6\)**. No rigid quotient or prescribed housing phase is used.

This improves the prior exact \(u=2/5\) result by changing only the estimate (using primary velocity correlations and exact relative Duhamel identity); it does **not** establish \(u=100\) coherence, ringdown, a physical UD realization, or a spacetime map. The rational \(9/10\) horizon was selected post-exposure by seeking a positive sufficient margin; it is not a physical transition or independent prediction.

## Sources, state and mechanical assumptions

- Verified integrated `main` at `2b133c7889cde7aae9127d0c0fa2036c278884a9` (2026-10-22); held session `phasewindow-20261022-gpt6-7c41`, claim `claims/icosahedral-phasewindow-20261022`, owned Discovery branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
- Baseline unchanged code `experiments/icosahedral-mountloss/mountloss.py`, `experiments/icosahedral-tolerances/hardware.py`, and prior `experiments/icosahedral-phasewindow-20261022/PULSE_SAFETY.md`, with the previous `SHORTTUBE` correction preserved. Parent source blob SHAs were checked equal between earlier `ce89a9c` and the current main for the consequential mechanics.
- Full state: 13 free 3D primary points (centre and 12 shell), one scalar heart variable, 150 auxiliary device coordinates, 30 free housing positions: 280 configurations and 560 mechanical phases; energy scalar bookkeeping is not another mechanical mode. Each of the 30 housings has four instantaneous direction dampers to its edge endpoints and the two adjacent-face opposite vertices, using reciprocal reactions.
- Euclidean 3D geometry, shell-edge reference length \(\ell_0=1\), continuous dimensionless clock \(u=t/t_0\) (uncalibrated), reference circumradius squared \(R^2=(5+\sqrt5)/8<1\), and conservative/dissipative positive mechanical energy. Positive material settings, \(\Omega=10\), \(\beta\in[1/200,1/20]\), housing weights \(w_e\in[9/10,11/10]\), primary masses and spoke strengths \([19/20,21/20]\), shell stiffness \([19/50,21/50]\), \(0\le\nu\le1/20\) (includes fitted \([1/25,1/20]\)), \(c_f\ge0\). Device gains remain the original positive values. No variation beyond this declared box is asserted.
- Initial \(\alpha=1/10\) with all primary and auxiliary positions at reference and zero velocities; every housing's position/velocity can vary subject only to the total allowed \(E_h\), including rigid translation/rotation kinetic energy. No extra physical targets/fits or new force law.

## 1. Positive energy, instantaneous velocity and initial housing bounds

The unchanged constitutive law gives \(E'(u)=-P_{\rm loss}\le0\) on the domain of positive spoke, edge, and damper-strut lengths. All time-uniform comparisons below are made only up to a putative first singularity, then closed by continuation.

\[
 E(u)\le E(0)\le\frac{34}{5}(1/10)^2+\frac{51}{20{,}000{,}000}
 =\frac{1{,}360{,}051}{20{,}000{,}000}=E_*.
\]

Each primary position \(X_a\) has inertial coefficient \(m_a/R^2>19/20\); including all 13 primary kinetic energies, not just one,

\[
 \sum_{a=0}^{12}|\dot X_a|^2 < \frac{2 E_*}{19/20}<\left(\frac{19}{50}\right)^2
 =:v_*^2.
\]

Individual primary speeds are also \(<2/5\), each housing's speed \(<9\), initial housing speed \(<3/50\), and initial housing-to-midpoint error \(|D_e|<1/180\). These exact rational inequalities follow from housing inertia \(>9/5000\), mount stiffness \(>9/50\), and initial additional housing energy \(\le51/20{,}000{,}000\). **Do not replace the summed primary-speed budget by 13 independent speed maxima.**

For the sinusoidal homogeneous oscillator initial data, Cauchy--Schwarz yields a tighter combined bound than the earlier sum:

\[
 \left|D_e\cos(10u)+\frac{\dot H_e(0)}{10}\sin(10u)\right|
 \le\sqrt{|D_e|^2+\frac{|\dot H_e(0)|^2}{100}}
 <\frac{41}{5000}=:c_*.
\]

This is for vectors in \(\mathbb R^3\), componentwise cosine/sine factors, and does not assume initial vectors are orthogonal.

## 2. The exact *relative* Duhamel identity

For housing \(e=(i,j)\), write its moving midpoint \(A_e=(X_i+X_j)/2\), \(H_e\) its position, and \(F_e=(\eta/m_{he})\sum_{a\in\{i,j,k,l\}} n_{ea}[n_{ea}\cdot(\dot H_e-\dot X_a)]\), the true moving-axis dissipative acceleration, with \(\eta/m_{he}=\nu/w_e\). Its original equation is

\[
 \ddot H_e+100 H_e=100 A_e-F_e.
\]

Given \(H_e(0)=A_e(0)+D_e\), straightforward integration by parts in the oscillator Green formula gives, for **any** anchor \(a\),

\[
 \begin{aligned}
 H_e(u)-X_a(u)={}& A_e(0)-X_a(0)+\cos(10u)D_e
 +\tfrac{\sin(10u)}{10}\dot H_e(0)\\
 &+\int_0^u\big[(1-\cos(10(u-s)))\dot A_e(s)-\dot X_a(s)\big]ds\\
 &-\tfrac1{10}\int_0^u\sin(10(u-s))F_e(s)\,ds.
 \end{aligned}
\]

No prescribed midpoint path or fixed damper directions are inserted. The original model's four-anchor viscous law plus the energy bounds give

\[
 |F_e(u)|\le\frac{\nu}{w_e}\sum_a(|\dot H_e|+|\dot X_a|)
 <\frac1{18}\,4\left(9+\frac25\right)=\frac{94}{45}.
\]

This force is nonconservative but **dissipative** in the total mechanical energy, so the speed bounds remain valid.

### Endpoint anchors

If \(a=i\) (and analogously \(j\)), let \(c=\cos(10(u-s))\). The velocity integrand is exactly

\[
 -\tfrac{1+c}{2}\dot X_i+\tfrac{1-c}{2}\dot X_j.
\]

The Euclidean norm of its two scalar coefficients is

\[
 \sqrt{\frac{(1+c)^2+(1-c)^2}{4}}
 =\sqrt{\frac{1+c^2}{2}}\le1.
\]

Consequently, by the *shared* primary kinetic-energy budget, the integrand has norm \(<v_*=19/50\), uniformly in all dynamics, coordinates, and phases.

### Opposite-face anchors

If \(a=k\) or \(l\), the same integrand is \((1-c)(\dot X_i+\dot X_j)/2-\dot X_a\); the coefficient norm is \(\sqrt{1+(1-c)^2/2}\le\sqrt3\), so its vector norm is \(<\sqrt3v_*\). At the reference geometry the midpoint-to-endpoint distance is exactly \(1/2\), while midpoint-to-either opposite face vertex distance is exactly \(\sqrt3/2\). The opposite-face lower bound is at least \(\sqrt3(1/2-v_*u)-B(u)\) versus \((1/2-v_*u)-B(u)\) at endpoints, where \(B(u)\ge0\) is the *same* homogeneous-plus-viscous error. Whenever the endpoint lower bound is positive, the opposite-face lower bound is strictly larger. Thus endpoint estimates suffice for all 120 struts.

## 3. Exact global sine-average lemma

For all \(x\ge0\),

\[
 \boxed{\int_0^x|\sin t|dt\le\frac34x}.
\]

Here is a proof that does not rely on numerical sampling. It suffices to establish \(1-\cos r\le3r/4\) for \(0\le r\le\pi\): the integral over \(n\) complete positive half-periods is \(2n+1-\cos r\), and \(2n\le(3/4)n\pi\) follows from \(\pi>3>8/3\).

- For \(0\le r\le3/2\), \(1-\cos r\le r^2/2\le3r/4\).
- For \(3/2\le r\le8/5\), the alternating Taylor upper bound \(1-\cos r\le r^2/2-r^4/24+r^6/720\) and rational endpoint estimates give \((1-\cos r)/r\le4/5-9/64+(8/5)^5/720=6065447/9000000<3/4\).
- For \(8/5\le r\le8/3\), \(1-\cos r\) is concave since \(\cos r<0\). Its tangent at \(2\pi/3\) is \(L(r)=3/2+(\sqrt3/2)(r-2\pi/3)\). At \(r=8/5\), \(L<7/6<3r/4=6/5\), using \(\pi>3\), \(\sqrt3/2>5/6\). At \(r=8/3\), \(L<3/2+(13/15)(43/75)=4493/2250<2=3r/4\), using the standard rational bounds \(\pi>157/50\), \(\sqrt3/2<13/15\). The affine difference \(L(r)-3r/4\) is negative at both endpoints; concavity makes \(1-\cos r\le L(r)<3r/4\) throughout.
- For \(8/3\le r\le\pi\), \(1-\cos r\le2\le3r/4\).

Substitution \(x=10u\) therefore yields

\[
 \frac1{10}\int_0^u|\sin(10(u-s))|\,ds\le\frac3{40}u.
\]

## 4. Strict strut length bound to u=9/10

Combining the relative Duhamel formula, \(c_*<41/5000\), \(v_*<19/50\), the viscous acceleration \(<94/45\), and the lemma, for *all* endpoint anchors and \(0\le u\le9/10\),

\[
 |H_e(u)-X_a(u)|>
 \frac12-\frac{41}{5000}-\left(\frac{19}{50}+\frac{47}{300}\right)u.
\]

The right-hand side decreases linearly. Its exact value at \(u=9/10\) is

\[
 \frac12-\frac{41}{5000}-\left(\frac{19}{50}+\frac{47}{300}\right)\frac9{10}
 =\boxed{\frac{11}{1250}>0}.
\]

The opposite-face argument above then gives the *same strict lower bound* for every one of the 120 struts, uniformly for every allowed housing phase and every qualified parameter set. The spoke/edge strains satisfy \(|s_i|<2/5\) and \(|e_j|<3/5\) at all times up to the first hypothetical domain exit, ensuring the 42 primary members cannot collapse either.

## 5. Cell orientations and continuation

For one oriented cell, set \(A=[X_a-C,X_b-C,X_c-C]\). At the reference, \(\sigma_{\min}(A_{\rm ref})=1/\sqrt2\). The map from the four primary point velocities \((\dot C,\dot X_a,\dot X_b,\dot X_c)\) to its three relative columns is the \(3\times4\) star-incidence operator \(B\) (tensored with \(I_3\)), with \(BB^T=I_3+\mathbf1\mathbf1^T\) and \(\|B\|_2=2\). Hence, using the same **total kinetic energy bound**,

\[
 \|\dot A\|_F<2v_*,\quad
 \|A(u)-A_{\rm ref}\|_F<2v_*u,\quad
 \|A_{\rm ref}^{-1}(A-A_{\rm ref})\|_2
 <2\sqrt2v_*u.
\]

At \(u=9/10\), exact rational squaring verifies

\[
 (2\sqrt2\cdot\tfrac{19}{50}\cdot\tfrac9{10})^2
 =\frac{29241}{31250}<\left(\frac{97}{100}\right)^2<1.
\]

Thus all 20 oriented cell volumes retain their reference sign continuously. Their fixed ratio bounds, throughout \([0,9/10]\), are

\[
 \boxed{
 \left(\frac3{100}\right)^3 <\frac{V_k(u)}{V_{k,\rm ref}}<
 \left(\frac{197}{100}\right)^3
 }.
\]

These deliberately weak volume-domain bounds are **not** the 80% breathing-retention and 5% mismatch screens. With finite total energy, positive mass/auxiliary spring storage, bounded velocities, and positive lower margins for spokes, edges and struts, the finite-dimensional ODE stays in a smooth domain on \([0,9/10]\), so the bootstrap/continuation argument supplies existence through the horizon. Global existence to \(u=100\) is **not** inferred.

## Source checks, evidence labels and limitations

**EXACT / CONDITIONAL:** Every algebraic bound in `relative_tube.py` uses `fractions.Fraction`; independent same-runtime `independent_check.py` computes the star-incidence spectrum and reference cell Gram eigenvalues with SymPy, and samples the sine lemma only as a numerical diagnostic. The analytic sine proof above, rather than the sampling, is the mathematical justification. Both scripts were executed locally; source SHA-256 checks and outputs are captured in the immutable run.

**OPEN:** All-phase full nonlinear `u=100`, breathing RMS >80% and 5% mismatch, housing half-energy deadline, higher-dimensional space mapping, physical hardware and clock/energy calibration. The previously exposed `nu=.02`, low-beta failure and original `alpha=.1` energy-only housing-endpoint witness remain valid. Draft PR #44 owns complementary forced-Green/reconstruction work; no overlapping files or conclusions were modified. This result is a positive-length and orientation safety certificate, not a physical operating-performance guarantee.
