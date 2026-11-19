# Independently anchored quadratic baseline v0.1

**EXACT / conditional; agile design.** Resume 17d09c6, held claim
577b2d5, main 2ab32f5. Follow
[full-box overlap](CHARGE_BOX_OVERLAP_v0.1.md) and
[mixed Taylor coverage](MIXED_TAYLOR_COVERAGE_v0.1.md).
No physical data, empirical fit, or frozen bench modification.

## Anchor contract

Keep the six work preparations x,c,m,p,z,y, normalized (u,v) charges,
W* work units, receipt radii B, and direct mixed Taylor allowance D.
Write Q=κ_u u²+κ_uv uv+κ_v v². κ_uv is the polynomial coefficient,
twice the off-diagonal matrix entry, not an independently defined
physical coupling. An anchor is a separate observation of a selected
coefficient, with absolute error ≤δ in W* units under either model.
The anchor measures the quadratic part without witness contribution,
using data independent of the six full-amplitude receipts. This is
a requirement, not an obtained calibration. For example, the model's
Hessian at zero kills both witnesses, but a finite-amplitude Hessian
estimate still needs a remainder and instrument bound.

For the earlier fixed full-box pair, the minimal common radii allowing
its coefficient differences are (27/400,29/400,1/40) for
(u²,uv,v²), respectively. An anchored radius below the matching
entry excludes that pair regardless of observed anchor center.
This alone does not exclude differently adjusted quadratic baselines.

## Uniform certificate

Append unit coefficient rows to the quadratic sample matrix of the
six receipts for the selected anchors. In the augmented receipt space
the null–alternative difference has radii 2B_i+D_i(a,b) on work
and 2δ on each anchor, with zero witness signal on anchors. Eliminate
quadratic nuisance by projection as in
[the seventh-probe proof](SEVENTH_PROBE_SCREEN_v0.1.md). Signed cofactors
of rank-three four-row subsets include every needed contrast w=(g,n)
in the left nullspace, where g weights work and n weights anchors.

At (a,b)=d/2, ||d||∞=1, the two outer enclosures overlap iff all
contrasts obey

    |g·[P,J]d| − |g|·D(d) − 4|g|·B ≤ 4δ||n||₁.

As δ increases, overlap only expands. A contrast with n=0 already
separates some directions, independent of δ. Restrict to the remaining
directions and minimize the maximum left-side surplus divided by
4||n||₁ over contrasts with n≠0. This gives the critical common
anchor radius. Resolve each absolute value at its exact zero on the
unit-square boundary; use central sign symmetry. Within each resulting
segment, unanchored constraints clip a closed interval, and the
anchored upper envelope is piecewise affine. Its minimum is at a
clipped endpoint or at an active line intersection. Exact rational
replay uses the ordered upper envelope and independently checks each
record-improving segment via all pairwise intersections.
Monotonic scaling of each fixed-direction contrast margin beyond
half amplitude preserves separation.

| Independently anchored coefficients | Certified sufficient common radius δ |
|---|---:|
| κ_u, κ_uv | 7/200 |
| κ_u, κ_v | 17/1000 |
| κ_uv, κ_v | 4/125 |
| κ_u, κ_uv, κ_v | 11/250 |

All radii are dimensionless in reference-work units and are inclusive
sufficient bounds. For (κ_u,κ_uv) the exact critical radius is
3548697225629395855505826137/101348827411725000000000000000
(strictly between 35/1000 and 36/1000). For all three it lies between
44/1000 and 45/1000; the output gives its exact value. At equality
the respective enlarged enclosures touch. Each of the three single
coordinate anchor tests still overlaps for some half-amplitude
direction even at radius zero in the enlarged model. This is scoped
to these six work preparations and coordinate anchors; an arbitrary
linear combination is a different anchor design.

For sufficiency allowing unrestricted quadratic nuisance is conservative
relative to additional stiffness or positivity constraints. Overlap in
that enlarged model is not evidence of physically attainable errors.
There is no certified hardware measurement, empirical identification,
or physical promotion. Replay: python3
experiments/ud-channel-metric-bridge/baseline_anchor_replay.py
