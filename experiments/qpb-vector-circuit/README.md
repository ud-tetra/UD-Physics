# Vector-charge/current circuit bridge — source, port, and scale-identifiability test

**RESULT — EXACT / CONDITIONAL:** Adding a specified external edge-current source to the already hypothetical tetrahedral charge-field Hamiltonian yields exact vertex-charge continuity, a gauge-consistent action, and physical voltage–current power balance. A longitudinal charge-injection port and a neutral transverse-cycle port behave differently even at equal integrated source effort. **FAILED unique physical identification:** an ordinary reciprocal LC multiport implements exactly the same response, and a continuous internal scaling changes the native action/constitutive parameters while leaving *all* physical capacitance, inductance and calibrated port responses unchanged.

## Question, source versions, and typed definitions

Could UD's existing six-edge/tetrahedral field-candidate current become a *physical measurement bridge* rather than a dimensionless support-current analogy? The relevant integrated files are [charge-field](../qpb1-charge-field/README.md), [source reservoir](../qpb1-source-reservoir/README.md), [quantized charge](../qpb1-quantized-charge/README.md) and [impedance-selection](../qpb1-impedance-selection/README.md) at **main revision \`18a84984af40265d673b7b893c73de152a7cc8c5\`**, imported read-only. The prior separate [native finite scalar-charge PR #168](https://github.com/ud-tetra/UD-Physics/pull/168) is draft, unmerged and not a task dependency. It concerns a different finite quotient; its scalar-charge no-go is neither overwritten nor silently exported.

Conventional physical baseline: Stern, Tong, Desbrun and Marsden, [variational electrodynamics with external sources](https://www.cds.caltech.edu/~marsden/bib/2008/15-StToDeMa2008/) and [their discrete variational Maxwell framework](https://arxiv.org/abs/0707.4470). For actual circuit Hamiltonian and flux/charge canonical structure, compare Osborne et al., [*Symplectic Geometry and Circuit Quantization*](https://doi.org/10.1103/PRXQuantum.5.020309). These references supply conventional context; they neither identify UD with hardware nor determine native dimensional scales.

Use the **added field carrier** \(a,p\in\mathbb R^6\), separately from UD's original active \(\mathbb R^{14}\). The edge order is 01,02,03,12,13,23. Over \(\mathbb Q\) in the exact audit, \(B_1:\mathbb R^6\to\mathbb R^4\) is the signed vertex–edge incidence and \(B_2:\mathbb R^4\to\mathbb R^6\) is the oriented face–edge incidence. They obey \(B_1 B_2=0\), \(P_L=B_1^\top B_1/4\), \(P_T=B_2 B_2^\top/4\), \(P_L+P_T=I_6\), and \(\operatorname{rank}P_L=\operatorname{rank}P_T=3\). These combinatorial identities are source-defined; the canonical field interpretation is NOT.

Let \(U=u_LP_L+u_TP_T\), with \(u_L,u_T,v>0\) separate adjustable constitutive parameters, and
\[
H_0(a,p)=\tfrac12p^\top Up+\tfrac v2\|B_2^\top a\|^2,\qquad
\rho=B_1 p,\qquad b=B_2^\top a.
\]
Native clock \(s\) is dimensionless; \(\mathcal A_0>0\) is a *newly assumed physical action reference*, \(q_0>0\) a *newly assumed physical charge unit*, and \(\tau_0>0\) seconds per native time. No measured apparatus is provided.

## 1. Explicit external port, continuity and gauge action

**HYPOTHESIS, not source-autonomous dynamics:** supply an externally controlled edge drive \(f(s)\in\mathbb R^6\) and a vertex-current history \(j(s)=B_1 f(s)\in\mathbb R^4\). Require \(\sum_i j_i=0\). Introduce a prescribed zero-sum source charge history \(\rho_{\mathrm{ref}}'(s)=j(s)\) and gauge multiplier \(\psi(s)\). Postulate
\[
S=\mathcal A_0\!\int\left[p^\top a'-H_0(a,p)+a^\top f(s)-
\psi^\top(B_1p-\rho_{\rm ref}(s))\right]ds .
\]
Variation at fixed endpoints yields
\[
\boxed{a'=Up+B_1^\top\psi,\qquad p'=-vB_2B_2^\top a+f,\qquad
 \rho'=B_1f=j.}
\]
The total vertex charge stays zero because \(\mathbf1^\top B_1=0\). Under \(a\mapsto a+B_1^\top\chi\), \(\psi\mapsto\psi+\chi'\), the action changes only by the endpoint \(\mathcal A_0[\chi^\top\rho_{\rm ref}]\), *provided* \(\rho_{\rm ref}'=B_1 f\). If a charge-changing source is inserted but its continuity history is omitted, that gauge property is not obtained. The external current supplies or removes charge/energy, and the external reservoir/controller must account for the opposing charge and work. This is not a native self-generated electron or current law.

Exact source work, valid for arbitrary gauge multiplier:
\[
\boxed{H_0'=(Up)^\top f.}
\]
The gauge component does not contribute because \(B_2^\top B_1^\top=0\). Without source \(f=0\), the ideal stored energy is conserved.

## 2. Two controlled drive ports with different physical responses

For any zero-sum vertex current \(j\), a minimal-norm longitudinal edge source is \(f_L=B_1^\top j/4\). It obeys \(B_1 f_L=j\) and \(P_T f_L=0\). In particular choose \(j=(r',-r',0,0)\) and initial vanishing transverse field. Then after injecting native signed charge \(r\),
\[
\rho=(r,-r,0,0),\quad p_L=B_1^\top\rho/4,\quad
\boxed{H_C=u_Lr^2/4.}
\]
The energy depends only on the final charge, not on pulse shape, **within the ideal decoupled longitudinal model**. The external source supplies the work during injection. The physical nodal charge unit and voltage are defined in the mapping below; no isolated single-charge production follows because the opposite node charge is compulsory.

For an independently chosen neutral transverse cycle \(w=(1/2,0,-1/2,1/2,0,1/2)\), exactly \(\|w\|=1\), \(B_1w=0\) and \(B_2B_2^\top w=4w\). Set \(f_T(s)=wF(s)\) with mode variables \(a=\alpha w,p=\beta w\) initially zero. Then
\[
\alpha'=u_T\beta,\quad \beta'=-4v\alpha+F(s),\quad
\omega_{\rm native}=2\sqrt{u_Tv}.
\]
The final cycle energy after a zero-to-\(T\) input is
\[
\boxed{H_T(T)=\frac{u_T}{2}\left|
\int_0^T e^{-i\omega_{\rm native}s}F(s)\,ds\right|^2.}
\]
For a rectangular drive \(F(s)=F_{\rm area}/T\), this becomes
\[
\boxed{H_T(T)=\tfrac{u_TF_{\rm area}^2}{2}
\operatorname{sinc}^2(\sqrt{u_Tv}\,T).}
\]
For the selected source normalization \(u_Tv=1\), a pulse of native length \(T=\pi\) leaves zero final cycle energy; a pulse of length \(\pi/2\) leaves fraction \(4/\pi^2\approx0.40528\) of the short-impulse limit. The two drives have the **same integrated modal current**, but different Fourier overlap with the oscillator. This is an exact linear-system consequence and is already explained by conventional resonator dynamics. A rectangular finite drive lasting one oscillator period returns the unforced oscillator to zero in this lossless model; it is not a physically sourced cancellation miracle.

## 3. Typed SI dictionary and exact power balance

Add the external conversion
\[
\Phi=\frac{\mathcal A_0}{q_0}a\ \mathrm{(Wb)},\qquad
Q=q_0p\ \mathrm{(C)},\qquad
t=\tau_0s\ \mathrm{(seconds)},\qquad
E=\frac{\mathcal A_0}{\tau_0}H_0\ \mathrm{(J)}.
\]
This has the physical canonical one-form \(Q^\top d\Phi=\mathcal A_0 p^\top da\). The generalized physical positive inverse capacitance and inductive quadratic form are
\[
C^{-1}_{\rm eff}=\frac{\mathcal A_0}{\tau_0q_0^2}U,\qquad
L^{-1}_{\rm eff}=\frac{v q_0^2}{\mathcal A_0\tau_0}B_2B_2^\top.
\]
The second has rank three; its gauge kernel does **not** mean six independent ordinary inductors have been specified. These matrices define a reciprocal generalized coupled LC multiport; a concrete wiring layout, ideal-transformer realization, parasitics and hardware sign/port calibration are an additional engineering problem. No passive real-world device was fabricated or measured.

Define gauge-independent physical edge effort and controlled physical edge current
\[
V_{\rm edge}=\frac{\mathcal A_0}{\tau_0q_0}Up,\qquad
I_{\rm edge}=\frac{q_0}{\tau_0}f.
\]
Then \(V_{\rm edge}=\dot\Phi-\frac{\mathcal A_0}{\tau_0q_0}B_1^\top\psi\), and
\[
\boxed{\frac{dE}{dt}=V_{\rm edge}^\top I_{\rm edge}.}
\]
The physical source-supplied vertex current is \(I_{\rm vertex}=B_1I_{\rm edge}\). For \(\rho=(r,-r,0,0)\), the positive/negative node charge magnitude is \(q_0r\), the nodal potential difference is \(\Delta V=\mathcal A_0u_Lr/(2\tau_0q_0)\), and the effective two-node dipole capacitance is
\[
C_{\rm dip}=\frac{2\tau_0q_0^2}{\mathcal A_0u_L}.
\]
Independent current and voltage calibration could measure this *circuit response*; it would not in itself prove that a measured coulomb corresponds to one primitive UD register or one electron.

## 4. Strong all-port scale degeneracy

Let \(h>0\). With the same physical charge unit \(q_0\), same physical time map \(\tau_0\), and same externally prescribed native drive \(f\), apply
\[
\boxed{(U,v,a,\mathcal A_0,\psi)\mapsto
(hU,v/h,ha,\mathcal A_0/h,h\psi),\qquad p\mapsto p.}
\]
For every physical initial state and current, \(\Phi=(\mathcal A_0/q_0)a\) and \(Q=q_0p\) are unchanged. Both \(C^{-1}_{\rm eff}\) and \(L^{-1}_{\rm eff}\) are **exactly unchanged**, so all physically calibrated multiport time responses, node charge, effort, source work and resonance are also unchanged. The transformed native ODE remains valid with the transformed state and gauge multiplier.

This is a **continuous identifiability counterfamily**: even *complete* linear network measurements cannot distinguish \(h\), \(\mathcal A_0\) and its compensating native constitutive coefficients without an independently justified cross-system normalization. The exact Fraction constructor tests \(h=1/2,2,3\) on 24 rational mixed drive/state fixtures, but the algebra proves it for every positive real \(h\). Imposing \(\mathcal A_0=\hbar\), choosing a particular \(q_0\), fixing \(u_Tv=1\) or choosing a native unit preparation are separate external/calibrated premises, not native consequences.

## 5. Conventional comparison, falsification and disposition

The **matched conventional baseline** is exactly the reciprocal linear Hamiltonian multiport with charge \(Q\), flux \(\Phi\), the same positive inverse-capacitance \(C^{-1}_{\rm eff}\) and semidefinite inductive matrix \(L^{-1}_{\rm eff}\). It gives every displayed current, voltage, charge-storage and pulse-shape response without invoking UD. The topology only furnishes an attractive 4-node/6-edge coordinate framework. Finite graph combinatorics is not proof of physical 3+1 spacetime, electron structure or a microscopic material law.

A future physical protocol should (i) independently specify and build a reciprocal multiport or demonstrate an already existing device with measured \(C^{-1}_{\rm eff}\), inductive couplings and losses; (ii) measure balanced two-node injected physical charge and differential voltage with a documented reference/ground; (iii) excite a separately calibrated neutral cycle through a current transducer and compare impulse/half-period/full-period energy response; (iv) deliberately inject longitudinal/transverse crosstalk to measure leakage, dissipation and residuals; (v) freeze a *new* UD-specific constitutive restriction before held-out evaluation against the conventional LC network. Such an experiment would test the **declared circuit construction**, not automatically its origin in UD.

**Evidence:** EXACT / CONDITIONAL matrix algebra, gauge/action and time-response, and exact scale equivalence. NUMERICAL only for the displayed \(4/\pi^2\) approximation. HYPOTHESIS physical charge/flux identification, extra source and circuit realization. FAILED unique selection/physical attribution. No measured physical apparatus, externally validated UD action scale, independent mathematical reviewer or empirical predictive success.

## Reproducibility

Run from repository root:
\`python3 experiments/qpb-vector-circuit/port_audit.py --out /tmp/qpb-vector-full.json\`

The exact Fraction constructor checks \(B_1B_2=0\), projector identities, neutral/charged drive isolation, 24 rational mixed state/constitutive fixtures with arbitrary gauge, source work, SI power equality, nine exact pure-dipole checks, and three scale fixtures per mixed state. It was executed in a local staging path \`/mnt/data/qpb_vector_circuit_20261024/port_compact.py\` with full output \`compact_summary.json\`. The committed [immutable vector-001](../../artifacts/qpb-vectorcircuit-20261024-gpt6-a1/vector-001/manifest.json) stores byte-identical source under \`port_audit.py\` and a **selected reproducible excerpt** of the full summary, not the complete original local JSON. This narrowing is explicit: the example excerpt uses the five keys \`B1B2_zero\`, \`PL_PT_ranks\`, \`case_count\`, \`pulse_energy_fraction\`, \`status\`. The full script reproduces the rest of the machine-readable output. Source SHA-256 \`44f2d0f6203320a12786a57364b6bd91cee0a2f911b34effdab61494fd00f137\`, excerpt SHA-256 \`e06bd01e17a4702d45ad9564c9cc74a9e569f4053bf3002eb4cb7c5cdf73595e\`. No prior artifacts are modified.

**NEXT (priority 98/100):** obtain an independently sourced relation between native action/charge reference and a real multiport circuit's measured capacitance, current and flux, or park unique physical bridge attribution while retaining the useful exact port-design mathematics.
