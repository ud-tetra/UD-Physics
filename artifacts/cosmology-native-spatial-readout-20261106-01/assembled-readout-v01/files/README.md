# Intrinsic assembled-cell support filtration v0.1

Session `cosmology-native-spatial-readout-20261106-01`; source base `ud-tetra/UD-Physics@9360f5571a495ea29316bdece020eb8378d1b87b`. **EXACT conditional combinatorics / CANDIDATE observable / physical promotion 0.** No sky data, physical embedding, length, time or emission intensity.

## Object, map and assumptions

Take a finite pure 3D tetrahedral simplicial complex `K` with distinct top cells `T(K)` and real signed simplex amplitudes `c_σ` on unique simplices. Ledger `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) Q165 and Q177–Q179 define fixed-complex squared support and equal ownership `1/n₃(σ)` among top cells containing simplex `σ`. Define cell support `s_τ=Σ_(σ⊆τ)c_σ²/n₃(σ)`; `s:T(K)→R_≥0`. This is a sourced native stock allocation, not gravitational mass, energy, radiation or physical area.

**CANDIDATE readout choice:** use the top-cell dual graph `G_K` with vertices `τ∈T(K)` and edges when two tetrahedra share a triangular face. At threshold `u`, let `G_K[u]` be the induced subgraph on `s_τ≤u`, and `β₀(u)` its number of connected components. Keep the *whole* step function over exact support values; no target-picked single threshold. The graph adjacency and use of sublevel rather than superlevel are declared mathematical choices. This is an intrinsic cell adjacency filtration, not an image, physical spatial metric or nebular prediction. Domain is `(K,c)`; codomain is an integer-valued step function on native squared-amplitude stock `u≥0`.

**EXACT relabeling covariance:** a simplicial vertex bijection `p` maps each simplex and cell to its relabeled image, preserves containment and counts `n₃`, and signed amplitude transformation preserves `c_σ²`. Hence `s_{pτ}(pc)=s_τ(c)` and `G_{pK}[u]≅G_K[u]` for every `u`; `β₀` is invariant. This proof holds for all such bijections and any real amplitudes. It is not invariance under changing triangulation, metric or physical projection.

## Exact controls and limitations

Three top cells `0123,0124,0145` form a face-adjacent chain; first and third share only edge `01`. Put all lower-grade amplitudes zero and top amplitudes `(1,3,2)`, so `s=(1,9,4)` exactly. At `u=(0,1,4,9)`, `β₀=(0,1,2,1)`. The script checks all `6!=720` relabelings. If adjacency is changed to sharing an edge, `β₀(4)=1`: relabeling invariance alone does not select the *observable*. Q177/Q178 select `s` under declared fixed-complex conventions; they do not demand this filtration.

Under the source integral 1→4 chain subdivision on one tetrahedron, a unit old top coefficient maps to four unit new top coefficients. Q165 top stock and summed Q178 cell stock change exactly `1→4` in the unit metric. Thus the proposed filtration has no established cross-refinement stock or barcode invariance; the example witnesses a necessary normalization/contact rule, even though a particular `β₀` value may coincide. The [v2.1 action/metric audit](../cosmology-galactic-entry/G0_OPERATOR_RECOVERY_v0.1.md) keeps such newborn metric selection open.

The source fixed-complex generator `A_K=D_K−D_Kᵀ` gives a formal trajectory and conserves global Q165 stock, but neither selects the dual-graph threshold readout nor proves its persistence or preference for clusters. A conditional experiment may compute `β₀(u;s)` along a specified native trajectory; that is distinct from growth selection. No map to projected Hα intensity, PSF, gas dynamics or astronomical segmentation is available. The N0 physical readout remains **SOURCE_BLOCKED**.

Run `python3 experiments/cosmology-native-spatial/assembled_readout.py`. Exact integer/fraction assertions cover the filtration, 720 relabelings, adjacency negative control, and unit-metric 1→4 stock mismatch. Reopen the bridge with a source-selected assembled carrier and topology/readout convention, refinement/contact rule, physical projection and instrumental response; freeze an independent comparison before target exposure.
