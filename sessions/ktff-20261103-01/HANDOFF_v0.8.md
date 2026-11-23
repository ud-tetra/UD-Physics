# UD-Physics Klein–K4 scale-aware coarse dynamics handoff v0.8

**Claim:** Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`; live claim ref `refs/heads/claims/klein-tetra-face-flip-20261103` HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated Discovery branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`; PR #301 draft and unmerged. Original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, main reverified at `e400dfb715262a44b3bbb2e929c7b438028af67e`. Do not release claim or update shared CURRENT before integration. Physical promotion 0.

## Source, assumptions and completed work

Original native generator source: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3. Conditional prior mathematics: `INTEGRAL_SUBDIVISION_STRONG_RETRACT_v0.6.md` exact integral P,S,H on the assumed Klein×I 72-tetrahedron orientation-twisted chain (348 real coordinates) and minimal CW (12 coordinates), and `REFINEMENT_LOCALITY_AND_DYNAMICS_v0.7.md` exact failure of two unrelated naive unit-metric skew dynamics. The seam gluing, fine unit matrix metric, formal clock u and CW subdivision are **declared assumptions**. No SI or physically calibrated coframe or mass.

Define coarse induced Gram `G=S^T S` from exact integer S; full local replay determines exact diagonal
```
G=diag(1,1,2,2,2,2,2,8,8,12,12,72).
```
Define unique orthogonal Galerkin left map `L=G^-1 S^T` and candidate coarse `A_G=L A_s S`, where `A_s=D_s-D_s^T` on fine 348D unit metric. Exact boundary intertwining `D_s S=S D_c` yields
```
A_G = D_c - G^-1 D_c^T G,
A_G^T G + G A_G=0.
```
The 12D generator has exactly 11 CW incidence pairs, no nonincidence couplings. Exact signed currents `J_i<-j=2G_ii(A_G)_ij y_i y_j` are antisymmetric and conserve `y^T G y` for formal `y'=A_G y`. G weights are subdivision-amplitude counts, not physical energy/length.

**NO-GO, exact source-type hypothesis:** The fine image of S is not invariant under `A_s`. Residual `R=A_s S-S A_G` orthogonal to image has rank11, Frobenius squared157, and weighted input norm squared242/3. `A_G` differs from naive `A_0=D_c-D_c^T` in rank5 and squared Frobenius151/18. Thus an exact physical evolution-intertwiner is not established by the metric-compatible Galerkin model. Formal-time error bound:
```
|| ( exp(u A_s) S - S exp(u A_G) ) G^-1/2 ||_F
   <= |u| sqrt(242/3).
```
No SI physical u-to-time map.

**Separate independent-form refinement control:** m unit-weight fine edges between two retained coarse endpoints give `G_m=diag(1,1,m)`, projected `A_G` with squared angular frequency2/m and fine-image leakage squared2(1-1/m). Exact m=1,2,4,8,16,32,64 fixtures pass. This shows no refinement-independent *native unit-weight frequency* or exact closure for m>1, but it does not preclude other metrics, physically calibrated clock choices, or 3D mesh refinement rules. Do not fit a compensating gain without labeling it candidate.

## Reproduction

Repository:
- `experiments/klein-tetra-face-flip-20261103/SCALE_AWARE_COARSE_EVOLUTION_v0.8.md`
- `experiments/klein-tetra-face-flip-20261103/metric_coarse_generator_v08.py`
- `experiments/klein-tetra-face-flip-20261103/scale_interval_control_v08.py`
- `experiments/klein-tetra-face-flip-20261103/induced_generator_results_v08.json`, `scale_interval_results_v08.json`.
- `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.8.json`, this handoff, candidate/session journal and record.

Full standalone verified `KLEIN_SCALE_AWARE_EVOLUTION_v0.8.zip`: includes exact local v0.6/v0.7 dependencies, `induced_generator_v08.py`, `interval_scale_control_v08.py`, outputs, README and SHA256 manifest. ZIP SHA256 `58999dcc1a030c4ac427ef1c2c57c384e04b0d4bafd7a2ba8001ddf3b9cd92d7`; local `induced_generator_results_v08.json` SHA256 `cbea7c133b7dad69a7a95e14d9cd24f07ab6ad1546825beb69d67177a1f76493`. These are local bytes; do not assert byte identity with GitHub scripts. Exact local SymPy replay PASS. Github integrity CI should be checked for the final commit. External non-constructor mathematical review NOT_RUN.

## Next discriminant and stop condition

A mathematical coarse generator with conserved native quadratic support now exists for the *chosen* fine metric, and the cross-scale discrepancy is exactly quantified. The physical frontier is not another arbitrary scaling factor. Specify source-admitted metric/clock and topological-frame preparation across at least **two tetrahedral refinement levels**; preregister current, loop holonomy, acceptable dynamical error and null. Without an independently selected physical unit map and reference, park Klein correspondence as a conditional mathematical transport sector; physical promotion remains 0.
