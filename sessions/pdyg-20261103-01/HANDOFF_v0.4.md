# Discovery handoff v0.4 — QPB1 admissibility and sampled parity retention

**Task:** parity-dynamics-gauge-20261103. **Session:** pdyg-20261103-01. **Claim:** refs/heads/claims/parity-dynamics-gauge-20261103 at d0950c1c5376a31b483908c819123914ae59c404, HELD. **PR:** #284 DRAFT, isolated discovery branch. **Physical promotion:** 0. **Original integrated base:** 2207611450df9106adccaf8189a50734fef5a46b; repository main advanced and requires rebase prior to integration.

## Source scope

The source-native QPB1 filled-simplex chain flow is specified in experiments/qpb1-local-generators/README.md v1.0, §§1–3, and experiments/qpb1-native-events/EVENT_CONTRACT.md v1.0. Chain carrier R15 with f=(4,6,4,1), signed boundary d, unit Euclidean metric, A=d-d^T, continuous dimensionless flow u. Native quadratures q=Ex, p=EAx/2 satisfy q'=2p,p'=-2q. No full binary admissibility rule, physical clock, or physical retention operator is imported.

## New result and conditions

Choose sampling τ=π/4 using the source-native active frequency 2; declare it as observation convention. Then F=I+A/2+A²/4 and QF(q,p)=(p,-q). The admissible sampled domain consists of x with every q and p coordinate nonzero, invariant at the chosen sample times. Sign readout creates 4096 sign states; opposite-edge parity of q and p creates 64 paired labels. The induced evolution swaps θq and θp exactly. Three-bit θq alone does not close, and 64 histories are necessary to reproduce the full observable θq output on the declared domain.

The signed S4 action (including edge-orientation reversals) respects the quotient; 24*4096=98304 exact sign-state covariance cases checked. This is carrier equivariance, not a physical gauge group.

Sign/pair parity is a **readout**, not irreversible material retention. Source-native norm is not reconstructible from a sign bin, because x and λx share all signs yet have norm-squares in ratio λ². A sign-only material reset requires an explicit energy/stock reservoir and constitutive update. No such law has been selected or established, so do NOT promote this to UD matter creation, mass, source conservation or physical time.

## Reproduction and capture

- experiments/parity-dynamics-gauge-20261103/ADMISSIBILITY_RETENTION_QUOTIENT_v0.4.md
- experiments/parity-dynamics-gauge-20261103/retention_gate_v04.py
- experiments/parity-dynamics-gauge-20261103/retention_gate_v04.results.json
- experiments/parity-dynamics-gauge-20261103/test_retention_gate_v04.py
- candidates/parity-dynamics-gauge-20261103/mathematical_receipt_retention_v0.4.json

Run:
```bash
python3 experiments/parity-dynamics-gauge-20261103/retention_gate_v04.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_retention_gate_v04.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Local constructor test PASS for exact source matrices and exhaustive sign-state checks, plus four independently structured local unit tests PASS; not a non-constructor scientific review. Repository integrity CI must be checked for latest commit; prior PR #284 integrity runs passed at earlier heads. Keep any future CI status tied to its actual SHA.

## Decision and next source gate

**EXACT/CONDITIONAL:** 64-state sampled sign-parity quotient and S4 covariance within QPB1. **NO-GO/CONDITIONAL:** sign-only material reset cannot conserve full native norm for arbitrary amplitudes without added storage. **OPEN:** physical retention, actual finite-register Adm/T, source/sink and environment exchange, event-to-physical-time map, external non-constructor review. The next high-value task is a source-bound search for constitutive retention/current laws followed by an exact receipt, not a fitted contraction factor.

No merge, no mainline export, and no claim release authorized by the present evidence.

## Last source refresh

Coefficient provenance ledger v0.39, objects Q169–Q179, was reread. Q170–Q173 supply conservative support/control-volume and face/top-cell signed-current receipts; Q177–Q179 supply equal-share cell support and exact current change. The same ledger explicitly leaves environment, dissipation, renewal and gate-transition sources OPEN (also G05 action-weight gate). Therefore the 64-state sign readout is neither a proof nor a replacement for material retention. The next source-bound question is an admissible source/sink operator compatible with those established current identities and with physical readouts kept separate.
