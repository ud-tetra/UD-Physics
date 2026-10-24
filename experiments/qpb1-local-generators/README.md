# Local generators, detuning and exact-return sensitivity v1.0

**RESULT — EXACT / CONDITIONAL.** On the single filled tetrahedron with the
signed S4 action and Euclidean chain metric, every real linear skew-adjoint
equivariant generator is

\[
\boxed{G(g_1,g_2,g_3)=g_1K_1+g_2K_2+g_3K_3},\qquad
K_k=D_k-D_k^T.
\]

Here D_k embeds the oriented boundary from degree k to degree k-1. This
three-dimensional family is already simplex-incidence-local and commutes
with the original J. The earlier visible/hidden two-rate law is exactly
`g1=g2=omega_v/2`, `g3=omega_h/2`. A single added face–cell gain therefore
realizes the proposed detuning locally. Symmetry, locality, positivity and
nilpotence permit it but do not select it or its value. The unmodified
unit-metric, unit-incidence source retains `g1=g2=g3=1` and trivial ray motion.

**New limitation:** the earlier state-ball certificate does not extend to
independent gain errors at a newly chosen exact ray recurrence. An explicit
arbitrarily small gain perturbation changes the reference recurrence phase
from -1 to +1 while its exact return time diverges. A finite-window phase
readout needs its own endpoint and error contract.

Source base `ud-tetra/UD-Physics@79fd6d6cc8f2d40d516df0074e728e3f9428f60b`;
recorded 2026-10-23 (America/Chicago). [SOURCES.json](SOURCES.json) binds sixteen
read-only dependencies and fresh exact-byte comparisons of the supplied
v0.39 ledger and CRL2 proposal with their committed imports. Archive v0.85
retains scientific_revision v0.43; [SOURCE_ROWS.json](SOURCE_ROWS.json)
preserves thirteen literal rows. The recovered carrier/master-action/packet
attachments contain placeholders and supply no new law. Missing Genesis PNG
is unused. Physical score **UNSCORED**, promotion **0**. No mainline ledger,
earlier candidate, or shared CURRENT is amended.

## 1. Typed question and retained conventions

Work over Q for exact matrices and over R for their coefficient spans and
states. The carrier is

\[
C=\bigoplus_{k=0}^3 C_k(\Delta^3;\mathbb R),\quad
f=(4,6,4,1),\quad\dim C=15,
\]

with ascending simplex orientations, unit metric, and the actual full
signed action R(p) induced by all 24 vertex permutations. The matrices D_k
are 15 by 15 embeddings of the three boundary blocks. Retain

\[
d=D_1+D_2+D_3,\quad A=d-d^T,\quad
J=A/2,\quad P=-A^2/4,\quad \operatorname{rank}P=14.
\]

**Incidence locality** means `G_sigma,tau=0` unless one simplex is a
codimension-one face of the other. It is locality on chain registers, not
an established distance, material interaction range or spacetime causal cone.
The question concerns real **linear, time-independent** generators on this
carrier, with `G^T=-G` and `R(p)G=GR(p)`. It does not classify nonlinear
state-dependent sources, gated open systems, larger glued carriers,
reduced symmetry, different metrics or dissipative generators.

## 2. Complete equivariant skew classification

There are `15*14/2=105` standard skew matrices S_ij, each with entries +1 at
(i,j) and -1 at (j,i). Define the exact finite-group projection

\[
\mathscr R(M)=\frac1{24}\sum_{p\in S_4}R(p)MR(p)^T.
\]

Because R is orthogonal, this maps skew matrices to skew matrices, is
equivariant, and fixes every equivariant skew matrix. Its image is therefore
the entire desired space. Compute its action on **all 105 basis matrices**,
not a sample of possible generators. The exact signed orbit sums give:

| Pair type | Unordered register pairs | Reynolds image |
| --- | ---: | --- |
| Vertex–edge incidence | 12 | `D1_ij K1/12` |
| Edge–face incidence | 12 | `D2_ij K2/12` |
| Face–cell incidence | 4 | `D3_ij K3/4` |
| Every other pair | 77 | 0 |

Here i<j uses the degree-ordered carrier. These finite equalities are
reproducibly checked in [audit.py](audit.py). They show the image is spanned
by K1,K2,K3; the three matrices are independent because their nonzero blocks
are disjoint. This proves the full real coefficient classification. In
particular no additional nonlocal skew coupling survives this exact signed
S4 averaging on this carrier.

For any equivariant G, the coefficients are explicitly recoverable:

\[
g_k=\frac1{n_k}\sum_{\substack{\sigma\subset\tau\\
\dim\tau=k,\ \dim\sigma=k-1}}
(D_k)_{\sigma\tau}G_{\sigma\tau},\qquad (n_1,n_2,n_3)=(12,12,4).
\]

An additional algebraic check uses characters. If chi(p)=Tr R(p),
antisymmetric tensor projection gives character
`(chi(p)^2-chi(p^2))/2` on skew matrices. The exact sums over all 24 actions
yield

\[
\dim\operatorname{End}_{S_4}(C)=\frac1{24}\sum_p\chi(p)^2=13,
\]
\[
\dim\mathfrak{so}(C)^{S_4}
=\frac1{48}\sum_p[\chi(p)^2-\chi(p^2)]=3.
\]

This corroborates the Reynolds image rank via a separate algebraic formula
in the same constructor audit; it is not independent empirical or peer review.

## 3. Sectors, positive energy and local support receipts

Boundary composition and the degree blocks imply

\[
D_iD_j=0\quad\hbox{for all }i,j,\qquad K_iK_j=0\quad(i\ne j).
\]

Set `P_k=-K_k^2/4`. Exact matrices verify that these are mutually orthogonal
orthogonal projectors with ranks `(6,6,2)`, sum P, and

\[
P_1+P_2=P_v,\qquad P_3=P_h,\qquad [K_k,J]=0.
\]

Thus every classified generator automatically preserves the original
complex structure, the active carrier, and all three sectors. Its spectrum,
with multiplicities retained even when values coincide, is

\[
\operatorname{spec}G:quad 0^1,
\quad(\pm2ig_1)^3,\quad(\pm2ig_2)^3,\quad(\pm2ig_3)^1.
\]

Zeros or negative gains remain skew-equivariant possibilities; zero gains
add static modes and negative gains reverse their phase orientation. For
the positive-energy branch impose g_k>0 explicitly. Then

\[
\Omega_g=-JG=2\sum_k g_kP_k>0\quad\hbox{on }\operatorname{im}P,
\qquad G=J\Omega_g,
\]
\[
H_g(x)=\tfrac12\langle x,\Omega_gx\rangle
=\sum_k g_k\|P_kx\|^2.
\]

All three sector norms and H_g are conserved. This is a conservative family;
it supplies no growth, attraction, intersector support transfer or preferred
preparation. Weighted differential `d_g=sum g_k D_k` still satisfies `d_g^2=0`.
It is a weighted real differential, distinct from changing the original
integer incidence definition.

For local stock `rho_i=x_i^2` and `x'=Gx`, define

\[
j_{i\leftarrow j}=2G_{ij}x_ix_j=-j_{j\leftarrow i},\quad
\dot\rho_i=\sum_j j_{i\leftarrow j}.
\]

Only incident pairs carry this current. For **every** register subset U,
antisymmetry cancels its internal currents, leaving
`d sum_(i in U)rho_i/ds=sum_(i in U,j outside U)j_(i<-j)`.
The code verifies stock rates and 15 prefix cuts at each of 30 rational gain
triples, giving 450 cut checks. The all-subset assertion follows from the
displayed cancellation proof, not exhaustive subset sampling.

## 4. Detuning is local, but its selection is an extra premise

Using `P_v=P1+P2` and `P_h=P3`, the previous two-rate generator obeys

\[
J(\omega_vP_v+\omega_hP_h)
=\frac{\omega_v}{2}(K_1+K_2)+\frac{\omega_h}{2}K_3.
\]

With the lower two source gains held at one, the one-parameter family is

\[
\boxed{G=A+(\gamma-1)K_3},\qquad\gamma>0.
\]

The change modifies only the four face–cell incidence pairs, with their
existing orientations. Nontrivial relative phase requires gamma different
from one. No nonlocal projector needs to be implemented as an interaction;
the projector expression was a spectral description of this local law.

| Declared premises | Consequence | Unselected input |
| --- | --- | --- |
| Original unweighted incidence and H=I | `g=(1,1,1)`, G=A | No detuning in this retained law |
| Signed S4, Euclidean skewness, incidence locality | Full `R3` gain family | All three gains |
| Add positive energy in original J structure | `g_k>0` | Positive gain ratios and common scale |
| Also preserve the two lower incidence rates | `g=(1,1,gamma)` | gamma and why it differs from one |
| Require the visible sector to retain one rate | `g1=g2` | This equality and the hidden contrast |

S4 preserves degree; it cannot by itself equate vertex–edge, edge–face and
face–cell rates. Nor does the classification disprove a future nonlinear or
constitutive rule selecting them. It establishes **permission, not native
selection**, within the stated linear class. The old native law and its
constant-ray result remain intact.

There is a second conditional realization if the metric is changed. Keep
unweighted d but assume a positive degree-scalar metric
`H=diag(h0 I4,h1 I6,h2 I4,h3 I1)`. The metric-skew operator is

\[
A_H=d-H^{-1}d^TH.
\]

Under whitening `y=H^(1/2)x`, its Euclidean representative is precisely
`G(g1,g2,g3)`, where

\[
g_k=\sqrt{h_{k-1}/h_k},\qquad
h_k=\frac{h_0}{(g_1\cdots g_k)^2}.
\]

Every positive triple has such a metric, unique up to common metric scale
within this degree-scalar family. For the one-parameter contrast with
`h0=h1=h2=1`, take `h3=gamma^(-2)`. Thirty rational whitening fixtures verify
both the transformed operator and metric adjoint exactly. Changing metric
changes the support/readout convention as well: original x has norm `x^THx`
and `J_H=H^(-1/2)JH^(1/2)`. The corresponding connection uses that metric and
J_H. This does not select a metric or identify it with the original unit
metric; it exposes the alternative assumption and coordinate map explicitly.

## 5. General ray return and a gain-error challenge

Retain `alpha=<Jx,dx>/||x||^2` from the previous audit and its convention
`Hol=exp(i*(chi_end-integral alpha))`. For an active state with all three
sectors populated, write `r_k=||P_k x||^2/||x||^2`. Along the new law,
sector k rotates at angular rate `2g_k`. A ray closes at T exactly when

\[
(g_k-g_1)T=\pi n_k,\quad n_k\in\mathbb Z,\quad n_1=0.
\]

Its geometric phase is

\[
\boxed{\mathrm{Hol}(T)=\exp\left(-2\pi i\sum_k n_kr_k\right)}.
\]

For rational gains not all equal, let q be the positive rational gcd of
their differences; the minimal populated-three-sector ray period is
`T=pi/q`. For a full state return, absolute gains must instead satisfy
`g_k T in pi Z`. With real gains a ray return requires commensurate active
relative gaps. Example `g=(1,2,1+sqrt(2))` with all sectors populated has no
nonzero exact ray return, since simultaneous conditions would make sqrt(2)
rational. Two populated sectors always have a ray period when their rates
differ. The three-sector incommensurability conclusion is explicitly scoped.

The previous unit reference `y0=(e01+h)/sqrt(2)` has

\[
(r_1,r_2,r_3)=(1/4,1/4,1/2).
\]

At `g=(1,1,3/2)` the ray period is `2pi`, relative windings are `(0,0,1)`,
and Hol=-1. Now take any odd integer N>=3 and perturb only the second gain:

\[
g^{(N)}=(1,1+1/N,3/2).
\]

The error is `1/N -> 0`. Because `gcd(1/N,1/2)=1/(2N)`, the **new minimal
ray period** is `2N*pi`; relative windings are `(0,2,N)`. Hence

\[
\sum_k n_kr_k=\frac12+\frac N2=\frac{N+1}{2}\in\mathbb Z,
\qquad \boxed{\mathrm{Hol}=+1}.
\]

This is an exact arbitrarily-small-error family; the six audited values
`N=3,5,11,101,1001,1000001` verify the implementation. The proof applies
to every odd N, not only those fixtures. At the old window `T=2pi`, the
two formerly locked visible sectors instead have a relative endpoint
phase of `4pi/N`: the ray is no longer exactly closed. Return times change
and diverge, so this is not a discontinuity of finite-time state evolution.

The earlier norm1/10 state-ball result is preserved at its **fixed two-rate
generator**. It never certified independent gain errors. The two-rate
equality `g1=g2` is a codimension-one condition in this symmetry-permitted
family; exact three-rate return itself is generally lost for incommensurate
gaps. Finite-window phase estimation, endpoint closure tolerance and an
operational interference/readout rule are needed before claiming robust
phase under parameter uncertainty. This challenge does not show those
separate finite-window constructions impossible.

## 6. Selection, evidence and handoff

Reproduce with standard-library Python, from repository root:

```bash
python3 experiments/qpb1-local-generators/audit.py --out /tmp/ud-local-generators
```

The audit passes sixteen source hashes, thirteen literal ledger rows, all
24 signed actions, the complete 105-element skew basis with Reynolds rank3
and character dimension3, sector ranks6/6/2, 30 positive gain triples,
450 cut checks, 30 metric-whitening checks, three two-rate local identities,
27 rational recurrence receipts and six odd-N gain challenges. Central
matrix statements are exact finite-dimensional calculations; the general
coefficient family follows from the complete basis projection. Continuous
parameter and recurrence-limit claims have the proofs above. This is
constructor work with an additional algebraic check, not non-constructor
review or empirical replication.

The gain contrast and phase-sign examples were selected after exposure to
the earlier two-rate candidate. No physical dataset, measured rate or
action target was fitted. The positivity cone and metric freedom leave
continuous parameters, and common rescaling `g -> lambda*g` changes native
periods while leaving closed-ray geometric phases unchanged. These phase
receipts cannot alone determine a native clock scale or A0/hbar. O14's
ratio direction remains fixed; its numerical value remains OPEN.

See [candidate](../../candidates/qpb1-local-generators/candidate.json),
[receipt](../../sessions/qpb1-local-generators-20261023-a1/mathematical_receipt.json)
and [immutable run](../../artifacts/qpb1-local-generators-20261023-a1/exact-001/manifest.json).

**Next discriminant:** define a finite-window phase observable with explicit
endpoint correction, visibility/closure floor and independent gain-error
budget. Test whether the local face–cell contrast has a stable measurable
response without relying on exact recurrence or silently assuming
`g1=g2`. Rate/metric selection remains a separately named source gap.
