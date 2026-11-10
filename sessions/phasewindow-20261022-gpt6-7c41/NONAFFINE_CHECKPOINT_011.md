# CHECKPOINT — Non-affine shell dynamics 011

Date: 2026-10-23. Session `phasewindow-20261022-gpt6-7c41`, existing held claim `claims/icosahedral-phasewindow-20261022`, isolated branch `discovery/icosahedral-phasewindow-20261022/phasewindow-20261022-gpt6-7c41`.

Read-only main source `a4ae75dd55cd2b691c811c4d6eeae1367fcba015`, unchanged physics file blobs pinned in SOURCE_LEDGER.json. PR44 greenbounds held by other owner and untouched; mainline not changed.

**EXACT / FAILED energy-only Z certificate:** One admissible full-12-vertex R3 static state has `||Z||F²=2/1875>(1/40)²` and U<=197/56250<E_pulse. Thus no static total-energy implication bounds Z. This is not a reachable alpha=.1 trajectory.

**NUMERICAL finite dynamics u0..100:** four full 560-state trajectories; uniform symmetric Z~6.19e-15, nominal random ~4.19e-5, low-beta scattered Gaussian ~4.90e-4, same property with optimal u0 acceleration phase ~4.943e-4. All samples below1/40; no all-phase bound. Max relative E+heat residual <6.64e-10. Two low-beta trajectories refined at tighter tolerance and twice readout sample density; Z peaks change<6e-12.

**Executed:** exact_witness.py SymPy+Fraction PASS; verify_audit.py gradient/force/torque and initial-phase gain PASS; DOP853 four full pulse trajectories + two refined trajectories PASS. **NOT_RUN:** GitHub repository scripts/validate.py and 16 unit tests in local container; independent full source-file reproduction and physical experiment NOT_RUN. CI on branch after publication to be checked.

Archive `nonaffine-011` contains original source input bytes, four finite time-series and refined traces (local zip includes all), printed checks, mathematical receipt, SHA256 digests, plus findings and limitations. An integrated/mainline publication was not requested.

**Next:** Develop all-phase u100 projected Green/remainder certificate for nonaffine mode, using PR44 recovery with distinct claim coordination; do not claim full pulse cell safety, strut safety or breathing/ringdown result from finite samples.
