# Radius-12 clock alignment and gain replay v0.1

**NUMERICAL / CONDITIONAL.** Compare terminal position offsets and complex gains for the matched-frequency site-clock readout.

## Test contract

Discovery parent d5390bd3a627ba0dd4b6b14862390329d27a90bc. Retain [Tracked phase v0.1](TRACKED_CURRENT_CLOCK.md) and [Window noise v0.1](WINDOW_NOISE.md), including the scalar transport generator, passive local clock rule, lattice metric, window stock normalization, and radius 12. No refitting. At native time 12 apply independently to each detector an integer offset in [-2,2]^3. This tests 125 offsets per channel. The radius is Euclidean in lattice coordinates. Reconstruct the additional sites and integrate their fixed site clocks from launch. Offsets change only the terminal observation mask. The default radius-three replay is byte-identical after the new parameterization.

Let U_r be the offset readout divided by launch total stock. Apply a spatially uniform complex gain per detector, U'_r = a_r exp(iφ_r) U_r, with amplitude a_r in [9/10,11/10]. Phase bounds are 0, 1/400, and 1/160 rad per detector, with adversarial opposite signs. With no wrap over these phases, positive gain amplitude leaves phase unchanged and the worst gap is the smallest offset gap minus twice the gain-phase bound. The replay applies gain corners to the complex readouts and compares against this formula. A common phase gain cancels. The amplitude floor matters for additive noise after gain.

Require at least half the nominal zero-offset, zero-gain-phase gap. If the worst gap after position and gain errors is g and the nominal gap is Δ, the shared additive budget is min|U'| sin((g−Δ/2)/2) when g≥Δ/2 and no positive budget otherwise. This follows from the exact disk-angle bound of Window noise v0.1 and uses the weakest signal over allowed offsets and amplitudes. There is no stochastic noise model.

## Results and limitations

At native time 12 the finer replay gives nominal gap 0.01177996778 rad. Independent sampled offsets reduce it by at most 1.57×10⁻¹⁰ rad. The smallest captured stock fraction across both channels and all offsets is 2.16045×10⁻⁵. The gain sweep gives:

| Phase cap per detector | Worst remaining gap (rad) | Additive budget per launch stock |
| ---: | ---: | ---: |
| 0 | 0.01177997 | 5.73×10⁻⁸ |
| 1/400 | 0.00677997 | 8.65×10⁻⁹ |
| 1/160 | −0.00072003 | Half-gap fails |

The two replays agree at the displayed precision. The half-gap threshold for the magnitude of differential gain phase alone is approximately 0.00588998 rad over this sampled offset set. This is conditional on the numerical gap and the stated uniform gain model.

The sweep uses Gauss order 8 with trapezoid step 1/4 and order 12 with step 1/8. The reported numbers are numerical estimates and do not certify unsampled offsets, nonuniform gains, or time-dependent tracking. The two gain settings test retention of the half-gap and an adversarial sign reversal. The gain model and tolerances are test choices, not measured hardware parameters.

Replay with `OPENBLAS_NUM_THREADS=1 python3 experiments/clock-matrix-question/clock_alignment.py`. Physical promotion 0. Independent review NOT_RUN.
