# Actual K4 recursion: native metric, transport-current and clock selection audit v0.9

**2026-11-05 — UD-Physics Discovery. EXACT/CONDITIONAL; SCOPED NO-GO; physical promotion 0.**

## Scope, sources and types

Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, HELD claim `refs/heads/claims/klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated Discovery branch and draft PR #301; original task base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, main reverified at `e400dfb715262a44b3bbb2e929c7b438028af67e`. No mainline promotion or overwrite.

Read-only exact UD source: `experiments/four-cell-tetrahedron/README.md` v1.0 §§Definition and scope, Exact sharing/geometry/recursive counts; `experiments/pachner-state-transport/README.md` v0.1 §1→4 transport and metric mismatch; `experiments/qpb1-local-generators/README.md` v1.0 §§1–3 unit-incidence K4 generator and S4 action. Current v0.8 Klein CW metric-pullback theorem is background only. This experiment uses **actual K4 tetrahedron refinement, not the assumed Klein×I seam**; orientation character `rho(h)=-1` is optional scalar path transport over these carriers, not a new clock.

Let `K_0` be the filled tetrahedron [0123], `K_1` its centroid 1→4 subdivision, and `K_2` the centroid 1→4 subdivision of each of the four top cells. Each uses ascending oriented simplicial bases and **unit Euclidean chain metric** `H_n=I`, exact Z boundary `D_n`, and source-type formal unit-incidence generator `A_n=D_n-D_n^T` on real chains. No empirical time, volume conductance, physical energy or length map is assumed.

## 1. Exact native 1→4 subdivision and S4 covariance

A parent oriented top tetrahedron [a b c d] with new centroid z maps to the signed sum of four positively oriented child tetrahedra:
```
F_3([a b c d]) = Σ_i (-1)^(i+1) [sorted((a,b,c,d)\{vertex_i}) ∪ {z}].
```
Every lower-dimensional old simplex maps identically to its existing target simplex. The sign is fixed by `D_f F=F D_c`, not by normalizing top stock. Apply it at each stage. Exact f-vectors:
```
K0: (4,6,4,1), total 15
K1: (5,10,10,4), total 29
K2: (9,26,34,16), total 85.
```
Both integer chain maps satisfy all graded boundary compositions. The centroid labels transform under the induced action of all 24 S4 permutations. Exact tests give `R_{n+1}(g)F_n=F_n R_n(g)`, `[R_n(g),A_n]=0`, and `[R_n(g),A_{G,n}]=0` for every g∈S4 at both refinement transitions.

## 2. Canonical induced metric / local quadratic currents

The integral maps `F_{01}:R15→R29`, `F_{12}:R29→R85` have exact pullback metrics
```
G_01=F_01^T F_01=diag(1 repeated14, 4),
G_12=F_12^T F_12=diag(1 repeated25, 4 repeated4).
```
Their composite `F_02=F_12 F_01` gives `G_02=diag(1 repeated14, 16)`. These are chain-amplitude squared multiplicities under fine **unit weights**, not physical tetrahedral volumes. No coefficient is calibrated.

For every transition c→f set `G=F^TF` and the **unique unit-fine-metric Galerkin coarse generator**
```
A_G = G^-1 F^T A_f F.
```
Since `D_f F=F D_c` exactly,
```
A_G = D_c-G^-1 D_c^T G.
```
It obeys `A_G^T G+G A_G=0`. With coarse simplex i and boundary/coface neighbor j,
```
J_(i←j) = 2 G_ii (A_G)_ij y_i y_j = -J_(j←i)
d(G_ii y_i²)/du = Σ_j J_(i←j).
```
Thus local quadratic support is conserved on the coarse incidence graph; it is **not** a physical energy current. There are 28 native incidence pairs on K0 and 66 on K1 (12+12+4 and 20+30+16, respectively). The same source-type conservation holds separately for the full fine A_f under the fine unit metric.

## 3. Exact nonclosure and spectrum controls

Define `R=A_f F-F A_G=(I-FG^-1F^T)A_f F`. Exact results:

| Transition | Induced top diagonal | squared Frobenius norm of R | weighted residual² |
|---|---|---:|---:|
| K0→K1 | 4 | 13 | 13 |
| K1→K2 | 4 each of 4 | 52 | 52 |
| K0→K2 | 16 | 151/4 | 151/4 |

Every R is orthogonal to im F, but nonzero. Hence **NO-GO (scoped)** for exact native unit-incidence dynamics intertwining under the chosen subdivision and metric; the projected coarse systems conserve their own induced norms but are not closed subsystems of the fine dynamics.

The exact characteristic polynomials, with angular frequencies measured per **dimensionless formal u**, are:
```
native K0: lambda*(lambda²+4)^7
native K1: lambda*(lambda²+1)*(lambda²+5)^13
induced coarse K0 from K1: lambda*(lambda²+1)*(lambda²+4)^6
induced coarse K1 from K2:
  lambda*(lambda²+5)^10*(4lambda²+1)*(4lambda²+5)^3/256
induced coarse K0 directly from K2:
  lambda*(lambda²+4)^6*(4lambda²+1)/4
```
Source-preferred unit gains have native K0 frequency2 but K1 frequencies1 and√5. No **single scalar clock rescaling** can send both distinct K1 active frequencies to K0's one active frequency. Different gain functions or mode projections alter the hypotheses; they are not a derived universal physical clock.

## 4. Orientation holonomy, information and no physical promotion

A separately declared flat Klein seam orientation character `rho(h)=-1` acts as a scalar sign on either parent or refined chain carrier, hence `F rho=rho F` at all stages. Squared norms and quadratic-current magnitudes remain unchanged under this global sign, so the refinement test is blind to this topological orientation character. Nontrivial source-native signed S4 transports and relative-frame readouts remain subject to the earlier even/odd seam-extension selection ambiguity. The Klein geometry, physical clock, mass/charge, matter retention and measured orientation frame have **not** been selected. Do not call the multi-level calculation evidence of time dilation, new particle sector or physical duality.

## Reproduce and evidence scope

```bash
python3 experiments/klein-tetra-face-flip-20261103/k4_two_refinements_v09.py
python3 -m unittest discover -s experiments/klein-tetra-face-flip-20261103 -p 'test_k4_refinement_v09.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Local equivalent exact SymPy script PASS at levels 0,1,2; 24 exact signed S4 checks PASS; standalone verification package and exact JSON receipt attached separately. The independent check of the native K0/K1 characteristic polynomials uses factorized exact integer matrix spectra and the source QPB1 boundary rank identity. This is still constructor scrutiny, not external scientific replication. GitHub CI tests repository integrity only; external non-constructor math review NOT_RUN.

**Disposition:** AUTO_LOCK only the scoped K0/K1/K2 exact signed subdivision, induced metric, conservation and spectral mismatch calculations (conditional on unit fine metric). AUTO_FREEZE claims that a Klein phase or a universal time-dilation clock is derived. **Next discriminant:** source the criterion that selects a metric/clock from geometry and a real packet evolution/observable, or stop the physical branch; do not repair frequency mismatch by target-informed gains without labeling FIT/CANDIDATE.
