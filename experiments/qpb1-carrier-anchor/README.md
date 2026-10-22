# QPB1 carrier, observable and action-anchor audit v1.0

**EXACT / CONDITIONAL / OPEN.** The isolated unit-metric active Hodge sector does not supply a measurable quantum phase rate through projective Born readouts. A classical oscillator family reproduces its one-plane flow and loop action while leaving the physical unit-amplitude scale arbitrary. These are scoped obstructions to particular correspondence/test choices, not a universal rejection of QPB1.

Discovery base 5ca396d67579bfb741ea8f784045353ec144f615. Dependencies: [previous source/action audit](../action-normalization-audit/README.md), its exact recovered ledger v0.85 and C0906 receipt, and [original experimental-entry contract](ENTRY_CONTRACT_SOURCE.json). The upstream contract remains proposed/unscored. [Protocol](PROTOCOL.md), [anchor test](ANCHOR_TEST.md), [blank measurement template](MEASUREMENT_TEMPLATE.json), [exact audit](audit.py), [intake utility](intake.py), [receipt](../../sessions/qpb1-carrier-anchor-20261022-a1/mathematical_receipt.json), [captured run](../../artifacts/qpb1-carrier-anchor-20261022-a1/exact-001/manifest.json).

## 1. Typed carrier and sign dictionary

Use the original filled tetrahedron with f=(4,6,4,1), real chain dimension 15, unit metric, generator A=d-d^T. The active projector and complex structure satisfy

\[
 P=-A^2/4,\quad\operatorname{rank}P=14,\quad
 J=A/2,\quad J^2=-P,\quad \Omega=2P.
\]

The active real vector space E=imP can be viewed intrinsically as a complex 7-dimensional space. Fix a unit pair e,f=Je. Native coordinates x=qe+pf give J(q,p)=(-p,q). To match the usual positive-energy Schrodinger sign, explicitly choose the dictionary z=q-ip, so multiplication by complex i corresponds to -J. Then

\[
 z(t)=e^{-i2t/\tau_0}z(0),\qquad
 U_{\rm native}(t)=e^{-i2t/\tau_0}I_7.
\]

The conjugate dictionary z=q+ip identifies i with J and reverses this complex sign. Source Q287's mention of J does not alone select the physical complex/time/energy-sign dictionary. This choice must be frozen in a proposed map; it is not an extra derivation of a physical arrow of time.

The native energy quadratic form is H=||x||^2=a. Under the separately declared dimensionalization E_native=A0*a/tau0, its putative quantum energy operator on normalized states is (A0/tau0)I7. Postulating the Schrodinger law with hbar would give scalar phase exp(-i*eta_A*t/tau0). Exact lifted phase equality with native evolution would select eta_A=2, but this is an additional correspondence, not an observed frequency equality within projective readout.

## 2. Projective readout obstruction

For every density matrix rho and scalar unitary U=e^{-i chi}I7,

\[
 U\rho U^\dagger=\rho,\qquad
 p(M;t)=\operatorname{Tr}[M\rho(t)]=\operatorname{Tr}(M\rho(0)).
\]

Thus every fixed Born effect M on this isolated carrier is independent of the free common phase and its rate. Any eta_A producing only that common phase gives the same output probabilities. This follows directly from the declared projective quantum readout; standard global-phase equivalence is described by [IBM Quantum Learning, Irrelevance of global phases](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/quantum-circuits/limitations-on-quantum-information), accessed 2026-10-22. The UD generator specialization and resulting test obstruction are constructor deductions.

The code checks 32 exact rational state/phase cases in C7. The proof is universal in rho,M and scalar phase; finite checks supplement the identity rather than extend its scope.

A phase-dependent native observable cannot silently become an isolated quantum observable under this map. Choose e to be the unit edge01 coordinate. Then e and Je lie on the same complex projective ray, but the normalized real edge-coordinate square is 1 at e and 0 at Je. Any function on their shared projective ray has one value, so it cannot reproduce both native readings.

More generally, for a real symmetric active quadratic form x^T Bx, invariance under every exp(phi J) is equivalent to BJ=JB: differentiate the form and use symmetry of BJ-JB. A possible invariant readout is the phase average

\[
 B_{\rm av}=\tfrac12(B+J^TBJ).
\]

For the edge witness this commutes with J and has value 1/2 at both states. Choosing invariant observables resolves this particular readout conflict while leaving the absolute phase rate unobservable. It does not derive which observables nature selects.

| Carrier/readout | Mathematical size | Consequence |
| --- | --- | --- |
| Original real chain carrier | R15 | Includes one real harmonic line |
| Active intrinsic complex carrier | R14 equivalent to C7 | Free evolution is common phase |
| Normalized active projective state | S13/U(1), real dimension 12 | Removes support scale and common phase from R14 |
| Full complexification | C15, real dimension 30 | Explicitly doubles the full real carrier |
| Minimal intrinsic-complex extension | R16 equivalent to C8 | Adds one real coordinate to pair the harmonic line |

Dimension differences here are typed state/readout dimensions, not physical dimensions or percentages of information capacity.

## 3. Full-carrier parity and a reference extension

A real complex structure K on all 15 original real coordinates would obey K^2=-I15. Taking determinants gives det(K)^2=(-1)^15=-1, impossible over R. This does not obstruct the intrinsic complex structure on the active 14-dimensional sector, nor an explicitly enlarged complexification.

There is an exact minimal one-real-coordinate extension. Let h be the unit harmonic vector, with four vertex entries 1/2 and all others zero, so P0=hh^T. On R15 plus one real coordinate define

\[
 K=\begin{pmatrix}J&-h\\h^T&0\end{pmatrix},\qquad
 \widetilde A=\begin{pmatrix}A&0\\0&0\end{pmatrix}.
\]

Because Jh=0 and J^2=-P,

\[
 K^T=-K,\qquad K^2=-I16,\qquad[K,\widetilde A]=0.
\]

The harmonic vector and new coordinate now form one static complex reference mode. This is an added state-space assumption; the original 15-dimensional real subspace is not closed under multiplication by K. The free extended equations preserve the old motion, but preparing/measuring the enlarged complex state space is additional physical work.

Under a proposed coherent reference preparation psi=(|r>+|u>)/sqrt2, with u active and r static, the plus readout gives

\[
 p_+(\phi)=\tfrac14|1+e^{-i\phi}|^2=\tfrac12(1+\cos\phi).
\]

Eight exact rational phase cases and the 16-by-16 matrix identities are verified. Relative phase is now visible within this extended model. No physical reference, coupling, coherent preparation or detector has been derived, and such an interference formula also has classical-wave realizations. This is a constructive extension candidate, not a quantum experiment or original-carrier theorem.

## 4. Classical one-plane realization and anchor ambiguity

Let m,L,omega be arbitrary positive physical parameters. Take one active native pair (Q,P), with t=tau0*s and native phase rate2. Define

\[
 q=LQ,\qquad p_{\rm mech}=-m\omega LP,\qquad
 \tau_0=2/\omega,\quad a_0=L,\quad B_0=2m.
\]

Then the native flow maps exactly into the classical harmonic oscillator equations

\[
 \dot q=p_{\rm mech}/m,\qquad
 \dot p_{\rm mech}=-m\omega^2q.
\]

The physical energy and symmetrized canonical one-form pull back as

\[
 E=\tfrac12m\omega^2L^2(Q^2+P^2)
 =\frac{\mathcal A_0}{\tau_0}a,
\]
\[
 \tfrac12(p_{\rm mech}dq-q\,dp_{\rm mech})
 =\mathcal A_0\,\tfrac12(Q\,dP-P\,dQ),
 \qquad
 \boxed{\mathcal A_0=m\omega L^2=\frac{2E_*}{\omega}}.
\]

Here E_* is the energy of the physical preparation assigned to native support a=1. One full winding has loop action integral p_mech dq=pi*A0. The two factors 2 in B0=2m and tau0=2/omega originate in the declared native frequency/energy normalization and cancel in A0; they are not a fitted action ratio. Three rational oscillator examples verify the exact intertwiner, energy relation and one-form pullback.

This provides a conditional physical-scale estimator without inserting hbar into its formula. It also exposes a missing source rule: L is the physical amplitude assigned to one unit native state. L->cL leaves the normalized native trajectory unchanged and changes A0 by c^2. Native projective normalization alone cannot choose that physical amplitude. Picking L=sqrt(2*hbar/(m*omega)) would manufacture the candidate action ratio and is excluded from independent calibration.

This ordinary classical family reproduces the one-plane motion and geometric action, with no quantum identification. Matching those features alone does not discriminate QPB1. The map is a proposed analogue family; no actual classical device is admitted as the fundamental UD carrier.

## 5. Conditional test and calibration independence

[ANCHOR_TEST.md](ANCHOR_TEST.md) specifies the prospective test. Freeze a justified correspondence and physical unit preparation before collecting m,L,omega. Their interval estimator is

\[
 [A_L,A_U]=[m_L\omega_LL_L^2,\ m_U\omega_UL_U^2],
\]

for positive intervals. This deterministic enclosure does not require statistical independence, but its experimental coverage must be evidenced. If energy is inferred from the same m,omega,L data, 2E/omega is an algebraic cross-check rather than a second independent measurement.

The operational meaning of non-hbar calibration must be precise. The SI kilogram is defined using a fixed numerical value of Planck's constant: [BIPM kilogram definition](https://www.bipm.org/en/si-base-units/kilogram), and [SI Brochure 9th edition, version4.01,§2.3.1](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf), accessed 2026-10-22. Therefore an SI-based test must disclose h-dependent unit traceability. The classical formula alone cannot certify a strict h-free full traceability chain. This metrological fact does not itself impose A0=2*hbar; avoiding that target-dependent physical inference is a distinct requirement.

The intake offers two explicit proposed classifications: target-independent inference with disclosed SI traceability, and strict h-free full-chain claims. It rejects the latter when h-dependent ancestry is declared. Neither classification automatically satisfies an external registry or establishes independence. The ancestor check rejects use of the candidate relation or hbar inside the anchor formula, including hidden dependencies; a separate final comparison node does not change anchor arithmetic.

Fourteen synthetic/prospective intake cases check valid interval calculation, missing maps, amplitude backsolving, hidden target ancestry, traceability, angular-frequency units, malformed intervals and graph errors. The blank real template is BLOCKED/UNSCORED. Receipt names are metadata; no program checks their scientific truth, verifies uncertainty coverage, or scores a physical bridge. No physical measurements, non-constructor review or independent quantum-holonomy reconstruction occurred.

## Reproduce

From repository root, standard-library Python:

```bash
python3 experiments/qpb1-carrier-anchor/audit.py --out /tmp/ud-qpb1
python3 experiments/qpb1-carrier-anchor/intake.py experiments/qpb1-carrier-anchor/MEASUREMENT_TEMPLATE.json
```

Next discriminant: find a target-independent physical preparation rule selecting the unit-state amplitude/action map on a named carrier, and either identify its J-invariant physical readouts or specify a physical relative-phase reference. The exact free-sector obstruction remains valid under its stated hypotheses; altered metrics,generators or extensions define separate models. QPB1 stays a candidate and physical promotion remains 0.
