# UD Discovery — exact all-time symmetric-pulse geometric benchmark

**RESULT: EXACT / CONDITIONAL in an invariant 3D subfamily.** Full pulse and all 180 housing phases in the scattered-material case remain **OPEN**. **EXACT / FAILED:** non-affine shell control and the total-energy sublevel alone cannot bound every housing-to-anchor length. This record is a target-exposed, lower-dimensional control case; not independent physical evidence and not the separately claimed PR #44 Green recovery.

## Question and provenance

Can an actual nonlinear moving reference trajectory, rather than an artificial static equilibrium, have an **all-time strictly positive length domain**, so that a subsequent perturbative bootstrap can be formulated relative to it? Can bounding the projected non-affine shell observable `Z` alone guarantee the moving-axis housing domain?

Original full passive surrogate: 280 configuration and 280 velocity coordinates plus one heat ledger, 12 icosahedral shell vertices, centre, 30 housing vectors, 150 auxiliary scalars, 120 current-axis viscous paths. Length is in reference shell-edge units; time `u` is internal Newtonian model time, not physical clock time. Imported read-only GitHub repo `ud-tetra/UD-Physics`, main `a7c6b123c144d37fb7a3fcefed36a3ff764af027`; the held 3D claim is `icosahedral-phasewindow-20261022`, session `phasewindow-20261022-gpt6-7c41`, isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Original force-law versions `experiments/icosahedral-free3d/model.py` c480411..., `experiments/icosahedral-multiport/network.py` 010629..., `experiments/icosahedral-tolerances/hardware.py` 663ee8..., `experiments/icosahedral-mountloss/mountloss.py` aa4ad2...; previous 018 convex phase-domain result imported read-only. Distinct PR #44 held by another task is untouched.

## Theorem A — symmetric nonlinear invariant family

Let `v_i` be the twelve regular icosahedron vertices in Euclidean R³ with exterior edge length 1 and `R²=(5+sqrt(5))/8`. For each of the 30 shell edges `e={i,j}` define `m_e=(v_i+v_j)/2` and `M²=|m_e|²=(3+sqrt(5))/8`.

**Assumptions (not the full qualified box):** uniform primary masses `m_i=1`, spoke couplings `g_i=1`, exterior edge springs `k_e=2/5`, unit reciprocal device gains, uniform housing weights 1, positive beta (including [1/200,1/20]), any nonnegative damping parameters including nu in [1/25,1/20] and cf in [0,1/1000]. Original heart initial `alpha(0)=1/10`, reference shell at `b(0)=1`, primary velocities 0; all auxiliary scalar positions and velocities initially zero. **Only radial-symmetric housing preparations:** for all 30 edges `H_e(0)=c(0)m_e`, `dot H_e(0)=dot c(0)m_e`, with housing energy at most `E_h=51/20000000`. This is a 2-parameter initial housing sector, **not** the 180-dimensional housing-phase ball, and is not valid for scattered parameters/gains.

The full ODE leaves invariant

`C=0; X_i=b v_i; H_e=c m_e; z_p=dot z_p=0`, with scalar generalized coordinates `alpha,b,c` and their velocities. Reason: all twelve spoke and all 30 exterior length strains equal `b-1`; every reciprocal difference transmission with gain=1 therefore has zero port error. The remaining primary elasticity, axial damping, housing midpoint springs and four-anchor moving-axis viscous law are equivariant under the full icosahedral rotation group; the site stabilizers force each shell and housing acceleration into its reference radial span. The centre force is zero by symmetry. Local uniqueness makes this family invariant until any possible domain boundary.

Write `s=b-1` and `M_c=12 beta M²/R²>0`. The exact mechanical energy (the auxiliary storage vanishes in this sector) is

```
E = 1/2[ alpha_dot² + 12 b_dot² + M_c c_dot² ]
  + 1/2[ 13 alpha² - 24 alpha*s + 36 s² + 100 M_c (c-b)² ].
```

Completing the square,

```
U_primary = (13/2)*(alpha-12*s/13)² + (162/13)*s².
```

For the original uniform heart pulse, `E_primary(0)=13/200`. Including the previously exposed enlarged housing-phase budget gives `E(0)<=13/200+51/20000000=1300051/20000000`. Passivity ensures `E(u)<=E(0)` on any regular interval. The exact rational check

`1300051/20000000 < (162/13)*(3/40)²`

therefore yields `37/40<b(u)<43/40` for **all** times on the maximal solution.

For an edge `e={i,j}`, let `w=(v_i-v_j)/2`, with `w·m_e=0`, `|w|²=1/4`. The two endpoint strut lengths satisfy

```
|c m_e - b v_i|² = |c m_e-b v_j|²
                   = M²(c-b)² + b²/4 >= b²/4.
```

For either opposite adjacent-face anchor `k`, `m_e·v_k=R²-1/2` and its component perpendicular to `m_e` has squared norm exactly `M²`; hence

```
|c m_e-b v_k|² = M² b² + M² [c-b(R²-1/2)/M²]² >= M² b².
```

Since `M²>1/4`, every one of the **120 housing-to-anchor lengths** is strictly greater than `b/2>37/80` for all times, independently of the symmetric housing displacement `c`. All primary spokes have length `bR>0`, shell edges have length `b>0`, and the 20 oriented centre-to-face cell volume ratios equal `b³`, so

```
(37/40)^3 < V_f(u)/V_f(0) < (43/40)^3
         = lower 50653/64000, upper 79507/64000.
```

The mount energy controls `c-b` and positive masses bound velocities. The state remains bounded on any finite interval and all divisors in the smooth ODE stay positive; continuation gives a **global-in-u** solution with these lower bounds. Neither the ratio >80%-RMS versus undamped baseline, nor housing half-energy ringdown, is implied.

### Explicit reduced dynamics and passivity check

For beta, nu, cf as above, set `eta=(2/5)nu beta/R²`, `lambda=(R²-1/2)/M²`, `M_c=12 beta M²/R²`,

```
L_e = sqrt(M²(c-b)² + b²/4),
L_o = sqrt(M²[(c-lambda*b)²+b²]).
```

Let `r_e=dot L_e`, `r_o=dot L_o` and use the corresponding scalar gradients. The exact reduced dissipative equations are

```
alpha_ddot = -13 alpha + 12(b-1),
12 b_ddot = -36(b-1)+12 alpha +100 M_c(c-b)
            -30 cf b_dot -60 eta[(dL_e/db)r_e+(dL_o/db)r_o],
M_c c_ddot = -100 M_c(c-b)
            -60 eta[(dL_e/dc)r_e+(dL_o/dc)r_o].
```

Their energy identity is `dE/du = -30 cf b_dot² - 60 eta(r_e²+r_o²) <=0`. These are the original forces restricted to the invariant family, not a separately imposed surrogate damping law. The absorbed heat ledger accounts for the integrated loss.

## Theorem B — exact negative control on a proposed general bootstrap

Even with shell coordinates **exactly at the regular reference** (so projected non-affine `Z=0` and all cell orientations positive), the full mechanical energy sublevel does **not** exclude strut collapse for arbitrary housing configurations. Fix beta `1/200`, weight1, all shell/auxiliary positions at rest, alpha0, and initial velocities zero. Choose one housing at

`H_e=m_e+(1-epsilon)(v_i-m_e)` with `0<epsilon<1`.

The housing-to-endpoint distance is `epsilon/2` while the energy in its midpoint spring is

`U_mount=(1-epsilon)²/(40 R²) <1/36<13/200`.

For this static family choose `alpha=0` so that all other energy terms vanish. The configuration is **not asserted reachable from the prepared pulse**, and it is not in the symmetric housing family from Theorem A. It proves that `Z` and energy alone cannot bound the strut lengths in the general phase-ball bootstrap: a **separate housing-relative tube** and a time-varying propagator are indispensable.

## Verification and target exposure

- **EXACT:** `exact_symmetry.py` checks rational completion of squares and energy inequalities, and independently expands the key Q(sqrt5) geometric identity; `zero_Z_strut_obstruction.py` checks the separate negative control.
- **EXACT / second-implementation:** `independent_symmetry.py` independently reconstructs the 12 reference vertices, all 30 edges, 20 faces, and all 120 anchor identities with SymPy; checks the energy completion of squares.
- **NUMERICAL / constructor:** `symmetry_dynamics_check.py` checks 12 random-ish scalar-state/beta/nu combinations against the archived full560-state `nonaffine_audit.py` source reimplementation (not an original direct checkout). Maximum tangency/acceleration discrepancy ~`1.7e-14`. It integrates the 6-state reduced dynamics to `u=100` at beta=.005, nu=.05, cf=0 with a radial housing initial energy at the budget. Numerical min shell scale ~`0.98375`, strut min ~`0.49188`, and compares the independently embedded 560-state solver over `[0,4]`, max discrepancy ~`9.91e-12`. These sampled values are consistency tests, **not prerequisites to the all-time exact theorem**, and are not independent empirical replication.
- **FIT / DEVELOPMENT:** The original alpha pulse, enlarged housing budget, 80%-volume and 1/40 projected threshold were known targets; the symmetric subfamily was selected as a control-case bridge after the general bootstrap difficulty became known. No holdout physical data, no hardware demonstration, no native UD time or constitutive bridge.
- **OPEN:** Scattered material coefficients, any asymmetric or 180-dimensional housing preparation, nonlinear `u100` projected response and strut domain in that full phase family, breathing RMS, hub-volume matching, half-energy ringdown, and physical realization remain unproved.

**Next discriminant (priority 99/100):** Put a dynamically bounded error tube around this **moving symmetric baseline**, simultaneously controlling primary/housing coordinate deviations and the projected non-affine shell sector. A sufficient geometric criterion is `|H_e-H_e^sym|+|X_a-X_a^sym|<37/80` for every strut, while full orientation requires a compatible deformation readout. Attempt certified time-dependent Green plus quadratic bootstrap; report a failed majorant if necessary. For scattered source-frozen parameters the baseline is nonsymmetric, so repeat the domain analysis about that actual trajectory, rather than assuming symmetry.
