# Klein–K4 Discovery v0.7 — refined-hop locality and exact generator nonintertwining

**Session:** ktff-20261103-01; **task:** klein-tetra-face-flip-20261103; **claim:** `refs/heads/claims/klein-tetra-face-flip-20261103` HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Existing isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, PR #301 draft. Original source main base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, main checked at `fbb21d58a7662b737e4a2fb5276fefedc547412b`. No integration, mainline export, physical promotion or claim release.

## Sources and typed model

The imported native K4 basis/generator is `experiments/qpb1-local-generators/README.md` v1.0 §§1–3. The prior source-bound construction is `experiments/klein-tetra-face-flip-20261103/INTEGRAL_SUBDIVISION_STRONG_RETRACT_v0.6.md` and its **complete locally archived integer P,S,H matrices**. The assumed Klein×I nonorientable seam, orientation local coefficients and 72-tetrahedron topology remain unchanged; no physical clock or SI metric is supplied.

The source 72-tetrahedron twisted simplex carrier has 348 real coordinates and the minimal CW target has 12. The v0.6 reverse integral chain map P and forward local barycentric subdivision S satisfy `PS=I`, `d_c P=P d_s`, `d_s S=S d_c` and `d_s H+H d_s=I-SP` exactly.

## 1. Corrected finite graph support audit

Previous v0.6 `minimum distance≤1` is a weak vertex-pair diagnostic, not a full support radius. Compute quotient shortest paths on the 18-vertex ordinary barycentric 1-skeleton, whose graph diameter is 3. For each nonzero P_k[i,j], form X=vertices of source simplex j, Y=union of vertices of every simplex appearing in the forward subdivided target cell S_k[i]. New max-pair metric `r=max_{x∈X,y∈Y}dist(x,y)`. Over all P nonzero entries, counts by degree are (18,181,50,1), and the **exact global maximum r is 2**. The degree1 max-pair histogram has 67 entries at distance1 and114 at distance2; degree2 all 50 at distance2; degree3 its sole entry distance2. Hausdorff maximum is also2. Thus the old one-hop statement cannot be promoted to a full support guarantee, but this fixed complex has an exact two-hop maximum under the declared unweighted graph metric.

## 2. Refinement-stability: exact scoped no-go

In a separately controlled chain of m refined edges joining retained coarse endpoints A and B, assume an **integral augmentation-preserving** degree0 retraction P0 to Z[A]⊕Z[B] fixing original endpoints. For the middle refined vertex v_i, the two output coefficients sum to1, so at least one endpoint occurs; its refined graph-hop distance is at least min(i,m−i). Consequently
```
sup_i radius(P0(v_i)) >= floor(m/2).
```
Constructive threshold retractions attain this bound and obey chain commutation with a corresponding P1 edge map and PS=I. Exactly computed controls m=2,4,8,16,32,64 give radii1,2,4,8,16,32. There can therefore be **no uniform bound in refined graph hops to retained original endpoints** across arbitrary m within these hypotheses. This is NOT a general obstruction to metric length locality, coarse-cell support, hierarchy-aware renormalization, or all possible Klein refinements. It does not show that every different refinement of the 72-tetrahedron P has this particular growth.

## 3. Evolution: boundary intertwinement does not imply skew-generator intertwinement

Extend the two integer carriers to real coefficients with **separately chosen unit Euclidean coefficient metrics**. Define `A_s=d_s-d_sᵀ` on 348 real coordinates and `A_c=d_c-d_cᵀ` on 12. These are source-*type* skew operators, not a uniquely sourced 3D physical law.

Exact integer matrix residuals:
```
E_P = A_c P - P A_s : 12 × 348,
  rank_Q 10, 244 nonzeros, ||E_P||_F²=2842.
E_S = A_s S - S A_c : 348 × 12,
  rank_Q 11, 286 nonzeros, ||E_S||_F²=298.
```
Thus **NO-GO under the selected two unit metrics and unmodified skew generators**: the exact integral P,S,H chain equivalence does not intertwine continuous-time evolution. It also does not generate a physical time-to-event map or conserved energy translation. Changing the coarse metric/generator would create a new branch requiring explicit normalization and source-current budget.

## 4. Completed, not completed and release

**COMPLETED exact finite mathematics:** full-support two-hop locality audit on the fixed complex, interval refinement graph-hop no-go under endpoint anchoring, complete exact coarse/fine skew mismatch matrices.

**NOT ESTABLISHED:** strict refinement-uniform packet locality using a physical/spatial metric; any natural multiscale metric or chosen coarse generator; physical orientation-reference readout; causal propagation; native Klein seam selection; material retention; empirical correspondence. The v0.5 native 5D K4 invariant hull is a different conditional model, not a source for full 348-to-12 intertwining.

The scripts `locality_audit_v07.py`, `refinement_control_v07.py`, `dynamical_intertwiner_v07.py` and result JSON live beside this proof. Because exact full v0.6 integral-map reconstruction is archived as a standalone user-visible reproducibility ZIP rather than included as byte-identical GitHub source, the dependent v0.7 scripts should be copied into an extracted v0.6 package. A new ZIP `KLEIN_LOCALITY_DYNAMICS_v0.7.zip` contains these exact local executable programs and the v0.6 dependencies, results and SHA-256 manifest. ZIP SHA-256 `7768e734829db3e725318592fcd95f41c0f7a7ab8e2e87888c73e4e42f36c6ca`. Equivalent local exact execution PASS, external non-constructor review NOT_RUN. Repository CI verifies integrity only.

**Next discriminant:** declare a physically and structurally meaningful notion of *scale-aware locality* (e.g. bounded original-cell neighborhoods, or calibrated lengths), then derive a source-selected metric-compatible coarse generator or prove a new no-go under those declared hypotheses. Do not hide mismatches by arbitrary rescaling.
