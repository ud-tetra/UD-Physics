# Bounded seventh preparation screen v0.1

**CANDIDATE / exact conditional finalist audit.** Resume d2483e2, held
claim 577b2d5, main 2ab32f5. Inherit the work and charge model, direct
mixed Taylor endpoint bounds, and six commands from
[mixed Taylor coverage](MIXED_TAYLOR_COVERAGE_v0.1.md). No physical data,
fitting, calibration changes or frozen bench changes.

## Screen and exact check

For each possible seventh command on the upper half of a 1/40 charge
grid in the unit box, skip the origin and commands equivalent to existing
ones under simultaneous sign reversal. This leaves 3313 candidates.
Screen with a 1/50 angular grid on the three edges of the upper half unit
amplitude box (201 distinct directions). Use floating point only for
ranking; it can miss a worse direction between sample points. The first
six candidates by that ranking receive exact rational verification.

For each set of sites, let A have rows (u²,uv,v²). The quadratic nuisance
space is the column span of A, of rank three (already witnessed by
x,c,p). Work receipts are projected to the quotient by this span, with
the same receipt used each time. The difference of the null and mixture
outer boxes projects to a symmetric zonotope. Its facet normals lift
to contrasts in ker(Aᵀ). In a quotient of dimension m−3, a facet normal
kills at least m−4 independent projected coordinate generators, and
thus is supported on at most four receipt coordinates. Its support is
a minimal dependence of rows of A: otherwise the space of normals
supported there would have dimension at least two, contradicting the
facet's one-dimensional normal space. Any such minimal row dependence
can be extended to a four-row rank-three submatrix by adjoining
independent rows. Signed three-row cofactors recover its contrast,
including smaller supports. Enumerating all four-subsets therefore
includes every needed facet; any redundant contrasts remain valid.

For each contrast w, the signed center is Σ_i w_i (aP_i+bJ_i), and its
overlap radius is Σ_i |w_i|(2B_i+D_i(a,b)). B and the direct mixed
D are inherited, evaluated at the new site too. Apply the same exact
piecewise affine directional minimax as the six-probe proof. Verify that
the quotient construction reproduces the previous six-probe radius
exactly before comparing the seven-probe configurations.

## Outcome and limits

The best exact finalist is (-5/8,1). Its largest overlapping amplitude
norm is strictly between 603/1000 and 604/1000; the replay records the
exact value and maximizing direction. Thus 604/1000 is sufficient,
versus 618/1000 before. The half-amplitude witness (1/20,1/2) still
overlaps for all six exact finalists. No uniform half-amplitude
guarantee was obtained. Neither the finite float screen nor the exact
finalist result proves a continuum optimum or a one-probe impossibility.
New path-level certificates remain open. Physical promotion 0.

Replay: run seventh_probe_screen.py (NumPy) and seventh_probe_replay.py
(standard library only) from the directory of this note.
