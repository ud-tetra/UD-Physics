# Reviewer Addendum: PR #308 (Commit 1f1c794)

- Date: 2026-11-05
- Reference: [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md)
- Reviewed commit: 1f1c794ec8b7477ccb3282ff2b6c7bfa5f29634d
- Reviewer: Devin Perry Ramos (AI-Assisted Independent Review)

### 1. Second-Derivative Metric Clarification (Analytical Check 3)

The value ΔW''(0) = 2 belongs strictly to the v0.1 mask-hypothesis comparison.
For the +1/4 e3 apex probe under the v0.2 full-vs-projected comparison,
ΔW''(0) = 1/2. The separation bound (1/4) × (1/240)^2 / 2 = 1/460800
and downstream classifier budgets (v0.3–v0.6) already use this value.

### 2. Preparation Blindness Formulation (Analytical Check 2)

The nominal preparation check establishes identical target and memory
trajectories between full and projected continuations. This trajectory
agreement does not imply vanishing individual target coordinates.

### 3. Verification of v0.9 Counterexample (CELL_ROOT_v0.9.md / cell_root_probe.py)

- **Status: Independently checked analytically**
- **Analytical finding:** Under the antisymmetric top-cell perturbation,
  the unique reserve crossing persists and shifts, while both old-cell
  amplitudes remain strictly nonzero at the shifted crossing time.
  The reserve zero does not imply native cell-root alignment.

### Disposition

**PASS IN SCOPE (Conditional).** The conditional readout invariants are
cleared in the stated scope. Autonomous startup remains SOURCE_BLOCKED.
No physical clock or correspondence is approved.

Intake provenance: the initial response is preserved as submitted (with
trailing whitespace normalized); this addendum resolves its identified
ambiguities. The user confirmed Option A for §3. This is an intake record
of the supplied reviewer attestation, not a GitHub approval filed on the
reviewer's behalf. The review applies to the pinned commit above.
