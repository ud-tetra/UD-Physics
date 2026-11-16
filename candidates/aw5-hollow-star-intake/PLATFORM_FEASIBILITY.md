# AW5 signed-coupling platform feasibility

**CANDIDATE / ENGINEERING ESTIMATE. Physical Promotion = 0.** This is a desk comparison. No AW5 hardware calibration or measured noise floor was supplied.

## Comparison

| Platform | Signed generator | Timing evidence | Operator calibration | Noise / readout | Disposition |
| --- | --- | --- | --- | --- | --- |
| Active analog summing integrators | One signed continuous-time state equation per simplex. Each oriented incidence contributes opposite coefficients to the two state equations. | A shared clock and trigger can support synchronized face readout. Verify effective aperture, group delay and trigger alignment with timestamp loopback. | Direct access to state voltages supports basis injections and transient identification. Check the full effective generator, including leakage, cross-talk, switch parasitics, and unmodeled dynamics. | Signed DC-capable readout is suitable in principle. Baseline offsets, drift, and filter-induced correlation need measurement. | First prototype candidate. |
| Programmable photonic interferometer mesh | A coherent mesh can compile a finite-time transformation. A single feed-forward mesh implements a finite-time map. Recirculation or a separately identified map-based realization would be needed. | Certify the optical delay and the preparation/readout reference plane against the actual storage or update clock. | Component errors, drift, loss and detector transfer enter the model. For a map-based realization, derive a sampled-map error bound with the correct units before applying the contrast analysis. | Sign-sensitive coherent detection, phase reference, loss and correlated drift need characterization. | Secondary candidate for a separately scoped propagator test. |
| Superconducting resonators | A candidate rotating-frame realization uses H=iA in the normalized model, plus a specified loss map. Tunable resonator couplers are demonstrated at smaller scope. | Certify common drive/acquisition references, group delay and the native coupling-rate conversion. | Identify signed effective couplings, detuning, residual interactions and loss as a matrix. Resonator Q alone cannot bound generator mismatch or certify dimensionless damping. | Calibrate phase-sensitive state readout and shared electronics noise. Published smaller systems do not certify AW5 face readout. | Defer until a full signed-coupling and readout proposal exists. |

Analog computer precedent documents operational summing integrators. Published nonreciprocal topolectrical circuits support signed active coupling as a candidate technique. Published photonic work describes mesh component-error limits. Resonator work demonstrates tunable two-resonator coupling and studies engineered couplings. These sources support implementation approaches. They provide no AW5 pass at the tolerances below.

- [Donner analog computing manual](https://www.analogmuseum.org/library/donner_3000.PDF) and [Chiral Voltage Propagation and Calibration in a Topolectrical Chern Circuit](https://doi.org/10.1103/PhysRevLett.122.247702)
- [Asymptotically fault-tolerant programmable photonics](https://doi.org/10.1038/s41467-022-34308-3)
- [Tunable and switchable coupling between two superconducting resonators](https://doi.org/10.1103/PhysRevB.91.014515) and [Tunable coupling engineering between superconducting resonators](https://doi.org/10.1103/PhysRevB.87.134504)
- [AD7768 data sheet and synchronization guidance](https://www.analog.com/media/en/technical-documentation/data-sheets/AD7768.pdf) and [ADS131M08 data sheet](https://www.ti.com/lit/ds/symlink/ads131m08.pdf)

## Analog feasibility calculation

Choose 1 ms per native time unit as a reversible bench design assumption. This is a laboratory emulator scaling choice, with no UD physical time identification. The 32-unit observation window is 32 ms. The midpoint grid is 8 ksample/s with maximum effective timestamp error 1/1024 ms, approximately 0.977 µs. The shortest path to proving timing is a trigger-and-readout loopback through the final acquisition filters. Multi-ADC synchronization support is available; it still requires system-level aperture and group-delay verification.

The operator error bound converts to 125/512 s⁻¹ and exterior damping to at most 125/64 s⁻¹ in this scale. Exact signed incidence has at most six nonzero entries per row and column in both carriers. For error confined to that support, entrywise error ≤ 1/49152 of a native unit coefficient gives ||E||₂ ≤ sqrt(||E||₁||E||∞) ≤ 1/8192. That assigns half of the total operator budget to supported coefficients, about 20.3 ppm per coefficient, and leaves half for leakage, cross-talk and other identified errors. This is one sufficient allocation, with independently certified matrix norms also admissible. Verify the symmetric part is negative semidefinite in the declared norm. An intentionally dissipative guard can help certify that inequality if its added error is included in the budget.

Set drive and sensor error targets ≤ 1/512 each and mean bias ≤ 1/256 per trace. The acquisition noise condition is a centered sub-Gaussian scale ≤ 1/16 with independence across the retained samples and traces. This is a 16:1 unit-amplitude to proxy ratio, roughly 24.1 dB by amplitude convention. Measured SNR requires calibration of the acquisition chain. Check analog-chain filtering and common-mode drift. A correlated-noise design needs a certified mean-error model and a protocol revision before measured scoring.

A two-state signed integrator pair with independent state taps is the first prototype. Check both coefficient signs, trigger alignment, offsets, and dissipativity with out-of-fit excitations. Establish an uncertainty-bounded induced-norm calibration procedure before replicating the pair into the full 47/46-state fixture. Disable the hub state and its couplings for the hollow configuration while retaining the face-drive and readout coordinate basis. Preserve the same loaded channel response across configurations or account for the difference.

## Run footer

- **Mission** — Compare physical platforms against the frozen AW5 acquisition limits.
- **Done** — Screened photonics, superconducting circuits, and active analog circuits and calculated a candidate bench budget.
- **Finding** — Analog is the first prototype candidate. The induced-norm generator certificate is the hardest gate in this desk screen.
- **Bridge value** — The design supports a calibrated classical emulator test. No platform has certified AW5 compliance.

## Next step

1. **Priority 90/100** — Specify the two-state signed pair, then test whether a basis-injection calibration with explicit uncertainty can establish the generator and timing budgets before full-carrier replication.
