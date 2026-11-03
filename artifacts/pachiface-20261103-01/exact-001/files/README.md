# Pachner local interface and memory audit v0.1

**2026-11-03 — development, no registry entry; physical promotion 0.** Base `6c9f3b855169448d224d7c9f9badee02d4d5a1e3`. This follows the [exact switch ledger](../pachner-switch-ledger/README.md) and its source-bound chain maps. The supplied *UD coefficient provenance ledger v0.39(2)*, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q165/Q169/Q170/Q173/Q177–Q179, defines fixed-complex stock, skew incidence flow, control-volume continuity, hard face gating and cell ownership. None of those entries defines a Pachner-event trigger, event support source, memory dynamics, or physical time/charge. This note tests what an additional event interface **must** account for; it does not import those missing rules.

## State, map and exact event receipts

Let `K_old,K_new` be the previously snapped finite balls, `V_K=⊕_(k=0)^3 C_k(K;Q)` with ascending oriented simplex bases, unit coefficient metric and `S_K(c)=cᵀc` in native squared-amplitude units. The previously fixed full-symmetry chain map is `M:V_old→V_new`. At a **prescribed** event, `c⁺=Mc⁻`. Before and after an event the only sourced generator is `A_K=B_K−B_Kᵀ`; its formal parameter has no seconds map. The 1→4 map is injective; the 2→3 map has a two-dimensional kernel.

For 2→3 denote the old internal-face amplitude by `x`. Let `y` be the six old oriented outer-cap face amplitudes; let `b_i=±1/2` be the exact coefficients of that face's image on these six caps, so `bᵀb=3/2`, and put `z=bᵀy`. Write `u,d` for the two old *geometrically oriented* top amplitudes, i.e. old ascending-basis coordinates are `u,−d` in this snapped bipyramid. The map sends outer-cap amplitudes to `y+bx` and both top amplitudes to one half of the three-cell geometric fundamental chain, giving top output stock `3(u+d)²/4`.

The event changes **outer-cap face stock**, a precisely defined shell readout, by

`J_shell^event=||y+bx||²−||y||²=2xz+(3/2)x²`.

This is an exact jump receipt, **not** a Q170 flow integrated over time. It can have either sign: `x=1,y=0` yields `+3/2`, while `x=1,y=−b` yields `−3/2`. Every old boundary-face *basis vector* remains fixed under `M`, yet a general internal-face amplitude changes the shell state. A demand that all shell amplitudes remain identical restricts `x=0` for this map. Q170 by itself does not identify the event jump as an external flux rather than a local source or a readout change.

## Minimal kernel record and positive support obligation

Let `P` be the unit-metric orthogonal projector onto `ker M` in `V_old`. In the face coordinates its basis vector is `v_f=(−b,1)` with norm squared `5/2`; in geometrically oriented top coordinates its basis vector is `v_t=(1,−1)` with norm squared `2`. Thus, writing the old vector in the corresponding blocks,

`P_f c=[(2/5)(x−z)]v_f`, and `P_t c=[(u−d)/2]v_t`.

The carried memory `k=Pc` has exactly two independent amplitudes and stock

`S_mem=||Pc||²=(2/5)(x−z)²+(u−d)²/2`.

**EXACT, conditional on retaining this new memory carrier:** The event map `c↦(Mc,Pc)` is injective (`rank=23`) and its total stock gain is a sum of two nonnegative rational squares:

`G(c)=||Mc||²+||Pc||²−||c||²=(3x+2z)²/10+(u+d)²/4 ≥ 0`.

For 1→4, no memory is required and `G(c)=3a²` for old top amplitude `a`. On 2→3 the positive quadratic port rank is **2**, and linear memory dimension is at least **2**, under the fixed map and injective linear record requirement. The factorization above uses the **assumed** positive rational port metric `diag(1/10,1/4)` on amplitudes `(3x+2z,u+d)`; it is an exact identity derived from the unit simplex metric, not a source-selected extra simplex or a physical material metric. An equivalent real unit-port expression uses `(3x+2z)/√10,(u+d)/2`. The recorded memory transforms covariantly under all 12 geometric automorphisms; `P` and the gain form commute with their signed simplex actions.

**CANDIDATE admission only:** If an auxiliary nonnegative stock `R` exists, take `R⁺=R⁻−G(c⁻)` and admit the prescribed event when `R⁻≥G(c⁻)`. Then `S_old(c⁻)+R⁻=S_new(c⁺)+S_mem(k⁺)+R⁺`. The reserve has the same declared native stock unit, but its location, generator, replenishment, coupling, and actual transfer are **OPEN**. This inequality is a necessary budget check for this proposal, not a trigger predicting when a move occurs. It admits a continuum of possible event schedules. No event rate or energy conversion follows.

| Old input | Old `S` | New `S` | Memory `S` | `G` | Shell receipt |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2→3 `u=d=1`, `x=y=0` | 2 | 3 | 0 | 1 | 0 |
| 2→3 `u=1,d=−1`, `x=y=0` | 2 | 0 | 2 | 0 | 0 |
| 2→3 `x=1,y=0,u=d=0` | 1 | 3/2 | 2/5 | 9/10 | 3/2 |
| 2→3 `x=1,y=−b,u=d=0` | 5/2 | 0 | 5/2 | 0 | −3/2 |
| 1→4 `a=1` | 1 | 4 | 0 | 3 | 0 |

## Dynamical obstruction and source-selection result

The event inverse exists **on the image** of `(M,P)` with the memory and reserve receipt. This does not establish reversible *post-event dynamics*. Holding memory constant and evolving the new simplex state with the sourced `A_new`, the tangent image of the 23-dimensional event manifold has rank **29** after adding its target-flow directions. It is therefore not invariant under that uncoupled generator. A memory generator/coupling, a restricted admissible state manifold, or a different transport is required for persistence. `A_new M≠M A_old` was already established in the prior audit.

**NO-GO / source scope:** Q165/Q169/Q170/Q173/Q177–Q179 fix flows and ownership *on declared complexes*, and Q173 gates an existing face coupling. They do not provide a transition between complexes, choose a time for it, or allocate a new reservoir at a change of simplex dimension. The budget inequality, even with symmetry and locality on one Pachner ball, leaves the event schedule arbitrary. A genuine predictive switch needs an independently sourced trigger, auxiliary carrier state and update, event support-current attribution across the control volume, and a memory evolution rule. Until those are specified, the event interface is an exact **conditional construction**, not UD dynamics or a charge/energy mechanism. Physical promotion 0; nonconstructor review NOT_RUN.

Run `python3 experiments/pachner-interface-defect/audit.py`. It imports the prior exact maps, checks rational matrix identities `P²=P`, `MP=0`, rank/injectivity, the two-port Gram identity, all 12 symmetry actions, four input receipts and the target-flow tangency rank. The [exact output](results.json), [receipt](../../candidates/pachner-interface-defect/mathematical_receipt.json) and immutable run capture record assumptions and hashes. The next discriminant is a source or explicitly new axiom that couples this two-mode memory and reserve to the fixed-complex generator and selects the switch, followed by a held-out boundary readout with a conventional baseline.
