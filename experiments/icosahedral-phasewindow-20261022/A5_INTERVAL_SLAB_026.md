# A5 sector-4 spline time-slab certificate — Discovery checkpoint 026

**RESULT — EXACT / CONDITIONAL for the frozen binary64 spline surrogate; NUMERICAL / OPEN for the original continuous-time 3D system.**

Session `phasewindow-20261022-gpt6-7c41`, held claim `claims/icosahedral-phasewindow-20261022`. Baseline source at read-only main `447ee4df3b9bc3e71bdfee3e29f7ee9379410df7` has unchanged icosahedral mechanical source blobs. Separate held PR44 owns forced-Green recovery; no overlapping edits or mainline export.

## Question and typed model

Check the original uniform symmetric moving-pulse model with `alpha0=1/10, beta=.005, nu=.05, cf=0`, 560 original phase variables, and one A5 *representation-theoretic* sector `4` (18 multiplicity coordinates, 36 first-order coordinates). The sector number is not physical spatial dimension; physical reference geometry stays Euclidean R3. Model time `u` has no SI calibration.

The previous checkpoint025 used numerical cubic interpolants for reduced moving-pulse generator matrices. Checkpoint026 preserves a **21 MB frozen binary64 npz** of all 4,001 nodes and the sector-4 4x4000x18x18 cubic stiffness/damping matrices. The SHA-256 of the full local ZIP is `fb0476f40c90eaf8cc210db7b7955b9b253b409de43bdd19c9c247d15c5cf449` (ZIP is a **local artifact** not a committed GitHub run; the binary input exceeds repository's per-file artifact guidance). Every binary64 value is treated as an exact real dyadic for the surrogate mathematical proposition.

Let `x=(16q,v)` for the 18-dimensional multiplicity coordinate `q` and its velocity `v`. On each normalized slab `z in [0,1]`, `x_z=B_j(z)x` where `B_j(z)=sum_{k=0}^3 B_{j,k}z^k` is exactly cubic, and `B_j(z)=h_j[[0,16I],[-K_j(z)/16,-C_j(z)]]`.

## All 4000 slabs: uniform analytic Taylor remainder (EXACT under dyadic spline premise)

The archived `uniform_cubic_slab.py` encloses nonnegative sums and products using IEEE754 binary64 plus upward `nextafter`, and then uses exact `fractions.Fraction` for consequential comparisons. For every one of the 4,000 slabs,

```
sum_k ||B_{j,k}||_infty <= M* = 0.4000200891691032... < 401/1000.
Q_j = sum_k m_{j,k} * 8^(k+1)/(k+1)
Qmax = 3.2007154928021437... < 321/100,
```

where `m_{j,k}` are outward upper bounds on matrix infinity norms, and both maxima occur at slab index 50. Cauchy estimates for the entire matrix-valued solution at complex radius 8 show `||[z^n]Phi_j||_infty <= exp(Q_j)/8^n`. Since `exp(Q) <= (1-Q/64)^(-64)` for `0<=Q<64`,

```
||Phi_j(1) - Taylor_degree20_j(1)||_infty
 <= (1-Qmax/64)^(-64) / (8^20*7)
 = 3.3045975200932015e-18...  (decimal display)
 < 4e-18  [uniformly over all 4000 frozen spline slabs].
```

The simple rational `Qmax<321/100` itself yields the conservative independently reproducible `<4e-18` theorem without depending on decimal precision.

## Three computed local transfer matrices: rational fixed-point residual (EXACT surrogate)

`time_slab_fixedpoint.py` rounds dyadic spline coefficients onto grid `1/10^24` and computes a degree-20 transfer Taylor polynomial, with all recurrence and residual norm checks in exact integers/Fractions. For exact polynomial residual `R=P'-B_fixed P`, coefficient norm upper `r`, rounded generator norm upper `M`, and original-coefficient rounding upper `eps`,

```
||Phi_spline(1)-P(1)||_infty <= r/(1-M) + eps/(1-M-eps),  M+eps<1.
```

FROZEN source coefficient npz replay (exact decimal displays of rational strict bounds):
* initial slab u=0 to .025: 2.2849092681846946e-21;
* near gain peak u=4.65 to 4.675: 2.203184367848278e-21;
* terminal slab u=99.975 to 100: 2.162400918796548e-21.

Independent exact Fraction spot checks at slab indices 0,50,186,2000,3999 pass, and a separate DOP853 polynomial solve differs from the fixed-point transfer on peak slab by 2.43e-15 (NUMERICAL only). The full 4000-term uniform Taylor bound concerns exact Taylor truncation, **not** 4000 independently computed and certified finite-precision matrices.

## Missing original-source and global-composition certification

A 23-time numerical comparison of the original source reduced K/C and the cubic surrogate on the peak slab has sampled infinity-norm differences 9.5052e-9 and 3.2813e-9. Samples do not bound the between-sample defect, and the numerical symmetric baseline itself is not interval-enclosed.

Let `eta=sup_z ||B_true(z)-B_spline(z)||_infty`, where `B_true` uses an *interval-verified original source baseline and Jacobian*. The independently checked rational perturbation inequality yields:

```
eta <= 1e-8  =>  ||Phi_true - P20||_infty < 1.667e-8 < 1/50000000.
```

**CONDITIONAL only:** `eta<=1e-8` has NOT been proved. The stored binary64 cubic is a fitted/development surrogate. Neither global QR/interval composition of 4000 transfers nor checkpoint025's true-ODE nodal/jerk hypotheses is certified. Full nonlinear u100 initial housing-phase ball, all struts, breathing and ringdown, physical constitutive scales and native UD mapping remain OPEN.

## Reproduction and next discriminant

Local package: `UD_3D_A5_Sector4_Slab_Certificate_026_20261025.zip`, SHA-256 above. Includes 28 explicit source inputs (including the frozen coefficient array), 12 outputs, byte-hash manifest, proofs and scripts. Six exact replay outputs matched bit-for-bit after fresh extraction, with 40 input/output digests checked. Repository retains this documentation, not the 21 MB binary or a claimed complete schema2 artifact.

**NEXT (99/100):** Interval-enclose the actual six-state symmetric baseline and projected original-source stiffness/damping on peak slab `[4.65,4.675]`; prove or refute `eta<=1e-8` with directed rounding. Then stabilize QR/interval composition of the true-source four-sector transfers across `[0,100]`. Preserve PR44 ownership.
