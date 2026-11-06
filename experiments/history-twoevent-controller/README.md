# Two-event token write and capacity gate v0.1

2026-11-06. Discovery session `history-twoevent-controller-20261106-01`; base `ud-tetra/UD-Physics@116155bb07da16338fb36560549b68fb102d6058`; held claim `94b65d153344a6ded5623faf63740f1ba2f19630`. Physical promotion 0. No measurement target used; independent physics review NOT_RUN.

## Source and typed construction

Source inputs: `ud-tetra/UD@a78193d420f3bac957be081aed0525fbc1457825`, `Docs/UD native crossing-to-receipt audit v0.1.md` §§1–3 (resolved root, latch, local ordinal, receipt, Ack); `Docs/UD capacity mechanisms and native crossing bridge audit.md` §§1–3 (SA-TIME-018 finite Fire/Ack); `docs/UD_CARRIER_WRITE_DISTINGUISHABILITY_AND_ENERGY_v0.1_RELEASE.zip` §§1–4, SHA-256 `5bb7d306ef539d30e3e0ce1dc7c85e6182a39404e0bb774430fed08b4665eda8` (face-label pulse and energy); and the preceding [source gate](../history-write-trigger/README.md). All source claims retain their development status.

This **CANDIDATE** adapter takes *already resolved* root tokens from a detector and does not construct a detector from real amplitudes. For two cells `A,B`, let `T={(A,1),(A,2),(B,1),(B,2)}` be the finite token alphabet. `M=M_1 tensor M_2`, with each slot a five-dimensional Hilbert space spanned by blank `|0>` and four orthogonal token words `|a>`. This memory is distinct from the published twelve-bit exposed-face carrier memory and from the SA-TIME-018 bounded counter. It is a new extension, not an identification of those carriers.

A classical controller has next local ordinal `o_c`, the two slots, and a FIFO of unacknowledged token identities. On a resolved root for cell `c`, if a blank slot remains, it allocates `(c,o_c)`, applies a controlled pulse on the first blank slot, increments `o_c`, and queues the token for Ack. Ack of the FIFO head removes only the pending acknowledgment, not the stored word. Duplicate or out-of-order Ack has no effect. At two occupied slots, another root is rejected and is reported as loss; losslessness would require source-defined backreaction, export or additional storage.

The assumed pulse may be represented by `V=sum_{a in T}|a><a|_T tensor X^{code(a)}` on the selected five-state slot, with `X|j>=|j+1 mod 5>` and an injective `code:T->{1,2,3,4}`. The token control register and pulse enable are supplied; `V` is unitary on token times slot and maps the prepared blank to an orthogonal token word. It is not the published face-projector `U_w`. A controlled inverse exists, so an Ack does not itself entail thermodynamic erasure. The source gives no pulse Hamiltonian, preparation work, clock or energy cost for this extension.

## Result and exact checks

**EXACT/CONDITIONAL:** For histories of at most two admitted roots over `{A,B}`, ordered slot words are injective: the seven histories `empty`, `A`, `B`, `AA`, `AB`, `BA`, `BB` have seven distinct records. In particular `AB` and `BA` are distinct, and `AA` stores local ordinals 1 and 2. The proof is direct: the first occupied slot decodes the first token and the second occupied slot decodes the second; the injective token code and position recover the entire admitted history. Ack leaves both words unchanged. A third root at full capacity cannot be admitted by this finite controller.

`python3 experiments/history-twoevent-controller/check.py` independently enumerates all seven histories, checks collision-free output, FIFO/duplicate Ack, and third-root rejection for each two-root history. It reports seven distinct records and zero collisions. This is finite enumeration of the defined toy model, not a native UD event-law proof.

**OPEN:** The source does not supply a real-amplitude root detector with guaranteed resolution, a native token-controlled pulse, an autonomous scheduler, a conserved resource/energy account, or a rule that halts a continuing native root flow at full capacity. The controller therefore closes only a conditional finite interface design. Its exhausted third root is a counterexample to indefinite losslessness under an independently continuing source. Physical time, metric and units are unassigned; event ordinal is not a clock calibration. Physical promotion remains 0.

## Next gate

Derive or source an event-triggered coupling that implements the token pulse, including a bound on detector delay and a native admission/backreaction rule at capacity. Verify the joint carrier-controller evolution and energy exchange before interpreting the retained words as a physical universal record.
