# Three-residual mixture coverage v0.1

**EXACT / conditional.** Resume 99680a3, held claim 577b2d5, integrated main
2ab32f5. Follow [square/radial coverage](SQUARE_RADIAL_MIXTURES_v0.1.md).
Agile mathematical test only; no empirical inputs and no bench amendment.

Retain the same two-polynomial work model Q+aP+bJ, reference work units,
endpoint boxes, and path-level work budget. Add the old y preparation
(−1/2,1) and its old fourth-reading residual R. In receipt order x,c,m,p,z,y,
append to the old two-row error map the row (−1/2,1,1,0,0,−2). Reuse the
same x,c,m,p,z observations across rows. In residual order S,T,R the
centers are (a,(3321/625)a−(4149/3125)b,a+b); each row kills Q.

The six error columns span three dimensions. The sum of the null and
alternative enclosures is the zonotope with these columns and receipt
radii 2B_v+|a|D_P(v)+|b|D_J(v), using the same Taylor bounds as before.
A face maximizing a linear functional has free generators precisely
where the normal dot product is zero. Each facet has two independent
free generators, so the primitive nonzero cross products of generator
pairs enumerate all facet normals up to sign. There are ten. Overlap
holds iff the center satisfies all ten two-sided support inequalities.

As before, each sign quadrant gives a polygon in amplitude space.
It is bounded because projecting it to the first two residuals imposes
the earlier bounded overlap region. Enumerating all boundary intersections
in the quadrants proves that the largest overlap infinity norm is
147290080559083100000000000/232732360394806259987469681, strictly between
632/1000 and 633/1000. Thus norm at least 633/1000 is uniformly sufficient
under the enclosing boxes, improving the earlier sufficient 723/1000.

The old counterexample (11/100,1/2) now separates, but (1/20,1/2) still
overlaps the null. The added reading narrows the gap without closing
uniform half-amplitude coverage. Overlap here describes the stated outer
enclosures; it does not claim that every enclosed error is physically
attainable. Path and hardware certificates remain open; physical
promotion stays 0.

Replay: python3 experiments/ud-channel-metric-bridge/three_probe_replay.py
