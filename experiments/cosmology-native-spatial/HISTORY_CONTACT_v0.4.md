# Conditional ancestry contact and local move-order test v0.4

Session `cosmology-history-contact-diamond-20261106-01`; base `ud-tetra/UD-Physics@29d831b571a0a3177a1fb1b1a5bc7cf3c7a8f747`. **EXACT under declared bookkeeping / CANDIDATE constitutive rule / SOURCE_BLOCKED dynamics.** Physical promotion 0. Extends [v0.3](CONTACT_OWNERSHIP_v0.3.md); no empirical or astronomical data.

## Proposed event/history rule

On a finite pure tetrahedral complex, retain a labelled ancestry forest of top cells. For each old simplex `σ` and original parent top cell `τ` containing it, store its initial Q177 share `w_(σ,τ)=1/n₃^old(σ)` as a separate nonnegative account. At a **postulated** local 1→4 event in a descendant cell, divide that cell's account equally among its child tetrahedra containing `σ`, assigning zero to children not containing `σ`. Leave other accounts unchanged. Old simplex amplitudes are copied by the source chain map on lower grades. The event trigger, new top amplitude contact, newborn simplex stock and current across the event are **not** defined by this rule. It is a local conditional bookkeeping map, motivated by parent-share conservation and symmetry among incident children, not selected by Q169/Q170.

**EXACT conditional conservation:** for each account, the three incident children of a vertex each take one third of its prior share (or the corresponding number of incident children for another simplex), so their sum equals that account. Every event preserves the sum over cells of old-simplex support. All weights remain nonnegative and relabel equivariantly if the ancestry labels transform with the cells. This does not preserve the intrinsic new-only Q177 allocation, nor global support of new simplex amplitudes.

## Glued diamond and nested control

Start with `T₀=0123,T₁=0125` sharing face `012`, unit amplitude on vertex 0 and initial accounts `(1/2,1/2)`. Refine `T₀` at center 4, then choose two distinct incident children `A=0124` and `B=0134` to refine at centers 6 and 7. The order `A→B` or `B→A` gives the identical final labelled carrier and account map. Each selected child's `1/6` account becomes three `1/18` accounts; the third incident child remains `1/6`, and untouched `T₁` remains `1/2`. Six `1/18` shares plus `1/6+1/2` sum to 1. **EXACT:** this one disjoint-event commuting diamond is flat for this rule. It does not establish general Pachner coherence, overlapping-interior move commutation, or a physical event update.

If only `A` is refined after the first split, five descendants of `T₀` contain vertex 0. Recursive shares are `(1/18,1/18,1/18,1/6,1/6)` up to ordering; untouched `T₁` retains `1/2`. A different **CANDIDATE** that globally redivides the old parent's `1/2` evenly among its five incident leaves assigns `1/10` to each, also preserving parent support and relabeling symmetry of the final descendant set. Intrinsic new-carrier Q177, which forgets ancestry, assigns `1/6` to each of the six currently incident cells including `T₁`, changing parent shares to `(5/6,1/6)`. The three allocations are distinct:

| Rule | Refined original parent's five leaf shares | Untouched neighbor | Parent total |
| --- | --- | --- | --- |
| Recursive local split | `3×1/18, 2×1/6` | `1/2` | `1/2` |
| Global parent redivision | `5×1/10` | `1/2` | `1/2` |
| Intrinsic new Q177 | `5×1/6` | `1/6` | `5/6` |

**Selector result:** positivity, parent-share conservation, relabeling covariance and this commuting diamond do not select recursive versus global parent allocation. Recursive locality plus an explicit no-redistribution-of-existing-descendant-accounts axiom would select the recursive update for that event, but this axiom is a new constitutive premise. The old and new metrics/generators and open-system currents must then be made compatible; neither bookkeeping rule supplies a Q170 event flux or a physical spatial metric.

**Disposition:** retain the exact narrow diamond and ambiguity witnesses; no AUTO_LOCK of a UD constitutive contact. **AUTO_FREEZE** a claim that conservation and one commuting check uniquely derive history contact. Test overlapping move relations and source-select a metric-adjoint generator/current only after a justified event rule appears. N0 and G0 physical scoring remain parked; promotion 0.

Replay `python3 experiments/cosmology-native-spatial/history_contact.py` with exact fractions and explicit labelled tetrahedra. The calculation uses no fitted constants or observational target.
