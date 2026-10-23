# Integral tetrahedral duality audit v1.0

**RESULT — EXACT / CONDITIONAL.** In the preceding hypothetical tetrahedral field model, integral graph flows and their Euclidean dual have discriminant group `Z/4 × Z/4`. They are not similar lattices. The natural reduced integral phase grid therefore obstructs the isotropic electric–magnetic exchange used in the preceding normalization proposal. A different equal-cycle grid permits that exchange, but is an additional preparation convention; its relative scale remains free. No physical action, impedance or charge unit is selected.

**Discovery boundary:** this is a new lattice/preparation branch of [the real classical field candidate](../qpb1-charge-field/README.md). It changes no source ledger, theorem status or previous immutable run. Physical score **UNSCORED**; physical promotion **0**. No quantum commutator, compact gauge theory, measured charge or physical spacetime correspondence is derived.

## 1. Sources, objects and hypotheses

Repository base: `ud-tetra/UD-Physics@d7980ade886ff95083e1bb17641ab5af8be2265a`. [SOURCES.json](SOURCES.json) binds seven local dependencies by SHA-256. The uploaded historical v0.39 ledger and CRL2 proposal match their imported bytes; neither replaces the pinned v0.85 ledger. The missing Genesis PNG was not used. The executable imports rational matrix helpers from the preceding field audit and its action-normalization dependency.

External mathematical comparison: Bacher, de la Harpe and Nagnibeda, *The lattice of integral flows and the lattice of integral cuts on a finite graph*, Bull. SMF 125 (1997), 167–198, DOI `10.24033/bsmf.2303`; [author-hosted preprint](https://www.unige.ch/~laharpe/articles/19BaHaNa3fev97.pdf), dated 1997-02-03, §1 Propositions 1–2, §3 Proposition 8, §4 Lemma 1 and §6 complete-graph example. Its flow/cut lattice framework and projection description provide context. Every finite K4 assertion below is derived or checked here. The paper supplies no UD physical evidence.

Use the filled tetrahedron, ascending simplex orientations, lexicographic edges `(01,02,03,12,13,23)`, integral boundaries `B1: Z6→Z4`, `B2: Z4→Z6`, and the unit Euclidean edge metric. Write

\[
P_L=B_1^TB_1/4,\quad P_T=B_2B_2^T/4,\quad P_L+P_T=I_6.
\]

Retain the **hypothetical** real canonical fields `a,p∈R6`, vertex charge `rho=B1 p`, noncompact additive gauge, canonical one-form `pᵀda`, and positive energy

\[
H=\frac12p^T(u_LP_L+u_TP_T)p+\frac v2\|B_2^Ta\|^2,
\qquad u_L,u_T,v>0.
\]

Neutral gauge reduction gives three oscillators with native frequency `nu=2 sqrt(uT v)` and impedance factor `lambda=(1/2)sqrt(uT/v)`. Matching the already exposed native frequency 2 imposes `uT v=1` by inverse design. The optional physical dictionary remains `Q=q0 p`, `Phi=A0 a/q0`, `t=tau0 s`, `Zmode=lambda A0/q0²`. Neither `q0` nor `lambda` is independently anchored here. This R12 field carrier is distinct from native UD's active R14 carrier.

The new hypothesis is a **classical preparation grid**: edge coordinates and/or momenta may be integral in specified units at a preparation or strobe. Integer vertex charge alone, integer momentum on every edge, compactness, quantum quantization and all-time dynamical closure are different conditions. None implies the others automatically.

## 2. Exact integral bases and dual pairing

Let `F=ker B1` and `C=im B1ᵀ=F⊥`. Define flow and cut lattices

\[
\Lambda=F\cap\mathbb Z^6,\qquad
\Gamma=C\cap\mathbb Z^6=B_1^T\mathbb Z^4.
\]

An integral flow basis `L` consists of the first three face boundaries; a cut basis `C0` consists of vertex-gradient columns 1,2,3, with vertex 0 fixed:

\[
L=\begin{pmatrix}1&1&0\\-1&0&1\\0&-1&-1\\1&0&0\\0&1&0\\0&0&1\end{pmatrix},\quad
G=L^TL=\begin{pmatrix}3&1&-1\\1&3&1\\-1&1&3\end{pmatrix},\quad
C_0^TC_0=\begin{pmatrix}3&-1&-1\\-1&3&-1\\-1&-1&3\end{pmatrix}.
\]

The last three rows of `L` are `I3`; any integral flow is uniquely determined by those chord entries, proving this is the full saturated flow lattice. The first three rows of `C0` are `I3`; every integral edge gradient has integral potential differences, proving cut saturation. The fourth oriented face is `L(1,-1,1)`, so `im_Z B2=Lambda`. In particular **H1 of the filled complex is zero**. A rank-three graph flow lattice is not a new topological hole in the filled tetrahedron.

For `w=(1,-1,1)`,

\[
G=4I-ww^T,\quad G^{-1}=(I+ww^T)/4,
\quad\operatorname{spec}G=(1,4,4).
\]

Both Gram determinants are `16=2^4`; their Smith invariants are `(1,4,4)`, obtained from gcds of minors `(1,4,16)`. Each lattice has covolume 4, while its Euclidean dual has covolume 1/4. Gram determinant is the **square** of covolume.

Define the Euclidean dual **within F** by `Lambda#={x∈F:x·Lambda⊂Z}`. With `D=L G^-1`,

\[
L^TD=I_3,\quad \Lambda^\#=D\mathbb Z^3=P_T\mathbb Z^6,
\qquad \Gamma^\#=P_L\mathbb Z^6.
\]

Indeed `PT=D Lᵀ` and the chord identity gives `LᵀZ6=Z3`. Thus

\[
\Lambda^\#/\Lambda\cong\mathbb Z/4\oplus\mathbb Z/4,
\qquad [\mathbb Z^6:\Gamma\oplus\Lambda]=16.
\]

**Typed distinction:** the cut lattice `Gamma` lies in C, whereas the lattice dual `Lambda#` lies in F. They are not the same object. A graph cohomology quotient `Z6/Gamma` is not first cohomology of the full filled complex unless its closed-cochain condition is also imposed.

Starting with the extra edge grid `Z6_a × Z6_p`, neutral reduction gives

\[
A_{\rm grid}=\Lambda^\#\cong\mathbb Z^6/\Gamma,
\qquad P_{\rm grid}=\Lambda.
\]

In coordinates `a=Dq,p=Ln`, `pᵀda=nᵀdq`: this is a perfect integer pairing. It is classical kinematics, with no assumed quantum commutator or value of Planck's constant.

## 3. All sixteen discriminant classes and certified minima

The minimum nonzero squared norms are 3 in `Lambda` (8 vectors, the signed triangular boundaries) and 1/2 in `Lambda#` (12 vectors).

For flows, any nonzero integer circulation contains a directed simple cycle, and K4 has girth 3. Since `G≥I`, all vectors of norm at most 3 also lie in the coefficient cube `{-1,0,1}³`, allowing a complete minimal-vector count. For the dual,

\[
\|Dz\|^2=\frac{\|z\|^2+(z_1-z_2+z_3)^2}{4}.
\]

Its positive integer numerator is even, hence at least 2. Norm at most 1/2 forces `||z||²≤2`, making the same cube sufficient for the complete count.

Represent classes by `delta=G^-1 z mod Z3`, with `z∈{0,1,2,3}³`; these give all sixteen classes. For each class compute

\[
\mu(\delta)=\min_{n\in\mathbb Z^3}(\delta+n)^TG(\delta+n).
\]

| Class order | Number | Minimum squared transverse norm | S4 orbit size |
| --- | ---: | ---: | ---: |
| 1 | 1 | 0 | 1 |
| 2 | 3 | 1 | 3 |
| 4 | 12 | 1/2 | 12 |

This enumeration is complete, not a random sample. A centered representative has coordinates at most 1/2 in magnitude, so `G≤4I` bounds its cost by 3. Since `G≥I`, any coefficient of magnitude at least 2 gives cost at least 4. With `delta∈[0,1)³`, shifts outside `{-2,-1,0,1}³` cannot minimize. Exactly 64 shifts suffice per class. All 24 signed S4 actions preserve class minima and orders; the computed orbit sizes are 1,3,12.

For any integral zero-sum vertex charge rho choose integral `p0` with `B1p0=rho`. All integral solutions are `p0+Lambda`. Their common longitudinal part is `pL=B1ᵀrho/4`; their transverse parts lie in an affine coset of Lambda inside Lambda#. This coset depends on rho modulo the vertex Laplacian image. At zero configuration,

\[
H_{\min,\,p\in\mathbb Z^6}(\rho)
=\frac{u_L}{8}\|\rho\|^2+\frac{u_T}{2}\mu([\rho]).
\]

The identity class is precisely `rho∈B1 B1ᵀ Z4`, equivalently integral `pL`. These sixteen preparation obstructions do not establish sixteen particles, physical charge species or a quantization law.

## 4. A consequential preparation change: 1/6 versus 1/3

For `rho=(1,-1,0,0)`, the real electrostatic minimizer has `||pL||²=1/2`, nonintegral edge entries and energy `uL/4`. Integer **vertex** charge permits it.

The stronger requirement `p∈Z6` instead permits `p=(-1,0,0,0,0,0)`. It has the same rho, `||pL||²=||pT||²=1/2`, and attains the integral minimum `(uL+uT)/4`. Any nonzero integer edge vector has norm at least 1, proving optimality. A neutral triangular flow at zero configuration has energy `Hface=3uT/2`. Consequently

\[
\frac{H_{\min,\,p\in\mathbb R^6}}{H_{\rm face}}
=\frac{u_L}{6u_T},\qquad
\frac{H_{\min,\,p\in\mathbb Z^6}}{H_{\rm face}}
=\frac{u_L+u_T}{6u_T}.
\]

Under the additional identical-edge electric hypothesis `uL=uT`, these become **1/6** and **1/3**, respectively. The latter preparation carries irreducible radiative energy `uT/4`; it is **not a static electrostatic equilibrium**. Real oscillator evolution exchanges its radiative kinetic and magnetic energy. This new preparation branch does not falsify or silently amend the preceding real-valued 1/6 result.

## 5. Exchange obstruction and remaining scale freedom

The preceding isotropic canonical exchange is

\[
\mathcal D_\sigma(a_T,p_T)=(\sigma p_T,-a_T/\sigma),\quad\sigma>0.
\]

Energy invariance requires `uT=4v sigma²`; at matched frequency 2, `uT=2 sigma`, `v=1/(2 sigma)` and `lambda=sigma`.

On the natural grid `Lambda# × Lambda`, whole-grid bijectivity requires `sigma Lambda=Lambda#`. More strongly no similarity `sigma O Lambda=Lambda#` exists: the determinants require `sigma^6=1/256`, whereas the minimum norms require `sigma²=1/6`, giving `sigma^6=1/216`. The full S4 cycle representation has scalar commutant (character inner product 1, checked over all 24 elements), so there is also no same-sector S4-equivariant linear exchange between these lattices.

This is a scoped obstruction, not a prohibition of every integral canonical exchange. In perfect-pair coordinates `(q,n)`, `(q,n)→(n,-q)` is integral and symplectic. But

\[
H=\frac{u_T}{2}n^TGn+2v q^TG^{-1}q,
\]

so this exchange would require `uT G=4v G^-1`, impossible because `G²` is nonscalar. Changing the metric, representation, carrier or energy defines a different model.

An **extra** equal-cycle grid `A=P=Lambda` permits the scalar exchange only at `sigma=1`, selecting `lambda=1` at matched frequency. It retains only one of the sixteen natural configuration cosets and its coordinate pairing is G, determinant 16, rather than a unimodular perfect pairing. Moreover the family

\[
A=r\Lambda,\quad P=r^{-1}\Lambda,\quad
\sigma=\lambda=r^2,\quad u_T=2r^2,\quad v=1/(2r^2),\qquad r>0
\]

retains the same integer labels and canonical pairing matrix G while allowing every positive relative scale. Five rational fixtures are checked; the displayed algebra proves the whole family. No independently sourced rule chooses r or turns these labels into a measured charge/flux normalization.

There is an integral isometry between the cut and cycle lattices: the signed edge-complement star S obeys `S²=I`, maps Lambda bijectively to Gamma and satisfies `S Rpi=sign(pi) Rpi S`. It swaps orthogonal spaces and is parity twisted. This planar graph self-duality is not Lambda# and is not the same-sector phase exchange above. A separately specified dual-mesh field theory is not ruled out.

## 6. Clocks and dynamical compatibility

A nontrivial continuous oscillator flow cannot preserve a discrete full phase grid at every real time: each continuous trajectory into a discrete set would be constant. Thus an integral grid here is a preparation/strobe restriction, or it requires changed dynamics. It is not by itself a quantum theory.

For matched frequency 2, oscillator phase is `theta=2s` and

\[
F(\theta)=\begin{pmatrix}
\cos\theta\,I&\lambda\sin\theta\,I\\
-\sin\theta\,I/\lambda&\cos\theta\,I
\end{pmatrix}.
\]

A whole-grid map forces `cos(theta)` to be an integer because it acts as a scalar endomorphism on each full-rank lattice. Only 0,±1 are possible. On the natural grid, quarter-turns are obstructed by §5, leaving `theta∈pi Z`: a **Z2** whole-grid strobe per oscillator period. On the additional scaled-cycle grid with `lambda=r²`, quarter-turns work, giving `theta∈(pi/2)Z`: **Z4**. The corresponding smallest positive native intervals are `pi/2` and `pi/4`; mapping them to physical time still requires tau0.

These are **whole-grid automorphism** statements. Special initial states may return at additional phases. For example, at lambda 1 the natural grid contains a stable equal-cycle subgrid of index 16 that admits quarter-turns. No claim that every individual orbit has only Z2 returns is made.

## 7. Reproduction, evidence and next discriminant

Run from the repository root:

```bash
python3 experiments/qpb1-integral-duality/audit.py --out /tmp/qpb1-integral-duality
```

The standard-library rational audit checks seven source hashes, exact incidence/basis/Gram/Smith identities, sixteen complete class minimizations, 64 parameter/class energy checks, all 24 S4 permutations, four dipole parameter cases, five scale fixtures, and an explicit natural-grid quarter-turn failure. General minimum bounds, the no-similarity result, free positive scale family and continuous/stroboscopic arguments are analytic proofs above, with finite checks where stated. This is constructor verification, without a separate LLM review or empirical test.

See [the lattice contract](LATTICE_CONTRACT.md), [receipt](../../sessions/qpb1-integral-duality-20261022-a1/mathematical_receipt.json), [candidate](../../candidates/qpb1-integral-duality/candidate.json) and [immutable run](../../artifacts/qpb1-integral-duality-20261022-a1/exact-001/manifest.json).

**Next discriminant:** construct the finite discriminant bilinear pairing and classify its admissible phase/character choices. Test whether a primitive UD loop or holonomy rule independently supplies the needed choice before using a finite phase algebra as an action-normalization bridge. Dimensionless fourth-root phases alone would not determine hbar or q0.
