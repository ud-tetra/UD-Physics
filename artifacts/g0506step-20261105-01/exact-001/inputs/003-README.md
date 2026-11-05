# QPB1 unit-preparation audit v1.0

**Development — no registry entry. EXACT / CONDITIONAL / OPEN.** A target-independent physical preparation can define an analogue's action scale. A separate correspondence is needed to identify that reference with the universal native action unit. Neither a normalized ray, an integer count nor a native amplitude attractor supplies that physical identification.

Source base: UD-Physics `7ae79d882e44446c7b4aefd4fdbe9ee781b9bafe`. This extends the [carrier/anchor audit](../qpb1-carrier-anchor/README.md). The candidate eta_A=2 was exposed before this work. No numerical hbar input, physical data or empirical score is used. [Source bindings](SOURCES.json), [prospective preparation protocol](LC_PREPARATION.md), [exact audit](audit.py), [mathematical receipt](../../sessions/qpb1-unit-preparation-20261022-a1/mathematical_receipt.json), [captured run](../../artifacts/qpb1-unit-preparation-20261022-a1/exact-001/manifest.json).

## 1. Source findings and limits

The supplied ledger v0.39 is a historical snapshot. Its G05/G06 and Q139 already leave action normalization, physical scale or generator identification open. The recovered ledger archive labelled v0.85, pinned through the preceding audit to UD commit `957d443e25008632ab9d9328c162343b6a651ee7`, adds more precise statements:

| Source object | What it supplies | What remains separate |
| --- | --- | --- |
| Q181 | Reconstruction of a normalized positive-ray representative | Physical preparation and measurement |
| Q282–Q286 and C0906 theorem §§5–6 | Specific native action scale A0/2; a unit-norm representative | Physical support quantization and physical units |
| O10/O15 | A0=B0*a0^2/tau0, with B0 mass-like | Native-to-physical anchors |
| O14 | eta_A=A0/hbar direction | Numerical physical ratio |
| Q287/Q288 | Quarantined QPB1 map and candidate ratio2 | Independent physical A0 anchor |
| Q378 | A discrete winding-formation increment | Its source law; no unit-amplitude rule follows |
| O54/O55 | Physical anchor open; frozen candidate/test control | Executed independent anchor packet |

The supplied `carrier_definition.md` and `master_action.md`, and those two corresponding ZIP entries, contain placeholder text. The other seven short equation/transport files inspected are also placeholders. The dependency map describes a programme but supplies no calibration/preparation law. The historical Gap2 status concerns cosmological simulations and is not an action-anchor receipt. No claim here depends on its observational assertions. The unavailable Genesis image was not used.

The ledger search was bounded: fourteen action rows plus Q181 and Q378 were inspected, with a declared keyword scan over all723 rows. It is not a proof that no rule exists anywhere in the UD archive. The PDFs and the remainder of the ZIP were not inspected for this audit. Uploaded source text is evidence, not executable runtime authority. The supplied governance amendment remains a proposal; this work stays in its development lane and claims no promotion or non-constructor review.

## 2. The original linear flow cannot select norm

Use the filled tetrahedron, f=(4,6,4,1), real chain dimension15 and unit metric. With ascending oriented simplices,

\[
A=d-d^T,\qquad P=-A^2/4,\qquad J=A/2,\qquad J^2=-P.
\]

On the active real14-dimensional sector, a=||x||^2 is conserved because A is skew. Thus the original closed evolution cannot attract preparations of different norms to a=1. Choosing the normalized representative x/sqrt(a) is a state/readout convention, not such an evolution or a physical preparation.

## 3. Integer-amplitude selection: an exact conditional obstruction

Integer simplex counts do not imply integer state amplitudes. Nevertheless, test the explicit alternative

\[
\Lambda=\mathbb Z^{15}\cap\operatorname{im}P.
\]

Every nonzero x in Lambda has integer squared norm at least1. A unit edge vector e is active and attains1. Therefore an added minimum-nonzero-support rule would select a=1 on this lattice. This is a new amplitude-domain and selection assumption, not a consequence of f-counts or binary receipt labels.

It conflicts with the original nonstatic continuous active flow. At native time s=pi/4,

\[
e^{As}e=Je.
\]

Je has four entries of magnitude1/2 and all other entries zero, so it has unit norm but is not an integer vector. More generally, a continuous trajectory entirely inside a discrete lattice must be constant; the active generator has no nonzero stationary state.

For this particular Lambda, the phase rotations preserving the entire lattice are exactly phi=0 or pi modulo2pi. The edge coordinate of exp(phi J)e is cos(phi), which must be an integer. The alternatives cos(phi)=0 give plus/minusJe, which is not integral; the remaining alternatives give plus/minusI on the active sector. Consequently a sampled clock with native step pi/2 can preserve Lambda through the sign flip -I, with nonzero orbit length2. This is a different sampled-state model: it does not make the intervening continuous trajectory integral or supply a physical tick duration. Other lattices or dynamics define other branches.

Allowing rational amplitudes instead does not give a minimum: e/n is active and has support1/n^2 for every positive integer n. The positive supports have infimum0. Twelve exact members of this sequence and the quarter-phase witness are computed; the proof applies to all n.

### An integer preparation event is a distinct, admissible alternative

The lattice obstruction does not prohibit an integer-valued preparation followed by real-valued evolution. An explicitly added reset/source rule x=0 followed by x_plus=e_cell, where e_cell is the unit oriented top-cell vector, prepares support1; the subsequent original Hodge motion preserves it. No all-time lattice restriction is required. This is a possible native preparation hypothesis, not a source-derived birth/reset law or a physical calibration.

Repeated unit injections do not generally give one support unit per event. For any kick u,

\[
\Delta a=\|u\|^2+2\langle x,u\rangle.
\]

For two identical top-cell kicks separated by phase phi, support after the second is2+2cos(phi), ranging from0 to4. Eight exact rational phase cases verify the balance, including reinforcement and cancellation. Thus a binary event count does not by itself quantize the retained support. Orthogonal preparation, phase conditioning, incoherent averaging or isolated reset cycles would require additional source/environment rules and accounting. In particular, reset costs and outgoing records cannot be omitted. Even a valid isolated native unit injection still needs a physical kick magnitude and the map selecting the dimensional action scale.

## 4. A native amplitude attractor still leaves a physical scale

As a constructive alternative, add the following explicitly hypothetical source/sink law on the active sector:

\[
x'=Ax+\gamma(1-\|x\|^2)x,\qquad\gamma>0.
\]

Then

\[
a'=2\gamma a(1-a),\qquad
a(s)=\frac1{1+(1/a(0)-1)e^{-2\gamma s}}.
\]

Every a(0)>0 tends to1; the zero state stays zero. The phase rate remains2. The law adds or removes support off the unit sphere and therefore changes the original conservative dynamics. Gamma and the feedback mechanism have not been derived from a UD source. Sixteen rational identity checks supplement the differential-equation derivation.

This demonstrates that native norm selection and physical action calibration are distinct. Under the previous mechanical map q=LQ, p=-m*omega*L*P, the selected native unit circle has physical amplitude L and action unit m*omega*L^2. A different physical mapping L->cL changes this unit by c^2. The same native attractor exists in both descriptions. A physical feedback threshold can select L operationally, but that threshold is an additional dimensional input whose source and calibration must be supplied.

## 5. A concrete target-independent analogue preparation

Postulate an ideal isolated single-mode LC carrier with positive capacitance C and inductance ell. Define flux Phi and charge Q_ch as canonical coordinate and momentum:

\[
\dot\Phi=Q_{\rm ch}/C,\qquad
\dot Q_{\rm ch}=-\Phi/\ell,\qquad
\omega^2=1/(\ell C),
\]
\[
E=Q_{\rm ch}^2/(2C)+\Phi^2/(2\ell).
\]

This is an assumed classical model, not a newly measured circuit or the full C7 quantum carrier. Prepare zero current/flux and a capacitor precharge V_ref selected without the candidate action relation. Let Phi_ref=V_ref/omega. One active native plane maps as

\[
\Phi=\Phi_{\rm ref}X,\qquad
Q_{\rm ch}=-C\omega\Phi_{\rm ref}Y,\qquad
t=\tau_0s,\quad\tau_0=2/\omega.
\]

The preparation is (X,Y)=(0,-1). Direct substitution gives the correct equations, energy and canonical one-form:

\[
E=\frac{CV_{\rm ref}^2}{2}(X^2+Y^2),
\]
\[
\frac12(Q_{\rm ch}d\Phi-\Phi dQ_{\rm ch})
=\mathcal J_{\rm ref}\frac12(XdY-YdX),
\qquad
\boxed{\mathcal J_{\rm ref}=\frac{CV_{\rm ref}^2}{\omega}
=\frac{2E_{\rm ref}}{\omega}}.
\]

One positive winding has canonical loop action pi*J_ref. Four rational LC families verify the intertwiner, energy and one-form pullback. The action units are kg*m^2/s. Capacitance is not mass: C is not silently substituted for source B0. J_ref is an oscillator-map scale; identifying it with source A0 requires an additional typed correspondence. A mechanical transducer would need its own map.

The readouts V=Q_ch/C and I=Phi/ell determine classical quadratures. They are phase-dependent readouts, not the fixed isolated Born effects from the preceding audit. This model therefore does not remove that audit's projective-readout obstruction or establish a quantum implementation. Nor does a single active plane realize all seven complex active modes.

## 6. Fixed-map consistency and changing the reference

Keep C,omega and V_ref fixed. Preparing another actual voltage V=r*V_ref gives

\[
a=r^2,\qquad \oint Q_{\rm ch}d\Phi=\pi a\mathcal J_{\rm ref}.
\]

Doubling the actual preparation voltage multiplies support and loop action by4. **The fixed map scale J_ref does not change.** Sixteen rational preparation controls verify this. The intensive ratio S/(a*Delta_phi)=J_ref/2 also stays fixed.

In contrast, choosing a different reference V_ref defines a different map, with J_ref proportional to V_ref^2. Calling every physical preparation a fresh native unit state conceals this change unless the scale/support record is retained. No contradiction is implied when one fixed map correctly retains a.

The voltage intervention checks scale bookkeeping and the ideal analogue law. It cannot by itself select which reference is the fundamental UD unit or independently establish quantum correspondence. Selecting V_ref^2=2*hbar*omega/C would set J_ref=2*hbar by construction and cannot test that relation. An exact generic target-backsolve identity is included as a negative control.

## 7. Prospective test, not an executed experiment

The [LC preparation protocol](LC_PREPARATION.md) defines the missing apparatus/calibration inputs and an optional analogue consistency experiment. For positive intervals, a conditional enclosure is

\[
\mathcal J_{\rm ref}\in
\left[\frac{C_LV_L^2}{\omega_U},
      \frac{C_UV_U^2}{\omega_L}\right].
\]

Eight exact corner checks and two invalid-interval controls pass. The algebra needs no independence assumption, but actual coverage, correlations, loading, losses and model error require evidence. No numerical uncertainty budget is invented. Frequency is angular frequency; cycle-frequency conversion must retain2pi. Computing energy from the same C,V data is an identity check, not independent evidence.

Calibration receipts must distinguish candidate-dependent inference from metrological h traceability, as discussed in the preceding protocol. This work does not certify a fully h-free chain or relax the imported experimental-entry requirements.

## Reproduction and next discriminant

From repository root, standard-library Python:

```bash
python3 experiments/qpb1-unit-preparation/audit.py --out /tmp/ud-unitprep
```

All proofs and fixtures are constructor work. No independent review, physical preparation or empirical evaluation occurred. Physical promotion remains0. The decisive missing source is a native-to-physical preparation/constitutive law that selects the reference action, rather than allowing an externally chosen reference to stand in for it. A calibrated analogue can be pursued on its own declared scope; its success would not supply that source law automatically.
