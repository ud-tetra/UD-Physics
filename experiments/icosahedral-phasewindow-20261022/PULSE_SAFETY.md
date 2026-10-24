# Reduced-amplitude full-pulse nonlinear safety (v1.0)

**RESULT — EXACT / CONDITIONAL.** This is a separate follow-up to the enlarged linear phase-window calculation; it neither revises that result nor closes the original amplitude-0.1 full-pulse theorem.

## Scope and typed objects

Source integrated revision: `ce89a9cd15439463d9a64d983d91c22ea4368726`; exact passive MountLoss model as in `experiments/icosahedral-mountloss/README.md`, `experiments/icosahedral-nonlineartube/README.md` and `experiments/icosahedral-jointwindow/BUDGET.md`. The model has 280 configuration coordinates, 560 mechanical phase coordinates, a separate heat accumulator, 13 primary 3D vertices, 30 moving housing points, 150 device coordinates and 120 current-axis housing-anchor viscous paths. The fourth-dimensional proposal is parked and **not** imported.

Physical geometry uses positive Euclidean 3D length metric; reference squared circumradius `R^2=(5+sqrt(5))/8<1`. The continuous clock is dimensionless `u=t/t0`, with length `ell0` and energy `E_*` uncalibrated. Initial conditions have heart scalar `alpha(0)=a`, all primary positions at reference and initially at rest, device coordinates and velocities zero, and **arbitrary initial housing position and velocity directions** of total energy `Eh<=3 E_p,ref/80000`. The reference pulse energy `E_p,ref` here means the *original* amplitude-0.1 `(1+sum g_i)/200`, not the energy of the reduced pulse.

Qualified box: `g_i,m_i in[19/20,21/20]`, `k_ij in[19/50,21/50]`, `beta in[1/200,1/20]`, housing weights `w_e in[9/10,11/10]` with average one, reciprocal gains `[.99,1.01]`, `Omega=10`, `cf in[0,1/1000]`, `nu>=0`. The original passive constitutive law, constraints and reactions are unchanged.

## Exact global energy majorant

The unchanged model has nonnegative stored energy and `E'=-P_loss<=0`. The scalar pulse contribution at reference satisfies `E_p(a)=(1+sum g_i)a^2/2 <= (34/5)a^2`. Also `E_p,ref<=17/250` and thus `Eh<=51/20000000`. Hence throughout any existing trajectory,

```
E(u) <= Emax(a) := (34/5) a^2 + 51/20000000.
```

For radial strains `s_i=|X_i-C|/R-1`, shell-edge strains `e_ij=|X_i-X_j|-1` and mounts `d_e=H_e-(X_i+X_j)/2`, positive energy terms give

```
|s_i| <= sqrt(2 Emax),
|e_ij| <= sqrt(2 Emax / k_min),   k_min=19/50,
|d_e| <= sqrt(2 Emax / k_h,min), k_h,min=9/50 (strict).
```

The mount stiffness bound follows from `k_h,e=(2 beta/5) w_e Omega²/R²`, `beta>=1/200`, `w_e>=9/10`, `Omega=10` and `R²<1`.

For any house on edge `(i,j)`, endpoint strut lengths exceed `(1-epsilon)/2-delta`. For either opposite vertex `k` on an adjacent icosahedral face, the exact median identity gives

```
|X_k-(X_i+X_j)/2|²
 = (|X_k-X_i|²+|X_k-X_j|²)/2 - |X_i-X_j|²/4
 > (1-epsilon)² - (1+epsilon)²/4.
```

Subtracting mount lag `delta` bounds the opposite struts. The face condition uses the original icosahedral incidence, not an assumed spatial rigidity in the perturbed shape.

### Regime A: |alpha(0)|<=1/25 = 0.04

At `a=1/25`, `Emax=217651/20000000`. Exact fractions satisfy the simultaneous strict bounds

```
|s_i|<3/20,  |e_ij|<1/4,  |d_e|<7/20.
```

Each endpoint strut therefore exceeds `(1-1/4)/2-7/20=1/40`. Opposite-face median squared exceeds `11/64`; since `sqrt(11)>3`, those struts also exceed `1/40`. Thus **all 120 strut lengths are >ell0/40 for every future u**. All radial and shell-edge member lengths remain nonzero. Kinetic energy bounds every velocity on finite time intervals, and the positive-energy springs bound scalar/device variables. Finite-speed continuation plus absence of denominator singularities establishes **global existence** for every housing phase in the budget. A quantitative cell-orientation or coherence bound is not asserted at this amplitude.

### Regime B: |alpha(0)|<=3/100 = 0.03

At `a=3/100`, `Emax=122451/20000000`. Choose `|s_i|<1/9`, `|e_ij|<1/5`, `|d_e|<4/15`. The same strut proof gives all struts `>2/15`, preserving global existence.

For an oriented centre-to-face tetrahedron, let `G=A^T A` be its three-column Gram matrix. Reference Gram `G0=(1/2)I+(R²-1/2)11^T` has eigenvalues `1/2,1/2,(7+3sqrt(5))/8`. Squared spoke/edge changes determine

```
Delta G = (t 1^T + 1 t^T - U)/2,
t_i=R² (2s_i+s_i²), U_ij=2e_ij+e_ij² (i!=j), U_ii=0.
```

The **shared** local energy constraint, rather than assigning an independent full energy budget to both sets of strains, gives

```
||Delta G||_F²
 < 2 Emax [3(2+1/9)² + (2+1/5)²/(2(19/50))]
 = 206656471/855000000
 < (123/250)² < 1/4.
```

Therefore `||G0^(-1/2) DeltaG G0^(-1/2)||_2<123/125<1`. Every tetrahedron remains nonsingular and its initial positive orientation is preserved by continuity. For each of the 20 normalized oriented cell volumes:

```
(2/125)^(3/2) < V_k(u)/V_k,ref < (248/125)^(3/2),  all u>=0.
```

These volume bounds are deliberately conservative and are **not** 80% breathing-retention or 5% nonuniformity bounds.

## Failures, assumptions and selection disclosure

The exact constants `1/25` and `3/100` are exploratory rational *sufficient* thresholds chosen after the original `1/10` energy-sublevel obstruction was known; they are development selections, not unique critical amplitudes or nature-derived constants. The chosen rational majorants fail at `a=41/1000` and `a=31/1000` respectively, which **does not** establish dynamical collapse at those amplitudes.

The parent full-pulse `a=1/10` energy sublevel contains a low-beta housing-at-endpoint witness of cost `1/(40R²)<1/36<13/200` (nominal initial pulse energy), so *total-energy-only* certification cannot solve its positive-length problem. This witness is not a dynamically reached trajectory; the original nonlinear all-phase `u=100` question remains OPEN.

No old fitted `nu` or hardware parameter is retuned. Positivity and passivity hold for `nu>=0`, including `cf=0`; the proof does not establish dissipation by a given deadline, nonlinear mean-volume RMS retention, physical calibration, or a native UD dynamics selection rule. Unlike ongoing [Draft PR #44](https://github.com/ud-tetra/UD-Physics/pull/44), this run does not claim a full forced-Green or alignment bound.

## Reproduce

Run `python3 experiments/icosahedral-phasewindow-20261022/pulse_safety.py --out /tmp/ud-pulse-safety.json` from a checked-out branch. The source uses only Python standard library exact `Fraction` comparisons; an independent SymPy calculation checked the reference Gram eigenvalues. Original inputs and output are captured by the session's distinct immutable pulse-safety run. Same-runtime exact checks are not independent experimental replication.
