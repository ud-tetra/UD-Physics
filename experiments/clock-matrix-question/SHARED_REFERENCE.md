# Shared reference phase calibration v0.1

**EXACT / CONDITIONAL.** A shared reference cancels arbitrary differential detector gain phase if each detector applies the same nonzero complex gain to its science and reference readings. The reference contributes its own additive phase uncertainty.

## Calibration contract

Discovery parent 6964c47c89b9dd661e98b50115b63b361c170b3c. Retain the terminal radius-12 offset sweep, uniform gain model and half-gap criterion of [Clock alignment v0.1](CLOCK_ALIGNMENT.md). Work with complex terminal readouts divided by launch total stock, in the same declared normalization for science and pilot. For detector r, write S_r=g_r U_r exp(iδ_r)+e_r and P_r=g_r R exp(iψ)+n_r. Here U_r is the ideal window phasor, R>0 is pilot amplitude, ψ is its common phase, g_r is a nonzero complex gain, δ_r is residual path phase mismatch, and e_r,n_r are errors after gain. The science and pilot must see the same gain at the readout or any differential phase must be included in δ_r. In the absence of additive errors the ratio S_r/P_r has phase arg U_r+δ_r−ψ. Differencing the two ratios removes ψ and both gain phases exactly. No physical pilot delivery or drift control is assumed.

## Error bound and replay

Let g be the smallest gap across prior sampled offsets, Δ the nominal gap, b the cap on each |δ_r|, and S and P the post-gain magnitude floors for science and pilot. For a common absolute additive error E below both floors, the disk-angle bound gives a worst differential perturbation of at most 2[asin(E/S)+asin(E/P)]. To retain Δ/2 require that sum to be at most g−Δ/2−2b. For positive spare and h=(g−Δ/2−2b)/2 in (0,π/2), the common bound is

    E = sin(h) / sqrt(1/S² + 1/P² + 2 cos(h)/(SP)).

This follows by resolving the sum of the two disk angles. The replay applies tangent perturbations to both channels and both pilots to attain the half-gap on the floor model. It uses both saved refinements of the position sweep. The science floor S is recovered from the zero-phase budget in that replay by dividing it by sin((g−Δ/2)/2). Pilot ratios P/S are test choices. The finer science floor is approximately 1.94440×10⁻⁵ of total launch stock.

| Pilot floor relative to S | Shared additive error budget at b=0 | Shared budget at b=1/400 rad |
| ---: | ---: | ---: |
| 1 | 2.86312×10⁻⁸ | 4.32621×10⁻⁹ |
| 4 | 4.58099×10⁻⁸ | 6.92194×10⁻⁹ |
| 10 | 5.20567×10⁻⁸ | 7.86584×10⁻⁹ |

Budgets are fractions of launch stock per phasor. At opposite injected gain phases ±1/160 rad and b=0 the uncalibrated gap is −0.00072003 rad. Ratio calibration restores approximately 0.01177997 rad before additive noise. The matched path condition is consequential: with residual mismatch 1/400 rad per detector, the restored gap falls to approximately 0.00677997 rad. The computations use synthetic complex gains and a shared pilot, with no apparatus, stochastic noise or empirical calibration. Physical promotion 0. Independent review NOT_RUN.

Reproduce with `python3 experiments/clock-matrix-question/shared_reference.py` using the saved clock-alignment JSON beside the script.
