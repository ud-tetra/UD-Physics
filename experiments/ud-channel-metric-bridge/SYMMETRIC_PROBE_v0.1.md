# Symmetric work probe v0.1

Agile candidate; exact conditional result. Resumed held claim 577b2d5,
isolated Discovery head 32d6761; integrated main observed at 2ab32f5.
Uses [the prior work-plane witness](WORK_GRAM_CLOSURE_v0.1.md) and
[the fourth-reading error model](FOURTH_RESIDUAL_v0.1.md). No new physical
data, timing assumption, or change to the frozen bench.

## Design and scope

In normalized terminal charge coordinates (u,v) in the basis (x,c),
use x=(1,0), c=(0,1), p=(1,1), and m=(-1,1). All per-terminal command
magnitudes are at most one. Work is signed-average, sham-subtracted,
in units of W*. Define S=[W(p)+W(m)−2W(x)−2W(c)]/10. The numerator
vanishes on every homogeneous quadratic form by expansion.

The pre-existing alternative from WORK_GRAM_CLOSURE is W=Q+εP,
where Q is quadratic and P=α²β²(2α−β)² in the (x,y) basis.
Here α=u+v/2 and β=v, so P=4u²v²(u+v/2)². The old residual
has value ε for this witness. The square probe has the same normalized
response ε, since P(p),P(m),P(x),P(c) are 9,1,0,0. Division by ten
normalizes by that explicitly derived response, not by a measured target.

## Transferred error and guarantee

Assume η=1/100 per coordinate at every endpoint and an independently
certified non-preparation bound 1/32 per corrected receipt in W* units,
including for the new paths. Transfer the existing quadratic prep model
4η||v_command||₁+16η² to a quadratic part with stiffness row-sum ≤2.
Axes cost 1457/20000 each and corners 2257/20000 each. The sharp null
radius for this induced independent receipt box is E0=5171/100000
in normalized S units (raw numerator radius 5171/10000).

For the alternative, separately bound endpoint sensitivity of P;
the quadratic stiffness bound alone does not control it. P expands
as 4u⁴v²+4u³v³+u²v⁴. For any command in the unit box and perturbations
of size η, binomial expansion bounds the change in P by
9[(1+η)⁶−1]. At a zero command its value is bounded by 9η⁶.
The same signed-average and sham subtraction permits one loaded
term and three zero-command terms per corrected receipt. Thus the
normalized alternative radius is bounded by
E1(ε)=E0+(6/10)|ε|·9[(1+η)⁶−1+3η⁶].
Using the strict decision |reported S|>E0, the guarantee condition
is |ε|>E0+E1(ε). It holds at |ε|=1/2 with the same endpoint and
non-preparation limits, conditional on the prospective certificates
and the stated endpoint-work model. No independence distribution or
common-error cancellation is presumed.

## Counterexample and exposure

No general dominance over the old residual follows. Replace P by
P·(4−5uv)/9. This even polynomial is still zero at the original
three reference commands, equals one at m, and minus one at p.
It retains the old residual ε and has zero square residual.
The design was selected with explicit knowledge of the earlier
mathematical witness; there were no physical targets or fits.

Simultaneous full charge on both terminals can increase voltage and
work, including under the quadratic null. Per-terminal command range
alone cannot certify device range, work integration, or loss.
The non-preparation budget for the new paths is OPEN and the hardware
hold stands. Physical promotion 0. Do not substitute these preparations
into the frozen protocol.

Replay: python3 experiments/ud-channel-metric-bridge/symmetric_probe_replay.py
