# UD Discovery continuation handoff — Q170–Q179 retention-current gate v0.5

**Status:** EXACT CONDITIONAL SUPPORT-RECEIPT / NO UNIQUE RETENTION SELECTOR / PHYSICAL PROMOTION 0.

**Claim:** `refs/heads/claims/parity-dynamics-gauge-20261103` held by `pdyg-20261103-01` at commit `d0950c1c5376a31b483908c819123914ae59c404`; existing isolated branch `discovery/parity-dynamics-gauge-20261103/pdyg-20261103-01`; draft PR #284. Verified main at resume `6c9f3b855169448d224d7c9f9badee02d4d5a1e3`; original task base `2207611450df9106adccaf8189a50734fef5a46b`. Rebase before integration. No shared CURRENT, mainline export, merge, or release.

## Sources and types

- `sources/imports/2026-10-22/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39.md` (2026-08-22 baseline), Q169–Q179 and G05: exact support ownership, signed currents and unclosed open-system constitutive law.
- `experiments/four-cell-tetrahedron/README.md` v1.0: 1→4 subdivision, 29 unique simplices, four maximal 3-cells.
- `experiments/parity-dynamics-gauge-20261103/ADMISSIBILITY_RETENTION_QUOTIENT_v0.4.md`: 64-state sampled sign-parity **observer only**, not physical retention.

Carrier: finite 1→4 K4 3-ball, simplex amplitudes real with unit chain metric; stock `s_sigma=c_sigma²`. Cell weights `w_(sigma,tau)=1/n3(sigma)` for incident cells; support `S_tau=Σw s`. No physical clock or calibrated energy/charge unit.

## Exact proof and independent-form checks

`Σ_tau w_(sigma,tau)=1`; `Σ_tau S_tau=Σ_sigma c_sigma²`. Declare oriented lower→upper signed current `J_(sigma→eta)=−2B_(sigma,eta)c_sigma c_eta`. Differentiation yields `dS_tau/du=Σ_(sigma⊂eta)(w_(eta,tau)−w_(sigma,tau))J_(sigma→eta)`, matching ledger Q179 under this sign convention. The all-cell sum is zero.

For a candidate event adding nonnegative retained stock r, choose **additional** transfer δ_sigma∈[0,s_sigma]; set `s_sigma' = s_sigma−δ_sigma` and `r_tau'=r_tau+w_(sigma,tau)δ_sigma`. Then `S_tau'+r_tau'=S_tau+r_tau` in every cell. This is a **conditional accounting family**, not a derived selection mechanism.

Exact witness: prepare shared face (0,1,4) and coface (0,1,2,4) with unit amplitudes. Source current produces cell-derivative vector `(-1,+1,0,0)`, checked directly and independently by weighted J. Null δ=0 retains 0 and total=2; capture δ=1 retains 1 as two 1/2 shares and total=2. Both satisfy every stated conservation identity. **Selection nonuniqueness** is therefore exact. Capture persistence or growth preference not proved; disallowing reverse transfer is an extra assumption.

## Reproduce

```bash
python3 experiments/parity-dynamics-gauge-20261103/retention_receipt_v05.py
python3 -m unittest discover -s experiments/parity-dynamics-gauge-20261103 -p 'test_retention_receipt_v05.py' -v
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Saved: `experiments/parity-dynamics-gauge-20261103/CONSTITUTIVE_RETENTION_CURRENT_GATE_v0.5.md`, script `retention_receipt_v05.py`, result `retention_receipt_v05.results.json`, alternate test `test_retention_receipt_v05.py`, and typed receipt `candidates/parity-dynamics-gauge-20261103/mathematical_receipt_retention_v0.5.json`.

**Immutable artifact:** `artifacts/pdyg-20261103-01/retention-receipt-v05/` with captured input and output bytes, SHA-256 manifest v2. Local equivalent Python execution PASS (exact Fraction), with second all-29-simplex transfer audit PASS. Committed script execution, repository CI and non-constructor external review must be scoped to their actual receipts; none establishes physical truth.

**Next discriminant:** source an actual microscopic gate `δ_sigma=G(c,closure,transport,history)` and reverse-release/environment law. Freeze it before testing new states; compare with δ=0 and with reversible release. Specify typed conserved stock and boundary flux. Do not identify this new r stock as physical mass without the independent physical bridge. Claim remains held.
