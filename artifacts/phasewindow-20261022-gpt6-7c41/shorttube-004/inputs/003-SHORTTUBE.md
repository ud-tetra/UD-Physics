# Original-amplitude all-housing-phase nonlinear short-time safety

**RESULT: EXACT / CONDITIONAL.** This is a new a-priori domain and orientation certificate for the original amplitude `alpha(0)=1/10` of the *unchanged* 280-position/560-mechanical-phase UD Discovery `MountLoss` surrogate. It is not an all-time theorem, a nonlinear ringdown/coherence certificate, a spacetime identification, or an experimental measurement.

## Provenance, assumptions, and target exposure

- Repository `ud-tetra/UD-Physics`; current integrated read-only main `7ae79d882e44446c7b4aefd4fdbe9ee781b9bafe` (2026-10-22), owning Discovery research branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41` (prior head `0391afb4617db89690a5eaee9b5fc6c0ae3c9b70`). The parent model, formula, and bounds were originally integrated at `ce89a9cd15439463d9a64d983d91c22ea4368726` and earlier.
- Read-only sources: `experiments/icosahedral-mountloss/{README.md,mountloss.py}`, `experiments/icosahedral-tolerances/hardware.py`, `experiments/icosahedral-free3d/model.py`, `experiments/icosahedral-nonlineartube/README.md`, and `experiments/icosahedral-phasewindow-20261022/PULSE_SAFETY.md` on the owning branch. A separate held task / Draft PR #44 owns the forced-Green/alignment reconstruction; no files in that task are edited.
- Positive masses/spring storage, reciprocal loss with nonnegative Rayleigh dissipation, positive housing lengths on the local ODE domain. All retained coordinates: 1 heart scalar, 13 free 3D primary points, 150 auxiliary coordinates, 30 free 3D housings; 280 configurations, 560 phase variables, plus heat bookkeeping. The primary shell is **not** fixed or projected to a rigid quotient.
- Qualified continuous parameter box: primary masses and spoke strengths in `[19/20,21/20]`, shell springs `k_e in[19/50,21/50]`, beta in `[1/200,1/20]`, housing weights `w_e in [9/10,11/10]` with mean 1, `Omega=10`, housing damping `0<=nu<=1/20` (includes the fitted `[1/25,1/20]` window), `c_f>=0`, and the existing positive device settings/gains.
- Initial conditions: scalar `alpha0=1/10`; primary points at reference and primary velocities zero; auxiliaries reference/rest; each housing has *arbitrary* initial displacement and velocity with **total** housing energy `E_h<=51/20000000=3 E_p,ref/80000`. The extra housing energy ball includes all 180 phase directions and their rigid kinetic energy.
- Internal units: shell edge length `ell0=1`, physical clock `u=t/t0`; no calibration. The original `0.1` pulse and tests were exposed before this analysis. The rational deadline `T=2/5` was selected from a sufficient inequality after inspecting it (**FIT/development**, not an independent prediction). No model parameter was retuned and no empirical data were used.

## 1. Universal energy and speed bounds

The parent exact balance is `E'(u)=-P_loss(u)<=0`. With 12 spoke strengths `g_i<=21/20`:

```
E(u) <= E0 <= (1+sum_i g_i) alpha0^2/2 + E_h
             <= 34/5 * (1/10)^2 + 51/20000000
             = 1360051/20000000.
```

Reference squared circumradius `R²=(5+sqrt5)/8 <1`. Primary point masses `m_i/R²>19/20`, housing masses `m_he=2 beta w_e/(5 R²)>9/5000`, and housing mount stiffness `k_he=Omega² m_he>9/50`. The *positive* kinetic and mount energy terms yield, for every future time on the positive-length existence domain,

```
|X'_a(u)| < 2/5                   (all 13 primary points),
|H'_e(u)| < 9                     (all 30 housings).
```

The **separate initial housing energy** gives substantially better startup bounds:

```
|H_e(0)-A_e(0)| < 1/180,
|H'_e(0)| < 3/50,
A_e(u)=(X_i(u)+X_j(u))/2.
```

Each primary point and midpoint therefore obeys `|X_a(u)-X_a(0)|<=(2/5)u` and `|A_e(u)-A_e(0)|<=(2/5)u` (strict for positive u). The positive primary spoke/edge potential also bounds each spoke strain by `<2/5` and each exterior-edge strain by `<3/5`; none of the corresponding 42 member lengths can vanish on any existence interval.

## 2. Duhamel bound on all housing displacements

The **actual** housing equation for a housing at the midpoint of edge `e` is

```
H_e'' + Omega² H_e
   = Omega² A_e(u) - (eta/m_he) sum_(a in anchors(e)) n_ea r_ea,
eta/m_he = nu/w_e,
r_ea = n_ea · (H'_e-X'_a),
n_ea = (H_e-X_a)/|H_e-X_a|.
```

There are exactly four anchors per housing, and their forces are reciprocal; no fixed-axis damping approximation is used. As long as strut lengths are nonzero, the unit-vector property, speed bounds, and `nu/w_e<=1/18` imply

```
|(eta/m_he) sum_a n_ea r_ea|
  <= (1/18) 4 (9+2/5)
  = 94/45.
```

Write `A0=A_e(0)` and `D0=H_e(0)-A0`. Duhamel's exact oscillator formula, with `Omega=10`, yields

```
H_e(u)-A0 = cos(10u) D0 + sin(10u)/10 H'_e(0)
    + 10 integral_0^u sin(10(u-s)) [A_e(s)-A0] ds
    - (1/10) integral_0^u sin(10(u-s)) F_e(s) ds,
|F_e(s)|<=94/45.
```

Apply `|cos|<=1`, `|sin x|<=min(|x|,1)`, and `|A_e(s)-A0|<=(2/5)s` (equality at s=0 only). For `0<=u<=1/10` this gives

```
|H_e(u)-A0| < 1/180 + (3/50)u + (20/3)u³+(47/45)u².
```

For `u>=1/10`, integrate the two explicit polynomials obtained by splitting the majorant at `u-s=1/10`:

```
|H_e(u)-A0| < 1/180+3/500
       + (2u²-u/5+1/150)
       + (47/225)(u-1/20).
```

Every reference strut has length at least `1/2` (endpoint anchors exactly `1/2`; the opposite face vertices at `sqrt(3)/2`). Using also `|X_a(u)-X_a(0)|<=(2/5)u`, the triangle inequality proves for every one of 120 struts:

```
|H_e(u)-X_a(u)| > 1/2 - [1/180+(23/50)u+(47/45)u²+(20/3)u³],
                                                   0<=u<=1/10;
|H_e(u)-X_a(u)| > 1/2 - [7/900+(92/225)u+2u²], 1/10<=u<=2/5.
```

Both right-hand sides decrease on the indicated nonnegative intervals and agree at `u=1/10` (equal `647/1500`). At `T=2/5`, the second lower bound is **exactly** `13/1500>0`. At the more conservative `u=39/100`, it is `257/9000>1/40`. The argument applies jointly to *every* allowed initial housing phase and every set of qualified parameters, including `c_f=0` and the low-mass endpoint. The damping force bound uses only instantaneous positivity of unit directions and the global energy bound; it does not pretend that the dampers have fixed directions.

## 3. Every cell preserves oriented volume through T=2/5

At reference the 3x3 matrix `A_ref=[X_a-C,X_b-C,X_c-C]` for each oriented tetrahedral cell has `sigma_min(A_ref)=1/sqrt(2)>7/10`. Every primary point moves by `<=(2/5)u`, so each of the three relative spoke columns moves by `<=(4/5)u`. Consequently, for all `u>=0`,

```
||A(u)-A_ref||_F <= (4sqrt(3)/5)u <= (7/5)u,
||A_ref^{-1}(A(u)-A_ref)||_2 <= 2u <= 4/5 <1.
```

The first two inequalities are strict for `u>0`, while equality at the zero displacement is allowed at `u=0`.

The matrix remains nonsingular, with determinant sign continuous from the initial positive orientation. All singular values of `I+A_ref^{-1}(A-A_ref)` lie between `1-2u` and `1+2u`. Hence each normalized oriented volume obeys the **non-strict** time-dependent enclosure

```
(1-2u)^3 <= V_k(u)/V_k,ref <= (1+2u)^3
```

for every `0<=u<=2/5`. The bounds are strict for `u>0` under the stated strict velocity majorants, but at `u=0` both sides equal exactly one. In particular, the fixed constants give **strict** bounds `1/125 < V_k(u)/V_k,ref <729/125` on the whole interval including its endpoints. These are deliberately broad shape/domain bounds, **not** 80% breathing or 5% leakage guarantees.

## 4. Continuation, failure preservation, and interpretation

Use a bootstrap up to the first putative strut/member singularity. On that interval the derived positive length margins, finite-energy bounds on all generalized velocities, and positive storage bounds on `alpha`, primary strains, mount lags, and device errors control positions on finite times. The right-hand side of the mechanical ODE is smooth while all member and strut lengths stay positive. A first singularity before `T=2/5` contradicts the strict lower bounds. Therefore **every qualified trajectory exists through T and meets the stated safety inequalities**.

The original amplitude `1/10` has a known *energy-sublevel* counterexample to all-time safety by energy alone: moving a low-beta housing to an endpoint can cost `1/(40R²)<1/36<13/200`. That configuration is not a demonstrated reachable trajectory. No full-pulse result at `u=100` follows; the forced-Green/alignment work remains in a different held task (Draft PR #44). Hardware fabrication, physical calibration, native UD constitutive selection, and mainline physical promotion remain OPEN/UNSCORED.

## Reproduction and evidence

Execute `python3 shorttube.py --out result.json` for exact Fraction checks and `python3 independent_check.py` for a separate same-runtime SymPy integration of the Duhamel kernel and a Gram check. The SHA-256 manifest contains byte-copied scripts and results. This is an **exact conditional mathematical calculation with constructor checks**, not an independent scientific replication. The horizon `2/5` is target-informed from the successful sufficient polynomial and must not be read as an empirically observed threshold.
