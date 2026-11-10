# UD Discovery — nonlinear curvature hidden in the projected adjoint kernel

**RESULT: EXACT / CONDITIONAL local force derivative; NUMERICAL / DEVELOPMENT full-model phase tests. Universal nonlinear phase-ball bound OPEN.**

Task `icosahedral-phasewindow-20261022`, session `phasewindow-20261022-gpt6-7c41`, held claim, isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Imported integrated source main `0abea764505989dde38fe0906d0d32c53d76b93c` (mechanical source blobs verified unchanged). This report does not alter mainline, existing 015 observations, or independent greenbounds task/PR #44.

## Question and typed dynamics

Does the computed 156-dimensional nullspace of the 24×180 initial-housing-phase-to-non-affine-shell first derivative remain invisible under the **full nonlinear** mechanical evolution? If not, which housing displacement/velocity mechanisms excite the nonlinear response?

Full mechanical state `y=(q,v)∈R^560`, one separate heat accumulator, Euclidean 3D primary positions, 30 moving housings, 150 relative device coordinates, and 120 moving-axis central viscous paths. The time `u=t/t0`, length `ell0=1`, and energy `E_*` remain uncalibrated. The source-frozen case is `edge-p1-b0.005-cf0.0`, coefficient SHA-256 `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`, `nu=.05`, initial `alpha0=.1`. Additional housing initial phase energy `Eh=2.430311755526067e-6`, `epsilon=sqrt(2 Eh)=.002204682179147855`. Initial phase `a∈R^180`, `||a||2<=1`, injects as `y(0,a)=y0+epsilon B a`, including housing position and velocity and conserved rigid kinetic energy. The projected output is `z(u,a)=C y(u,a)∈R^24`; `C` has orthonormal rows, and its norm equals the shell non-affine Frobenius norm. No empirical observations are fitted.

## Exact second-variation identity (under smooth positive-length dynamics)

Set `J(u)=DF(ybar(u))` for the baseline `ybar(u)=flow_u(y0)`, and let `Phi(u,s)` solve `d/du Phi=J(u)Phi`, `Phi(s,s)=I`. With `w_a(s)=Phi(s,0)B a`,

```
G_u = C Phi(u,0) B                                      (24×180)
D_a z(u,0)[a] = epsilon G_u a
D_a² z(u,0)[a,a] = epsilon² * C integral_0^u Phi(u,s)
                              D²F(ybar(s))[w_a(s),w_a(s)] ds.
```

Thus `a∈ker G_u` cancels the first derivative at that observation time; no identity forces the second derivative to vanish. The finite symmetric even part `(z(+a)+z(-a))/2-z(0)` estimates one-half of the second variation, with higher even orders. The central odd part estimates `epsilon G_u a`, with higher odd orders. These identities are conditional mathematical properties of the smooth ODE, not a validated bound on its solutions.

## Numerical source-matched structure at u=4

Read unchanged 015 snapshot `gain_t4p0.npz` (24×180 first-derivative matrix, 24D reference output). Numerical rank `rank(G_4)=24`; its nullspace has dimension156. Both position-only block `G_q` (24×90) and velocity-only block `G_v` (24×90) have numerical rank24. Their kernels each have dimension66, and a complementary 24D mixed cancellation sector is given by the orthonormalization of `[G_q^+;-G_v^+]`. All nullspaces here are **numerically constructed**, not exact algebraic certificates for the full nonlinear flow.

The 48 direction screen uses 24 row singular vectors, 12 SVD-null vectors, and 12 seeded random null vectors. All phases are energy normalized. Max observed symmetric even projected outputs at u=4:

| sampled class | directions | largest even response |
|---|---:|---:|
| first-order active row space |24| 1.050887e-8 |
| SVD null basis |12| 9.997754e-10 |
| random computed null directions |12| 1.558874e-9 |

Numerical null first-order leakage <3.6e-20 in displacement output; finite central odd components can be O(1e-11), consistent with higher odd orders and integration error. Separately 12 position-only and 12 velocity-only null phase checks have maximum even responses 1.098135e-10 and 3.868932e-10. A further 24 mixed cancellation basis phases plus12 random mixed phases reach a larger even response **5.714001e-9** at u=4, with `||G Qmixed||F < 5.9e-16` for the unscaled first derivative.

## Approximate 10D curvature slice and refinement

A frozen seed generates 10 orthonormal directions in the 156D numerical nullspace. Polarization of symmetric nonlinear finite differences constructs a **numerical** 10×10 scalar quadratic form aligned with the reference `zbar(4)`. Its extreme eigenvalues are approximately `-1.316414e-9` and `+1.286237e-9` at full allowed phase amplitude. The selected positive eigenvector produces a vector even response `1.812931e-9`, with residual first derivative ≈1.7e-20. Half/full and quarter/full even-response ratios are `0.250000205` and `0.062500424`. DOP853 tolerance refinement across `rtol=2e-9…5e-13` changes the full even norm by at most `2.03e-13`; tolerance agreement is **not a validated integration error bound**.

A source-frozen full156D *matrix-free scalar adjoint Hessian* probe returns a gradient-to-frozen-G difference `6.42e-13`, directional Hessian-action norms `3.90e-9`/`4.94e-9`, and bilinear symmetry discrepancy `5.08e-17`. The attempt to compute its full extremal eigenspectrum **TIMED_OUT**, so there is no full156D Hessian norm or spectral bound. These numbers are only sample diagnostics.

## Exact local moving-axis bilinear forcing mechanism

For one current-axis housing-to-anchor loss `F_anchor=eta n(d)[n(d)·(v_H-v_a)]` with `d=H-X_a`, `n=d/|d|` and `Pperp=I-nn^T`, the cross term when housing displacement and relative velocity both vary about the zero-relative-velocity reference is

```
Fcross = (eta/|d|) [ (Pperp δd)(n·δv) + n(Pperp δd·δv) ].
```

This is an **EXACT local differential identity** on positive strut lengths. Its numerical check in the source-frozen 560-state assembly for the most curved mixed basis direction gives predicted projected shell *initial acceleration* `2.792356e-9` and direct finite cross difference `2.790464e-9`; the 0.1508% relative error halves as phase scale halves, consistent with neglected cubic terms. This identifies a possible physical term coupling displacement and velocity; it does **not** prove that it is solely responsible for the later t=4 second-order projected output.

## Conditional sufficient remainder budget, not achieved

Let `M2(u)` bound the **entire phase ball**, including all directions, by

```
M2(u) >= sup_{||b||<=1, ||a||=1} ||C D² flow_u(y0+epsilon B b)[B a,B a]||2.
```

Taylor's theorem then gives `||R(u,a)|| <= Eh M2(u)` for any `||a||<=1`, provided the whole initial ball of trajectories exists smoothly through `u`. At the **sampled** u=4 source-frozen first-order triangle value `0.0004356646893`, an illustrative sufficient condition would be `M2(4) < 10107.48323`, using the earlier `1/40` threshold and taking the sampled first-order numerical value as if verified. The requirement itself is a correct **conditional formula**; the source numerical value, full-ball `M2`, continuous-time extrema, and reference/solver error are **not certified**. In particular the sampled 10D scalar Hessian is not a substitute for M2.

## What failed, and next discriminant

- **FAILED as universal inference:** an all-phase first-order bound does not alone bound nonlinear effects; 156 first-order-null directions exist numerically and some generate nonzero even response.
- **NOT COMPLETED:** full156D Hessian eigenspectrum; matrix-free probe passed but the eigenanalysis exceeded the compute budget.
- **OPEN:** validated full180-phase nonlinear remainder, continuous `0<=u<=100` output bound, multidimensional tolerance-box coverage, all-time strut/volume coherence, and physical calibration.
- **Next priority 98/100:** exploit the exact local bilinear derivative and block sparsity to bound full nullspace curvature in a compatible positive mechanical norm, with interval/reference/Green remainder control; independently recover PR44 source for its own task rather than overwriting it. Consider mixed cancellation directions mandatory adversarial tests.

Targets, case selection and prior 015 peak were exposed before choosing the 10D nullspace slice and phase sets. Seeded basis, sample counts, timeout, source hash, tolerance ranges and no retuning are recorded in the runnable scripts and JSON. This is same-runtime constructor verification, not independent mathematical/empirical replication.
