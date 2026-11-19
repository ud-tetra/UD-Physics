# Direct mixed Taylor coverage v0.1

**EXACT / conditional.** Agile planning calculation; no measured data.
Baseline e48b44c, held claim 577b2d5, integrated main 2ab32f5.
Uses [three-residual coverage](THREE_PROBE_COVERAGE_v0.1.md); preserves
the six commands, work and charge normalization, path-level bounds, and
shared receipt map. The frozen bench has not been extended.

## One charge perturbation per preparation

For the declared dimensionless charge coordinates and work units W*,
write the departure F=aP+bJ. At each nominal command v expand both
polynomials in the same endpoint error variables. Let p_(v,k), j_(v,k)
be the Taylor coefficients at multi-index k, already multiplied by
η^|k|, where η=1/100. Define

    L_v(a,b) = Σ_(k≠0) |a p_(v,k)+b j_(v,k)|,
    D_v(a,b) = L_v(a,b)+3L_0(a,b).

The endpoint box implies the bound by direct monomial domination.
Evenness under simultaneous sign reversal preserves the bound for the
negative command, and the signed average and sham use the same one
loaded plus three zero-command bounds as before. Combining coefficients
prior to the absolute value preserves cancellation within an endpoint;
D_v(a,b)≤|a|D_v(1,0)+|b|D_v(0,1). This remains an upper bound, not an
exact extremum of the endpoint polynomial. Cross-receipt correlations
beyond reusing the same reading in different residuals are not assumed.

## Exact worst direction for these outer enclosures

Let g_i be the inherited receipt columns, B_i the unchanged quadratic
receipt radii, M(a,b) the inherited residual center, and n any of the
ten inherited facet normals. Define h_n=2Σ_i |n·g_i|B_i>0 and

    f_n(d) = [ |n·Md| − Σ_i |n·g_i|D_i(d) ] / h_n.

On the amplitude ray λd, ||d||∞=1 and λ≥0, overlap of the two
enclosures holds iff λ max_n f_n(d)≤1. This is the same exact
facet test for the sum of the two enclosing zonotopes with tighter
alternative receipt radii. The score is centrally symmetric in d.
Three edges cover the upper half of the unit square boundary. Split
them at every zero of a linear form inside an absolute value.
On each resulting segment all ten f_n are affine. The minimum of
their upper envelope occurs at an endpoint or at an intersection of
two of those affine functions: between intersections their ordering
is constant. Exact rational replay checks 83 segments, including all
such intersections. The minimum is strictly positive, and its
reciprocal gives the largest overlapping amplitude infinity norm.

The largest overlapping norm is
6288871753696320200000000000/10180223594200285859314975003,
strictly between 617/1000 and 618/1000. Thus ||(a,b)||∞≥618/1000
suffices uniformly, down from 633/1000 with the separate bound.
The witness (1/20,1/2) still overlaps: its maximum normalized strip
score is 53774878484448047/62198100000000000 < 1. This is overlap
of certified outer sets; it does not construct a physically realized
error sequence. Half-amplitude coverage is not certified.

No empirical result, no certified apparatus, no calibration change,
and physical promotion 0. Replay:
`python3 experiments/ud-channel-metric-bridge/mixed_taylor_replay.py`.
