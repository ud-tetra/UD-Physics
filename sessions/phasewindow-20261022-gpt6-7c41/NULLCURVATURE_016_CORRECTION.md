# UD016 integrity correction and checkpoint — 2026-10-24 UTC

**STATUS: CORRECTED CAPTURE / CI PASS / EXACT local mechanism + NUMERICAL finite tests / UNIVERSAL NONLINEAR U100 OPEN.**

Session `phasewindow-20261022-gpt6-7c41`; held live task claim `claims/icosahedral-phasewindow-20261022`; original read-only main source `0abea764505989dde38fe0906d0d32c53d76b93c`. No writeback to mainline or PR44.

The full frozen executable source/data archive is a 162972-byte ZIP with SHA-256 `e58aa2f25d9295c2fe16bc9cdb50b87a170673551321e0382a7646b9d2c4dcee` and 39 ZIP members. The repository run `artifacts/phasewindow-20261022-gpt6-7c41/nonaffine-nullcurvature-016/` stores 14 ordered UTF-8 Base64 parts, two manifest-tracked reconstruction inputs, the full report/checkpoint/receipt, and a schema2 SHA-256 manifest. Read-back of **all 14 parts directly from this GitHub branch** produced the same ZIP length/hash as the constructor-local copy. The restore script is `inputs/001-restore_bundle.py`.

## Historical integrity failure and correction

Initial GitHub Actions Discovery integrity run **40053618552 failed** with `Invalid external input source metadata`: two manifest source fields were `source_location=local` (not an accepted value) with non-null source_path. No force law, code, computation, initial phases, results, or archived bytes failed this check.

On the same unvalidated metadata draft, commit `e707361f2afad2a57d68bf3f685ef56a6427033a` corrected **only** the outer manifest input provenance fields to `source_location=external` and `source_path=null`. The original invalid manifest persists in Git history. Run **40053706700 completed SUCCESS**, reporting `PASS: 213 records; manifest digests and local documentation links valid` and `Ran 16 tests ... OK`. This is tooling/integrity confirmation, not mathematical/empirical replication.

**Nested archive qualification:** The historical byte-identified ZIP contains a separate local inner capture manifest with `source_location=local` under `capture-016/`. Its own bundled hash/bytes audit passed, and the input data and numeric replay are intact, but moving that inner directory verbatim into the repository's validator would require correcting that provenance metadata. The GitHub outer manifest is corrected, valid and fully hash-verified. Avoid claiming the inner manifest itself passed repository schema validation.

## Scientific boundary

- Computed source-frozen `G_4` rank24/null156; positive and negative finite phases in 48 general,24 pure-channel and36 mixed cancellation directions produce small nonlinear even responses.
- The largest tested mixed-cancellation even response at `u=4` is `5.7140005e-9`; a fitted10D quadratic slice reaches `1.8129311e-9` and scales approximately quadratically with phase amplitude.
- **EXACT/CONDITIONAL** moving-axis damper differential includes a displacement×velocity bilinear term; numerical projected source cross-force verification agrees within0.16% at full phase and improves at smaller amplitudes.
- **NOT COMPLETED:** full156D Hessian eigenspectrum timed out. There is no `sup_a` second-order response certificate, continuous-time error enclosure, physical validation, or `u=100` full nonlinear phase-ball proof.

The correct high-value next calculation is a compatible full-null Hessian/forced-Green bound including mixed cancellation and source/interval errors. The branch remains a draft research handoff, not an integrated result.
