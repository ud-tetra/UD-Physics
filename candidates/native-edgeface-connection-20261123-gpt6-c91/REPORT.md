# Conditional intercarrier edge/face coupling — v0.1

**2026-11-23 | Development, no registry promotion | Physical Promotion = 0.**
**Task claim:** `claims/native-edgeface-connection-20261123-gpt6-c91` at `daaea96c4a0113303f65c66c2b47c325784613d8`.
**Base:** `ea93a86305925aced4ad9aa43b8bc7979f5b0f15`. No shared state or mainline amendments.

## Source and typed assumptions
- UD PR #611 at `ed7e860a0912d9480a19707be42771f155d0dee0` §§2–5: octahedral fan/graded transfer are prescribed, not source-selected.
- UD PR #613 at `90154eb0bd3088f0c72c3eb61e63ea56ca701ce9` §§2–5: relative geometry not determined by fixed native tuple; no sourced metric/event.
- UD-Physics `AW5_STRUCTURAL_EXCLUSIVITY_AND_GAP4_DRAFT.md` §2 (blob `5c088ce09f6aaf02217c3dc84af808e38bff7da1`): the compact edge connection and Wilson loops are conditional.
- `HISTORY_CONTRACT.md` v1.0 (blob `4d2c39554b73f27883a49801aa32002aecb2a2c0`): edge-sign transport is not identified with the native Hodge loop.
- `THREED_KLEIN_PACKET_SEAM_v0.4.md` §§3,7–8 (blob `72eb7a2b6a600512117459ba762b1690671bd4bd`): a directed seam admits inequivalent full K4 extensions.
- `seam_phase_transport.md` §§1–5 (blob `667ce62892e2b5a8a523a740f38673bb527ce800`): candidate U_ij with unsourced coefficients.
- UD coefficient ledger v0.85, blob `93e2ca31eba625989087275a71c4857848e321c6`, Q165/Q169/Q177–Q179/Q200–Q210: support/ownership defined, not native intercarrier event.

Let `x_A,x_B ∈ R^15` be graded chain coordinates on independent oriented K4 simplices with unit coefficient metric, increasing simplex orientation, and signed S4 relabelings `R(g)`. `P1,P2` denote orthogonal edge/face projectors. Formal parameter `s` is not a physical clock.

## Constructed model — not source-derived
Define `e_i=P1 x_i`, `f_i=P2 x_i`,
`K_AB=e_A f_B^T+f_A e_B^T`,
`rho=||x_A||²-||x_B||²` and
`J(x)=rho [[0,K_AB],[-K_AB^T,0]]`.

The candidate nonlinear flow is `x' = (A_old + J(x))x`, with `A_old=diag(A_K,A_K)`, `A_K=∂^T−∂`. For every x, J is skew; hence `d||x||²/ds=x^T[(A_old+J)^T+(A_old+J)]x=0`. Because grade projectors commute with signed S4 actions, `K_AB -> R(g_A) K_AB R(g_B)^T`. The stock difference rho is separately invariant under S4, and odd under swapping A/B; combined J is covariant under carrier swap. At equal source stock rho=0 and the coupling vanishes. The choice of rho and its unit normalization is **an authored ansatz**, not source-native.

## Exact verification
The attached standalone verifier `verify.py` constructs signed S4 simplex permutations and checks boundary nilpotency, all 576 independent gauge relabelings, source-unit skew, carrier swap, nonzero edge/face response and 96 matching orbit. Constructor result:
- `rank(J)=4` and `rho=-4` for the declared nontrivial integer fixture.
- `K_AB` has 23 nonzero entries.
- 576/576 gauge-pair tests pass, unit-support derivative 0, carrier-swap covariance passes.
- 96 matchings remain in one gauge orbit: **no unique matching selected**.

## Constitutive disposition
**EXACT/CONDITIONAL:** finite-dimensional equivariant, exchange-covariant, stock-preserving edge/face amplitude coupling exists as constructed.
**NO-GO_SCOPED:** equal-stock indistinguishable carriers remain uncoupled under this particular ansatz; no face matching is produced.
**OPEN:** source-selected interaction, pre-contact graph incidence, independently produced two paths, target-domain event, lineage receipt and dynamics on the true 117D fan.
**Physical Promotion = 0**. Do not reinterpret this amplitude-space cross-map as an existing simplicial edge or as measured physical interaction.
