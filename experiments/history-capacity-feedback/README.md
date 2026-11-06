# Finite recorder feedback and energy gate v0.1

2026-11-06. Discovery session `history-capacity-feedback-20261106-01`; base `ud-tetra/UD-Physics@7ef45805563b47cbe1e2f34bb9e6e97ce5f5c962`; claim `33189ef40b017bbd298d78a1779a868c2039eae1`. Physical promotion 0; no target data; independent physics review NOT_RUN.

## Source-bound question

Can the existing native cell oscillator, resolved-root adapter and finite recorder themselves select a root-triggered token pulse and stop the real flow at capacity? Sources: `ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD native crossing-to-receipt audit v0.1.md` §§1–3, 7; `Docs/UD capacity mechanisms and native crossing bridge audit.md` §§2–6; `Docs/UD crossing completion and finite capacity deadlock audit.md` §§2–4; `docs/UD_CARRIER_WRITE_DISTINGUISHABILITY_AND_ENERGY_v0.1_RELEASE.zip` §§1, 3 (SHA-256 `5bb7d306ef539d30e3e0ce1dc7c85e6182a39404e0bb774430fed08b4665eda8`); and Discovery [two-event controller](../history-twoevent-controller/README.md). The manuscript's SA-TIME-018 Fire/Ack gate acts on discrete logical events; the source audit explicitly says it does not feed back on real amplitudes. The published face-label pulse is externally prescribed, with declared work and blank preparation.

## Exact conditional capacity obstruction

Under the source's no-backreaction branch, the real oscillator keeps crossing while recording can stall. The v0.1 crossing-to-receipt audit §7 gives `Q >= N-1` after N resolved roots during one publication stall; every finite queue K is exceeded for sufficiently large N. For the two-slot controller, acknowledgment removes pending credit but preserves the retained token words. It therefore cannot free a slot without export or erasure. A third root is not losslessly admissible under continued independent flow. This is a scoped result for continuing roots and bounded internal storage, not a universal no-go for UD extensions.

## Minimal feedback candidate and its price

Declare a **new** global gate, not a recovered UD law. On the real two-coordinate cell/face plane, let `x=(u,f)` and `B=[[0,-2],[2,0]]`, with dimensionless evolution `dx/ds=g(N) Bx`. `N` is the number of occupied retained token slots, `g(N)=1` for `N<2`, `g(N)=0` for `N=2`. A resolved root with available blank slot triggers the separate assumed token pulse and increments N only after the completed event is written. This ordering avoids freezing a provisional zero before completion, the deadlock in the cited audit. The initial state and boundary are the source oscillator plane; no physical time or spatial metric is assigned. The source's unit Euclidean carrier metric is used; the output is the occupied token list.

**EXACT/CONDITIONAL:** `B^T=-B`, so `d(x^T x)/ds=2g x^T Bx=0`, even across a gate switch when x is continuous. `B^2=-4I`; the open generator has characteristic polynomial `lambda^2+4`, while the full generator is zero with polynomial `lambda^2`. Thus this lossless two-slot stop changes the native propagation spectrum and freezes all coordinates of this plane. Acknowledgment alone leaves N=2; this model remains halted after both acknowledgments. It does not derive a pulse, detector, geometry, or a usable indefinitely evolving world.

If the declared physical Hamiltonian is `H_g=i epsilon g B` on the complexified carrier, an instantaneous switch from `g=1` to `g=0` changes its expectation by `Delta E=-Tr(i epsilon B rho)` for a fixed state rho. That is an external control/work term under this embedding. For real-coordinate pure states the expectation is zero, but that special value does not supply a physical energy law or pay for token writing, blank preparation, pulse drive or later erasure. The source's face-label pulse work formula applies to a different memory and cannot be copied onto this token pulse. Energy conservation of the enlarged carrier-controller-memory system is **OPEN**.

`check.py` verifies the exact matrix square, skewness, 98 integer-state norm derivatives, the open/full characteristic polynomials, and the fact that Ack does not free storage. These are checks of the declared toy gate. The symbolic identities above establish their all-state scope.

## Decision

**NO-GO under sourced no-backreaction, finite-capacity, indefinitely continuing-root hypotheses:** lossless internal retention of every root fails. **CANDIDATE:** global scalar stop preserves Euclidean norm but changes the spectrum and permanently halts this plane at capacity. No source selects this feedback or the root-triggered token pulse. The native coupling and joint energy account remain **OPEN**; physical promotion 0. Reopening requires a source-specified detector/control interaction, capacity admission or export law, and full joint conserved quantities, followed by spectrum/locality checks.
