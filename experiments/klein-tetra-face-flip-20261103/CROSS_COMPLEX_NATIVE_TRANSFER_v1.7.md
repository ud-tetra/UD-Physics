# Native K4 1→4 cross-complex admission and conserved transfer gate v1.7

**2026-11-05 | UD-Physics Discovery | EXACT-CONDITIONAL; scoped NO-GO; source-selected event OPEN. Physical promotion 0.**

## Ownership and source provenance

Existing held task \`klein-tetra-face-flip-20261103\`, session \`ktff-20261103-01\`, claim ref \`refs/heads/claims/klein-tetra-face-flip-20261103\` at \`667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4\`. This work is on existing isolated branch and draft PR #301. Original task base \`0eef9a3f77198810b35bee8d3ef578ebc3af403a\`; source main checked \`234f54471c32cc9ad4873cd8042103fa19795909\`. No mainline export or accepted ledger edits.

Read-only source: \`sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md\` Q165 support norm, Q166 adjacent-degree currents, Q169 full fixed-complex Hodge skew, Q170 cut-current, Q171 top-cell core stock/current, Q173 face current masks, Q177–Q179 cell ownership. \`experiments/pachner-state-transport/README.md\` v0.1 (§1→4 map), \`experiments/pachner-current-metric/README.md\` v0.1, \`experiments/pachner-local-jump-current/README.md\` v0.1, \`experiments/qpb1-native-events/EVENT_CONTRACT.md\` v1.0. None supplies a physical event-selection law or dimensional time.

## Types and hypotheses

Let K0 be filled old oriented tetrahedron [0123] with real graded chain C0 of dimension15 and K1 the centroid 1→4 subdivision with C1 dimension29, graded vectors (4,6,4,1) and (5,10,10,4). For each fixed complex K use the ascending oriented integral boundary D_K, unit Euclidean metric, and native generator A_K=D_K−D_Kᵀ (D_K indexes the **complex**, not boundary grade). The evolution parameter u is formal, not seconds. Use Q165 squared stock S=||x||².

The integral degree-preserving subdivision F:C0→C1 acts as the identity on the 14 old lower-grade simplices and maps the old oriented top cell e to the signed sum q of the four child top cells. The original *shell geometry* is unchanged; shell amplitudes need not remain fixed after evolving.

## Theorem A — exact full-state chain/stock incompatibility

The top boundary B3(K1):R4→R10 has full column rank4. Because B3(K1) q=B3(K0)e, q is the **unique** top-grade column satisfying the old-boundary-identity chain equation. With child coefficients q=(1,−1,1,−1) under the fixed top basis,

\`\`\`
  D_K1 F=F D_K0,   FᵀF=diag(I14,4),
  FᵀF−I15=3 e eᵀ,
  ||F x||²−||x||²=3 c_parent_top²  (for every x).
\`\`\`

Thus F is exactly isometric on the 14D old lower-grade shell subspace and is not an isometry for any old state with occupied top amplitude. A half-amplitude top map q/2 makes its top norm1 but fails B3(K1)(q/2)=B3(K0)e. No **grade-preserving, boundary-identity, degree-one integral chain transport** simultaneously conserves the unchanged Q165 unit norm on every state. Additional metric, reservoir/source-sink, altered boundary transport or input restriction changes the assumptions.

This sharpens the source v0.1 top-cell mismatch (1→4) to a complete all-state operator identity, not a blanket ban on source-free support movement after a selected subdivision.

## Theorem B — exact conservative post-event native transfer WITHOUT a new reservoir

Let b=(B3(K0)e)/2 be the unit normalized oriented *outer-shell face chain*. b is a 2-cycle with B2 b=0 and contains no parent top amplitude, so F b is the same unit shell chain in K1 without a stock discontinuity. Define w=A_K1 b. Direct exact 29D matrices give

\`\`\`
 w=−q/2 (embedded at top degree),  <b,w>=0,
 ||b||²=||w||²=1,
 A_K1 b=w,  A_K1 w=−b.
\`\`\`

The full 29D source flow **restricts exactly** to the two-dimensional span{b,w}:

\`\`\`
 x_new(u)=cos(u)b+sin(u)w,
 S_original_shell_faces(u)=cos²u,
 S_four_new_top_cells(u)=sin²u,
 J_into_new_top(u)=sin(2u).
\`\`\`

This conserves total Q165 support, uses only source Q169 signed face–top incidences on the **already chosen refined complex**, and is covariant under all 24 signed S4 relabelings (b and w transform by the orientation sign). No extra reservoir or imported coupling is needed *after the subdivision*. However this flow is exactly reversible, with full top support at u=π/2 and zero at u=π. It supplies no one-way retention, action cost or time calibration.

On K0, the same b obeys A_K0² b=−4b; the old native phase has frequency2 and top stock sin²(2u), while new source flow has frequency1 and top stock sin²u. The differing continuation exposes the **missing rule selecting whether/when to change the active complex**. The carrier transition was postulated, not derived.

If the entire original shell amplitudes (or their squared norm) are required pointwise constant, interior starts with zero stock and Q165 norm is conserved, then no positive new interior stock can develop. Fixed shell *geometry* is a weaker and compatible hypothesis.

## Theorem C — Q173 masks are readouts, not an autonomous switch

K1 has ten distinct faces: 4 original outer faces and 6 new interior faces. If one *extends* Q173's binary face-current mask idea to all 10 faces, there are 2^10=1024 binary assignments. Full S4 symmetry permits four masks constant separately on the two face orbits. A masked readout h_f J23=0 when h_f=0 does **not** turn off the unchanged Q169 generator; the unmasked face-to-new-top stock current is nonzero for a suitable shell preparation.

A **different, explicitly added** model replaces only B3 with B3_h=diag(h)B3, leaving B2 unchanged. Exact exhaustive evaluation of all 1024 masks gives B2 B3_h=0 for **only all-off and all-on**. Two orbitwise-constant mixed masks violate boundary nilpotency. Both surviving choices are S4-covariant and their associated A_h=D_h−D_hᵀ conserve their own unit norm, yet for b the initial top derivative has squared norm0 (off) or1 (on). Source Q169 chooses the all-on original differential, whereas allowing all-off is a different rule. Symmetry, nilpotency and conservation therefore do not select a *new event trigger*. The historical Q173 128-mask audit was on a **different carrier** and is not this 1024-mask enumeration.

## Explicit Q171 sign-convention gate

With the same ascending boundary B3 and native A=D−Dᵀ, the direct derivative of top-core stock is

\`\`\`
 d(c3_tau²)/du = −2 Σ_f B3(f,tau) c2_f c3_tau.
\`\`\`

The literal frozen ledger Q171 row instead prints \`dot S_tau^core=+Σ_f 2 B3(f,tau)c2_f c3_tau\`. For face f=012, top tau=0124, signed B3(f,tau)=−1, and amplitudes c_f=c_tau=1, the **native matrix derivative** is +2 whereas literal plus-B3 formula gives −2. This is a typed **OPEN convention collision** if the same boundary basis is meant. An outward-vs-inward-current definition or opposite B3 convention might resolve it; do not silently rewrite frozen Q171 or claim that the printed sign is a measured physical flux. Preserve both formulas and require source reconciliation.

## Status and independent controls

- **EXACT conditional:** unique boundary-compatible signed F, rank-one norm defect 3eeᵀ; a source-native, S4-covariant and norm-conserving 2D shell-to-new-top oscillator under postulated K1; 2^10 mask exhaustive nilpotency gate and native/ledger signed-current witness.
- **NO-GO scoped:** full-stock isometry and degree-one boundary-identity top transport cannot coexist under unchanged Q165; no conservative new interior occupation if original shell stock is fixed pointwise and interior initially empty; face masks cannot be treated as a free modified boundary operator while retaining d²=0 except all-on/off.
- **OPEN:** an autonomous rule initiating K0→K1, Q173 mask selection, Q171 current direction alias, generic preparation, one-way retained burden, physically admitted observable and time/length/action bridge.
- **PHYSICAL PROMOTION = 0.** No Planck length or meters, no simulated physical measurement, no new accepted particle or matter claim.

Full local executable package \`UD_K4_CROSS_COMPLEX_ADMISSION_v1.7.zip\` contains complete exact source \`cross_complex_audit_v17.py\`, independent exhaustive \`mask_current_v17.py\`, \`test_cross_complex_v17.py\`, source report, exact JSON, local 11/11 PASS log and SHA-256 manifest. Archive SHA256 \`1f4c8afb5fba580b3e5edf719deb61d772c8593f2fb07a19a21247ed3d5d7ae0\`. Repository replay can be mathematically equivalent but may not be byte-identical; non-constructor scientific review NOT_RUN. Repo CI is only structural integrity.

**Next gate:** resolve Q171's signed-current direction under frozen oriented bases, then investigate a source-selected cross-complex admission predicate and its Q165/Q170 interface receipt. Without a trigger, stop the claim that native recursion itself supplies a physical minimum resolution.
