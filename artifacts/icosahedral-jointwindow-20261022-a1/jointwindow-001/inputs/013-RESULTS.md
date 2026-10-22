# Joint housing ringdown / breathing window — results v1.0

**RESULT — candidate strength window [1/25,1/20]=[.04,.05] passes the declared finite-family linear enclosure and nonlinear endpoint checks.** The latest consolidated machine record is [milestone.json](../../artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/milestone.json); [immutable manifest](../../artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/manifest.json). Read [model/proofs](README.md), [budget and scope](BUDGET.md), [exposure/protocol history](PROTOCOL.md) and [receipt](../../candidates/icosahedral-jointwindow/mathematical_receipt.json).

## Declared preparation and what is covered

Keep the prior280-coordinate model and120 ideal central viscous struts. Qualified beta=[.005,.05],c_f=[0,.001],Omega=10 and the inherited primary/ratio/housing scatter. Prepare alpha=.1 and add housing energy **E_h<=E_p/40000**,where E_p is that realization's reference pulse energy. Length,energy,time units remain uncalibrated.

The linear enclosure spans every strength in [.04,.05] for **50 distinct parameter sets behind56 case records**. Its final housing scope includes **all90 housing directions and their180-dimensional position/velocity phase space**,with conserved rigid kinetic energy retained. This is a continuum of initial phases;180 is the dimension,not a count of random preparations. The parameter family is finite. The nonlinear checks use finite endpoint phases.

| Readout | Result | Evidence scope |
| --- | ---: | --- |
| Housing energy at u=100,entire strength interval | <=.456666071 | Numerical full180-phase enclosure over50 parameter sets |
| Breathing RMS,all housing phases within energy budget | >=.813561792 of matching original linear RMS | Exact sufficient inequality,evaluated numerically across the strength interval and finite parameter family |
| Nonlinear endpoint pulse screen | 64/64 records pass;58 distinct trajectories | Finite prepared phases at nu=.04/.05 |
| Minimum nonlinear breathing retention | .872564120;fine .872563911 | Original undamped/nohousing nonlinear baselines |
| Maximum hub-volume mismatch | .007582052;fine .007582070 | Finite nonlinear endpoint readout |
| Residual absolute shell-shape RMS ratio | .0425850–.0967082 | Finite nonlinear endpoint readout |

At nu=.04 the minimum nonlinear retention is88.180%;at nu=.05 it is87.256%. The64 records consist of32 specified case IDs per endpoint;exact duplicate physics/preparations are reused,leaving58 trajectories. These pulse phases maximize **linear ringdown energy**,not nonlinear volume error. The linear breathing bound covers the whole allowed housing-energy ball;the nonlinear pulse checks do not.

## Exact / conditional mathematical results

1. The reference mean-volume gradient is l_alpha=l_C=0,l_Xi=r_i/(4R²),verified in Q(sqrt5) by summing oriented cell-volume derivatives. It is the linearized mean observable,distinct from finite volume and mismatch.
2. The continuous allowed g,k box has static compliance lK^dagger l^T<=**930/2513**. Positive energy therefore gives an all-phase perturbation bound RMS(delta mean volume)<=sqrt(2E_h*930/2513). This is valid for the full linear assembly,any positive masses and nonnegative losses,independently of the finite numerical case family.
3. In the **fixed-primary equilibrium-linear housing limit**,every nu in[1/25,1/20] and housing weight[.9,1.1] obeys E(100)/E(0)<**722733/1749367≈.413140**. The rational exponential bound and all coefficients are reproduced in `bounds.py`. Finite-beta return forces require the full-system calculation above.
4. Every allowed initial housing phase starts with displacement<ell0/200,speed<ell0/(20 units u),and all120 strut lengths>99ell0/200. The total-energy bound gives radial lengths>5R/8 and shell edges>2ell0/5 while the trajectory exists in the housing-strut domain. This does not establish future strut noncollapse,global existence or cell orientation.
5. As beta tends0 with bounded nu,c_f=0 and ideal gains,the primary breathing poles approach the undamped parent poles. Thus a strictly positive full-assembly exponential rate cannot be uniform over the old open beta>0 range. On the compact qualified positive box,local uniform decay exists qualitatively;this supplies no useful numerical deadline or nonlinear coherence bound.

## Continuous strength and the full housing scope audit

The planned old54-mode audit used nine adaptive strength nodes and450 case/node evaluations. Energy-contraction Duhamel inequalities covered the full strength interval. Its conservative envelopes were46.229% housing energy and81.356% all-phase linear breathing.

The disclosed post-campaign audit expanded the energy Gram to all90 housing modes. It adds the conserved rigid-velocity energy after the nonrigid projection;discarding it would undercount energy for arbitrary housing velocities. The coarse strength bound exhausted its17-node cap with four coverage gaps,although every node passed. This raw result remains in `full_housing_summary.json` as OPEN_OR_FAILED,with gaps and trajectories intact.

A sharper valid interpolation bound follows from unit initial energy E0=1/2 and nu0 integral(v^T Dv)<=1/2:

\[
 \|\Phi_\nu B-\Phi_{\nu_0}B\|_G
 \le |\nu-\nu_0|
 \min\{T\lambda_D,\sqrt{T\lambda_D/(2\nu_0)}\}.
\]

Evaluating that stronger inequality on the **same saved17 nodes** closes the interval,with full-housing energy upper45.667%. See `full_housing_refined.json`. No strength,threshold,initial preparation or trajectory was changed. There are850 full-housing case/node evaluations;these include the450 earlier parameter/strength pairs with a larger initial space. They are numerical calculations,not independent experiments. One duplicate constructor timing/check evaluation is separately noted in the journal.

All interpolated envelopes use float64 values and disclosed cushions. The extrema are evaluated at every cusp/pairwise affine-piece intersection,not merely on a plotting grid. This is **not verified interval arithmetic**,and the50 parameter sets do not certify the continuous uncertainty box. The refined full-housing bound and the old-sector bound use different interpolation estimates;their conservative upper values need not preserve subspace ordering.

## Nonlinear ringdown and numerical verification

| Housing-only preparation | nu | Linear energy fraction at100 | Full nonlinear fraction |
| --- | ---: | ---: | ---: |
| Worst old54-mode sector,scattered beta=.005,c_f=0 | .04 | .305754734 | .305752991 |
| Same parameter case,own worst phase | .05 | .239929054 | .239927288 |
| Worst full90-housing space,uniform beta=.05,c_f=0 | .04 | .440064969 | .440064551 |
| Same full-housing parameter case,own worst phase | .05 | .359171145 | .359171338 |

Quarter-energy old-sector reruns reduce the linear/nonlinear energy discrepancies from about1.75e-6 to about4.5e-7. The two additional full-housing phases agree within4.18e-7. This supports the small-amplitude calculation for those preparations without establishing nonlinear all-phase behavior. Nonlinear initial P,L are measured and conserved;small quadratic initial angular momentum is retained.

Two representative augmented linear ODE integrals independently check the Lyapunov pulse RMS/sensitivity assembly:changes<=3.14e-12/1.46e-12. Maximum Lyapunov residual over the qualified case/node family is2.55e-10. A separate spatial P,L centre-of-mass/inertia assembly checks the conserved rigid kinetic energy against the mass projection across all50 parameter sets;see `rigid_energy_checks.json`. These are constructor/second-method checks,not non-constructor review or empirical replication.

Across the nonlinear pulses,maximum E+heat relative residual is4.01e-11;total P/L drifts are1.36e-15/1.09e-15. Minimum sampled strut length is.491777ell0 and oriented cell-volume ratio.951748. Two sample-doubled/tighter reruns change retention<=2.10e-7 and mismatch<=1.81e-8. These sampled trajectory facts do not replace domain or orientation proofs.

NumPy2.3.5/SciPy1.17.0,float64,DOP853;precision/tolerances and all amendments are in the protocol. Frozen original20 coefficients and nonlinear baseline bytes are checked unchanged. Saved phase files identify the actual eigenspace preparation;degenerate worst eigenspaces do not specify a unique physical direction.

![Full-housing strength enclosure,linear breathing bound and nonlinear endpoint ringdowns](../../artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/jointwindow-summary.png)

The zigzag curves show the piecewise interpolation construction. Linear and nonlinear readouts use their own matching original baselines.

## Remaining gap and next discriminant

The original nu=.02,beta=.005,c_f=0 half-energy failure remains valid for that earlier design. The current window is an explicitly different FIT,with a stated energy/preparation budget. Earlier20% mass and high-friction challenge failures remain in their source artifacts. No result is silently overwritten.

The full linear housing-energy-ball calculation is now stronger than the earlier tiny single-direction check. Continuous parameter-box uncertainty,nonlinear all-phase control,future housing-strut noncollapse and actual fixture/strut inertia/routing remain OPEN. Physical tests are **UNSCORED / NOT_EXECUTED**;native UD constitutive/time selection and mainline promotion remain unchanged.

Next:construct a validated nonlinear perturbation tube for the housing-energy ball,starting with the limiting ringdown and breathing preparations,and explicitly bound future strut lengths and volume response.
