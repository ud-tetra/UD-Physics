# Two-port capacitor work emulator v0.1

Development candidate. Exact circuit algebra and deterministic error budget;
no hardware measurements. Physical promotion 0.

## Circuit and preparation contract

This is an endpoint-energy emulator for [centroid work port v0.1](WORK_PORT_v0.1.md),
not a realization of the 29-dimensional incidence generator. Use two terminal
charges q=(q1,q2) in coulombs, with common reference ground and positive
current entering the device. Use coordinates in the ordered basis (x,c) of
that work port: command q=a(1,0), a(−1/2,1), and a(0,1), respectively, for
x,y,c. Fix a>0 independently of work. Run positive, negative, and zero
preparations from a verified zero-charge reset; disconnect and check the
endpoint without allowing charge exchange with the driver.

For a linear lossless network q=C V, terminal work integrated from zero
is qᵀC⁻¹q/2. Indeed power Vᵀ dq/ds is the derivative of this quadratic
form in laboratory time s. For a reference capacitance C* in farads, the
dimensionless stiffness is K=C*C⁻¹. The H_t endpoint form and the uniform
coefficient-energy control in the chosen basis are
K_t=[[1,1/2],[1/2,(1+5t)/4]] and K_U=I, respectively.

At t=1, C/C*=[[6/5,−2/5],[−2/5,4/5]], realized by ground capacitors
4C*/5 and 2C*/5 with mutual capacitor 2C*/5. The uniform control uses
two ground capacitors C* and no mutual capacitor. More generally, inversion
gives the two ground capacitances C*(5t−1)/(5t) and 2C*/(5t), with mutual
capacitance 2C*/(5t). The simple three-capacitor topology permits t≥1/5
(with one zero branch at equality); positive H_t alone does not guarantee
realizability by this topology. This circuit deliberately implements the
tested forms. Passing tests the work method, not UD metric selection.

## Instrument audit and rejection rules

Use bipolar charge actuators with terminal voltage and current logging
at the device reference plane. Integrate both signed V_i I_i channels over
the same declared window; do not substitute source-supply work. Use a
separately calibrated bipolar charge integrator for the signed endpoint
check, with a distinct current measurement channel, or independent
destructive charge readout on matched repetitions with a bounded repeat
error. Do not infer endpoint q from V using the very C matrix being tested.
Calibrate each sign, gain, offset and channel crosstalk against an
independent charge reference before the run. Include leakage between the
charge observation and the work endpoint in the charge-error bound.
A circuit schematic establishes neither sensor independence nor an achieved
instrument tolerance.

Repeat sham and sign reversals in randomized order, with the same reset and
window. Measure recoverable work during return to zero, and bound loss,
untracked ports, and unclosed energy balance separately from endpoint
charge error. Irreversible loss can survive both reversal and sham.
Reject the bench result if charge, dissipation, timing, or electrical
calibration cannot be certified within the declared bounds.

## Exact decision and sufficient error budget

Fix the two emulator arms t=1 and uniform before collecting data.
Normalize by the independently set reference W*=a²/(2C*), in joules;
do not normalize by a fitted arm. The three ideal works (W_x,W_y,W_c)/W*
are (1,5/4,3/2) and (1,5/4,1), respectively. Thus the work ratio alone
ties. The predeclared statistic S=W_c−W_y has ideal signs + and −, with
magnitudes W*/4. The exact sign rule is robust if
|error_c|+|error_y|<W*/4. Zero or intervals that cross zero are inconclusive;
passing the sign test alone does not certify the quantitative work ratio.

A sufficient deterministic allocation for these ideal arms is as follows.
Use componentwise absolute charge error at most ηa at every endpoint
(including start and sham). For the ideal dimensionless command v,
max absolute row sum of K is at most 2, and
|energy error|/W* ≤ 4η||v||₁+4η². Here ||v||₁≤3/2, so averaging
the active signed receipts and subtracting the sham costs at most
6η+16η², allowing independent error at all four endpoints of an
active/sham pair. This bound also covers wrong-sign and off-direction
components within the specified endpoint box. Allocate the remaining
instrument integration, circuit deviation from the exact arms,
unaccounted loss, and reference-scale uncertainty together to at most
W*/32 per corrected work receipt. At η=1/100 the total per-receipt
bound is (6/100+16/10000+1/32)W*=1857W*/20000<W*/8. The signed
statistic retains margin at least 643W*/10000. These are required
certificates, not measured device performance. Keep the full work
intervals for the separate estimate of t in the work-port protocol.

Replay: python3 experiments/ud-channel-metric-bridge/capacitor_replay.py
