# Native charge and finite Weyl Hamiltonian source-selection audit

**RESULT — EXACT / CONDITIONAL:** The tetrahedral graph-critical/discriminant charge labels support a perfect finite pairing, but cannot act as nonzero scalar additive integer electric charge. Under complete finite Weyl symmetry, no nontrivial Hermitian Hamiltonian survives; under only full tetrahedral symmetry, nontrivial Hamiltonians exist with **unselected** energy parameters. The candidate *physical quantum-charge and interaction selector* is PARKED.

## 1. Sources, question, and typed conventions

Read-only integrated source: \`ud-tetra/UD-Physics@59814ea16e94ac4048dc878ef99d23097ca63b9b\`, especially [finite discriminant pairing](../qpb1-finite-pairing/README.md), [integral cut/flow duality](../qpb1-integral-duality/README.md), [classical charge/field source](../qpb1-charge-field/README.md), [impedance selection](../qpb1-impedance-selection/README.md), and [loop-history/winding action](../qpb1-loop-history/README.md). The recent [two-boson nonselection PR #159](https://github.com/ud-tetra/UD-Physics/pull/159) is separate, unmerged, and read-only. No mainline writeback or source-ledger change.

Question: Does an existing native charge/coset object supply a physical scalar additive charge operator and a nontrivial, source-selected quantum Hamiltonian that could fix a quantum interaction rather than borrowing transmon spectroscopy?

Fix the complete graph K4 from the filled oriented tetrahedron. Reduced graph Laplacian (delete vertex3) is
\[
L=4I_3-\boldsymbol 1\boldsymbol 1^\top
=\begin{pmatrix}3&-1&-1\\-1&3&-1\\-1&-1&3\end{pmatrix},
\quad L^{-1}=(I_3+\boldsymbol1\boldsymbol1^\top)/4,
\quad\det L=16.
\]
Let \(D_{\rm cut}=\mathbb Z^3/L\mathbb Z^3\cong\mathbb Z_4^2\), with exact representatives and the induced tetrahedral permutation action on zero-total integer vertex-divisor charges. All calculations use integer and rational coefficients, not empirical units. This is the **cut-lattice graph-critical-group presentation**; the integrated finite-pairing audit uses the **flow-lattice discriminant** \(\Lambda^\#/\Lambda\) with a different Gram basis and bilinear convention. They have the same abstract K4 critical-group order and S4 orbit structure, while the respective perfect pairings should not be identified without explicitly fixing the cut/flow duality and sign. No equality of specific pairing matrices is assumed.

## 2. Complete signed permutation orbit test

Write integer vertex charge vector \(\rho=(t_0,t_1,t_2,-t_0-t_1-t_2)\). Under a vertex permutation \(p\in S_4\), permute all four entries and project to the quotient. The canonical class can be computed exactly from \(L^{-1}(t_0,t_1,t_2)^\top\bmod\mathbb Z^3\). Enumerating the 64 triples \(t_i\bmod4\) yields **16** distinct classes, as predicted by detL16. The 24 S4 actions preserve the quotient; all 64 representatives agree under each action.

**EXACT** S4 orbits:
- identity \(D[1]\): one zero class, order1;
- nonzero two-torsion \(D[2]\setminus\{0\}\): three order2 classes;
- all remaining classes: twelve order4 classes.

The sole S4-fixed class is zero. The cut-graph finite bilinear pairing \(b([t],[u])=t^\top L^{-1}u\bmod1\) is perfect and S4-invariant. Exactly 6,144 triples (24 permutations × 16 × 16 pairs) verify invariance; all 16 character orthogonality sums vanish for nonidentity characters by integer residue counts.

## 3. Charge operator: finite labels versus physical additive charge

A physical total additive charge \(Q\), if represented as a homomorphism \(q:D_{\rm cut}\to(\mathbb Z,+)\), must obey
\[
4q(d)=q(4d)=q(0)=0,
\quad\text{hence}\quad\boxed{q(d)=0\quad\forall d\in D}.
\]
The same holds for any torsion-free target group, including \(\mathbb R\). This is an exact group-theoretic obstruction **only for a scalar additive homomorphism defined on the finite quotient D**. It does NOT prevent additive integer charges on an unquotiented lattice, charge vectors transforming covariantly under S4, external source/reservoir flux, or a separately defined quantum charge-number operator.

For a scalar S4-invariant character \(\chi:D\to U(1)\), use the perfect S4-invariant pairing to identify the character group \(\widehat D\cong D\) equivariantly. Since \(D^{S_4}=\{0\}\), only the **trivial invariant scalar character** remains. Distinguish that from source finite Weyl **central characters** of \(\mu_4\), whose conjugate faithful choices \(k=1,3\) remain available because the center has trivial S4 action. A nontrivial central phase is not the same thing as a nontrivial invariant scalar additive charge on D.

The source charge-field work postulates a separate R6 field carrier with vertex charge \(\rho=B_1p\), and an independently added scale \(q_0\). That vector-valued continuous charge law is not the finite quotient scalar homomorphism tested here. Its physical Coulomb correspondence, impedance, clock and constitutive coefficients remain open under its own stated assumptions. Thus this theorem is not an obstruction to *every* UD charge hypothesis.

## 4. The Weyl-algebra Hamiltonian dichotomy

On a **newly assumed** quantum Hilbert space \(\mathcal H_D=\mathbb C[D]\) (complex dimension16), finite shifts act as \(T_x|z\rangle=|z+x\rangle\), and modulations as \(M_y|z\rangle=\exp(2\pi i b(y,z))|z\rangle\). Their nontrivial commutation phase is the finite source algebra, not a time-evolution law, physical hbar, a vacuum or a Born/charge calibration.

If an operator \(H\) commutes with every \(M_y\), perfect character separation forces \(H\) diagonal in the \(|z\rangle\) basis. If H also commutes with every translation \(T_x\), transitivity forces all diagonal entries equal:
\[
\boxed{[H,T_x]=[H,M_y]=0\ \forall x,y\in D\quad\Rightarrow\quad H=cI_{16}.}
\]
So requiring **full Weyl invariance of the Hamiltonian** yields a trivial single energy. This strong invariance is a separately imposed hypothesis, not native instruction that all Weyl operators must be physical symmetries of time evolution.

Relax that demand to full tetrahedral \(S_4\) invariance, and let H be merely diagonal in the finite charge-coset basis. It must then be constant on the three orbits:
\[
H=v_0P_{1}+v_2P_{2}+v_4P_{4},
\]
with freely selectable real \(v_0,v_2,v_4\). Removing an overall energy shift leaves TWO arbitrary spectral gaps. Positive examples such as \((v_2,v_4)=(1,1),(1,2),(2,1),(1,3)\), with \(v_0=0\), show that symmetry and positivity alone cannot fix an energy ratio. This is an explicit **subfamily** of S4-equivariant Hermitian operators, not a claim to classify their whole commutant. Adding finite Weyl hopping/flux terms would introduce further constitutive choices rather than a native physical source-selection rule.

Conventional graph chip-firing and finite Heisenberg/Weyl representations produce the exact same group, orbit and operator algebra. Consequently the source material yields no distinctive physical prediction, measured coupling or quantum charge unit.

## 5. Reproducibility, target exposure, and status

Reproduce:
\`python3 experiments/qpb-native-charge/audit.py --out /tmp/qpb-native-charge-001.json\`.

The exact Python 3 standard-library constructor verifies reduced Laplacian determinant16 and inverse, 16 class labels and 24 S4 permutations, all 64 representative well-definedness tests under all actions, orbits of sizes1/3/12, perfect pairing/character cancellation and 6,144 S4 pairing checks. It also checks six nonnegative S4-diagonal energy examples. The broad no-go statements follow from finite-torsion and Weyl irreducibility arguments, not numerical extrapolation. The input and output are retained in immutable [charge-001](../../artifacts/qpb-charge-20261024-gpt6-a1/charge-001/manifest.json), with source SHA-256 \`e62712e44162e3d4433c0a983cf1239c69917f0f339dd85ab8e6850e63cd8e6c\` and output SHA-256 \`1d4c6701b36badd8933bff10045362a2a35df40088f6f3c6912bc2acc1be8f81\`.

FIT / target exposure: the problem was selected after quantum-interaction nonselection in PR159 and publication of transmon spectra. No physical data, charge units or Hamiltonian coefficients were fitted; six integer energy choices are transparent development fixtures. The quantum Hilbert interpretation \(\mathbb C[D]\), full Weyl Hamiltonian symmetry and scalar-additive charge map are explicitly **HYPOTHESIS**, each with a separate scope. Other carrier choices or charge-valued vectors remain open.

This is constructor math, not independent mathematical peer review. Physical quantum UD device, Coulomb charge calibration, measured spectrum and genuine held-out test: NOT_EXECUTED. Candidate physical scalar-charge/Hamiltonian selector PARKED. No source was promoted to mainline.

**REOPEN only with:** a versioned native source process that selects a physical vector/charge current with \(q_0\) and a nontrivial quantum Hamiltonian, physical conjugate phase and action/clock scale, and a frozen test distinct from ordinary graph/Weyl and conventional superconducting-circuit nulls. **Next priority 98/100:** change the primitive/source-carrier rather than select more arbitrary orbit energies on the same D.
