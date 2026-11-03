# UD parity dynamics and gauge quotient — session pdyg-20261103-01

BOOT: BOOTLOADER v1.1, AGENTS, Discovery v1.2, Mathematical Method v1.0, CURRENT, CONCURRENCY v2.0, ARTIFACTS loaded. Verified base `2207611450df9106adccaf8189a50734fef5a46b`; claim `d0950c1c5376a31b483908c819123914ae59c404` HELD; connector-only branch isolation.

EXACT conditional proof and exhaustive count: see `experiments/parity-dynamics-gauge-20261103/README.md` and `results.json`; 1024 raw assignments, 8 parity fibers of 128, 90 S4 orbits. For illustrative `T(b,e)=(b,e+delta b)`, three-bit parity is not dynamically closed; four-bit `(theta,q)` is. `kerP=128`, P-history-invisible translations=64, P-preserving commuting translations=16. Distinct types; not physical hidden states or canonical gauge.

Verification: standalone Python 1024 x 24 exact check PASS; repository `scripts/validate.py` and unittest NOT_RUN because no authenticated local Git checkout in connector runtime. Source gate: canonical raw-state admission predicate and total native evolution law not identified in inspected files, so no negative assertion about canonical UD. Related `experiments/pachner-boundary-observability/README.md` demonstrates observer-dependent finite boundary response but does not select the present update.

Target exposure: earlier 128/90 results known; no physical target used or fitted. Clock = formal update index; no physical metric, units or empirical bridge. Claim remains held pending review/integration. Handoff: obtain source-native Adm,T and full action/transport observables; retest lumpability, action-preserving gauge and response separation; no mainline export.

## 2026-11-03 source-native continuation v0.2

Located and source-checked `experiments/qpb1-local-generators/README.md` v1.0, `experiments/qpb1-native-events/EVENT_CONTRACT.md` v1.0, `experiments/qpb1-loop-history/HISTORY_CONTRACT.md` v1.0. The real 15D unit-incidence law `x'=Ax`, `A=D-D^T` is explicit. Independently reconstructed exact simplex incidence; ran `python /mnt/data/ud_pdyg/native_chain_probe.py` using SymPy 1.14.0: PASS; edge observability ranks 6→12 (saturates), 3D hidden subspace, edge-only nonclosure witness, 12D `(q,p)` closure. Added proof and script `experiments/parity-dynamics-gauge-20261103/SOURCE_NATIVE_CHAIN_CLOSURE_v0.2.md` and `native_chain_probe.py`. Pure additive real-to-F2 map is identically zero (exact characteristic-two obstruction). This is source-native *within* the QPB1 unit-metric linear model, not canonical raw binary `Adm,T`; no full-UD nonlinear selection or physical gauge proof. Repository CI and non-constructor review NOT_RUN. Claim stays held pending draft PR review; `state/CURRENT.md` untouched.

## 2026-11-03 v0.3 — binary-to-chain interface / supporting review

Mathematical basis: QPB1 source-native real unit-metric chain flow `x'=Ax` and the distinct assumed finite register `F2^10`; typed basis/orientation, metric and formal time conventions in `experiments/parity-dynamics-gauge-20261103/NATIVE_BINARY_CHAIN_INTERFACE_v0.3.md`.

EXACT/NO-GO: additive maps between the binary additive state group and real additive chain state group vanish in both directions; a finite embedded alphabet invariant under *every* continuous QPB1 flow time contains only equilibrium states (by continuity). These do not exclude nonlinear quantizers or discrete samples.

EXACT/CONDITIONAL: an exploratory set encoding 0/1 vertex and edge coordinates in R15, with face and cell zero, at the source's dimensionless half-period `u=pi/2`, admits only eight of 1024 embedded states as invariant under the exact halfstep `I+A²/2`: `0,3,5,6,9,10,12,15`. The eight have all six edge bits zero and opposite-edge parity 000, so they do not represent UD's eight Theta labels. Two are fixed; the remaining six are vertex-pair complement toggles. Native time and encoding were selected in the experimental comparison, not derived as a physical coupling. Script `interface_audit_v03.py`, expected exact results `interface_results_v03.json`, typed receipt `mathematical_receipt_interface_v0.3.json`.

Supporting math checks: reran earlier locally captured F2 exact enumeration and real QPB1 observability scripts; both PASS. Alternative exact incidence unit test suite of four checks PASS locally: rank 12, q/p closure, D1D2=0 with independent incidence ranks, and half-period orthogonal involution. This is a constructor cross-check, not independent non-constructor review.

GitHub Actions previous run 41723839958 FAILED due task.status='in_progress' and missing candidate.baseline. Both faults were fixed on claimed branch (task.status='active' and baseline included), and new CI was triggered. GitHub Actions validates repository integrity, not mathematical truth. Non-constructor review NOT_RUN.

The active claim `claims/parity-dynamics-gauge-20261103` remains held at `d0950c1c5376a31b483908c819123914ae59c404`. The branch remains isolated; no merge, release, mainline export or CURRENT.md update. Next: independently source a complete finite-register Adm,T or nonadditive quantizer and prove a commutative discrete/continuous diagram on the admitted states; require non-constructor review.
