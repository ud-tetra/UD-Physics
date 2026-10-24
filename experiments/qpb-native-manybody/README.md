# Native UD many-body interaction source audit

**RESULT — EXACT / CONDITIONAL** two-boson symmetry classification; **FAILED** source selection of \(U/\varepsilon\); quantum physical attribution **PARKED**. The original carrier, finite pairing, native action and source laws remain read-only.

## Typed setup and source provenance

Integrated source base: \`ud-tetra/UD-Physics@e8a6a40d229090a1c6c783aef2832d38c3e7784f\`. Read-only [local generators](../qpb1-local-generators/README.md), [finite discriminant pairing](../qpb1-finite-pairing/README.md), [integral duality](../qpb1-integral-duality/README.md), [loop history](../qpb1-loop-history/README.md), [native events](../qpb1-native-events/README.md), [unit preparation](../qpb1-unit-preparation/README.md) and [source reservoir](../qpb1-source-reservoir/README.md). Previous [quantum-extension PR #154](https://github.com/ud-tetra/UD-Physics/pull/154) is unmerged research, NOT an integrated dependency. None of these inspected source objects selects a bosonic pair-interaction energy. The source audit is scoped; unread/new primitives can change its premises.

The underlying state is the oriented filled-tetrahedron real chain C=R15 with unit Euclidean metric H=I and ascending simplex orientation. On the native rank14 active plane, J=A/2 defines an assumed complex scalar i=-J. The resulting one-particle representation of signed S4 is \(\mathcal H_1=\mathbf3\oplus\mathbf3'\oplus\mathbf1'\) (complex dim7). This is a native simplex-label symmetry, **not** an experimentally established spacetime/superconductor symmetry. Native time s is dimensionless; physical chi (action, joule-seconds) and tau0 (seconds per native unit) remain external.

## Exact symmetric-square and the interaction parameter

**NEW HYPOTHESIS:** impose identical-boson exchange and \(\mathcal H_2=\operatorname{Sym}^2\mathcal H_1\), complex dimension 7*8/2=28. For a finite-group element g, \(\chi_{\mathrm{Sym}^2V}(g)=[\chi_V(g)^2+\chi_V(g^2)]/2\). Across S4 classes identity, transposition, double transposition, 3-cycle and 4-cycle (sizes 1,6,3,8,6), the native one-particle character is (7,-1,-1,1,-1), so the two-boson character is **exactly (28,4,4,1,0)**.

Inner products with the five irreducible characters give the exact decomposition
\[
\boxed{\operatorname{Sym}^2(\mathbf3\oplus\mathbf3'\oplus\mathbf1')
=3\mathbf1\oplus\mathbf1'\oplus3\mathbf2\oplus4\mathbf3\oplus2\mathbf3'.}
\]
Dimension check 3+1+6+12+6=28. The S4-compatible Hermitian commutant has REAL dimension 3²+1²+3²+4²+2²=**39**. The three native one-body Hermitian sector scalars induce a three-dimensional subspace, leaving 36 additional operator directions under the broad two-boson assumptions. This is an algebraic model-family count, **not** a count of physical species or independently realizable laboratory couplers.

The hidden \(\mathbf1'\) one-particle mode has a trivial signed-S4 two-boson state \(|hh\rangle\). Thus \(Q_{hh}=|hh\rangle\langle hh|\) is an invariant positive rank-one projector. For any real \(U\ge0\), the postulated
\[
H_2=d\Gamma(h)+UQ_{hh}
\]
has the same symmetry and a positive extra pair energy. \(|hh\rangle\) has energy \(2\varepsilon+U\) while a free pair has \(2\varepsilon\). All ratios \(U/\varepsilon\in\{0,1/8,1/4,1/2,3/4,1\}\) pass the exact positivity check. They are **selected illustrative fixtures**, not six privileged physical values. The native incidence, winding and source-reservoir laws do NOT fix \(U\).

## Finite Weyl phase cannot fix the energy

The integrated finite discriminant has \(D=\mathbb Z_4^2\) and two faithful primitive central Weyl phases \(i^k\) for k=1 or3, but no full-S4-fixed scalar quadratic refinement for its primitive pairing. Those phases are dimensionless finite algebra, NOT an automatically selected Hamiltonian or action scale.

To stress the strongest conceivable correspondence, additionally POSTULATE/FIT that one primitive Weyl phase equals the pair interaction phase after one native free recurrence s=pi. With \(\varepsilon\tau_0/\chi=2\), this gives
\[
e^{-i U\pi\tau_0/\chi}=i^k,\quad
\boxed{U/\varepsilon\equiv-k/4\pmod{1}}.
\]
For k=1 the nonnegative values include 3/4,7/4,11/4,...; for k=3 they include 1/4,5/4,9/4,... . Both orientations and infinitely many temporal phase aliases remain, and imposing this relationship is a new bridge assumption. Without it, \(U/\varepsilon\ge0\) remains continuous and free.

## Null, verification, and next gate

A conventional two-boson projector/Kerr Hamiltonian with the same U has *exactly the same* spectrum and readout law. The full transmon charge rotor, physical action, clock, port and source/measurement coupling are not derived from UD. Choosing U to match known transmon anharmonicity is FIT, not a held-out prediction.

Reproduce: \`python3 experiments/qpb-native-manybody/audit.py --out /tmp/ud-manybody-001.json\`. An exact standard-library Fraction constructor checks 24 signed S4 permutations, five cycle classes, squared classes, symmetric-square character/irrep multiplicities, commutant dimension39, six positive interaction ratios and eight primitive alias fixtures. A longer separately coded constructor was also run in the **same assistant context**, not externally reviewed. See [immutable source/result manifest](../../artifacts/qpb-manybody-20261024-gpt6-a1/manybody-001/manifest.json). The actual local executed path was \`/mnt/data/qpb_manybody_20261024/compact.py\`; the manifest gives the byte-identical **repository-root reproduction command**, not the literal staging pathname. Source SHA-256 b8f7310bceddb67a45b8c00f20e929a0f171d21795d50787ed36ff48fdc40c38; output SHA-256 b5b02dd4b3f90390ecc8e815a95bf8f6b2e06570463102fcc1e2c0ad5a9001fe.

**Status:** EXACT/CONDITIONAL no-selection result, HYPOTHESIS tensor/Fock and Weyl-energy maps, FAILED physical attribution, independent mathematical review NOT_RUN, empirical test NOT_EXECUTED. No mainline writeback.

**Next step, priority 98/100:** seek a separately versioned *native microscopic* pair interaction with fixed \(U/\varepsilon\), independently calibrated physical action/time/port mapping and genuinely unused transition data. Otherwise retain this source-selection obstruction and park the present quantum bridge.
