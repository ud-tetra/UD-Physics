# UD-Physics Discovery handoff v0.7 — autonomous scalar feedback

**Task:** parity-dynamics-gauge-20261103; **session:** pdyg-20261103-01; **claim:** refs/heads/claims/parity-dynamics-gauge-20261103 held SHA d0950c1c5376a31b483908c819123914ae59c404; **branch:** discovery/parity-dynamics-gauge-20261103/pdyg-20261103-01; **PR:** #284 draft. Main at this resume: d4b10ea6abeab50d5e1b74e8735fb98955c6e017; original exact base 2207611450df9106adccaf8189a50734fef5a46b. Do not merge without reconciling current main and running required integrity checks. Physical promotion 0.

## Source and typed setup

QPB1 source-reservoir `experiments/qpb1-source-reservoir/README.md` v1.1 §§1–5: real 15D filled K4 chain plus additional matched real 2D reservoir, top-mode embedding E_top; g is not selected. Original joint generator is skew under unit Euclidean metric; native evolution u dimensionless. In co-rotating addressed subspace r,y∈R2, scalar coupling has `r'=g y, y'=-g r`. No physical clock/metric/charge. The Q170–Q179 29D subdivided support carrier is a distinct typed object and no 29D-to-17D intertwiner is sourced.

## Exact result / crucial distinction

Two algebraically independent invariants hold for every scalar feedback g(r,y): `N=||r||²+||y||²` and `D=det(r,y)`. Therefore `||y||²≥D²/N`. If D≠0, **no scalar feedback can achieve complete source-to-target transfer**, no matter how its strength depends on source/current or history as a scalar multiplier of the same reciprocal port. This is a scoped no-go; nonscalar extra channels or genuinely open dynamics escape it.

The exploratory **CANDIDATE** choice `g=||y||²/N` (N>0, 0 otherwise) is S4-equivariant under the source matched sign representation and bounded in [0,1], but **not selected by UD**. With special preparation `r0=0`, `||y0||²=N`, solution is exactly `||r||²=N u²/(1+u²)`, `||y||²=N/(1+u²)`: transfer is asymptotic, not finite-time latch. At u=1,2,10 (N=1), target = 1/2, 4/5, 100/101. Generic D≠0 has nonzero source floor and persistent reciprocal circulation, hence the candidate FAILS robust all-phase retention. Controls: g=0 null, g=constant reciprocal release, externally switched latch (added controller). No physical target used/fitted; selection biased toward aligned capture, disclosed.

## Reproduction

```bash
python3 experiments/parity-dynamics-gauge-20261103/autonomous_gate_v07.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_autonomous_gate_v07.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

- `experiments/parity-dynamics-gauge-20261103/AUTONOMOUS_SCALAR_FEEDBACK_GATE_v0.7.md`: exact derivations, hypotheses, failure cases.
- `experiments/parity-dynamics-gauge-20261103/autonomous_gate_v07.py`: stdlib rational exact verification.
- `experiments/parity-dynamics-gauge-20261103/autonomous_gate_v07.results.json`: seven-field scoped outputs and five rational initial preparations.
- `experiments/parity-dynamics-gauge-20261103/test_autonomous_gate_v07.py`: four focused tests.
- `candidates/parity-dynamics-gauge-20261103/mathematical_receipt_autonomous_v0.7.json`: typed provenance, candidate normalization, target exposure, null and phase controls.

Local equivalent constructor calculation PASS; four alternative-construction unit tests PASS. Separate non-constructor scientific review NOT_RUN. GitHub workflow integrity must be checked for the final head SHA, and it tests repository integrity not scientific truth.

## Decision and next source gate

**EXACT/CONDITIONAL:** determinant invariant and source-floor obstruction under all scalar reciprocal feedback laws; candidate's aligned asymptotic solution. **FAILED:** robust generic-phase full retention by proposed stock-only scalar gate. **OPEN:** selected nonlinear/nonreciprocal additional channel, controller/source receipts, 17D–29D bridge, particle-law prediction. No mere nonzero stored modal support constitutes physical matter.

**Next recommended:** identify the minimal *source-derived* non-scalar/rank-two coupling capable of changing D while maintaining a declared enlarged total support/current receipt; test source/generic-phase classes without target-informed adjustments. If no source supplies it, record a DISCOVERY candidate and preserve the original obstruction.

Claim held; no integration, mainline export or claim release.
