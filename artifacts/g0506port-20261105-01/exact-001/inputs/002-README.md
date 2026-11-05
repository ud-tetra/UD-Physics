# Complete continuous phase/action readout v1.0

**RESULT — EXACT / CONDITIONAL.** The metric connection `alpha=<Jx,dx>/a`
is smooth on every nonzero active native state, including the two-dimensional
cell/surface plane invisible to edge events. Its gauge transformation and loop
normalization are explicit. Native undriven motion has nonzero loop action but
**trivial projective geometric holonomy**. A separately declared two-rate law
gives nontrivial geometric phase on an entire perturbation ball; the phase varies
continuously and is not a quantized sign. Connection normalization does not
independently determine the physical action ratio.

Discovery base `a4ae75dd55cd2b691c811c4d6eeae1367fcba015`; recorded 2026-10-23
(America/Chicago). [Source bindings](SOURCES.json) pin fourteen files, including
the imported archive v0.85 (inherited scientific revision v0.43), native source
text and earlier Discovery audits. [Selected rows](SOURCE_ROWS.json) preserve
thirteen literal ledger rows. Original uploaded paths were unavailable after
runtime recovery; this run verifies committed imports, not a new comparison
against those uploads. Missing Genesis PNG is unused. Physical score
**UNSCORED**, promotion **0**; no mainline/source-ledger/shared-CURRENT amendment.

## 1. Objects and scope

Retain the oriented filled tetrahedron chain carrier
`C_*(Delta3;R)=R15`, ascending simplex orientations, unit Euclidean chain metric,
boundary `d`, and the imported conventions

\[
A=d-d^T,\quad P=-A^2/4,\quad J=A/2,\quad
E=\operatorname{im}P\cong\mathbb R^{14},\quad J^2=-I_E.
\]

Here E denotes the active **space**; the code's `E` is explicitly the edge
projector. Use `P_edge` in this text. For `x in E`, set `a=<x,x>>0` and retain
the imported native loop one-form

\[
\Theta_x(v)=\tfrac12\langle Jx,v\rangle,\qquad
\mathcal I=\int\Theta,\qquad
\mathcal S_{\rm native}=\mathcal A_0\mathcal I,
\quad\mathcal A_0=B_0a_0^2/\tau_0.
\]

`I` is dimensionless native loop action; `S_native` has declared action units.
This is not the complete first-order functional `integral(Theta-H ds)`, which
vanishes on the unmodified native orbit. O14 fixes the direction
`eta_A=A0/hbar`; its numerical physical identification stays OPEN. Bare G06 is
not reused. No amplitude/support quantization is assumed.

**Added quotient hypothesis:** regard `J` as multiplication by i and identify
normalized states under `x -> exp(J chi)x`, with chi modulo `2pi`. Thus the
unit sphere is `S13`, its ray quotient is `CP6`, and the declared fiber is an
ordinary period-`2pi` U(1). This is a mathematical construction on the given
carrier, not an imported physical gauge principle or a spinor double cover.

## 2. A smooth complete connection and its gauge law

Define

\[
\boxed{\alpha=\frac{\langle Jx,dx\rangle}{a}
                 =\frac{2\Theta}{a}}.
\]

For every nonzero x, `alpha_x(x)=0` and `alpha_x(Jx)=1`. It is invariant under
positive radial scaling, constant fiber rotations and every signed simplex S4
action, since those actions are orthogonal and commute with J. On the unit
sphere, its horizontal vectors are exactly the metric-orthogonal complement
to the fiber direction Jx. These properties define the metric-orthogonal
principal connection for the declared U(1) action. Other connections can be
formed by adding basic one-forms; S4 symmetry alone is not a uniqueness proof.

For a differentiable path and any real differentiable gauge chi,

\[
\widetilde x=e^{J\chi}x,\quad
d\widetilde x=e^{J\chi}(dx+Jx\,d\chi),
\]
\[
\boxed{\widetilde\alpha=\alpha+d\chi},\qquad
\boxed{\widetilde\Theta=\Theta+\tfrac a2d\chi}.
\]

For `x -> r x`, `r>0`, Theta scales by `r^2` and alpha is unchanged; the
radial derivative term vanishes because `<Jx,x>=0`. The origin is excluded,
not patched with an arbitrary phase. No nonzero component, edge detector,
threshold, or event-order convention is required. This is carrier-complete
coverage, not a claim that a scalar one-form reconstructs all fourteen state
coordinates or supplies an apparatus.

The earlier invariant splitting remains

\[
P_v=P_{\rm edge}+JP_{\rm edge}J^T,\quad P_h=P-P_v,
\quad (\operatorname{rank}P_v,\operatorname{rank}P_h)=(12,2).
\]

It gives `a=a_v+a_h`, `Theta=Theta_v+Theta_h`, and, when both sectors are
nonzero, `alpha=(a_v alpha_v+a_h alpha_h)/a`. The numerator formula remains
well defined when either sector vanishes. A pure hidden-plane state has a
valid alpha despite emitting no edge events.

## 3. Curvature and an explicit normalization check

For active tangent vectors u,v, differentiating alpha gives

\[
F_x(u,v)=d\alpha_x(u,v)
=\frac{2\langle Ju,v\rangle}{a}
-\frac{2}{a^2}\left[
\langle x,u\rangle\langle Jx,v\rangle
-\langle x,v\rangle\langle Jx,u\rangle\right].
\]

It annihilates x and Jx. On their orthogonal complement it equals
`2<Ju,v>/a`, a nondegenerate skew form, so its rank is twelve and its kernel
in E is exactly `span{x,Jx}`. This moving kernel differs from the fixed
two-dimensional edge-observer kernel. For x the unit edge01 register and h
the unit oriented top-cell register, h and Jh are horizontal and
`F_x(h,Jh)=2`: the hidden plane is present in this readout.

A two-complex-coordinate projective line supplies a direct integral check.
Choose complex-orthonormal u,h. With latitude theta in `[0,pi]` and longitude
varphi modulo `2pi`, use the north and south sections

\[
z_N=\cos(\theta/2)u+\sin(\theta/2)e^{J\varphi}h,\qquad
z_S=e^{-J\varphi}z_N.
\]
\[
\alpha_N=\sin^2(\theta/2)d\varphi,\quad
\alpha_S=-\cos^2(\theta/2)d\varphi,\quad
\alpha_N-\alpha_S=d\varphi,
\]
\[
F=\tfrac12\sin\theta\,d\theta\wedge d\varphi,\qquad
\frac1{2\pi}\int_{\mathbb{CP}^1}F=1.
\]

The orientation is fixed by this displayed coordinate form. This is unit
curvature flux in the declared real-connection convention; associated line
bundle sign conventions may reverse the Chern-number sign. It is not a
physical charge. Halving alpha would give flux pi and half a fiber response:
`(Theta/a)(Jx)=1/2`. It therefore fails normalization as a connection for this
same period-`2pi` principal action. A different covering group, quotient or
associated representation would be an additional premise.

## 4. Geometric holonomy, native action and the factor of two

For a normalized path y whose ray closes, choose endpoint phase modulo `2pi`
so `y(T)=exp(J chi_end)y(0)`. Fix the convention

\[
\boxed{\mathrm{Hol}=\exp\left(i\left[\chi_{\rm end}
                                   -\int_0^T\alpha\right]\right)}.
\]

Under a path-dependent gauge, chi_end and the integral change by the same
endpoint difference. The exponential is therefore gauge independent.
It is the endpoint rotation of the horizontal lift. Closed representatives
have `Hol=exp(-i integral alpha)`; endpoint correction is essential for a
general ray-closed path. Integer associated weights w give `Hol^w`.

For the unmodified source law `x'=Ax=2Jx`, a is constant,

\[
\alpha(x')=2,\quad\Theta(x')=a,\quad
\chi_{\rm end}=2T\pmod{2\pi},\quad\mathrm{Hol}=1.
\]

Every native orbit is a **constant ray**. At a full state recurrence `T=pi*n`,
`I=pi*a*n` and `S_native=pi*a*n*A0` are generally nonzero. The quotient removes
the common rotation while the lifted native action retains it. Neither
observable replaces the other; neither conclusion contradicts the earlier
threshold-event obstruction or action-carry receipt.

There is a concrete half-normalization failure. Along a closed representative,
a gauge of winding m changes `integral(Theta/a)` by `pi*m`; its exponential
flips sign for odd m. Thus that exponential is not an ordinary-ray invariant
under the declared full gauge group. An apparent native `-1` from this
half-connection cannot establish physical spin.

If one **additionally postulates** unit support `a=1` and physical phase
`exp(i eta_A integral Theta)`, gauge independence under all winding gauges
requires `eta_A/2` to be an integer. Choosing the positive primitive
weight-one character further selects `eta_A=2`. Higher weights, sign and the
physical phase map are not selected by the native law. This restates the
already exposed Q287/Q288 phase-identification candidate, not an independent
action calibration or a new target-blind prediction.

For arbitrary continuous positive support there is no fixed nonzero eta_A
that makes this **raw** action exponential gauge independent for all states:
constant a would require `eta_A*a/2` integral for every a. With variable a,
even zero-winding gauges change it: `a(t)=2+cos(t)`, `chi(t)=sin(t)`,
`t in [0,2pi]` gives `Delta integral Theta=pi/2`. These are legitimate smooth
paths with common endpoints. Normalizing the connection solves a geometric
problem; identifying A0 with a measured action unit remains a separate one.

## 5. Conditional nontrivial phase from relative-mode detuning

A minimal testable change of law is

\[
\boxed{G=J(\omega_vP_v+\omega_hP_h)},\qquad
\omega_v,\omega_h>0.
\]

This is an **added two-rate hypothesis** using the existing invariant
splitting. G is skew, S4-equivariant and J-commuting; it conserves a_v,a_h
and a. There is no transfer of support or energy between these sectors.
The source generator is recovered exactly at `omega_v=omega_h=2`.

Set `Delta=omega_h-omega_v != 0` and `r=a_h/a`. If both sectors are nonzero,
the ray period, common endpoint rotation and loop readouts are

\[
T=\frac{2\pi}{|\Delta|},\quad
\chi_{\rm end}=\omega_vT\pmod{2\pi},\quad
\int\alpha=(\omega_v+\Delta r)T,
\]
\[
\boxed{\mathrm{Hol}=e^{-2\pi i\,\operatorname{sgn}(\Delta)r}},\qquad
\mathcal I(T)=\pi a\left[\frac{\omega_v}{|\Delta|}
                                  +\operatorname{sgn}(\Delta)r\right].
\]

No commensurability of the two absolute rates is required for a ray return;
a full state return requires their common endpoint phase also be integral
in units of `2pi`. For a pure sector the ray is constant and T need not be
its minimal ray period. As Delta tends to zero, this chosen T diverges;
the native Delta=0 case has Hol=1, with no contradiction at a fixed time.

| Hidden support fraction r | Hol for positive Delta |
| --- | --- |
| 0 | 1 |
| 1/4 | -i |
| 1/2 | -1 |
| 3/4 | i |
| 1 | 1 |

These fractions are illustrative preparations, not privileged quantized
states. Every intermediate r is allowed; Hol changes continuously.

**Open-domain certificate.** Take unit reference `y0=(u+h)/sqrt(2)` with
the unit edge and top-cell registers above. For every active perturbation
delta of norm at most `epsilon=1/10`, let `y=y0+delta`, without requiring
unit norm. Write `D=P_h-P_v`, so `||D||=1`, `<y0,Dy0>=0`. Then

\[
|a_h-a_v|=|\langle y,Dy\rangle|\le2\epsilon+\epsilon^2,
\quad a\ge(1-\epsilon)^2,
\]
\[
\left|r-\tfrac12\right|
\le\frac{2\epsilon+\epsilon^2}{2(1-\epsilon)^2}
=\frac7{54},\quad
r\in[10/27,17/27]\subset[1/3,2/3].
\]

Therefore **`|Hol-1|>=sqrt(3)` throughout this entire ball** for any fixed
nonzero detuning, evaluated at its ray period. Exact -1 occurs at r=1/2;
the nontriviality is robust, the exact sign is not. This is an analytic
all-state norm certificate for an ideal mathematical readout and changed
law, not a finite sampling claim, measurement-noise bound or physical
implementation. Native selection of the detuning and a physical relative
phase observable are OPEN.

## 6. Evidence, comparison and next discriminant

Reproduce from repository root with standard-library Python:

```bash
python3 experiments/qpb1-continuous-phase/audit.py --out /tmp/ud-continuous-phase
```

The code reconstructs the 15-register carrier using exact Fractions and
checks fourteen source hashes, thirteen literal ledger rows, ten state
fixtures, 450 gauge cases, all 24 signed S4 actions with 480 readout checks,
2,250 curvature derivative checks, and 28 native/30 detuned loop receipts.
Rational fixtures test the gauge law with
radial derivatives and time-dependent fiber rotations; a quotient-rule
implementation independently checks the displayed curvature expression.
The rank/kernel theorem, patch integral, general gauge laws, rate-family
solutions and perturbation certificate have analytic proofs above.
Constructor calculations and algebraic cross-checks are not independent
LLM review or empirical replication. No ODE sampling or external numeric
package is needed.

The external baseline is ordinary geometric phase: Simon's 1983 paper
connects Berry phase to bundle holonomy, and Aharonov–Anandan's 1987 paper
describes a phase for cyclic ray evolution without an adiabatic restriction.
Publisher abstracts were consulted; these comparisons do not establish a
UD-to-quantum correspondence. See DOI links in SOURCES.json. Our connection,
sign convention, curvature and loop formulas are derived here on the
specified native carrier. This reproduces established geometric machinery;
its UD-specific value is complete visibility, the native constant-ray
obstruction and the explicit conditional detuned realization.

Known targets include native frequency2, the earlier eta2 candidate and
finite recurrence signs. The unit-support physical phase map, weight-one
choice, common-phase quotient and two-rate law are disclosed premises.
No empirical target was fitted, no fresh prediction was tested, and no
native-to-SI clock/action map was supplied.

See [receipt](../../sessions/qpb1-continuous-phase-20261023-a1/mathematical_receipt.json),
[candidate](../../candidates/qpb1-continuous-phase/candidate.json) and
[immutable run](../../artifacts/qpb1-continuous-phase-20261023-a1/exact-001/manifest.json).

**Next discriminant:** classify source-compatible symmetry-preserving local
generator changes on this same carrier. Determine whether relative-mode
detuning is permitted or selected by a stated local law, and what minimal
additional assumption is required. Compare the surviving family against
the undetuned null before proposing a physical phase or action-unit bridge.
