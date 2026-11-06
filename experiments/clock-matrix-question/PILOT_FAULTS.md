# Dropped pilot samples and drift outside the bound v0.1

**EXACT / CONDITIONAL.** Recompute the timing and phase bounds using the timestamps of the surviving samples. Wrapped endpoints alone cannot detect an extra full turn if the assumed drift envelope fails.

Discovery parent afee825d8657ace903d03cd3e3cdf4cbb6fd7741. Retain [Wrapped reference v0.1](WRAPPED_REFERENCE.md) and [Timestamp reference v0.1](TIMESTAMP_REFERENCE.md), with their L, K, η, pilot noise angle and half-gap budget. Assume trustworthy sample presence and timestamp metadata, a common pilot phase, and a science snapshot at time zero. This replay addresses one detector's pilot bracket at a time. Both detectors must satisfy the same admission contract.

A surviving bracket must contain both phasors and have reported endpoints r₋<−η and r₊>η. With right weight w=−r₋/(r₊−r₋), the weighted true time has magnitude at most η. Its weighted second moment is bounded by (1−w)(|r₋|+η)²+w(|r₊|+η)². Taylor's theorem gives the per-detector timing penalty Lη plus K/2 times that second-moment bound. Compare it with the saved drift allowance after reserving the existing additive noise budget. If it passes, use the observed-span increment cap and unique-lift check from Wrapped reference v0.1. A dropout count or a nominal cadence alone does not establish the surviving bracket's phase accuracy.

**NUMERICAL.** Keep r₋=−1/4 native time. The nominal r₊=1/4 is admitted. A missing endpoint is rejected. A replacement at 3/4 is admitted at a timing penalty of 0.00117550 rad. A replacement at 5/4 is rejected at 0.00180467 rad against the allowance of 0.00153067 rad. A 0.1-rad wrapped endpoint step on the nominal bracket fails the increment check.

**EXACT / NO-GO.** On the nominal symmetric bracket, two linear histories can start at phase zero and end at 1/100 or 2π+1/100. They have identical timestamps and phasors. The first obeys the slope cap and the second violates it. Their midpoint phases differ by π. The replay admits the same principal lift for both, so the gate cannot verify its own drift premise. An independent midpoint phase observation with error strictly below π/2 distinguishes these two histories. A finite set of samples by itself does not exclude arbitrary unbounded drift between sample times. Independent drift characterization or an independent science-time reference remains open. No physical time calibration or measured drift enters this replay. Independent review NOT_RUN. Physical promotion 0.

Reproduce with `python3 experiments/clock-matrix-question/pilot_faults.py`.
