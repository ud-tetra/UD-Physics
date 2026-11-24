# Second-generation 16-tetrahedron Gram and native shared-face redistribution v0.1

**Exact finite model; conditional on externally prescribed second-generation 1→4 geometry; Physical Promotion = 0.**
**Source:** UD-Physics main `80525f1296a15f4a87f0efecc491679deec39b9b`, `experiments/four-cell-tetrahedron/README.md` v1.0, blob `697b5cb0207f01286e27eb8198fdb31fc129ae6e`, sections *Exact sharing, geometry and recursive counts* and *Why the full dynamics is different*. Preceding draft #477 head `f82620113a532ce88eb2408c2cab53e0efd410a2`, candidate report blob `f26afb52ee70f678d5398dfae8108b60f09ef0eb`. The user-reported 29→85 three-stage exchange is independently **not** reconstructed in this work.

## Exact geometry and Gram
Using rational vertices of regular tetrahedron, first central vertex and the four distinct second-generation tetra centroids, the complex has `(V,E,F,T)=(9,26,34,16)` and 85 total chain coordinates. With coherent ambient orientation and unit coefficient top-cell metric, `B3∈Z^(34×16)`, and `G=B3ᵀ B3=4I16−A_dual`.

Label each daughter cell `(i,j)` with parent `i∈{0,1,2,3}` and daughter `j∈{0,1,2,3}`: the four exterior cells are `(i,i)`; twelve `(i,j),i≠j` are interior. The dual adjacency has four parent-internal K4 cliques and six reciprocal inter-parent edges `(i,j)~(j,i)`. Exterior dual degree 3, interior degree 4. Thus `G·1_16=(1_4,0_12)^T` exactly: uniform all-16 top state is not an eigenvector.

`det(zI−G)=(z−6)^3(z−4)^2(z²−5z+1)(z³−11z²+35z−26)^3`.

The natural S4 permutation module of the 16 coherently oriented cell labels decomposes into `2[4] ⊕ 3[31] ⊕ [22] ⊕ [211]`. The quadratic accounts for the two trivial modes, cubic three times for the standard modes, factor `(z−4)^2` for `[22]`, and `(z−6)^3` for `[211]`. No sign irrep. All sixteen Gram eigenvalues are positive. This is a combinatorial top-chain spectrum, NOT physical excitation energies or the missing original 23-complex catalogue.

## Source-state firewall and conservative dynamics
On the already constructed complex, let `q∈R16` be signed oriented top-chain amplitudes and `f∈R34` face-chain amplitudes; declare a formal dimensionless evolution parameter s and the **unmasked** skew generator `d[f;q]/ds=[B3 q; −B3ᵀf]`, with conserved unit `||f||²+||q||²`. This generator does NOT build tetrahedra or select a 29→85 event.

The S4-fixed two-amplitude subspace has four equal exterior top amplitudes `x(s)` and twelve equal interior ones `y(s)`. At zero initial face amplitudes:
`x''=−4x+3y`, `y''=x−y`, `G_sym=[[4,-3],[-1,1]]`, `λ±=(5±√21)/2>0`, `ω±=√λ±`. Coefficient norm on the two-amplitude subspace is `4x²+12y²` (not the identity quadratic metric).

**Test 1: only four exterior top cells funded.** `x(0)=1,y(0)=0,x'(0)=y'(0)=0`. Then `y(s)=[cos(ω−s)−cos(ω+s)]/√21`, `x(s)=[(1−λ−)cos(ω−s)−(1−λ+)cos(ω+s)]/√21`. Hence interior top stock is `12y(s)²=3s⁴+O(s⁶)`; the exact total stock remains `4` when face stock is included. The bound `|y|≤2/√21` gives `S_interior≤16/7`, i.e. **≤4/7 of initial stock**. It is a sharp supremum (the frequency ratio is irrational), not an attained finite-time maximum. No total transfer of all initially available stock exclusively into interior top cells under this unmasked dynamics.

**Test 2: all sixteen initially funded uniformly.** `x(0)=y(0)=1`; interior top cells are already nonzero and `y''(0)=0`, so the starting uniform state cannot demonstrate funding of initially empty interior cells.

**NO-GO_SCOPED:** uniform top vector is not a single collective eigenmode; bare post-insertion incidence does not autonomously authorize 1→4 events, child vertices or the user-reported three-stage schedule.
**OPEN:** source-derived vertex birth, 29→85 isometric event map and funding protocol, per-event external/owned stock, future recursive transition, continuum/physical correspondence. Physical Promotion = 0.

## Verification
An independent rational-coordinate script reconstructed all 16 signed tetra-to-face columns and checked the exact 34×16 Gram against the separately constructed 16-vertex dual graph; `verify.py` captures reproducible abstract-graph/S4/ODE checks. Local full archive `UD_LEVEL2_PACHNER_GRAM_AND_FUNDING_v0.1.zip` SHA-256 `458e8e9e192c80b9bc8ab0dcaeedc33a7ecdd27d4678cf5a1faaed20d8cb4a3e`. Exact local constructor replay PASS, published GitHub script independent fresh-checkout NOT_RUN, independent scientific review NOT_RUN. No physical promotion.
