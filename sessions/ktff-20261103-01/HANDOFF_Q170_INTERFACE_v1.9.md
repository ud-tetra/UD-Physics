# v1.9 — Q171 source review and Q170 complete interface handoff

**2026-11-05 | EXACT / CONDITIONAL / PROPOSED signed amendment / NO-GO native C2 continuation / physical promotion 0.**

Task `klein-tetra-face-flip-20261103`, session `ktff-20261103-01`. Coordination claim `refs/heads/claims/klein-tetra-face-flip-20261103` remains HELD at `667e2cfe3c1507a47e8f4dc1aa8766fec8d280c4`. Same isolated Discovery branch `discovery/klein-tetra-face-flip-20261103/ktff-20261103-01`, draft PR #301. Main verified `b04652406b5579ca172564d0e3a6fe3aca75693a`, original base `0eef9a3f77198810b35bee8d3ef578ebc3af403a`. No mainline, frozen ledger or public site edit; no source promotion.

## Source-authoritative amendment SUBMITTED, NOT ACCEPTED

[Issue #338](https://github.com/ud-tetra/UD-Physics/issues/338) is an explicit source review request for the proposed `Q171_DIRECTION_AMENDMENT_PROPOSAL_v0.39a.md`. Current v0.39 Q171 prints `+2B3 cface ctop` as top-stock derivative. Using identical ascending signed B3 and source Q169 `A=D−Dᵀ`, this quantity is instead **face gain / top outflow**; top-stock gain equals its negative. Witness B3(012,0124)=−1 and unit face/top amplitudes yields actual native top derivative +2 versus printed expression −2 if the B3 aliases coincide. The proposed amendment names `J_out(f,tau)=+2B3 cface ctop`, `J_in(tau,f)=−J_out`, `dot S_top=ΣJ_in`. An alternate accepted path would explicitly define `B3_Q171=−B3_Q169`. The source custodian/reviewer has NOT yet accepted either, so no source rewrite or AUTO_LOCK of the alias.

## Complete shared-shell Q170 test

Let old `C0=R15`, new `C1=R29`, `F` the unique source integral degree-one 1→4 chain map, `T=F[:,original 14 lower-grade coordinates]`, and `N=I29−TTᵀ`. At a candidate top-zero event `a=0`, `x_old=(z,0)`, `x_new=Tz`. Both native metrics are independent unit Euclidean and generators `A0=D0−D0ᵀ`, `A1=D1−D1ᵀ`. Exact `TᵀA1T=(A0)_shell,shell`; old removed top and all new born modes have zero amplitude at the event. Thus **every** original 14-shell control volume has identical Q165 stock and identical first derivative / Q170 signed cut current on either side, with zero old/new complement stock/current. A 16,384-cut rational-state fixture verified this; matrix identity proves it for arbitrary z.

**New all-state exact obstruction:** Each original vertex, edge or outer face has a unique newly born cone simplex involving centroid4 with a unit signed incidence coefficient. Consequently `Lnew=N A1 T` is a rank14 signed isometry, `LnewᵀLnew=I14`; the remaining new centroid vertex is initially not excited. The old removed top excitation `Lold=e_topᵀA0T=−2bᵀ`, where `b=∂3 e_top/2`, has rank1 and Gram `LoldᵀLold=4bbᵀ`. Hence

```
Tᵀ A1² T − (A0²)_shell,shell = 4bbᵀ − I14.
eigenvalues: +3 once, −1 thirteen times; rank14.
```

**Scoped NO-GO:** No nonzero eligible old shell state has matching shared-shell amplitude second derivatives under both unmodified generators. Native old removed-top stock begins `4beta² u²`, refined new born support begins `||z||²u²`; cut-current slopes are `8beta²` versus `2||z||²` for `beta=<b,z>`. Special unit b has exact old top `sin²(2u)`, new child tops `sin²u`, currents `2sin(4u)` vs `sin(2u)`. The one-instant Q170 match is genuine but cannot be interpreted as a complete finite-time cross-complex current law.

## Reproducible evidence and limitations

- `experiments/klein-tetra-face-flip-20261103/Q171_DIRECTION_AMENDMENT_PROPOSAL_v0.39a.md` — review-only proposed alias.
- `experiments/klein-tetra-face-flip-20261103/CURRENT_INTERFACE_Q170_v1.9.md` — theorem and explicit hypotheses.
- `experiments/klein-tetra-face-flip-20261103/q170_interface_v19.py`, `independent_q170_cone_v19.py`, `q170_interface_results_v19.json`.
- `candidates/klein-tetra-face-flip-20261103/mathematical_receipt_q170_interface_v1.9.json`.
- This handoff, candidate/session journal and run capture.
- Full locally executed `UD_K4_Q170_INTERFACE_v1.9.zip`, 12 files, SHA-256 `4650a66caf1016a7494348bb0aadbf1e7743f51e49400ccfa3813788f62f3704`. Contains v1.7/v1.8 source-input scripts, full v1.9 exact and independent cone programs, proof, sign-amendment proposal, two exact JSON results, **12/12 passing tests**, 16,384 rational shell-cut comparisons, README and per-file hash manifest. Local version is not asserted byte-identical to shorter GitHub replay. External non-constructor mathematical review NOT_RUN. GitHub CI validates repository integrity only.

**NEXT GATE:** Obtain source-authoritative review and accepted versioned Q171 convention from issue #338. For any new cross-complex event theory, choose a new metric/contact/controller or correctly specified nonsmooth event jump and test Q165/Q170 continuity over a finite interval, not just at the switch. No SI time, physical event selection or Planck resolution floor; physical promotion 0.