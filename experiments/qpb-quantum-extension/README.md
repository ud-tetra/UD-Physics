# Minimal quantum extension of the tetrahedral UD carrier

**RESULT — EXACT / CONDITIONAL** representation rigidity under full signed S4 and retained complex J; **HYPOTHESIS** bosonic Fock lift; **FAILED** native selection of anharmonicity and uniquely physical transmon correspondence.

## Task, sources and typed conventions

Question: Do the source-defined tetrahedral incidence operators select a Hermitian interaction capable of producing a nondegenerate anharmonic seven-level transition ladder **without** borrowing a Josephson frequency target or an independently fitted coefficient?

Read-only integrated source is \`ud-tetra/UD-Physics@211f2e72fc72867bac1b3c8712bf0d5c2464e509\`, especially [local generators](../qpb1-local-generators/README.md) and [carrier anchor](../qpb1-carrier-anchor/README.md). [Draft PR #149](https://github.com/ud-tetra/UD-Physics/pull/149) establishes the previous direct-C7 spectrum obstruction and is an unmerged, **read-only research reference**, NOT an integrated task dependency. [Draft PR #128](https://github.com/ud-tetra/UD-Physics/pull/128) provides conventional Josephson-harmonic baseline and is also not an integrated task dependency. Empirical published context is Willsch et al., [Nature Physics 20, 815–821 (2024)](https://doi.org/10.1038/s41567-024-02400-8), measured transmon f0j j=1..6 and a conventional higher-harmonic spectrum fit; raw Jülich f0j files were not acquired.

Native state: real chain C=⊕_(k=0)^3 C_k(Delta^3;R), dimensions (4,6,4,1); ascending simplex orientation, unit Euclidean metric, signed vertex permutation representation R(p) for all p in S4, native A=d-d^T, J=A/2 and sector projectors Pk=-Kk²/4 with Kk=Dk-Dk^T. Positive active carrier E=imP has real dimension14. Choose **physical complex i=-J** as a bridge assumption, so E is C7; the opposite sign is a distinct convention, not proof of physical time orientation. Original native s is dimensionless; physical action chi (joule-seconds) and time tau0 (seconds per native unit) remain OPEN. These are not the physical Josephson phase angle, flux, charge or voltage.

## 1. Exact S4 representation and universal Hermitian commutant

For each of the 24 signed actions construct the real 15x15 representation and real sector projectors Pk. Because J commutes with every signed action and all Pk, each active real sector becomes a complex representation with dimension rank_R(Pk)/2=(3,3,1). Its complex character equals half the real trace of R(p)Pk; the imaginary component vanishes in the exact constructor.

The resulting complex characters are:

| S4 cycle class | Size | Sector1: 3 | Sector2: 3' | Sector3: 1' |
| --- | ---: | ---: | ---: | ---: |
| identity | 1 | 3 | 3 | 1 |
| transposition | 6 | 1 | -1 | -1 |
| double transposition | 3 | -1 | -1 | 1 |
| 3-cycle | 8 | 0 | 0 | 1 |
| 4-cycle | 6 | -1 | 1 | -1 |

Character inner products (1/24)Σ_classes size*chi_i*chi_j form the exact identity matrix. Thus the three complex sectors are pairwise inequivalent irreducible S4 representations: the standard 3, the sign-twisted standard 3', and the sign 1'.

**Schur consequence:** if a quantum Hamiltonian on the original active C7 is complex-linear relative to J, Hermitian in H=I and commutes with the entire signed S4 action, then
\[
\boxed{H=c_1\Pi_1+c_2\Pi_2+c_3\Pi_3,\qquad c_i\in\mathbb R.}
\]
This is the FULL Hermitian S4+J commutant, **even without incidence locality**, and it has real dimension3. No S4-preserving single-particle interaction on this unchanged space can split the 3/3/1 multiplicities; no more than three distinct energies are possible. To obtain seven distinct transmon energy eigenvalues one must enlarge the representation, reduce/break S4, abandon J complex-linearity, or introduce a physical Hamiltonian not covered by these premises. Merely changing gains or clock/action scales cannot help.

This conclusion concerns full signed simplex-label S4, **not** an established symmetry group of a real superconducting device, its laboratory frame or spacetime. Treating S4 as physically mandatory remains HYPOTHESIS.

## 2. Minimal new bosonic Fock state space

Select the unique hidden complex sign sector as a one-complex-mode **candidate**. Introduce an *entirely new bosonic quantization assumption*: an infinite Fock Hilbert space with |n>, n=0,1,... and b†|n>=sqrt(n+1)|n+1>, N=b†b. Under a signed S4 permutation p, b† transforms by sign(p), and N is invariant. The source-defining hidden one-particle rate is 2g3 per native time, so its physically dimensioned one-particle energy would be \(\varepsilon=2\chi g_3/\tau_0\), **conditional** on the external chi and tau0.

The minimal free lift is
\[
H_{\mathrm{free}}=\varepsilon N,\quad E_n=n\varepsilon .
\]
It produces arbitrarily many distinct energy values and hence can accommodate a seven-level *count*, but every adjacent transition has the same frequency and the discrete second differences vanish exactly:
\[
(E_{n+2}-E_{n+1})-(E_{n+1}-E_n)=0.
\]
Source-selected linear incidence yields no anharmonicity, no quantum particle statistics, and no transmon measurement/drive-selection rules by itself. The Fock lift is an imposed choice of a new Hilbert space, not a consequence of C7's dimension.

A low-order interaction that preserves the same S4 action and global U1 number phase is the **additional hypothetical Kerr term**
\[
H_U=\varepsilon N+\frac{U}{2}N(N-1),\quad
E_n=n\varepsilon+\frac{U}{2}n(n-1).
\]
It gives \(\Delta(E_{n+1}-E_n)=U\) exactly. Symmetry permits U=0, U>0 and U<0, so it selects **neither the sign nor the magnitude**. Extracting U from measured transmon transition differences would be FIT, not an independent UD prediction. For an infinite Fock space, bare U<0 makes energy unbounded below; such a softened truncated ladder requires a stabilizing higher-order/periodic Hamiltonian. The conventional Josephson cosine law already supplies one possible stable nonlinear quantum system, but it is not derived from UD's incidence.

The exact constructor records three **arbitrary-unit** examples: ε=5 and U=0,+1/4,-1/4 on n=0..6. These are neither GHz values nor measured transmon data. They show an equally-spaced free ladder and two distinct permitted anharmonic spacings. A matched ordinary bosonic/Kerr Hamiltonian produces the same observables.

### Finite cutoff does not derive the bosonic algebra

If instead n is truncated to 0..6 in a seven-state matrix with the usual square-root ladder entries, then
\[
[b,b^\dagger]=I_7-7|6\rangle\langle6|.
\]
Thus the exact canonical Fock algebra fails at the truncated boundary (trace of the commutator is zero). Low-lying finite numerical states can still approximate an infinite oscillator; the obstruction is to **exact** identification, not to approximate low-energy simulation. The native C7 cannot simply be relabeled as an exact seven-state oscillator without this changed operator/readout structure.

## 3. Baselines, degrees of freedom, selection, and scope

Minimal source restrictions tested: (a) original C7 one-particle carrier and full signed S4; (b) original complex J and Euclidean Hermiticity; (c) imported one-particle hidden frequency; (d) optional added bosonic Fock quantization preserving S4; (e) minimal Kerr interaction. The source selects the S4 representation and native rate structure, not the Fock statistics, physical chi/tau0, U, charge rotor, resonator, physical state preparation or measurement.

Classical and quantum **null models:** an ordinary bosonic oscillator is identical to the free lift; an ordinary Kerr oscillator is identical to H_U. The established superconducting transmon model uses an infinite integer-charge rotor with conventional Josephson harmonic potentials and independently fitted/calibrated circuit couplings. It can produce higher transition spectra without UD.

Fit exposure: the measured transmon multilevel structure and prior direct C7 failure were known before Fock and Kerr choices. The \(\varepsilon=5, U=\pm1/4\) numbers are simple illustrative rational fixtures, not data fits. Selecting any U so that the model reproduces f12-f01 is post-target calibration; no independent held-out UD gain is established.

**FAILED uniquely physical identification:** The only source-selected single-particle spectrum remains at most three energies. Extra bosonic Fock structure produces many levels but no anharmonicity; extra Kerr U produces anharmonicity but is independently arbitrary and conventionally reproducible. Source-selected physical quantum bridge remains OPEN. This is a constructive mathematical investigation, not a physical demonstration, published spectrum fit or mainline promotion.

## 4. Reproducibility and captured correction

Run from repository root:
\`python3 experiments/qpb-quantum-extension/audit.py --out /tmp/ud-qextension.json\`

The Python 3 standard-library Fraction audit constructs all 15 oriented simplex registers, K/P/J, evaluates the 24 signed S4 actions and five conjugacy characters, proves exact character orthonormality and verifies the 3/3/1 decomposition. It checks three exact seven-level occupation ladders, their finite differences, and the seven-state truncated bosonic commutator. A separate longer same-constructor exact implementation corroborated the character calculations; that is not independent non-constructor review. All categorical no-go claims follow the displayed analytic/representation proofs, not just a finite grid.

The first immutable run [qext-001](../../artifacts/qpb-qextension-20261024-gpt6-a1/qext-001/manifest.json) recorded manually assigned future UTC timestamps for claim/run metadata. This is a provenance defect, not a scientific formula error. Do not rewrite that run. The corrected [qext-002](../../artifacts/qpb-qextension-20261024-gpt6-a1/qext-002/manifest.json) repeats **identical SHA-256 source and output bytes** with actual runtime timestamp and is the authoritative capture; see [timestamp correction](../../sessions/qpb-qextension-20261024-gpt6-a1/timestamp_correction.md). Source SHA-256 \`be065eb7bd5573fe972c471915c224d5ca002e421ffae0d29fbb39dab8f18242\`, output SHA-256 \`0721d516583094f86977369ad31339c5b5fd1333f9c955bdb9517af12e1f2171\`.

Actual hardware, measured quantum level spectrum fitting, independent empirical replication and outside proof reviewer: **NOT_EXECUTED / NOT_RUN**. Earlier PR #149 and PR #128 remain unmodified.

**NEXT (priority 98/100):** seek a versioned native many-body interaction that fixes U/ε, or a physically derived charge-rotor and quantized action/clock/port dictionary, before evaluating truly unused transmon f0j data against a conventional harmonic transmon null. If absent, PARK this candidate's unique quantum correspondence, retaining both exact representation rigidity and the explicitly hypothesized Fock construction.
