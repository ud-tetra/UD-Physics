# Simultaneous-reference bench acceptance v0.1

**CANDIDATE PROTOCOL.** Qualify a two-detector differential phase readout using injected complex signals and simultaneous pilots. The bench result would establish instrument capability on a declared operating envelope. Physical correspondence of the lattice clock requires a separate experiment.

Discovery parent c3c4d2aaca0baafdde455e9beea13a068f676049. Retain [Science-time reference v0.1](SCIENCE_TIME_REFERENCE.md) and the half-gap target from [Clock alignment v0.1](CLOCK_ALIGNMENT.md). The arithmetic checker uses explicit per-detector signal floors, additive error caps, path phase, and timing bounds.

## Setup and sequence

1. Freeze the acquisition mode, integration windows, gain settings, amplitude range, disturbance envelope, drift observation bandwidth, test ordering and pass threshold before the verification run. Use a common phase origin and simultaneous science and pilot records on each detector. Record raw complex samples, timestamps or aperture markers, source settings, and traceable instrument uncertainties. Define a phasor normalization for both streams. Bench voltage or digital counts require their own unit map to the synthetic launch-stock scale.
2. Feed both paths with a common injected phase and measure the residual science-to-pilot phase after gain correction. Use an independent phase standard or calibrated loopback and swap detector assignments to expose source or cable asymmetry. Sweep the declared amplitudes and acquisition conditions. Obtain a bound b on phase mismatch at equal effective sample time. Obtain lower post-gain magnitude floors S and P and upper additive complex error bounds E_s and E_p in the same normalization. Include the uncertainty of the calibration standard and any residual correction.
3. Apply known phase ramps and record the relative science-to-pilot effective sample skew with a common timebase or independent marker. Bound its magnitude by τ. Independently bound the common gain phase slope over the full skew interval by L in rad per unit of that same timebase. Use simultaneous apertures or establish that aperture averaging fits the point-sample model within the declared error budget. Treat fixed path mismatch and skew-induced drift as separate terms. Do not infer a slope bound from only the wrapped science-bracket endpoints.
4. Freeze the bounds before the held-out verification. Run a zero differential phase, known positive and negative gaps at the target scale, detector swaps, and a hidden-turn control with the same endpoint phasors and an independently established opposite phase at science time. Also check missing or weak pilots and inject excess skew or mismatch. For accepted records, check that the independently known phase lies inside the declared error interval. For the signed gap controls, require preservation of ordering and at least the predeclared gap magnitude after accounting for the truth standard's uncertainty. Require out-of-envelope controls with known violations to exercise the rejection path. Record coverage, invalid records and individual failures. Include both detectors and all required conditions in any joint uncertainty coverage statement.

## Arithmetic acceptance

Let g be a lower bound on the injected noiseless differential gap magnitude and T the predeclared minimum retained gap. For each detector the phase error is bounded by

    b + Lτ + asin(E_s/S) + asin(E_p/P),

provided both ratios are below one and the phase differences use a branch consistent with the known injection. The mean-value theorem gives Lτ, and the disk-angle construction gives the additive terms. Use E/(A−E) as a rational upper bound for asin(E/A) on 0≤E<A, by integrating its derivative bound 1/(1−E/A). Accept the arithmetic only if g minus the two channel bounds is at least T. The full bench verdict also requires valid calibration evidence and all held-out controls. An arithmetic pass with unmeasured or incomplete inputs is UNSCORED. Statistical intervals support a conditional verdict at their stated joint coverage, not a deterministic guarantee inferred from finite samples.

## Synthetic fixture

The replay rounds the existing synthetic gap and magnitude floors down and the target up. It uses b=1/1000 rad, L=1/50 rad per native time and E_s=E_p=1/40000000 per launch stock. Equal skew of 1/50 native time passes with a lower gap of 0.00614799 rad. Equal skew of 3/100 fails with 0.00574799 rad against T=0.005889984 rad. The sufficient symmetric skew cap is approximately 0.02645008 native time. A weak pilot can fail with zero skew. A pilot floor no larger than the additive cap is invalid. None of these fixture values were measured on an apparatus or converted to seconds. Physical promotion 0. Independent review NOT_RUN.

Reproduce with `python3 experiments/clock-matrix-question/bench_reference.py`.
