# Phase-window non-affine source-frozen checkpoint — 014

Date (UTC): 2026-10-24 (artifact capture local; repository state checked against `main` `1e6e0f2abe3fa234919c5a6701547883a807b3e5`).
Claim: `claims/icosahedral-phasewindow-20261022`, held by `phasewindow-20261022-gpt6-7c41` (verified). Owned branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Other PR #44 claim held and untouched.

RESULT: NUMERICAL / DEVELOPMENT. An archived case `edge-p1-b0.005-cf0.0` has source coefficient SHA256 `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd` reproduced exactly. Full 560-state moving reference plus 8 tangent directions over 401 sampled times u0..100. Selected direction's max first-order predicted `||Z||` 3.726089188e-4 and largest finite `||Z||` 3.72609063e-4. Full selected-direction finite nonlinear Taylor residual ≤2.93734e-9 sampled; half phase ≤7.34339e-10; ratio0.250002. Energy balance, momentum, finite differences checked. Not a whole phase-ball theorem.

IMPORTANT FAILED/INCOMPLETE attempts: full 180-column source-matched tangent exceeded compute cap before result. Full five-run refinement at rtol3e-11 similarly timed out after three trajectories; precision refinement of scalar peak/balance is diagnostic only. Preserve these limitations. Earlier 180-column result checkpoint 013 was for a distinct generated scattered case, not this exact frozen source case.

EXECUTED: `source_case.py`; `run014_small.py --tangent-only`; `replay014.py`; local numpy/scipy checks. Python py_compile PASS. NOT_RUN: full source-matched 180-column gain, uniform nonlinear remainder, high-precision complete refinement, independent mathematical review/experiment. Repository CI integrity must be checked separately at the final branch head.

Capture: `artifacts/phasewindow-20261022-gpt6-7c41/source-frozen-remainder-014/` with schema2 SHA256 manifest; local ZIP includes the big binary stage state, time trace, failed full run and full source files. Do not edit earlier immutable runs or shared main state.

Next discriminant: scalable full R180 source-case projected tangent operator and rigorous time- and phase-uniform nonlinear remainder. Preregister/freeze candidate before claiming independent test. Mainline promotion=0; physical clock/material calibration OPEN.
