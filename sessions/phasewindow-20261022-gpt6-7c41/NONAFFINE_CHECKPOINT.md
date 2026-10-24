# Checkpoint — exact full 12-vertex 3D non-affine threshold

STATUS: EXACT / CONDITIONAL; full u100 orientation/ringdown/coherence remains OPEN.
Task: `icosahedral-phasewindow-20261022`. Session: `phasewindow-20261022-gpt6-7c41`. Claim: `claims/icosahedral-phasewindow-20261022` status HELD by `phasewindow-20261022-gpt6-7c41` (initial held SHA `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`).
Research branch: `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`. Last prior checked head `36e81aca89f4441fe7f36cf0b4d8813cfbcdcc09`. Current read-only main at discovery boot: `0a058176d9dd079b6aad8fa530cd8093f1fcf43c`.

## Finding

For any complete physical 3D shell with original 12 radial +30 exterior spring energy `U<=1360051/20000000`, **a flattened original cell requires the full non-affine projector norm** `||(I-P0-PV)Y||_F > 1/40`. The stricter affine-only case `Z=0` is therefore excluded. Exact spectral-stress corollary: `tr(Y^T Ω Y)>(1+sqrt5)/1600` for such a hypothetical flat configuration.

This is **not** a global energy barrier, proof that `Z` remains small during the pulse, housing-strut safety, u100 breathing/ringdown, hardware or physical clock calibration.

## Completed checks

- `python3 affine_barrier.py --out affine_result.json`: PASS all 36 exact 4th-order icosahedral edge-frame polarization tests, every face plane/inradius check, and affine-shell rational contradiction.
- `python3 whole_shell_nonaffine.py --out whole_shell_result.json`: PASS all 20 face covariance identities and three rational edge-energy ranges. Minimum contradiction `414763/72000000 >0`.
- `OPENBLAS_NUM_THREADS=1 python3 independent_check.py --out independent_result.json`: PASS separate numerical graph/projector/edge-frame checks; constructor self-test only.
- SHA-256 source/output archive: captured under `artifacts/phasewindow-20261022-gpt6-7c41/affine-barrier-010/`, schema v2.
- Repository `scripts/validate.py` and 16 unit tests: NOT_RUN in local runtime without full checkout; CI to be separately verified at new head.

## Target exposure and failed alternatives

Threshold `1/40` and three bins chosen after exposure to original pulse budget and prior rank-four/9-vertex failures; no held-out data or independent physical predictions. Previous relaxed and induced-patch failures untouched; full12 numerical flattened candidate `~0.124426` still not a proven global minimum. The live PR44 Green-response task is owned separately; do not modify its files.

## Highest-value next action

Priority 98/100: test whether the nonlinear original pulse dynamics can keep `||Z(u)||_F <=1/40` for the entire `u∈[0,100]` phase/qualified-parameter envelope, using forced-response/geometry bounds under the correct PR ownership. If that fails, develop a stronger global stress-energy certificate; do not claim mainline physical closure.
