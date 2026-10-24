# Finite discriminant pairing and holonomy audit v1.0

**RESULT — EXACT / CONDITIONAL.** The tetrahedral discriminant group `D=Lambda#/Lambda ≅ Z4×Z4` has a perfect bilinear pairing. Its two faithful central characters are conjugate. For either primitive pairing, no scalar quadratic refinement is invariant under the full inherited S4 action. Four homogeneous refinements correspond equivariantly to the four boundary faces. Squaring them gives one common invariant sign rule on `D/2D ≅ Z2×Z2`. A finite Weyl algebra exists without choosing a refinement, but neither it nor a finite endpoint phase selects a physical action normalization.

Discovery base `ud-tetra/UD-Physics@a4e588d84ad8b7acf080a93d40a63e27b0aeb48c`. The [source manifest](SOURCES.json) binds nine local dependencies. Mainline head was verified unchanged at `ud-tetra/UD@957d443e25008632ab9d9328c162343b6a651ee7`. Fifteen relevant ledger rows are preserved in [SOURCE_ROWS.json](SOURCE_ROWS.json); archive label v0.85 and inherited scientific_revision v0.43 remain distinct. The uploaded historical v0.39 ledger and CRL2 proposal hash-match their imported copies. They supply historical provenance and governance context, not a new primitive holonomy operator. The uploaded seam_phase_transport file contains only a reconstruction placeholder. Missing Genesis PNG was not used. This is not a complete audit of every attachment or ledger dependency.

Physical score **UNSCORED**; physical promotion **0**. No source status, mainline registry, previous immutable result or shared CURRENT file is changed.

## 1. Typed objects and conventions

Retain the Euclidean K4 flow lattice from [the integral audit](../qpb1-integral-duality/README.md). Let L be its three-column cycle basis and

\[
G=L^TL=\begin{pmatrix}3&1&-1\\1&3&1\\-1&1&3\end{pmatrix},
\qquad G^{-1}=\frac14\begin{pmatrix}2&-1&1\\-1&2&-1\\1&-1&2\end{pmatrix}.
\]

A class has cycle coordinates `delta∈G^-1 Z3/Z3`. Choose `u=[G^-1 e1]`, `v=[G^-1 e2]`; they freely generate D as a Z4-module. This is the **ring Z/4**, not a field; 2 has no modular inverse. Coordinates `(m,n)` are taken modulo 4. The Euclidean pairing descends because changing either representative by a lattice vector changes its pairing with a dual-lattice vector by an integer:

\[
b(x,y)=x\cdot y\pmod1,
\quad [b]_{u,v}=\frac14\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

The numerator determinant is 3, a unit modulo 4, so `b:D→Hom(D,Q/Z)` is an isomorphism. Phases are written in **turns**: `r∈Q/Z` represents `exp(2 pi i r)`. No action dimension, physical clock or Planck constant appears in this definition. These classes are lattice quotients, not holes of the filled tetrahedron, whose H1 is zero.

Primary mathematical comparisons, with assumptions checked rather than silently imported:

- Deloup–Massuyeau, *Quadratic functions on torsion groups*, [arXiv:math/0301040v3](https://arxiv.org/pdf/math/0301040), version dated 2004-07-15; §1 and §§2.1–2.2. Their quadratic functions over a fixed bilinear pairing form an affine family; characteristic forms implement the lattice construction. The PDF also carries a later typesetting date, not treated here as a new arXiv version.
- Prasad–Vemuri, *Inductive algebras for finite Heisenberg groups*, [arXiv:0803.2921v1](https://arxiv.org/pdf/0803.2921), 2008-03-20; §2 and §4. Their finite abelian setting permits exponent 4; no odd-prime finite-field theorem is applied here. Our finite operator construction is checked explicitly below.

These papers provide conventional mathematical context, not UD physical evidence. See [external-source metadata](EXTERNAL_SOURCES.json).

## 2. Characters and invariant bilinear forms

All sixteen additive characters of D are `x→exp(2 pi i b(t,x))`, labelled by `t∈D`. This does **not** mean D has a faithful one-dimensional character: D is noncyclic. Instead, consider characters of the **central phase group** `mu4={1,i,-1,-i}`:

\[
\chi_k(i^j)=i^{kj},\quad k\in\mathbb Z/4,
\qquad B_k(x,y)=\exp(2\pi i k b(x,y)).
\]

| k | Radical size of k b | Central character | Consequence |
| --- | ---: | --- | --- |
| 0 | 16 | Trivial | No pairing information |
| 1 | 1 | Faithful | Perfect phase pairing |
| 2 | 4 | Nonfaithful | Factors through D/2D |
| 3 | 1 | Faithful, conjugate to k=1 | Perfect conjugate pairing |

A complete search over the 64 symmetric bilinear forms on Z4² gives exactly four invariant under all 24 inherited S4 actions: `0,b,2b,3b`. Thus full tetrahedral symmetry preserves both primitive central characters; it does not choose between them. The given Euclidean pairing is b; replacing it by k b is an explicit phase-character choice.

The two-copy phase-label group `D×D` with this pairing supports a finite central extension by mu4 of order `4*16²=1024`. This is an algebraic construction, not a count of physical states or particles.

## 3. Oddness prevents naive quadratic descent

A quadratic refinement here means `q:D→Q/Z` with

\[
q(x+y)-q(x)-q(y)=b(x,y),\qquad q(0)=0.
\]

The expression `||x||²/2 mod1` does **not** descend to D: 0 and one triangular boundary are representatives of the same zero class, but their half squared norms are 0 and 3/2, differing by 1/2 modulo 1. This explicit witness prevents silently dividing the bilinear form by 2 in Z4.

A valid coordinate refinement is

\[
q_0(m,n)=\frac{m^2+n^2-mn}{4}\pmod1.
\]

Changing m or n by 4 changes this by an integer. Every other refinement is

\[
q_t(x)=q_0(x)+b(t,x),\quad t\in D.
\]

**Completeness proof:** the difference of two refinements is additive; perfect b supplies all sixteen additive characters. Hence there are exactly sixteen refinements, not merely sixteen examples. Four are homogeneous, equivalently `q(-x)=q(x)`; in this parametrization they are the shifts `t∈D[2]`.

Under the inherited S4 action, the sixteen refinements form orbits of sizes **4,6,6**, with the four homogeneous refinements constituting the orbit of size 4. None is fixed. The conjugate pairing −b has the same statement by `q→−q`.

A short proof independently checks the absence of an invariant refinement. S4 is transitive on the twelve order-four classes. If q were invariant, its value on `u,v,-v,u+v,u-v` would be one common a. Polarization with `(u,v)` would require `-a=-1/4`; polarization with `(u,-v)` would require `-a=+1/4`. These are incompatible in Q/Z. No homogeneity assumption is needed for this obstruction.

This excludes a single invariant scalar refinement of this particular primitive b. It does not exclude an equivariant family, a projective action with compensating characters, another phase carrier, or the Weyl algebra in §5.

## 4. Four faces and an invariant parity shadow

For each oriented triangular boundary `c_f∈Lambda`, its coefficient vector satisfies `G c_f ≡(1,1,1) mod2`: it is characteristic. The corrected expression

\[
q_f([x])=\frac{\|x\|^2-x\cdot c_f}{2}\pmod1
\]

is representative independent. For a shift `ell∈Lambda`, the change is `x·ell+(||ell||²-ell·c_f)/2`, an integer. Reversing the orientation of c_f changes q by the integer `x·c_f`, so the refinement depends on the unoriented face. The four faces give exactly the four homogeneous refinements:

| Boundary face | Shift t relative to q0 |
| --- | --- |
| 012 | (0,2) |
| 013 | (2,0) |
| 023 | (0,0) |
| 123 | (2,2) |

The exact covariance is `q_(pi f)(pi x)=q_f(x)`. Choosing one homogeneous refinement is equivalent to choosing a face, or its opposite vertex; its stabilizer has order 6. An S4-invariant central hub alone does not select a boundary face. There is no asserted physical symmetry-breaking mechanism here.

A useful reduction survives without choosing a face:

\[
\bar q(x):=2q_f(x)
=\begin{cases}0,&x\in2D,\\1/2,&x\notin2D.\end{cases}
\]

This is independent of f and S4 invariant. It descends to the four-class quotient `D/2D≅Z2²`, with sign +1 on zero and −1 on its three nonzero classes. Its polarization is **2b**, whose radical in D is `2D` of size 4; it is not a primitive refinement of b. Squaring loses the fourth-root distinction. Multiplying all four face phases instead gives the identity at every class; that product cannot restore the missing information.

## 5. Explicit finite Weyl algebra and its limits

On the deliberately introduced complex vector space `H=C[D]` of dimension 16, define

\[
T_x|z\rangle=|z+x\rangle,\qquad
M_y^{(k)}|z\rangle=e^{2\pi i k b(y,z)}|z\rangle.
\]

For k=1 or 3,

\[
M_yT_x=e^{2\pi i k b(y,x)}T_xM_y,
\qquad \frac1{16}\operatorname{Tr}(T_xM_y)
=\begin{cases}1,&x=y=0,\\0,&\text{otherwise}.\end{cases}
\]

The audit verifies every x,y,z for both primitive characters: **8192 commutation checks**, plus **512 trace checks**. Perfect b makes the modulations separate all basis states; an operator commuting with all modulations is diagonal, and commuting also with all translations makes it scalar. This proves irreducibility of this representation directly. The inherited S4 action `U_pi|z>=|pi z>` is covariant for translations and modulations because b is invariant. No quadratic refinement is needed for this construction.

This is a finite algebra of unitary matrices, **not** a derivation of continuous quantum dynamics, a vacuum, a Born rule or physical hbar. In finite dimension an exact additive CCR `[Q,P]=i hbar I` with nonzero hbar is impossible: taking the trace gives `0=i hbar dim(H)`. Finite Weyl relations are multiplicative relations, not an exception to that trace identity. No Hamiltonian, continuum limit or physical apparatus has been selected by the finite construction.

## 6. Winding, source gates and physical normalization

The inspected source subsystem says:

| Source objects | Source content | Consequence here |
| --- | --- | --- |
| O09 | Lifted action I=(1/2)sum a Delta_phi; closed I=pi sum a n | Winding and support must be retained to recover action |
| O10/O11 | Native A0 and conditional recurrence pi A0 | No independent physical unit anchor |
| O14/G06 | eta_A=A0/hbar direction fixed; numerical value and primitive normalization equality open | Finite character choice cannot silently close this gate |
| Q282–Q286 | Single-tet specific action A0/2; normalized-ray recurrence | Normalization is not physical support quantization |
| Q287/Q288 | Postulated QPB1 eta_A=2 candidate | Preserve status; no promotion or refutation from an unrelated finite phase |
| Q339 | Integer-winding seam endpoint e^(i2pi n)=1 loses winding | Finite endpoints require a separate lifted-history receipt |
| G07 | Raw-trace factor 1/d_R is conditional bookkeeping | The new finite trace factor 1/16 is not an action coefficient |

A fourth-root character of the lifted winding group, `n→i^(k n)`, retains at most n modulo 4. Histories n and n+4 have identical finite endpoint phase but native action difference `4 pi a A0` for any fixed positive support a. Twenty-seven support/winding aliases are checked. A source-native full-period endpoint is identity; a nontrivial fourth-root assignment must be a map from **lifted histories**, not a function of that endpoint alone.

For a deliberately **added test dictionary**, identify a normalized Hodge winding's action `S=pi A0 n` with the physical phase formula `exp(i S/hbar)`, and demand it equal `i^(k n)` for every integer n. Then and only then,

\[
\eta_{\mathcal A}\equiv k/2\pmod2.
\]

For k=1 the positive examples are `1/2,5/2,9/2`; for k=3 they are `3/2,7/2,11/2`. Endpoints leave an infinite branch ambiguity. The previously exposed eta_A=2 would give a trivial full-winding phase, so it is incompatible **with this added primitive-fourth-root-per-Hodge-winding dictionary**, not with the existence of the finite algebra. This is a comparison between explicit hypothesis branches, not a falsification of source QPB1. There is no source-derived reason here to impose this dictionary.

More generally, any identity between phase turns, the Hodge lifted action and a measured quantum phase needs an explicit same-carrier path map, composition rule, normalization and independently anchored action unit. The finite algebra does not select q0, the constitutive factor lambda, physical time or an absolute impedance. The inspected sources do not supply the missing loop-history-to-discriminant map or a primitive physical central-character rule. This is a scoped source finding, not a proof that no such rule exists anywhere in UD.

## 7. Reproduction and next test

```bash
python3 experiments/qpb1-finite-pairing/audit.py --out /tmp/ud-finite-pairing
```

The standard-library audit checks nine source hashes, fifteen exact ledger-row matches, all 256 class pairings, all 64 symmetric bilinear forms, all 24 S4 actions, all sixteen refinements, 1728 characteristic representative shifts, 8192 finite Weyl commutations, 512 traces, 27 winding aliases and two conditional eta congruence families. General completeness, the independent invariant-refinement obstruction, quotient construction and trace/scale limitations are proved above. This is constructor verification; no separate LLM or empirical review is claimed.

See [phase contract](PHASE_CONTRACT.md), [receipt](../../sessions/qpb1-finite-pairing-20261023-a1/mathematical_receipt.json), [candidate](../../candidates/qpb1-finite-pairing/candidate.json) and [immutable run](../../artifacts/qpb1-finite-pairing-20261023-a1/exact-001/manifest.json).

**Next discriminant:** construct a typed map from native lifted loop histories into this finite algebra, preserving composition and S4 covariance, and test its kernel against O09 action. Compare an invariant parity readout with the face-indexed fourth-root family. Retain any missing lift explicitly; do not identify a residue label with unrestricted action.
