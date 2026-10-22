# Joint housing ringdown / breathing window — development protocol v1.0

Base `92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa`. All prior targets and cases are exposed. This is FIT/development, with mathematical bounds separated from numerical evaluation. Preserve the nu=.02,beta=.005,c_f=0 half-energy failure. Do not modify prior runs or models.

## Model and qualified parameter box

Use the unchanged 280-coordinate MountLoss model: mu=2,kappa=50,gamma=5,Omega=10,120 central massless housing-anchor struts with eta=nu*2beta/(5R²). Primary m,g within±5%,k within±5% of2/5; reciprocal gain errors within±1%; housing weights [.9,1.1],mean1;c_f in[0,.001]. Define a **qualified** housing mass range beta in[.005,.05]. The earlier open lower endpoint beta>0 remains a separate limiting question; do not silently replace it. Physical time/energy/length scales remain uncalibrated.

Derive (1) an exact fixed-primary / beta-to-zero housing-energy bound, (2) the uniform static compliance bound for the linear mean-volume readout, (3) an all-initial-phase readout perturbation bound, and (4) valid strength-interpolation inequalities. Explain why local decay alone does not imply half-energy at100 and why beta-to-zero,c_f=0 prevents a uniform full-assembly exponential rate. Prove only what the stated carrier/readout supports.

## Frozen parameter cases and candidate strength interval

Build56 parameter cases deterministically: the20 prior in-budget cases with exact frozen coefficients;20 copies with c_f=0;12 boundary combinations from three exposed primary realizations with beta in{.005,.05},c_f in{0,.001},using the stored ratio/housing patterns numbered1,2,3 respectively;four uniform cases from the same beta/c_f endpoints. Record exact duplicate coefficient sets instead of claiming56 independent samples. Add two uniform beta=.0005/.00005,c_f=0 limit checks outside the qualified box; these do not select the design.

Deduplicate exact coefficient sets for matrix and nonlinear execution, retaining every original case ID as an alias. Thus the64 endpoint/case pulse records need not represent64 distinct trajectories. Numerical interpolation uses explicit1e-6 cushions in energy-operator norm/readout RMS and1e-6 added to the sensitivity integral; these are disclosed numerical allowances, not verified interval arithmetic.

The **candidate** interval is nu in[1/25,1/20]=[.04,.05], selected using the prior nominal results and an analytic fixed-primary limit bound. It is a design FIT. Start numerical full-system evaluations at the interval endpoints and midpoint. At each node compute all108 initial phases of the old54-dimensional housing sector and an energy-metric contraction interpolation radius. Include the all-phase linear breathing sufficient inequality, with housing energy E_h<=E_p/40000 and E_p=(1+sum g)*(.1)²/2. Require worst housing energy fraction<=.5 at100 and lower-bounded linear breathing RMS>=.8 of the matching original undamped linear RMS.

Intersect the valid strength neighborhoods across all56 cases. If gaps remain, evaluate the midpoint of the largest uncovered interval, with a maximum17 distinct strengths. Ties use the smaller midpoint. This is deterministic numerical subdivision, not outcome-blind evaluation. If a node fails, report it; if coverage remains incomplete at the cap, report OPEN. Do not add strengths outside the candidate interval or silently narrow a failed interval. The interpolation formulas may be exact while their float64 inputs remain numerical; no interval-arithmetic or full continuous-parameter-box certificate is implied.

## Nonlinear nonzero-housing checks

At **both interval endpoints**, integrate32 cases: the20 original in-budget cases plus the12 additional boundary combinations. Initialize each with alpha=.1,other primary/relative strains and velocities0,plus its own worst linear housing phase scaled to **E_h=E_p/40000**. Thus64 full nonlinear pulse trajectories explicitly contain housing motion. Match original undamped/nohousing nonlinear baselines by primary realization. Use the inherited80% breathing /5% hub-volume mismatch /50% residual-shape screen. A worst ringdown direction need not be a worst breathing direction; the linear all-phase bound and nonlinear finite preparations have different scopes.

Also integrate housing-only worst phases for the worst linear case at each endpoint,using E_h=E_p/40000; compare energy fractions with the linear prediction. Repeat at quarter energy to examine small-amplitude sensitivity. Tighten and sample-double the worst pulse mismatch/retention trajectories (deduplicate same case). Verify total E+heat,P,L and sampled member/strut lengths and cell orientation. Retain failures.

Use float64 matrix exponentials/SVD/Lyapunov solves; record residuals and a second calculation of representative readout integrals. Full nonlinear DOP853 rtol1e-10/atol1e-12,u0..100,2001samples; refined2e-12/2e-14,4001samples. Tiny housing-only atol1e-15. Independent trajectories may use two CPU processes; no LLM delegation/independent review is claimed. Capture all code, frozen cases, bound derivations, receipts, coverage nodes/intervals, results and limitations before integration.

## Post-campaign scope audit — all90 housing directions

After the declared old54-sector campaign passes,explicitly audit the remaining36 housing directions. Use all180 initial housing position/velocity coordinates,including their conserved linearized rigid kinetic energy. Reuse the observed nine strength nodes and50 unique parameter sets;calculate full-housing energy-Gram maxima. If ringdown coverage gaps remain,subdivide the largest gap with the same deterministic rule,up to17 total audit nodes,inside the unchanged [.04,.05] interval. This is an exposed scope extension,not independent validation or strength retuning. The existing all-phase breathing bound already covers this larger energy ball. Report any failed extension separately from the completed old-sector result.

At each endpoint,run the worst full-housing phase once in the nonlinear model at E_h=E_p/40000,alpha0=0. Total initial P,L may be nonzero;include their energy/conservation rather than projecting away rigid kinetic energy. These two additional ringdowns do not expand the64 pulse records or establish nonlinear all-phase behavior.

After observing gaps in the coarse full-housing strength interpolation,derive the sharper valid bound min(T*lambda_D,sqrt(T*lambda_D/(2nu0))) from the unit initial energy and dissipated-energy integral. Evaluate it on the same saved full-housing nodes in a separate `full_housing_refined.json`;preserve the original coarse audit and its17-node cap status. No design parameter,threshold,initial preparation or simulated trajectory is changed. This analytic refinement is exposed development,not independent confirmation.
