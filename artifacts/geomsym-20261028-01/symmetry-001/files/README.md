# Symmetry-selection audit of the six-sector tetrahedron/cube map

**Status:** EXACT finite cube-isometry group audit; CONDITIONAL interpretation for map selection. No native UD map law, physical coupling, or promotion; independent review NOT_RUN.

## Question and typed groups

The [six-sector construction](../geometry-six-sector-map/README.md) starts at one distinguished tetrahedral vertex, labels the other three axes, and maps the four original vertices to the cube corner star `H={000,100,010,001}`. A regular tetrahedron's four vertices carry full `S4` permutation symmetry (ledger v0.39(2), P03); the target cube has 48 Euclidean isometries, represented by coordinate permutations and independent coordinate flips. Does the *specific map* intertwine full `S4` through target cube **isometries**? This is stricter than allowing arbitrary conjugated piecewise-linear target actions.

## Exact scoped obstruction

The six squared pairwise edge lengths in `H`, in cube-edge units, are `(1,1,1,2,2,2)`. Cube isometries preserving `H` form a group of order **6**, permuting the three axis neighbors while fixing the distinguished corner. Thus the selected map is equivariant under the `S3` stabilizer of the original root vertex, but it **cannot** be equivariant under the full order-24 `S4` by cube isometries. One source permutation swapping the root with a neighbor would need an isometry inducing an absent star permutation. Exact enumeration checks all 48 cube isometries.

The restriction is about this map. Four alternating cube vertices `E={000,011,101,110}` have six equal squared pairwise distances `(2,2,2,2,2,2)` and a cube-isometry stabilizer of order **24**, inducing all `S4` permutations on `E`. That is a vertex-level alternative to the star image; this audit does **not** construct an equivariant interior/face map or prove one impossible.

## Boundary-density consequence

The previously computed induced surface stock from a uniform tetrahedral source is `(3/2)3^(1/6)` on the three zero-coordinate cube faces and `(1/2)3^(1/6)` on the three unit-coordinate faces. This 3:1 split follows the **selected star map**, not a tetrahedral invariant. Composing with cube inversion `u -> 1-u` exchanges the two groups. An equal mixture of the two pushforward *area measures* has uniform density `3^(1/6)` on all six faces and the same total stock. That mixture is a statistical preparation over two maps, not a single determined homeomorphism; it supplies no automatic current evolution.

Ledger Q166/Q167/Q170 define native oriented support currents and stock balances under stated carrier ownership. Those identities can test continuity once a carrier map and face measure are given. They do not specify the cube, pick one source vertex, or select a Euclidean target-isometry representation. The current six-sector map therefore has an unprovided symmetry-breaking preparation or boundary condition. Full `S4` invariance of an unconditioned packet does not select its corner-star density contrast.

The exact replay `python3 experiments/geometry-s4-selection/replay.py` enumerates isometries, star and alternating-tetra stabilizers, squared distances, and the inversion average. No measured angle, friction, load response, parameter fit, or physical constant enters. The next gate is an actual packet-level selector (e.g. sourced boundary/contact state) that yields one of these geometry maps, a law for induced face density/current, and an observable distinction from the symmetric mixture.
