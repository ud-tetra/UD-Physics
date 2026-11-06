# Native K4 eight-projector and 13/8 leakage handoff v1.1

**STATUS:** EXACT/CONDITIONAL source-constructible native projectors; CANDIDATE parity-label interpretation; NO-GO fixed equal-sector/Planck promotion. Physical promotion 0.

**Task and ownership:** klein-tetra-face-flip-20261103, session ktff-20261103-01, HELD claim SHA 667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4 at refs/heads/claims/klein-tetra-face-flip-20261103. Existing isolated Discovery branch discovery/klein-tetra-face-flip-20261103/ktff-20261103-01, PR #301 draft and unmerged. Original task base 0eef9a3f77198810b35bee8d3ef578ebc3af403a; current main examined 698d6d66147131d43e364a1736ca07ad0f3fa9d4. No mainline export, claim release or state/CURRENT update.

## Source provenance and version correction

Frozen ledger v0.39 P01–P06 gives the eight opposite-edge parity labels Theta=F2³. Source QPB1 local generators v1.0 §§1–3 gives filled K4 C15, H=I, A=d−dᵀ, J=A/2 and signed S4. Prior K4 multilevel v0.9 gives residual R01 squared norm 13, R12 52 and R02 151/4. Prior 13/8 audit v1.0 only provided eight projectors after adding an auxiliary real eight-fiber. The **new v1.1 theorem improves that result:** source-constructed eight orthogonal projectors exist on the original C15 itself. Earlier negative conclusions about S4 not forcing equal weights, normalization invariance and Planck-length identification remain correct. This is a versioned amendment, not a silent replacement.

## Native projector construction

Let h be the normalized constant K4 vertex chain, v its oriented top-cell vector, E_A/E_B/E_C the native 2-column embeddings for opposite edge pairs (01,23), (02,13), (03,12). Set Q000=hhᵀ, Q111=vvᵀ+(Jv)(Jv)ᵀ; assign weight1 Q from E_p E_pᵀ, complementary weight2 Q from J E_p E_pᵀ Jᵀ. Exact native C15 matrix checks show ranks 1,2,2,2,2,2,2,2; QthetaQphi=delta Qtheta; sum Q=I15; signed S4 covariance across all 24 permutations.

These operators require **no extra Hilbert carrier**. However assigning them to *parity polarity states* is a candidate correspondence; the ledger does not postulate that spectral readout or a constitutive transition rule.

## Exact first-level leakage theorem

With source integral F01:C15→C29, induced G=diag(1^14,4), fine A1=d1−d1ᵀ and R01=A1F01−F01 G⁻¹ F01ᵀ A1F01, exact full matrices prove:

**R01ᵀ R01=I15−Q111.**

Thus R01 is an isometry on the 13-dimensional complement to the 2D top/Jtop plane and annihilates that plane. All Qtheta commute with the first leakage Gram; parent native A commutes with it too. The exact per-label squared leakage is [000:1, each of six intermediate labels:2, 111:0], so total13 and arithmetic mean13/8. Not every label has equal leakage and their ranks differ. Native source dynamics rotates each 4D paired E_p⊕J E_p subspace, exchanging the weight1/weight2 projectors; individual middle labels are not dynamically invariant.

## Next-level obstruction

For R12:C29→C85, source-normalized inherited projectors T Qtheta Tᵀ, T=F01G01⁻¹/², resolve only a 15D image of C29. Inherited leakage contributions [000:3; weight1 each4; weight2 each15/4; 111:3/4] sum27; new 14D complement contributes25, total52. There is no source-selected extension of the original eight Q to a full orthogonal resolution on all 29 refined dimensions.

For direct R02:C15→C85 the original projectors yield [000:4; weight1 each6; weight2 each5; 111:3/4], total151/4, label mean151/32. The composite Gram fails to commute with native A (commutator rank14) and three weight2 Q (each rank4). Unit-rate gain scaling or measurement metric scaling changes the mean, and neither case creates a Planck-length physical bridge.

## Reproducibility

- Proof: experiments/klein-tetra-face-flip-20261103/NATIVE_EIGHT_PROJECTOR_LEAKAGE_v1.1.md.
- Executable: experiments/klein-tetra-face-flip-20261103/NATIVE_EIGHT_PROJECTORS_v1.1.py.
- Tests: experiments/klein-tetra-face-flip-20261103/test_native_eight_projectors_v11.py, comparing against the prior independent-form K4 v0.9 matrix generator in the same repository directory.
- Exact summary: experiments/klein-tetra-face-flip-20261103/native_eight_projectors_results_v11.json.
- Typed receipt: candidates/klein-tetra-face-flip-20261103/mathematical_receipt_native_eight_v1.1.json.

Complete locally generated ZIP: K4_NATIVE_EIGHT_PROJECTOR_13_OVER_8_v1.1.zip. Its SHA-256 is aa07b52dd79196a43732d0c2359a2ac1bbf253c4dbe8cb5981e8852d9673d00a; sparse exact matrix-certificate SHA-256 is 65d3d152c1f4b11b284d0d3c2057628c9f06458b1272ee0657ff5c82e7bbb630. Includes local exact source and prior v0.9 independent-form replay (adapted output path), 8/8 passing unit tests, matrix certificate, JSON results and SHA-256 manifest. Local source not claimed byte-identical to GitHub script. This is constructor mathematical verification, not external non-constructor review. GitHub repository-integrity CI must be checked on final head.

## Acceptance and next discriminant

Scoped EXACT proofs now pass: eight native projector orthogonality and S4 covariance, first-leakage Gram rank13 partial isometry and formal native dynamics exchange. The chosen Theta-label assignment, true finite parity evolution/admissibility, 29D refined complete projector law, physical length/clock and measured Planck link remain OPEN_GATED. Do not promote a first-level label average into a universal physical constant. Next highest-value step: derive a source-implied parity-to-K4 operator identification and functorial refined-carrier sectors, then test independently registered physical bridge if available. Stop a physically promoted 13/8 claim until that gate passes.
