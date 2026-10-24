# Which graphite angles does the honeycomb harmonic port select?

**Status: EXACT / CONDITIONAL topology limitation; NUMERICAL source-rounded conventional contrast; UD material selection OPEN.** This follows the [graphite working preprint](../graphite-superlubricity/README.md), [source constraints](../graphite-source-constraints/README.md), and [cross-loss bound](../graphite-cross-loss/README.md). The observed angle pair was known before this audit; it is not an independent prediction.

## State the experimental target accurately

The [Chen *et al.* PRL abstract](https://doi.org/10.1103/ly48-b4l2) reports **sharp detectable friction peaks** at 21.8° and 38.2°, corresponding to the `(2,1)` commensurate moiré. Other tested commensurate `(m,n)` patterns had no detectable signal, while the paired peaks had negligible load dependence compared with the coaligned state. A detectable peak is not zero force. The accessible article and supplement require subscription; no force table, detection threshold, uncertainty, or mode-loss matrix was available here. The reported weak load dependence is an observed comparison, not a numerical zero derivative.

## Exact quotient-family result

For a connected, closed periodic honeycomb quotient with `N` hexagonal faces on a torus, the chain dimensions are `(dim C₀,dim C₁,dim C₂)=(2N,3N,N)`. Over `Q` or `R`, connectedness and orientation give `rank B₁=2N−1` and `rank B₂=N−1`, hence

`dim H¹=3N−(2N−1)−(N−1)=2`, independent of `N`.

Let `M∈R^(3N×2)` have columns in the harmonic edge subspace, so `B₁M=0`. The proposed weighted incidence port `S_N(w)=Mᵀ W B₁ᵀ` vanishes when `W=wI`, because `S_N=w(B₁M)ᵀ=0`. The same two-dimensional carrier and uniform-weight cancellation therefore occur in *every* such toroidal quotient. Neither property alone selects `N=7`.

An independent exact integer incidence replay constructs quotients indexed by `N=m²+mn+n²` for `(2,1)`, `(3,1)` and `(3,2)`, checks `B₁B₂=0` and rational ranks, and obtains:

| Pattern | N | `(V,E,F)` | `(rank B₁,rank B₂)` | `(b₀,b₁,b₂)` |
| --- | ---: | --- | --- | --- |
| `(2,1)` | 7 | `(14,21,7)` | `(13,6)` | `(1,2,1)` |
| `(3,1)` | 13 | `(26,39,13)` | `(25,12)` | `(1,2,1)` |
| `(3,2)` | 19 | `(38,57,19)` | `(37,18)` | `(1,2,1)` |

This is an **angle-selectivity no-go for the two stated topological features**, not a no-go for an additional constitutive UD law. A proposed nonuniform material weight or damping law could depend on `N`; it must be specified independently and compared against other moiré quotients before it explains the seven-cell signal.

## Conventional static contrast and its limits

The independent [Lebedeva *et al.* first-principles study, arXiv:2511.01338v1](https://arxiv.org/abs/2511.01338) reports, for *rigid* twisted graphene bilayers, the following source-rounded values (Table 2, Table 6 and text following Table 2). These are computations, not the PRL friction measurements:

| Source quantity | `(2,1)`, N=7 | `(3,1)`, N=13 | Ratio `(2,1)/(3,1)` |
| --- | ---: | ---: | ---: |
| DFT PES corrugation, µeV per atom (Table 2) | 0.347 | 0.027 | ≈12.9 |
| DFT-derived ideal rigid static shear strength, Pa (Table 6) | 13,900 | 6,680 | ≈2.08 |
| Earlier reported KC PES corrugation, µeV per atom (as compared in source text) | 87.7 | 20.6 | ≈4.26 |

The source-reported KC corrugation exceeds its DFT value by about **253×** for `(2,1)` and **763×** for `(3,1)` under the compared rigid-layer calculations. The source stresses that empirical potentials do not reproduce its quantitative PES amplitudes. This does **not** establish corresponding errors in the vertical mode frequencies or cross-mode damping of our KC-plus-plate toy model: those are different derivatives and boundary conditions. It does mean that toy-model transfer coefficients must not be treated as calibrated graphite friction.

The approximately 12.9-fold corrugation contrast is **not** a 12.9-fold ideal static force contrast: the paper's first-harmonic shear estimate is only about 2.08-fold, reflecting different moiré periods and PES types. Nor is either ratio a measured kinetic-force ratio. Table 2 gives an approximately 0.004 µeV/atom `(3,1)` profile barrier, while Table 6 lists a 0.0239 µeV/atom first-harmonic derived barrier; the paper identifies numerical scatter for this small profile. Keep the two estimates and their methods separate instead of selecting one as a measured value.

**Conditional detection example, not a fit:** if one assumes the same positive force-to-ideal-shear factor `α` for both contacts and a shared force threshold `T`, then `6680 Pa < T/α ≤ 13900 Pa` is sufficient for the conventional static estimates to give a detectable `(2,1)` signal but an undetectable `(3,1)` signal. Neither `α` nor `T` is supplied by the public PRL abstract, and static strength is not kinetic friction. This example shows why the reported detection pattern, by itself, does not establish an added UD mechanism.

## Discriminating measurement

For each angle and matched contact/temperature/speed/load, retain the **signed** lateral force, uncertainty, and a calibrated detection limit. Fit a two-dimensional conventional PES and force readout independently. Then freeze a restricted `N`-dependent UD source-and-loss law *before* testing its force residual at the paired angles and at `(3,1)` and another moiré control. A law with a free weight and bath at each angle would be unidentifiable; the UD candidate must predict a shared contrast or parameter constraint. Complex loss and its pressure derivative remain necessary for the earlier drag reduction. No independent physics review or mainline physical promotion is claimed.

Run `python3 experiments/graphite-quotient-contrast/replay_quotient_contrast.py`. [Captured calculation](../../artifacts/graphcontrast-20261023-f7047e21/exact-001/manifest.json) and [mathematical receipt](../../candidates/graphite-quotient-contrast/mathematical_receipt.json) record the source versions, units, assumptions, exact ranks, and rounded-input arithmetic.
