# A full S4-equivariant, volume-preserving tetrahedron-to-cube map

**Status:** EXACT Euclidean/simplicial existence construction and CONDITIONAL measure/current transfer. The map is selected by us, not by a native UD law; no physical promotion, friction prediction or independent physics review.

## Definitions and triangulation

Let a regular tetrahedron of edge `a` have source vertices `v0,v1,v2,v3`; use standard affine coordinates `v0=000,v1=100,v2=010,v3=001`. Its physical edge-basis determinant is `a³/sqrt(2)` and volume `a³/(6sqrt(2))`. Let `fi` be the barycenter of the triangular face opposite `vi`, and `g` the tetrahedron centroid. This gives nine source vertices.

Let the cube have edge `b=(sqrt(2)/12)^(1/3)a`, equal bulk volume. Assign the original four source vertices to alternating cube corners

`e0=000, e1=011, e2=101, e3=110`,

the face centers `fi` to `oi=111-ei`, and `g` to the cube center `c=(1/2,1/2,1/2)`. Each odd corner `oi` is adjacent to the **three** even corners corresponding to the vertices of the opposite tetrahedral face. Triangulate each original face into three triangles `[fi,vj,vk]` with `j,k != i`, and cone all 12 boundary triangles to `g`. Map corresponding labeled vertices and extend affinely over each of the 12 cells. This maps each boundary triangle onto half of one square cube face; two triangles tile each of the six faces. The interiors of the cells tile the cube by coning its triangulated boundary to `c`, so the result is a piecewise-affine homeomorphism.

Every source cell has coordinate volume `1/72`, one twelfth of the standard simplex volume `1/6`. Every cube cell has coordinate volume `1/12`. Their coordinate Jacobian is positive `6` with the consistent physical orientation. Since `b³=a³/(6sqrt(2))`, the physical Jacobian is **exactly 1 in each cell**. The common abstract complex has `f=(9,26,30,12)` and an oriented cell sum with 12 external triangles; internal faces cancel and `∂²=0`. The vertex-defined simplicial chain map obeys `∂F#=F#∂`.

## Equivariance and boundary measure

The cube isometry group stabilizing the alternating four-corner set has order 24. Each source vertex permutation `p∈S4` matches exactly one of those isometries `R_p`. Because `oi` is the complement of `ei`, `R_p` also sends `oi` to `o_{p(i)}` and fixes the cube center. It permutes the 12 simplicial cells. Affine extension therefore gives **full equivariance** `F(p·x)=R_p·F(x)` on every point. The map is not an isometry of the source and target solids: it preserves selected symmetry actions and volume, while changing local lengths and surface area.

Each tetrahedral face has area `sqrt(3)a²/4`; its three equal subtriangles each have area `sqrt(3)a²/12`. Each maps to half a cube face, area `b²/2`. Therefore the induced cube boundary density from a source-uniform surface density `σ_t` is **uniform**:

`σ_c/σ_t = sqrt(3)a²/(6b²) = 3^(1/6)`.

This is the reciprocal of the equal-volume total surface ratio `S_cube/S_tet=3^(-1/6)`. It preserves total boundary stock; the earlier [rooted six-sector map](../geometry-six-sector-map/README.md) preserved that stock with a 3:1 *nonuniform* density instead. Standard change of variables with physical `J=1` preserves volume stock, and the cellwise Piola pushforward `j_c(Fx)=DF_x j_t(x)/J` preserves weak continuity and total oriented normal flux when a source current is specified. Neither construction derives that current.

## Scope, source relationship, and next gate

This construction resolves the **existence** question left by the [star-map symmetry audit](../geometry-s4-selection/README.md): the order-six stabilizer was specific to its distinguished-corner image. It also shows that the 3:1 induced boundary-density pattern is not forced by tetrahedron-to-cube topology, equal volume, or full native `S4` symmetry. The uniform factor `3^(1/6)` is an exact normalization under *this* equal-volume measure correspondence, not a dynamical coefficient.

`replay.py` checks the 12 rational cell determinants, oriented boundary cancellation, face tiling, and all 24 matching isometries. The shape/triangulation and regular Euclidean target are chosen after the user's triangle/square analogy, not derived from UD packet rules. The supplied ledger v0.39(2) P03 gives the native `S4` group; Q166/Q167/Q170 give typed native support currents/stocks. They do not select a cubical embedding or identify packet stock with Euclidean area. The next test must define a native map or selection functional that distinguishes this symmetric map from the rooted construction or their mixtures, and a measurable response tied to that selection. No graphite twist-angle, damping, or force/load conclusion follows from this geometry alone.
