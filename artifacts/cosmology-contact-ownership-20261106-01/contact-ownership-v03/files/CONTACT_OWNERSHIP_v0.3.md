# Glued 1→4 contact and ownership obstruction v0.3

Session `cosmology-contact-ownership-20261106-01`; base `ud-tetra/UD-Physics@2ed0e784af4d1836fc03cba41443fee69b3e5b11`. **EXACT conditional / NO-GO scoped / CANDIDATE repair.** Physical promotion 0. This extends the [v0.2 filtration test](REFINEMENT_DYNAMICS_v0.2.md) to a genuine glued interface.

## Source and objects

Ledger `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165, Q169, Q177–Q179, gives unit fixed-complex quadratic support, numerical skew incidence `A=D−Dᵀ`, and equal ownership `w_(σ,τ)=1/n₃(σ)` for each containing top cell. `experiments/pachner-state-transport/README.md` v0.1 §1→4 gives the integral degree-one map fixing old vertices, edges and faces and mapping an old top tetrahedron to four signed children. The [v2.1 source-selection audit](../cosmology-galactic-entry/G0_OPERATOR_RECOVERY_v0.1.md) finds no selected newborn contact/metric.

Let old cells be `T₀=0123` and `T₁=0125`, sharing face `012`. Refine only `T₀` with centroid vertex `4`, producing four children and leaving `T₁` unchanged. The carrier is a finite pure tetrahedral complex before and after. Put amplitude 1 on shared vertex `0`, zero elsewhere. This is a fixed initial state, not a material source or physical mass.

## Exact local obstruction

Before refinement `n₃^old(0)=2`, so the Q177 cell supports are `(s_T0,s_T1)=(1/2,1/2)`. After refinement vertex 0 belongs to three children of `T₀` and to `T₁`: `n₃^new(0)=4`. The three incident children receive `1/4` each, the fourth receives 0, and `T₁` receives `1/4`. On grouping children by old parent, `(s_children,s_T1)=(3/4,1/4)`. Both totals equal 1; the state is unchanged on the vertex under the source chain map.

**NO-GO under Q177 on both carriers, fixed vertex amplitude and local 1→4 transport:** equal current-incidence ownership is incompatible with preserving each old parent's support across this glued move. A quotient that merely sums all children does not repair the neighbor's loss. This does not preclude changing ownership, state transport, adding a reservoir, or choosing a different observable under explicitly new assumptions.

## Conditional ancestry repair and skew compatibility

**CANDIDATE:** retain the *old* parent share `1/n₃^old(σ)` and divide it evenly among that parent's descendants containing `σ`. For vertex 0, each of three refined descendants receives `1/6`, while untouched `T₁` receives `1/2`; parent totals remain `(1/2,1/2)`. Under the declared axioms of fixed old-parent shares, no cross-parent reassignment and symmetric division among equivalent incident children, those numbers are forced. This is a history-labelled allocation, not intrinsic new-carrier Q177. It needs a persistent ancestry map and a rule when histories merge or two refinements overlap. The corresponding cellwise continuity/current law is not supplied by Q170/Q179.

Separately, the old top-unit coefficient maps to four unit top coefficients, giving unit-metric stock `1→4`. A **symmetric diagonal** changed metric that retains unit old-face weights and makes this one top map isometric assigns weight `1/4` to each child top coordinate. Across an incident face–top pair of nonzero unit Q169 incidence, `H_face=1`, `H_top=1/4` gives a skew defect `(H A+Aᵀ H)_(face,top)=±3/4`, not zero. Thus this **particular diagonal repair** cannot conserve its weighted stock under the *unchanged numerical* Q169 generator. A modified metric adjoint such as the unselected v2.1 `H_t` branch changes the generator and requires new cellwise ownership; the counterexample does not exclude such a changed-assumption construction.

**Decision:** no source-selected rule simultaneously provides intrinsic Q177 ownership, old-parent support continuity, unit top map isometry and unchanged Q169 skew flow for these tested branches. The ancestry allocation is a well-typed possible history-dependent bookkeeping rule, not an accepted constitutive contact or physical spatial metric. AUTO_FREEZE any claim that Q177 alone ensures parentwise refinement continuity; retain the exact scoped counterexample and the conditional ancestry receipt. N0 astronomical scoring stays parked; promotion 0.

Reopening requires a versioned event/history carrier and a local cross-complex current that accounts for shared-simplex ownership transfers, a positive metric and compatible generator, explicit old/new cell aggregation, boundary conditions and verification on overlapping moves. Test path independence of two move orders and a 2↔3 event before calling the rule selected; separate a physical image map thereafter.

Run `python3 experiments/cosmology-native-spatial/contact_ownership.py` for exact fractions and the diagonal skew defect. Independent algebra: count old/new incident top cells and evaluate `(HA+AᵀH)_{ij}=A_{ij}(h_i-h_j)` for a skew incidence pair. No empirical data were read.
