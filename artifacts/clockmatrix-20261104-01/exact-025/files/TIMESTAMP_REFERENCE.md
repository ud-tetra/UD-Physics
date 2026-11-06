# Timestamp-weighted reference under independent jitter v0.1

**EXACT / CONDITIONAL.** Timestamp-weighted interpolation removes linear phase drift for arbitrary actual bracketing times when their timestamps are accurate. Timestamp errors reintroduce a linear term bounded by the drift slope times the timestamp error cap.

Discovery parent 90e4017ecc411160a2bba99a1ff379d6b1b7916d. Retain the [interleaved reference v0.1](INTERLEAVED_REFERENCE.md) science snapshot, magnitude floors, additive errors and half-gap criterion. Keep L=1/50 for the slope magnitude at the science time and K=1/100 for the curvature magnitude throughout the pilot interval. Use the science reading at relative time zero, with a known time origin or the tag-error bounds already expressed relative to it. The true pilot times are t₋=−h+j₋ and t₊=h+j₊, with independent |j±|≤J=1/20. The reported times are r±=t±+e± with independent |e±|≤η=1/100, compared against η=0. These are synthetic caps in native time units.

Require h>J+η for a guaranteed true and reported bracket. Average the two unwrapped pilot phases with weight w=r₊/(r₊−r₋) on the left and 1−w on the right. Then the weighted true time μ=wt₋+(1−w)t₊ equals −we₋−(1−w)e₊ and satisfies |μ|≤η. The weighted second moment is exactly −t₋t₊+(t₋+t₊)μ. Taylor's theorem therefore bounds the per-detector phase error by

    Lη + K[(h+J)² + 2Jη]/2.

The positive weights retain the previous deterministic pilot noise allowance. The rule does not extrapolate across an invalid bracket. With prior per-detector drift allowance B, a sufficient upper half-spacing is sqrt(2(B−Lη)/K−2Jη)−J when the square root is real and the result exceeds J+η. The formula is sufficient; no sharpness claim is made for the curvature term with inaccurate tags.

**NUMERICAL.** With B≈0.00153067 rad, the sufficient upper half-spacing is 0.50329 native time for accurate tags and 0.46491 at η=1/100. At h=1/4 the noisy-tag drift bound is 0.000655 rad per detector, below B. At h=1/2 accurate tags still pass, while a tested inaccurate-tag corner reaches 0.0017125 rad and exceeds B. The replay enumerates the independent sampling and tag corners with opposite slope and curvature signs and rejects an invalid bracket. This is a deterministic synthetic test, without physical time calibration, phase unwrap failures, or measured timestamp errors. Independent review NOT_RUN. Physical promotion 0.

Reproduce with `python3 experiments/clock-matrix-question/timestamp_reference.py`.
