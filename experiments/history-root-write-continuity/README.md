# Exact-root write continuity gate and source correction v0.1

2026-11-06. Discovery session `history-root-write-continuity-20261106-01`; base `ud-tetra/UD-Physics@a635d13f2552a313f245c6d837f549c913b16286`; held claim `93e76e5c9661456bbbfdccf11323a654eed2aad9`. Physical promotion 0; no physical target or fitting; independent review NOT_RUN.

## Source correction

The prior [capacity-feedback audit](../history-capacity-feedback/README.md) omitted a consequential existing source: `ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD finite admission and wave-feedback discriminator v0.1.md` §§1, 3–5, SHA-256 `9cf1c88ed2815e0af51ab4d8df7d86b36f6670857da843b43aa61d8eec7918a7`. It had already compared finite admit/reject, global scalar pause and local whole-cell pause. It established bounded active slots only with explicit rejected roots, norm and orbit preservation under a *declared* global gate, and changed rank/frequencies plus a zero-plateau crossing counterexample for local pause. The later Discovery calculation in PR #341 independently checked a two-coordinate special case and the distinct point that Ack does not free its retained token slots. It must not be read as first discovery or native selection of scalar feedback. This addendum preserves the prior report and corrects its dependency and novelty scope.

Also relevant: `Docs/UD event admission and interface memory.md` §§1–3, SHA-256 `675f970b258ecea88ee0b1eb198000164d548f05fc9c15d4ba242ac07192874a`, finds an explicit signed hidden-memory witness and leaves formation trigger and interaction open. `docs/UD_CARRIER_WRITE_DISTINGUISHABILITY_AND_ENERGY_v0.1_RELEASE.zip` §§1–3 (SHA-256 `5bb7d306ef539d30e3e0ce1dc7c85e6182a39404e0bb774430fed08b4665eda8`) describes an externally prescribed carrier face-label pulse. No cited source promotes a root-triggered token controller to native law.

## Precise fixed-map obstruction

Let `C` be a finite-dimensional real or complex Hilbert carrier with a cell coordinate `u_t` and a face vector `f` such that the native transverse-root slope `g_t=(B_3^T f)_t != 0`. Let `M` be a pointer initially in `|0>`. Consider one *fixed linear* map `V:C tensor M -> C' tensor M'` applied at the same instant to every input, with an orthogonal blank-pointer subspace `C' tensor span{|0'>}`. Unitarity is sufficient but not required. Assume the strict root-only specification: every carrier input with `u_t != 0` produces a blank pointer, while the transverse root input `x_0=(u_t=0,f)` must produce a nonblank pointer with nonzero probability. Other coordinates are fixed to zero for this witness. The coordinate slope and orientation conventions are those of the cited crossing audit. This is an instantaneous state-only interface, with no prior-side detector register, event clock, nonlinear switch, or externally timed pulse.

Choose a nonzero cell basis vector `e_t`, and `x_+=x_0+e_t`, `x_-=x_0-e_t`. Both have nonzero cell coordinate, so by premise `V(x_+ tensor |0>)` and `V(x_- tensor |0>)` lie in the blank subspace. By linearity,

`V(x_0 tensor |0>) = [V(x_+ tensor |0>)+V(x_- tensor |0>)]/2`,

which also lies in the blank subspace. Normalizing the three nonzero inputs only rescales outputs and does not change blank support. This contradicts the required nonblank transverse-root readout. Equivalently, the off-root inputs span the carrier and the blank subspace is closed. A continuous channel with a blank pointer on every off-root state also cannot have a positive write probability at a limit root state.

**EXACT / NO-GO under these hypotheses:** a fixed linear instantaneous write map cannot be exactly silent on every nonroot input and write only at a transverse root. This says nothing about approximate finite-width detectors, continuous interactions accumulated over a time interval, externally timed pulses, or an enlarged state with prior-side/latch/controller variables and hybrid switching. It is not a no-go for all autonomous Hamiltonian models. A fixed map can write face labels, as in the published pulse, but that is a different condition from root-only selection.

## Energy and decision

No Hamiltonian or pointer spectrum is selected by this theorem. Adding an energy-conservation requirement only restricts the already impossible fixed-map class; it does not produce a pulse work value. The source's face pulse has a declared drive and separate work account, while the two-event token extension uses a different pointer. Copying the former cost to the latter would mix carriers and units.

The next admissible branch must carry detector history or continuous-time interaction dynamics: specify the state space, local coupling, initial memory preparation, root-resolution tolerance/latency, capacity state and admission rule; derive the joint generator or transition map and energy balance; test root multiplicity, false triggers, exhaustion and spectrum. The present fixed-map branch is **AUTO_FREEZE** under its exact-root-only specification. Reopen it only by changing a stated hypothesis, especially by adding a controller state or finite-width event window. Native root-to-write coupling remains **OPEN**; physical promotion 0.
