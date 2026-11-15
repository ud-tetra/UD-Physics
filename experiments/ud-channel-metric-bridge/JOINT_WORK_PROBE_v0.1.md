# Joint work-probe identification v0.1

**EXACT / conditional; agile alternative family.** Discovery baseline 7f3b7a2,
held claim 577b2d5; main observed at 2ab32f5. This follow-up uses
[the fourth residual](FOURTH_RESIDUAL_v0.1.md) and
[the square probe](SYMMETRIC_PROBE_v0.1.md). No physical target was used.
Preparations and normalization are inherited; no frozen bench changes.

## Dependence and ideal identification

In normalized terminal coordinates (u,v) let W=Q+aP+bJ, where Q is any
homogeneous quadratic form, P=4u²v²(u+v/2)², and J=P(4−5uv)/9.
Here a and b are amplitudes in common reference work units W*; the charge
coordinate is separately normalized to unit command range. P and J are
declared mathematical witnesses, not inferred material energy laws.

Assemble the five corrected work receipts in order (x,y,c,m,p), where
x=(1,0), y=(−1/2,1), c=(0,1), m=(−1,1), and p=(1,1).
Use the same shared receipt for each repeated symbol. The old residual R
and normalized square residual S have columns g_i:

    L = [[−1/2, −2, 1, 1, 0],
         [−1/5,  0,−1/5,1/10,1/10]].

Both kill Q. The exact mixture map is (R,S)=(a+b,a); determinant −1.
Thus a=S and b=R−S. The pair is complete on this declared two-dimensional
alternative span; arbitrary work laws outside that span need not be detected.

## Joint box and strict guarantees

With η=1/100, use radii (1457,1857,1457,2257,2257)/20000 for the
quadratic preparation and non-preparation error, following the previous
error model on each command. The assumed work and loss budget for new
paths still needs its own certificate. The common receipt error box
pushes forward to Z0 = {Σ g_i e_i: |e_i|≤radius_i}. Its exact directional
radius is h0(n)=Σ radius_i |n·g_i|. The polygon has edges parallel to
the five column directions: each generator segment adds one edge
direction under Minkowski addition. Thus the ten signed inequalities
|n·r|≤h0(n) for n in {(2,−5),(0,1),(1,5),(1,−10),(1,0)} are necessary
and sufficient for consistency with a zero true residual under this
box. Reject only for strict violation. This joint rule uses shared
reading errors directly; it does not assume independent noise samples
or combine marginal residual intervals as if errors were unrelated.

For alternatives, add a common per-receipt endpoint-error bound δ,
where h_k=(1+η)^k−1+3η^k and

    δ(a,b)=9|a|h_6 + |b|(4h_6 + 5h_8).

The absolute coefficient sums are 9 for P and at most 4 and 5 for
the degree-six and degree-eight pieces of J; the preparation and three
zero-command endpoint argument is as in the square probe. This bounds
the extra contribution even when the alternative changes sensitivity
to endpoint charge. Write h_ab(n)=h0(n)+δ(a,b)Σ|n·g_i|.
All realizations in the certified enclosure are guaranteed to reject
the quadratic null iff some tested n has

    |n·(a+b,a)| > h0(n)+h_ab(n).

For any two mixtures substitute their residual difference on the left
and the sum of their two h bounds on the right. Proof: their output
sets are disjoint iff their center difference is outside the Minkowski
sum of the centrally symmetric error polygons. The sum has the same
five directions and adds the supports. Equality permits contact.
This is an exact decision for the specified enclosing boxes, not a
claim that every error in an outer enclosure is physically attainable.

The replay certifies detection of (1/2,0) and (1/2,−1/2), including
the latter's exact cancellation in R. A pure b=1/2 is not guaranteed
even in the planning box with only the quadratic-side radii on both
sides: its output set overlaps the null enclosure. Rank does not give
uniform half-W* sensitivity. As a strict benefit over two marginal
tests, the synthetic residual (2/5,1/20) lies inside both marginal
null intervals but violates the (1,5) joint strip.

No measured work, calibration, hardware release, or physical promotion.
Replay: python3 experiments/ud-channel-metric-bridge/joint_probe_replay.py
