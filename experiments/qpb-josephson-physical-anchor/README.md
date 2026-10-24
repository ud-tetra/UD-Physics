# Ideal Josephson junction as an independent physical constitutive benchmark

**RESULT — EXACT / CONDITIONAL physical-model sign test; NUMERICAL example; FAILED positive-star mapping; OPEN UD physics.**

This is a separate Discovery physical-anchor test, not a continuation or overwrite of the parked constitutive coefficients in PR #87. The Josephson constitutive relation is grounded in conventional superconducting-circuit physics, and its constants and observable physical units are distinct from native UD quantities. We find a sign contradiction for one explicit positive-star UD mapping. This is **not** evidence of unique UD dynamics or a general no-go against other UD constructions.

## Versioned sources, question and provenance

- External conventional physical source: Rasmussen et al., *Superconducting Circuit Companion*, PRX Quantum **2**, 040204 (14 December 2021), DOI https://doi.org/10.1103/PRXQuantum.2.040204 — ideal Josephson current-phase relation, flux-phase relation, and Josephson cosine energy. The source provides conventional theory, **not** a UD identification.
- External analytical reference: *Phase-tunable thermoelectricity in a Josephson junction*, Physical Review Research **2**, 043091 (2020), https://doi.org/10.1103/PhysRevResearch.2.043091 — finite-amplitude pendulum/elliptic-integral frequency context.
- External unit authority: BIPM, https://www.bipm.org/en/measurement-units/si-defining-constants — exact SI values of h and e; flux quantum Φ0=h/(2e) follows from Josephson theory.
- Versioned read-only UD-Physics imports at integrated main \`5fd737fda4dadd6f1cc3d9c3c6c086473b7f72bb\`: [unit preparation](../qpb1-unit-preparation/README.md), [impedance selection](../qpb1-impedance-selection/README.md), and [charge-field analogue](../qpb1-charge-field/README.md). The parked positive-star branch at PR #87, commit \`86d2a86570c807bc980819809312cd3255a2852a\`, remains **unmerged and read-only**. The specific hidden-star energy imported as a hypothetical comparator is \`H=||x||²/2+λr3²/4\`, λ>=0, r3=x^T P3x.
- Question: can a physical nonlinear element supply a coefficient/sign without using the old UD phase target, and does a zero-amplitude-matched UD hidden-star model agree with it?

## Native versus physical definitions and dimensional map

Physical ideal lumped circuit: a zero-current-biased, lossless Josephson junction in parallel with total capacitance C>0; positive critical current Ic>0; gauge-invariant superconducting phase *difference* \(\varphi\in\mathbb R\) within one potential well, with turning amplitude \(0\le a<\pi\). Define the full flux quantum \(\Phi_0=h/(2e)\), reduced flux \(\phi_0=\Phi_0/(2\pi)\) in weber, and Josephson energy \(E_J=I_c\phi_0\) in joules. For physical seconds \(t\),
\[
I=I_c\sin\varphi,\qquad V=\phi_0\,d\varphi/dt,
\qquad U_J(\varphi)=E_J(1-\cos\varphi).
\]
For capacitor charge \(Q=C V\), the Hamiltonian is \(Q^2/(2C)+U_J(\varphi)\). In the phase coordinate, the effective inertia is \(M=C\phi_0^2\) (joule-seconds-squared), so the closed equation is
\[
M\ddot\varphi+E_J\sin\varphi=0,\qquad
\omega_0=\sqrt{E_J/M}=\sqrt{I_c/(C\phi_0)}.
\]
This is a **conventional physical constitutive law** with a nonlinear shape fixed by the sinusoidal relation; its apparatus-dependent *scales* Ic and C must be independently determined for an actual experiment. They are not native UD source selections.

The UD hidden sector remains a separate real two-plane defined using the oriented tetrahedral chain projector P3, metric H=I and internal J=A/2, with \(\dot x=A\nabla H_{\rm UD}\) in *dimensionless native time* s. Identifying physical seconds via \(t=\tau_0s\) with \(\tau_0=2/\omega_0\) is an **assumed calibration** matching only the linearized frequency. Identifying the superconducting \(\varphi\) with any internal UD J-fiber angle is a **separate, unproved mapping**: the two U(1) notions are not identical merely by nomenclature. For the sign test postulate an amplitude correspondence \(r_3=\kappa a^2\), \(\kappa>0\), with zero amplitude mapped to zero. The numerical value of \(\kappa\) is unspecified and not fitted.

## Exact finite-amplitude frequency law and sign

For the physical pendulum turning at amplitude a, energy conservation yields
\[
T(a)=\frac{4}{\omega_0}K(\sin(a/2)),\quad
\frac{\omega(a)}{\omega_0}
=\frac{\pi}{2K(\sin(a/2))}
=\operatorname{AGM}(1,\cos(a/2)).
\]
Here K is the complete elliptic integral of the first kind, and AGM is the arithmetic–geometric mean; this is exact for the ideal nondissipative equation and \(0\le a<\pi\). If \(0<a<\pi\), then \(0<\cos(a/2)<1\), so AGM lies strictly between zero and one. Consequently **all nonzero trapped physical oscillations are softer** than the harmonic limit.

Expand \(K(k)/(\pi/2)=1+k^2/4+9k^4/64+O(k^6)\), and \(k^2=\sin^2(a/2)=a^2/4-a^4/48+O(a^6)\). With exact rational arithmetic:
\[
T(a)/T(0)=1+\frac{a^2}{16}+\frac{11a^4}{3072}+O(a^6),
\]
\[
\boxed{\omega(a)/\omega_0=1-\frac{a^2}{16}+\frac{a^4}{3072}+O(a^6).}
\]
The sign is fixed by the current-phase law, not selected by the earlier UD target.

The earlier positive quartic UD comparator, with the same native zero-amplitude linearization, obeys
\[
H_{\rm UD}=\frac12\|x\|^2+\frac{\lambda}{4}r_3^2,\quad
\omega_{\rm UD}(r_3)/\omega_{\rm UD}(0)=1+\lambda r_3,\quad \lambda\ge0.
\]
Under \(r_3=\kappa a^2\), its leading amplitude coefficient \(\lambda\kappa\ge0\) cannot equal Josephson's \(-1/16\). Thus **FAILED / CONDITIONAL** for the specified positive-star UD mapping. This does *not* rule out a negative local quartic over bounded amplitudes, a bounded nonlinear energy, a new primitive, a different amplitude map, or an independently sourced UD constitutive law. Matching this physical slope by allowing negative λ requires λκ=-1/16, **a physical-data/backsolved FIT**, and the naked negative quartic H is not globally coercive. The complete conventional cosine potential already supplies a stable physical law without any UD hypothesis.

## Reproducible design-only numerical example

For *illustration only*, choose Ic=100 nA and total C=100 fF, both **design inputs, not measurements**. SI h and e are exactly defined; the derived low-amplitude frequency is about 8.773083155 GHz, and the assumed UD time scale would be \(\tau_0=3.62825566064716\times10^{-11}\) seconds per native unit.

| Physical turning amplitude a (rad) | Conventional Josephson \(\omega(a)/\omega_0\) | Equal-magnitude positive UD hardening toy |
|---|---:|---:|
| 0 | 1.0000000 | 1.0000000 |
| 0.2 | 0.9975005 | 1.0025000 |
| 0.4 | 0.9900082 | 1.0100000 |
| 0.6 | 0.9775407 | 1.0225000 |
| 1.0 | 0.9377923 | 1.0625000 |

The positive UD illustrative curve in the last column chooses λκ=1/16 **for equal slope magnitude only**; it is not a physical fit or native coefficient. The sign contradiction holds for every λ>=0, κ>0 without selecting that magnitude. No numerical values of observed laboratory residuals or instrument uncertainties have been invented.

## Exact and numerical reproducibility

From this repo branch run:
\`python3 experiments/qpb-josephson-physical-anchor/anchor.py --out /tmp/ud-jj-anchor-summary.json\`.

Standard-library Python uses exact SI-decimal-to-rational h/e, exact fractions for the two leading Taylor coefficients, an arithmetic–geometric mean and a separate 8,192-interval Simpson integral for K. Five constructed amplitude cases agree between the independent numerical formulae within 1e-11, with four strict softening sign checks. The [immutable captured run](../../artifacts/qpb-josephson-20261024-gpt6-a1/jj-001/manifest.json) holds source and output SHA-256. Constructor crosschecks do not constitute experimental reproduction or a separate referee.

## Null, discriminating experiment and limitations

The explanatory baseline is the **ordinary ideal Josephson junction pendulum** using the independently specified Ic,C and nonlinear sinusoidal constitutive relation. It predicts the full elliptic frequency curve; there is no incremental UD prediction from reproducing it.

Prospective target-blind protocol: (i) independently characterize the junction's Ic, effective total capacitance C, bias and losses; (ii) calibrate physical peak phase from a physical flux/voltage measurement that does *not* assume UD amplitudes; (iii) freeze the model and instrument error budget; (iv) record amplitude-dependent periods at a=0.2,0.4,0.6 rad and compare signed residuals with the ordinary Josephson null, the positive-star comparator, and any separately frozen UD bridge; (v) reject or revise the comparator if softening occurs as the standard law predicts. Phase noise, quantum corrections, junction harmonics, damping, capacitor dispersion and mode coupling need independent quantification in real hardware. None of these experiments is executed here.

**Disposition:** physical source of a *conventional* nonlinearity is identified, and it gives an independent counterexample to the positive-star UD mapping; the native-to-physical correspondence, measurement data and a unique UD mechanism remain OPEN. No mainline promotion, no merge of parked phase-009 PR, and no empirical success claim.

**NEXT (priority 97/100):** seek a UD-native constitutive selector that predicts *before* looking at physical data a sign and scaling different from or more constrained than the conventional Josephson null; separately specify a physical 15-port transducer and held-out experiment. Otherwise preserve this as an exact negative benchmark rather than forcing a fit.


## JJ-002 public empirical source audit

[Joint plasma fit provenance, physical-unit re-expression, and absent amplitude heldout](EMPIRICAL_SOURCE_AUDIT.md). Bias-dependent small-signal resonance is distinct from zero-bias oscillation amplitude; no experimental UD bridge is claimed.
