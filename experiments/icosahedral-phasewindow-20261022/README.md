# Expanded housing-phase budget: joint 3D damping window

**RESULT — EXACT / CONDITIONAL (housing-only geometry); NUMERICAL / DEVELOPMENT (full linear all-phase window).**

Task `icosahedral-phasewindow-20261022`, session `phasewindow-20261022-gpt6-7c41`, verified integrated source `ce89a9cd15439463d9a64d983d91c22ea4368726`; active task claim `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`.

## Question and scope

Can the published passive icosahedral housing-loss window `nu in [1/25,1/20]` preserve its joint **linear** ringdown and breathing screens at a larger initial housing-phase energy budget, including nonzero housing positions and velocities, low positive beta, and c_f=0? Does exact passivity separately protect the nonlinear *housing-only* positive-length domain at that larger budget?

The unchanged 280-configuration/560-mechanical-phase MountLoss surrogate has 13 primary vertices, 150 device coordinates, 30 housing positions, and 120 central viscous paths. The original linearized energy metric retains rigid kinetic energy; initial housing perturbation dimension is 180. The distinct nonlinear full-pulse, housing-only, and linearized questions are never identified with one another. Reference geometry is over Q(sqrt(5)); physical time/length/energy are uncalibrated.

## Source and target exposure

All 50 distinct coefficient sets, the nine adaptive strength nodes, the passive law, and the original 80%-breathing/50%-ringdown targets were **already exposed**. This post-selection development calculation evaluates `E_h <= (3/2) E_p/40000 = 3 E_p/80000`; factor 3/2 is a new chosen test budget, not experimentally fitted or independently predicted. Its source is the immutable original integrated `artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/linear.csv` (450 source rows, SHA-256 `971a8dc46bc42fc9b246ef7c20b13b9f3651d29d4704e111fa402f9e2edaf3e5`) and `full_housing_refined.json` (SHA-256 `d3fc9c63f21811b65e3d0bed04063d8f4725eaab01970602e560876ccc569427`).

## Exact conditional readout and ringdown inequalities; numerical new evaluation

For each of the 50 property sets at each saved node nu_j, denote the stored linear zero-housing pulse RMS by R_p, matching undamped linear baseline by R_0, prior all-phase housing readout bound by delta = sqrt(2 E_h_old S_*), and proven (conditional on model) damping-strength Lipschitz constant by L_R. Since the linearized perturbation is homogeneous in initial phase,
```
R_total(nu, E_h_new) >= R_p(nu_j) - L_R |nu-nu_j| - sqrt(3/2)*delta.
```
A sufficient breathing neighborhood at node j for each property case is therefore
```
r_j,case = (R_p - sqrt(3/2)*delta - (4/5)*R_0)/L_R.
```
Taking the smallest radius across all 50 cases at each of nine saved nodes, the overlapping closed neighborhoods cover **all nu in [.04,.05]**. The smallest overlap between adjacent nodes is **0.00031000469824** (computed in float64 from the frozen source records). All limiting breathing cases are `seed10422-0-boundary2`.

Separately, the existing `full_housing_refined.json` numerical continuous-strength envelope is **0.4566660701874066 < 1/2** over all 180 housing initial-phase directions and the same 50 coefficient sets. Because this is a *linear energy fraction*, changing the amplitude of the initial energy ball leaves the fraction unchanged. Combining these two **separate** source-certified inequalities supports the expanded **linear** joint window, conditional on the original numerical source enclosures. No new full560 matrix exponential or floating interval certification was performed.

## New exact housing-only all-time length/domain bound

Housing-only means alpha=0 and primary/device reference initial values, plus **arbitrary** housing position/velocity phase with `E_h <= 3 E_p/80000`. In the qualified continuous property box, E_p<=(1+12(21/20))/200=17/250, giving
```
E_h <= 51/20000000.
```
Passivity E(u)<=E_h and positive spoke/edge/mount potential terms, k_e>=19/50 and mount k_h>9/50 yield for all future u:
```
|s_i|<1/400, |e_ij|<1/250, |H_e-A_e|<1/180.
```
For endpoint anchors, strut length exceeds `(1-1/250)/2-1/180=554/1125`. For either opposite face anchor, the median identity gives squared center-to-anchor distance exceeding `(249/250)^2-(251/250)^2/4=185003/250000>1/4`; subtracting 1/180 still leaves a larger margin. Thus **every one of the 120 current-axis struts stays longer than 554/1125**. All primary members remain noncollapsed.

For each oriented cell, its reference Gram has minimum eigenvalue 1/2. Set sigma=1/400, epsilon=1/250. The derived Gram perturbation obeys
```
||Delta G||_F <= 3(2 sigma+sigma^2)+sqrt(3/2)(2 epsilon+epsilon^2)
 < 496767/20000000 < 1/40.
```
The inequality uses sqrt(3/2)<49/40. Therefore the relative Gram perturbation has operator norm <1/20. Continuous orientation and the determinant identity give for every cell and every u>=0:
```
(19/20)^(3/2) < V_k(u)/V_k(0) < (21/20)^(3/2).
```
Positive energy bounds velocities on finite intervals and the length bounds exclude all ODE strut/member singularities; standard continuation gives global existence in the housing-only preparation. This is an **EXACT/CONDITIONAL** all-phase, all-time domain/orientation guarantee for a larger initial budget. It is *not* a nonlinear half-energy-by-u100, full-pulse coherence or manufacturing guarantee.

## Independent fixed-primary benchmark

A separate locally executed symbolic/ODE check treats the primary points as fixed. For a mass-normalized housing direction with local Gram eigenvalue lambda in `{2,(3-sqrt5)/3,(3+sqrt5)/3}`, damping d=nu*lambda/w, mount frequency Omega=10 and horizon T=100, its sharp all-phase energy fraction is
```
exp(-d*T) (sqrt(1+q^2)+q)^2, q=abs(d*sin(sqrt(Omega^2-d^2/4)*T)/(2*sqrt(Omega^2-d^2/4))).
```
At nu .02/.04/.05 its numerical worst fixed-primary fractions are .629640489/.396447128/.314580341 over w in [.9,1.1]. A safe common envelope is `exp(-T*d_min)*(2Omega+d_max)/(2Omega-d_max)`; this reaches 1/2 at approximately nu=.0302324840. This **fixed-primary** result neither changes nor certifies the coupled full assembly; beta cancels only in this reduced direction.

## Validation status and limits

- EXECUTED: local exact Python Fraction checks, SymPy scalar eigenvalue checks, DOP853 scalar oscillator check (energy-formula discrepancy 3.6e-12).
- EXECUTED: connector-side deterministic scan of 450 immutable source rows across nine nodes, 50 cases; verified published SHA-256 source bytes.
- CAPTURED: immutable run `artifacts/phasewindow-20261022-gpt6-7c41/phasewindow-001/manifest.json`, input bytes, replay script and `result.json`.
- NOT_RUN: Python `replay.py` from a complete local repository checkout; network prevented Git clone. Do not claim it passed until CI/checkout runs it.
- NOT_RUN in this runtime: `python3 scripts/validate.py`, `python3 -m unittest discover -s tests -v`. Repository checks and reviewer assessment remain required.
- No sampled nonlinear extension, no high-dimensional continuous property-box guarantee, no verified interval arithmetic, and no independent physical experiment. The original beta=.005/nu=.02/c_f=0 failure and out-of-budget mass/friction failures remain preserved.
- Full nonlinear alpha=.1 pulse with all 180 initial housing phases through u=100 remains OPEN, as does a validated forced Green/remainder tube.

**Next discriminant:** obtain a positive full-state/block-norm forced Green bound and a nonlinear alignment/flow remainder under the original and enlarged energy budgets at beta=.005,c_f=0; do not reinterpret the exact housing-only safety certificate as pulse coherence.

## Original-amplitude finite-time nonlinear safety addendum — shorttube-003

[Full proof and exact calculator](SHORTTUBE.md) and [immutable record](../../artifacts/phasewindow-20261022-gpt6-7c41/shorttube-003/manifest.json) provide a distinct EXACT/CONDITIONAL result for the **original** `alpha0=1/10` heart pulse, enlarged housing energy `E_h<=51/20000000`, all initial 180 housing phases, and the unchanged full 560-phase ODE.

For every qualified property realization and every `u in[0,2/5]`, all 120 housing struts are strictly longer than `13/1500 ell0`, all primary members remain noncollapsed, and all oriented cell ratios lie between `1/125` and `729/125`. This follows from a moving-midpoint Duhamel bound (not equilibrium linearization) plus an exact 3D Gram/singular-value orientation estimate. The previous full-pulse exact bound reached only `u=1/20`, under a smaller housing budget. At `u=39/100`, all struts exceed `257/9000>1/40`.

The rational horizon `2/5` was selected after inspecting the sufficient proof polynomial (development/FIT). This **does not certify any u100 nonlinear ringdown/coherence or all-time alpha=.1 safety**. The original energy-only singular-configuration witness and separately held forced-Green recovery task PR44 retain their scopes; no files of that task were changed. For reproducibility, run `python3 shorttube.py --out /tmp/shorttube-result.json` and `python3 shorttube_check.py`.

## Versioned correction (shorttube-004)

The historical immutable `shorttube-003` proof used strict time-dependent volume/point-displacement signs at `u=0`, when those quantities equal their reference values. This was a notation error, not a changed model or conclusion. [SHORTTUBE_ERRATUM.md](SHORTTUBE_ERRATUM.md) gives the correction: use non-strict time-dependent inequalities on `0<=u<=2/5`, with equality at `u=0`; strict **fixed** bounds `1/125<V_k/V_k,ref<729/125` and `ell>13/1500` remain valid on the closed interval. Updated [SHORTTUBE.md](SHORTTUBE.md) is captured byte-for-byte as immutable [shorttube-004](../../artifacts/phasewindow-20261022-gpt6-7c41/shorttube-004/manifest.json); prior 003 remains preserved. Original alpha=.1 u100 remains OPEN.
