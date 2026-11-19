# UD-Physics Klein–K4 two-level clock and metric audit v0.9

**2026-11-05 / Discovery, EXACT-CONDITIONAL + NO-GO / physical promotion 0.**

**Task:** `klein-tetra-face-flip-20261103`; **session:** `ktff-20261103-01`; live **HELD** claim at `refs/heads/claims/klein-tetra-face-flip-20261103`, SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Existing isolated Discovery branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, draft PR #301. Task original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; main at this resume `e400dfb715262a44b3bbb2e929c7b438028af67e`. Reconcile main before any integration; do not change shared CURRENT, release claim or promote physics.

## Source and exact test

Read-only `experiments/four-cell-tetrahedron/README.md` v1.0 (definition/recursive counts), `experiments/pachner-state-transport/README.md` v0.1 §1→4, and `experiments/qpb1-local-generators/README.md` v1.0 §§1–3. Use unmodified signed simplicial incidence and the exact degree-one oriented 1→4 top-cell chain map; retain H=I at each level, no freely chosen gains.

K0 original filled tetrahedron, K1 four child tetrahedra, K2 sixteen child tetrahedra. Exact chain dimensions by degree:
```
K0 (4,6,4,1), total15
K1 (5,10,10,4), total29
K2 (9,26,34,16), total85.
```
Both integer F subdivision maps pass dF=Fd. Composite map also integral. All 24 signed S4 vertex relabelings commute with both subdivision maps, the source-type native skew generators and the projected coarse generators; centroids are permuted according to their parent tetrahedra.

## Exact induced metric and local dynamics

Pull the unit fine metric back through integer F: `G01=diag(1^14,4)`, `G12=diag(1^25,4^4)`, composite `G02=diag(1^14,16)`. No coefficients are fitted. For each map, `A_G=G^-1 F^T A_f F=d_c-G^-1 d_c^T G` with `A_f=d_f-d_f^T`. The induced generator is G-skew and conserves `y^T G y`; signed antisymmetric incidence currents `2Gii Aij yi yj` conserve native quadratic support. This is mathematical chain-amplitude bookkeeping, not calibrated physical energy.

Fine-image dynamical residuals `R=A_f F-F A_G` are orthogonal to the embedded coarse image but **not zero**. Exact squared Frobenius norms:
```
K0→K1   13
K1→K2   52
K0→K2   151/4.
```
The K0 native charpoly is `λ(λ²+4)^7`, K1 native `λ(λ²+1)(λ²+5)^13`. The projected K0 generator from K1 has `λ(λ²+1)(λ²+4)^6`. The projected K1 from K2 has `λ(λ²+5)^10(4λ²+1)(4λ²+5)^3/256`. The K0 direct projection from K2 has `λ(λ²+4)^6(4λ²+1)/4`. Thus **NO-GO** for one scalar clock normalization making the complete native K0 and K1 active spectra identical: K0's only nonzero angular magnitude is 2; K1's are 1 and √5. A changed metric/generator, mode restriction, or physical time correspondence changes the assumptions.

## Klein seam relevance and limits

A separately **assumed** flat orientation character rho(h)=-1 commutes with every integral K4 refinement map and its scalar action does not change squared norms. However ordinary centroid splitting is NOT a derivation of the nonorientable Klein seam topology, an autonomous face flip, time dilation, persistent matter or a physical frame reference. The nonorientable 72-tetra Klein×I model of v0.4–v0.8 is a **distinct carrier**. The present test isolates the underlying K4 metric/clock dependency without fitting any physical constants.

## Reproduction

In GitHub branch:
- `experiments/klein-tetra-face-flip-20261103/K4_MULTILEVEL_METRIC_CLOCK_v0.9.md`
- `experiments/klein-tetra-face-flip-20261103/k4_two_refinements_v09.py`
- `experiments/klein-tetra-face-flip-20261103/test_k4_refinement_v09.py`
- `experiments/klein-tetra-face-flip-20261103/k4_multilevel_results_v09.json`
- `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.9.json`
- This handoff and session journal/record.

Standalone local `KLEIN_K4_TWO_REFINEMENT_v0.9.zip` has equivalent exact SymPy scripts, six passing local regression tests, results, replay log, README and SHA-256 manifest. ZIP SHA256 `83a4e83ab4af8a985a4e951e4a55296f16bc216763c0fe6e70f5ab1b346ae147`. Local source not asserted byte-identical with GitHub source; constructor verification is **not** external non-constructor review. Repository integrity CI status should be tied to final head.

## Next discriminant

Need a source-selected metric/time law and measured framed transport observable across at least two K4 levels; freeze tolerances and null before any exposure to laboratory measurements. Stop the scalar-clock repair branch under unchanged unit-incidence hypotheses. Physical promotion 0.
