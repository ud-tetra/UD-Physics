# Equal-measure triangle/square and tetrahedron/cube geometry

**Status:** EXACT Euclidean geometry under declared regular-shape and equal-measure conventions; HYPOTHESIS as a UD map. Physical promotion 0; independent review NOT_RUN.

## Question and source

The user supplied three frames of a four-piece hinged triangle-to-square rearrangement. Those frames motivate an equal-area condition but do not establish the cut coordinates, continuous hinge path, or a three-dimensional transformation. This note uses no geometric measurements extracted from the images. The supplied coefficient ledger v0.39(2), F03 and F04, already assigns typed tetrahedral coframe and center factors 4/3 and 3/4; the ratios below are different objects. The existing [center-split tetrahedron](../four-cell-tetrahedron/README.md) has four equal-volume **nonregular** children, so its factor 1/4 is also distinct.

Let `a>0` be the edge length of a regular equilateral triangle or regular tetrahedron. Let `b>0` be the edge of a square or cube, respectively, in ordinary Euclidean length. The shape maps and equalities below are separately chosen constraints. No packet clock, simplicial boundary map, physical length unit, or transport law is inferred.

## Typed exact ratios

| Object | Declared equality | Exact `b/a` | Approximation | Scope |
| --- | --- | --- | ---: | --- |
| `g_A`, face-to-face | equilateral triangle area `sqrt(3)a²/4 = b²` | `3^(1/4)/2` | 0.658037006476 | one triangle and one square |
| `g_S`, total boundary | tetrahedron surface `sqrt(3)a² = 6b²` | `sqrt(sqrt(3)/6)` | 0.537284965912 | all four triangular and six square faces |
| `g_V`, bulk | tetrahedron volume `sqrt(2)a³/12 = b³` | `(sqrt(2)/12)^(1/3)` | 0.490280458905 | Euclidean enclosed volume |

If equal volume sets `b/a=g_V`, the cube's total surface relative to the tetrahedron is

`rho_S = S_cube/S_tet = 6 g_V²/sqrt(3) = 3^(-1/6) = 0.832683177656...`.

The tetrahedral boundary area exceeds the equal-volume cube boundary by the ratio `3^(1/6)`. The two edge calibrations differ by `g_S/g_V = 3^(1/12) = 1.095872691135...`. Thus **no single positive edge scale** preserves both total boundary area and bulk volume for these two regular solids. Proof: equality of both demands `g_S=g_V`, but their quotient is `3^(1/12)≠1`. Equivalently, the scale-free shape index `S³/V²` is `sqrt(3)` times greater for the regular tetrahedron than for the cube. The statement holds for regular shapes with the stated Euclidean measures; it says nothing about a piecewise nonsimilar image, a non-Euclidean effective metric, or added boundary stock.

Facewise equal area would make the cube's six-face total surface `3/2` the tetrahedron's four-face total. It is a different constraint from `g_S`. The 2D four-piece rearrangement preserves total area while allowing perimeter to change; the pictures do not give a 3D hinged tetrahedron-to-cube dissection.

## Interpretation and coefficient gate

`g_A`, `g_S`, and `g_V` are exact dimensionless **conversion factors** after choosing source and target regular shapes and a conserved measure. The scale-free mismatch `rho_S` is the cleanest shape diagnostic. Each is a candidate derived-geometric ledger object, not an automatically active UD dynamics coefficient. Equal-volume calibration gives a unit Jacobian for the *total bulk measure* by construction; it does not define a map of interior points, faces, currents, or energies.

To promote a physical use, specify (1) an actual UD carrier and map `T` from tetrahedral states/geometry to cubic readout; (2) the pulled-back metric and measure; (3) what is conserved, including surface reservoirs or a boundary term; (4) a source-selected update/transport law and physical units; and (5) a consequence that changes when the mapping is changed. One testable conditional budget is `J_boundary = 1-rho_S = 1-3^(-1/6)` when **equal bulk volume and a unit reference boundary stock per tetrahedral surface area are independently assumed**. This is a dimensionless geometric shortfall, not an observed flux, friction, or universal coupling. Its sign and dynamics must come from a constitutive law.

The baseline is elementary Euclidean geometry. No fit or empirical data enter the identities. The shape choice came from the user's exposed prompt; the exercise provides no independent prediction for the graphite twist angles or load response. A relevant next discriminant is to build one explicit simplicial-to-cubical chain/measure map and test boundary commutation plus stock continuity. Until such a map exists, keep `rho_S` and the three `g` factors as scoped geometry rather than assign a canonical UD coefficient ID.

Run `python3 experiments/geometry-equal-measure/replay.py` for independent floating-point checks of the exact algebra. See the candidate mathematical receipt and immutable capture for provenance.
