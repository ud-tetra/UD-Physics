# Square and radial mixture coverage v0.1

**EXACT / conditional; agile witness family.** Baseline 14ca4c6 and held
claim 577b2d5. Uses [square probe](SYMMETRIC_PROBE_v0.1.md) and
[radial J probe](RADIAL_J_PROBE_v0.1.md); no physical data or target.
No amendment to the frozen bench.

For work in W* units, W=Q+aP+bJ with Q homogeneous quadratic and P,J
as in the earlier probes. Keep charge normalized and cap each endpoint
coordinate error at 1/100. Use the same five corrected readings at
x,c,m,p,z, with z=(4/5)p, and reuse the very same reading at p.
The linear map of reading errors to (S,T) has respective columns
(−1/5,0),(−1/5,0),(1/10,0),(1/10,1),(0,−25/16).
Both rows annihilate Q. Evaluating the two witnesses gives
(S,T)=(a,(3321/625)a−(4149/3125)b), a full-rank map.

For each command v the quadratic-side error radius B_v is
4η||v||_1+16η²+1/32, η=1/100, under the prior stiffness and work
bounds. On the alternative side use B_v+|a|D_P(v)+|b|D_J(v).
For f=P,J, D_f(v)=L_f(v)+3L_f(0); L_f(v) is the sum of the absolute
nonconstant Taylor coefficients at v weighted by η to their degree,
as in radial v0.1. Both polynomials are even under simultaneous sign
reversal, so the same bound covers the negative command. The extra
terms explicitly cover endpoint sensitivity on the alternative side.

The shared-error polygon has three edge directions from the columns
g_i. Two residual enclosures (quadratic null and given mixture) overlap
iff for all n in {(1,0),(0,1),(10,−1)} the following holds:

    |n·(S,T)| ≤ Σ_i |n·g_i|[2B_i+|a|D_P(i)+|b|D_J(i)].

Proof: intersection is equivalent to membership of the center difference
in the Minkowski sum of the two centrally symmetric polygons. The
listed normals are perpendicular to all distinct generator directions.
Their strips therefore describe the sum exactly. The extra strip uses
the shared p reading; equality allows contact. This is exact for the
chosen outer enclosures, not an assertion of attainable physical errors.

The no-guarantee region is a polygon in each sign quadrant of (a,b):
replace absolute amplitudes by signed linear expressions and split
the left side into two inequalities. Boundedness follows by using the
S inequality to bound |a| in terms of |b| and substituting into the T
inequality; the remaining coefficient of |b| is positive in replay.
Enumerate all boundary intersections in each quadrant and retain those
satisfying every inequality. The largest sup norm occurs at a vertex.
Its exact value is in the saved replay output: it lies strictly between
722/1000 and 723/1000. Thus an amplitude norm ≥723/1000 is sufficient
in every direction under these enclosures. Pure half-amplitude P and J
are both detected, but (a,b)=(11/100,1/2) still overlaps the null
enclosure. There is no uniform half-amplitude guarantee at this budget.

Replay: python3 experiments/ud-channel-metric-bridge/mixture_probe_replay.py
All path-level certificates and empirical work remain open.
Physical promotion 0.
