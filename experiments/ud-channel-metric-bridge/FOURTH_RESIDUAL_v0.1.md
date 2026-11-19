# Sharp fourth-work residual envelope v0.1

**EXACT / conditional.** Follow-up to [work Gram closure](WORK_GRAM_CLOSURE_v0.1.md)
and [capacitor error budget](CAPACITOR_PORT_v0.1.md), baseline d0ed586.
This is a prospective mathematical check, not an amendment to the frozen
bench. No hardware or physical data are used.

## Sharp bound and detection rule

In the same calibrated preparation basis define c=y+x/2, d=y−x/2,
and let W(v) be corrected work in units of common reference work W*.
The quadratic prediction is R=W(d)+W(c)−2W(y)−W(x)/2=0.
If the four reported values differ from their true values by errors
in the Cartesian product of symmetric intervals with radii b_v, then

    |R_reported−R_true| ≤ E=b_d+b_c+2 b_y+b_x/2.

This is sharp for that box: take positive endpoint errors on d,c and
negative endpoint errors on y,x, or reverse all signs. No statistical
independence is needed. Known correlations may justify a smaller joint
bound, but none is assumed here. Reject zero only when |R_reported|>E.
Every realization of an alternative with |R_true|=Δ is guaranteed to
reject zero exactly when Δ>2E. At equality a worst-case realization
touches the null threshold. If only the null-side certificate applies,
it can exclude the null on a particular reading, but does not certify
power against an alternative with unbounded errors.

## Transfer of the current budget

In the terminal basis (x,c), d=(-1,1) has L1 norm 2, exceeding the
original maximum 3/2. The endpoint preparation bound of capacitor
port v0.1 is 4η||v||_1+16η² per corrected receipt. Transferring its
same assumptions, including certified absolute stiffness row sum ≤2
and an independently certified non-preparation budget n=1/32, gives
b_x=b_y=b_c=1857/20000 at η=1/100 (use the existing common cap) but
b_d=2257/20000. Thus E=17513/40000 in W* units, or 17513/80 nJ
at W*=500 nJ. The new charge path and all these bounds would require
their own certificate; the frozen three-preparation protocol supplies
no fourth receipt.

At this planning budget, guaranteed detection requires Δ>17513/20000.
A half-W* nonquadratic departure therefore has no worst-case detection
guarantee under the box, even though a measured half-W* residual would
exclude zero. The candidate and uniform fixtures themselves are both
quadratic: both have R=0. Their different fourth work values are not
alternative residuals. Δ=1/2 here is a planning benchmark, not a
prediction of nonquadratic physics.

For an equal-radius box the strict design condition for that benchmark
is b<1/18 per reading. Keeping n=1/32 and the same endpoint argument,
the transferred E is 29η+72η²+9/64. For example, η=1/300 gives
E=28571/120000<1/4, enough under the same assumptions if achieved and
certified. This is a sufficient prospective budget, not a measured
instrument tolerance or a mandate to change the frozen bench.

Replay: python3 experiments/ud-channel-metric-bridge/fourth_residual_replay.py
Physical promotion 0; hardware hold and scorer unchanged.
