# Directional packet identifiability and common-input quotient ratio

**EXACT finite-carrier matrix analysis / CONDITIONAL cross-quotient control; physical friction OPEN.** The [directional packet replay](../graphite-directional-packet/README.md) externally prepares two zero-sum B-neighbor direction coordinates. This note asks what its exact native harmonic readout can constrain when those coordinates are unknown and what survives if a single preparation and clock are imposed across N=7,13,19. The known 21.8°/38.2° pair and weak load trend are exposed targets and are not used in the algebra.

## Source audit: preparation remains supplied

The supplied *UD coefficient provenance ledger v0.39(2)* (SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`) Q166/Q167/Q170 provides support-current and conditional mask identities, not a mapping from a registered graphite displacement or sliding velocity into the two packet amplitudes. The [UD local-source selection note v0.1 at `a78193d`](https://github.com/ud-tetra/UD/blob/a78193d420f3bac957be081aed0525fbc1457825/docs/UD_Local_Source_Selection_v0.1.md) explicitly supplies a localized vertex and incident-edge gate on a 600-cell; its carrier and observable differ from this graphite quotient. It likewise does not provide the graphite directional preparation, physical update clock or material force map.

The attachments named `packet_modulation_layer.md`, `triangular_transport_symbol_alphabet.md`, and `seam_phase_transport.md` in this runtime contain only title lines and “Placeholder content for reconstructed repository snapshot.” Their SHA-256 values are respectively `a3275849a09d9c29cb3f8a369fc7ca113ba3cd7529e7db443529097ccaf088ec`, `0da16aba90969fa5b08fce771f62dd7ee2c99fd0b033fc961241b94754b60606`, and `f1bc7725268362c47938d5487e9463dd42b5bd210230419d1b866ceb390c1b7c`. They cannot substantiate a preparation law. This audit does not claim the titles' full historical documents never existed.

## Pointwise rank and its limit

On the earlier full 0/1/2 unit-metric honeycomb carrier, let `a∈R²` denote the supplied directional packet coefficients in the fixed integer input basis and `p_N(s)=L_N(s)a` the coefficient of the formal packet amplitude in the signed two-coordinate stock-flow readout. All contacts are open; `s` is dimensionless native time. The exact series has

`L_N(s)=s M₁+O(s³),  M₁=[[-12,4],[-12,-12]], det M₁=192`,

`M₁⁻¹=[[-1/16,-1/48],[1/16,-1/16]]`.

Thus `det L_N(s)=192s²+O(s⁴)` and the two-coordinate map is invertible for sufficiently small nonzero `s`. At one quotient and one fixed `s`, if both packet coordinates may be chosen freely, a target signed vector in the *linearized local range* can be matched by `a=L_N(s)⁻¹p`. The leading inverse scales as `1/s`; a fixed large target as `s→0` can require amplitudes outside the small-packet regime. This is a pointwise identifiability limit, not a claim that UD fits every physical force. A packet amplitude bound or an independently measured preparation would constrain the range.

## What a common packet would constrain

Under the **additional and unverified** conditions that the same `a`, native `s`, direction frame and reporting normalization apply to N7, N13 and N19, the amplitudes cancel:

`p₇=L₇L₁₃⁻¹p₁₃`, `p₁₃=L₁₃L₁₉⁻¹p₁₉`.

Exact rational matrix-series inversion of the prior Taylor data gives

`L₇L₁₃⁻¹=I−(s⁸/7560)I+O(s¹⁰)`,

`L₁₃L₁₉⁻¹=I+(73s¹²/194594400)I+O(s¹⁴)`.

These leading ratio corrections are scalar in the fixed input/output coordinate convention, so at those orders every packet direction shares the same native relative change. The exact [replay](replay_identifiability.py) checks the formal inverse convolution through the available `s¹⁷` Taylor data. The ratios are local series at `s=0`; no finite-speed or full-time error bound is asserted. Different quotient clocks, interface preparation strengths, contact areas, material loss or detector maps invalidate a direct comparison. The common-input premise has **not** been established in graphite, and this is **not** a friction ratio or a load prediction.

The [mathematical receipt](../../candidates/graphite-packet-identifiability/mathematical_receipt.json) and [immutable capture](../../artifacts/graphpktid-20261024-01/exact-001/manifest.json) record the exact fractions, source statuses and assumptions. A conventional full two-dimensional PES/contact/loss baseline must still be subtracted before any signed residual is attributed to this candidate. Independent physics review NOT_RUN; physical promotion 0.

## Next discriminant

Independently measure or derive the map from registered sliding displacement, direction and load to the two packet coordinates, including its shared or quotient-specific normalization and physical clock. Fix the material cross-Hessian, complex loss and force estimator on data disjoint from held-out angle/load traces. If that map cannot be fixed, this candidate remains pointwise underidentified regardless of its exact finite-size series.
