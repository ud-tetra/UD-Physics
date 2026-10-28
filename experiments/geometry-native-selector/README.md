# Native symmetry and support-current gate for tetrahedron/cube map selection

**Status:** EXACT finite K4 symmetry statement; CONDITIONAL on an S4-equivariant deterministic evolution and an invariant preparation. No native cubical geometry selection, material coupling or graphite prediction. Physical promotion 0; independent physics review NOT_RUN.

## Typed question

The [rooted six-sector map](../geometry-six-sector-map/README.md) distinguishes one of the tetrahedron's four vertices and creates a 3:1 target surface-density split. The [12-cell map](../geometry-s4-full-map/README.md) respects all 24 `S4` vertex permutations and gives a uniform induced cube surface density. Does the current K4 packet support law select the first map from an unconditioned, fully symmetric packet?

Use vertex set `V={0,1,2,3}` with full native `S4` action (supplied ledger v0.39(2), P03). Let `X` be a packet state space on which the action is defined; let `x0∈X` be fixed by every group element. An assumed deterministic map selector `r:X→V` is `S4`-equivariant when `r(gx)=g r(x)`. Then `r(x0)=g r(x0)` for every `g`, but no vertex of a transitive four-element `S4` set is fixed by every `g`. **There is no such single-root selection at `x0`.** If a unique deterministic equivariant update preserves the invariant subspace, the same result holds at every later update. This is a scoped symmetry theorem, not a theorem against spontaneous branch choice, nonunique dynamics, external contact, or a symmetric 12-cell map.

An equivariant *random* root from an invariant state must give each vertex probability `1/4`; every root has stabilizer `S3` of order 6. This mixture does not by itself produce a single cube embedding or material current. A one-hot contact state or another explicit boundary state can reduce the stabilizer to `S3` and make a rooted branch admissible, but its preparation and persistence must be supplied.

## Current and stock scope

The signed oriented edge space `C1(K4;R)` has **no full-S4-invariant vector**: for each edge, swapping its endpoints fixes the underlying edge while reversing its orientation, forcing that coefficient to zero. The invariant vertex subspace is one-dimensional (uniform amplitude). For a fully invariant packet's vertex `x` and oriented edge `y`, therefore, `y=0` and the Q166 local vertex-edge current `J_ie=2 B1_ie x_i y_e` vanishes. The Q167 fixed-mask stock/current version has the same zero-current statement for `y=0`. This does not make every native current zero in asymmetric or driven states.

Q170 gives a stock balance `dS=J_in-J_out`; Q177–Q179 assign equal-top-star support shares and continuity *after* a cell ownership relation is specified. These identities are conditional on their carrier/incidence and do not name cube coordinates, a target Euclidean surface measure, or a rule choosing the 6-cell versus 12-cell refinement. Both geometric maps can be paired with a measure pushforward conserving total stock and oriented flux. Conservation alone consequently leaves the geometric choice underidentified. Equating native quadratic stock with Euclidean boundary area would be an additional physical map, not a consequence of Q170.

`replay.py` enumerates all 24 source permutations, the six oriented K4 edges and an endpoint-swap sign witness for each, root orbit/stabilizers and the forced uniform random-root law. It does not numerically simulate Q166 dynamics. The theorem is proved directly above; the replay checks its finite action premises. No measured twist angle, friction, force or load enters.

## Next discriminant

Define one **native** boundary/contact state and update rule (including support ownership and oriented flow) that produces either a persistent rooted branch or the symmetric map without imposing cube coordinates by hand. Then map native stock/current to a specified physical boundary density and calculate a response not already fixed by Euclidean shape normalization. Until that source exists, `3^(1/6)`, the rooted 3:1 split and the two Jacobian-one constructions are conditional geometry, not dynamical coefficients.
