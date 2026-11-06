# Crossing-to-carrier-write source gate v0.1

2026-11-06. Session `history-write-trigger-20261106-01`; Discovery lane, physical promotion 0. Base `ud-tetra/UD-Physics@b04652406b5579ca172564d0e3a6fe3aca75693a`. Claim `d1231cf04ff8a031f88713ee9e74f8ac69a0660f`. No target physical measurement was used. Independent physics review NOT_RUN.

## Question and source boundary

Can a resolved native cell crossing, as described in `ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD native crossing-to-receipt audit v0.1.md` §§1–3, trigger and be identified by the published boundary-memory write in `docs/UD_CARRIER_WRITE_DISTINGUISHABILITY_AND_ENERGY_v0.1_RELEASE.zip` §§1–4 (SHA-256 `5bb7d306ef539d30e3e0ce1dc7c85e6182a39404e0bb774430fed08b4665eda8`)? The intermediate finite recorder is described in `Docs/UD capacity mechanisms and native crossing bridge audit.md` §§1–3, and the correlated history candidate is a dependency of `docs/UD_RECORD_ENERGY_AND_SPATIAL_BOUNDARY_v0.1_RELEASE.zip` (native propagation and record entropy rate v0.1, §§1, 7). These sources are development candidates, not accepted native interaction laws.

The crossing source takes a real cell port `u_t=0`, transverse derivative `g_t=(B_3^T f)_t != 0`, previous side, zero latch and local ordinal. It declares a root detector, FIFO, readiness, publication and durable acknowledgment. The finite recorder separately declares a source Fire, Ack, pending bit and bounded no-wrap word. Neither source derives the other's input.

The carrier-write source uses `C=C_*(K;C)` of dimension 47 for five tetrahedra, twelve orthogonal exposed-face projectors `P_f`, `Q=I-sum_f P_f`, and twelve pointer bits. Its one-pulse operator is

`U_w=Q tensor I + sum_f P_f tensor X_f`.

The pointer begins in a blank word. The declared drive duration `tau`, carrier energy `epsilon`, pointer coupling `J`, and bath are separate physical inputs; no event-count-to-time or energy calibration is assumed here. The readout is a diagonal pointer word. No metric beyond the source's orthonormal simplex basis is introduced.

## Exact scoped test

1. **Type and trigger.** `U_w` is a unitary on carrier times pointer and is applied by an externally prescribed pulse. It has no input port for the root detector's previous side, latch, local ordinal, queue, or Ack. In particular `Q P_f=0`, so on a pure top-cell coordinate `|t>` (in `Q`) it acts as identity on a blank pointer. The face-coordinate write condition is not the crossing condition `u_t=0, g_t!=0`. A root may coexist with face support, but the existing operator contains no rule to initiate its pulse *at that root*. Thus the supplied native propagation plus `U_w` does not constitute an autonomous Fire/Ack-to-write coupling.

2. **Readout collision.** For any input density matrix `rho`, the pointer marginal after one blank write is `p_out |0><0| + sum_f p_f |e_f><e_f|`, where `p_f=Tr(P_f rho)` and `p_out=Tr(Q rho)`. Hence any two distinct event histories with the same instantaneous exposed-face probabilities give identical pointer readouts under this one-pulse interface. The token's local ordinal and predecessor identity are absent. This is a no-go only for reconstructing those histories from this specified marginal readout without an added token encoding or retained controller; it is not a no-go for all UD memory extensions or the full coherent joint state.

3. **Finite retention.** Reusing a one-hot pointer without a fresh slot can toggle a face bit back to blank because `U_w^2=I`. The source itself treats the pulse as a write from a prepared blank. Fresh slots, protected append, acknowledgment gating, reset, or an explicit lossy rule must be supplied for repeated events. The earlier conditional Markov history model proves its fixed finite closed memory cannot store unlimited exact histories (§7), while the later thermal collision model loses distinguishability under its declared bath (§4). Neither statement selects an actual universal memory budget.

**RESULT — EXACT/CONDITIONAL NO-GO:** The published one-pulse face-label memory readout does not autonomously detect native cell crossings or encode their ordinal lineage. This conclusion is scoped to the stated carrier, pulse, blank preparation and pointer marginal. **OPEN:** source-derived root-to-pulse control; an injective token/address write including ordinals and predecessor links; a finite resource/retention rule; and a coupling of real amplitude evolution to Fire/Ack. The five-tetrahedron spatial alphabet (thirteen outcomes) and finite bit counter are distinct typed records. No physical promotion follows.

## Independent algebra check and next gate

The source's `U_w^2=I` follows independently from `P_f P_g=delta_fg P_f`, `Q P_f=0`, `Q^2=Q` and `X_f^2=I` on each block. The pointer marginal is obtained by tracing orthogonal carrier sectors; cross terms vanish under that trace. These checks do not verify a native detector. A future source must define a typed map from `(cell, root ordinal, previous side, latch, predecessor receipt)` into a prepared memory address and explicit pulse enable, and then test a second crossing before acknowledgment, simultaneous roots, capacity exhaustion and reversible erasure under its specified energy account.
