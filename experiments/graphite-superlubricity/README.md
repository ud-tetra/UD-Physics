# Graphite at complementary commensurate angles

**Status: HYPOTHESIS / EXACT lattice geometry / CONDITIONAL port / NUMERICAL same-source material replay / OPEN kinetic residual.** This is Discovery development, with no mainline registry entry or physical promotion.

## Read this first

- [Two-page working preprint (PDF)](GRAPHITE_UD_HYPOTHESIS_PREPRINT_v1.pdf), [TeX source](GRAPHITE_UD_HYPOTHESIS_PREPRINT_v1.tex), and [claim/data gate](MANUSCRIPT_CLAIM_AND_DATA_GATE.md).
- [Long technical working paper v9](../../artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures/2026-10-23T041457Z-codex-graphite-probe-identifiability-61717e00-44d3-4e29-8c40-64bc81f702e4/UD_GRAPHITE_SHORT_PAPER_DRAFT_v9.md) has the wider derivation and references. Its duplicated equation tag (7b) and old relative figure link are known editorial defects; the standalone preprint corrects them. The long paper remains an immutable development draft.
- [Complete selected graphite development archive](../../artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/manifest.json) retains all 37 graphite captures and seven preceding octahedral geometry/model tests, including superseded drafts, failed alternatives, verifier scripts, numerical outputs, original manifests and event receipts. [Machine-readable index](HISTORY_INDEX.json).
- [Candidate](../../candidates/graphite-superlubricity/candidate.json), [mathematical receipt](../../candidates/graphite-superlubricity/mathematical_receipt.json), and [session handoff](../../sessions/graphpub-20261023-gpt6-4f9a/journal.md).
- [Passive-port attribution follow-up](../graphite-port-attribution/README.md): exact conditional proof that the seven-orbit source plus an unrestricted passive bath permits every passive two-dimensional residual tensor. Independent source and loss calibration is necessary for a quantitative force/load prediction. This follow-up limits the interpretation of the versioned preprint; it is not new friction data.

## Claim at its actual scope

For a triangular Bravais basis at 60°, the conventional (2,1) directions have squared length (7a^2) and mutual dot product (13a^2/2). Thus their acute angle is exactly \(\arccos(13/14)=21.7867893\ldots^\circ\); the sixfold complementary orientation is \(60^\circ-\theta=38.2132107\ldots^\circ\). The paired angles are ordinary lattice/moiré geometry, not a novel UD angular prediction.

The seven-cell honeycomb quotient has 14 vertices, 21 bonds and seven faces, with \(b_1=2\). An explicit harmonic 1-cochain map can carry two lateral displacement coordinates. A proposed source map \(S(w)=M^T W B_1^T\) vanishes for uniform edge weights. This is an exact selection rule inside the declared finite model; the real material weights and their coupling to graphite are unknown.

Passive internal-mode loss would contribute \(\Gamma_{\rm add}=CK^{-1}D_hK^{-1}C^T\) under the stated linear-response assumptions. Neither \(C,K,D_h\), the contact transfer, nor a signed residual force and load slope at both angles has been established independently. The published DFT line profiles constrain a conventional first-shell static model, but leave the two-dimensional saddle and kinetic friction unresolved. The illustrative static strength ratio across two separations is **2.104**, not an observed friction ratio.

The proposed discriminant is to freeze an independently checked two-dimensional conventional PES and contact model; independently determine a restricted source pattern and loss response; then forecast the *signed* paired-angle force residual and its pressure derivative before reading held-out force traces. Mirror symmetry alone is a conventional control. A null or failed signed result would reject or narrow this bridge.

## Provenance and replay

The source archive is an intentionally selected byte-for-byte import from local `ud-tetra/UD` commit `f5cb15c454e17e4b26519475d625745c7014f779` (the final preprint commit was local when imported); the preceding graphite development base is `404462b1bf93f08c61c473dd57d3a6b8f84746dc`. Original capture manifests retain their source revisions and primary-source identifiers. The imported files themselves are in this repository, so the local-only final source commit is not needed to read or verify them.

```bash
python3 experiments/graphite-superlubricity/verify_history.py artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The first check verifies both original capture payload hashes and Discovery import hashes. It does not rerun Quantum ESPRESSO or certify the physics. The archived QE source data were externally published by their authors; the six-archive geometry audit and proposed five off-line probes are documented in the long paper and captures. No new off-line QE calculations or experimental force-load dataset were produced here.

Primary material references: [Chen *et al.*, PRL 137, 166201 (2026)](https://doi.org/10.1103/ly48-b4l2); [Lebedeva *et al.*, arXiv:2511.01338](https://arxiv.org/abs/2511.01338); [associated DFT archive](https://doi.org/10.5281/zenodo.16318186); [Minkin *et al.*, PRB 108, 085411 (2023)](https://doi.org/10.1103/PhysRevB.108.085411). The PRL abstract was accessible, but its force tables and supplement were not available for a numerical residual fit at drafting time.
