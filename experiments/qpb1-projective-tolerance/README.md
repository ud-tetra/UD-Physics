# Projective polygon phase and differential meter tolerance v1.0

**RESULT — EXACT / CONDITIONAL.** A direct variation bound for the complete
overlap polygon removes radial and common-phase errors exactly and avoids
charging the same state error independently at every link. On the proposed
balanced local meter, two explicit protocols allow differential operator
norms **1/1000000** (26bits) and **1/5000000** (21bits), respectively,
while keeping total phase error below **1/250 rad** and the existing
visibility gates. These are more than 11,413 and 570 times the previous
sufficient operator limits, measured against the shared 0.004-rad screen.

This is an **explicit protocol amendment**: dynamical mismatch now has its
own projective-phase budget. The previous raw-model-error and strict
overlap-accuracy requirements are not retained. Sensor accuracy, reference
calibration, native clock, preparation/reset and a physical instrument are
not thereby established.

Base `ud-tetra/UD-Physics@4aaf0a39d24328e27bc425e333e3612baea888a5`;
2026-10-24, America/Chicago. [SOURCES.json](SOURCES.json) pins 27 dependencies;
[SOURCE_ROWS.json](SOURCE_ROWS.json) preserves 13 literal archive-v0.85 rows
and scientific revision v0.43. Fresh uploaded historical v0.39/governance
bytes match their imports. G06 remains frozen; numerical physical eta_A is
not inferred. Missing Genesis PNG and placeholder sources supply no law.
Physical score **UNSCORED**, promotion **0**; no mainline/shared CURRENT edit.

## 1. Observable and the phase derivative

Use the inherited active complex Hilbert space E, complex dimension7/real
dimension14, on the filled-tetrahedron carrier, Euclidean chain metric,
ascending orientations, J=A/2 and
h(u,v)=<u,v>+i<Ju,v>. Multiplication by i is J. The exact local 14-row decoder
and Gaussian integer phase estimator are unchanged.

For M+1 unit vectors v_j with nonzero endpoint and neighboring overlaps,
define the phase direction of

\[
B=h(v_0,v_M)\prod_{j=0}^{M-1}\overline{h(v_j,v_{j+1})}.
\]

Let z_j=h(v_j,v_{j+1}), z_e=h(v_0,v_M). Along any differentiable deformation
of these samples, a continuous argument F of B obeys

\[
dF=\sum_{j=0}^{M}\Im h(g_j,dv_j),
\]

where complex division acts on vectors and

\[
\begin{aligned}
g_0&=v_1/z_0-v_M/z_e,\\
g_j&=v_{j+1}/z_j-v_{j-1}/\overline{z_{j-1}},\quad0<j<M,\\
g_M&=v_0/\overline{z_e}-v_{M-1}/\overline{z_{M-1}}.
\end{aligned}
\]

To derive this, differentiate each log overlap, using
d arg z=Im(dz/z), then collect both occurrences of each vertex. Since h is
conjugate-linear in its first slot, each collected difference has exactly
the conjugations displayed. Direct substitution gives

\[+h(v_j,g_j)=0.
\]

Thus both radial changes and vertical phase changes dv_j=a_j v_j+b_j Jv_j
with real a_j,b_j contribute zero. The formula is unchanged by independent
sample phase choices. This identifies the harmless directions without
claiming that all differential errors are harmless.

For unit u,v and z=h(u,v), the component of v/z perpendicular to u has norm

\[
q(|z|):=\frac{\sqrt{1-|z|^2}}{|z|}.
\]

Both terms in each g_j have the same component parallel to v_j, which
cancels. The triangle inequality therefore gives one q contribution for
each incident overlap. If ||dv_j/dt||<=chi along a deformation, with
endpoint visibility >=a_e and all link visibilities >=a_l, then

\[
\boxed{|F(1)-F(0)|\le2\chi\,[q(a_e)+M q(a_l)]}.
\]

More generally integrate the corresponding variable speeds and q values.
The circular phase distance is at most this continuous-argument bound;
no branch-cut or lifted winding claim is needed. Nonzero overlaps along
the entire deformation are a required hypothesis.

## 2. Bounded sample errors give an explicit homotopy

Let unloaded raw active states u_j have common norm s in [s_min,s_max],
s_min=9/10, s_max=11/10. Allow an independent phase choice at each sample.
Suppose calibrated active meter samples equal these states plus errors e_j,
with ||e_j||<=B<s_min. Use

\[
v_j(t)=\frac{u_j+t e_j}{\|u_j+t e_j\|},\qquad0\le t\le1.
\]

The normalization derivative is a real orthogonal projection divided by
the raw norm. Consequently

\[
\|v'_j(t)\|\le\chi:=\frac{B}{s_{\min}-B},\qquad
\|v_j(t)-u_j/s\|\le2B/s_{\min}.
\]

Complex Cauchy-Schwarz bounds overlap change by the sum of the two unit
state errors. From the parent's endpoint/link lower bounds v,v_l it follows
throughout the homotopy that

\[
a_e=v-4B/s_{\min},\qquad a_l=v_\ell-4B/s_{\min}.
\]

These are conservative lower bounds, not equality predictions. They remain
positive in both selected profiles. This proof covers arbitrary sample
error directions; it is not restricted to the structured numerical probes.

For exact evaluation, avoid numerical square roots. For any chosen rational
c>0,

\[
q(a)\le\overline q_c(a):=\frac{1-a^2+c^2}{2ca},
\]

because (sqrt(1-a^2)-c)^2>=0. Use c_e=3/20 and c_l=1/25. The exact rational
meter phase allowance is

\[
b_m=2\chi\,[\overline q_{3/20}(a_e)+128\overline q_{1/25}(a_l)].
\]

## 3. Separating common meter motion from differential error

Retain the previous proposed 30-state balanced meter. Choose a declared
common reference law

\[
x'=Gx-\kappa_c m,\qquad
m'=(G+2cJ)m+\kappa_c x-\gamma_c m,
\]

with |c(s)|<=1/1000,
kappa_c=(1/4)(1+k_c), |k_c(s)|<=1/1000, and
gamma_c=1+d_c, |d_c(s)|<=1/1000. These common controls may vary with native
time. Both the reference and actual laws must have positive full storage
and balanced ports/damping so their propagators are contractions.

The reference has m_c(tau)=beta_c(tau)U(tau)seed. Its scalar/common-J motion
is exactly invisible to projective phase when beta_c is nonzero. The
common generator difference from the nominal kappa=1/4,gamma=1,c=0 law is
bounded by

\[
\delta_c\le2/1000+1/4000+1/1000=13/4000.
\]

Variation of constants on a unit active seed, combined with the previous
nominal b>1/8 on tau in [1,H], H=5107/700, proves

\[
|\beta_c(\tau)|>1/8-H\delta_c
=283609/2800000>1/10.
\]

The positive calibration gain is **1/|beta_c(tau)|**, bounded by10.
The unknown phase of beta_c need not be subtracted: the polygon cancels
it. Accurate amplitude/reference calibration remains an explicit changed
readout assumption; dividing by the old nominal b without accounting for
common gain changes is not this contract.

Write the actual passive generator as L_c+R with ||R(s)||<=delta_d. The
remainder is specified relative to this declared common reference; it is
not asserted to be an orthogonal or unique operator decomposition. For
example it can contain nonuniform balanced ports/damping and local skew
generator differences, including noncommuting channel patterns. An initial
meter residual of norm<=e0 and seed norm<=s_max give

\[
\|W-W_c\|\le e_0+H\delta_d s_{\max}.
\]

Projection to active meter coordinates and division by |beta_c| cannot
increase this beyond

\[
\boxed{B=10(e_0+H\delta_d s_{\max})}.
\]

The reference samples can carry the phase arg beta_c; their polygon still
equals the unloaded polygon and their overlap magnitudes have the parent
bounds. Applying the homotopy theorem above separates differential error
from all exactly common motion. No empirical common/differential parameter
identification is supplied.

## 4. Sensor errors, quantization and the complete certificate

Let the combined calibrated per-register sensor/reference error be <=r.
Keep the inherited b-bit uniform range[-2,2), nearest-even quantizer with
half-step2/2^b, and the exact integer estimator/gates. Since the raw active
meter norm is now >=s_min-B, the additional normalized complex-overlap
error is at most

\[
\zeta=\frac{31}{2}\frac{r+2/2^b}{s_{\min}-B}.
\]

Here meter dynamics are already accounted for by b_m; they are not charged
again as sensor noise. With parent gain/time contribution b_g and sampling
contribution b_s, the total circular error relative to the same seed's
Q0=exp(-2pi*i*r_hidden) obeys

\[
\boxed{b_{\rm total}=b_g+b_s+b_m+
\frac{\zeta}{a_e-\zeta}+128\frac{\zeta}{a_\ell-\zeta}}.
\]

All comparisons below are exact rational comparisons in audit.py; displayed
phase decimals are rounded upward.

| Quantity | PHASE_26 | PHASE_21 |
| --- | --- | --- |
| ADC bits | 26 | 21 |
| Differential operator allowance delta_d | 1/1000000 | 1/5000000 |
| Combined sensor/reference budget r | 9/320000000 | 9/80000000 |
| Initial meter norm e0, retained | 9/12800000000 | 9/3200000000 |
| Meter phase allowance b_m, rad | <0.000871534 | <0.000141857 |
| Total phase bound, rad | <0.002468774 (<1/400) | <0.003980161 (<1/250) |
| Observed endpoint visibility | >0.99107 | >0.99134 |
| Observed link visibility | >0.99931 | >0.99958 |
| New/previous sufficient operator allowance | >11413 | >570 |

Both retain endpoint >0.99, links >0.999, raw active norm in(0.8,1.2),
no ADC saturation, and nontrivial phase chord |Qhat-1|>1.7. The shared
target is0.004rad. PHASE_26 does not retain the prior stricter0.002rad bonus,
and neither new protocol requires model error to fit the old per-register
raw budget. Exact arithmetic does not erase this amendment or the exposed
selection of delta_d, ADC bits, common controls and rational root bounds.

The old/new allowance ratios combine this explicit budget amendment with
the sharper phase argument. To isolate the mathematical improvement, the
audit also uses the **same amended settings** with an independent-overlap
model bound, setting z_m=4B/s_min and adding
z_m/(v-z_m)+128*z_m/(v_l-z_m) instead of b_m. That estimate exceeds0.004rad
for both selected profiles. Its failure is a failure of that sufficient
bound, not a failed physical trajectory. The new polygon estimate passes
without changing those settings.

For explicit gain/timing/noise controls, put S_max=11/10+e0 and choose
eps_a=r/(30S_max), j=r/[150S_max(1+eps_a)], nu=r/3. Since ||m'||<=5S_max
in the declared family,
10S_max*eps_a+50S_max*(1+eps_a)j+nu=r. Amplitude-reference computation error
must also fit this calibrated budget. These are still very demanding
assumptions, not measured sensor accuracy or timing in seconds.

The previous finite64-native-unit reset and bounded off-port leakage can
supply the retained e0 precondition. Digital reference storage and exact
Gaussian integer phase accumulation remain as previously specified; added
analog meter coordinates, calibration workspace and external record/reset
operations are not removed by taking a projective quotient.

## 5. Verification, failed extensions and remaining scope

From repository root, standard-library Python:

```bash
python3 experiments/qpb1-projective-tolerance/audit.py --out /tmp/ud-projective-tolerance
```

**EXACT constructor checks:** 27 source hashes, 13 literal ledger rows,
100 rational unit polygons/tangent variations with exact collected-gradient
identity, radial/vertical annihilation and squared gradient bounds, plus
the rational common-signal, homotopy, noise, support/visibility and total
phase inequalities. The general proofs above cover continuous bounded
errors; finite examples alone do not. Twenty centered binary64 finite
differences cross-check the derivative with tolerance2e-6; observed maximum
discrepancy is about3.094e-9.

**NUMERICAL constructor:** 360 windows cover two bit profiles, five seed
preparations, three plant gain triples, four common-control profiles and
three differential directions/window choices. Closed binary64 coupled-mode
solutions include initial residual and imposed combined sensor error,
then exact nearest-even digitization and the inherited integer estimator.
Model phase, sensor phase and total phase are checked separately. Maximum
displayed total error is about0.000365350rad; reference meter gain stays
above0.15632 in these cases. Observed calibrated model error can exceed
the previous raw budget, confirming that the amplitude restriction was
actually relaxed. A captured integer witness replays without the numerical
trajectory generator.

Synthetic model-norm comparisons use5e-13 and phase comparisons5e-11
tolerance. These are not interval enclosures, an independent review or an
experiment. The general norm theorem allows nonuniform/noncommuting
passive remainders; this finite campaign uses a commuting sector subset.
Quantization does not acquire exact continuous gauge covariance; its
bounded error is evaluated separately after the exact geometric quotient.

The attempted PHASE_21 differential allowance1e-6 fails this sufficient
certificate. That is not an impossibility theorem or a measured threshold.
The previous out-of-budget0.05 hidden-detuning failure and stock-only
observability obstruction retain their original scopes. No source law,
physical U(1), spin, clock/action calibration or numerical eta_A follows.

See [contract](PHASE_CONTRACT.json),
[candidate](../../candidates/qpb1-projective-tolerance/candidate.json),
[receipt](../../sessions/qpb1-projective-tolerance-20261024-a1/mathematical_receipt.json),
and [immutable run](../../artifacts/qpb1-projective-tolerance-20261024-a1/exact-001/manifest.json).

**Next discriminant:** derive a sharper structured three-sector bound that
uses near-return and amplitude/phase cancellation, testing whether the
previous0.01 passing development point can be enclosed uniformly rather
than requiring a general full-state norm estimate. Arbitrary channel errors
and physical calibration must retain their separate budgets.
