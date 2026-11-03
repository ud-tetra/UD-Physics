# Checkpoint — expanded 3D housing-phase window

Timestamp: 2026-10-22T22:27:37Z
Session: `phasewindow-20261022-gpt6-7c41`; held claim `refs/heads/claims/icosahedral-phasewindow-20261022` at `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`.
Integrated read-only source: `ce89a9cd15439463d9a64d983d91c22ea4368726`.
Isolation: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.
Task status: HANDOFF / Draft PR pending validation; not integrated or exported.

## Result (scope separated)

1. **NUMERICAL / CONDITIONAL:** Original 50 exposed coefficient cases, original nine adaptive strengths, entire continuous chosen `nu∈[.04,.05]` through established Duhamel readout neighborhoods, all 180 initial housing phase directions **in the full linearized model**, now with `E_h<=3 E_p/80000` (1.5× original). Adjacent valid breathing-strength neighborhoods overlap by at least 0.00031000469824; original independent full-housing energy ratio upper0.4566660702<1/2 still applies because linear energy is homogeneous.
2. **EXACT / CONDITIONAL:** For every initial housing position/velocity phase with `alpha=0` and `E_h<=51/20000000`, across the original continuous qualified property box and `nu>=0`, nonincreasing energy gives positive primary members, all120 housing struts >554/1125 at all u>=0 and oriented cell volume ratios in `((19/20)^(3/2),(21/20)^(3/2))`, hence global housing-only ODE continuation.
3. **NUMERICAL (separate reduced benchmark):** Fixed-primary housing all-phase oscillator energies at u100 for nu=.02/.04/.05: 0.62964049/0.39644713/0.31458034; the full coupled system is not replaced with this scalar model.

## Recorded target exposure

Factor3/2 is a post-exposure developmental perturbation. The50 coefficient cases, nine nodes, old 80%/50% screens and nu interval were all used before and are not fresh validation data. Previous low-beta nu=.02, high mass and high friction failures remain. No nonlinear joint-pulse u100 all-phase theorem was claimed.

## Reproducibility and validation

- Original integrated input `linear.csv` SHA256 `971a8dc46bc42fc9b246ef7c20b13b9f3651d29d4704e111fa402f9e2edaf3e5`.
- Integrated `full_housing_refined.json` SHA256 `d3fc9c63f21811b65e3d0bed04063d8f4725eaab01970602e560876ccc569427`.
- Captured source bytes/output: `artifacts/phasewindow-20261022-gpt6-7c41/phasewindow-001/manifest.json`.
- Script: `experiments/icosahedral-phasewindow-20261022/replay.py` and original SHA256-pinned branch copy in capture; run with `python3 experiments/icosahedral-phasewindow-20261022/replay.py --repo-root . --out /tmp/phasewindow-result.json` from checked-out repo.
- Executed: connector-side parse/compute all450 source rows; local exact Fraction comparisons; independent fixed-primary scalar SymPy/DOP853 calculation.
- NOT_RUN: complete repository replay script, `scripts/validate.py`, repository unit tests (local GitHub network not reachable). No independent non-constructor mathematics review or empirical experiment claimed.

## Highest-value next step

Prioritize the existing full560 moving-pulse nonlinear certificate at the limiting beta=.005,c_f=0 case: enclose forced Green U(t,s), positive full-state norm and reference defect, proper-frame readout chart, and uniform nonlinear remainder; reproduce original E_h first, then test enlarged budget. Until this is done, full nonlinear all-phase breathing/ringdown and continuous property-box claims are **OPEN**.

No change to `state/CURRENT.md` or other sessions. Claim remains held pending separate review/integration or explicit abandonment.
