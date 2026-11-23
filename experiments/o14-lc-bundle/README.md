# O14 calibration schema and K-minus redistribution check

Physical Promotion = 0. This follow-up starts from the [PR #464 merge](https://github.com/ud-tetra/UD-Physics/pull/464).

## O14 calibration schema v0.1

The [JSON Schema](LC_CALIBRATION_BUNDLE_SCHEMA_v0.1.json) defines channel, calibration, native-basis and verification records. Its 15-by-14 basis embeds the active modes in the full filled-tetrahedron chain space. SI calibration, covariance validity, cross-record dimensions and numerical rank over the admitted band require the semantic and evidence checks described in the schema. No device data or derived physical scale are included. See the [action-transfer specification](../g05-relay-o14/README.md).

## G05 exact fixed-carrier result

Construct the two tetrahedra 0123 and 0124 with ascending simplex orientations and the Euclidean coefficient metric. For the signed boundary D, let A = D − Dᵀ. Exact eigenvalue multiplicities of −A² are 0 (1), 3 (8), and 5 (14). Under fixed Q169 flow ẋ = Ax, each spectral projector P_j commutes with A, so d‖P_j x‖²/ds = 0. The two frequencies alone supply no exchange. This also constrains any sequence of uninterrupted segments with the same generator and identity state handoffs.

For a prescribed driven control, use one oriented rotation plane per frequency and phase rates √3 and √5. In the canonical modal convention θ = ½ Σ a_j dφ_j, let the two histories take a₁ = S/2 ± ε sin²(πs/T) and a₂ = S − a₁, with 0 < ε < S/2 and identical initial phases. Both histories have the same endpoints and duration with fixed total stock S. The difference of canonical modal integrals is εT(√3 − √5)/2. This calculation uses unit-normalized plane complex structures. The separate form ⟨Ax,dx⟩/4 has frequency-weighted plane coefficients on K-minus, so its difference for these same paths is εT(3 − 5)/4. These two forms coincide on the active single-cell carrier where the frequency is 2.

A prescribed stock-preserving drive can realize the control. For either prescribed path, write w = ẋ − Ax. Then w is orthogonal to x and the added skew operator (wxᵀ − xwᵀ)/S maps x to w. This depends on the prescribed history and supplies no native constitutive selector.

The [conditional Pachner reserve guard](../pachner-trigger-lift/README.md) can be kept strictly off by choosing R > 3S/2: its obligation form G has largest eigenvalue 3/2, so R − xᵀGx remains positive along either control. That certificate covers only the stated reserve guard. A source-admitted C06 all-pass history additionally needs its authoritative receipt evolution and first-entry rules on the driven trajectory. An externally supplied mask cannot certify those rules. Actual Q136 attribution and a native guard-admitted exchange remain OPEN.

## Replay

From the repository root, run `python3 experiments/o14-lc-bundle/audit.py` with SymPy and jsonschema installed. The replay checks the schema metaschema, the exact spectrum and commutation, and the two integral conventions.
