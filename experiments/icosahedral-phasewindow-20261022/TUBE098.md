# Original-amplitude 3D pulse — exact relative short tube to u=49/50

**EXACT / CONDITIONAL / FIT (horizon selection).** The original passive MountLoss model is unchanged. This analysis refines only estimates from the previous `relative-tube-005`, which certified u=9/10. It does **not** establish full u=100 coherence, a nonlinear housing-energy half-life, or physical identification.

## Question, source revision and model

For the original dimensionless pulse α(0)=1/10, all initial primary/device positions at reference, all primary/device velocities zero, and **every** initial 180-component housing phase with additional energy ≤ 51/20,000,000, can all 120 moving housing-to-anchor struts and all 20 oriented cells be guaranteed positive for longer than u=9/10?

Integrated reference revision: `127c5fb995cdd218fecc479bccec8ed7a2c2bad0` (Oct 22, 2026), with `mountloss.py`, `hardware.py`, `free3d/model.py`, and `multiport/network.py` verified blob-identical to previously verified `2b133c7889cde7aae9127d0c0fa2036c278884a9`. Prior branch revision: `782cd7fb93e0001bd6bb159857d85e09f1fc4100`. Retain the original orientation convention for the 20 centre-to-face tetrahedra.

Full mechanical state: 280 generalized coordinates (α, 13 primary 3D points, 150 auxiliary coordinates, 30 housing 3D points), their 280 conjugate velocities, plus one heat bookkeeping scalar. Three-dimensional Euclidean spatial lengths are normalized to shell-edge reference length ℓ0=1; continuous u=t/t0 is uncalibrated. All original positive springs, masses, reciprocal forces, central moving-axis dashpots and the positive strut-length ODE domain are assumed. Qualified coefficients include m,g in [19/20,21/20], edge k in [19/50,21/50], β in [1/200,1/20], housing mass weights in [9/10,11/10] (mean 1), Ω=10, ν∈[0,1/20], c_f≥0 and positive remaining device constants. All 180 housing phases, including nonzero initial rigid momentum, are covered.

## 1. Uniform energy and kinetic bounds

Mechanical passivity implies E'=-P_loss≤0 before any possible member/strut singularity. With original pulse α0=1/10 and enlarged housing initial energy:

```
E(u)≤E*= (34/5)(1/10)² + 51/20,000,000
     = 1,360,051/20,000,000.
```

Reference R²=(5+√5)/8 <181/200, since √5<56/25 (square both positive sides). Each primary point has mass coefficient m_i/R² with m_i≥19/20. Therefore all 13 primary velocities have a **shared** Euclidean bound:

```
Σ_i |X_i'(u)|² ≤ (2 E* R²)/(19/20)
                   < (2 E* (181/200))/(19/20)
                   < (9/25)².
```

The last comparison is an exact fraction check. For a housing of mass m_h=(2/5)β w/R² >9/5000, its speed is <35/4, also from E*. Its mount spring stiffness k_h=m_h Ω²>9/50. Importantly, the initial housing *position and velocity share one energy budget*, so for each housing,

```
|D_e(0)|² + |H'_e(0)/Ω|² ≤2 E_h/k_h <(1/180)²,
D_e(0)=H_e(0)-A_e(0), A_e=(X_i+X_j)/2.
```

Thus the complete homogeneous housing-oscillator term has norm <1/180 at every u by Cauchy–Schwarz for its cosine/sine coefficients. This is sharper than independently adding separate amplitude bounds.

The positive spoke/edge energy terms further ensure |radial strain|<2/5 and |edge strain|<3/5 for all u on the solution. Consequently primary spokes and all boundary edges remain nonzero.

## 2. Current-axis forces and exact relative oscillator identity

Each housing's original equation is H''+100H=100A-F, where

```
F_e=(ν/w_e) Σ_{a∈{i,j,k,l}} n_ea [n_ea·(H'_e-X'_a)]
```

for instantaneous unit directions n_ea along housing-anchor separation. Thus, using ν/w≤1/18, all four anchors, housing speed <35/4 and individual primary speed <9/25,

```
|F_e(u)|<(1/18)⋅4⋅(35/4+9/25)=911/450.
```

Direct integration by parts in the harmonic Green representation, valid for the *actual moving midpoint*, gives for any anchor a:

```
H_e(u)-X_a(u) = A_e(0)-X_a(0)
 + D_e(0) cos(10u) + (H'_e(0)/10) sin(10u)
 + ∫_0^u [(1-cos(10(u-s))) A'_e(s)-X'_a(s)] ds
 - (1/10)∫_0^u sin(10(u-s)) F_e(s) ds.
```

For endpoint a=i, the velocity-integrand coefficients on X'_i, X'_j have squared norm `(1+cos²θ)/2≤1`; shared primary kinetic energy gives integrand norm <9/25. For opposite-face anchor a=k, the coefficient norm is at most √3 and its reference midpoint distance is √3/2 instead of 1/2. The same homogeneous/viscous error applies. Whenever the endpoint bound is positive, the opposite-anchor bound is strictly larger. No primary rigid-motion quotient is imposed.

## 3. Finite sine-kernel bound (exact trigonometric step)

Set T=49/50; 10T=49/5. The standard rational bounds `3<π<22/7` imply `3π<49/5<4π`. Write r=49/5−3π. Because π>3, `0<r<4/5`. On [0,T] the absolute-sine integral is monotonically increasing and

```
∫_0^T |sin(10v)| dv = [6+(1-cos r)]/10
                           ≤ [6+r²/2]/10
                           < [6+(4/5)²/2]/10
                           =79/125.
```

The inequality `1−cos r≤r²/2` holds for all real r. This finite-T result replaces the earlier global average `∫_0^t|sin(10v)|dv≤3t/4`, which was substantially looser for this interval.

The complete viscous convolution error is therefore <(911/450)/10×(79/125), uniformly on [0,T]. The endpoint strut satisfies

```
|H_e(u)-X_i(u)| > 1/2−1/180−(9/25)(49/50)
                     − (911/4500)(79/125)
                    = 3853/281250 > 1/100 >0.
```

The opposite-face anchor estimate is greater whenever the endpoint bound is positive. Hence **all 120 struts remain strictly longer than 3853/281250 ℓ0** on [0,T].

## 4. All 20 cell orientations

Let A_k(u)=[X_a−C,X_b−C,X_c−C] for one positively oriented centre-cone cell. The star-incidence matrix for its three relative 3D columns has singular values 2,1,1. From the shared velocity bound,

```
||A_k(u)-A_k(0)||_2 ≤||ΔA_k||_F < 2 (9/25)u.
```

For the exact reference icosahedron, the Gram `G_ref=A_ref^T A_ref` has eigenvalues `1/2,1/2,(7+3√5)/8`, so σ_min(A_ref)=1/√2. Thus

```
||A_ref^{-1}(A_k(u)-A_ref)||_2 <2√2 (9/25)u.
```

At T=49/50, the square of this upper bound is `388962/390625 <(499/500)²<1`, checked with exact integers. Every cell stays nondegenerate and preserves initial positive orientation. The singular-value bounds give

```
(1/500)³ < V_k(u)/V_k,ref < (999/500)³,
```

i.e. `(1/125000000, 997002999/125000000)` for all twenty oriented cells. These deliberately broad bounds are **not** an RMS breathing or mismatch certificate, and orientation alone is not convexity.

## 5. Continuation, failed extension and exposure

Before a putative first singularity, positive energy bounds velocities on finite times; primary locations stay bounded by kinetic integration, the auxiliary device displacement is bounded by its positive elastic energy and input strains, and housing points are bounded by their mount energy and moving midpoints. The positive primary-member and housing-strut margins eliminate the ODE's non-smooth denominators through T. Standard ODE continuation therefore gives existence through u=49/50 for **every** permitted initial housing phase and all qualified property settings.

The same kinetic star-incidence sufficient bound fails at u=1, because `8(9/25)²=648/625>1`. This is a **failed proof extension**, not evidence of a physical singularity or an actual counterexample. A further substantial extension will require a dynamical invariant, correlation/response tube or stronger displacement control; simply refining rational roundings is nearly exhausted for this method.

Source exposure: the original α=0.1, 80% breathing, 50% energy and u=100 targets were already inspected. T=49/50 was selected after seeing the u=9/10 result and testing nearby inequalities (development/FIT). Exact arithmetic does not remove that target selection. The original 560-state nonlinear full-pulse u=100 all-phase outcome remains OPEN, as do native UD constitutive selection, any physical clock/energy map, real housing hardware and independent experimental evidence.

## Reproduction

```
python3 experiments/icosahedral-phasewindow-20261022/tube098.py --out /tmp/tube098.json
python3 experiments/icosahedral-phasewindow-20261022/tube098_check.py
```

`Fraction` assertions verify all decisive inequalities; `SymPy` recomputes the cell Gram spectrum and star-incidence spectrum; a numerical quadrature of the sine kernel is an **independent diagnostic**, not the basis of the exact inequality. These checks are constructor/same-runtime checks, not independent peer review or experimental replication.
