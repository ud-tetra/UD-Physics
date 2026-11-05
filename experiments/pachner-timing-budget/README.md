# Pachner crossing and projected-mask readout tolerance v0.1

**EXACT / CONDITIONAL.** Discovery base `41da46f2f3f3dd25f794fbbb5dedc16ea00854d8`.
This consolidates and extends the prior chat-only mask comparison with executable
rational checks and an analytic crossing-time/readout proof. No empirical data
or physical units enter. Physical promotion 0. Constructor verification only.

## Objects and assumptions

Use the snapped 2-to-3 ball, ascending signed simplex bases, transport
M:R^23->R^27, orthogonal kernel projector P, and H=M^T M+P=I+G
from ../pachner-trigger-lift/README.md (Objects; post-event memory coupling).
G has eigenvalues 0,1/2,3/2. The old skew generator A_o has norm <=5
in the unit simplex metric. Nominal c_0 has amplitude 1 on face (0,1,2)
and edge (0,1), zero elsewhere; ||c_0||^2=2, c_0^T H c_0=29/10.
Reserve R_0=9/10; define g(c)=c^T Gc and F(t)=R-g(c(t)).
At nominal event time 0, F=0 and F'=3.

The pre-event trajectory is exp(A_o t)c_0, prepared at t=-a, a=1/600.
An actual preparation differs there by Euclidean norm <=epsilon, propagated
by this SAME generator until the event. Actual reserve is constant and differs
from R_0 by at most r. Both bounds are nonnegative. The event is the unique
inward zero in [-a,a]; no assertion covers earlier history or competing balls.

Two alternative post-event target generators A_h are compared: all active,
and only edge (0,1) active in the vertex-edge block. Both transpose coupling
entries are masked; face-edge and face-top blocks are unchanged.
For BOTH hypotheses the rule projects onto the same event image:
K_h=H^-1 M^T A_h M. The mask stays fixed through the sampling interval.
The single-edge hypothesis may select the unique largest absolute transported
edge amplitude AT the event, then hold it. The selector and holding rule are
constitutive assumptions, not source-derived Q167/Q173 laws.

Tq=(Mq,Pq) embeds into new-plus-memory unit Euclidean space; T^T T=H.
Thus the projected flow is an orthogonal compression of diag(A_h,0);
its H norm is <=5 and its evolution is an isometry. This remains a conditional
projected branch: ../pachner-locality-port/README.md records nonincident
old-coordinate couplings, and ../pachner-current-metric/README.md distinguishes
it from the full new-carrier flow. This work does not resolve that choice.

## Local crossing proof

Let C=G A_o-A_o G. It is symmetric and ||C||<=15.
For the nominal trajectory, |F''|<=2*5*15*2=300, so F'>=5/2
on [-1/600,1/600]. At matching times the actual and nominal states
differ by <=epsilon, because the pre-event flow is an isometry.

Using 2sqrt(2)<3,
|F_actual(0)| <= r+(3/2)(2sqrt(2)epsilon+epsilon^2)
                <= d := r+5epsilon  (epsilon<=1/1000).
The derivative perturbation is at most
15(2sqrt(2)epsilon+epsilon^2)<=45epsilon+15epsilon^2.
If epsilon<=1/1000 and d<=1/1000, the actual derivative is strictly >2
throughout the interval. Nominal endpoint magnitudes are >=(5/2)/600,
larger than d; hence the actual endpoints have opposite signs.
The intermediate value theorem and strict monotonicity give exactly one
inward crossing t_star in the interval. The mean value theorem gives
|t_star|<=(r+5epsilon)/2.

The reserve remains nonnegative in this domain. The event's assumed
stock/reserve balance is the prior conditional balance, not a physical
source of energy or an autonomous derivation of the reserve.

## Readout and deterministic separation

Use the signed target vertex amplitude contrast V(q)=(Mq)_1-(Mq)_0.
Vertex amplitudes are model coordinates, not an orientation-independent
quadratic stock or a calibrated instrument output. The initial signed state
is fixed as above; changing its sign reverses this readout.
Its functional norm is <=sqrt(2) in the event metric.

Exact rational derivatives of V_single-V_all at 0 are (0,0,2,2)
through order 3. ALL target coordinate derivatives agree at orders 0 and 1.
Thus among fixed linear target-state readouts, second order is earliest
for this witness; no statement covers memory readouts or other witnesses.

Each scalar third derivative is bounded by sqrt(2)*5^3*sqrt(29/10).
Taylor's theorem therefore gives
Delta V(s)>=s^2-105s^3>=s^2/2 on 0<s<=1/210.
On s in [1/420,1/210], Delta V>=1/352800.
The nominal classifier compares one scalar reading with the midpoint
[V_single(s)+V_all(s)]/2, assigning the greater value to the single mask.
Its predictions are the exact model functions, not a truncated Taylor
implementation. Finite-precision midpoint computation must be included
in the scalar error eta; it has not been implemented or tested here.

## Joint preparation, reserve, timing and readout tolerance

Let actual sample time be s+delta, |delta|<=nu, in the SAME formal clock
as the pre-event evolution. Nominal event is 0; actual event is t_star.
No additional event timestamp uncertainty is assumed.

At the actual event,
||c_actual(t_star)-c_0||_H <= 2epsilon+12|t_star| =: E.
The coarse crossing domain gives E<=1/125, below 1/2. Since M is a contraction
from H to target Euclidean norm, the transported edge (0,1) retains its
strict amplitude lead (nominal leading amplitude 1, others 0).
Thus the event-based largest-amplitude selection remains unchanged.

Propagate each hypothesis by its own H-isometric K_h. Comparing its
actual reading at elapsed time s+delta-t_star with the same hypothesis's
nominal reading at s gives:
preparation contribution <=sqrt(2)E<=3epsilon+17|t_star|;
time contribution <=5sqrt(29/5)(nu+|t_star|)
                  <13(nu+|t_star|).
Including additive scalar error eta, total error is at most
3epsilon+30|t_star|+13nu+eta
 <=78epsilon+15r+13nu+eta.

Sufficient joint condition:
78epsilon+15r+13nu+eta <= 1/800000.

This condition implies the coarse crossing domain, nu<1/100000,
and s+delta>t_star throughout the sample window.
Since 1/800000<1/705600 (half the certified separation), midpoint
classification is correct for either hypothesis. Hold the mask at least
until actual elapsed time 1/210+nu+d/2. No time-in-seconds map is supplied.

Concrete simultaneous example:
epsilon=1/200000000, r=1/100000000,
nu=1/100000000, eta=1/4000000.
Budget used=23/25000000<1/800000.
Crossing shift <=7/400000000.

These are conservative sufficient bounds, not optimal tolerances or
empirically measured errors. They assume unchanged generator, transport,
metric and signed readout calibration. Perturbations of those objects,
competing events, mask restoration, physical instrumentation and native
derivation of the mask/trigger remain OPEN.

## Reproduction and scope

Run from repository root:
python3 -B experiments/pachner-timing-budget/audit.py

The script uses only the Python standard library and existing Fraction
helpers. It checks ranks, metric identities, skewness, exact derivatives
and the rational inequalities used in this proof. Those checks support
this proof; no automatic interval solver or independent reviewer is claimed.

Sources: ledger v0.39 Q165-Q173 and Q177-Q179, as identified in the prior
trigger-lift source receipt; prior transport/interface scripts at the base
revision. The projected law, reserve, selected mask, hold duration,
preparation and readout remain explicitly conditional. No Klein bottle
topology or basin attraction has been established.

## Continuation comparison

[Comparison amendment v0.2](COMPARISON_v0.2.md) proves the original preparation
is exactly blind to full-versus-projected continuation and gives a separate
controlled apex probe. The v0.1 mask distinction above is unchanged.

[Finite classifier v0.3](CLASSIFIER_v0.3.md) implements the controlled-probe
midpoint with rational arithmetic and certified prediction enclosures.
