# Full charge-box overlap certificate v0.1

**NO-GO / exact for the declared outer error-box model.** Resume
178e3d5, held claim 577b2d5, main 2ab32f5. Follow
[seventh preparation screen](SEVENTH_PROBE_SCREEN_v0.1.md).
No physical data, hardware change, or amendment to the frozen bench.

Use normalized charge (u,v) in [-1,1]^2 and work in reference units W*.
Retain the homogeneous quadratic nuisance class and the scalar
per-receipt bound B(u,v)=4η(|u|+|v|)+16η²+1/32, η=1/100.
The null and alternative enclosures each permit at least this radius.
The alternative's extra mixed Taylor bound is not needed below.

## A fixed pair fits the entire box

Put F=P/25+J/2 with P and J from
[mixed Taylor coverage](MIXED_TAYLOR_COVERAGE_v0.1.md), and use the
quadratic correction

    q = (27 u² - 29 uv + 10 v²)/200.

The exact certificate establishes |F−q| < (19/20)(2B) everywhere
on the charge box. Compare work models W_alt = u²+v²+F and
W_null = u²+v²+q. Both quadratic parts are positive definite and
satisfy the stiffness absolute row-sum cap of two. The alternative has
amplitude infinity norm exactly 1/2. The single common receipt function
(W_alt+W_null)/2 differs from each model at every command by less
than (19/20)B. It therefore belongs to both receipt boxes for any
finite list of permitted commands, independent of how many are added.
All residuals calculated from those receipts are identical. The same
witness survives a uniform five-percent reduction of these radii.

This scope allows the quadratic nuisance to differ between models.
An independent constraint fixing its coefficients or a stricter,
jointly certified physical error model is a different problem.
The result does not assert the midpoint receipt pattern is realizable
by actual charge perturbations. It rules out a guaranteed classifier
based solely on the declared boxes, not on physical laws not supplied
to the model.

## Exact continuum check

The witness and rational quadratic were selected after an exploratory
floating point weighted fit on a charge grid; no empirical target was
used. The fit is not evidence for continuum coverage. Both F and q
are even under simultaneous sign reversal, so it suffices to take v≥0.
For u=±x with x≥0 and each sign of the residual, form
(19/20)2B(x,v) ± (F−q)(±x,v) on the unit square. Convert each polynomial
to tensor Bernstein form of bidegree (6,6) using
x^i=Σ_(k≥i) [C(k,i)/C(6,i)] b_(k,6)(x).
The basis is nonnegative and sums to one, so positivity of all
coefficients proves positivity on a cell. Subdivide by exact
midpoint de Casteljau steps, alternating axes. The four checks use
20 terminal cells total, maximum depth six, and strictly positive
rational coefficient floors. The replay also cross-checks the basis
and split identities at rational coordinates.

Replay: python3 experiments/ud-channel-metric-bridge/continuum_overlap_replay.py
Physical promotion 0.
