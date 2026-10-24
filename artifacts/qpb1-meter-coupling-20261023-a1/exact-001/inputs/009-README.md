# Typed loop-history maps and action sufficiency v1.0

**RESULT — EXACT / CONDITIONAL.** We constructed composition-preserving maps and identified the extra inputs they need. The natural edge-chain projection to the tetrahedral discriminant is S4 equivariant but kills every closed graph cycle. An unframed native scalar winding receipt cannot map nontrivially into that discriminant under S4. A directed-edge frame repairs the latter map, while independent translation/modulation word channels produce finite Weyl holonomy. Neither finite record recovers unrestricted native action. A residue plus an unbounded integer carry and support does.

This is Discovery work at `ud-tetra/UD-Physics@92ef753389a3f2fe40f1423355d2c6f02169fbdc`, with mainline head verified unchanged at `ud-tetra/UD@957d443e25008632ab9d9328c162343b6a651ee7`. [SOURCES.json](SOURCES.json) binds eleven local dependencies; [SOURCE_ROWS.json](SOURCE_ROWS.json) preserves thirteen exact rows of ledger archive v0.85, whose inherited scientific_revision field is v0.43. The uploaded historical v0.39 ledger and CRL2 proposal match imported bytes and retain their separate status. Missing Genesis PNG is unused. No full attachment/corpus audit or new primitive source rule is claimed.

Physical score **UNSCORED**; physical promotion **0**. This report does not amend previous results, source ledgers, mainline or shared CURRENT.

## 1. Three different history domains

| History | Data and composition | What is source-bound or added |
| --- | --- | --- |
| Native closed Hodge orbit | Nonzero active state x, support a=||x||², integer winding n; compose loops at the same orbit/base state by adding n | Native A=d-dᵀ, active J=A/2, frequency2, O09 loop action I=pi*a*n |
| Integer graph walk | Ordered vertices in the K4 1-skeleton; concatenate compatible endpoints; signed edge chain p adds | New event/walker interpretation, not native chain-amplitude evolution |
| Finite Weyl word | Ordered translation/modulation letters; operator multiplication | Added finite algebra on C[D], not yet an event stream extracted from native trajectories |

Native x lies in active R14 inside the 15-register filled-tetrahedron carrier. The integer chain p lies in Z6 on graph edges. A Weyl basis label lies in `D=Lambda#/Lambda=Z4²`; its Hilbert carrier has complex dimension 16. Similar counts and a shared K4 incidence structure do not identify these spaces or histories.

The native one-form convention gives `I=pi*a*n` on a closed orbit and `S_native=A0 I`. Native dimensional units and physical action identification remain separate. Negative windings below belong to the mathematical group completion; an undriven positive-time trajectory traverses positive periods. Composition at changed support or changed carrier needs an explicit intervention/reset law and is not assumed here.

## 2. Natural additive projection: an endpoint class, not closed-loop holonomy

Use ascending oriented edges `(01,02,03,12,13,23)`, the Euclidean flow lattice `Lambda=ker B1∩Z6`, cut lattice `Gamma=im B1ᵀ∩Z6`, and the dual projection `PT Z6=Lambda#`. In the previous cycle basis L with Gram G, define

\[
\kappa(p)=[P_Tp]\in D,
\quad\delta(p)=G^{-1}L^Tp\pmod{\mathbb Z^3}.
\]

Choosing the previous generators `u=[G^-1 e1],v=[G^-1 e2]`, its Z4-coordinate matrix is

\[
K=\begin{pmatrix}1&2&1&1&0&3\\1&1&2&0&1&1\end{pmatrix},
\qquad \kappa(p)=Kp\pmod4.
\]

It is additive and S4 equivariant. Its kernel is exactly `Gamma+Lambda`: if `PTp∈Lambda`, subtract that integral flow from integral p to obtain an integral cut; the converse follows because PT kills cuts and fixes flows. Thus the quotient has index 16, as previously verified.

For every closed integer graph chain `B1p=0`, p already lies in Lambda, so **kappa(p)=0**. Two walks with the same endpoints differ by an integral cycle and have the same kappa. A single walk from i to j has class `delta_ij=kappa(e_ij)`; its twelve directed possibilities give all twelve order-four classes. The zero class occurs for closed walks; the three order-two classes require more general composite charge patterns. The image of single-walker histories therefore contains thirteen classes, despite the full chain map being surjective onto sixteen.

The representation `walk→T_(kappa(p))` preserves concatenation exactly, but returns identity on every closed walk. This construction supplies an **endpoint charge-coset tag**, not a nontrivial holonomy of graph circulation. The filled complex also has H1=0; graph cycles bounding faces and discriminant classes remain different objects.

All 4372 graph walks of lengths 0 through 6 were checked, including 1096 closed walks. The all-length statement follows from the kernel proof, not from extrapolating the finite check.

## 3. Native scalar winding and the missing frame

All 24 signed native simplex actions are orthogonal and commute with A and J. They preserve both support a and native orbit winding n. In contrast, the inherited action on D has fixed subgroup

\[
D^{S_4}=\{0\}.
\]

Consequently any S4-equivariant map into D that depends **only** on the scalar receipt `(a,n)` is zero. For an additive winding map it suffices to inspect the image of n=1: that image would have to be fixed. The same statement holds for D×D.

The scope matters. A map depending on extra state structure need not factor through `(a,n)`. However, a **continuous** D-valued map defined on all nonzero active states is constant for each n because `R14 minus{0}` is connected and D is discrete. Equivariance then forces that constant to zero. A sector restriction, discontinuous event boundary, state-derived frame or added readout can change the premises; it must be specified rather than assumed.

Nor does this prohibit scalar phase characters. The center mu4 has trivial S4 action, so all four maps `n→i^(kn)`, k modulo4, are symmetry compatible. They are choices of central character, not D-valued maps, and symmetry does not select one.

An explicit nontrivial **framed** map is

\[
F_e(n)=n\delta_e\in D,
\qquad F_{\pi e}(n)=\pi F_e(n).
\]

Here e is a supplied directed edge. All twelve delta_e have order4, so each map has kernel `4Z`. It preserves winding composition; covariance holds when the frame is transformed with the state. No independently selected physical frame or native edge-event extractor has been derived here.

## 4. Endpoint parity versus a path connection

The previous invariant quadratic parity readout is

\[
s(x)=e^{2\pi i\bar q(x)},\quad
\bar q(x)=0\ (x\in2D),\quad \bar q(x)=1/2\ (x\notin2D).
\]

It is **not a character**:

\[
s(x+y)=s(x)s(y)\,e^{2\pi i\,2b(x,y)}.
\]

The full 256-pair table contains 96 multiplicativity failures if that cocycle factor is omitted. An endpoint observable cannot silently be used as a multiplicative path holonomy. The three nonzero parity labels correspond to the three opposite-edge matchings; opposite edges have equal labels modulo2. This is an exact S4 quotient relation, not a physical particle identification.

For the triangle `0→1→2→0`, the endpoint class is zero and its endpoint sign is +1. Each directed edge has nonzero parity class and sign −1; their edgewise product is −1. These are different readouts, not inconsistent calculations.

There is a valid alternative **connection hypothesis**: assign link phase −1 to every oriented edge and multiply along the walk. It preserves concatenation, backtracking gives +1, and it is strictly S4 invariant. Every triangular face has curvature −1; the product over all four faces is +1. It is therefore a nonflat connection on the filled complex. It does not descend through face contraction to a flat/homotopy-invariant loop observable.

For a strictly label-invariant scalar link assignment, transitivity on directed edges makes every link phase zeta equal, and an edge-reversing permutation plus inverse-link consistency gives `zeta=zeta^-1`. The two possibilities are +1 and −1. This classifies that strict assignment ansatz, not all connections invariant up to gauge. Selecting the nonflat one and identifying its edge count with native action are additional assumptions. A nontrivial face holonomy does not contradict contractibility when the connection has curvature.

## 5. Two Weyl channels give a compositional finite loop operator

Retain `b` with generator matrix `(1/4)[[2,-1],[-1,2]]`, and choose k=1 or3 explicitly. Write

\[
W(c,x,y)=i^cT_xM_y,\qquad
W(c,x,y)W(d,u,v)
=W(c+d+4k b(y,u),x+u,y+v),
\]

with central c,d modulo4 and x,y,u,v in D. Bilinearity of b proves the cocycle identity and associativity. The inverse is `(-c+4k b(y,x),-x,-y)`. Word operators are multiplied in their written order; the rightmost operator acts first on a state. This is an algebraic word convention, with no selected physical timing law.

The closed two-channel commutator is

\[
M_yT_xM_y^{-1}T_x^{-1}
=e^{2\pi i k b(y,x)}I.
\]

For `x=u,y=v`, this is −i for k=1 and +i for k=3, while net translation and modulation are both zero. Reversing the commutator inverts the phase. Thus an ordered two-channel record carries nontrivial finite holonomy that the endpoint translation tag omits. This is a concrete compositional candidate, conditional on supplying the two event types.

A complete search over all 256 Z4-module endomorphisms of D finds only the four scalar maps commuting with S4. Hence if two proposed channels are equivariant linear adapters of **one same instantaneous D input**, they have the form `(alpha*x,beta*x)`. Their alternating commutator pairing is

\[
b(\beta x,\alpha y)-b(\beta y,\alpha x)=0.
\]

Such a channel image is isotropic: its elements commute, and it cannot supply the full noncommuting Weyl pair by this mechanism. This does not rule out stateful, nonlinear or separately controllable event records.

The audit checks both k choices, 8192 bilinear cocycle identities, 512 commutators, all 9362 words of length at most4 in four generators and their inverses, direct operator application on all sixteen basis states per word, and 28080 S4 word-covariance checks. All 4096 same-input scalar-channel commutator tests vanish. These are constructor checks, not separate-context or empirical review.

## 6. An action-sufficient lift with exact carry composition

For a fixed native orbit of positive support a, every winding has a unique Euclidean decomposition

\[
n=r+4m,\qquad r\in\{0,1,2,3\},\quad m\in\mathbb Z.
\]

A primitive fourth-root endpoint retains r. To retain native action, store also a and the integer carry m:

\[
\mathcal I=\pi a(r+4m),\qquad
\mathcal S_{\rm native}=\pi a(r+4m)\mathcal A_0.
\]

Composition is explicit:

\[
r_{12}=(r_1+r_2)\bmod4,\qquad
m_{12}=m_1+m_2+\left\lfloor\frac{r_1+r_2}{4}\right\rfloor.
\]

This handles negative windings as well. All 51 receipts across three rational supports and seventeen windings, and 867 same-support composition pairs, reconstruct action exactly. Source O09 supplies the action shape; the carry is a lossless implementation of its required integer lift, not a derived physical clock or charge spectrum.

A finite readout alone cannot recover unrestricted action at fixed a>0: the windings have infinitely many distinct values `pi*a*n`, while a finite codomain must identify two of them. In particular n and n+4 share every primitive mu4 character but differ by `4pi*a` in I. Support cannot be discarded either unless it is known independently or a declared normalized representative is used. The weighted action coefficient a*n itself is another sufficient statistic; the displayed `(a,r,m)` receipt preserves both phase residue and the source variables transparently, without a claim of unique or minimal storage.

This closes a mathematical information-loss issue for the stated orbit domain. It does not determine A0 in physical units, eta_A=A0/hbar, the electromagnetic constitutive factor or an electron preparation. G06/O14 normalization gates and Q287/Q288 candidate status remain unchanged. A word commutator phase has not been identified with this action integral.

## 7. Source scope, artifacts and next discriminant

The source imports are O09/O10/O11/O14, G06/G07, Q282/Q283/Q284/Q286/Q287/Q288 and Q339. They establish the declared native orbit action, unit and lifted-history requirements, with physical normalization still open. None of those inspected rows supplies a native two-channel discrete event extractor. No global absence theorem over UD's entire corpus is claimed.

Primary mathematical comparisons: Bacher–de la Harpe–Nagnibeda, *The lattice of integral flows and the lattice of integral cuts on a finite graph*, author preprint dated 1997-02-03, [§4 projection lemma and §6 complete graphs](https://www.unige.ch/~laharpe/articles/19BaHaNa3fev97.pdf); Prasad–Vemuri, *Inductive Algebras for Finite Heisenberg Groups*, [arXiv:0803.2921v1](https://arxiv.org/pdf/0803.2921), 2008-03-20, §§2,4. They provide conventional lattice/finite-algebra context, not native event rules or physical evidence. All consequential finite identities and scoped obstructions are derived or checked here.

Reproduce from repository root:

```bash
python3 experiments/qpb1-loop-history/audit.py --out /tmp/ud-loop-history
```

See [adapter contract](HISTORY_CONTRACT.md), [source manifest](SOURCES.json), [mathematical receipt](../../sessions/qpb1-loop-history-20261023-a1/mathematical_receipt.json), [candidate](../../candidates/qpb1-loop-history/candidate.json) and [immutable run](../../artifacts/qpb1-loop-history-20261023-a1/exact-001/manifest.json).

**Next discriminant:** construct an S4-covariant event rule using native edge amplitudes and their J-quadratures. Test whether its events supply distinct translation/modulation records, including zero-amplitude degeneracies and simultaneous events; preserve the action carry receipt. This would test a missing mechanism rather than select a physical normalization by analogy.
