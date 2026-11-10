# JJ-003 — Higher Josephson harmonics, accessible spectroscopy provenance, and sign-test scope

**RESULT — EXACT / CONDITIONAL:** A two-harmonic conventional Josephson current–phase relation can produce a positive finite-amplitude frequency shift. Therefore the JJ-001 softening-versus-UD-hardening contrast is **specific to the ideal single-sine junction**, not a universal physical sign rule. **EMPIRICAL SOURCE:** measured higher-harmonic effects in multi-level superconducting-qubit spectroscopy have been published with a public dataset pointer, but the raw spectroscopy bytes were NOT_ACQUIRED here. No classical turning-phase amplitude sweep or held-out UD physical test was performed.

## Verifiable primary sources and data-access scope

Willsch et al., *Observation of Josephson harmonics in tunnel junctions*, Nature Physics **20**, 815–821 (2024), published 14 February 2024, https://doi.org/10.1038/s41567-024-02400-8. Publisher correction 4 April 2024, https://doi.org/10.1038/s41567-024-02491-3, corrects swapped bibliography references 87/88 to the dataset. The article experimentally measures superconducting **transmon transition frequencies** f_0j to higher energy levels across several laboratories, and compares standard cosine Hamiltonian to higher-harmonic models. It reports deviations for f_03 greater than 10 MHz in some samples, compared with a conservative measurement imprecision on the order of 1 MHz; the full harmonic models achieve improved agreement. The authors also discuss percent-level higher Josephson harmonics. These are **empirical published article statements**, not a new reanalysis in this task.

The corrected data DOI is https://doi.org/10.26165/JUELICH-DATA/LGRHUH, "Spectroscopy Data and Model Parameters for: Observation of Josephson Harmonics in Tunnel Junctions", Willsch & Rieger (2023). The live Dataverse landing page lists version 2, an accessible 97-byte README, and the project location https://jugit.fz-juelich.de/qip/josephson-harmonics. The GitLab raw/README route currently presents an automated-access verification challenge to this session. We do not bypass that access protection. **DATA ACCESS STATUS:** public provenance and repository location verified; raw spectroscopy files, measurement covariance and model parameters NOT_DOWNLOADED / NOT_AUDITED. The DOI is a valid source locator, not proof we have imported its measurements.

Crucial observable distinction: transmon f_0j transition spectra are **quantum energy-level differences**, not a calibrated classical zero-DC-bias oscillation turning amplitude a versus frequency omega(a). They cannot be used as a classical phase-amplitude dataset by treating the integer level j as a physical phase amplitude. A future quantum test needs a separately specified UD Hilbert space, action/commutator scale, state identification and measurement map. Neither the 2024 paper nor its raw repository alone supplies those UD assumptions.

## Exact independent two-harmonic physical model

Take an ideal, zero-bias, lossless lumped Josephson phase oscillator with a positive inertial coefficient M, I1>0, and an *added* second harmonic with real coefficient q=I2/I1:

I(phi)=I1 sin(phi)+I2 sin(2phi).

Let E1=I1 Phi0/(2pi) be a physical energy scale, and set U(phi)/E1 = (1-cos(phi))+q*(1-cos(phi)^2). This produces current as U'(phi) times the inverse flux-phase factor. The phase origin is a stable equilibrium if U''(0)/E1=1+2q>0; so q>−1/2 is the local-stability domain, provided I1>0.

Taylor expand around phi=0:
U(phi)/E1 = (1+2q)phi²/2 - (1+8q)phi⁴/24 + O(phi⁶).

For a conservative oscillator in a local well, with *physical turning-phase amplitude* a, standard weak-nonlinear period perturbation gives the exact leading coefficient

omega(a)/omega(0)=1-[(1+8q)/(16(1+2q))] a² + O(a⁴).

The same result for a general multiharmonic CPR I(phi)=sum_m I_m sin(m phi) is

omega(a)/omega(0)=1-[sum_m m³ I_m /(16 sum_m m I_m)] a²+O(a⁴),

assuming a stable equilibrium sum_m m I_m > 0, convergent sums, constant positive inertia, and small a. This formula is a CONDITIONAL model theorem, not a measured harmonic coefficient.

For the sine-only ideal q=0, the leading correction is −a²/16, as in jj-001. For an illustrative stronger negative harmonic q=−1/4 (NOT measured in the 2024 paper), curvature at zero is 1/2>0, the leading correction is +a²/8, and the potential is **globally nonnegative**:
U/E1 = (1-cos(phi))*(3-cos(phi))/4 >=0.
Thus a conventional Josephson-like periodic energy can **harden** near equilibrium while having a stable well. The mathematical hardening interval in this two-harmonic family is −1/2<q<−1/8. At q=−1/8 the a² coefficient vanishes and higher orders decide the response. This shows that hardening itself is not an exclusive UD signal.

**Evidence limit:** The published paper's percent-level harmonics do not establish that any of its measured samples lies in this sign-reversal interval. The q=−1/4 example is a deliberately chosen constitutive counterexample, and must never be presented as a measurement or fitted value from the source.

## Numerical constructor and conventional baseline

Run from repository root:

python3 experiments/qpb-josephson-physical-anchor/harmonics_audit.py --out /tmp/ud-jj003.json

The executable uses exact fractions for the leading coefficients and positivity test. It independently computes the finite-amplitude period by 4,096-panel Simpson quadrature of the energy integral with an analytic endpoint limit. For q=0 it agrees with jj-001's exact AGM frequency at a=0.4 rad to less than 2e-10. For q=−1/4, the normalized frequency at a=0.4 rad is approximately 1.0188746247532; at q=0 it is approximately 0.9900082042903. These are **NUMERICAL predictions of two selected conventional circuit models**, not raw experiment or observed UD deviations.

Input source SHA-256: 51bf4b8301c11beb44b1e16d0195ddf55739242819cc37dfe1a591b05677d9d1; output SHA-256: 621b64bd5adc8c29485279b9c05be04b86894c8a8483106ab82b8f7e29bf6248. See the immutable [jj-003 artifact manifest](../../artifacts/qpb-josephson-20261024-gpt6-a1/jj-003/manifest.json). Earlier jj-001 (ideal sine) and jj-002 (published bias-fit audit) bytes were not altered.

The correct explanatory baseline is the **conventional physical Josephson current–phase relation with allowed harmonics and the same calibration/parameter budget**. It reproduces the sign and observable entirely without UD. Allowing harmonic coefficients to be fitted after seeing the spectrum entails additional degrees of freedom and model-selection exposure; a genuinely held-out test must freeze them first. There is still no UD-native sign/coefficient selector or physical superconducting-phase to J-fiber map.

## Status and next discriminant

**EMPIRICAL:** 2024 published transmon spectroscopy and its DOI are independently sourced. **NOT_ACQUIRED:** actual raw measured f_0j tables and model files. **EXACT/CONDITIONAL:** higher-harmonic leading shift and conventional hardening counterexample. **NUMERICAL:** selected model integration. **FAILED:** interpreting sine-only Josephson softening as a universal physical sign discriminant. **OPEN:** calibrated classical amplitude-frequency dataset and physically derived UD quantum/classical port map. No external non-constructor review, raw held-out regression, laboratory measurement, unique UD physics, or mainline promotion.

**Next action, priority 98/100:** (a) for a genuine classical amplitude test, seek independently calibrated peak-phase a and period/frequency observations, with a frozen realistic multi-harmonic CPR/null; (b) as a separate and potentially higher-yield *quantum spectroscopy frontier*, retrieve the actual Jülich/GitLab transmon f_0j tables through ordinary authorized access and define a distinct UD quantum Hamiltonian and scale **before** any use of high-j data. If neither dependency is met, retain the exact mathematical counterexample and park unique physical attribution.
