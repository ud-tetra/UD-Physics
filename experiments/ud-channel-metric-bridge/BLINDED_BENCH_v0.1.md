# Blinded capacitor work bench protocol v0.1

**Frozen scoring and acquisition specification. No bench run, assignment
commitment, or measured certificate yet. Physical promotion 0.**
Dependencies: [capacitor fixture v0.1](CAPACITOR_PORT_v0.1.md) and
[acquisition simulation v0.1](ACQUISITION_SIM_v0.1.md), baseline e3ec2d3.

## Fixed design

Use the two prescribed capacitor fixtures: H_1 endpoint energy and
uniform coefficient energy. Use nominal C*=1 µF, a=1 µC and load/return
windows T=1 s each. Reference W*=a²/(2C*)=1/2 µJ. These are bench settings,
not physical UD unit assignments. Verify timing, reference calibration,
and actual stiffness tolerances independently. No endpoint charge may
be inferred from the tested capacitance and measured voltage.

Sixteen blocks B01–B16, eight per fixture, each contain the nine
signed/sham preparations x±, y±, c± and a separate sham for each mode
(144 shots total). Each shot starts near zero charge, reaches the
commanded charge, then returns near zero while measuring both signed
terminal work integrals. Keep the switch sequence, terminal reference
plane, integration windows and settling rules fixed across fixtures.
Execute the full scheduled inventory without optional stopping or
replacement blocks. An aborted block may be recorded as an abstention
with a failed certificate; record the reason and preserve raw data.
An incomplete block inventory prevents a scored run.

## Separation and seals

A custodian builds or characterizes the two fixtures, masks identity and
randomly assigns the balanced fixture sequence using fresh entropy.
Commit to the canonical JSON key (protocol, a fresh secret 32-byte salt
as lowercase hex, and the arms map) using SHA-256 before collecting
work. Also seal the independently randomized within-block shot order
and the protocol/scorer hashes before acquisition. Preserve raw time
series, shot order, timestamps, reset records and instrument certificates.
The custodian provides only coded fixtures and identity-neutral
certificates. Staff exposed to wiring or characterization must not
adjudicate the blind calls. No arm labels, component values by code,
or key salt go to the analyst before sealing the predictions.

A non-constructor checks the calibration evidence and freeze records
before acquisition. The analyst seals canonical prediction JSON,
which includes the canonical input digest and key commitment, before
receiving the fixture key. Score verifies the pre-reveal prediction
digest and original key commitment. The scorer cannot prove custody,
timestamps, real calibration, randomization or independent review;
these are explicit bench evidence obligations.

## Gates and units

Use independently calibrated signed charge and terminal work channels.
The calibrated V/I pairing skew must be at most T/10000. Work
integration uncertainty must cover time alignment, gain, reference-scale
uncertainty and any omitted sample contribution. Gate each shot:

1. For each terminal at initial, loaded and returned states, the absolute
   measured charge residual plus its certified error must be ≤ a/100.
2. Absolute load and return work uncertainties must each be ≤ W*/512.
3. With return work signed into the device, require
   |load+return| + both work uncertainties + 8(1/100)² W* ≤ W*/128.
   The last term bounds the reset-energy difference. This certifies a
   loss bound only with an independently verified passive device and
   complete terminal energy accounting. It does not rule out cancellation
   by an unseen active source; reject if that assumption cannot be audited.
4. Require an independently characterized bound of 3W*/512 per shot
   for the work change due to circuit deviation from the assigned exact
   fixture over all admitted charge endpoints. The custodian signs the
   bound without revealing the arm. For example, a max absolute row-sum
   stiffness deviation ≤1/512 in normalized units suffices for the
   two-coordinate boxes (largest command L1 norm 3/2).

These give W*/64 of non-preparation error per load shot and W*/32 after
signed averaging and sham subtraction. Apply the fixed endpoint preparation
budget from capacitor port v0.1 separately. A non-constructor must
audit the identity-neutral certificate flag against the raw evidence.
No gate can be waived after data access.

## Frozen decision

Normalize input charge by a, work by W*, and timing by T. For each block
subtract the corresponding sham from the mean of each signed pair.
Classify the sign of S=W_c−W_y only if the entire interval with
radius 1857W*/10000 lies strictly to one side of zero. Positive predicts
H_1; negative predicts uniform. A failed certificate or interval
touching zero is an abstention, not an incorrect forced guess.

Accept only with at least seven correct blocks per arm and zero wrong
calls overall. Record all abstentions and report the first failed gate
per block. This is an engineering acceptance rule; the repeats are not
independent devices and the threshold is not a significance claim.
Report the pure ratio as a diagnostic only. An accepted bench run
would establish discrimination of known circuit fixtures; it would
not select a physical UD metric.

## Replay and input contract

Run `python3 bench_score.py classify INPUT.json` in the experiment directory.
INPUT keys: protocol (UD-CAP-BENCH-v0.1), commitment (hex digest), blocks
(in fixed ID order). Each block has id, timing_bound_over_T,
independent_certificates_ok, and shots keyed x-, x0, x+, y-, y0, y+, c-, c0,
c+. Each shot has initial, loaded, returned (each two [value,error] pairs),
load_work, return_work, load_uncertainty and return_uncertainty. Numeric
fields use integers or exact rational strings. A failed certificate
block can omit shots; it still needs its scheduled ID. Invalid structure
is not a substitute for a measurement abstention; do not proceed to unblind
on a scorer error.

Canonical JSON for hashes is UTF-8 from the scorer's canon() function
(sorted keys, compact separators, no terminal newline). After sealing,
run `python3 bench_score.py score PREDICTIONS.json KEY.json SEALED_SHA256`.
Run `python3 bench_dry_run.py` for synthetic controls: clean, one allowed
abstention, two same-arm abstentions, wrong sign, altered key and altered
prediction seal. Its fixed synthetic key must never be used at the bench.
