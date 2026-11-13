# Wrapped pilot phase admission v0.1

**EXACT / CONDITIONAL.** A valid timestamp bracket alone can admit a cycle slip. A separate phase-increment bound can certify a unique lift, modulo an irrelevant common integer turn.

Discovery parent e7d60ef60be016d2eb6488e535ebd9a4aefdcf3f. Retain the relative timestamps, slope cap L, curvature cap K, tag cap η, and additive pilot phase bound α=asin(E/P) of [Timestamp reference v0.1](TIMESTAMP_REFERENCE.md) and [Interleaved reference v0.1](INTERLEAVED_REFERENCE.md). Assume reported endpoints r₋<−η and r₊>η, so both true samples bracket the science snapshot. Pilot phasors must be nonzero. The shared pilot phase is stable or derotated. No physical timing or phase calibration is assumed.

A sufficient observed endpoint increment cap is

    D = L(r₊−r₋+2η) + K[(|r₋|+η)²+(|r₊|+η)²]/2 + 2α.

This follows by expanding each true phase about the science time and including both pilot readout errors. Form d=arg(P₊ conj(P₋)). Possible noisy endpoint increments are d+2πn for integer n. Admit the principal lift exactly when |d|≤D<2π−|d|. D<π guarantees uniqueness whenever a lift is consistent. With right weight w=−r₋/(r₊−r₋), interpolate arg(P₋)+wd. A common 2π shift leaves the interpolated phasor invariant. A one-turn error in the relative increment instead changes the interpolated phase by 2πw before reduction.

**NUMERICAL.** Across 512 synthetic corners at half-spacings 1/4 and 9/20 native time, including pilot phases straddling the principal branch cut, the largest cap was 0.02376115 rad. The guarded interpolation agreed with the known lifted interpolation within 7×10⁻¹⁶ rad modulo 2π. Averaging the wrapped endpoints directly made a π-rad error in one of these valid timing brackets. This replay checks wrap handling, not an expanded timing or noise budget.

**EXACT / NO-GO.** With a looser cap 3π/2, increments 3π/4 and −5π/4 yield identical endpoint phasors and both satisfy the cap. Linear histories with those increments on the same symmetric timestamp bracket differ by π at the midpoint. This synthetic alias lies outside the previous small-drift contract. The guard rejects it. If the actual drift violates the supplied cap, a false unique lift may still pass, so an independent drift envelope is a prerequisite. Physical promotion 0. Independent review NOT_RUN.

Replay with `python3 experiments/clock-matrix-question/wrapped_reference.py`.
