# Post-event generator and activation-ramp tolerance v0.4

**EXACT / CONDITIONAL.** Continues the finite classifier at
`5549d2b077313eebe776850aa6aae8f70fd0729f`.
The readout, signed apex probe, nominal clock, event transport and metric
are those of [v0.2](COMPARISON_v0.2.md); the implemented threshold is from
[v0.3](CLASSIFIER_v0.3.md). This is an uncertainty extension of two
conditional models, not a derivation selecting either one.

## Fixed-metric domain

Work in the COMMON target-plus-memory ambient carrier with unit metric.
Let (Tq=(Mq,Pq)), (H=T^	op T), and let (Pi) be the orthogonal
projection onto (operatorname{im}T). Full nominal generator is
(B_F=operatorname{diag}(A_{m new},0)). Projected nominal generator can
be represented on the ambient carrier by (B_P=Pi B_FPi); on the event
image it reproduces (T K_0). Both are skew and have norm at most 5.
The coordinate readout is (W=x_4-x_3), with norm (sqrt2).

For EITHER hypothesis let the actual post-event generator be

[
widetilde B_h(t)=B_h+(1-ho(t))(B_{m off}-B_h)+E_h(t).
]

Assume (B_{m off}) is skew with norm at most 5 in this SAME metric,
(0lehole1), (|E_h(t)|lekappa), and
(int_0^{1/100}(1-ho(t)),dtleell).
Coefficients may be piecewise continuous, or bounded measurable with the
associated finite-dimensional propagator. The error (E_h) need not be skew:
small gain/loss errors are covered by the norm estimate below.
Each hypothesis must satisfy its bounds; their errors need not coincide.
An actual projected-hypothesis perturbation may leak out of the event image;
such leakage is treated as an ambient error, not silently declared absent.

The metric, event map and pre-event generator stay FIXED. The instantaneous
Pachner transport occurs first; the ramp here controls subsequent evolution
on the ALREADY chosen common carrier. It is not a derivation or interpolation
of a topology-changing actuator. Error in the time of that instantaneous
event is covered by the existing preparation/reserve crossing bound.

## Cumulative mismatch bound and classification theorem

For actual post-event elapsed time (	aule1/100),

[
D(	au):=int_0^	au|widetilde B_h(t)-B_h|,dt
 le rac{kappa}{100}+10ell.
]

The factor 10 bounds (|B_{m off}-B_h|le5+5).
For a ramp from zero generator the sharper factor 5 is available,
but the implemented certificate uses the general factor 10.

The skew ramp part has an isometric propagator. The additional error gives
an actual propagator norm at most (exp(int|E_h|)le e^D).
Variation of constants relative to (B_h) therefore bounds the state
difference, from the same actual event state (z_*), by
(e^D D|z_*|).
In the pre-existing coarse preparation domain, the actual event norm is
less than (7/4). Thus (sqrt2|z_*|<5/2).
For (Dle1/100), the exact series bound
(e^Dle1/(1-D)le100/99<6/5) yields

[
|widetilde W_h(	au)-W_h(	au;z_*)|le3D.
]

Add this to the v0.2 data/crossing error budget, using the triangle inequality.
The SAME finite rational classifier remains correct if

[
oxed{78epsilon+15r+13
u+eta+
       rac{3kappa}{100}+30elllerac1{1000000}.}
]

This condition implies the earlier coarse crossing domain, guarantees that
sampling follows the actual event, and implies (	au<1/100):
(1/120+1/2000+1/100000<1/100).
It also implies (Dle1/3000000<1/100), so the propagator estimate is
self-consistent. The v0.3 polynomial midpoint radius is already accounted
for in its residual margin. No extra floating-point midpoint term arises.

## Concrete simultaneous allocation

Keep the v0.2 example:
(epsilon=1/200000000), (r=
u=1/100000000),
(eta=1/4000000).
Add (kappa=1/1000000) and (ell=1/1000000000).
Then

[
Dlerac1{50000000},qquad
B_{m total}=rac{49}{50000000}<rac1{1000000}.
]

For a linear activation (ho(t)=t/T_r) on ([0,T_r]), followed by 1,
the integrated deficit is (T_r/2). The allocation above permits
(T_r=1/500000000). This is a sufficient formal-time tolerance, not an
optimal bound or measured switching duration. It is intentionally conservative.

## Exact clock/rate ambiguity

The readout rows satisfy the global identities

[
ell_F B_F^2=-5ell_F,qquad ell_P K_0^2=-3ell_P.
]

Here (ell_F) is the ambient apex contrast row and (ell_P=ell_F T)
is its old-coordinate pullback; neither is the ramp-deficit bound (ell).
For the fixed nominal apex probe (W(0)=-1/4), (W'(0)=0), these imply

[
W_F(s)=-	frac14cos(sqrt5,s),qquad
W_P(s)=-	frac14cos(sqrt3,s).
]

A full-flow rate multiplier (sqrt{3/5}) therefore makes THIS ONE readout
identical to the unit-rate projected readout for all times.
It does not establish equality of the full states or every other readout.
A shared registered clock/rate convention, or independently bounded rate
error, is required for this discriminator. Unlimited rate freedom cannot
be overcome by greater precision on this single signal.

Likewise an unrestricted off-gate held at zero throughout sampling makes
both branches static and indistinguishable. Such ramps exceed the admitted
deficit budget; the narrow positive theorem does not cover them.

## Execution and limitations

Run `python3 -B experiments/pachner-timing-budget/robustness.py`.
The script checks both exact readout ODEs, the rate-alias identity,
rational constants, simultaneous allocation and 1,028 adversarial
expanded-prediction endpoint readings at 257 times using the implemented
robust-budget wrapper. The continuous uncertainty guarantee comes from
the proof above, not from enumerating all possible perturbation functions.
Negative and excessive uncertainty declarations are rejected.

Changes to the metric/readout calibration, pre-event generator,
event transport, or topology-changing transition law are outside this
certificate. Declared error and deficit bounds are supplied, not inferred.
No empirical test, independent review, attraction basin, or physical
promotion is established.
