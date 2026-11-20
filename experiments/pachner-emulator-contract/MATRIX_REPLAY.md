# Matrix-source cross-check

The v0.1 contract, classifier and latch are unchanged. The new source
propagates the reviewed full and projected state vectors by direct
matrix-power Taylor evaluation and reads the same vertex contrasts. It
does not call the old scalar cosine/sine source. It shares the pinned
matrix construction and the classifier; it is a constructor
cross-implementation check, not an independent reviewer run.

The contract and runner were committed locally before a single entropy
draw. The seed was then retained. The new schedules were unavailable to
the original harness and were not redrawn. They vary rate and sample
interval within a trace. Gains, offsets and noise are bounded synthetic
inputs; no instrument calibration or physical time units are implied.

The inherited event metric gives an isometric nominal evolution with
generator norm at most 5 and readout-norm times event-state-norm less
than 5/2. For phase at most 1/20, the integral Taylor remainder per channel
is bounded by (5/2)(1/4)^17/17!. The sensor gain scales this bound and it
is charged to the noise envelope. All operations in the evaluator and
classifier are rational.

Result: 24 FULL and 24 PROJECTED correctly classified; zero wrong labels
and zero abstentions across 980 samples. This is a finite coverage result,
not a universal error-rate estimate. Autonomous startup remains SOURCE_BLOCKED.

Replay from the repository root:

    set -o pipefail
    p=experiments/pachner-emulator-contract
    python3 -B "$p/matrix_replay.py" "$p/seed.txt" | python3 -B "$p/summarize_matrix.py" | diff - "$p/matrix_receipt.json"

The receipt includes SHA-256 of the complete generated stdout and each
trace. The original negative controls remain covered by replay.py.
