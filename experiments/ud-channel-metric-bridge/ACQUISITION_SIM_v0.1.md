# Signed capacitor acquisition simulation v0.1

EXACT synthetic calculation; no hardware or empirical data. Physical
promotion 0. Source: [capacitor port v0.1](CAPACITOR_PORT_v0.1.md),
commit 5438685a9903201cadcacb05b41207d902191a10, circuit and decision sections.

## Signals and certificate boundary

In normalized units a=C*=T=1, prescribe a linear charge ramp
q(s)=s q_f for s in [0,1] from zero. The two-component state has
voltage V(s)=s K q_f and terminal input I(s)=q_f+λV(s), the sum of
storage current and a passive linear shunt (λ≥0). This is an ideal
driven model, not a simulated closed-loop actuator. It uses independent
multiplicative gain errors for the two work sensor types and a separate
gain error for the endpoint charge sensor. Charge is observed from q_f
through that sensor model, never reconstructed from K and measured V.
This is separation in software; hardware independence is unverified.

The work integrator uses 32 midpoint samples, pairing voltage at s+δ
with current at s. It measures both terminal powers and sums them.
The code feeding the classifier passes only observations and externally
supplied synthetic calibration bounds, never the arm or hidden state.
Calibrations are presumed truthful. No noise distribution, fitting,
or statistical confidence claim is used.

## Exact uncertainty calculation

With absolute charge gain bound G<1 and observed charge z,
the true endpoint differs from z by at most |z|G/(1−G).
Adding the observed command residual certifies endpoint error η=1/100,
or triggers abstention. Next, require timing skew no larger than half
a sample interval so shifted samples stay on the ramp.

All tested stiffnesses have max absolute row sum at most 2. With
certified |q_f,i|≤1+η, use B_V=2(1+η), B_I=1+η+λ B_V, with λ
replaced by its certified upper bound. In normalized work units, per
shot the leakage loss is bounded by 2λ B_V²/3; the unskewed midpoint
quadrature error is at most 2λ B_V²/(12 N²) because only the quadratic
power term contributes. Timing costs at most 2 B_V B_I |δ|.
Work gain costs at most 2 B_V B_I (1+|δ|)(G_V+G_I+G_VG_I).
Twice their sum bounds the corrected signed-average-minus-sham work
receipt, even though the synthetic zero-sham has exactly zero work.
If it exceeds W*/32, abstain. Add the separate endpoint preparation
bound from capacitor port v0.1 to each work receipt. Twice that
combined bound gives the radius for S=W_c−W_y; sign is reported only
if the entire interval has a strict sign. This rule classifies the
sign in the scoped fixture comparison, not all possible energy laws.

## Executed checks

* 64 accepted cases: both fixed fixtures across all 32 sign corners
  of preparation, charge gain, voltage gain, current gain, and skew,
  at fixed positive leakage. The ideal signed value was contained in
  every reported interval; all signs matched.
* 12 injected fault cases (six faults on both fixtures): four charge,
  six work budget, and two timing alignment abstentions.
* One missing certificate abstention.
* One exact zero-sign comparator (off-diagonal stiffness 1/4) abstained
  despite passing the calibration gates. Its interval contained zero.

The finite grid is a deterministic synthetic replay, not a statistical
validation or test of fabricated calibration bounds. The measurement
model omits offset drift, charge redistribution at switching, nonlinear
loss, and hardware noise. Reopening for bench execution requires
independent charge and timebase certificates and an energy closure
check on a real device. No physical UD correspondence is scored.

Replay: python3 experiments/ud-channel-metric-bridge/acquisition_replay.py
