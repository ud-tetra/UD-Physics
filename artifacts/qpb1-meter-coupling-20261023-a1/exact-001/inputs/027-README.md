# Finite-window phase and snapshot acquisition contract v1.0

**RESULT — EXACT / CONDITIONAL.** A gauge-invariant finite-window readout is
defined by endpoint and neighboring-state overlaps. It requires no exact
return and no subtraction of assumed nominal rates. Under the explicit
preparation, commuting gain, timing and acquisition budgets below, **129
normalized snapshots** give phase error below **1/250 rad**, observed endpoint
visibility above **99/100**, and every observed adjacent visibility above
**999/1000**. The resulting phase remains separated from +1 across the entire
declared preparation ball. Physical snapshot/overlap acquisition remains a
hypothesis, with no measured apparatus or noise budget established.

Source base `ud-tetra/UD-Physics@e9dc0e074af561a8e9e309f72f2b6b365a7553c8`;
recorded 2026-10-23 (America/Chicago). [SOURCES.json](SOURCES.json) pins eighteen
dependencies and the supplied ledger/governance comparisons. Historical v0.39
does not replace archive v0.85 and its inherited scientific_revision v0.43;
[SOURCE_ROWS.json](SOURCE_ROWS.json) preserves thirteen literal rows. Physics
placeholders and missing Genesis PNG supply no input law. Physical score
**UNSCORED**, promotion **0**; no mainline/source-ledger/shared-CURRENT changes.

## 1. Objects, retained dynamics and an ordinary baseline

Use the same filled tetrahedron, real 15-register chain carrier, ascending
orientations, Euclidean metric and signed S4 action as the previous audits.
On the active space `E=im P`, rank14, retain `J=A/2`, `J^2=-I_E`, and the
three orthogonal J-invariant projectors P1,P2,P3 of ranks6,6,2. Here
`P1+P2=Pv`, `P3=Ph`, including the formerly edge-hidden cell/surface plane.

For nonzero active x let y=x/||x||. Define the Hermitian pairing, conjugate
linear in its first argument and linear in its second,

\[
h_J(u,v)=\langle u,v\rangle+i\langle Ju,v\rangle.
\]

It satisfies `h_J(u,e^(J chi)v)=e^(i chi)h_J(u,v)` and is invariant under the
signed S4 action. Retain the normalized connection

\[
\alpha=\langle Jy,dy\rangle=\langle Jx,dx\rangle/\|x\|^2.
\]

This uses the existing ordinary U(1) ray-quotient hypothesis; it does not
derive a physical gauge principle. Samuel–Bhandari's 1988 primary paper is
the standard noncyclic/nonorthogonal phase-comparison baseline (publisher
abstract consulted; DOI in SOURCES.json). The construction and bounds here
are derived on the declared UD carrier, not a novel quantum phase principle.

The local gain family is

\[
x'=G(s)x,\qquad G(s)=\sum_{k=1}^3g_k(s)K_k
=2J\sum_kg_k(s)P_k.
\]

Constant gains recover the previous task. Bounded piecewise-continuous
time-dependent gains are an explicitly allowed extension for drift testing.
All K_k commute, so sector fractions `r_k=||P_k y||^2` remain constant and
sector phase advances are exactly `lambda_k=2 integral g_k ds`. Norm and
sector support are conserved; a time-dependent quadratic energy need not
be conserved. No arbitrary mode-mixing perturbation is included.

## 2. Continuous endpoint correction and its visibility gate

For any finite window [0,T], define

\[
z=h_J(y(0),y(T)),\quad V=|z|,\quad
\Lambda=\int_0^T\alpha,\quad
Z=z\,e^{-i\Lambda},\qquad Q=Z/|Z|\quad(V>0).
\]

Under an arbitrary differentiable phase choice `y(s)->e^(J chi(s))y(s)`,
z gains the factor `exp(i(chi(T)-chi(0)))` and Lambda gains that endpoint
difference. Z, V and the defined unit phase Q are gauge invariant. At a
ray return, `z=exp(i chi_end)` and Q equals the previous endpoint-corrected
holonomy. At general endpoints it is a finite open-path phase comparison.
The metric ray-closure distance is

\[
\min_\chi\|y(T)-e^{J\chi}y(0)\|=\sqrt{2(1-V)}.
\]

Nonzero endpoint overlap replaces an exact-return requirement. It cannot
be dropped: balanced visible/hidden support at reference gains below has
`z=0` at T=pi, so phase is undefined. For that same balanced trajectory,
`Z=cos(T/2)`; its unit phase changes across this zero. No zero-visibility
phase is silently assigned.

On the three-sector family,

\[
z=\sum_kr_ke^{i\lambda_k},\quad
\Lambda=\sum_kr_k\lambda_k,\quad
\boxed{Z=\sum_kr_ke^{i(\lambda_k-\sum_jr_j\lambda_j)}}.
\]

These formulas include all active dimensions, arbitrary within-sector
directions and unequal visible rates. A common addition to all lambda_k
cancels exactly. The original undetuned law has Q=1 at every window; the
new readout does not manufacture nontrivial phase from native global rotation.

**Acquisition issue.** The displayed Lambda must be the actual connection
integral or an independently controlled estimate. Assuming the nominal
value is insufficient. For a common gain error c at T=2pi, the endpoint
phase shifts by `4pi*c`; actual Lambda cancels it, while nominal-only
subtraction leaves that first-order error. At c=1/100 it is about0.12566rad.
The snapshot protocol below computes the correction from overlaps instead.

## 3. A finite-snapshot estimator with exact discrete gauge invariance

Take M+1 normalized active snapshots y_j in chronological order, including
both endpoints. Measure or compute complex overlaps

\[
z_{0M}=h_J(y_0,y_M),\qquad z_j=h_J(y_j,y_{j+1}).
\]

For all overlaps nonzero, define

\[
\boxed{Q_M=\frac{z_{0M}}{|z_{0M}|}
\prod_{j=0}^{M-1}\overline{\left(\frac{z_j}{|z_j|}\right)}}.
\]

Every snapshot can have its own phase chi_j. The endpoint factor gains
`exp(i(chi_M-chi_0))`; the product of conjugated link factors gains its
inverse. Thus the discrete estimator is exactly gauge invariant, with
no phase unwrapping, rate values or continuous integral needed as inputs.
Equivalently it is the unit phase of
`z_0M product conjugate(z_j)`, which the audit checks with exact rational
complex arithmetic. Normalizing factors avoids a long product of small
magnitudes in implementation.

The acquisition contract requires full-carrier normalized state/overlap
access, including hidden-plane information, and a consistent J comparison
frame. The real channels are `<y_j,y_(j+1)>` and `<J y_j,y_(j+1)>`, with
the same two endpoint channels. These are declared observations, not an
identified physical interferometer. A streaming implementation retains the
initial reference, previous/current state and running phasor; it need not
retain an unbounded trajectory. Norm calibration and coherent reference
retention are real requirements, not supplied by edge events alone.

For observed overlaps hat(z), use their unit factors only if

\[
|\widehat z_{0M}|>99/100,\qquad |\widehat z_j|>999/1000
\quad\hbox{for every link}.
\]

Otherwise report `LOW_VISIBILITY` with no phase. Error bounds below are
absolute errors of normalized complex overlaps, not percentages of unknown
signals. Bounds are deterministic; no statistical independence is assumed.
Under a change of comparison frame, overlap estimates must transform with
their respective endpoint phase factors; their absolute error bounds then
remain unchanged.

## 4. Continuous preparation/rate/timing certificate

Set reference gains `g*=(1,1,3/2)` and nominal window `T0=2pi`. This window
is chosen using the already exposed reference candidate; it is not a blind
prediction. Actual rates and the actual endpoint need not recur there.

Let `y*=(e01+h)/sqrt(2)`, where h is the unit oriented top-cell register.
For every active perturbation delta with `||delta||<=rho=1/10`, use the ray
of `y*+delta`. Its hidden support fraction obeys the retained norm estimate

\[
|r_3-1/2|\le\frac{2\rho+\rho^2}{2(1-\rho)^2}=7/54,
\quad r_3\in[10/27,17/27]\subset[1/3,2/3].
\]

At the exact reference window all three reference endpoint phases agree
modulo2pi, and the phase for this **same preparation** is

\[
Q_0=e^{-2\pi i r_3},\qquad |Q_0-1|\ge\sqrt3.
\]

In particular Q0=-1 at the central preparation; it is not exactly -1
throughout the ball. Define the following illustrative development budget:

| Quantity | Declared bound |
| --- | --- |
| Preparation displacement rho | 1/10 in original active Euclidean norm |
| Each absolute gain error | `|g_k(s)-g_k*|<=epsilon=1/100`, independently |
| Total window error | `|T-2pi|<=h=1/100` in native parameter units |
| Sampling | M=128 links; maximum native gap <=T_plus/M |
| Endpoint overlap error | `|hat(z_0M)-z_0M|<=zeta_e=1/1000` |
| Each link overlap error | `|hat(z_j)-z_j|<=zeta_l=1/1000000` |

These constants are protocol controls, not theory constants or measured
hardware tolerances. Gains are absolute native coefficient errors; the
timing bound is not physical seconds. Uniform sampling over actual T
satisfies the maximum-gap condition, but that condition must be established
for an acquisition clock.

Write `delta_k=lambda_k-lambda_k*`. The half-range of these phase errors is
bounded by

\[
d=\tfrac12(\max\delta_k-\min\delta_k)
\le\tfrac h2+2\epsilon T
<D=\frac{2291}{17500},\quad
T\le T_+=\frac{44}{7}+\frac1{100}=\frac{4407}{700}.
\]

This uses pi<22/7. An elementary exact justification is
`integral_0^1 x^4(1-x)^4/(1+x^2) dx=22/7-pi>0`, obtained by polynomial
division and `4 arctan(1)=pi`.

Let `e_k=delta_k-sum r_j delta_j`, so `sum r_k e_k=0`. A variable confined
to an interval of width2d has variance at most d^2: subtract the interval
midpoint, then subtract the squared mean. Consequently

\[
\sum r_ke_k^2\le d^2,\quad |e_k|\le2d,\quad
\sum r_k|e_k|^3\le2d^3.
\]

At the chosen reference window, `Z=Q0 W`, with `W=sum r_k exp(i e_k)`.
The elementary Taylor remainder bounds
`|exp(it)-1-it|<=t^2/2`, `cos(t)>=1-t^2/2`, and
`|sin(t)-t|<=|t|^3/6` give

\[
|W-1|\le d^2/2,\quad \Re W\ge1-d^2/2,\quad
|\Im W|\le d^3/3.
\]

For positive real part, absolute angle is at most absolute imaginary/real
ratio. Hence the actual endpoint visibility and circular phase error obey

\[
V\ge v=1-D^2/2=\frac{607251319}{612500000},\qquad
\operatorname{dist}_{S^1}(Q,Q_0)\le b_g=\frac{D^3}{3v}.
\]

The quadratic complex-error and cubic phase-error estimates apply at this
nominal reference-return window. They are not universal cubic protection
for arbitrary windows, noncommuting perturbations or changing metrics.

## 5. Sampling and acquisition error complete the bound

Throughout the gain box, the maximum simultaneous gain spread is
`sigma=13/25`. On a step of length Delta_s, the half-range of phase advances
is at most `sigma*Delta_s`. Apply the same centered-moment argument to that
step, now comparing its overlap phase to the actual local connection integral.
Set

\[
d_\ell=\sigma T_+/M=\frac{57291}{2240000},\quad
v_\ell=1-d_\ell^2/2,\quad
b_s=\frac{M d_\ell^3}{3v_\ell}.
\]

All true link visibilities are at least v_l. Summing local circular phase
errors gives `dist(Q_M,Q)<=b_s`. This holds for the bounded commuting drift
family as well as constant errors; it does not require g1=g2. With nonuniform
sampling the displayed conservative sum is still valid when every gap is
at most T_plus/M and there are M links.

If a complex z has magnitude at least v and absolute error at most zeta<v,
rotate it to the positive real axis. The estimate has real part at least
v-zeta and imaginary error at most zeta. Thus its phase error is at most
`zeta/(v-zeta)` and its magnitude at least v-zeta. Applying this to all
overlaps yields

\[
b_a=\frac{\zeta_e}{v-\zeta_e}
 +\frac{M\zeta_\ell}{v_\ell-\zeta_\ell},\qquad
\boxed{\operatorname{dist}_{S^1}(\widehat Q_M,Q_0)
\le b_g+b_s+b_a<1/250\ \mathrm{rad}}.
\]

Here dist is the absolute shortest angular separation, not chord length.
All budget comparisons are evaluated with exact fractions in audit.py.
Decimal upper bounds below are for readability, rounded upward:

| Contribution | Upper bound, rad |
| --- | ---: |
| Independent gains and endpoint timing b_g | 0.000755 |
| Finite sampling b_s | 0.000715 |
| Endpoint/link acquisition b_a | 0.001138 |

Their exact sum is about0.00260614rad, below the declared0.004rad certificate.
Also `v-zeta_e>99/100` and `v_l-zeta_l>999/1000`, so every allowed case
passes both visibility gates. The ray-closure distance is at most D for
the actual noiseless endpoint; an exact return is unnecessary.

Since unit-circle chord separation is at most its circular angular error,

\[
|\widehat Q_M-1|\ge\sqrt3-1/250>17/10.
\]

Thus nontriviality survives the **joint continuous** preparation, gain,
timing and acquisition domain under this contract. Exact -1 is not a
quantized or neighborhood-constant outcome. The old gain-error challenge
at newly selected, diverging exact recurrence times remains valid; this is
a different finite-window observable and protocol.

## 6. Verification, limitations and next discriminant

Reproduce from repository root, standard-library Python only:

```bash
python3 experiments/qpb1-finite-window/audit.py --out /tmp/ud-finite-window
```

**Exact constructor checks:** eighteen source hashes, thirteen literal ledger
rows, 5,625 rational centered-moment fixtures, 625 exact polygon gauge
fixtures, all24 signed S4 polygon checks and exact fraction evaluation of
the continuous certificate. The general arguments above establish the
continuous domain; finite fixtures alone would not.

**NUMERICAL constructor cross-checks:** 45 preparations, 27 gain choices and
three timing choices give3,645 constant cases. Eight endpoint-noise directions
and four radial/tangential link-noise directions give116,640 acquisition
cases. Sixteen bounded time-varying profiles independently form129 full
15-register snapshots and their overlaps. Binary64 comparisons use5e-12
tolerance; this is not interval arithmetic, independent review or an
experiment. Captured outputs include aggregate extrema, worst-case and
representative receipts; the full deterministic grid is regenerated by code.
The strengthened radial-link campaign supersedes the pre-capture tangential
noise-only campaign. Pre-capture self-review also aligned equality rejection
with the strict visibility contract and added both gate-boundary checks;
the final audit was rerun. No frozen artifact was overwritten. The analytic
certificate concerns the mathematical readout; a deployed estimator must
account for its arithmetic errors as well. The binary64 example is not a
formal floating-point implementation certificate.

Negative controls retain the exact zero-visibility phase failure, native
trivial-phase null and first-order nominal-correction error. The estimator
uses phase modulo2pi; it does not reconstruct lifted winding or raw native
action. Native action calibration, numerical eta_A, physical clock, rate
selection and an actual snapshot/overlap instrument remain OPEN. The
one-part-per-million link-overlap budget is an assumed measurement
requirement, not a demonstrated sensor capability. No support quantization,
spin, physical U(1) field or causal spacetime structure follows.

See [candidate](../../candidates/qpb1-finite-window/candidate.json),
[receipt](../../sessions/qpb1-finite-window-20261023-a1/mathematical_receipt.json),
[readout contract](READOUT_CONTRACT.json), and
[immutable run](../../artifacts/qpb1-finite-window-20261023-a1/exact-001/manifest.json).

**Next discriminant:** derive the snapshot/overlap acquisition map from local
register observations, including hidden-plane access, normalization,
reference memory and error propagation. Determine whether the assumed
endpoint/link accuracy can be achieved without ideal full-state access;
physical calibration and rate selection remain separate gaps.
