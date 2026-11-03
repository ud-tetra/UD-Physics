# UD parity dynamics and gauge quotient — session pdyg-20261103-01

BOOT: BOOTLOADER v1.1, AGENTS, Discovery v1.2, Mathematical Method v1.0, CURRENT, CONCURRENCY v2.0, ARTIFACTS loaded. Verified base `2207611450df9106adccaf8189a50734fef5a46b`; claim `d0950c1c5376a31b483908c819123914ae59c404` HELD; connector-only branch isolation.

EXACT conditional proof and exhaustive count: see `experiments/parity-dynamics-gauge-20261103/README.md` and `results.json`; 1024 raw assignments, 8 parity fibers of 128, 90 S4 orbits. For illustrative `T(b,e)=(b,e+delta b)`, three-bit parity is not dynamically closed; four-bit `(theta,q)` is. `kerP=128`, P-history-invisible translations=64, P-preserving commuting translations=16. Distinct types; not physical hidden states or canonical gauge.

Verification: standalone Python 1024 x 24 exact check PASS; repository `scripts/validate.py` and unittest NOT_RUN because no authenticated local Git checkout in connector runtime. Source gate: canonical raw-state admission predicate and total native evolution law not identified in inspected files, so no negative assertion about canonical UD. Related `experiments/pachner-boundary-observability/README.md` demonstrates observer-dependent finite boundary response but does not select the present update.

Target exposure: earlier 128/90 results known; no physical target used or fitted. Clock = formal update index; no physical metric, units or empirical bridge. Claim remains held pending review/integration. Handoff: obtain source-native Adm,T and full action/transport observables; retest lumpability, action-preserving gauge and response separation; no mainline export.
