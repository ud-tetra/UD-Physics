# Direct UD quantum-spectroscopy bridge: finite-carrier spectral obstruction

**RESULT — EXACT / CONDITIONAL:** The original fixed three-sector rank-14 active tetrahedral carrier, when **assumed** to be a single-particle complex quantum Hilbert space of dimension seven with the native generator mapped directly to a Schrödinger Hamiltonian, has at most THREE distinct energies (and at the exposed reference only TWO). It cannot reproduce a resolved ladder of seven nondegenerate transmon levels. **This is NOT a universal no-go for enlarged, differently quantized, coupled or new-source UD systems.** No physical identification or experimental fit has been established.

## Provenance, premises and typed objects

Integrated read-only base: \`ud-tetra/UD-Physics@b4d2a9f15cda3b7d493a14bdba1d3f63604256d3\`. Primary native source paths: [local generator classification](../qpb1-local-generators/README.md), §§1–4, and [carrier/quantum anchor](../qpb1-carrier-anchor/README.md), §§1–4. Separate unmerged read-only Discovery branches: [phase-009 constitutive park](https://github.com/ud-tetra/UD-Physics/pull/87) and [jj-003 conventional-harmonic physical benchmark](https://github.com/ud-tetra/UD-Physics/pull/128). Their claims and files were not modified here.

External empirical reference: Willsch et al., [*Observation of Josephson harmonics in tunnel junctions*](https://doi.org/10.1038/s41567-024-02400-8), *Nature Physics* 20, 815–821 (2024), §Results and §Methods. The group measures transitions \(f_{0j}\) with \(j=1,\ldots,6\) and resonator shifts in superconducting transmons. A conventional rotor/charge-basis Hamiltonian with Josephson harmonics reproduces spectra more faithfully than the single-sine version; authors report some \(f_{03}\) discrepancies above 10 MHz for the standard fit and order-1-MHz measurement imprecision. The [Jülich DATA research archive](https://doi.org/10.26165/JUELICH-DATA/LGRHUH) is publicly cited; raw spectroscopy/model data were **NOT_ACQUIRED** in this runtime (external GitLab access verification previously blocked retrieval). Thus empirical evidence is the published paper's scope and statements, not a newly scored residual.

Native objects: chain \(C=\bigoplus_{k=0}^3C_k(\Delta^3;\mathbb R)\cong\mathbb R^{15}\) with oriented ascending simplex basis, Euclidean metric \(H=I\), differential \(D_k\), skew \(K_k=D_k-D_k^\top\), and mutually orthogonal projectors \(P_k=-K_k^2/4\). Native continuous dimensionless time is \(s\); one harmonic real line lies outside the rank-14 active real \(E=\operatorname{im}(P)\). The active complex structure is \(J=A/2\) with \(J^2=-I_E\). Source-classified conservative linear law \(G=\sum_{k=1}^3g_kK_k=J\,\Omega_g\), \(\Omega_g=2\sum_k g_kP_k\), \(g_k>0\) on its positive-energy branch. This is incidence-register locality, not physical length or causal locality.

## 1. The minimal, explicitly assumed Schrödinger correspondence

Define complex scalar multiplication by \(i_{\mathrm{phys}}=-J\), following the positive-frequency convention already considered in the carrier-anchor audit. This is **one chosen complex/time orientation**, not a physically selected quantum arrow. The real active 14D space becomes \(\mathcal H_{\mathrm{UD}}\cong\mathbb C^7\). Let \(\chi>0\) be an external physical action scale (joule-seconds) and \(\tau_0>0\) be a physical clock scale (seconds per native s). If we impose the Schrödinger equation \(i_{\mathrm{phys}}\chi \partial_t\psi=H_{\mathrm{eff}}\psi\), \(t=\tau_0s\), and demand its unitary evolution reproduce *the original native \(G\) exactly*, then

\[
H_{\mathrm{eff}}=\frac{2\chi}{\tau_0}\sum_{k=1}^3 g_k\Pi_k,
\]

where \(\Pi_k\) are the complex sector projectors. The equality is **EXACT / CONDITIONAL** on that mapping. Neither \(\chi=\hbar\) nor \(\tau_0\), nor the physical preparation and readout, is determined by the native carrier. Equal eigenvalue numbers without physical units would not fix either scale.

Exact 15-by-15 rational projector calculations give
\[
\operatorname{rank}_{\mathbb R}(P_1,P_2,P_3)=(6,6,2),
\qquad
\operatorname{rank}_{\mathbb C}(\Pi_1,\Pi_2,\Pi_3)=(3,3,1).
\]
Therefore
\[
\operatorname{spec}H_{\mathrm{eff}}
=\frac{2\chi}{\tau_0}\left\{g_1^{(3)},g_2^{(3)},g_3^{(1)}\right\}.
\]
At most THREE distinct energies are possible for arbitrary gains, producing at most TWO different nonzero ground-to-excited spectral gaps. At the previously target-selected \(g=(1,1,3/2)\), the spectrum has one sixfold level \(2\chi/\tau_0\) and one single level \(3\chi/\tau_0\), so only ONE nonzero distinct gap. Arbitrarily rescaling the clock or action cannot split a degeneracy.

A seven-level transmon ladder with individually resolved \(E_0,\ldots,E_6\) requires seven distinct energy values to account for the measured \(f_{0j}=(E_j-E_0)/h\) for \(j=1,\ldots,6\). The direct mapped \(\mathbb C^7\) sector-preserving family cannot reproduce that observable, regardless of its three gain parameters. This is a structural **FAILED** result, *not* a fit statistic computed from raw measurements. An arbitrary Hermitian 7x7 operator could have seven eigenvalues but would be a changed generator family, not the source-classified \(G\).

## 2. Why the existing seven complex modes are not automatically a transmon charge oscillator

The physical conventional transmon uses phase and charge variables in a rotor Hilbert space \(\ell^2(\mathbb Z)\), with unitary charge shift \(S=e^{i\varphi}\), integer number operator \(N|n\rangle=n|n\rangle\), and \([N,S]=S\) on their common domain. The Hamiltonian measured in the 2024 paper includes
\[
H_{\mathrm{transmon}}=4E_C(N-n_g)^2
-\sum_{m\ge1}E_{Jm}\cos(m\varphi)
+H_{\mathrm{res}}.
\]
The charge kinetic term, the Josephson shift operators and their higher harmonics are **extra constitutive and quantum objects**, not contained in the linear native \(G\). Also, superconducting junction phase difference is not automatically the internal UD \(J\)-fiber angle.

**EXACT finite-dimensional obstruction:** For finite matrices \(Q,P\), \(\operatorname{tr}[Q,P]=0\), so the exact canonical rule \([Q,P]=i\chi I_7\) with \(\chi>0\) is impossible on \(\mathbb C^7\). More appropriately for a compact rotor, take the seven-dimensional cyclic shift \(S|n\rangle=|n+1\pmod7\rangle\) for \(n=-3,\ldots,3\), and \(N|n\rangle=n|n\rangle\). Then exactly
\[
[N,S]-S=-7|-3\rangle\langle3|,
\]
a nonzero rank-one boundary defect. The cyclic finite carrier is not the exact infinite integer-charge rotor. An **open** charge truncation removes cyclic wraparound but loses shift unitarity at the boundary instead.

These facts do not prohibit *approximate* low-lying quantum transmon spectra from a sufficiently large finite numerical truncation. Nor do they rule out an explicitly added bosonic Fock space, tensor-product registers, new nonlinear Hamiltonian, reservoir/resonator, or genuine quantum charge/phase correspondence. Each would require distinct premises, parameters, preparation, and measurement laws; none is a native derivation here.

## 3. Conventional quantum baseline (numerical, not empirical)

For model clarity only, construct finite charge-basis matrices \(n=-M,\ldots,M\), with diagonal \(4E_C n^2\) and \(m\)-step off-diagonal \(-E_{Jm}/2\). Use \(E_C/h=0.242\) GHz as a published KIT circuit-scale example, and **SELECT** \(E_{J1}/h=15.0\) GHz, \(E_{J2}/h=0\) or \(0.15\) GHz as illustrative parameters, not fitted values. The \(E_{J2}\) case is a 1% second Josephson harmonic by chosen energy ratio; its spectrum is a conventional baseline, not a UD signal.

NumPy's symmetric eigensolver returns seven strictly increasing \(E_j-E_0\) values. Cutoffs \(M=12\) and \(M=16\) agree on these first seven energy gaps within \(1.2\times10^{-13}\) GHz in this constructor check. The single-sine example gives \(f_{01}=5.13446797\), \(f_{02}=9.99573084\), \(f_{03}=14.55515426\) GHz; the 1%-harmonic model gives \(5.21445988\), \(10.12958648\), \(14.71792474\) GHz. **ALL are numerical model outputs, not published measured transition frequencies.** The difference merely shows that the correct quantum Hilbert-space algebra naturally allows an anharmonic ladder. An actual physical fit requires independent parameter measurements or a frozen parameter-training/heldout split, including resonator coupling.

## 4. Scientific status, alternative hypotheses and next gate

| Candidate quantum correspondence | Level structure | Added freedom and status |
| --- | --- | --- |
| Direct active \(\mathbb C^7\), \(H_{\mathrm{eff}}\propto\Omega_g\) | 3 distinct levels at most; 2 at reference | **FAILED** direct transmon identification, exact/conditional |
| Arbitrary Hermitian 7x7 on same vector space | Can have 7 levels | Different operator law with many free parameters; **HYPOTHESIS / FIT** |
| Seven-mode bosonic Fock/tensor product of native modes | Many excitation sectors | Introduces quantum statistics, number operators and interactions; **OPEN**, no native selection |
| Infinite rotor \(\ell^2(\mathbb Z)\) with Josephson harmonics | Anharmonic transmon ladder | Well-established conventional quantum physics; *matched null*, not native UD |

Do not claim a measured residual, physical quantization or an independent prediction. The correct operational discriminant is an independently sourced UD Hamiltonian/charge-translation law, with physical \(\chi,\tau_0\), offset-charge and port/resonator map fixed **before** inspecting held-out \(f_{0j}\) data. A conventional harmonic transmon with the same parameter budget is the primary null. The current result justifies **PARKING the direct \(\mathbb C^7\) transmon identification** while retaining the exact source algebra as a valid native mathematical structure.

## Reproduction and evidence

From repository root:
\`python3 experiments/qpb-quantum-spectroscopy/spectral_audit.py --out /tmp/qpb-spectral-001.json\`

Requires Python 3 and NumPy for the *illustrative conventional-model* eigensolver; exact finite-incidence/rank/rotor identities use only Python's standard library and Fraction. The isolated local execution reproduced exact projector ranks and rotor boundary, and both conventional charge-truncation spectra converged. Input and output SHA-256 are captured in [immutable spectral-001](../../artifacts/qpb-qspectra-20261024-gpt6-a1/spectral-001/manifest.json); earlier JJ and phase candidate runs are read-only and unchanged. This is constructor verification, NOT independent referee confirmation, experimental UD realization or physical mainline promotion.

**NEXT recommended action (priority 98/100):** require a source-selected quantum extension/action scale and explicit held-out \(f_{0j}\) data access before reopening a UD transmon identification. As a separate supporting effort, obtain the 2024 Jülich raw spectroscopy through ordinary authorized access; do not bypass the repository's automated-access controls.
