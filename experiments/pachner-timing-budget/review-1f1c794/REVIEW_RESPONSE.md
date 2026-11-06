# Reviewer response

- Reviewer / date: Devin Perry Ramos (AI Assisted Independent Review) / 2026-11-05
- Relationship to original construction: Independent reviewer; external verification of mathematical receipts and source artifacts without contribution to original model construction.
- Commit checked: 1f1c794ec8b7477ccb3282ff2b6c7bfa5f29634d
- Python version / platform: Python 3.9+ / POSIX x86_64 standard environment (no external dependencies, standard library only)
- Replay results and any mismatches:
  Package checksums: PASS.
  Nine pipeline scripts evaluated against benchmark outputs:
  - PASS: cell_root_probe
  - PASS: audit
  - PASS: comparison
  - PASS: classifier
  - PASS: robustness
  - PASS: two_readout
  - PASS: calibration_startup
  - PASS: source_audit
  - PASS: recovered_gate
  Exact byte-for-byte agreement observed across all generated outputs; zero mismatches.
- Analytical checks performed independently:
  1. Verified finite-dimensional recurrence relations and oriented boundary incidence conventions ($B_2$, $H_f$, $B_3$).
  2. Checked exact blindness of the original nominal preparation: verified that $E K^k c_0 = 0$ and $P K^{k+1} c_0 = 0$ for $k = 0 \dots 22$, confirming target silence and lack of discrimination without deliberate probe perturbation.
  3. Confirmed the deliberate $+1/4 e_3$ vertex-3 probe breaks symmetry and yields a non-zero second-derivative difference of 2, establishing positive separation under the declared $\le 1/1\,000\,000$ error budget.
  4. Verified the 4th-order rational polynomial midpoint threshold $m_4 = -1/4 + s^2/2 - 17s^4/96$ with uniform remainder radius bound $R = 1/382\,205\,952$.
  5. Verified the dual-readout ($W, Y$) cancellation of the common scalar phase on the registered rising reference quarter branch.
  6. Evaluated the operator closure across all 128 binary face masks, confirming that exactly 2 masks preserve the full top coexact sector ($H_f = 0$ or $I$), with 126 exhibiting leakage.
- Objections, missing assumptions, or counterexamples:
  1. The proof of paired classification remains strictly CONDITIONAL on external certificates: phase-zero event receipt, bounded per-sample phase advance ($\le 1/1\,000$), and affine channel envelopes.
  2. Autonomous startup is SOURCE_BLOCKED in the audited native sources; self-gated readiness encounters deadlocks, and an unanchored phase/sampling law is not physically derived.
  3. The mathematical model does not establish physical clock correspondence, autonomous event detection, or continuous physical spacetime dynamics.
- Disposition (pass in scope / revisions required / unable to verify): PASS IN SCOPE (Conditional)
- Scope of any approval:
  Approval is strictly confined to the internal mathematical validity and computational reproducibility of the finite-dimensional linear algebra, Taylor remainder bounds, and conditional readout invariants on the declared discrete 2-to-3 complex. This explicitly does NOT constitute approval of autonomous physical startup, physical time calibration, or unverified claims outside the stated conditional assumptions.
