# Centroid work port for the intercomplex metric scale v0.1

Development candidate; exact conditional identification, no data or physical
promotion. No model family or threshold fitted to physical targets.

## Model and preparation

Use the separate *UD K4 intercomplex action and positive metric
source-selection audit v2.1*, 2026-11-06, §§3–5 (archive SHA-256
37077981370f88ee62f0e24234c782ebb63d24ea57b03560b10fe36f0f79ef46).
On the 29D filled centroid split, F is integral chain transport and P is the
barycentric chain retraction. Set Q=I−FP and H_t=PᵀP+tQᵀQ, t>0.
Q here is the barycentric projector; it is not the unit-orthogonal
complement N or a parity projector. Use formal, dimensionless coefficients
in ascending simplex orientation and a fixed physical carrier throughout
the trials. Three vertex preparations suffice; all are invariant under
relabeling the four outer vertices.

* Inherited reference x=(e0+e1+e2+e3)/2 (fine embedding of the parent harmonic).
* Newborn y=Qe4=e4−(e0+e1+e2+e3)/4.
* Mixed witness c=e4=x/2+y.

With the ordinary coefficient dot product, xᵀx=1, yᵀy=5/4, xᵀy=−1/2.
Under H_t, x and y are orthogonal and the squared norms are 1 and 5t/4.

## Candidate operational bridge and controls

Assume the device's reversible stored energy is E(z)=κ zᵀH_t z/2 plus an
irrelevant constant, with a single κ>0 in joules across all three
preparations. This is an additional constitutive hypothesis, not Q165,
Q169, or the fixed-state observability result. The unforced H_t-skew
generator conserves this energy. A driven preparation must account for
work, losses and any energy exchange with other states before the
preparation receipt can be used.

From the same measured baseline b, impose b±a v for v=x,y,c at the same
independently verified coefficient amplitude a. Measure signed net work
in joules with the same calibrated acquisition chain, using conjugate
effort and flow at the actual actuator (e.g. voltage and current if an
electrical implementation is built). Repeat the sequence with zero
command as a sham. Account for losses by an independent recovery or
energy-balance measurement; reject trials with unresolved heat or hidden
state energy above the declared budget. The sham alone does not remove
amplitude-dependent loss. Alternate the signs and randomize trial order;
keep baseline, timing, instrumentation and reset rule fixed. An
independent state readout must certify the achieved amplitudes and
off-direction leakage, not infer either from work. The equal-command
condition does not by itself certify equal achieved amplitudes.

For each v, write W_v for the mean of the positive and negative work
receipts minus the zero-command receipt. In the reversible quadratic
model the symmetric difference cancels the baseline cross term exactly:
W_v=κa² vᵀH_t v/2. Hence

* r=W_y/W_x=5t/4 and t=4r/5.
* The independent mixed prediction is W_c=W_x/4+W_y.
* Uniform coefficient energy on the same preparations gives r=5/4
  but predicts (W_c−W_y−W_x/4)/W_x=−1/2, versus 0 throughout H_t.

The mixed witness matters: at t=1 the two pure-port ratios agree, yet
the mixed residual separates the two energy forms. The uniform energy
control compares endpoint work forms only; no claim is made that it has
the same compatible fine generator. A newborn amplitude gain g relative
to the inherited gain changes r to (5/4)t g²; a channel-dependent work
gain is also confounded. A common energy conversion and common amplitude
scale cancel. This measures a dimensionless sector ratio, not κ or an
absolute length, clock or action unit.

## Decision rule before data

Require positive reference work and simultaneous bounded intervals
[L_x,U_x], [L_y,U_y], [L_c,U_c] for net work after calibration, leakage
and loss corrections, with L_x,L_y>0. Include independently certified
relative amplitude error in the work intervals, or bound g separately.
For known equal achieved amplitudes the admissible t interval is
[(4/5)L_y/U_x,(4/5)U_y/L_x]. For separate gain bounds
0<g_min≤g≤g_max divide the lower limit by g_max² and the upper by g_min².
Reject a predeclared t value only if it lies outside this interval.
Use independent mixed trials to test the prediction by comparing the
interval for W_c−W_y−W_x/4 against zero and against the uniform prediction
−W_x/2, with joint error coverage. If both models remain compatible, or
if neither is compatible, report that outcome without choosing a weight.
Freeze the hardware, calibration bounds, trial count, and exclusions
before collecting test work. This protocol has no certified device yet.

Replay: python3 experiments/ud-channel-metric-bridge/work_replay.py
