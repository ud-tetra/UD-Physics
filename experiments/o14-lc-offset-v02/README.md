# O14 LC offset dimension follow-up

Physical Promotion = 0. Version 0.2 follows the [review of PR #465](https://github.com/ud-tetra/UD-Physics/pull/465#pullrequestreview-6027627546). The [v0.1 schema](../o14-lc-bundle/LC_CALIBRATION_BUNDLE_SCHEMA_v0.1.json) remains available for existing bundles.

| offset_space | Equation | Offset entries |
| --- | --- | --- |
| channel | z = M(y − b) | N, where N is the number of ordered input IDs |
| modal | z = My − b | Exactly 14 |

Both use a 14-by-N readout matrix and allow N greater than 14. Draft 2020-12 checks the equation and offset-space pairing and the fixed modal length. The companion checker validates the variable-length constraints and requires finite native-basis entries with ‖UᵀU − I₁₄‖_F < 10⁻¹². See the [exact reference basis](../o14-lc-bundle/K4_NATIVE_BASIS_U_REFERENCE_v0.1.json) for the replay convention.

`python3 experiments/o14-lc-offset-v02/validate_offsets.py BUNDLE.json`

To migrate a v0.1 bundle that already follows its channel-space equation, set schema_version to "0.2" and calibration.offset_space to "channel", then run the checker. A modal offset changes the equation and requires the corresponding calibrated values. Covariance, numerical rank, hardware calibration and the other semantic checks retain their existing evidence requirements.
