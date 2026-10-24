# Balanced local meter and projective loading cancellation v1.0

**RESULT — EXACT / CONDITIONAL.** An added, matched 15-register classical
meter can exchange and dissipate storage while preserving the unloaded
carrier's projective trajectory. The finite-window phase is therefore
unchanged whenever the meter signal is nonzero. This replaces the previous
unloaded-meter assumption with an explicit dynamical model, not a built
instrument. Differential mismatch, analog calibration, clock realization
and source selection remain open engineering/physical questions.

Base `ud-tetra/UD-Physics@0abea764505989dde38fe0906d0d32c53d76b93c`;
2026-10-23, America/Chicago. [SOURCES.json](SOURCES.json) pins 24 dependencies;
[SOURCE_ROWS.json](SOURCE_ROWS.json) preserves 13 literal archive-v0.85 rows
and scientific revision v0.43. Fresh supplied v0.39/governance bytes match
their committed imports; historical G06 is not restored as a physical
coefficient. Genesis PNG unavailable, unused. Score **UNSCORED**, physical
promotion **0**. No mainline, source-ledger or shared CURRENT change.

## 1. Proposed finite local meter

Retain C=R^15 for the filled tetrahedron, ascending simplex orientations,
Euclidean metric, J=A/2, active projector P and the three local skew
generators K_k. The plant generator is the parent's
G(s)=sum g_k(s)K_k, with g*=(1,1,3/2) and independent absolute errors
<=1/100. The native parameter s is not physical seconds.

Add another copy m in C, coupled at corresponding simplex registers:

\[
\boxed{x'=G(s)x-\kappa m,\qquad
m'=G(s)m+\kappa x-\gamma m},\qquad \kappa,\gamma>0.
\]

This is a **proposed classical state-space law**. Each copy uses the same
28 undirected Hasse-incidence pairs; 15 corresponding-register ports join
the copies. There are 30 real storage coordinates (28 active for active
seeds), 71 off-diagonal pairs and 15 local damping terms. The meter does
not compress the required active information into edge-only stocks.

For S=(||x||^2+||m||^2)/2, balanced port terms give

\[
S'=-\gamma\|m\|^2\le0.
\]

Locally the port contribution to (x_sigma^2)' is -2kappa*x_sigma*m_sigma,
and to (m_sigma^2)' its positive opposite, followed by meter loss
-2gamma*m_sigma^2. These terms can reverse direction; only total storage
is guaranteed nonincreasing. This is balanced two-way energy exchange;
electrical reciprocity, transducer hardware and thermal noise are not
inferred from skew matrix entries. Storage units have not been mapped to
joules. Gain control keeps G skew but has no established physical cost.

## 2. Exact factorization and phase cancellation

Let U'=G(s)U, U(0)=I, seed v active and m(0)=0. The exact solution has

\[
x(s)=a(s)U(s)v,\quad m(s)=b(s)U(s)v,\qquad
a'=-\kappa b,\quad b'=\kappa a-\gamma b,
\quad (a(0),b(0))=(1,0).
\]

Direct substitution proves this for every seed and every common G(s),
including time-varying gains. Equality of the two generators is essential;
commutation at different times is unnecessary for this factorization.
The parent's sector structure is retained when applying its phase bound.

Whenever a,b are positive, normalizing either copy gives the unloaded unit
state Uv/||v|| exactly. The plant loses amplitude and the meter acquires an
attenuated signal; this is not two unloaded, unit-gain copies. Such a
duplicate from a zero meter would double positive storage without a source.
No quantum-state copying or measurement theorem is proposed.

There is a wider exact invariance. If ports/damping remain scalar and the
meter generator is G(s)+omega_c(s)J, a,b become complex scalars satisfying

\[
a'=-\kappa b,\qquad b'=\kappa a+(i\omega_c-\gamma)b.
\]

Complex multiplication means (Re b)I+(Im b)J on the active space. Provided
b is nonzero at each sample, m and Uv are the same projective ray. Scalar
time-dependent port/damping changes and a common J detuning therefore need
not be small to preserve this ray; they still require nonzero usable signal.
This does not cover differential sector or channel mismatch.

For any nonzero complex factors beta_j, the unnormalized overlap polygon

\[
B=z_{0M}\prod_{j=0}^{M-1}\overline{z_{j,j+1}}
\]

changes by exactly the positive factor product_j |beta_j|^2 under
y_j->beta_j y_j. Its direction, normalized visibilities and finite-window
phase are unchanged. Exact acquisition-frame cancellation is geometric;
requantizing transformed coordinates can produce a different bounded
digitization error, as already noted in the acquisition contract.

## 3. Warmup and a nonzero signal bound

Choose illustrative controls kappa=1/4, gamma=1 and one native unit of
warmup. They were selected after exposure to the existing phase contract;
they are neither UD-selected constants nor optimal hardware values.
For tau measured from meter initialization,

\[
\begin{aligned}
a(\tau)&=e^{-\tau/2}\left[\cosh(\sqrt3\tau/4)
 +\frac2{\sqrt3}\sinh(\sqrt3\tau/4)\right],\\
b(\tau)&=\frac1{\sqrt3}e^{-\tau/2}\sinh(\sqrt3\tau/4).
\end{aligned}
\]

Measure over tau in [1,1+T], with the parent's |T-2pi|<=1/100,
128 links and maximum native gap <=T_plus/128. Write
H=1+T_plus=5107/700, so 7<H<15/2. Both a,b are positive for tau>0.

A rational lower bound is **b(tau)>1/8** throughout [1,H]. To verify it,
b/a stays below its positive fixed point 2-sqrt3<1/3, so a>=exp(-tau/12).
Also b(tau)>=a(tau)(1-exp(-tau))/4. At tau=1, e>8/3 and exp(-1/12)>11/12
give b(1)>55/384. At H use

\[
e^{-5/8}\ge1-5/8+(5/8)^2/2-(5/8)^3/6=1627/3072,
\]

and 1-exp(-H)>127/128 to give b(H)>206629/1572864>1/8.
The displayed b has a single maximum: its derivative changes sign when
tanh(sqrt3*tau/4)=sqrt3/2. Thus its minimum on [1,H] is at an endpoint.
At initialization b(0)=0: an empty meter supplies no initial phase.

The nominal calibrated readout is z=m/b(tau), with inverse gain <8.
Seed norm [9/10,11/10] maps to the old amplitude range exactly in the
matched model. Calibration of b is an assumed observation operation;
physical amplification, digitizer power and probe loading are not free.
The nominal meter has a specified nonzero signal, not an overlap oracle.

Seed preparation is imposed before warmup, in the parent's radius-1/10
ball. U(1) rotates that ball and preserves all sector fractions; hence the
parent's phase proof still applies during the subsequent window. The
window-start reference is co-rotated, rather than assumed equal to the
original coordinate vector. The same-seed baseline remains
Q0=exp(-2pi*i*r_hidden), not -1 for every seed in the ball.

## 4. Finite mismatch, readout and initialization certificate

Allow local nonuniform but balanced diagonal port/damping matrices:

\[
x'=Gx-Km,\qquad m'=(G+E)m+Kx-Dm.
\]

Here E=sum Delta_g_k K_k is skew, |Delta_g_k|<=eps_g;
K=diag((1/4)(1+c_sigma)), |c_sigma|<=eps_c;
D=diag(1+d_sigma), |d_sigma|<=eps_d<1. These choices retain the total
energy inequality even when they break S4 symmetry. Extra readout loss
must fit D or another explicitly bounded dissipative perturbation; it is
not automatically absent because it was omitted from an instrument sketch.

In the positive Euclidean product norm the actual and nominal propagators
are contractions, and

\[
\|L-L_0\|\le\delta:=2\epsilon_g+\tfrac14\epsilon_c+\epsilon_d.
\]

Variation of constants therefore gives, for an initial meter residual
||m(0)||<=e0 and seed norm <=s_max=11/10,

\[
\|W(\tau)-W_0(\tau)\|\le e_0+\tau\delta s_{\max}.
\]

This covers arbitrary residual directions, channel patterns and bounded
time dependence in the stated family. Harmonic leakage from nonuniform
ports is included in the full norm and then removed by the active readout.
Dividing meter values by nominal b multiplies this bound by at most 8.

For a per-channel gain error <=eps_a, native sampling offset <=j and
combined calibrated additive/readout-reference error <=nu, put
S_max=s_max+e0. The actual combined norm is <=S_max. A uniform bound
||m'||<=5S_max holds for the profiles below on the small timing-extended
domain (since ||G||<=151/50 and all declared perturbations are tiny).
Thus every calibrated raw register differs from the nominal unloaded
common-instant sample by at most

\[
\boxed{r_{\rm raw}\le8e_0+8H\delta s_{\max}
 +8S_{\max}\epsilon_a+8S_{\max}(1+\epsilon_a)5j+\nu}.
\]

This is deterministic and makes no independence or averaging assumption.
Allocate each of its five terms r/5:

\[
e_0=r/40,\quad\delta=r/(40Hs_{\max}),\quad
\epsilon_a=r/(40S_{\max}),\quad
j=r/[200S_{\max}(1+\epsilon_a)],\quad\nu=r/5.
\]

For example eps_g=delta/6, eps_c=4delta/3 and eps_d=delta/3 realize the
operator allocation. The exact fractions are in
[METER_CONTRACT.json](METER_CONTRACT.json) and captured tolerances.json.

| Inherited profile | Combined r | Sufficient operator delta | Sufficient channel jitter, native units | Phase bound |
| --- | --- | --- | --- | --- |
| STRICT_A, 26 bits | 9/320000000 | <8.762e-11 | <1.279e-10 | <1/500 rad |
| REALLOCATED_B, 21 bits | 9/80000000 | <3.505e-10 | <5.114e-10 | <1/250 rad |

Displayed decimal limits are rounded upward for readability; the operative
allowed maxima are the smaller exact fractions, not the rounded decimals.
These **very tight sufficient tolerances are not measured feasibility or
necessary limits**. The proof overbounds harmless scalar loading along with
harmful transverse errors. A direct projective-phase analysis could be much
less restrictive. In particular the numerical 0.01 hidden-detuning control
breaks exact cancellation yet remains inside the 0.004-rad phase screen.

Feeding r_raw<=r into the pinned acquisition normalization/quantization
proof preserves its exact integer gates, endpoint visibility >0.99, link
visibility >0.999 and |Qhat-1|>1.7. STRICT_A satisfies the earlier 10^-6
overlap condition. REALLOCATED_B remains the explicit amended allocation,
not a strict-parent pass. No new ADC bit-depth optimization is claimed.

## 5. Finite reset, reference retention and accounting

The proof permits e0>0, so it does not require an exactly empty meter. One
conditional reset protocol uses 64 native units with damping D>=I/2.
Suppose combined storage amplitude at reset start is <=s_max and the
off-state port norm is <=ell=e0/(4s_max). Balanced coupling keeps the full
state bounded; comparison of the meter norm gives

\[
\|m(64)\|\le s_{\max}e^{-32}+2\ell s_{\max}
 <s_{\max}/2^{32}+e_0/2<e_0
\]

for either declared profile. e>2 and the final rational inequalities are
checked exactly. Port gating, the initial reset bound, residual-preserving
seed preparation and damping are controlled assumptions, not a native reset
selection law. Reset is dissipative; no joule or entropy/erasure-cost claim
follows without a physical unit and bath model.

After initialization and one-unit warmup, keep the prior finite classical
reference records and exact integer phase accumulator through the window.
This adds 15 analog meter coordinates to the plant, on top of the prior
digital buffers and arithmetic workspace. Digital storage remains bit-exact
by default; bounded decoded-reference errors can instead consume nu. No
unbounded trajectory or coherent copy of an unknown quantum state is stored.
Commit phase, gate status and calibration metadata before reusing buffers.

## 6. Verification, negative controls and remaining gap

Reproduce with standard-library Python from repository root:

```bash
python3 experiments/qpb1-meter-coupling/audit.py --out /tmp/ud-meter-coupling
```

**EXACT constructor checks:** 24 pinned hashes, 13 literal ledger rows,
30-state energy identity, 28-active rank, 71-pair count, matched and common-J
intertwining, passivity with nonuniform ports/damping, all 24 signed S4
actions at nominal scalar ports, 50 rational complex-gain overlap polygons,
signal lower bounds, reset and five-way tolerance fractions. The displayed
proofs establish the general conditional statements; fixtures alone do not.

**NUMERICAL constructor checks:** 120 windows cover two bit profiles, five
seed preparations, three gain triples and four error/window profiles.
Closed binary64 sector solutions include bounded initial residual, meter
generator/port/damping errors, alternating readout gains, asynchronous
channel sampling and additive errors. They feed exact nearest-even
digitization and the inherited exact integer estimator. Worst displayed
phase error is about0.000365466 rad. Raw-error comparisons allow5e-13 and
phase comparisons5e-11 numerical tolerance; no interval or empirical result
is asserted. One captured integer witness replays exactly without analog
trajectory evaluation.

A separately implemented full 30-state RK4 solution agrees with the matched
scalar formula at tau=3: maximum coordinate differences about9.411e-12
(2048steps) and5.886e-13 (4096steps), under a2e-10 display tolerance. This is
another constructor calculation, not independent review or a certified ODE
error enclosure. Nonuniform full-state perturbations are covered by the
analytic norm proof; the finite numerical tolerance campaign uses a
structured commuting subset.

Negative controls retain the empty-meter startup failure and differential
hidden-sector detuning. At Delta_g_hidden=0.01, the ideal unquantized
finite-window phase changes by about0.000366517 rad; at0.05 it exceeds the
0.004-rad screen. These exposed development probes demonstrate sensitivity,
not sharp thresholds or the necessity of the conservative small-error box.

This is a finite passive **model** with an explicit readout contract.
Matching G, physical signed-variable encoding, classical sensors and their
loads/noise, reference storage, gate control, seed preparation, clock/action
units and native selection of the engineered meter remain OPEN. No physical
U(1), spin, eta_A value or spacetime mechanism is established.

See [candidate](../../candidates/qpb1-meter-coupling/candidate.json),
[receipt](../../sessions/qpb1-meter-coupling-20261023-a1/mathematical_receipt.json),
and [immutable run](../../artifacts/qpb1-meter-coupling-20261023-a1/exact-001/manifest.json).

**Next discriminant:** bound differential meter errors directly in the
projective phase readout, separating exactly harmless scalar/common-J
directions. Determine whether useful matching/calibration tolerances can
replace the conservative full-amplitude box before proposing hardware.
