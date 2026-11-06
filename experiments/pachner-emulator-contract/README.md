# Controlled paired-readout emulator v0.1

The machine-readable contract fixes the reviewed classifier and latch from
PR #308, signed probe channels, externally supplied event marker, sample
schedule, affine errors and acceptance criteria. The contract and replay
driver were committed locally before the scored replay. This is a constructor
verification of new deterministic fixtures, not a blind or physical experiment.

The scalar emulator computes the two declared channels with exact rational
series; the alternating-series first omitted terms bound truncation over
the admitted phase domain. The terms decrease there since u <= 1/20.
Channel gain multiplies the series remainder; that error plus the injected
noise fits the declared eta. Phase increments are supplied by the emulator
scheduler, not estimated from readouts. Samples are synchronous.
The underlying transport, trigger and perturbation estimates are inherited,
not revalidated by this scalar emulator.

The matched-continuation null deliberately runs the baseline law on both
sides. Identical traces and labels are required; no third model label is
expected. The four abstention controls concern declared violations or lack
of progress. They do not imply detection of unreported physical error.

Replay from repository root:
`python3 -B experiments/pachner-emulator-contract/replay.py`.

Autonomous startup remains SOURCE_BLOCKED. No dimensional clock, native
event law, fitted physical parameter, or physical correspondence is claimed.
