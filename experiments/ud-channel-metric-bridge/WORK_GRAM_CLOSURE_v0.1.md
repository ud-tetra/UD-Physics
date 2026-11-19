# Work Gram closure on the inherited/newborn plane v0.1

**EXACT / conditional.** This is an algebraic follow-up to
[centroid work port v0.1](WORK_PORT_v0.1.md). It neither amends
[the frozen bench](BLINDED_BENCH_v0.1.md) nor uses physical data.

Let x be the inherited harmonic, y the barycentric newborn mode,
and c=x/2+y. Let W(v) be the sham-subtracted average signed work in
joules (or in common reference-work units). Assume fixed, independently
certified preparation coefficients and a common positive work scale.
Assume W is a homogeneous quadratic form on span(x,y). Under the port
model W(v)=κa² vᵀH v/2, the coefficient basis and amplitude a are held
fixed and the scale κ has units of energy. No spatial or clock map
is assumed.

## Exact reconstruction and positive metric certificate

Write A=W(x), D=W(y), C=W(c). In the ordered basis (x,y), the unique
symmetric matrix compatible with the three work values is

    M = [[A,B],[B,D]],    B=C−D−A/4.

Expansion of W(c) proves both the formula and uniqueness. The normalized
plane metric is M/A if A>0 and AD>B². The candidate family has B=0 and
D/A=5t/4; hence t=4D/(5A) only on that family. The uniform-coefficient
control has D/A=5/4 and B/A=−1/2. Identifying this plane's form does
not recover a metric on the full refined carrier.

For a rectangular joint uncertainty enclosure of (A,D,C), the minimum
determinant occurs at a corner: AD−(C−D−A/4)² is concave separately in
each coordinate. Holding the other two fixed, moving to one endpoint
cannot increase the minimum; repeat for all coordinates. Thus positive
lower A and strictly positive minimum of the eight corner determinants
are necessary and sufficient to certify positive definiteness for every
triple in that rectangle. If the true joint set is smaller, this
certificate may be conservative for that set. Bounds touching zero do
not certify strict positivity.

## Falsification and identifiability limits

Three values always define a symmetric candidate, even if the actual
work law is nonquadratic. An additional independent mathematical
discriminator is d=y−x/2. Quadratic work predicts

    W(d) = D+A/4−B = 2D+A/2−C.

This polarization identity is a prospective check outside the frozen
scored bench. It can reject quadratic consistency on these directions,
but a pass does not establish quadraticity on all preparations.
For example, the polynomial response W(v)=vᵀMv+ε α²β²(2α−β)²
for v=αx+βy agrees on x,y,c for any ε, yet adds ε on d.

The common scale cancels from M/A. Uncertified gains that vary by shot
direction cannot be removed by this ratio: even uniform work reproduces
the candidate t=1 triple if the x and y gains are one and the c amplitude
gain is sqrt(3/2). Thus independent preparation measurement remains
necessary. The plane form gives no action normalization or spacetime
metric; cf. coefficient ledger v0.39, G05–G06 and Q101. No physical
promotion or new empirical claim.

Replay: python3 experiments/ud-channel-metric-bridge/work_gram_replay.py
