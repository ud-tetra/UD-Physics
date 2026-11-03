# UD Discovery handoff — parity dynamics / binary-to-chain interface v0.3

- **Task:** parity-dynamics-gauge-20261103; session pdyg-20261103-01.
- **Claim:** `refs/heads/claims/parity-dynamics-gauge-20261103`, held SHA `d0950c1c5376a31b483908c819123914ae59c404`; no release attempted.
- **Branch:** `discovery/parity-dynamics-gauge-20261103/pdyg-20261103-01`; PR #284 draft.
- **Verified integrated base at boot:** `2207611450df9106adccaf8189a50734fef5a46b`. Main later advanced to `3026f7a673dbec6103aae2a68a20bb94b61b61ae`; rebase and reconcile before merge. No shared `state/CURRENT.md` edits.
- **Primary source:** `experiments/qpb1-local-generators/README.md` v1.0 §§1–3; `experiments/qpb1-native-events/EVENT_CONTRACT.md` v1.0; `experiments/qpb1-loop-history/HISTORY_CONTRACT.md`; Discovery v1.2 and Mathematical Method v1.0. These support the real unit-metric QPB1 generator, **not** the extra binary encoding, update or physical clock.
- **Claim strength:** EXACT / CONDITIONAL for declared QPB1 and trial embedding; NO-GO under additive/full-time/injective-lossless hypotheses; OPEN for any canonical F2 admissibility and intertwinement; physical promotion 0.

## Findings

1. Source-native real 15D filled-tetrahedron flow `x'=Ax`, `A=D-Dᵀ` has `A³=-4A`; edge-only projection fails closure; `(Ex,EAx/2)` closes as `q'=2p,p'=-2q`. Edge-history observable rank 12, invisible dimension 3 (not necessarily gauge).
2. No nonzero additive group homomorphism exists between `F2^10` and `R15` in either direction; a nonadditive/quantized bridge requires separate justification.
3. A finite embedded alphabet invariant for every real flow time only contains equilibria. A lossless *sampled* finite intertwining with invertible QPB1 flow must be a permutation; irreversible retention requires a different law, a noninjective readout, or a larger/open state space.
4. Under trial coordinate-bit embedding and sample `u=π/2`, exact half-step `I+A²/2` returns only eight of 1024 bit states: `0,3,5,6,9,10,12,15`, with stationary `0,15` and 2-cycles `(3,12),(5,10),(6,9)`. All have zero edge bits and `theta=000`: **not** UD's eight-state opposite-edge fiber. No physical sample period is selected.

## Reproduce

```bash
python3 experiments/parity-dynamics-gauge-20261103/audit.py
python3 experiments/parity-dynamics-gauge-20261103/native_chain_probe.py
python3 experiments/parity-dynamics-gauge-20261103/interface_audit_v03.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_interface_v03.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Local constructor exact checks: F2 1024 × S4 permutations PASS; QPB1 native chain PASS; sampled 1024-state enumeration PASS; alternative four-test SymPy suite PASS. Earlier GitHub Actions runs failed on record metadata; metadata status and baseline corrected, then **Discovery integrity CI run 41727611691 PASS** and newer **run 41727801928 PASS**. CI comprises repository validation and capture/concurrency tests; not mathematical peer review. Full separate-context non-constructor review **NOT_RUN**. Latest commit may require another run.

## Reusable outputs

- `experiments/parity-dynamics-gauge-20261103/{README.md,SOURCE_NATIVE_CHAIN_CLOSURE_v0.2.md,NATIVE_BINARY_CHAIN_INTERFACE_v0.3.md}`
- `experiments/parity-dynamics-gauge-20261103/{audit.py,results.json,native_chain_probe.py,native_chain_results.json,interface_audit_v03.py,interface_results_v03.json,test_interface_v03.py}`
- `candidates/parity-dynamics-gauge-20261103/{candidate.json,mathematical_receipt.json,mathematical_receipt_native_chain_v0.2.json,mathematical_receipt_interface_v0.3.json}`
- Session journal and record.

## Next discriminant and reopening

Obtain a sourced `Adm` and `T_B` for binary K4 carriers (or construct and label a candidate nonlinear quantizer plus explicit clock). Specify domain, measure, S4 action, transport/action readouts, and verify `ι T_B=Φ_τ ι` or its explicitly noninjective/stochastic alternative. Test real prediction outside the construction set; do not count the coincidence of two eight-element sets as equivalence. Seek non-constructor review before integration. Claim stays held until merged or explicitly abandoned; no mainline export authorized.
