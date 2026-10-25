# Rank-three partial-patch no-go and exact icosahedral graph stress

**EXACT / CONDITIONAL / FAILED partial relaxation; full 12-vertex global lower barrier OPEN.**

Repository baseline `bbf7b9ec09a86378f6503c16460771a033e48593` (underlying full 3D model unchanged). Session `phasewindow-20261022-gpt6-7c41`; claimed branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Original full-pulse energy ceiling `1360051/20000000 = 0.06800255`.

## Exactly defined primary energy
Let twelve centre-relative vertices lie in physical Euclidean R3, reference shell edge=1, R²=(5+sqrt5)/8. For spoke strain s_i=|X_i|/R-1, edge strain e_ij=|X_i-X_j|-1 and heart scalar alpha, original positive conservative primary energy is

`U=1/2 [alpha² + Σ_i s_i² + Σ_i g_i(s_i-alpha)² + Σ_(i,j) k_ij e_ij²]`.

The physical source has g_i>=19/20 and k_ij>=19/50, and extra device/housing storage is nonnegative. A certificate that discards some positive terms is a lower bound on full energy.

## EXACT 9-vertex R3 witness to a partial-sum proof
Keep only shell vertex IDs 0..8 (9 radial and 18 induced exterior edge terms), and the same alpha² term. The archived rational coordinates have denominator 10^6, alpha=-4249/10^6, and impose X_2=(780694/10^6)X_0+(780310/10^6)X_1. The selected original face [0,1,2] has rank2 and determinant0 exactly; nine points span rank3, **not** four dimensions. All included edge and radial lengths are nonzero. The exact checker bounds every square root by rational integer-isqrt enclosures and verifies

`U_9 < 1/20 < 1360051/20000000`.

An independent same-runtime high-precision calculation gives U_9≈0.0495778040193576 (display only). Therefore this *specific nine-vertex induced-patch-only lower-bound method* CANNOT establish the required global barrier. The omitted three vertices and twelve other exterior edges have positive energy that may prohibit such a full-shell completion below the budget. **No globally admissible 12-vertex collapsed configuration below the pulse budget was constructed.**

## EXACT graph-spectral identity
Let V be the 12×3 exact regular-icosahedron reference array; A its 12×12 0/1 exterior adjacency, 30 edges, degree5. The exact field Q(sqrt5) calculation yields A V=sqrt5 V, 1^T V=0, V^T V=4R² I and

`charpoly(A)=(lambda-5)(lambda+1)^5(lambda²-5)^3`.

Define `P0=11^T/12`, `PV=V(V^TV)^(-1)V^T`, and

`Omega=sqrt5 I-A+(5-sqrt5)P0`.

Then Omega has zero eigenvalues with multiplicity4, and positive eigenvalues (1+sqrt5) with multiplicity5 and 2sqrt5 with multiplicity3. Thus

`Omega >= (1+sqrt5)(I-P0-PV) >= 0` (PSD Loewner).

For any shell placement Y in R^(12×d), define t=1^T Y/12, B=(V^TV)^(-1)V^T Y and Z=(I-P0-PV)Y. The exact spectral estimate is

`tr(Y^T Omega Y) >= (1+sqrt5)||Z||_F²`.

For physical **d=3**, if one centre-to-face cell is flat, Y_F=V_F B+1_3 t^T+Z_F is a singular 3×3 matrix; consequently

`tr(Y^T Omega Y) >= (1+sqrt5)*sigma_min(V_F B+1_3 t^T)^2`.

This is a globally valid necessary collapse inequality but its connection to the *spring energy* is not yet strong enough to establish the original threshold. The first stress inequality holds in any ambient dimension, so it does not repair the previously demonstrated rank-four Gram relaxation failure.

## Numerical development (not global minimization)
The local patch scan examined all 84 nine-vertex omissions with seven SLSQP starts, 36 ten-vertex omissions with ten starts, and nine eleven-vertex omissions with 60 starts; additional target-selected repeats used 55/80/200 starts. Several nine-vertex numerical local minima initially looked above the energy threshold; further starts exposed lower minima, invalidating the shallow candidate conclusions. The 11-vertex survey's smallest *observed* partial energy was ≈0.07609; this is **not a global infimum certificate**. The full 12-vertex prior numerical candidate ≈0.124426 and its exact collapsed upper witness below1/8 are preserved.

All thresholds, chosen patch, numerical seeds, coordinate denominator and prior failures were exposed/development-selected. The full 12-vertex rank-three global lower bound, u100 full nonlinear response, hardware realization and physical calibration remain OPEN. PR44 retains separate held ownership of forced-Green recovery, unchanged here.

## Reproduction and next discriminant
`python3 experiments/icosahedral-phasewindow-20261022/rank3_patch.py --witness experiments/icosahedral-phasewindow-20261022/rank3_partial_witness.json --out /tmp/rank3-patch.json`.

The full locally executed source, secondary checker, 84/36/9 patch scan, receipts and SHA-256 manifest are also preserved in the conversation ZIP. Reproduce before any integration; repository integrity checks are not independent scientific validation.

**Next (priority 98/100):** combine the exact stress projector with full-shell rank-three compatibility and bounds on affine translation/deformation, or run a validated global interval optimization. A proof must survive both the exact rank-four *relaxed* witness and exact rank-three *partial* witness.
