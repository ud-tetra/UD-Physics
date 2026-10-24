# Session journal — qpb1-finwindow-20261023-gpt6-b6f2

- 2026-10-24T01:00:17Z: Read BOOTLOADER, AGENTS, v1.2 instruction, mathematical protocol, CURRENT, concurrency and artifacts at 41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb; inspected live refs and latest qpb1-local-generators dependency.
- Verified no pre-existing `claims/qpb1-finite-window-phase-20261023`, atomically created held claim e38d9b6cfba644744eba92d668b670068751487f, reread live claim.json, then created isolated connector branch from exact main base. No authenticated local Git checkout; no files from other owners changed.
- Chose the next named discriminant from the completed qpb1-local-generators study: finite-window Pancharatnam endpoint correction, independent gain errors, visibility floor. Exposed prior -1 phase/g=(1,1,3/2) and newly selected screens recorded as such.
- EXACT/CONDITIONAL derivation: V>=30383/30625 and |phase shift|<=42592/15569925 rad for all independent |delta_gk|<=1/100 at T=2pi, relative to fixed state's own nominal phase; no g1=g2 premise.
- NUMERICAL constructor: executed `python3 experiments/qpb1-finite-window-phase/audit.py --out artifacts/qpb1-finwindow-20261023-gpt6-b6f2/phase-001/files/summary.json` in isolated local staging. PASS 125 gain triples and 3 odd-N examples. Output SHA-256 4697f1e3bfd058d884f1c5c7daf50ab860281755a570d6365583accecc51a6c2; script SHA-256 f0aac2f6d702def770319ab3c47d9e6008370f2f84ee6029574df485a69b9f0b.
- Captured source bytes and output in immutable schema2 artifact phase-001; repo test commands NOT_RUN because repository checkout unavailable. These constructor tests are not an independent physics validation.
- Handoff: request full-repo validation and non-constructor review before merge; keep claim held until successful integration/explicit abandonment. Do not release while the PR is pending.

## Follow-up checkpoint: operational receiver (2026-10-24T01:09:17Z)

- Reverified task claim held at e38d9b6cfba644744eba92d668b670068751487f and isolated PR #87 head faabd63e9fafc44e824423e85a272d1fca71d750; PR open, no external review.
- New independent-method *same-assistant* derivation: coherent four-fringe receiver can estimate complex endpoint overlap; geometric phase also requires calibrated D=2T sum(rk gk) in the same phase frame. Raw endpoint phase at the exposed baseline is 0, whereas corrected holonomy is pi.
- EXACT/CONDITIONAL: for independent gain magnitude<=.01, |delta T|<=.01 native units, state norm-preparation radius<=.0005, complex receiver error<=.001 and D calibration error<=.001 rad, visibility>=607251319/612500000, total phase error<=11101676085864605533/1345612732743408915000<.01 rad.
- NUMERICAL constructor second implementation: 243 structured cases and 25,000 seeded probes, four analyzer quadratures and four noise directions, PASS; script digest ba77e87a80e2fb6eb48d7dd0faabaad9ec76a700654c9511cc38f8c5c0e004c3, summary digest 1a5501cc82220e5661df0543979cebb0c5be3d03ea49f40d3df2f92fb1a7f98f.
- Captured new immutable phase-002 with source input, output and SHA-256 manifest; phase-001 unchanged. External mathematical review NOT_RUN, physical receiver NOT_EXECUTED, all-time/native selection remains OPEN.
- Handoff: run updated PR CI; request outside expert review, then identify experimentally realizable same-gauge D calibration. Retain claim until integration or explicit abandonment; no mainline writeback.

## 2026-10-24T01:20:30Z — Phase-003 short-time calibration checkpoint

- Verified held claim e38d9b6cfba644744eba92d668b670068751487f, draft PR #87 head dabd8037cc635b51042b79562c18ea15614d4890; separate reviewer list empty and previous CI success.
- New EXACT/CONDITIONAL: Richardson short-time slope recovers the dynamical D estimate with rational worst-case error 699576281715419/725760000000000000 rad <0.001, using only coherent positive-time Z(h),Z(h/2) under time-invariant conservative generator.
- Detailed assumptions: calibration complex amplitude<=2e-6, probe time error<=1e-7, repeated normalized state norm distance<=5e-6, gain drift<=5e-6, main native-T metrology <=1e-5, common gauge. With the prior exposed screens, new phase budget 0.00821419808694 rad. All calibration numbers are target-informed and physically unmeasured.
- Executed: `python3 /mnt/data/ud_qpb_calibration/calibration_audit.py --out /mnt/data/ud_qpb_calibration/summary.json`, PASS exact Fraction assertions, 125 grid+10000 seeded weighted probes+16 signed noise cases. SHA256 source 784eedc38b32187a383dda3be5e6bb28614b3572b4d389f0515cd7ff1f4251c6; output fb92ac9b048f259d94b4d475bdf37bc164fffcce0659c6e3b2a8e91fcfb7bc67.
- IMMUTABLE artifact phase-003 committed; phase-001/002 unmodified. External mathematics/empirical verification NOT_RUN/NOT_EXECUTED. Do not merge/export or release claim pending independent assessment.

## 2026-10-24T01:32:00Z — phase-004 statistical receiver and frame-reference checkpoint

- Live claim e38d9b6cfba644744eba92d668b670068751487f remains HELD. PR #87 draft, head before phase-004 7e100fa6504fde634fab08497afeb4467ecae710.
- EXACT / CONDITIONAL: under eight ideal independent Bernoulli streams, two calibrated overlaps with |complex error| <= 2e-6 are jointly within budget at >=99% probability if m=7.4e12 events per setting (59.2e12 total). Exact 13th Taylor bound establishes tail <1/100; this is sufficient, not optimal/minimal.
- EXACT / CONDITIONAL counterexample: untracked measurement-frame phase of .002 radians only at main endpoint is invisible to probe results and contrast, yet moves the corrected phase by .002; combined previous worst-case upper budget grows to .0102141981 and loses its .01 certification. Does not refute previous same-frame theorem.
- Constructor execution: python3 /mnt/data/qpb_phase004/shot_noise_audit.py --out /mnt/data/qpb_phase004/summary.json, PASS; source SHA-256 f73c9585f5707c5ac2a8e6b393a0510bd904c81dc734aa0ec3175253d8ce6dba, output SHA-256 a4e2e7d8d2b25a01fd963c23a73436a24adbf981a71e887d530f9bcae5f03f62. Immutable artifact phase-004; phases001-003 unchanged.
- Physical information: Nature Photonics 2017 standard shot-noise scaling and Applied Optics 2021 phase-stepping systematic errors, cited as external conventional context; no instrument or UD identification inferred.
- Review and physical testing remain NOT_RUN / NOT_EXECUTED. Next: independent proof audit and concrete reference-drift/null-channel feasibility. No merge, no release, no mainline export.

## 2026-10-24T02:00:10Z — phase-005 reference/null and conventional baseline checkpoint

- Verified claim e38d9b6cfba644744eba92d668b670068751487f HELD and draft PR #87; isolated parent 63c4f997b68563460b54af73b04105b3f15ab687. Added new immutable phase-005 under owned artifacts; older runs unchanged.
- Three-channel **HYPOTHESIS**: S=Z exp(i(theta+ds)), R=exp(i theta), N=exp(i(theta+dn)), plus bounded complex errors. **EXACT/CONDITIONAL** S/R retains ds, S/N retains ds-dn, N/R reads dn. A 0.002-rad signal-only drift is invisible to common reference and null but survives geometric phase with unchanged visibility.
- New target-selected **FIT** error budgets null amplitude<=1e-4, signal-null phase mismatch<=5e-4; retain all phase003 original premises, including independent D calibration. Result: exact conditional total bound 0.008814208087935455 radians <.01.
- **EXACT / CONDITIONAL measurement model**: optional ideal IID Bernoulli 2 monitor channels x four phase settings with 3e9 events each gives >99% probability of complex monitor error<=1e-4; requires 24e9 events. This statistical bound is separate from the phase004 short-time 59.2e12-event budget, does not establish joint full-device confidence, and has no measured rate.
- Executed locally: `python3 /mnt/data/qpb_phase005/null_protocol.py --out /mnt/data/qpb_phase005/summary.json`; PASS 5x1024 synthetic cases, min visibility 0.9931327589489719 and 5120 conventional 3-tone exact equalities. SHA256 code 8945b9ccc1273673ecef9577e23a3ecea9679961c53bf9e57275bed6c89ec05f; output 347c9094dce14eadc1a2cbf87e4bdc56cabd18007441199ed833d90ce3b86330.
- **FAILED attribution**: the allowed three-sector UD overlap is identical for all time to a conventional three-tone model with omega_k=2gk and weights rk; no distinctive held-out residual or empirical validation. Random weights in stress checks are not certified inside phase003 preparation norm ball; retain that scope boundary.
- External conventional background: Hechenblaikner JOSA A 2013 for heterodyne reference subtraction; Schwider Applied Optics 1989 for phase-step drift. Both background, not UD measurements.
- Non-constructor mathematical review NOT_RUN; physical apparatus/reference metrology NOT_EXECUTED. Next: derive a source-constrained discriminant unavailable to generic 3-tone evolution, and separately validate path-matched reference drift in apparatus. Leave PR draft and claim held.
