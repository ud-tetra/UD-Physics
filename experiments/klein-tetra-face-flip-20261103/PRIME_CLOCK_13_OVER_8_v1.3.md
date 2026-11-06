# Prime factorization and clock analysis of native K4 13/8 — v1.3

**2026-11-05 | UD-Physics Discovery | EXACT / CONDITIONAL / NO-GO SCOPED / PHYSICAL PROMOTION 0.**

**Ownership:** existing HELD claim `refs/heads/claims/klein-tetra-face-flip-20261103` at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`, session `ktff-20261103-01`, isolated draft PR #301. Base source `0eef9a3f77198810b35bee8d3ef578ebc3af403a`, current main checked `51bd7252473ecbbe3c4f5cb83011e45b5eeace09`. No shared state/mainline edits or physical promotion.

## Source and typed objects

- Frozen `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md`, P01–P06: K4 has four vertices, six edges, three opposite-edge pairs, finite Theta=F2^3 (eight **labels**), S4 order24 and local capacity N1=24×8=192. This is not a cyclic time-clock specification.
- `experiments/qpb1-local-generators/README.md` v1.0 §§1–3: native real filled-K4 chain C15 and unit coefficient metric; signed A=d−d^T, J=A/2, J³=−J, frequency2 per **formal dimensionless u**.
- `experiments/klein-tetra-face-flip-20261103/NATIVE_EIGHT_PROJECTOR_LEAKAGE_v1.1.md`: eight *candidate parity-labelled* native projectors, first-refinement R01^T R01=I15−Q111, rank13, scores1+6×2+0, unweighted arithmetic mean13/8; their label assignment is **CANDIDATE** and their statistic is not measured length/time.

## Exact prime and capacity arithmetic

```
13=13 prime, 8=2^3, gcd(13,8)=1
24=2^3·3, 192=2^6·3=24·8
13 = 15−2 = 1 + 3·4 native first-refinement leaking modes
312=24·13=2^3·3·13; gcd(312,192)=24
312/192=13/8=1+5/8=(1.101)_2
```

**EXACT/CONDITIONAL:** If the native trace13 is repeated over all 24 orientation frames (S4 covariance), averaging trace sum312 over the 192 selected frame-parity labels yields13/8 with common factor24 canceled. This is an S4-compatible **counting average**; no stochastic probability, successor, action-unit or time is defined. 13/8>1, so it is not a normalized per-label probability.

## Distinguish four different modular clocks

| Arbitrarily declared operation | Modulus | Exact return period |
|---|---|---:|
| Add 13 in cyclic Z8 | 8 | 8 |
| Add 13 in cyclic Z24 | 24 | 24 |
| Add 13 in cyclic Z192 | 192 | 192 |
| Add 312≡120 in cyclic Z192 | 192 | 8 |
| Multiply by 13 among units mod8 (starting at 1) | 8 | 2 |
| Multiply by 13 among units mod192 (starting at 1) | 192 | 16 |

Additive mod8 orbit is `0,5,2,7,4,1,6,3,0`. Exact multiplicative residues satisfy 13^8≡97 (mod192), 13^16≡1. **13/8 is not an element of Z192 obtained by division**, since 8 is noninvertible mod192; multiplying the rational mean by 192 gives the integer312 but does not supply an update.

A chosen circular phase increment 2π·(13/8) per tick has eight-event return (fractional rotation5/8). Matching native angular rate2 requires choosing native strobe separation Δu=13π/8, a *new convention*. Intermediate states are generally continuous superpositions of paired sectors, not eight orthogonal parity labels visited in sequence. No physical time calibration.

## Native signed-incidence clock

With Q000 the normalized constant-vertex harmonic projector, the exact full K4 native flow is
```
U(u)=exp(uA)=Q000+cos(2u)(I−Q000)+sin(2u)J.
```
At the **chosen observer** strobe τ=π/4: U(τ)=Q000+J; U(τ)^2=2Q000−I15; U(τ)^4=I15. The six middle projectors form three 2-cycles under conjugation `100↔011,010↔101,001↔110`, while Q000 and Q111 are invariant as subspaces. Active amplitudes require four such steps to return, projectors only two. The first-leakage Gram I−Q111 commutes with A; its trace13 and per-label average13/8 are stationary, not a clock phase.

## Exhaustive equivariant Theta-only no-go

The induced S4 action on Θ is full S3 coordinate permutation; Hamming-weight orbits have sizes 1,3,3,1. For every deterministic T:Θ→Θ satisfying T(gθ)=gT(θ), mapping a representative from each orbit to a stabilizer-fixed target gives admissible choices 2,4,4,2: **exactly 64 equivariant functions**. Only **four** are bijections; all have maximal cycle length2. In general 000 and111 are the only S4-fixed labels, so T must preserve their two-element subset, precluding one eight-state traversal.

**NO-GO (scoped):** no deterministic full-S4-equivariant update on Θ **alone** is an eight-cycle. An added clock memory, coupled orientation packet state, source-selected non-equivariant gate or explicit state-dependent successor changes the premise.

If one additionally declares the 192 address set as direct-product **group** S4×F2^3, it has 192 elements but maximal order of a group element **six**, not eight or192 (S4 element orders1/2/3/4, parity translations order1/2). The previously defined **diagonal S4 frame relabeling plus native Q-projector strobe** acts on that 192-label set with orbits of sizes 24,24,48,48,48. These are symmetry orbits, not natural-time trajectories. An arbitrary cyclic enumeration Z192 would be a distinct added group law.

## Decision and limits

**EXACT:** prime and gcd identities; possible 8-step arithmetic **given** a Z8 successor; native strobe projector 2-cycles and amplitude4-step recurrence; exhaustive 64 equivariant maps, four bijections and no eight-cycle.
**OPEN:** native update constituting a full parity tick, causal event-order rule, full 192-state path law, physical clock/metric and SI length calibration. The finite capacity192 does not itself imply a minimum physical distance or time; recursively subdivided tetrahedra remain admissible in the current mathematics.
**PHYSICAL PROMOTION=0.** Do not promote modular periods to Planck units or an observed minimum scale.

## Verification

Locally executed `UD_13_8_PRIME_CLOCK_AUDIT_v1.3.zip` contains self-contained SymPy exact `clock_audit_v13.py`, an independently expressed `equivariant_theta_maps_v13.py`, ten passing unit tests, detailed report, exact JSON receipts and SHA-256 manifest. ZIP SHA-256 `fc0b1c5cc754b39757ea8fe51044829f95a0f14ca88b4e8b981e531cac105eb2`. Exact local constructor tests PASS; non-constructor scientific review NOT_RUN. GitHub repository integrity CI must be tied to final head.
