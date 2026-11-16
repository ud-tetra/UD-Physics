# AW5 signed-pair bench data intake v1

**SOFTWARE VERIFIED ON SYNTHETIC INPUTS. Physical Promotion = 0.** Hardware calibration, certificates, and measured trace scoring remain open.

Run `python3 bench_pair_intake.py packet.json > receipt.json` with NumPy and SciPy. The receipt includes the SHA-256 of the input bytes. Run `python3 replay_bench_pair.py` to verify the synthetic fixtures. The fixture function also illustrates the full JSON structure.

| JSON field | Input contract |
| --- | --- |
| protocol, evidence | AW5-PAIR-v1 and either SYNTHETIC or MEASURED. Preserve evidence label and audit origin in the submission. |
| timing | 256 effective midpoint timestamps in ms relative to the impulse reference and a nonnegative upper bound uncertainty_ms. The score adds uncertainty to the maximum observed deviation from (2k+1)/16 ms for k=0,…,255 and compares the sum to 1/1024 ms (0.9765625 µs). The timing budget is independent of the nominal damping parameter. Decimal JSON timing inputs are evaluated exactly, and the receipt reports the exact sum as loopback_error_ms_exact alongside its numeric rendering. |
| shots | +e1, -e1, +e2, -e2. Each contains two rows, start then endpoint, each with both normalized state coordinates. The endpoint is at nominal h = 1/8 native units. Use signed, paired measurements after the impulse reference. |
| certificate | References for clock_reference, endpoint_uncertainty, lti_scope and loss_model. Supply nonnegative generator_norm_upper, delta_x and delta_y (induced 2-norm bounds of the reduced endpoints), and map_numerical_allowance and generator_numerical_allowance. The latter two are numerical inflations for map/radius and generator/gate calculations. |
| heldout | At least two independently preserved comparisons spanning mixed input and changed input amplitude. Each supplies time_native, start, end, start_error, end_error and numerical_allowance. Use the actual model reference and include timing uncertainty in endpoint bounds. |

Retain zero-input shots, gain/offset calibration, pulse and clock provenance with the endpoint certificate. The scorer consumes references and bounds; their evidentiary sufficiency needs separate audit. The 256-point loopback certifies the acquisition grid only. The endpoint matrix uncertainties must separately include the conditioning-sensitive timing, loading, gain, drift and filter errors. The declared common-bleed plus selective face-loss model is required for the loss interval. The assessment uses the previously specified 2-norm logarithm radius and dissipativity condition. Held-out comparisons use a contraction-based residual bound, evaluated as a gate only when dissipativity is certified.

PASS_CONDITIONAL means the packet's supplied bounds meet the unit-cell criteria. FAIL_GATES means the packet was scored and a recorded gate missed. INADMISSIBLE identifies incomplete or unusable input, including an uncertifiable initial span or a transition outside the logarithm radius. A pass from this tool reaches the two-state calibration scope only. The separate AW5 contrast scorer still admits synthetic data only.

See [refined-carrier intake scope](REFINED_INTAKE_SCOPE.md) for the audit of parasitic or intentional subdivisions.

## Raw archive preflight

Verify the custodian's signature, timestamp, and role-key chronology through the custody record. Then run the preflight against the authenticated SHA-256 manifest and the raw delivery directory. The expected manifest uses the standard sha256sum line format with paths relative to the delivery directory.

```bash
./aw5_archive_preflight.sh /path/to/expected.sha256 /path/to/raw > preflight.json
```

The script requires Bash and Python 3.11 or later. It checks every listed raw file before inspecting any formats and emits a JSON result. A missing file or SHA-256 mismatch skips format inspection for the entire batch. After all digests match, format inspection checks delimited-text structure for CSV and container metadata for ZIP and gzip tar. It performs no extraction, waveform conversion, or scoring. Preserve the JSON result with the authenticated manifest and the original bytes. The receipt itself is ordinary JSON. Instrument certificates and trace-specific validation are separate inputs to measured intake.

## Run footer

- **Mission** — Prepare the formal intake for timing-loopback and signed basis-injection records.
- **Done** — Implemented a machine-readable gate receipt and replayed nominal, timing, held-out, missing-evidence and rank-deficient fixtures.
- **Finding** — The prototype distinguishes independently scoped gate shortfalls from unscorable input.
- **Bridge value** — Bench packets can now be reduced consistently once the underlying measurements and certificates are supplied.

## Next step

1. **Priority 92/100** — Acquire the timing-loopback and paired basis shots with held-out mixed inputs. Audit their certificate sources, then run the unchanged unit-cell intake.
