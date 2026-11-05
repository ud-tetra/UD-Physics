# UD-Physics Discovery — Weighted K4 admission/observability v1.6 handoff

**2026-11-05. EXACT-CONDITIONAL / SCOPED NO-GO / SOURCE RULE OPEN; PHYSICAL PROMOTION 0.**

**Task ownership:** existing HELD `klein-tetra-face-flip-20261103` claim at SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`; session `ktff-20261103-01`, isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, draft PR #301. Base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, main checked `738b9d205fd9f9735a05d4976de70f1519474bff`. No mainline/accepted-ledger/site modification, merge or release.

## Source contract

Frozen ledger v0.39 Q165/Q166/Q169/Q170/Q171: signed fixed-complex Hasse generator, support/currents and top-core square; Q173 masks face-cell current but selects no mask transition or refinement; Q177–Q179 split existing stock per cell, not graph-edge conductance. A radial graph edge at the first centroid split belongs to 3 children, an old edge to 2; their ownership fractions are 1/3 and 1/2, not the 1/4 geometric-volume fraction. Source four-cell-tetrahedron v1.0 supplies child geometric volumes1/4, but not a conductance law. Source pachner-boundary-observability v0.1 specifies a development **candidate** static boundary port. Source pachner-state-transport v0.1 proves top-chain 1→4 degree-one map cannot conserve original Q165 unit top stock (1→4). Source pachner-current-metric v0.1 gives connected-Hasse diagonal-metric uniqueness for unchanged Q169. Uploaded master_action.md and packet_field_equation.md were inspected and contain reconstruction placeholders, not constitutive rules.

## Exact weighted-refinement theorem

For K_n the recursive 1→4 tetrahedral 3-ball, keep its six original edges at unit graph weight and assign every graph edge born at generation k>0 a **chosen** positive weight g_k. Fix four outer vertices and minimize 1/2 Σ(w_e(Δv_e)^2) over all internal vertices. The exact Schur boundary response is

```
Lambda_n = alpha_n (4 I4−1 1ᵀ),
alpha_n = 1 + 1/4 Σ_(k=1)^n (11/4)^(k−1)g_k,
alpha_(n+1)−alpha_n = (11/4)^n g_(n+1)/4.
```

Proof via old-old child multiplicity2, radial multiplicity3, and central five-node Kron elimination `w_parent=(11w_child+g_parent)/4`. **Every strictly positive new generation remains exactly distinguishable** under this static port. For nonnegative weights, finite exact saturation means all later g_k vanish (zero-weight disconnected vertices require energy-minimization limit).

For geometric g_k=g1 r^(k−1), response converges iff r<4/11, then `alpha_infty=1+g1/(4−11r)`; critical r=4/11 gives linear growth, larger r gives divergence. The **CANDIDATE** volume-inspired proxy g_k=4^(−(k−1)) gives alpha_n=9/5−4/5(11/16)^n, alpha∞=9/5 and exact native weighted results n0..3 = 1,5/4,91/64,1577/1024. It never reaches its limit at any finite n.

One invented response tolerance epsilon=1/100 gives earliest depth9 for a single adjacent increment ≤epsilon, and earliest depth12 for the entire remaining-to-limit tail ≤epsilon. They are different operational contracts, neither physical length, and Q171 internal core stocks can still differ.

## Current-source gate

Under **unchanged Q169** numerical skew A=d−dᵀ, connected full Hasse incidence and any positive diagonal H, skewness implies H=cI on every full fixed complex. The weight choice g_k≠1 requires a **changed** vertex-edge generator: `A_W=[[0,−B1W],[B1ᵀ,0]]`, `H_W=diag(I,W)`. This is exactly metric skew, preserving `||v||²+eᵀW e` and edge-incidence antisymmetric currents within each fixed complex. It does not preserve the *old* Q166 coefficients under their original normalization, nor supply a stock-conserving event between 15D and29D carriers. The integral K4 top map alone changes squared stock1→4. No source rule chooses g_k, a measurement tolerance, or a cross-complex event controller.

**VERDICT:** There is no source-selected finite K4 resolution floor or physical minimum length under examined sources. The optional geometric weighting can make a chosen boundary observable converge but not become exactly indistinguishable at a finite depth. Physical promotion 0.

## Reproducibility

Committed:
- `experiments/klein-tetra-face-flip-20261103/WEIGHTED_REFINEMENT_ADMISSION_v1.6.md`;
- `experiments/klein-tetra-face-flip-20261103/weighted_refinement_v16.py`, `independent_weighted_kron_v16.py`, `test_weighted_refinement_v16.py`, `weighted_refinement_results_v16.json`;
- `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_weighted_admission_v1.6.json`;
- this handoff plus updated candidate/session journal/record.

Complete locally executed `UD_K4_WEIGHTED_ADMISSION_GATE_v1.6.zip`: source, independent exact five-node Kron, detailed README, exact JSON, 8/8 passing local tests and SHA256 per-file manifest; archive SHA256 `5a788ed7d60d469c473acee1a60232069471606e47651b68b2bf176ba0ce635d`. Local source implementations are mathematically equivalent but not claimed byte-identical to GitHub scripts. Repo integrity CI status checked separately, not mathematics. Independent non-constructor verification NOT_RUN.

## Next discriminant / stopping rule

Do not assign g_k=1/4 from cell-volume counts or Q177 ownership. Find a source-selected refinement event/admission predicate and cross-complex current/reservoir with a fixed physical or native observer; only then test true operational stopping. If unavailable, retain exact optional weighted theorem and stop the native finite-floor mechanism branch pending new source evidence.
