# UD Discovery — Reduced moving-propagator validation and jerk-gate audit (025)

**RESULT — EXACT / CONDITIONAL mesh Taylor certificate; NUMERICAL / DEVELOPMENT source-matched four-sector derivative audit; FAILED coarse global log-norm proof. Validated continuous-time u100 gain and nonlinear phase-ball remain OPEN.**

## Question, typed objects, provenance

The physical question is whether the existing passive 3D icosahedral surrogate, with original symmetric moving pulse alpha(0)=1/10, uniform primary properties, beta=1/200, nu=1/20, cf=0, and enlarged initial housing energy E_h <= 51/20000000, has a certified all-180-initial-phase non-affine linear response small enough to support a future nonlinear u100 bootstrap. Model time u is a dimensionless, uncalibrated mechanical evolution parameter. Reference space is Euclidean R^3. The state is 280 configurations and 560 mechanical phase coordinates, plus a separate heat ledger. Initial phase a is in R^180 with Euclidean norm <=1 after mass-energy normalization. The readout L(u)=sqrt(2E_h) C Phi(u,0) B is the rank-24 non-affine shell position operator from a to R^24. Its derivatives D=L', A=L'', J=d3L are operator-valued continuous-time quantities. Gains are induced spectral norms, including the complete initial phase ball, **not** 180 sampled directions.

The frozen 024 A5 reduction decomposes the output into real irreps 3 + 3prime + 2(4) + 2(5) and the full mechanical configuration into multiplicity ranks 17,14,18,22. Symmetry is exact only for the **uniform moving baseline**. Source main read-only: `060e9187d88da7062ff4edce5513efabd1b100ff` (six source model blobs unchanged), original run: `a5-reduced-gain-024`; research branch prior head: `27b95110eacbc9beaa5326f050c2b4b0c440b02b`. The claim `claims/icosahedral-phasewindow-20261022` remains held by session `phasewindow-20261022-gpt6-7c41`. Separate owner PR44 untouched. No mainline writeback.

## Exact Banach-space Hermite/Taylor interpolation: improved proof obligations

For the uniform mesh t_j=j/40, j=0,...,4000, every t in [0,100] lies within delta=1/80 of some node. For the **true** moving-pulse operator L, suppose validated enclosures establish at every node:

    ||L(t_j)||_2 <= G,  ||L'(t_j)||_2 <= V,  ||L''(t_j)||_2 <= W,

and a continuous-time validated bound `sup_t ||d3L(t)||_2 <= J`. The fundamental theorem of calculus with Banach-valued third derivative gives the exact inequality

    sup_t ||L(t)||_2 <= G + delta V + delta^2 W/2 + delta^3 J/6.

A **robust** recommended verification gate is G=1/12500 (=0.00008), V=7/10000 (=0.0007), W=1/125 (=0.008), and J=1. The exact fractional bound is:

    ||L(t)||_2 <= 6889/76800000 = 0.0000897005208333333,
    ||L'(t)||_2 <= 281/320000 = 0.000878125,
    (1/40)-sup||L|| >= 1913111/76800000 = 0.02491029947916....

For a **tighter but harder-to-validate** alternative, G=7/100000, V=61/100000, W=31/5000, J=1 yields

    ||L(t)||_2 <= 30119/384000000 = 0.0000784348958333333,
    (1/40)-sup||L|| >= 9569881/384000000 = 0.02492156510416....

With the tight nodal G,V,W gates, even J<8406/125=67.248 suffices to put all continuous positions below 1/10000. These are EXACT mathematical implications *if their true-ODE premises are verified*. Neither their node premises nor the jerk bound has been validated by interval/defect error enclosures. No statement here upgrades the sampled numerical gains into a theorem.

This is an alternative to the 024 gate requiring a continuous acceleration bound below 0.01: a much more permissive continuous jerk bound plus three *nodal* values can suffice for continuous position gain. The small absolute h makes the h^3 jerk term forgiving.

## Recomputed full 180-phase sector results — NUMERICAL, not enclosures

Replayed the frozen source implementation with cubic coefficient grids 0.1 and 0.05, DOP853 relative tolerance 1e-10, and 4001 output times, using forward fundamental propagation in each isotypic multiplicity slice. The sample maxima for the *refined* 0.05 coefficient grid are:

| A5 sector | config. rank | position | velocity | acceleration | jerk |
|---|---:|---:|---:|---:|---:|
| 3 | 17 | 3.95777105e-05 | 0.00028616153 | 0.00291421861 | 0.0297348731 |
| 3prime | 14 | 6.2307142e-05 | 0.000545709768 | 0.00531751182 | 0.0522462674 |
| 4 | 18 | 6.6742004e-05 | 0.000608074567 | 0.00614434852 | 0.062120111 |
| 5 | 22 | 5.13130819e-05 | 0.00033955369 | 0.00358059826 | 0.0387193808 |

All four outputs reach their largest sampled value in the **4 sector**; specifically jerk ~0.062120111 at u=4.4. This is a target-exposed, numerical diagnostic. Relative source spline-derivative versus direct source finite-difference checks in 16 sector/time combinations have max K derivative spectral differences ~0.0011085 on coefficient step 0.1 and ~0.0001982 on step 0.05. Thus a sampled spline jerk is not a verified *true-source* continuous jerk bound.

An independent operator-valued central difference of the spline acceleration matrix tested four times in each of the four sectors (16 comparisons, central step 1e-4). Its maximum relative discrepancy against the analytic cubic-spline jerk expression was 3.5992e-7. Coefficient step 0.1 versus 0.05 produces jerk peak differences smaller than 2.1e-9 in gain units. These are useful implementation/mesh convergence checks; the finite differences are NOT rigorous enclosures of interpolation and DOP853 errors.

## Attempted quantitative proof via a fixed-energy logarithmic norm — FAILED METHOD

For each reduced first-order system y' = A(u)y, consider fixed SPD H=diag(S_ref + rho M, M) where S_ref=M K(u=0) is the frozen symmetric stiffness and rho is an adjustable stabilizer. A logarithmic norm at time u is max eigenvalue of H^(-1/2) (H A + A^T H) H^(-1/2)/2. Its integral of positive part is a sufficient exponential growth majorant only after rigorously enclosing the true A(u). Here we used 401 *sampled* moving source matrices and ordinary eigenvalue arithmetic, so the reported numbers are NUMERICAL DIAGNOSTICS and NOT certified supremum integrals.

With selected positive gauges, numerical integrated gamma samples are approximately 34.76 in sector 3 at rho=.3, 4.17 in sector 4 at rho=.1, and 5.85 in sector 5 at rho=.1. Even the smaller e^4.17 and e^5.85 amplification factors are much too coarse for a useful small-gain error enclosure. The frozen 3-sector K(u=0) has an eigenvalue about -0.09964, so a zero-gauge frozen potential is not positive. These findings **reject only the tested fixed-metric majorant**, not the positivity/stability of the actual pulse and not the possibility of a better co-moving metric or defect-controlled method. No physics failure is inferred.

## Exact a posteriori defect identity, and required missing data

Let A(t) be the *true* reduced linear generator, X(0)=I its exact fundamental matrix, and X_hat a continuously differentiable approximate propagator (for example from an ODE dense interpolant); define residual R(t)=X_hat'(t)-A(t)X_hat(t). Then the exact error has variation-of-constants representation

    X(t)-X_hat(t) = - integral_0^t Phi(t,s) R(s) ds

when X_hat(0)=I, with an additional Phi(t,0) initial error term otherwise. This yields a rigorous enclosure only if BOTH R is enclosed with directed rounding and the true propagator or a rigorously dominating Green kernel Phi(t,s) is bounded. Replacing Phi by a numerically computed matrix without a separate verified defect/Volterra bootstrap is circular. The tested fixed-energy log norm is too loose to supply the needed kernel bound.

A realistic next strategy is interval time-slab propagators in the four symmetry sectors with QR/positive-metric reconditioning, source baseline interval Taylor models, and a posteriori Green-kernel error bounds; exploit the close sampled margin and preferentially certify the limiting 4 sector. Prove all node and jerk premises for the **original source** rather than merely the spline ODE.

## Evidence boundaries and further dynamics

The robust gate is conditioned on the full all-180-linearized housing phase ball, not the nonlinear phase ball. An actual nonlinear orientation theorem would also need an independently bounded nonlinear remainder smaller than the unused 1/40 margin, a positive housing-strut domain throughout u100, and a verified comparison with the original full moving pulse. Material-property scatter, 80% breathing, 50% ringdown, SI calibration and UD native dynamics remain OPEN. All threshold and candidate choices are post-exposure FIT / development, not independent physical predictions; published prior negative controls (energy-only singular states and A5 nonlinear selection-rule width) remain valid.