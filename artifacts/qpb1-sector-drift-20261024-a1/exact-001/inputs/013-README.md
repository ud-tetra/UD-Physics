# Native quadrature events and recurrence holonomy v1.0

**RESULT — EXACT / CONDITIONAL.** A zero-crossing observer on native edge amplitudes and their J-quadratures produces an explicit S4-covariant two-letter Weyl record. It detects twelve of the fourteen active native dimensions. Its two event types are locked quadratures of the same oscillators, not independently controllable ports. For the stated simultaneous-event protocol, the full-recurrence phase is generically **+1**; nontrivial signs occur on special support/tie sets and are not stable on any open set of all native states. Mixed ties and vanishing amplitudes supply exact discontinuity witnesses. The robust nontrivial recurrence-bridge role is **PARKED**; the observer, visibility calculation and action-counter domain remain useful.

Discovery source base `ud-tetra/UD-Physics@68f54ac568b76a37594f981c4593898ea9778963`. Mainline head was verified unchanged at `ud-tetra/UD@957d443e25008632ab9d9328c162343b6a651ee7`. [SOURCES.json](SOURCES.json) binds eleven local dependencies; [SOURCE_ROWS.json](SOURCE_ROWS.json) preserves thirteen exact ledger rows. Archive v0.85 and inherited scientific_revision v0.43 remain separate. The supplied historical v0.39 ledger and CRL2 proposal hash-match their imports; neither supplies a new physical event law. Missing Genesis PNG is unused. Physical score **UNSCORED**, physical promotion **0**; no mainline/source-ledger/shared-CURRENT edits.

## 1. Native dynamics and explicitly added observer

Retain the filled-tetrahedron oriented carrier with unit Euclidean chain metric, `A=d-dᵀ`, active projector `P=-A²/4` of rank14 and `J=A/2`, `J²=-P`. A native active trajectory is

\[
x(s)=\cos\theta\,x_0+\sin\theta\,Jx_0,\qquad\theta=2s.
\]

Let E project onto the six edge registers, ordered `(01,02,03,12,13,23)`. Define observable quadratures

\[
q_e=x_e,\qquad p_e=(Jx)_e,\qquad
q'_e=2p_e,\quad p'_e=-2q_e.
\]

The symbol p here is a **native observed quadrature**, not automatically the new canonical momentum field of the preceding R12 field model. Each pair has constant radius `r_e²=q_e²+p_e²`. Writing initial values `(a_e,b_e)`, the observed functions are `q_e=a_e cos(theta)+b_e sin(theta)` and `p_e=-a_e sin(theta)+b_e cos(theta)`.

The **added observer hypothesis** is:

- At a transverse q_e=0 crossing emit `T_(epsilon delta_e)`, with `epsilon=sign(p_e)`.
- At a transverse p_e=0 crossing emit `M_(epsilon delta_e)`, with `epsilon=-sign(q_e)`.
- Suppress a pair that is identically zero. Every nonzero pair has exactly four events per native recurrence.

Here `delta_e=kappa(e)` are the previously derived order-four discriminant classes in `D=Z4²`. The native generator does not itself specify this threshold observer, the T/M labels, a finite quantum carrier or the physical implementation of their readout.

## 2. Exact timing, symmetry and simultaneous-event protocol

No sampled ODE, floating root finder or approximate trigonometric ordering is used. A clock direction is a ray proportional to `(cos(theta),sin(theta))`. For initial `(a,b)`, the positive-slope q crossing has ray `(b,-a)`; the negative-slope p crossing has ray `(a,b)`. Opposite rays give the other two events. Rational rays are ordered by their half-plane and exact cross products, and proportional rays are grouped as simultaneous.

All 24 signed simplex actions commute with A and J. They permute q and p with the same oriented-edge signs. A crossing sign and its oriented discriminant class therefore transform together, yielding S4 covariance. In the audit, transformed words agree at every batch prefix, as well as at the full recurrence.

**Protocol convention:** at a simultaneous batch, aggregate all translations and apply that translation first, then aggregate and apply all modulations. Within each type the letters commute. Chronological updates multiply the new operator on the left; the rightmost operator acts first on the state. The opposite uniform channel priority is a separately checked convention, not a source-derived timing law.

Mixed T/M ties can be noncommuting. For example, phasors `(1,0)` on edge01 and `(0,1)` on edge02 give a mixed batch whose two priorities differ by a primitive fourth-root central factor. Thus the protocol is well defined and covariant, but exact simultaneity does not determine a unique operator without an added rule. The two uniform priorities happen to give the same full-recurrence scalar in this model; their batch/prefix operators can differ.

Same-type simultaneous events are harmless for operator ordering. A mixed tie occurs when two active phasors are orthogonal: `a_e a_f+b_e b_f=0`. If the corresponding edges are disjoint their discriminant pairing vanishes and they commute; adjacent edges have primitive quarter-turn pairings.

## 3. Visibility: twelve active dimensions seen, two hidden

The edge subspace and its J image are orthogonal six-dimensional spaces. The invariant visible projector is

\[
P_{\rm vis}=E+JEJ^T,\qquad
P_{\rm hid}=P-P_{\rm vis},\qquad
\operatorname{rank}P_{\rm vis}=12,\quad\operatorname{rank}P_{\rm hid}=2.
\]

Both commute with A and all S4 actions; `E P_hid=E J P_hid=0`. The unit oriented top-cell register and its J quadrature span the invisible active plane. This is an observability kernel, not a Shannon-information-loss percentage.

Every initial pair `(q,p)∈R6×R6` is realizable by the native active state

\[
x_{\rm vis}=\iota q-J\iota p,
\qquad\|x_{\rm vis}\|^2=\|q\|^2+\|p\|^2,
\]

where iota embeds edges in the full chain carrier. Thus q and p can be prepared independently **initially**. Their subsequent events are constrained by the same quarter-cycle dynamics; they are not independent actuation channels.

Exact witnesses:

- A unit edge state has native support1; adding a unit top-cell state changes support to2 while leaving all observed edge events identical.
- Multiplying a nonzero visible state by2 preserves all event times, signs and finite letters while multiplying its native support/action by4.
- A pure unit top-cell state has native recurrence action pi and emits no edge events at all.

Hence edge events alone cannot reconstruct total native action or observe all active modes.

## 4. Full-recurrence formula and its generic collapse

Use the previous finite Weyl multiplication `W(c,x,y)=i^c T_x M_y`, with

\[
b_4(x,y)=4b(x,y)\pmod4,
\qquad W(c,x,y)W(d,u,v)
=W(c+d+k b_4(y,u),x+u,y+v),
\]

where the explicitly chosen faithful central character is k=1 or3. Every active edge produces opposite translation labels and opposite modulation labels, so net x and y vanish over one recurrence. The resulting operator is central.

Let S be the set of active edges and N its size. For either uniform simultaneous-event priority, the central quarter-turn exponent is

\[
c\equiv k\left[2N+
\sum_{\substack{e<f\in S\\a_ea_f+b_eb_f\ne0}}
2b_4(\delta_e,\delta_f)\right]\pmod4.
\]

A proof reduces the accumulated Weyl cocycle to its self-edge and unordered edge-pair terms. One edge's four crossings contribute2. For a pair, rotate the clock so the first phasor is on the positive q axis. The second phasor lies in one of four open quadrant ordering cells or on an axis. The signed cross-channel crossings contribute `+2 b4` or `-2 b4` when their dot product is nonzero; these agree modulo4. At orthogonality, uniform priority gives zero cross contribution. Collinear same-channel ties preserve the nonorthogonal result. This covers all relative directions; the rational direction checks below verify representatives and additional interior directions in every case.

If there are no mixed noncommuting ties, the expression simplifies to

\[
c=b_4\left(\sum_{e\in S}\delta_e,
                 \sum_{e\in S}\delta_e\right)\in\{0,2\}.
\]

Thus the recurrence gives only signs, despite primitive fourth-root coefficients occurring in intermediate words. More decisively, for **all six active edges** the sum of their classes is `(0,2)`, whose self-pairing is zero. The recurrence phase is **+1** whenever all six pairs are nonzero and no adjacent pair is orthogonal.

Those conditions define a dense open subset of the active carrier: their exceptions are a finite union of proper polynomial zero sets in the freely realizable q,p data. Consequently no nontrivial recurrence phase from this observer is stable on an open set of unrestricted native initial states. This is a scoped obstruction for this threshold encoding and protocol, not for every possible native phase observable or changed dynamics. The generic sign on sparse, support-restricted domains recovers the previous discriminant parity rule; it does not establish physical spin or action quantization.

## 5. Degeneracies and a positive stability certificate

**Mixed-tie challenge.** On edge01 take phasor `(1,0)` and on edge02 `(epsilon,1)`, with all other pairs zero. The full-period phase is −1 for either sign of nonzero epsilon, but +1 at epsilon=0 under either uniform priority. The exact arithmetic fixtures use epsilon `-1/1000,0,+1/1000`. The all-nonzero-epsilon result follows from the formula, not a numerical extrapolation.

**Sparse-state challenge.** Begin with a unit edge01 state and activate its disjoint edge23 with arbitrarily small positive amplitude epsilon. The phase changes from −1 at epsilon0 to +1 for every epsilon>0, while the native support changes only from1 to `1+epsilon²`. This is a nonzero-state discontinuity, without a mixed tie. An absolute detector threshold would define another observer with an additional unselected scale.

**Identically zero pairs.** A zero phasor emits no events; any arbitrarily small nonzero phasor emits four. Treating every time of an identically zero signal as a crossing would be undefined. Suppression repairs definition but not continuity across activation.

A useful **EXACT / CONDITIONAL chamber certificate** remains. Take

\[
q=(1,2,3,4,5,6),\qquad p=(1,3,2,5,4,7).
\]

For any active-native state perturbation with Euclidean norm at most1/10, every observed phasor changes by at most1/10, because each `(x_e,(Jx)_e)` is an orthonormal two-coordinate projection. The reference minimum squared radius is2. Bound the change of each phasor dot product by

\[
\epsilon(U_e+U_f)+\epsilon^2,
\qquad U_e=|q_e|+|p_e|,\quad\epsilon=1/10.
\]

The smallest remaining absolute dot-product margin is `429/100>0`. Every edge therefore remains active and all dots remain nonzero. The full-recurrence phase stays +1 throughout this entire perturbation ball. Ordering can change only at commuting same-type events. This is a continuous perturbation certificate for a trivial phase, not a robust nontrivial bridge or a timing/noise guarantee for an apparatus.

## 6. Winding counts and action receipts

With N>0 fixed active edge pairs, a complete forward recurrence has exactly `4N` individual crossings, counting multiplicity even when events are simultaneous or their summed finite labels cancel. Over n complete forward recurrences,

\[
n=\frac{N_{\rm crossings}}{4N}.
\]

This gives a frame-independent native winding count on the declared visible subdomain, under perfect event detection and known N. N is unchanged along undriven native evolution and under S4. It is not a physical tick rate. Pure hidden-plane motion has N=0 and needs another observer. General drives, missed events, reverse-time operation or incomplete intervals require additional rules.

Retain the previously constructed action receipt `a,r,m`, where `n=r+4m`, `r∈{0,1,2,3}` and m is unbounded. Then `I=pi*a*(r+4m)` and `S_native=A0 I`. The event count can supply n on this domain; total support a still requires information beyond the edge-event record, including the hidden plane. The audit checks945 event-count/carry reconstructions over189 preparations and n0..4. No new physical A0/hbar normalization is selected.

## 7. Evidence and next discriminant

Reproduce from repository root:

```bash
python3 experiments/qpb1-native-events/audit.py --out /tmp/ud-native-events
```

Exact constructor checks:11 source hashes,13 literal ledger rows,24 native symmetries and projector identities,189 support/phase fixtures across every nonempty edge support,2304 crossings,1208 batches,4536 full-word and batch-prefix covariance checks,3840 two-edge direction fixtures including480 orthogonal cases, both primitive central characters,945 action-carry checks, and the rational perturbation certificate. General visibility, recurrence and dense-open claims are justified above; no separate LLM or empirical review is claimed. Pre-capture self-review corrected chamber-output variable reuse and strengthened prefix covariance; the corrected audit was rerun successfully before capture.

See [observer contract](EVENT_CONTRACT.md), [receipt](../../sessions/qpb1-native-events-20261023-a1/mathematical_receipt.json), [candidate](../../candidates/qpb1-native-events/candidate.json) and [immutable run](../../artifacts/qpb1-native-events-20261023-a1/exact-001/manifest.json).

**Next discriminant:** construct a carrier-complete continuous phase/action readout, including the hidden cell/surface plane. Check its gauge transformation and loop normalization, separating geometric phase from native global Hodge rotation and leaving any physical scale choice explicit. Reopen this event route for robust nontrivial recurrence only after a separately justified observer regularization or changed law passes an open-domain stability test.
