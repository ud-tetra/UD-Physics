# UD-Physics Klein–K4 handoff v0.6 — integral strong deformation retraction

**STATUS:** EXACT / CONDITIONAL integral chain-homotopy equivalence and torsion closure; physical promotion 0. Same HELD claim `refs/heads/claims/klein-tetra-face-flip-20261103` SHA `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, session `ktff-20261103-01`, isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`; draft PR #301. Original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, current main advanced and requires rebase before integration. No mainline export, claim release or site edit.

## Source and exact result

Prior v0.4 assumed Klein×I 3D nonorientable tetrahedral Δ-complex, f=(18,102,156,72), and v0.5 pulled-back integral orientation local coefficient rho with twisted boundary d²=0, Smith H0=Z/2. A complete explicit **integral** chain-homotopy equivalence is now constructed from that twisted 72-Delta complex to minimal Klein×I CW with ranks (2,5,4,1). This supersedes the earlier rational-only comparison in new v0.6 receipts while preserving v0.5 unchanged.

1. Canonical cell-local signed barycentric subdivision from two-triangle prism CW (2,7,7,2) to twisted simplicial Δ (18,102,156,72), with exact boundary commutation.
2. Integral complement to subdivision image has dimensions (16,95,149,70). Exactly 165 unimodular ±1 algebraic Morse cancellations (16,79,70 across degrees1/2/3 respectively) eliminate it entirely; no residual cells. Recover integer P_big and degree+1 H_big, proving dH_big+H_big d=I−S_big P_big and P_big S_big=I.
3. Three further ±1 unit cancellations remove diagonal edge/triangle cells, reducing CW (2,7,7,2) to minimal (2,5,4,1), with a second integer chain contraction and an exact basis permutation W.
4. Compose integer `P=W P_small P_big`, `S=S_big I_small W^{-1}`, `H=H_big+S_big H_small P_big`. **Full exact matrix checks** pass: `PS=I`, `dP=Pd`, `dS=Sd`, `dH+Hd=I−SP`.
5. The previous minimal cellular-to-formal-60D K4 chain map composed with P is also integral and degreewise exact, ranks (2,5,4,1). This composite is **not** claimed to be an equivalence or a native 3D physical dynamical map.

Integral homology is preserved by the strong deformation retraction: `H0=Z/2,H1=Z,H2=Z,H3=0` for the stipulated twisted 72-complex, not merely real Betti numbers. A separately programmed sparse matrix certificate reader reconstructed all 16 integer P/S/H/composite matrices and independently checked these exact relations. Deterministic local regeneration of the 120KB integer JSON was byte-identical.

## Reproducibility and file hashes

- GitHub proof: `experiments/klein-tetra-face-flip-20261103/INTEGRAL_SUBDIVISION_STRONG_RETRACT_v0.6.md`.
- GitHub read-back checker: `experiments/klein-tetra-face-flip-20261103/verify_integral_bridge_v06.py`. This uses the prior repository v0.4/v0.5 source scripts; the full standalone local package also carries a checker matched to its own exact basis.
- Machine-result summary: `experiments/klein-tetra-face-flip-20261103/integral_strong_retract_results_v06.json`.
- Typed provenance: `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_v0.6.json`.
- Full runnable scripts, exact sparse matrix JSON, SHA-256 manifest and logs in user-visible `KLEIN_INTEGRAL_CHAIN_RETRACTION_v0.6.zip`. ZIP SHA256 `de4227b9b92b68d853ee5976b939c2ac7ff528e7add5dfe7a9451e32815aea41`. Exact matrix JSON SHA256 `3f7ffd1a1902da74055a3e6c1f969a8ff7101e60804a175e4a022d4d997b9a32`. Full local scripts and JSON are not claimed to be byte-identical with repository files.
- Local complete integral generator PASS; independent-form matrix readback PASS; no external non-constructor mathematical review.

## Essential limitation and next discriminant

The forward subdivision S is geometrically cell-local, but the **reverse integral P was obtained through algebraic Morse cancellation**. Strict geometric bounded-support locality of P is not established. No physical time, metric-compatible generator intertwining, measured orientation-reference coupling, particle retention or new force emerges from this theorem. Klein seam gluing, the even K4 S4 completion, and physical relevance remain candidate assumptions. **Physical promotion=0.**

Next: characterize support radius of P and check a geometrically local integral inverse if UD locality requires it; then source a native K4 seam rule and an independent framed transport measurement. Do not equate integral chain equivalence with physical equivalence.

## Weak finite-locality diagnostic (not a uniform theorem)

For this one 18-vertex barycentric quotient graph, the nonzero algebraic reverse-map coefficients have minimum source-simplex-to-output-subdivision-support vertex distance at most 1. Exact finite histograms: degrees 0/1/2/3 yield distances {0:2,1:16}, {0:76,1:105}, {0:45,1:5}, {0:1} respectively. The diagnostic takes the minimum among simplex/support vertices, so it does **not** prove that the entire output support is within one graph hop, nor a refinement-uniform physical locality bound. See `experiments/klein-tetra-face-flip-20261103/finite_locality_diagnostic_v06.json`. Strict locality remains OPEN.
