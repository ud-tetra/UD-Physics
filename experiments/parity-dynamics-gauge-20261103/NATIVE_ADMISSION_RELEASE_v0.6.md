# UD native admission and release: reciprocal-port selector test v0.6

**2026-11-03 — Discovery / EXACT-CONDITIONAL + NO-GO + OPEN / physical promotion 0.** Existing claim: `refs/heads/claims/parity-dynamics-gauge-20261103` HELD at `d0950c1c5376a31b483908c819123914ae59c404`; session `pdyg-20261103-01`; isolated discovery branch; PR #284. No mainline export.

## 1. Sources, types, and missing bridge

Primary exact source is `experiments/qpb1-source-reservoir/README.md` **v1.1 §§1–5**, whose real 15-dimensional filled-K4 carrier has `A=d-dᵀ`, `J=A/2`, active top-cell modal embedding `E:R²→R15`, and a *separate real two-coordinate reservoir* `y`. A declared matched-source coupling is
```
G_g = [ A     gE ; -gEᵀ   2j ],      j=[0,-1;1,0].
```
The source explicitly leaves the coupling strength, source preparation, and turn-off rule unselected. Native parameter `u` is dimensionless; metric is unit Euclidean for both modal and reservoir coordinates. The source's `E` is a top-cell *embedding*, not the edge extractor `E_edge` in the prior parity observer. Keep the two typed E operators distinct.

Second read-only source: imported UD coefficient ledger v0.39 Q170–Q179 (exact glued simplicial current and equal-share cell stocks), G05 (physical action weighting OPEN). Its 1→4 carrier has 29 real simplex coordinates. **Do not** identify the 29D cell-owned support `S_tau` or candidate `r_tau` with the 15D QPB1 source's two real modal coordinates `r=Eᵀx` or two reservoir coordinates `y`. A cross-carrier map is OPEN.

## 2. Exact reciprocal dynamics

For a constant source coupling `g∈[0,2)`, the joint generator is skew in the declared metric, so `N=||x||²+||y||²` is conserved. In the matched rotating frame, with addressed old target `r0` and incoming source `y0`:
```
r(u)=R(2u)[cos(g u) r0 + sin(g u) y0],
y(u)=R(2u)[-sin(g u) r0 + cos(g u) y0].
```
The internal rotation R preserves squared norms. For empty target `r0=0`, unit source `||y0||²=1`, target and reservoir support are exactly `sin²(gu)` and `cos²(gu)`. No physical clock, source action quantum, mass or particle quantity follows.

## 3. Independent choices admitted by all existing equations

Fix `g=1` (one permitted *test value*, not sourced universal constant), `r0=0`, `y0=(1,0)`, and evaluate three controls under identical preparation:
- **Null control**: `g(u)=0`. The target remains empty, source support 1.
- **Reciprocal release**: `g(u)=1` forever. Target support `sin²u`: zero at u=0, full at π/2, back to zero at π, and full again at 3π/2.
- **Switched-off latch (CANDIDATE)**: `g(u)=1` for `0≤u<π/2` and `g(u)=0` afterward. Target support remains 1 after π/2 because its uncoupled modal rotation preserves its own norm. **The switching command and its timing are additional constitutive inputs.** No independent source derives the command.

All three obey the same joint native conservation law, and the active source coupling is local and S4-compatible given the matching reservoir sign representation. Thus **NO-GO under source constraints alone:** conservation, K4 symmetry, modal locality and transport cannot uniquely select no transfer, continued exchange, or retained transfer.

## 4. Zero-current selection counterexample

For the prepared empty target, the support current into the target is
```
j_target(u)= d( sin²u )/du = 2sin u cos u = sin(2u).
```
It vanishes both at `u=0` (target empty) and at `u=π/2` (target full). A predicate `j_target=0` alone cannot select the retained state. Adding “positive target stock” plus the direction of first crossing and a one-way turn-off latch constitutes an added controller and history law, not a consequence of the source's antisymmetric generator. Initial phase also matters: old target `r0=y0` produces target norm 2 at `u=π/4`, while `r0=-y0` gives target norm 0 at the same `u`. A current-crossing selector would need to specify preparation, phase and admissible exclusions before any prediction.

## 5. Exact linear autonomous attraction obstruction

Suppose the whole joint state evolves under a **fixed** skew-adjoint matrix G and the unit metric. Then `exp(uG)` is an isometry: for any two initial states z1,z2, their distance remains `||z1-z2||`. Therefore no distinct open set of initial joint states can asymptotically converge onto a single retained state. This **NO-GO** applies only to fixed skew-adjoint linear flows with the full-state metric; nonlinear state-dependent feedback, open systems, projections or externally controlled envelopes change the hypotheses. Single-state periodic occupancy is allowed; *attraction* is not.

## 6. Q170–Q179 stock receipts and constitutive frontier

On the separate 29D 1→4 support carrier, Q177–Q179 fix `w_(sigma,tau)=1/n3(sigma)` for each incident maximal tetra and `S_tau=Σ_sigma w_(sigma,tau)c_sigma²`. For **any assumed** event transfer `δ_sigma∈[0,c_sigma²]`, adding a retained bookkeeping stock `r_tau'=r_tau+w_(sigma,tau)δ_sigma` and decrementing circulating `c_sigma²` by δ gives exact per-cell stock conservation. The reciprocal 17D source model shows how reversible transfer can happen without a destructive change of the original total norm; **it does not** source the 29D event transfer δ or an interface between the two spaces. The 29D model's release channel and environmental source/renewal are OPEN.

**Result:** No parameter-free, autonomous, persistent retained-state selector follows from Q170–Q179 plus the existing matched reciprocal port. A candidate event latch can be written and tested, but must be labeled HYPOTHESIS and requires an independent threshold/clock/preparation/controller and exact reservoir/stock receipt before any dynamical promotion.

## 7. Reproduce and governance

Execute `python3 experiments/parity-dynamics-gauge-20261103/reciprocal_gate_v06.py` (stdlib `fractions.Fraction`), compare `reciprocal_gate_v06.results.json`. Verify orthogonal 2×2 rational exchange fixtures, the seven exact trigonometric squared-support endpoints, phase-collision counterexamples, the null/latch/release difference, and algebraic conservation. Constructor exact replay PASS locally; independent non-constructor review NOT_RUN. No empirical target/fitting; illustrative coupling and off-command deliberately selected after exploring the model, not preregistered physical laws.

**Decision:** Retain source-native QPB1 reversible port as EXACT/CONDITIONAL within v1.1. Preserve Q170–Q179 support-current exactness. AUTO_FREEZE claims of autonomously selected irreversible matter, uniquely forced latch, physical time, or cross-carrier equivalence on these sources. Next: recover a source-accepted state-dependent gating mechanism and verify it against both null and reversible controls without importing an arbitrary one-way rule.
