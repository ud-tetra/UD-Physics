# Quantized charge, impedance and quantum preparation — v1.0

Status: **EXACT / CONDITIONAL** mathematical audit; charge-only universal-action selection **PARKED**. Physical score **UNSCORED**, promotion **0**. This is a new Discovery hypothesis study, not a source-ledger amendment or a fabricated apparatus.

## Question and source boundary

Does an added one-electron source remove the free action reference in the [passive port](../qpb1-passive-port/README.md)? The prior reference map was `A_map = Phi_ref^2/Z = Z Q_ref^2`. We now grant, rather than derive, `Q_ref=e>0`. The native mass-like `B0` in `A0=B0 a0^2/tau0` remains distinct from capacitance. Identifying `A_map=A0` remains a bridge premise. Canonical source object O14 is still `eta_A=A0/hbar`, with numerical value OPEN; bare G06 is not reused.

Dependencies are pinned at `467e2208fba9da086535bd5b8a6a07f6d6f8e08b` in [SOURCES.json](SOURCES.json). External reading supplies conventions, not UD bridge evidence: NIST's own single-electron program describes counted transfer/current; Vool–Devoret §§3.1.2,3.1.4.1 specify canonical circuit quantization and the LC model. See [EXTERNAL_SOURCES.json](EXTERNAL_SOURCES.json). All new consequences below are conditional constructor analysis.

## 1. Charge is an additional primitive, and impedance remains free

Grant the strongest classical reference preparation used previously: both node fluxes zero and `(Q1,Q2)=(0,e)`, with reference `Phi_ref=Ze`. Then

\[
 A_{\rm map}=e^2 Z,\qquad E_{\rm mean}=\bar\omega e^2 Z/2.
\]

For the ideal balanced two-node family

\[
 C=\begin{pmatrix}C_0+C_c&-C_c\\-C_c&C_0+C_c\end{pmatrix},\quad L=Z^2 C,
 \quad W=C^{-1}/Z=\bar\omega I+\kappa S,
 \quad g=2\kappa/\bar\omega,\quad\tau_0=2/\bar\omega,
\]

all positive scalings `s` give another allowed realization:

\[
 Z_s=sZ,\quad C_s=C/s,\quad L_s=sL,\quad W_s=W,
 \quad \Phi_{{\rm ref},s}=s\Phi_{\rm ref},
 \quad A_{{\rm map},s}=s A_{\rm map}.
\]

Proof: `C_s^{-1}/Z_s=s C^{-1}/(sZ)=W` and `Z_s^2 C_s=sL`. The native frequencies, g, clock map and normalized classical transfer are unchanged. The prepared charge stays e; its energy changes by s. Thus fixed charge plus those dynamical readouts cannot identify Z or the action scale. Independent impedance/energy measurement can calibrate a selected apparatus, but it does not select a universal UD correspondence.

This is a general positive-real nonidentifiability proof within this family. The exact rational cases are reproducible cross-checks, not its proof. Here Z is the positive constitutive impedance scale, not the frequency-dependent driving-point impedance at resonance.

## 2. Counted transfer does not fix the stored oscillator state

An ideal counted input `integral I(t)dt=e` constrains the zero-frequency component. It does not alone prescribe the canonical charge remaining in an LC resonator after its response. For an isolated mode with `L=Z/omega`, `C=1/(Z omega)`, driven through `Q_dot=-Phi/L+I(t)`, set

\[
 z=\Phi/\sqrt Z+i\sqrt Z Q,\qquad
 \dot z=-i\omega z+i\sqrt Z I(t).
\]

Starting at zero means, the final mean action is

\[
 A_{\rm mean}=|z(T)|^2
 =Z\left|\int_0^T e^{i\omega t} I(t)\,dt\right|^2.
\]

For a constant positive current `I=e/T`, it is `Ze^2 [sin(omega T/2)/(omega T/2)]^2`. At one full period it is zero, although the source transferred total charge e; an ideal instantaneous kick gives `Ze^2`. This is an ideal classical/quantum-mean drive counterexample, not an asserted single-electron device or a charge-fractionalization model. It shows why source envelope, impedance loading, timing and the actual source-to-resonator quantum channel are missing inputs. Pump count, stored canonical charge, and oscillator occupation are different observables.

## 3. Finite-energy quantum states require covariance

Now add a separate quantum model: one isolated noncompact mode on `L^2(R,dPhi)`, with `Phi` multiplication, `Q=-i chi d/dPhi`, `chi>0` an **externally supplied action constant**. Use normalized states with finite second moments and the common operator domains needed below. Time evolution is `U(t)=exp(-i H t/chi)`. Therefore the means obey the preceding LC equations. Taking `chi=hbar` recovers the usual external quantum assumption; this audit does not infer that equality or its scale.

Assume means `mean(Phi)=0`, `mean(Q)=e`. Define symmetrized centered covariance c and action-valued variances

\[
 u=\operatorname{Var}(\Phi)/Z,\quad v=Z\operatorname{Var}(Q),
 \quad c=\tfrac12\langle\Delta\Phi\Delta Q+\Delta Q\Delta\Phi\rangle.
\]

Cauchy–Schwarz applied to `Delta Phi |psi>` and `Delta Q |psi>` gives `uv>=c^2+chi^2/4`; mixtures obey the same bound. The imaginary part of their inner product is `chi/2`. In particular,

\[
 u+v\ge 2\sqrt{uv}\ge\sqrt{4c^2+\chi^2}\ge\chi.
\]

Since `H=Q^2/(2C)+Phi^2/(2L)`, direct expansion gives

\[
 \frac{2\langle H\rangle}{\omega}=e^2Z+u+v\ge e^2Z+\chi.
\]

Equality requires `c=0,u=v=chi/2`, realized by the displaced oscillator vacuum. Fixing the mean charge does not fix u,v,c. For example minimum-uncertainty squeezed Gaussians with `u=chi t/2`, `v=chi/(2t)`, `c=0`, `t>0`, have covariance action `chi(t+1/t)/2`. All have the same mean charge and different energy except reciprocal-t degeneracy. Correlated/mixed examples are included in the audit too. A state with both variances zero is inadmissible for positive chi.

A perfectly sharp Q is not a normalizable finite-energy oscillator state in this representation: its eigenfunction has constant modulus on the entire real Phi line; equivalently finite-u uncertainty forbids v=0. This statement does not apply indiscriminately to a compact-phase island/charge rotor. Such a system needs its own Hilbert space, Hamiltonian, boundary conditions and port map; it cannot be substituted while retaining this proof's assumptions.

This section applies to an isolated source at the gate endpoint or to one normal mode. It is not the total-energy formula for the full coupled two-mode apparatus: two-mode covariance and coupling terms must be retained there. The mean-state impedance obstruction in §1 already holds for that full two-node family, and does not depend on this one-mode restriction.

## 4. An energy convention can manufacture an apparent factor two

For the preceding isolated mode, with the **same supplied** chi in its commutator and time generator, define `a=(Phi/sqrt(Z)+i sqrt(Z)Q)/sqrt(2chi)`. Then `[a,a†]=1`, `H=chi omega (a†a+1/2)`. The resulting comparison is:

| Assumed preparation/readout | `2E/omega` | `2(E-Evac)/omega`, `Evac=chi omega/2` |
| --- | --- | --- |
| Displaced vacuum, mean Q=e | `e^2 Z + chi` | `e^2 Z` |
| Same means, squeezed covariance t | `e^2 Z + chi(t+1/t)/2` | `e^2 Z + chi[(t+1/t)/2-1]` |
| Number eigenstate n, zero means | `(2n+1)chi` | `2n chi` |

A one-quantum **excitation** gives `2chi`; its total energy gives `3chi`. Number states have zero mean charge, so they do not implement the assumed mean-Q=e preparation. A coherent state with mean occupation one is not a number-one eigenstate either. With charge displacement alone, its mean occupation is `e^2 Z/(2chi)`, which is continuously adjustable by Z. These alternatives require different state/readout contracts.

Consequently setting `chi=hbar`, choosing n=1, subtracting vacuum and then reporting `A0=2hbar` reuses the quantum scale and a chosen energy map. It is an explicit hypothetical correspondence, not an independent recovery of hbar or selection by electron count. Choosing `Z=2hbar/e^2` from the exposed target has the same target-informed status. No such impedance is selected by this study.

## 5. Decision, limits and reproduction

**PARKED:** the claim that quantized transferred charge alone selects a universal native action unit in the balanced linear port. **RETAINED:** conditional analogue with a declared charge reference, independent apparatus calibration, and an explicit state/energy convention. A source law selecting Z, a correspondence selecting native support, and an actual state-preparation/readout channel remain OPEN. No all-model quantization no-go, empirical falsification or mainline promotion follows.

The audit checks six exact two-node fixtures under five impedance scalings (30 comparisons); a 5-by-3 squeezed covariance bank (15 cases), four correlated/mixed covariance cases, five charge-displacement examples, and number-state algebra for n=0..5 (six cases). It independently checks the displacement energy using both covariance and occupation forms. These are constructor checks. There is no separate LLM review or experimental replication.

Run from the repository root:

```bash
python3 experiments/qpb1-quantized-charge/audit.py --out /tmp/qpb1-charge-output
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The audit uses only the Python standard library and existing exact matrix helpers. All rational fixture values are abstract coherent-unit examples; chi in the fixtures is a symbolic coefficient choice, not a measurement of hbar. The documented positive-real proofs and differential-equation solution cover the general statements; finite fixtures do not certify arbitrary devices or infinite-dimensional operator domains.

See [the receipt](../../sessions/qpb1-quantized-charge-20261022-a1/mathematical_receipt.json), [preparation contract](PREPARATION_CONTRACT.md), and [immutable run](../../artifacts/qpb1-quantized-charge-20261022-a1/exact-001/manifest.json).

Next discriminant: audit the native source ledger for an actual impedance/constitutive selection law, with its units and provenance. If none is available, retain the circuit as a calibrated analogue and identify the extra hypothesis needed; do not choose an impedance from the eta target.
