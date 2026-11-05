# Two-boundary-readout discriminator without absolute rate calibration v0.5

**EXACT / CONDITIONAL.** Continues source commit
`3434916ad00ffc63bf84180cabc93fa8e15dc635` and
[the v0.4 rate obstruction](ROBUSTNESS_v0.4.md).
The same deliberately prepared old state (c_0+rac14 e_3), event transport,
fixed metric and two all-active continuation hypotheses are retained.
Physical promotion 0. This is a new observable pair, not a native preparation law.

## Two source-bound boundary contrasts

Let (W=x_4-x_3) be the target apex contrast and
(Y=x_1-x_0) the target equatorial contrast, read simultaneously.
These are two distinct linear functionals of target vertex amplitudes.
Both have Euclidean functional norm (sqrt2); their pullbacks to the event
image have norm at most (sqrt2) in H.

The exact row identities for W have squared frequencies 5 (full) and 3
(projected). New exact row checks establish squared frequency 5 for Y in
BOTH models. The declared preparation gives
(W(0)=-1/4,dot W(0)=0,Y(0)=0,dot Y(0)=2).
Consequently, writing (u) for the common post-event phase,

[
W_F(u)=-rac14cos(sqrt5,u),quad
W_P(u)=-rac14cos(sqrt3,u),quad
Y_F(u)=Y_P(u)=rac2{sqrt5}sin(sqrt5,u).
]

All row and initial-data identities are checked with rational matrices.
These exact equations do not supply seconds or physical instrument gains.

## Remove the unknown common clock

Allow arbitrary common nonnegative scalar rate (v(t)), including a ramp
or pauses, so (u(t)=int_0^t v(s),ds). The two readings from a given model
must share this phase. Each model may use its own unknown rate.
No absolute scale, rate constancy, or known duration is needed below.

Define the algebraic residual

[
R(W,Y)=16W^2+rac54Y^2-1.
]

Full evolution satisfies (R_F=0) for every phase.
Projected evolution gives

[
R_P(u)=sin^2(sqrt5,u)-sin^2(sqrt3,u).
]

Thus the single-channel rate adjustment from v0.4 cannot make these two
curves agree on the startup segment. The squared frequency ratios are
1 for full and 3/5 for projected evolution; a common scalar rate cannot
change a within-model ratio.

## Startup segment and an observable admission window

Require the nominal reference phase to be on its first rising quarter,

[
0le ulerac{pi}{2sqrt5}.
]

This is an explicit startup/branch-registration assumption, supplied by the
caller; the two-reading implementation does not infer it from one snapshot.
Later cycles are not covered. In particular, phase zero has R=0 in both
models, so a nonzero reference-window condition is essential.

Let measured contrasts (widehat W,widehat Y) each differ from the same-phase
nominal contrasts by at most (delta=1/1000000).
Admit observations only when

[
widehat Yin[1/100,1/80].
]

These error and admission bounds imply ideal (Yin[1/120,1/60]).
On the first reference quarter, (sin zle z) and
(sin zge2z/pi) give (Yle2u) and (Yge4u/pi>u).
Therefore admitted ideal phases satisfy
(uge1/240) and (ule1/60<1/10), without a time measurement.

The fourth derivative of (R_P(u)) has magnitude at most
(8(25+9)=272). Its initial derivatives through order 3 give
(R_P=2u^2+O(u^4)). Taylor's theorem yields

[
R_P(u)ge2u^2-rac{34}{3}u^4
          ge u^2gerac1{57600}
]

throughout the admitted startup region.

## Finite exact classifier and noise certificate

Because (|W|le1/4), (Yle1/60), and each channel error is at most delta,

[
|widehat R-R|
leleft(8+rac1{24}ight)delta+rac{69}{4}delta^2
=rac{96500207}{12000000000000}
<rac1{115200}.
]

The first term comes from the linear perturbation of the two squares;
the second from (16delta^2+(5/4)delta^2).
The runtime computes only a rational quadratic polynomial in the measured
readings. It uses no trigonometric approximation, derivative estimator,
clock reading or numerical frequency fit:

- If startup is not registered, return INDETERMINATE_BRANCH.
- If the reference reading is outside its window, return OUTSIDE_REFERENCE_WINDOW.
- If (|widehat W|>1/4+delta), return OUTSIDE_MODEL_ENVELOPE.
- Otherwise, (widehat R<1/115200) selects FULL;
  (widehat R>1/115200) selects PROJECTED; equality is INDETERMINATE.

For either admitted model the residual margin is at least

[
rac1{115200}
-rac{96500207}{12000000000000}
=rac{22999379}{36000000000000}>0.
]

Arbitrary observations can still receive a label; classification does not
prove that either model describes the input.

## Preparation, reserve and nonscalar generator errors

Retain the v0.2 pre-event generator and local crossing domain.
Its event-time shift satisfies (|t_*|le(r+5epsilon)/2);
the event-state H error is at most (2epsilon+12|t_*|).
Unknown common phase absorbs the post-event timestamp and common sampling
jitter, so the observable-pair error does not need the earlier fixed-clock
13nu term. Independent channel sample displacement must instead be bounded
as part of the per-channel scalar error eta.

For each hypothesis, let the actual post-event generator be
(v(t)B_h+E_h(t)) in the fixed ambient metric, and let
(D=int|E_h(t)|dt) through the sample be bounded.
The scalar rate term is skew even when v is arbitrary.
As in v0.4, (Dle1/100) gives extra scalar error at most 3D.
The preparation contribution to either channel is at most
(3epsilon+17|t_*|).
Thus a sufficient PER-CHANNEL budget for the pair is

[
oxed{rac{91}{2}epsilon+rac{17}{2}r+3D+eta
       lerac1{1000000}.}
]

It implies the earlier coarse crossing domain and the small-D hypothesis.
There is no absolute-duration restriction here; D is a cumulative bound
through whatever sample reaches the reference window.
For epsilon=1/200000000, r=1/100000000, D=1/50000000,
eta=1/4000000, the used budget is 249/400000000.

A purely common scalar activation ramp is absorbed into u EXACTLY.
A gate that changes different couplings independently contributes to E and
must satisfy the D budget. A gate that never advances phase never enters
the reference window; the classifier abstains rather than guarantees detection.

## Executed checks and reproduction

Run `python3 -B experiments/pachner-timing-budget/two_readout.py`.

The script checks the four exact squared-generator row identities and
initial conditions, scalar-series coefficients through degree 12, rational
phase/window/noise inequalities, and the joint budget.
At 257 rational test phases, it encloses the two nominal signals by rational
degree-12 Taylor bounds and tests all four simultaneous noise corners for
both hypotheses: 2,056 adversarial checks. Fixed signs make the corners
the residual extrema within each tested rectangle.
Continuous guarantees follow the proof, not grid extrapolation.
Branch/window abstention and over-budget rejection are tested.

Constructor verification only; no independent review or empirical test.
Relative channel gain/offset calibration, simultaneity, phase-branch
registration, metric/event-map stability and native selection of the signed
probe remain separate dependencies. No Klein-basin attraction is established.
