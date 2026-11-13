# Interleaved reference timing v0.1

**EXACT / CONDITIONAL.** Bracketing cancels first-order gain drift at exact midpoint alignment. Curvature and midpoint timestamp skew bound the remaining error. This is a synthetic timing model.

Discovery parent 79972df9c9102a822d669e0e96c49a913e7ed5cd. Use [Shared reference v0.1](SHARED_REFERENCE.md) and [Clock alignment v0.1](CLOCK_ALIGNMENT.md) for the terminal science gap, aperture offsets and science magnitude floor S. Keep the science snapshot at relative native time zero. Set the pilot magnitude floor P=10S and each post-gain additive phasor error cap E=1/40000000 of launch stock. Let the effective gain phase of each detector be a twice continuously differentiable function θ(t), with |θ'(0)|≤L=1/50 and |θ''(t)|≤K=1/100 over the relevant interval. These are phase bounds per native time and per squared native time, respectively. They are selected synthetic inputs. Assume a stable or independently derotated shared pilot phase, no static science-to-pilot mismatch, and unwrapped phase samples. Treat the two detectors' drift as independent.

A one-sided pilot nominally at h is sampled at h+δ. A bracketing pilot nominally at ±h is sampled at δ±h, where the common offset for that detector satisfies |δ|≤ε=1/100. For the bracket use the arithmetic mean of the two unwrapped pilot phases. Taylor's theorem bounds per-detector drift error by:

- One-sided: L(h+ε)+K(h+ε)²/2.
- Bracket: Lε+K(h²+ε²)/2.

The bracket cancels the linear-in-h term. Common midpoint skew leaves a linear term. Independent timing jitter on the two pilot samples is outside this contract. The bounds are attained by opposite-sign quadratic drifts at δ=ε. Additive phasor noise contributes asin(E/S)+asin(E/P) per detector in either estimator. Averaging two pilot samples supplies no deterministic improvement against errors of the same sign.

With minimum offset gap g and nominal gap Δ from the saved replay, the per-detector drift allowance is (g−Δ/2)/2−asin(E/S)−asin(E/P). Solve each monotone timing bound against that allowance. The finer replay gives allowance 0.00153067 rad and maximum nominal delays of 0.06512286 native time for one-sided sampling and 0.51578571 native time for bracket half-spacing. The full bracket span is twice its half-spacing. The extrema are conditional on the prior numerical floors and gaps.

At h=1/4, the one-sided replay reverses the ordering (−0.00212467 rad) and the bracket retains 0.00792533 rad, above the half-gap target 0.00588998 rad. At h=3/5 both methods fail the half-gap criterion. The replay constructs complex science and pilot readings and applies tangent-disk perturbations. The saved coarse and fine inputs agree at the displayed precision. This test adds no conversion to seconds and no measured drift or timing data. Independent review NOT_RUN. Physical promotion 0.

Reproduce with `python3 experiments/clock-matrix-question/interleaved_reference.py`.
