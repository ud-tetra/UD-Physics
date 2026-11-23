# K4 parity-sector 13/8 invariance handoff — v1.0 (2026-11-05)

**Status:** EXACT / CONDITIONAL / SCOPED NO-GO / OPEN. **Physical promotion = 0.** Continuing existing task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, HELD claim `refs/heads/claims/klein-tetra-face-flip-20261103` SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`; PR #301 remains draft. Main rechecked at `698d6d66147131d43e364a1736ca07ad0f3fa9d4`; original research-task base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. No merge, claim release, physical promotion or shared state mutation.

## Exact source and distinct objects

- Frozen `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md` P01–P06: K4 f0=4,f1=6, S4=24, `|Theta|=8=2^3`. This is **finite label cardinality**, not an 8-dimensional orthogonal Hilbert decomposition of native chains.
- Read-only separate Discovery `experiments/parity-dynamics-gauge-20261103/README.md` v0.1: opposite XOR projection from **illustrative** 10-bit raw state, eight equal-size fibers128; no canonical real-chain embedding or native micro update. The supplemental `UD_PARITY_DYNAMICAL_CLOSURE_AND_SYMMETRY_AUDIT_v0.2.md` in supplied task files independently corroborates symmetry orbit calculation, subject to its stated development status.
- Current claimed `experiments/klein-tetra-face-flip-20261103/K4_MULTILEVEL_METRIC_CLOCK_v0.9.md`: squared native **real** 1→4 leakage13; 4→16 leakage52; composed 1→16 leakage151/4, unit incidence and Euclidean metric.
- `experiments/qpb1-local-generators/README.md` v1.0 §2 gives `dim End_S4(C15)=13`, an **unrelated typed integer**. Coincidence of integers does not identify objects.

## Calculation and decision

The induced S4 action on Theta permutes the 3 opposite-edge pair bits, orbit partition `{000}`, `{001,010,100}`, `{011,101,110}`, `{111}`. All 24 checks PASS. After **adding** ℝ8 orthonormal parity basis and choosing an isometric lift `J_pv=Σ sqrt(p_theta)|theta>⊗v`, each new sector projector `Q_theta` is orthogonal, S4-covariant for orbit-constant p, and contributes `||Q_theta J_p R01||_F²=13 p_theta`. For uniform p=1/8 each contribution is 13/8.

**NO-GO to native uniqueness:** a strictly positive unequal orbit-constant p with p000=p111=1/4 and p_other_each=1/12 respects all 24 S4 permutations yet yields contributions 13/4 on 000/111 and 13/12 elsewhere. S4 alone does not force equal parity weights. Projectors on ℝ8 tensor native real chains are *new candidate operators*; the original Theta count supplies none on C15/C29. In a **separate toy** raw ℓ²(F2^10) counting space, eight orthogonal fiber projectors of rank128 do exist, but no native refinement-leakage intertwiner is defined.

**NO-GO to invariant total-sector value under tested normalization:** same uniform extension of R12 gives 52/8=13/2, and of R02 gives (151/4)/8=151/32. Dividing R12 by its four coarse top cells additionally reproduces 13/8 but defines a different per-cell observable. With generator rate scaled 2 the first uniform share becomes 13/2; with metric-measured squared norm scaled 2 it becomes 13/4. No physical SI normalization is source selected. The numerical proximity of 13/8=1.625 to the Planck-length coefficient in SI is **not** a length derivation or prediction.

## Reproduce and artifacts

- `experiments/klein-tetra-face-flip-20261103/PARITY_13_OVER_8_SOURCE_AUDIT_v1.0.md` — proof, typed source dependence, alternative sector assignments.
- `experiments/klein-tetra-face-flip-20261103/parity_13_over_8_verify_v10.py` — self-contained exact SymPy K4 1→4→16 residual, S4 orbit and sector weight replay.
- `experiments/klein-tetra-face-flip-20261103/parity_13_over_8_results_v10.json` — machine-readable fixture and final archive hash.
- `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_parity_13_8_v1.0.json` — typed mathematical receipt.
- Standalone `K4_PARITY_LEAKAGE_13_OVER_8_AUDIT_v1.0.zip` includes two independent-form algorithms, toy raw-fiber group check, source v0.9 input, self-contained replay, complete exact JSONs, six passing unit tests and SHA256 manifest. Final archive SHA256 **`fa693e0812e44c95101858015461ea80801e5e4e0bfd69393f92d9caafefe4c8`**. GitHub code and standalone code are equivalent, but their bytes are not asserted identical.

**Local exact constructor:** PASS, six tests PASS, all 24 S4 checks PASS, three refinement residual totals PASS. External non-constructor mathematics review NOT_RUN. GitHub CI integrity status is tracked by final SHA; CI does not validate scientific truth.

## STOP/REOPEN condition

Freeze physical promotion of 13/8. Reopen the parity-leakage bridge only after identifying a typed native `Q_theta` projector or source-chosen sector measure, a compatible evolution/operator decomposition, and an invariance result across K0→K1/K1→K2 with a **fixed preregistered observable and normalization**. A Planck-length bridge additionally needs units, an independently justified length map, calibration, uncertainty, null and falsifiable held-out prediction.
