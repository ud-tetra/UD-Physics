# 3D UD global cell-collapse energy barrier — exploratory audit v1

**STATUS: EXACT CONSTRUCTIVE WITNESS / NUMERICAL SEARCH / GLOBAL LOWER BOUND OPEN.**

Session `phasewindow-20261022-gpt6-7c41`, task `icosahedral-phasewindow-20261022`, held claim `refs/heads/claims/icosahedral-phasewindow-20261022`, isolated Discovery branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Verified read-only main `467e2208fba9da086535bd5b8a6a07f6d6f8e08b`. Underlying `model.py`, `network.py`, `hardware.py`, `mountloss.py` blobs were checked identical to previously imported revisions. No mainline export.

## Question

Can all 20 centre-to-exterior-face tetrahedra remain positively oriented for all time at the *original* heart-pulse amplitude `alpha0=1/10`, without imposing a finite-time velocity tube, by proving a global lower bound on the conservative energy needed to flatten any one cell?

The actual initial pulse bound is `E_p + E_h <= 1360051/20000000 = 0.06800255` with the previously enlarged housing phase allowance. A lower bound on the *global* conservative energy of any flattened cell strictly above this would yield an all-time cell-orientation theorem by energy dissipation and continuity. It would **not** by itself give housing-strut noncollapse or breathing coherence (the total energy sublevel already contains housing-strut singular configurations).

## Typed model

12 exterior positions `X_i` and a centre `C` are points in Euclidean `R^3`; translation sets `C=0`. Outer reference vertices form a regular icosahedron of edge length 1, circumradius squared `R²=(5+sqrt(5))/8`. For each shell vertex `s_i=|X_i|/R-1`, and each of 30 graph edges `e_ij=|X_i-X_j|-1`. Scalar heart coordinate `alpha` is retained and optimized, not mistaken for time. The unchanged conservative primary energy is

`U_primary = 1/2 [ alpha² + sum_i s_i² + sum_i g_i(s_i-alpha)² + sum_{(i,j)} k_ij e_ij² ]`.

Auxiliary port storage and housing midpoint storage can both be set to zero for a static configuration by choosing device coordinates equal to their port differences and housings at corresponding midpoints. All kinetic energies are nonnegative and vanish at rest. Since the qualified box has `g_i>=19/20` and `k_ij>=19/50`, any full mechanical configuration has potential energy at least the same `U_primary` evaluated at the lower coefficients `g=19/20`, `k=19/50`, for its given positions and alpha. Thus a proved global bound for that lower-coefficient model would apply throughout the qualified box.

Minimization over the scalar alpha is exact:

`alpha_opt = (19/20 * sum_i s_i)/(1+12*(19/20))`.

By icosahedral vertex/face transitivity it suffices to study one fixed original exterior face in the uniform lower-coefficient surrogate. Let its three vectors from the centre be `a,b,c`; flattening means `det[a b c]=0`. Positive/negative oriented volume under the original face convention changes sign only by passing through zero.

## Numerical global-framework exploration — NOT a global bound

A 72-start SLSQP calculation minimized `U_primary` over all 36 shell coordinates (with center translation fixed), after eliminating alpha, subject to `det[a b c]=0`. Inputs: NumPy 2.3.5, SciPy 1.17.0, random seed 20261022, varied exact face-flattening initializations and Gaussian perturbations, analytic energy and determinant gradients, tolerance `ftol=2e-13`, at most 550 iterations per start. All 72 optimizations converged; 59 ended within `1e-6` of the lowest observed energy. Lowest reported candidate energy `0.12442609483988352`; constraint residual `2.55e-16`, tangential stationarity residual `1.02e-7`. A second independent parameterization imposed `c=p*a+q*b` identically, and L-BFGS-B recovered `0.12442609483988154`.

The numerical candidate is about **1.830 times** the original pulse energy ceiling, but this is **NOT** a proved lower bound: unexplored disconnected configurations and other local minima may have lower cost. Repeated same-runtime numerical searches do not constitute global optimization or independent replication.

## Exact positive-energy *collapsed* witness: a valid upper bound only

The frozen `flat_witness.json` lists 11 shell vertices with exact rational coordinates (on a grid of denominator 10^6), and gives the third face vertex as an exact rational linear combination of the other two, ensuring `det[a b c]=0` **exactly**. Choose rational `alpha=-9/500`, `g=19/20`, `k=19/50`. The reproducible `verify_witness.py` constructs the 30 original icosahedral graph edges and uses integer-square-root rational enclosures to bound *every* radial and edge length, with no floating-point assumption in the inequality. It verifies:

- A genuinely flattened original cell: exact determinant `0`.
- All 12 spokes, 30 shell edges and 120 housing-to-anchor paths at static midpoint housing positions are strictly positive; the minimum strut squared is recorded as a positive rational.
- A strict rational **upper bound** `U_primary < 1/8 = 0.125` for this particular static collapsed configuration. This is larger than `0.06800255` and therefore is *not* a reachable-energy counterexample to the original pulse.

This exact witness is a constructive **upper** bound on the infimum energy required to flatten a cell. It must not be inverted into a lower bound.

## Exact local six-member counterexample to a *local-only* energy proof

Ignore all edges outside the selected face and its three centre spokes. Place the three face vectors of length exactly `R` in one plane at angular positions `(-pi/4,0,+pi/4)` around the centre. Then all three spoke strains are zero and the face edge lengths are, exactly, `R sqrt(2-sqrt(2))` twice and `sqrt(2)R` once. With `alpha=0` and `k=19/50`, the **local six-member** elastic energy is

`E_local = (19/100) [ 2(R sqrt(2-sqrt(2))-1)^2 + (sqrt(2)R-1)^2 ]`.

Rational interval checks give `E_local < 0.050747479 < 0.06800255`. This is an exact statement only about those six local members. Completing the icosahedral shell introduces the other 27 edges and 9 spoke energies, so it is **not** a global collapse witness below the pulse energy. It shows why a certification based only on the six cell lengths cannot solve the full-amplitude problem; global network compatibility is essential.

## Verification and limitations

- `barrier_audit.py`: 72 deterministic numerical constrained optimizations; full result and all start outcomes in `barrier_results.json`. Independently enforced coplanarity formulation included in code. NUMERICAL / development.
- `flat_witness.json` + `verify_witness.py`: exact rational coplanarity and rational interval upper energy `E<1/8`, plus local-only witness `E_local<E_p+E_h`. EXACT / conditional on imported conservative energy.
- `independent_check.py`: separately reconstructs static energy and finite-difference tests energy/determinant gradients. Same-runtime self-check, **not independent peer review**.
- Source baseline is a versioned read-only import. No numerical fit to physical measurements, no physical time scale, and no hypothesized 4D structure.
- This investigation has **not** proved any global energy lower barrier above the original pulse energy, has **not** certified all-time oriented volumes, has **not** recovered PR #44 forced-Green data, and has **not** certified `u=100` nonlinear breathing/ringdown.
- Parameter selection exposed: reference pulse and constraints already inspected; `g,k` set to their allowable minima to maximize chance of a low barrier; face choice equivalent only because this lower-coefficient model is uniform. Search freedom: 72 numerical starts, seven distinct local stationary energy values in these attempts; no systematic global certification.

## Next discriminant

**Priority 98/100:** Formulate an independently verified global icosahedral length-energy barrier certificate (`U_min(flat cell) > 1360051/20000000`), perhaps using a semidefinite Gram completion/SOS or a validated branch-and-bound of the constrained 36-coordinate geometry. The upper witness `<1/8` and the numerical candidate near `0.124426` are useful bracket/test inputs, not proof premises. Continue the complementary time-domain full-Green approach under PR #44 ownership without overwriting its files. If a global barrier certificate fails, preserve the counterexample and pivot to a full nonlinear forced-Green tube.