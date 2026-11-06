# Relative calibration and startup registration v0.6

**EXACT / CONDITIONAL.** Source commit
`9c3a12e0ce7d7d1662040b89a990349aa9ce2f97`.
This extends [the two-boundary-readout certificate](TWO_READOUT_v0.5.md).
The same declared signed apex probe, metric, event map, all-active generator
hypotheses and scalar-phase model are retained. No empirical calibration
or native selection of that preparation is established.

## Affine measurement model

For nominal model channels W,Y at a common phase, use

[
w_m=(1+g_W)(W+e_W)+b_W+n_W,qquad
y_m=(1+g_Y)(Y+e_Y)+b_Y+n_Y.
]

Here (|g_i|legamma_i) are relative gain errors,
(|b_i|leeta_i) are additive offsets in native amplitude,
(|n_i|leeta) are post-gain noise/conversion errors, and
(|e_i|le d) is the pre-gain dynamic deviation, with

[
d=rac{91}{2}epsilon+rac{17}{2}r+3D.
]

The multiplicative gain applies to the actual dynamic signal, so its cross
term with d is retained. Common scalar phase is arbitrary and nondecreasing;
D bounds cumulative nonscalar operator error after extracting that phase.
Independent sampling displacement between channels must fit the declared
error model; it is not removed by the common-phase argument.

For ALL phases, (|W|le1/4), (|Y|le2/sqrt5<1).
Consequently the following two sufficient calibration conditions imply the
v0.5 per-channel error bound (delta=1/1000000):

[
rac{gamma_W}{4}+(1+gamma_W)d+eta_W+etaledelta,
]
[
gamma_Y+(1+gamma_Y)d+eta_Y+etaledelta.
]

These are global amplitude bounds, not circular estimates using the later
admission window. Gains/offsets need not be inferred from the comparison
signal; their declared envelopes must be supported externally.

One simultaneous allocation is

[
epsilon=r=rac1{10^9},quad D=rac1{10^8},quad
gamma_W=gamma_Y=rac1{2000000},quad
eta_W=eta_Y=rac1{8000000},quad
eta=rac1{4000000}.
]

It gives (d=21/250000000) and total channel errors
(292000021/500000000000000) for W and
(479500021/500000000000000) for Y, both below delta.
These are conditional tolerances, not measurements of an instrument.
Unrestricted gain freedom would include a zero-gain channel and cannot
support this discriminator.

## Reproducible startup latch

The v0.5 classifier required a registered first rising reference quarter.
Replace that Boolean assertion by the following conditional protocol:

1. At the declared event, anchor nominal phase (u_0=0). Record an event
   receipt identifier and check (|w_{m,0}+1/4|ledelta),
   (|y_{m,0}|ledelta). These envelope checks do not independently prove
   the event's identity; the event marker is a trusted input.
2. Supply a valid upper bound (0le u_{j+1}-u_jle h=1/1000) for every
   successive sample interval. This is a bound on integrated native phase,
   not a clock-to-seconds calibration. The implementation checks the
   declared certificate; it cannot infer its truth from endpoint readings.
3. Arm once and wait until the FIRST observed (y_{m,j}ge a=1/100).
   Invalid phase-step declarations permanently disarm that run.
4. At that first crossing require (y_{m,j}le b=1/80) and evaluate the
   existing paired residual threshold. Latch the result; do not scan for a
   later cycle or rearm the same event. A new event needs a new latch.

A stopped phase is allowed; no finite-time success is promised without
progress. The sampling protocol can have arbitrarily long absolute pauses
provided its phase-increment certificate remains valid.

## First-quarter and no-overshoot proof

The reference signal is (Y(u)=2sin(sqrt5u)/sqrt5).
On its first quarter, (Yge4u/pi>u).
Initially u=0. Suppose no trigger has occurred at sample j.
Then (y_{m,j}<a), and, provided the phase is on the first quarter,
(u_jle Y(u_j)<a+delta).
The next phase satisfies

[
u_{j+1}<a+delta+h=rac{11001}{1000000}<rac1{10}.
]

Since (1/10<pi/(2sqrt5)), induction keeps every pre-trigger sample and
its following interval on the first quarter. This supplies the branch
qualification instead of assuming it at the eventual snapshot.

The global reference Lipschitz bound is (|dY/du|le2).
At the first trigger, its previous observation was below a, so

[
y_{m,j+1}<a+2delta+2h
=rac{6001}{500000}<rac1{80}.
]

Thus every valid first trigger lands inside the admitted observed reference
window, without overshoot. Each channel still meets the v0.5 error bound,
so its full/projected classifier and residual margin apply unchanged.
The startup rule establishes phase-branch registration conditional on the
event anchor and phase-step certificate.

## Exact limitation: finite samples cannot supply their own phase bound

The reference has period (2pi/sqrt5). Without an upper phase-increment
bound, adding arbitrary whole reference periods between samples preserves
every reference snapshot. In the full branch, W has the same period, so
even both sampled boundary channels can conceal complete cycles.
Therefore finite endpoint data alone cannot certify that a sample belongs
to the first quarter when arbitrary phase jumps are allowed.

The phase-step certificate cannot be silently replaced by timestamps without
a rate bound, by an event count without a phase-per-event law, or by a
plausible-looking sequence. A continuous no-missed-crossing detector is
another possible acquisition assumption, not a consequence proved here.

## Implementation and executed tests

Run `python3 -B experiments/pachner-timing-budget/calibration_startup.py`.
The module provides calibration-bound checks and a one-event StartupLatch.
Its two terminal uncertainty states reject missing event envelopes and
unregistered phase steps; a result remains latched rather than reclassifying
later observations. It also checks over-budget gains.

The test creates 384 adversarial streams: two model hypotheses, three
phase-step limits, and 64 combinations of endpoint gain/offset/dynamic/noise
signs. The dynamic and post-gain noise signs are aligned at their extreme;
these give the extrema since all admitted gains remain positive.
Streams include pauses and varying phase increments. All advancing streams
register and classify correctly. Nominal trigonometric test data are enclosed
using rational degree-12 polynomials, with their remainder reserved inside
the dynamic-error allowance. The proof covers all admitted streams; the
tests are constructor checks, not empirical calibration or independent review.

Remaining source dependencies are the event anchor, a phase-per-sample
certificate, signed preparation/readout registration, and justified physical
calibration/noise bounds. Metric and event-map variations remain excluded.
Physical promotion remains 0.
