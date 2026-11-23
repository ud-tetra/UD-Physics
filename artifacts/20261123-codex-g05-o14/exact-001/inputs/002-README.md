# G05 relay control and O14 measurement specification

Discovery capture of note 11231155. Base `54c76f50f00f831409819d2ba11b55139261968a`.
Physical Promotion = 0.

## G05 — Exact conditional exclusion

Prescribe segments A → B → C, with one oriented rotation mode on each of A and B and a fixed C. Use the native dimensionless clock, a unit modal metric, positive winding, squared modal supports `a_A=1/3, a_B=2/3` and angular frequencies `√3, √5`. The periods are `T_A=2π/√3, T_B=2π/√5`. Added whole turns return the prepared mode to its previous endpoint. The control assumes fixed transition durations and unchanged transfer receipts. No actual first-entry event is asserted.

The synthetic ledger is `q_test=n_A+n_B`, with added O09 action `I=π(a_A n_A+a_B n_B)`. Histories `(1,0)` and `(0,1)` have equal q_test, action difference `−π/3`, and time difference `T_A−T_B`. The exact replay enumerates nine histories with 0–2 turns per segment and finds five unordered equal-statistic pairs. Each has different lifted action and time.

For arbitrary integer differences, `ΔT=0` gives `Δn_A √(5/3) = −Δn_B`. The 5-adic valuation of 5/3 is odd, so it is no square in the rationals. Thus `Δn_A=Δn_B=0`. This exclusion applies to whole-turn edits with those fixed periods and fixed remaining durations. Other dynamical clocks, interface waits, partial turns and changes in mode selection fall outside the fixture.

Q136 → O09 remains OPEN_CONSTITUTIVE_SOURCE. Compute Q136 from its actual sigma receipts and compare admitted histories with the same specified boundary conditions. Record complete pre-event state, reserve, memory, clock, transfer, and interface phase at each event. Check the first-entry guard along each extended history: a return of the isolated modal endpoint alone gives no guarantee about earlier guard crossings. The [timing source gate](../pachner-timing-budget/SOURCE_GATE_v0.7.md) and [joint action proof](../g05-g06-joint-proof/README.md) give the source limits. The synthetic counter and weights were selected for a discriminating control. No empirical targets or fits were used.

## O14 — Conditional same-carrier action standard

Use the existing [seven-mode K4 LC candidate](../g0506-source-bridge-screen/README.md). The proposed standard is a calibrated, phase-referenced voltage/current/clock measurement chain on that realization. Let `rho=2` be the dimensionless angular frequency for its native active modes and let `a=‖x‖²` be independently fixed native support. For the stated ideal generator and energy pullback, measure baseline-subtracted energy E in joules and the primitive signed state period T in seconds:

- `y_E=E=k_E B0 a0² τ0^(-2)`, with `k_E=rho*a/2=a`.
- `y_T=T=k_T τ0`, with `k_T=2π/rho=π`.
- The exponent rows are `(1,2,-2)` and `(0,0,1)`. With `c=(1,1)` their sum is `(1,2,-1)`. Hence `A_map=ET/(π a)` and the candidate estimator is `eta_A=ET/(π a hbar)` if the map is admitted as O10.

Calibrate the absolute flux quadrature `Phi_*` by integrating a traceable signed voltage, and calibrate the characteristic impedance `Z` from independently measured L and C or a de-embedded impedance model. These give the model's primary scale `A_map=Phi_*²/Z`. For the energy–period check, measure injected work with separately calibrated voltage and current, subtract losses through the preparation endpoint, and measure T by simultaneous signed quadratures against a traceable clock. Retain calibration ancestry and any shared covariance. Signed quadratures distinguish a full recurrence from the half-period that can appear in quadratic observations.

Freeze the physical-to-native map, orientation, unit-support preparation rule, phase convention, controls and acceptance bands before acquisition. Certify generator and energy pullback on independent preparations across the active subspace, quantify spillover and dissipation, and use held-out preparations to test whether both estimates agree and stay constant across different supports. The factor `a` requires independent source assignment. Free rescaling of the assigned preparation changes the inferred native unit. Propagate joint covariance: for the E,T,a estimate the first-order log sensitivity is `(1,1,−1)`, giving `vᵀ Σ_log v`; shared uncertainty must also enter the comparison with `Phi_*²/Z`. Hold if the neutral amplitude scale remains free, closure residuals fail the registered bounds, or the held-out estimates are inconsistent.

This is an alternate analogue candidate, scoped to the active K4 carrier. It supplies a conditional dimensional span and no measurement of O10 or O14. A classical phase reference would require additional evidence for a quantum phase identification. Prior O14 trial values were exposed in project sources and were unused in the measurement design. The QuiX 14-edge optical reconstruction remains a separate test. Both the signed session return and the independently justified action transfer for that optical protocol are pending.

## Replay and handoff

Run `python3 experiments/g05-relay-o14/audit.py`. Compare stdout to the immutable capture linked in the session journal. For G05, the next discriminant is a source-admitted pair of full event histories, or an exact negative result on their admissible timing and receipt fibres. For O14, the next discriminant is an independently specified unit-support preparation and joint calibration on a named device.
