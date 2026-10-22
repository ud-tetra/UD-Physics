# K5 vertex graph, four tetrahedral cells — v1.0

Status: EXACT finite-complex analysis; CONDITIONAL unit-metric dynamics; hypothetical physical use remains OPEN.

## Reading the supplied sketch

The user's IMG_0030.jpeg labels the common vertex v0 and four outer vertices v1,v2,v3,v4. Its cells, using ascending orientation, are:

| Drawn cell | Tetrahedron | Exterior triangle |
| --- | --- | --- |
| Cell 1 | [0123] | [123] |
| Cell 2 | [0124] | [124] |
| Cell 3 | [0134] | [134] |
| Cell 4 | [0234] | [234] |

Repeated labels identify the same vertices across drawings; the location of v0 inside each projected triangle is a drawing convention. It is not a separate vertex in each cell. A geometric centre/centroid interpretation is an additional realization, not information supplied by the graph alone. The photo is not republished; the session records its digest and this selected mathematical transcription.

The previous analysis used centre vertex 4 and outer vertices 0,1,2,3. The relabelling old (0,1,2,3,4) -> new (1,2,3,4,0) gives exactly this complex. No construction has changed.

## Three graph descriptions, different objects

The primal vertex-edge graph is K5: all 10 pairs of the 5 vertices are edges. Its edges split into 6 outer edges and 4 spokes from v0.

The internal cell-adjacency graph is K4: each of the four cells shares one triangle with every other cell. The interfaces are:

| Cell pair | Shared triangle |
| --- | --- |
| 1,2 | [012] |
| 1,3 | [013] |
| 1,4 | [023] |
| 2,3 | [014] |
| 2,4 | [024] |
| 3,4 | [034] |

If an exterior region is added as a fifth dual node, one exterior face per cell gives four more adjacency edges. The exterior-augmented dual is also K5. Its nodes represent regions/cells; primal K5 nodes represent vertices. A graph isomorphism does not identify these state spaces, signs, metrics or boundary laws.

## The missing-facet identity

Let T=[1234] and K=0*boundary(T), the cone on the tetrahedral shell. As a simplicial complex,

$$K=\partial\Delta^4\setminus\{[1234]\}.$$

Here removal deletes only the open tetrahedral facet; all its proper faces remain. Equivalently the realization is the 4-simplex boundary with one open facet removed, a closed 3-ball. It has a 3D filling realization with v0 inside T. The single tetrahedron T and the four cells of K have the same boundary. They are the complementary one-cell and four-cell sides of the 1<->4 move.

For ascending chain orientations,

$$\partial[01234]=[1234]-[0234]+[0134]-[0124]+[0123].$$

Consequently the coherently oriented four-cell chain

$$c_K=[0234]-[0134]+[0124]-[0123]$$

satisfies exactly

$$\partial c_K=\partial[1234].$$

Adding the abstract missing tetrahedral facet along that shell produces the full boundary of a 4-simplex, a triangulated 3-sphere. This is a different complex from the four-cell ball. In the centre-insertion realization in R3, a straight tetrahedron [1234] already occupies the entire parent volume: it overlaps the four existing cells. It cannot be added as a fifth disjoint straight tetrahedron in that realization. The abstract closed 3-sphere is naturally realized as a 4D simplex boundary; this does not imply physical 4D spacetime.

## Same graph, distinct topology and state spaces

| Specified filled structure | Face vector, including top cells | Chain dimension | Betti numbers over Q |
| --- | --- | --- | --- |
| K5 graph only | (5,10) | 15 | (1,6) |
| Drawn four-cell ball K | (5,10,10,4) | 29 | (1,0,0,0) |
| Closed boundary of a 4-simplex | (5,10,10,5) | 30 | (1,0,0,1) |
| Filled 4-simplex | (5,10,10,5,1) | 31 | (1,0,0,0,0) |

Every row has exactly the same vertex-edge graph K5. Graph connectivity alone therefore selects neither dimension, topology, filled cells nor dynamics. In particular, taking the flag/clique completion of K5 would fill the entire 4-simplex; that completion is an extra rule and does not describe the drawing's four-cell structure.

All 10 possible triangles are already present in K. What is absent is one tetrahedron, not an edge or triangle. Vertex v0 belongs to all four cells; each other vertex belongs to three. Thus the abstract K5 graph has 120 vertex permutations, but the filled four-cell complex has only the 24 permutations fixing v0. The full S5 symmetry of the abstract five-facet boundary is not inherited by the centre-selected ball. Geometry/weights can reduce these combinatorial symmetries further.

The supplied historical Coefficient Provenance Ledger v0.39, Q107, records (5,10,10,5) under f(Delta4). Those four entries are the vertex-through-tetrahedron counts of the 4-simplex boundary; the filled 4-simplex additionally has one 4-cell. This report distinguishes those objects without editing the historical entry or importing its physical status. Q108's S5-based ratio cannot be transferred to the centre-selected ball solely from its K5 graph.

## Conditional dynamical consequence

For each specified complex take real chain coordinates, unit metric H=I, ascending oriented incidence matrices B_k, and the skew generator with upper adjacent-grade block B_k and lower block -B_k^T. Evolution is dz/du=A z with arbitrary real initial state and dimensionless parameter u. No boundary forcing or physical unit map is imposed; norm-squared is conserved by skewness. Distinct complexes below define distinct model boundary closures.

The previous full four-cell model has

$$\chi_{A_K}(\lambda)=\lambda(\lambda^2+1)(\lambda^2+5)^{13}.$$

For the closed five-cell boundary the exact result becomes

$$\chi_{A_{\partial\Delta^4}}(\lambda)=\lambda^2(\lambda^2+5)^{14}.$$

The additional tetrahedron introduces one new chain coordinate and changes the operator: the active frequency 1 disappears, sqrt(5) remains, and the second zero mode is the oriented top-dimensional cycle. With this chosen metric the closed model has a universal model return time 2*pi/sqrt(5), whereas the four-cell model's two irrationally related frequency families have no universal nonzero return time. This is a boundary-closure effect within the assumed model, not a physical clock prediction.

The executable certificate verifies M=-A^2, M^2=5M, rank(M)=28 on the closed boundary. Since M is symmetric, its eigenvalues are 0 and 5 with multiplicities 2 and 28. Real skew eigenvalues pair, proving the stated characteristic polynomial. For comparison the filled 4-simplex gives lambda*(lambda^2+5)^15. No spectrum follows from a bare K5 label without selecting chain spaces and operator conventions.

## Verification, provenance and next question

Run `python3 experiments/k5-four-cell/analyze.py`. It uses integer incidence matrices and rational elimination to verify all face counts, boundary composition, field Betti numbers, sharing, all 120 candidate vertex permutations, the oriented cycle identity and closed-model spectral certificates. This is constructor verification with an explicit proof/certificate, not independent replication. No empirical targets, fitted coefficients or modular clock have been used.

The finite combinatorics agrees with CGAL's primary triangulation-data-structure description: the minimal closed 3D simplicial triangulation is a 4-simplex boundary with five vertices. Its discussion also distinguishes combinatorial structure from a geometric embedding:
https://graphics.stanford.edu/courses/cs368-00-spring/TA/manuals/CGAL/ref-manual2/Triangulation3/Chapter_TDS3.html (Degenerate Dimensions; Software Design).

See [previous four-cell analysis](../four-cell-tetrahedron/README.md) for geometry, recursion and parent/relative chain duality. See [candidate](../../candidates/k5-four-cell/candidate.json) for evidence scope.

HYPOTHESIS: K5 provides a common connectivity scaffold for comparing an open tetrahedral block, its environment and a closed cell model. OPEN: which boundary/readout and coupling law represents the intended UD system. Next discriminant: derive the boundary-driven four-cell response and compare it with the explicit fifth-cell closure under one fixed readout and metric. This would distinguish connectivity resemblance from a useful coarse-grained dynamical equivalence.
