# An explicit six-sector tetrahedron-to-cube map

**Status:** EXACT simplicial/Euclidean construction; CONDITIONAL measure and flux transport; HYPOTHESIS as a UD physical bridge. No graphite prediction, material law, physical clock, or mainline promotion. Independent physics review NOT_RUN.

## Carrier and map

Use the standard 3-simplex `Δ={(x1,x2,x3): xi>=0, x1+x2+x3<=1}` as affine coordinates for a regular Euclidean tetrahedron of edge `a`. Its physical edge-basis determinant is `a³/sqrt(2)` and its volume is `a³/(6sqrt(2))`. The target cube `[0,b]^3` has edge `b=(sqrt(2)/12)^(1/3)a`, so it has the **same bulk volume**. The map is introduced by construction, not selected by a native packet update.

For each subset `S⊆{1,2,3}`, put a source vertex at `v_S=1_S/|S|` when `S` is nonempty, `v_empty=0`; put its target at `w_S=1_S`. For each permutation `(i,j,k)`, take the oriented tetrahedral sector

`[v_empty, v_{i}, v_{i,j}, v_{i,j,k}] -> [w_empty, w_{i}, w_{i,j}, w_{i,j,k}]`.

There are six sectors. On each sector, extend the vertex assignment affinely. They agree on common faces, producing a continuous piecewise-affine homeomorphism `F:Δ→[0,1]^3` in cube edge units. In the chamber `xi>=xj>=xk`, the explicit formula in coordinate order `(i,j,k)` is

`u_i=xi+xj+xk`, `u_j=2xj+xk`, `u_k=3xk`.

It has positive determinant `6` on every chamber; each source sector has coordinate volume `1/36`, and each cube sector volume `1/6`. After embedding the source as a regular tetrahedron and scaling the cube to equal volume, the **physical** determinant is exactly `1` on every sector. A uniform bulk density consequently has equal total stock in source and target under this chosen map. The local metric is anisotropically distorted despite the unit volume Jacobian.

## Boundary and current

The two triangulations use the same eight Boolean-lattice vertices, 19 edges, 18 triangles, and six tetrahedra. Their oriented simplicial chain map sends each labeled simplex to its corresponding target simplex; hence `∂F_#=F_#∂` in every degree. The signed sum of the six positively oriented cells has 12 exterior triangles and six interior triangles paired with opposite signs; `∂²=0`. Three original faces `xi=0` each map to one zero-coordinate cube face (two triangles). The remaining original face `x1+x2+x3=1` maps onto **three** unit-coordinate cube faces (six triangles). Thus this is not a face-to-face one-triangle-to-one-square correspondence.

For a physical bulk density `ρ_t`, define `ρ_c(Fx)=ρ_t(x)/J(x)`, with `J=det DF=1`. For a source vector current `j_t`, define its Piola pushforward `j_c(Fx)=DF_x j_t(x)/J(x)` on each cell. Change of variables and the oriented surface element give `∫cube ρ_c dV=∫tet ρ_t dV` and `∫∂cube j_c·n_c dA_c=∫∂tet j_t·n_t dA_t`. The weak continuity equation is preserved if the source has one; across an interior sector face, transformed normal currents cancel. This is a conditional conservation construction, not a law selecting `ρ_t` or `j_t`.

The [prior equal-measure audit](../geometry-equal-measure/README.md) gives `S_cube/S_tet=3^(-1/6)` at this volume. An **equal numerical surface density** on the two surfaces therefore does *not* preserve total boundary stock. A source-uniform boundary density `σ_t`, pushed forward as an area measure, produces the following target densities:

| Target region | Original source face(s) | `σ_c/σ_t` |
| --- | --- | --- |
| Three faces `u_i=0` | Each one `xi=0` triangle | `(3/2)3^(1/6)` |
| Three faces `u_i=1` | Six pieces of the one opposite tetrahedral face | `(1/2)3^(1/6)` |
| Uniform target density matching **only total stock** | Global average, not the local pushforward | `3^(1/6)` |

These densities preserve the source boundary stock without a source or sink; the local values differ by a factor of three. The earlier `1-3^(-1/6)` is a deficit **only under the extra requirement that numerical boundary density stay the same**. Geometry alone imposes no lost stock. If one proposes a UD boundary coefficient, one must specify which surface-density or flux transformation is physically selected, and why.

## Evidence and next gate

`replay.py` uses rational coordinates and integer oriented incidence to check the six local determinants, `f=(8,19,18,6)`, 12 exterior triangles, 6 paired interior triangles, `∂²=0`, and the boundary grouping. The chain statement follows directly from the common labeled simplicial complex; the program enumerates it. The surface density ratios are exact Euclidean area calculations in the stated equal-volume embedding. No physical observations or fitted values enter; regular tetrahedron, cube, equal volume, and this particular Boolean-lattice map were chosen after the user's geometry prompt.

This map is a **constructive existence proof**, not a unique UD map. A nonlinear map, different triangulation, boundary ownership rule, or source-selected metric changes the local transport. The discriminant is whether current UD packet/face primitives can select this map and its boundary pullback without imported geometric preference, then yield an observable beyond the Euclidean baseline. The relevant provenance ledger v0.39(2) F03/F04, Q166/Q167/Q170 concerns other typed objects and native support continuity; none specifies this tetrahedron-to-cube identification.
