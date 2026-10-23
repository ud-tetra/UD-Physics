# Action convention, primitive-loop and phase-map audit v1.0

**EXACT / CONDITIONAL / OPEN.** O14's direction is source-verified. A literal O13 dimensional error persists in the recovered ledger and already has a correction proposal. The normalized single-tetrahedron specific action scale is A0/2. Its physical identification remains a candidate.

Discovery base ce89a9cd15439463d9a64d983d91c22ea4368726. Read-only mainline import from ud-tetra/UD at957d443e25008632ab9d9328c162343b6a651ee7. See [source manifest](SOURCES.json), [calculation receipt](../../sessions/action-normalization-20261022-a1/mathematical_receipt.json), [captured run](../../artifacts/action-normalization-20261022-a1/exact-001/manifest.json) and [audit code](audit.py). No mainline registry was edited.

## 1. Source recovery and correction

Recovered the archive labelled Ledger v0.85: SHA2568845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec,444587bytes,723rows and723unique IDs. Six selected upstream source files match their original Git blob hashes exactly. The archive retains inherited scientific_revision=v0.43 and source_baseline=v0.84 fields; those are preserved rather than silently rewritten or interpreted as a complete chronological audit. Source details are in SOURCES.json.

| Object | Recovered definition/status | Audit conclusion |
| --- | --- | --- |
| G06 | Bare xi_hbar frozen; historical reciprocal aliases; SOURCE_STRATUM | Use qualified ratios |
| O09 | I_lift=(1/2)sum a_omega Delta_phi_lift; closed history=pi sum n_omega a_omega | Lifted history is required |
| O10 | A0=B0*a0^2/tau0; native unit, no SI identification | Action dimensions under declared unit types |
| O11 | pi*A0 conditional on unit-support one-winding recurrence | Conditional native anchor |
| O12 | xi_phys/native=hbar/A0 | Explicit reciprocal alias; numerical value OPEN |
| O13 | Starts A0/hbar but ends a chained equality to1/xi_phys/native | Literal source chain fails dimensional typing |
| O14 | eta_A=A0/hbar | Canonical direction; numerical value OPEN |
| O15 | [B0]=M; energy-typed B0 branch frozen | Mass-like type is recovered, not still source-missing |
| Q287/Q288 | hbar<->A0/2; eta_A=2 | QUARANTINED_CANDIDATE; no empirical score |

O09–O15 have source claim_bin NOT_A_COEFFICIENT: they are maps, units or conventions, with separately stated lock/conditional statuses. The user report's uniform EXACT_INTERNAL label is not their literal source classification.

The original O13 exact_form contains

\[
 \mathcal A_0=\xi_\hbar^{[\mathrm{native/phys}]}\hbar
 =1/\xi_\hbar^{[\mathrm{phys/native}]}.
\]

The final equality mixes action and a dimensionless ratio. Preserve the source bytes and use the already archived append-only correction proposal:

\[
 \xi_\hbar^{[\mathrm{native/phys}]}=\frac{\mathcal A_0}{\hbar}
 =\frac1{\xi_\hbar^{[\mathrm{phys/native}]}},\qquad
 \mathcal A_0=\xi_\hbar^{[\mathrm{native/phys}]}\hbar.
\]

The overlay is constructor-checked with non-constructor review pending. This audit verifies its algebra and units; it does not approve a mainline amendment. Nonzero A0 and hbar are required for reciprocals.

## 2. Dimensions and scope

With [B0]=M,[a0]=L,[tau0]=T,

\[
 [\mathcal A_0]=ML^2T^{-1}=[\hbar],\qquad [\eta_{\mathcal A}]=1.
\]

The types are explicit native unit declarations. A common physical action-unit map and numerical anchors remain separate premises. Calling a native unit parameter-free introduces no fitted theory coefficient; its numerical SI value is not supplied by the declaration.

The existing reviewed verifier was rerun against exact recovered source bytes:18typed equalities from17source rows pass, four negative-control categories are rejected, and2952rational anchor banks satisfy its row-space/kernel criterion. The reproduced ACTION_UNIT_CONTRACT.json matches the archived original byte-for-byte. This is constructor reexecution of the same implementation, not independent review. The723-row inventory is counted; only the17-row action subsystem is typed here. No global EXIT-03 pass is claimed.

## 3. Exact tetrahedral normalization check

Independently construct oriented chain spaces C_k(Delta3;Q), ascending simplices, f=(4,6,4,1),dim15, unit chain metric H=I. Let d be boundary and A=d-d^T, fixing positive phase orientation. Exact rational checks give

\[
 d^2=0,\quad A^T=-A,\quad A^3=-4A,\quad
 P=-A^2/4,\quad P^2=P,\quad\operatorname{rank}P=14,
\]
\[
 J=A/2,\quad J^2=-P,\quad\Omega=2P.
\]

The remaining rank-one harmonic projector is constant on the four vertices. For an active state x, let a=||x||^2>0. Retain the source Hodge loop-action convention theta=(1/2)<Jx,dx>. Along x'=Ax, theta(x')=a and the phase rate is2 per native parameter s. Therefore

\[
 \mathcal I=\frac a2\Delta\widetilde\phi,\qquad
 \mathcal S_{\rm native}=\mathcal A_0\mathcal I,\qquad
 \boxed{\frac{\mathcal S_{\rm native}}{a\Delta\widetilde\phi}=\frac{\mathcal A_0}{2}}.
\]

This reconstructs the stated single-filled-tetrahedron action-phase specialization. The one-form/action convention is imported explicitly; this is not a derivation of a primitive quantum action. Exact rational matrix checks are an additional constructor verification of the carrier structure.

The energy/frequency check uses the declared native maps

\[
 H=\tfrac12\langle x,\Omega x\rangle=a,\quad
 E_{\rm native}=\mathcal A_0 a/\tau_0,\quad
 \omega=2/\tau_0,
 \qquad E_{\rm native}/(a\omega)=\mathcal A_0/2.
\]

For a normalized representative a=1 and one full winding Delta_phi_lift=2pi, the loop action is pi*A0. Normalizing a projective representative does not prove support quantization or a physical normalized-state correspondence. Arbitrary glued/multifrequency carriers are outside this specialization.

## 4. Endpoint trace obstruction

For the explicitly defined Hodge evolution,

\[
 U(\phi)=P_0+\cos\phi\,P+\sin\phi\,J,\qquad
 \operatorname{Tr}U(\phi)=1+14\cos\phi.
\]

At every phi=2pi*n, U=I15 and trace15, while the lifted action is pi*n*a. Thus two histories with windings0 and1 have identical endpoint operators/traces and different loop actions. No function of endpoint operator or endpoint trace alone can recover this action for unrestricted windings. Even orientation is lost by a cosine trace. Retaining a lifted path or winding receipt removes this particular information loss; it does not establish a physical normalization.

Fifteen rational support/winding cases were checked exactly, with a in{1/4,1,9/4},n in{-2,-1,0,1,2}. Clock arithmetic is continuous phase modulo2pi with a separate integer winding, not an imposed finite-state physical clock.

## 5. What xi_act would have to mean

Assume, as a bridge hypothesis, that a declared physical phase chi obeys chi=S_native/hbar for this same typed loop action. Then

\[
 \chi=\eta_{\mathcal A}\mathcal I
 =\frac{\eta_{\mathcal A}a}{2}\Delta\widetilde\phi.
\]

Consequently a coefficient multiplying I equals eta_A under that phase-map assumption. A coefficient multiplying the raw Hodge angle equals eta_A*a/2, or eta_A/2 on a normalized ray. The name xi_act alone does not specify which coefficient it is.

Postulating chi=Delta_phi_lift on normalized rays yields eta_A=2, matching the already quarantined Q287/Q288 candidate. This is a consequence of the phase-identification postulate; neither trace recovery nor dimensional consistency establishes that postulate. The value2 was exposed before this audit, so this is not a fresh target-blind prediction.

There is another action distinction: on this orbit theta(x')=H=a, so the first-order functional integral of(theta-H ds) is zero although the integrated loop one-form is generally nonzero. These are different typed action functionals. A proposed physical phase map must identify its action explicitly; a loop area cannot silently stand in for the complete master dynamical action.

## 6. Remaining discriminant

Dimensionless native carrier data are unchanged by B0->lambda B0 with a0,tau0 fixed, while A0 and eta_A at fixed external hbar scale by lambda. Thus such data alone do not select a numerical physical action ratio. The recovered monomial-anchor theorem makes the condition precise: with known target-independent same-carrier anchors y_j=k_j B0^p_j a0^q_j tau0^r_j, the exponent(1,2,-1) must lie in the row span of the anchor matrix W. Length/time alone fail; independently justified native energy and time anchors can identify A0=E0*tau0. Measured apparatus energy/time are not automatically those native anchors.

Highest-value next action: specify the primitive quantum-holonomy operator, state/trace normalization, path lift, physical phase map and independently sourced action anchor on a named carrier. Then test whether xi_act multiplies I or a phase coordinate and whether the QPB1 same-carrier identification survives. No unprovided primitive operator has been reconstructed here.

## Reproduce and status

From repository root, standard-library Python only:

```bash
python3 experiments/action-normalization-audit/audit.py --out /tmp/ud-action-audit
```

Imported source files are data with exact upstream hashes; the reviewed original verifier is intentionally imported by the audit with explicit paths. Results include source and type checks, exact carrier identities, winding witnesses and scope limits. Code, selected sources, outputs and receipt are captured in the immutable run. Constructor checks only; non-constructor review pending, no physical experiment, native-to-SI action/clock/energy map OPEN, mainline physical promotion0.
