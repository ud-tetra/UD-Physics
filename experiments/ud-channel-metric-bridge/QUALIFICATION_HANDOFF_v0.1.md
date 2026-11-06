# Bench qualification and independent review handoff v0.1

**STATUS: OPEN — no measured certificates, no independent review, and no
concealed assignment.** This handoff implements the existing
[frozen bench protocol](BLINDED_BENCH_v0.1.md) and scorer at
3fab543a570ef544058ced91880fa823568276ac. It does not amend their gates.

## What the bench must demonstrate

The frozen settings are a=1 µC, T=1 s, and W*=500 nJ. The limits below are
worst-case absolute bounds, including the uncertainty of the reference
and conversion. Record separate signed load and return work readings.

| Gate | Exact limit in bench units | Evidence to attach |
|---|---:|---|
| Signed charge, each terminal and endpoint | 10 nC for residual plus uncertainty | Independent charge injection and readout; both polarities, zero and half amplitude, on both channels; include offset, cross-talk, drift and reset |
| V/I pairing skew | 100 µs | Common-edge timing trace through the actual acquisition paths; include channel latency, drift and trigger alignment |
| Load and return work integration | 125/128 nJ uncertainty each | Separate traceable signed work reference over the declared window, including omitted transitions, skew, quadrature, gain and reference scale |
| Passive recovery closure | 125/32 nJ including both integration uncertainties and reset energy | Signed load/return trace and audited terminal boundary with no hidden energy input |
| Assigned-fixture deviation | 375/128 nJ per shot | Identity-neutral bound signed by custodian, with supporting characterization retained separately |

If both work uncertainty allowances are used in full, the largest
admissible measured absolute load-plus-return imbalance is
125/32 − 2(125/128) − 2/5 = **497/320 nJ**. The reset allowance is 2/5 nJ.
Use the actual certified integration uncertainties in the gate. Meeting
the timing limit by itself does not certify the work integral.

Use uncoded calibration references and practice waveforms before test
assignment. Record instrument serials, calibration date, traceable
standards, sensor and terminal diagram, bandwidth, ranges, timebase,
sample and integration rules, and raw signed data hashes. Exercise all
three command shapes and both signs at the frozen time and amplitude.
A known capacitance matrix must not be used to infer the independent
charge readout. Account for switching transients within the chosen
reference plane. For recovery, establish passivity and account for all
ports before interpreting a round-trip imbalance as a load-loss bound.
Record the largest supported error, including between-point uncertainty
over the admitted envelope. Any unbounded term leaves that gate OPEN.

## Independent reviewer response

Return this section with an attestation and linked evidence. Keep any
identity-bearing characterization out of the analyst packet.

- Reviewer, date, relationship to construction, and exact protocol and scorer hashes:
- Independent replay command, environment, results and discrepancies:
- Signed charge, timing, integration, recovery closure and fixture deviation:
  for each, enter PASS / FAIL / OPEN, measured bound with units, and evidence hash.
- Review specifically: whether signed charge is measured independently;
  whether timing uncertainty is carried into work; whether switch energy
  is captured; whether the recovery argument requires an unverified active
  or hidden port; and whether custody precludes label disclosure.
- Disposition: PASS IN SCOPE / REVISIONS REQUIRED / UNABLE TO VERIFY.
- Scope and remaining objections:

First reproduce `python3 bench_dry_run.py` in this directory. That replay
checks the scoring workflow; it cannot qualify a device. A protocol-only
review may be recorded while instrument gates remain OPEN. Only after
independent review and all measured gates pass should the custodian
commit a concealed assignment. Do not generate or expose a test key in
this qualification handoff.

Current evidence: PR #349 discussion checked, no review comments or
attestations returned. The repository's present records are synthetic;
no measured instrument or recovery data were available for this handoff.

Pinned SHA-256 values (raw file bytes):

```text
b82a4c071048dba9f4bc18189611997370dcaa3f094758c2f7e806033cfba291  BLINDED_BENCH_v0.1.md
845a38d2fdb2c263cd82eaa1f4c3a76cb9c0b2e65f09cf1d1d40579f6405c262  bench_score.py
6b9139e3b4ae690e92b9a758d6400d6597573a765dc0a38a04053451c8a1c4be  bench_dry_run.py
```
