# Joint housing ringdown and breathing window v1.0

**Development / FIT / EXACT / CONDITIONAL / NUMERICAL.** Base `92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`; [parent model/proof](../icosahedral-mountloss/README.md), [frozen protocol](PROTOCOL.md), [candidate budget](BUDGET.md), [results](RESULTS.md), [candidate](../../candidates/icosahedral-jointwindow/candidate.json), [mathematical receipt](../../candidates/icosahedral-jointwindow/mathematical_receipt.json).

## 1. Objects and scope

No mechanical law is changed. There are280 configuration coordinates q=(alpha,13 primary positions,150 device coordinates,30 housing positions),560 mechanical phase variables and one heat accumulator. The13 original complex vertices,30 housings,120 viscous paths and54 old hidden modes are different typed objects. Reference geometry is over Q(sqrt5); dynamics are real in uncalibrated ell0,E_*,t0 units, with continuous u=t/t0. No modular register or prime-factor mechanism is introduced.

Use the equilibrium linearization M q''+C_nu q'+Kq=0, with C_nu=C_0+nu C_h. M,K do not depend on nu. Positive masses/stiffness/device loss,positive reciprocal gains and nu>0 imply the parent's local decay theorem after removing six global rigid directions. Nonlinear checks retain all coordinates and current-axis forces. This study does not replace the ideal massless struts/routing with fabricated hardware.

The proposed qualified parameter box has beta in[1/200,1/20]=[.005,.05],c_f in[0,1/1000],Omega=10,primary masses/g in[.95,1.05],edge k in[.38,.42],reciprocal gains[.99,1.01] and housing weights[.9,1.1] of mean1. The earlier beta>0 open endpoint is preserved as a distinct limiting question. Candidate strength interval nu in[1/25,1/20] is target-informed, not a derived universal constant.

## 2. Exact linear mean-volume compliance

Let lq be the derivative at reference of the average normalized cell volume. Summing oriented determinant derivatives over all20 cells cancels the centre contribution. `bounds.py` verifies exactly

\[
 l_\alpha=l_C=0,\qquad l_{X_i}=\frac{r_i}{4R^2},\quad R^2=\frac{5+\sqrt5}{8}.
\]

Thus common primary scale b gives lq=3b. This **linear** readout differs from finite symmetric volume (1+b)^3-1 and from hub-relative volume mismatch.

For static primary displacement, minimizing over free device z and housing H makes their positive storage zero: z=Gy(q),H=Aq. Consequently the static compliance of any primary observable is that of the primary stiffness alone, independently of housing mass,nu,ratio errors and input loss. The pseudoinverse is interpreted on the rigid quotient; l annihilates rigid directions.

Decreasing all g,k to their allowed minima gives a positive-semidefinite lower stiffness. Its uniform alpha,b block is

\[
 K_{\min,\mathrm{coll}}=
 \begin{pmatrix}62/5&-57/5\\-57/5&174/5\end{pmatrix}.
\]

Icosahedral symmetry confines this mean observable to that block. Monotonicity of compliance on the rigid quotient therefore yields the continuous-parameter bound

\[
 lK^\dagger l^T\le (0,3)K_{\min,\mathrm{coll}}^{-1}(0,3)^T
 =\frac{930}{2513}=:S_*.
\]

For any added initial perturbation with linear mechanical energy E_h, passivity and energy Cauchy–Schwarz give, at every time and hence in RMS,

\[
 |l\delta q(u)|\le\sqrt{2E_h S_*},\qquad
 \operatorname{RMS}(l\delta q)\le\sqrt{2E_h S_*}.
\]

This is exact/conditional for the full linear assembly and **all** phases in the energy ball, not a random-direction observation. It does not require that the perturbation decay by a particular deadline. Set E_h<=E_p/40000,where E_p=(1+sum_i g_i)(1/10)^2/2 is the reference alpha-pulse energy. Across the property box E_p lies in[31/500,17/250]; the phase bound is in normalized volume units, not a percentage until divided by a specified pulse RMS.

If R_p(nu) is the linear pulse RMS without the housing perturbation, every housing phase in that ball satisfies

\[
 R_{\rm total}(\nu)\ge R_p(\nu)-\sqrt{2E_h S_*}.
\]

The original undamped **linear** RMS is computed separately for each primary realization by the exact cosine-integral formula from its numerical normal modes. Nonlinear pulse baselines remain the frozen original nonlinear baselines; those two normalizations are never interchanged.

The same declared energy budget gives a separate **nonlinear initial-domain bound**. E_h<=17/10^7,while beta>=1/200,w>=9/10,R²<1 imply each housing inertia>9/5000 and mount stiffness>9/50. Hence every initial housing displacement is<1/200 ell0 and every initial housing speed is<1/20 ell0 per unit u. Primary points start at reference,so all120 initial strut lengths exceed99/200 ell0,for every housing phase in the energy ball.

Total initial energy is at most680017/10^7. Positive parent storage then gives |s_i|<3/8 and |e_j|<3/5 throughout any existing trajectory in the strut domain. Thus radial lengths exceed5R/8 and shell edges exceed2ell0/5. This prevents primary member collapse before a possible housing-strut singularity; it does **not** prove all-time positive housing-strut lengths,global existence,cell orientation or coherence. These additional energy consequences were checked after the linear coverage run without changing any preparation or selection choice.

## 3. Exact bound in the fixed-primary linear housing limit

For fixed primary points at reference, each mass-normalized housing direction solves h''+d h'+Omega²h=0. The parent exact direction Gram has eigenvalues2,(3±sqrt5)/3,so

\[
 \frac{\nu(3-\sqrt5)}{3w_{\max}}\le d\le\frac{2\nu}{w_{\min}}.
\]

For0<d<2Omega,the exact scalar energy-coordinate propagator gives

\[
 \frac{E(u)}{E(0)}\le\frac{2\Omega+d}{2\Omega-d}e^{-du}.
\]

One derivation writes the propagator as e^(-du/2) times a determinant-one2x2 matrix. Its largest energy singular value squared is bounded by(2Omega+d)/(2Omega-d),uniformly in oscillation phase. Summing independent housing directions preserves the bound,including all90 housing directions and their position/velocity phases.

For all nu in[1/25,1/20],all weights[9/10,11/10],Omega=10,use sqrt5<9/4 to get d>=1/110 and d<=1/9. At u=100,

\[
 \frac{E(100)}{E(0)}
 \le\frac{181}{179}e^{-10/11}
 <\frac{181}{179}\frac{3993}{9773}
 =\frac{722733}{1749367}<\frac12.
\]

The rational exponential bound follows from e^(10/11)>1+10/11+(10/11)^2/2+(10/11)^3/6=9773/3993. `bounds.py` checks every fraction and the readout gradient.

This is a **fixed-primary equilibrium-linearization bound**, also describing the mass-normalized housing sector as beta approaches0 at fixed bounded nu. It is not a finite-beta coupled bound or a nonlinear housing result. Finite-beta backreaction is included in the numerical full-system evaluations.

## 4. Continuous-strength interpolation for each parameter case

Fix the mechanical parameter vector p. Remove the rigid directions and mass-normalize, obtaining k>0 and phase state y=(q_tilde,v_tilde),energy metric G=diag(k,I). Let Phi_nu(u) be the full548-dimensional nonrigid propagator. It is a contraction in G. Let B map108 unit-energy-norm initial phases of the old54-dimensional housing sector into this phase space: B^T G B=I. The all-phase energy fraction is

\[
 \rho_p(\nu)=\|\Phi_\nu(T)B\|_G^2,
 \qquad T=100.
\]

It is computed as the largest eigenvalue of B^T Phi^T G Phi B,not from the slowest pole. Let D=partial C_tilde/partial nu>=0 and L_D=||D||_2. Since only the velocity block changes,Duhamel's identity and contraction give

\[
 \sqrt{\rho_p(\nu)}\le\sqrt{\rho_p(\nu_0)}+T L_D|\nu-\nu_0|.
\]

This inequality controls a continuous strength neighborhood even though dissipative response need not be monotone in nu. Merely testing endpoints would not establish an interval.

For a tighter pulse-readout sensitivity,follow the prepared linear pulse at nu_0 and define

\[
 I_D=\int_0^T\|D v_{p,\nu_0}(s)\|^2ds.
\]

Another application of Duhamel,energy Cauchy–Schwarz and integral Cauchy–Schwarz gives

\[
 |R_p(\nu)-R_p(\nu_0)|
 \le |\nu-\nu_0|\sqrt{S_* T I_D/2}=:L_R|\nu-\nu_0|.
\]

In detail,the state difference at t is bounded by |delta nu| times integral_0^t||D v_0(s)||ds. Its squared RMS is at most delta nu² times T I_D/2; apply the dual readout norm<=sqrt(S_*). This retains the small housing-loss participation of the pulse,avoiding a much looser full-state bound.

A node therefore supplies a sufficient joint radius

\[
 r_p=\min\left\{
 \frac{\sqrt{1/2}-\sqrt{\rho_p(\nu_0)}}{T L_D},
 \frac{R_p(\nu_0)-\sqrt{2E_hS_*}-(4/5)R_{\rm orig}}{L_R}
 \right\}.
\]

Intersect across the finite parameter cases and join node neighborhoods as declared in the protocol. The formulas are exact conditional inequalities. Phi,R_p,I_D and radii are evaluated in float64 with explicit numerical cushions and residual/second-method checks; this is a **numerical enclosure**,not verified interval arithmetic. It covers a continuous strength variable for those parameter cases. It does not enclose the whole high-dimensional uncertainty box.

Pulse and sensitivity integrals use A^T W+WA=-Q and integral_0^T y^TQy=y0^TWy0-yT^TWyT. A direct augmented ODE integral checks representative cases. Neither the numerical Lyapunov solve nor CI is an exact proof.

### Full housing scope audit and stronger interpolation

After the old54-mode campaign,the scope audit includes **all90 housing directions and their180 position/velocity phase coordinates**. Projecting out rigid coordinates must not discard their kinetic energy. If R is a mass-orthonormal rigid basis and U injects90 mass-normalized housing velocities,the full initial energy-Gram is obtained by adding the conserved velocity block U^T R R^T U to the nonrigid propagator Gram. It equals I at time0. Global rigid displacement costs no stiffness energy;global rigid velocity carries kinetic energy and remains included. The largest Gram eigenvalue maximizes over every linear combination of the180 initial coordinates.

The coarse interpolation can leave gaps even while every evaluated node passes. A sharper bound follows without another model assumption. For any unit energy-norm initial phase,E0=1/2 and

\[
 \nu_0\int_0^T v_0^TDv_0\,ds\le\tfrac12,
 \qquad\int_0^T\|Dv_0\|^2ds\le\frac{\lambda_D}{2\nu_0}.
\]

Duhamel and integral Cauchy–Schwarz therefore replace T lambda_D by

\[
 L_H=\min\{T\lambda_D,\sqrt{T\lambda_D/(2\nu_0)}\}
\]

in the energy-operator norm interpolation. This applies to the full housing phase space,including its nonzero conserved rigid kinetic part. The breathing perturbation inequality already applies to the entire housing-energy ball and needs no restriction to the old54-mode kernel.

This strengthening was derived after observing the coarse audit's coverage gaps. The raw audit,its node cap and all trajectories are preserved;`refine_full_bounds.py` evaluates the stronger exact inequality on the saved numbers. It changes no strengths,thresholds or preparations. Full-housing nonlinear endpoint ringdowns remain two finite phase checks,while the64 pulse records retain their original old-sector preparations.

## 5. Why a lower mass boundary is explicit

For ideal gains,nominal primary properties,c_f=0,and beta tending0 with bounded nu,the housing return forces and primary strut loss vanish in mass-normalized equations. The primary common breathing poles approach ±i sqrt(8±sqrt37). Thus no strictly positive **full-assembly exponential decay rate** can be uniform over the old open beta>0 range. This does not obstruct a finite-time housing-sector bound; the two claims concern different initial spaces.

An initial housing-energy ball also permits displacement proportional to beta^(-1/2); without a lower mass boundary it supplies no uniform finite displacement/strut-length bound. These are reasons to state a qualified mass range,not to erase smaller-mass cases. Extra beta=.0005/.00005 cases test the limiting trend separately.

On the closed qualified parameter box and positive compact strength interval,the parent's absence of nonrigid imaginary poles plus continuity/compactness implies existence of a uniform local exponential rate. This existence result does not give a useful number,half-energy at100,or nonlinear coherence. A quantified continuous uncertainty-box bound remains OPEN unless separately proved.

## 6. Reproduction and physical scope

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-jointwindow/bounds.py --out /tmp/jointwindow
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-jointwindow/analyze.py --out /tmp/jointwindow
python3 experiments/icosahedral-jointwindow/envelope.py --out /tmp/jointwindow
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-jointwindow/full_housing.py --out /tmp/jointwindow
python3 experiments/icosahedral-jointwindow/refine_full_bounds.py --out /tmp/jointwindow
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 experiments/icosahedral-jointwindow/balancecheck.py --out /tmp/jointwindow
python3 experiments/icosahedral-jointwindow/finalize.py --out /tmp/jointwindow
python3 experiments/icosahedral-jointwindow/draw.py --out /tmp/jointwindow
```

The immutable run preserves code,source inputs,cases,duplicate aliases,nodes,radii,coverage,initial phases,nonlinear pulses/ringdowns,refinements and receipt. Two CPU workers run independent trajectories; there is no LLM delegation or independent review. In full nonlinear preparations the linear hidden-phase subspace cancels linearized rigid momenta; a displacement/velocity combination may have a small quadratic initial angular momentum. Actual total P,L and their conservation are measured,not assumed to vanish.

Nonlinear trajectories have E_h=E_p/40000 and their own worst **linear ringdown** phase. This is not necessarily a worst nonlinear volume phase. Exact linear superposition/readout bounds do not become nonlinear all-phase claims. Sampled positive lengths/oriented volumes do not become all-time guarantees. The original mass/friction failures and nu=.02 low-mass failure remain in their source records.

Physical testing remains UNSCORED. See the existing [mount test plan](../icosahedral-mountloss/MOUNT_TEST.md). Strut mass,routing,anchor compliance and native constitutive/time selection are still assumptions or OPEN; this work confers no mainline promotion.
