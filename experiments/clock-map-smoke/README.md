# Synthetic affine clock-map smoke trial

FIT + EXACT: the assumed map is `t_label_ns = offset_ns + scale_ns_per_tick * n`.
The integer event index `n` is counted in declared ticks; labels are synthetic
nanosecond numbers. No measured clock, UD construction, evolution law, causal
mechanism, reference frame, or physical unit realization is supplied.

The trial definition at base `fbf40e3f4daaf3f02af5db35fc1ee82f0da02190`,
`docs/HANDOFF_TRIAL_v1.0.md`, discloses all points before this work:
training `(0,1), (1,3), (2,5)`; evaluation `(3,7), (4,9)`.
Evaluation is development evaluation and cannot establish blinded prediction.

From the repository root, with Python 3 and its standard library:

```bash
python3 experiments/clock-map-smoke/clock_map.py --fixture experiments/clock-map-smoke/fixture.json
```

The script fits ordinary least squares using exact `Fraction` arithmetic. It
fits both affine parameters using training points only. It fits the constant
baseline to the training mean only. Both objectives minimize unweighted training
sum of squared residuals; no noise model or parameter uncertainty is justified.
The model families were prescribed by the exposed trial, not discovered by a
blind search. Two families are evaluated, with two and one free parameters;
there is no additional parameter search or tuning.

Expected affine offset: `1 ns`; slope: `2 ns/tick`. Residuals use prediction minus
label and are all zero. The constant baseline is `3 ns`, with training residuals
`2,0,-2 ns` and evaluation residuals `-4,-6 ns`. Baseline SSE is `8 ns^2` on
training and `52 ns^2` on exposed evaluation; affine SSE is zero on both.
Distinct training indices identify the affine parameters within this assumed
family. Many other functions can interpolate these five numbers; zero residuals
do not identify a native or physical clock law.

The candidate record and session handoff record limitations and next actions.
Output is deterministic JSON: rational numbers are strings, key order is sorted,
and no timestamps or environment-dependent fields are included.
