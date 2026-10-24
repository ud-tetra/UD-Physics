# Registered directional packet without an edge gate

**EXACT finite-carrier response / CONDITIONAL boundary preparation; physical friction OPEN.** The [endogenous gate audit](../graphite-endogenous-gate/README.md) showed that a C3-symmetric packet cannot spontaneously choose one contact under an equivariant deterministic law. Here a registered in-plane direction is supplied as an asymmetric *initial packet*, while all contacts remain open. This tests a possible preparation channel; the graphite sliding interface has not been shown to prepare it. The observed paired 21.8°/38.2° angles and weak load trend were known but did not choose its coefficients.

## Declared carrier and boundary packet

Use the same N=7,13,19 periodic honeycomb quotient and full 0/1/2 skew generator `ẋ=−B₁y`, `ẏ=B₁ᵀx−B₂z`, `ż=B₂ᵀy`, with unit chain metric and dimensionless native parameter `s`. Define `s_t=(0,m+n,n)` and edges `e(t,r):A_r→B_(r−s_t)`. The original harmonic edge columns have direction patterns `h₁=(1,−1,0)`, `h₂=(1,1,−2)`, each divided by `√N`. The reported readout is `P_N=√N MᵀJ`, `J_e=2 y_e(B₁ᵀx)_e`.

Take `x(0)=e_A0+ε Σ_t d_t e_B(−s_t)`, `y(0)=z(0)=0`. The two *integer input coordinate patterns* are `d^(1)=(2,−1,−1)` and `d^(2)=(0,1,−1)`; each sums to zero, and both rotate as a planar C3 direction pair. `ε` is a formal small native amplitude, not sliding speed, displacement or a measured material strain. This is a **specified asymmetric preparation**, not a Q167 gate law or a native source derived from graphite.

Let `L_N(s)` be the 2×2 coefficient linear in `ε`, mapping the two input coordinates to the reported harmonic coordinates. Directly from `y'(0)=B₁ᵀx(0)`, its first Taylor term is the same for all N:

`L_N(s)=s [[−12,4],[−12,−12]]+O(s³)`.

The full integer derivative recurrence and rational product convolution give:

| Term | N=7, 13, 19 common matrix coefficient |
| --- | --- |
| `s¹` | `[[-12, 4], [-12, -12]]` |
| `s³` | `[[24, -8], [24, 24]]` |
| `s⁵` | `[[-73/5, 73/15], [-73/5, -73/5]]` |
| `s⁷` | `[[156/35, -52/35], [156/35, 156/35]]` |

The first quotient contrasts in this exact supplied preparation are

`L₇−L₁₃=s⁹ [[1/630,−1/1890],[1/630,1/630]]+O(s¹¹)`,

`L₁₃−L₁₉=s¹³ [[−73/16216200,73/48648600],[−73/16216200,−73/16216200]]+O(s¹⁵)`.

All three quotients therefore activate at first order; the carrier does not select seven by merely admitting a direction. The lower-order equality and late finite-size differences are **native stock-flow** features of this specified packet. They are not a positive drag ranking: the matrix has signed components and no physical time, contact density, energy/length normalization, detector map or bath loss. Rotating the packet rotates the full-chain trajectory and readout consistently; the [replay](replay_packet.py) checks this on exact derivatives through `s¹⁷`. See the [receipt](../../candidates/graphite-directional-packet/mathematical_receipt.json) and [immutable capture](../../artifacts/graphdirpkt-20261024-01/exact-001/manifest.json).

## Physical bridge needed

The conventional honeycomb/moiré model already accounts for the paired angles. To predict a *remaining* kinetic force or load response, the directional packet's preparation amplitude and orientation must be independently tied to a registered graphite interface, followed by a dimensional material coupling, complex loss/contact dynamics and a signed force estimator. An arbitrary choice of those quantities could mimic a residual. The current result constrains one toy source mechanism and supplies no independent seven-cell friction forecast. Independent physics review NOT_RUN; physical promotion 0.
