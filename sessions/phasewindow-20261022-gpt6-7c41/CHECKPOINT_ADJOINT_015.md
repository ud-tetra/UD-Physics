# Checkpoint — source-matched 24-output adjoint / 180-phase response, run 015

STATUS: NUMERICAL/DEVELOPMENT; no full nonlinear u100 theorem or physical identification.

- Session phasewindow-20261022-gpt6-7c41; live claim `claims/icosahedral-phasewindow-20261022` held by this session, original held claim SHA `a6c0a36d74fdcc959441d81e2716fbd34d9a1ac4`.
- Research branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`; verified integrated read-only revision `53460195f74411ce764b24e0ab9d4fd772c4bd6f`. Core mechanical source blobs unchanged.
- Source-frozen coefficient case `edge-p1-b0.005-cf0.0`, canonical SHA256 `8c4d98b69171792190178b12b10a0648ca69aa545a750d3836963747015e98fd`; nu=.05, beta=.005, cf=0, alpha=.1, additional housing phase energy E_h=2.430311755526067e-6.
- 560 state variables retained; 24-output sparse backward adjoint replaces attempted 560x180 forward propagation. The 24x180 transfer includes every initial housing phase at the requested numerical snapshot, with correct velocity and position energy normalization.
- 12 target times u={1,2,3,4,5,6,8,10,20,40,70,100}; seven post-exposure near-u4 probes. Highest sampled firstorder triangle bound 0.00043566468927 (u4), threshold 1/40=0.025; u100 triangle 0.00017286147075, refined 0.00017286155699. Corrected u4 pointwise combined firstorder optimum 0.00040492925498.
- Jacobian independently checked versus original explicit JVP (approx 2e-13); four direct forward tangent comparisons at u4 (relative1.88e-8) and u100 (relative6.18e-5, absolute1.59e-8). Finite numerical errors are NOT bounded continuously.
- Nonlinear selected singular-phase ± and ±half through u100: largest sampled ||Z|| 0.00038058248626, full Taylor remainder 1.68264874085e-8, half remainder 4.20622829205e-9 (ratio0.2499766). Separate combined-optimized phase finite ||Z(4)|| 0.000404929565847, vector remainder2.376e-9. These are **directional**, not full180 nonlinear bounds.
- **FAILED/REPAIRED**: initial trust-region secular equation without scale normalization allowed phase ||a||>1; corrected normalized computation has phase norm1 and dual gap ~0. Coarse late-time adjoint-relative mismatch is preserved and refined, not hidden.
- Archive local `UD_3D_Full180_Projected_Adjoint_015_20261023.zip`, SHA256 `8a270616332dd8860fff1ba9e807dcdb94344651a40c1bf9ec0eb59a90911342`: 12 executable source inputs and 33 result outputs including all saved 24x180 operators, both finite traces, SHA256 manifest. Local archive verified. These bytes are **not** misrepresented as a complete committed repository artifact capture.
- Repository document `experiments/icosahedral-phasewindow-20261022/PROJECTED_ADJOINT_015.md`; typed receipt `sessions/phasewindow-20261022-gpt6-7c41/mathematical_receipt_adjoint_015.json`.
- Prior 4D track remains parked; separate PR #44 ownership not touched. PR #45 remains draft/unmerged. No mainline writeback.
- Next priority 98/100: validated continuous-time projected linear response and full phase-ball nonlinear remainder in a positive full-state norm for source-matched case; then parameter box. Existing original 80% breathing,5% mismatch,50% housing decay remain separate and unproved for full nonlinear R180 ball.

Checks actually run: local Python source coefficient hash and Jacobian JVP; DOP853 reference, 12 adjoints,7 local probes; 4 direct forward comparisons at u4 and100; full/half and combined-optimal finite nonlinear replays; local ZIP manifest validation PASS. GitHub integrity at final commit must be inspected separately before claiming CI.
