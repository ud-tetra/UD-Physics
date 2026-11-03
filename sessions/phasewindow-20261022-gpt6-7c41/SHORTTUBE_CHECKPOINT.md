# Checkpoint — original 0.1 pulse exact short-time tube (shorttube-003)

**STATUS:** HANDOFF / EXACT / CONDITIONAL / DEVELOPMENT. Not integrated, not exported to mainline, task claim still held.

- Current integrated read-only main: `7ae79d882e44446c7b4aefd4fdbe9ee781b9bafe`; source mechanics files checked byte-identical to parent main `ce89a9cd15439463d9a64d983d91c22ea4368726`.
- Owning task/session: `icosahedral-phasewindow-20261022` / `phasewindow-20261022-gpt6-7c41`.
- Held claim: `refs/heads/claims/icosahedral-phasewindow-20261022`, acquired at `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`. No change to other sessions.
- Branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`; Draft PR #45.
- Concurrent Draft PR #44 owns full forced-Green and alignment recovery. Its sources inspected read-only; no write overlap.

## Finding

For the **original** `alpha0=1/10` nonlinear 560-phase MountLoss surrogate and the enlarged, target-exposed `E_h<=51/20000000=3E_p,ref/80000`, every permitted 180-dimensional housing phase has, for **every u∈[0,2/5]** and every continuous parameter choice inside the qualified box:

1. All 120 current-axis housing struts have length strictly **>13/1500 ell0**, including at `u=2/5`; all primary spoke and edge lengths stay positive.
2. All 20 oriented cell volumes keep their reference orientation, with **`1/125<V_k(u)/V_k,ref<729/125`**.
3. Full nonlinear solution (no rigid quotient or frozen primary/housing coordinates) exists through `u=2/5` by continuation.

This increases the original-amplitude *all-phase exact domain* horizon by **8×** relative to the older `u=1/20` result, despite using a 50% larger housing-phase energy allowance. It does not establish stability or coherence to `u=100`. The rational horizon was selected as a sufficient proof choice after viewing the old target; not independent prediction.

## Proof technique

All estimates use the positive nonlinear energy, exact mass bounds and initial housing budget, and the **actual moving-midpoint housing equation**. Duhamel's harmonic kernel with `|sin x|<=min(|x|,1)` bounds housing displacement under current-axis Rayleigh forces; triangle inequalities bound struts. The reference Gram singular-value gap controls cell orientation. Exact fractions and same-runtime SymPy integration checks both pass. No 560-state numerical simulation or interval integrator is substituted for an exact theorem.

## Reproduction and provenance

- Executed locally: `python3 shorttube.py --out result.json` (exact Fraction PASS); `python3 independent_check.py` (separate SymPy derivation PASS).
- Branch code/docs: `experiments/icosahedral-phasewindow-20261022/{shorttube.py,shorttube_check.py,shorttube_results.json,SHORTTUBE.md}`.
- New mathematical receipt: `sessions/phasewindow-20261022-gpt6-7c41/shorttube_receipt.json`.
- Immutable source/data/manifest: `artifacts/phasewindow-20261022-gpt6-7c41/shorttube-003/`. All four copied source/output payloads compared byte-for-byte with their local Git blob SHA-1; manifest separately records SHA-256 digests.
- Repository validation and tests: **NOT_RUN in local container** (no local GitHub DNS/clone); check PR45 GitHub Actions after final branch commit. Integrity checks are not independent science reviews.
- No experiment or material prototype; uncalibrated physical units and 120 ideal massless struts remain OPEN.

## Negative result and next discriminant

The original amplitude total-energy *sublevel* still includes the known low-beta housing-at-endpoint collapse witness with energy smaller than the nominal pulse; it is **not** known to be dynamically reached. A pure energy-only proof cannot extend this to all time. The next discriminant is obtaining a full forced Green / nonlinear chart and reference-error certificate for the limiting original-amplitude `u∈[0,100]` pulse, without taking over the separately held PR44 recovery task. A local short-time bound does not establish the inherited `80% / 5% / 50%` nonlinear readout screens.

## Versioned correction
The historical `shorttube-003` proof contained a strict-sign notation error only at `u=0` for time-dependent volume/displacement envelopes. The fixed uniform strict safety theorem is correct. Corrected proof and `SHORTTUBE_ERRATUM.md` are captured immutably as `shorttube-004`; prior `shorttube-003` stays intact for audit. Source bytes were verified against Git blob hashes. No new empirical claim or altered result.
