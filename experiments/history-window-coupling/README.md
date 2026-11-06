# Bounded continuous crossing-window pointer v0.1

2026-11-06. Discovery session `history-window-coupling-20261106-01`; base `ud-tetra/UD-Physics@322ea849bfb949e4136a898e05d9d7fa0ec7604f`; held claim `5b4099ab90f2fbbd02af277f1ebbba33ec83bfc3`. CANDIDATE, physical promotion 0, no measurement target, independent review NOT_RUN.

## Sources and typed scope

`ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD native crossing-to-receipt audit v0.1.md` §§1–3,7, supplies a conditional real-cell root detector and separate receipt protocol. `Docs/UD finite admission and wave-feedback discriminator v0.1.md` §§1,3–5, compares admit/reject and wave pauses without selecting a native coupling. `docs/UD_CARRIER_WRITE_DISTINGUISHABILITY_AND_ENERGY_v0.1_RELEASE.zip` §§1–4, SHA-256 `5bb7d306ef539d30e3e0ce1dc7c85e6182a39404e0bb774430fed08b4665eda8`, supplies a different externally pulsed face-label memory. Discovery [fixed-map obstruction](../history-root-write-continuity/README.md) rules out an instantaneous fixed linear exact-root-only write under its hypotheses. No source selects the coupling below.

Let the real native cell coordinate `u(s)` have derivative `g(s)=du/ds` under a declared source orbit, with dimensionless evolution parameter `s`. Treat that orbit as an external path for a two-state pointer `M=C²` initially `|0>`. This is a one-way open-system candidate, not a joint native carrier-memory generator. Choose a dimensionless window half-width `a>0`; the unit-metric real carrier, cell orientation, and the pointer's computational basis are declared. No physical time, length, energy, or sampling calibration is used.

Set `phi_a(u)=3(1-u²/a²)/(4a)` for `|u|<a`, and zero outside, with primitive `F_a(-a)=0`, `F_a(a)=1`. Inside the window `F_a(u)=1/2+3u/(4a)-u³/(4a³)`; it is 0 below and 1 above. Declare the pointer evolution

`d|psi>/ds = -i (pi/2) g(s) phi_a(u(s)) sigma_y |psi>`.

All interaction generators commute along the imposed path. Hence for any piecewise differentiable path,

`U_M(s1,s0)=exp[-i (pi/2) {F_a(u1)-F_a(u0)} sigma_y]`.

This is exact chain-rule integration. The coefficient `pi/2`, window `a`, speed factor `g`, pointer preparation and path-to-control map are chosen to realize a full flip. Their selection is **FIT/CANDIDATE design**, not a native derivation. The response is an endpoint primitive of an exact one-form `dF_a`; it is neither an event count nor a physical action unit.

## Traversal and false-trigger gates

**EXACT/CONDITIONAL:** A completed traversal `-a -> +a` flips the blank pointer to the orthogonal word with probability 1, independent of speed or intermediate reversals. At the exact root `u=0` after starting at `-a`, `F_a=1/2` and the write probability is `sin²(pi/4)=1/2`, so the word is *not* completed at the root. A path `-a -> b -> -a` for any `b<a`, including a zero touch and return, has net angle 0 and final blank pointer. During the excursion it can have nonzero transient write probability, so an early readout is a false trigger. Initial conditions inside the window also need a declared initialization rule.

A complete native sign crossing with amplitude below `a` need not reach both boundaries and can be missed. A return `-a -> +a -> -a` yields identity on the same slot, erasing that slot's apparent crossing. Two oppositely directed full traversals are two events yet leave its final pointer blank. The joint path and single-slot endpoint are therefore not history injective. Fresh slot selection after each completed traversal needs a history-dependent controller; with two slots a third event still requires export, loss accounting, or backreaction. This model has no source-derived capacity law.

`check.py` verifies the exact rational primitive at the boundaries and root, six named paths, and 625 four-point paths for `a=1`. The endpoint identity is proved by telescoping and the chain rule for the stated full path class, beyond the finite checks.

## Energy and autonomy gate

This equation drives the pointer from an externally supplied `u,g` path. It supplies no reciprocal carrier force and no conserved energy on the combined carrier–pointer space. If one adds a nondegenerate pointer Hamiltonian `H_M=Delta |1><1|` throughout the drive, `[H_M,sigma_y] != 0` for `Delta != 0`, so the commuting-generator full-flip formula no longer follows; a new joint solution and drive work calculation are required. A degenerate pointer permits the exact kinematic rotation but does not derive preparation, switching, retention, or erasure costs. The face-label pulse's mean work formula belongs to a different carrier and memory and cannot be reused here.

**RESULT:** This bounded continuous coupling avoids the previous *instantaneous fixed-map* hypothesis and gives a speed-independent completed traversal response with no final response to a return excursion. It fails exact-at-root completion, early-readout immunity, small-amplitude completeness, repeated-history retention in one slot, finite-capacity continuation, autonomy and joint energy accounting. This specific one-way branch is **PARKED** for a universal recorder. Reopen with a source-selected detector/controller and a joint generator whose energy, latency and capacity contracts are explicit. Physical promotion 0.
