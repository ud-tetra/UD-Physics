# K4 13/8 prime-factor and clock audit — Discovery handoff v1.3

**Date:** 2026-11-05. **Status:** EXACT / CONDITIONAL / NO-GO scoped / PHYSICAL PROMOTION 0.

Existing task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`, HELD claim ref `refs/heads/claims/klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Isolated branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, draft PR #301. Original main base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`; current main observed `51bd7252473ecbbe3c4f5cb83011e45b5eeace09`. Rebase before any integration. No mainline, accepted ledger or site edit, no physical claim promotion.

## Authoritative source definitions

Frozen ledger v0.39 P01–P06 defines Theta=(F2)^3 (8 finite opposite-edge parity labels), S4 (24 symmetries), local capacity N1=24×8=192. QPB1 local generators v1.0 §§1–3 defines native real K4 C15 signed incidence, unit metric, A=d-d^T and J=A/2 with J^3=-J; formal native u is dimensionless. Native eight projectors v1.1 (same task) proves first-refinement R01^T R01=I15-Q111 and rank13, unweighted label mean13/8. QPB1 native events EVENT_CONTRACT.md v1.0 explicitly says observer thresholds are added and a native physical clock is not established. Sector-label correspondence is still candidate.

## New exact v1.3 results

1. Prime factors: 13 prime; 8=2^3; 24=2^3·3; 192=2^6·3; 312=2^3·3·13, gcd(312,192)=24. Native numerator rank13=15−2=1+3·4. Under *chosen* averaging over 24 S4 frames and 8 Theta labels, trace total24×13=312, mean312/192=13/8=1+5/8=(1.101)_2. This is a typed count/trace average, NOT probability, length or time.
2. Hypothetical numerical modular clock rules vary by operation. Add13 mod8 gives 8-cycle (0,5,2,7,4,1,6,3,0). Add13 mod24 gives 24-cycle; add13 mod192 gives 192-cycle; add312 mod192 gives 8-cycle; multiply13 mod8 gives order2 and mod192 order16. 13/8 is NOT a modulo192 residue from modular division because 8 has no inverse mod192.
3. Native 15D exact phase: chosen observer step Δu=π/4 yields U=Q000+J, U²=2Q000−I15, U⁴=I15. Six intermediate native Q projectors swap in three pairs (100↔011,010↔101,001↔110) with period2; harmonic and top-plane projectors fixed. Active real amplitude full return period4 steps. First leakage Gram commutes with A, making mean13/8 static, not itself a clock phase.
4. Source Θ additive group is (Z2)^3 with exponent2, not cyclic Z8. Assuming a natural *new* group law S4×Theta on the 192 labels, all 192 elements have maximal possible order6; no generator order8 or192. A declared diagonal S4 covariance plus Q-strobe partitions 192 address labels into orbits 24,24,48,48,48. These are mathematical symmetry orbits, not physical trajectories.
5. Strong no-go: exhaustively classify **all deterministic S4-equivariant Theta-only** maps T:Theta→Theta. The four Hamming orbit stabilizers allow 2×4×4×2=64 maps; exactly four are bijections, and every bijection has maximum cycle length2. General proof: fixed singleton labels 000 and111 must map within their two-element set, preventing a single 8-state orbit. This no-go does NOT apply if a larger packet state, memory, changed symmetry or a new event gate is admitted.
6. A hypothetical rational rotation number13/8 gives 8-step return only upon choosing its phase increment; realizing that native at angular speed2 requires a new interval Δu=13π/8, with intermediate superpositions rather than eight discrete orthogonal Q label visits. No SI time, Planck time/length or minimum physical floor is derived from prime factors.

## Reproducibility

- Experiment report: `experiments/klein-tetra-face-flip-20261103/PRIME_CLOCK_13_OVER_8_v1.3.md`.
- Repository exact replay: `experiments/klein-tetra-face-flip-20261103/prime_clock_v13.py`.
- Machine result: `experiments/klein-tetra-face-flip-20261103/prime_clock_results_v13.json`.
- Typed mathematical receipt: `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_prime_clock_v1.3.json`.
- Full standalone locally executed `UD_13_8_PRIME_CLOCK_AUDIT_v1.3.zip` (SHA256 `fc0b1c5cc754b39757ea8fe51044829f95a0f14ca88b4e8b981e531cac105eb2`) contains detailed report, native clock matrix source, independent exhaustive S4-equivariant-map algorithm, two JSON outputs, ten passing regression tests and a verified SHA-256 file manifest. GitHub source equivalence is not byte identity with local source. External non-constructor mathematical review NOT_RUN. GitHub CI validates repository structure, not physics.

## Decision and next discriminant

**EXACT** source-normalized 13/8 arithmetic/counting average and native paired-sector clock. **NO-GO scoped** eight-state full S4-equivariant deterministic Theta-only successor. **OPEN** a source-selected packet-coupled, state-dependent transition and admissible event sequence yielding a real finite physical clock; unit calibration and physical length floor remain absent.

Priority next: test minimal additional state/memory needed for a nontrivial parity cycle under full S4 symmetry, derive its update from source action/admission and check independent event and conserved-current receipts. Do not convert modular return periods into Planck time or length without an independent physical unit bridge.
