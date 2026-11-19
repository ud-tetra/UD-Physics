# Klein–K4 locality and generator intertwining audit v0.7

**2026-11-04 — UD-Physics Discovery. EXACT / CONDITIONAL / SCOPED NO-GO / physical promotion 0.**

Existing held task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, claim ref `refs/heads/claims/klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Work on isolated Discovery branch of PR #301. Original source base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, current main checked `fbb21d58a7662b737e4a2fb5276fefedc547412b`. No mainline promotion or integration.

## 1. Source-bound question, types and metrics

Read-only source native K4 unit-metric generator: `experiments/qpb1-local-generators/README.md` v1.0 §§1–3. Prior conditional 3D Klein seam: `THREED_KLEIN_PACKET_SEAM_v0.4.md`, full pulled-back orientation coefficients `TWISTED_72_AND_INVARIANT_HULL_v0.5.md`, and exact integral P,S,H strong deformation retract `INTEGRAL_SUBDIVISION_STRONG_RETRACT_v0.6.md`.

**Typed carriers:** source `C_s=C_*(72-tetra Klein×I;Zrho)` with dimensions (18,102,156,72), real total 348 coordinates; minimal target `C_c=C_*(Klein;Zrho)⊗C_*(I)` dims (2,5,4,1), real total 12. P:348→12 reverse integral chain map; S:12→348 forward barycentric chain map, H:348→348 degree+1 homotopy, with `PS=I` and `dH+Hd=I-SP`. New seam gluing and local system are **assumed**. A formal evolution is constructed by separate **selected unit Euclidean metrics** and skew generators `A_s=d_s-d_sᵀ`, `A_c=d_c-d_cᵀ`. Neither has physical time units.

## 2. Correct the earlier finite one-hop diagnostic

Build the 18-vertex quotient 1-skeleton of the 72-tetrahedron barycentric complex (graph diameter 3). For each nonzero integral reverse-map coefficient `P_k[i,j]`, let `X_j` be the barycentric vertices of source simplex j and `Y_i` the union of **all** vertices in the source-supported forward subdivision `S_k(cell_i)`.

The v0.6 result had measured `min_{x∈X_j,y∈Y_i} dist(x,y)≤1`. That is a minimum separation and does **NOT** bound the full support.

The stronger exact finite audit now computes `max_{x∈X_j,y∈Y_i} dist(x,y)`, together with Hausdorff distance and all coefficient counts:

| Degree | Nonzero P entries | Minimum distances (histogram) | Maximum-pair distances | Hausdorff |
|---|---:|---|---|---|
| 0 | 18 | 0:2, 1:16 | 0:2, 1:16 | 0:2, 1:16 |
| 1 | 181 | 0:76, 1:105 | 1:67, 2:114 | 0:4, 1:133, 2:44 |
| 2 | 50 | 0:45, 1:5 | 2:50 | 1:47, 2:3 |
| 3 | 1 | 1:1 | 2:1 | 2:1 |

**EXACT (one fixed complex):** Maximum pair distance is **2**, not 1. The degree-3 coarse cell has a full 72-tetrahedron fundamental-chain support; its minimum separation is 1 while its maximum separation is 2. This is a genuine correction/strengthening of the earlier v0.6 minimum diagnostic, not a new physical range.

## 3. Refinement-uniform graph-hop locality obstruction

Declare a simpler independent control: one oriented interval with original endpoints A,B and `m` subdivided edges. Let its refined 0-cells be v0...vm, with graph distance dist(vi,A)=i, dist(vi,B)=m−i. Require an integral augmentation-preserving degree-0 retraction `P0:C0(refined interval;Z)→Z[A]⊕Z[B]` fixing the endpoints. For each vi, augmentation preserving means the two integer coefficients in P0(vi) sum to 1, hence at least one is nonzero. Thus its image support necessarily contains an original endpoint at distance at least `min(i,m−i)`. Choose i at the midpoint to conclude

```
max_i radius(P0(vi)) >= floor(m/2).
```

The exact constructive family `P0(vi)=A` up to a chosen middle cut and `=B` thereafter, with `P1([v_(i-1),vi])=(s_i-s_(i-1))[A,B]`, has `P S=I` and attains the lower bound. Explicit m=(2,4,8,16,32,64) yield radii (1,2,4,8,16,32).

**NO-GO, exact hypotheses:** No uniform bound in *refined graph hops to retained original endpoints* can hold across arbitrary subdivision depth for this class of coarse-endpoint retractions. This is not a no-go for locality measured in physical length, bounded original-cell neighborhoods, or scale-changing packet operators. It does not itself prove every refinement of the Klein 72-tetrahedron map has growing radius; it establishes why a claimed universal refined-hop bound needs changed hypotheses.

## 4. The source-type skew evolution fails to commute with the integral chain maps

Assemble exact block signed boundaries for the 348-dimensional twisted simplicial source and 12-dimensional minimal CW target and use unit Euclidean coefficient metrics, as in the previous model. Define skew generators `A_s=d_s-d_sᵀ`, `A_c=d_c-d_cᵀ`. Exact comparisons are

```
E_P = A_c P - P A_s : R^348 → R^12,
E_S = A_s S - S A_c : R^12 → R^348.
```

Although `d_c P=P d_s` and `d_s S=S d_c` exactly, these skew intertwining errors are nonzero:

| Error | Nonzero entries | Rank over Q | Squared Frobenius norm |
|---|---:|---:|---:|
| E_P | 244 | 10 | 2842 |
| E_S | 286 | 11 | 298 |

**NO-GO (chosen metric and generators):** Integral chain equivalence does not yield the same native-form dynamical evolution at both resolutions. The obstruction arises from the transpose/metric adjoints and is not removed by invoking homology alone. A new metric, coupling or generator is a distinct branch requiring independent source and current receipts; no rescaling is silently applied.

## 5. What remains physically open

The source 15D K4 five-dimensional invariant Krylov hull from v0.5 remains a separate exact conditional result. It is not an evolution intertwiner for this full 348D-to-12D P/S map. Nor is the K×I seam a source-selected UD packet gluing, or a framed loop sign a measured physical observable. Physical promotion remains 0.

Prioritize a **scale-aware locality contract** stating whether support is measured in original CW cells, refined hops or physical metric distance. If native UD does not supply a length metric, use explicit combinatorial neighborhoods and avoid asserting physical microcausality. For dynamics, source a metric-compatible coarse graining with an explicit energy/current ledger and operational loop readout, then test against the exact null here.

## Reproduce

The following v0.7 scripts are intended to run **alongside the full executable v0.6 standalone scripts and matrix certificate**, not as stand-alone repository-only calculations:

```bash
python3 locality_audit_v07.py
python3 refinement_control_v07.py
python3 dynamical_intertwiner_v07.py
```

The previous local archive `KLEIN_INTEGRAL_CHAIN_RETRACTION_v0.6.zip` contains `full_integral_bridge_v06.py`, `twisted_cover_source_v06.py` and their dependencies. Copy v0.7 scripts into that extracted folder to replay them with exact same inputs. Source code in GitHub and the local package is not asserted byte-identical. Outputs: `locality_results_v07.json`, `refinement_results_v07.json`, `dynamics_results_v07.json`. Locally exact Python/SymPy replay PASS, but non-constructor mathematical review NOT_RUN. GitHub CI integrity does not certify the calculation.

**Disposition:** Corrected exact finite support radius =2; scoped no-go on uniform refined graph-hop locality under endpoint anchoring; exact dynamical nonintertwining under selected unit metrics. Forward CW subdivision still cell-local; reverse P finite but not refinement-uniform under the tested hop criterion. No physical promotion.
