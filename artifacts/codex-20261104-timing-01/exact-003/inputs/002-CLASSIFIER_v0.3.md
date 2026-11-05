# Finite rational prediction and classification v0.3

**EXACT / CONDITIONAL.** Source: comparison amendment v0.2 at
`b2a8abbc3ea24d6aeb6b75d3c644c054d4a6cedf`.
This implements the two-readout midpoint computation left open by
[the comparison proof](COMPARISON_v0.2.md). It preserves the original
preparation's all-times blindness theorem.

## Objects and nominal polynomials

Use the same deliberately prepared old state (c_0+rac14 e_3), reserve,
signed simplex bases, transport, metric and all-active generators as v0.2.
The scalar readout is the signed boundary contrast (W=x_4-x_3).
Full ambient flow uses (operatorname{diag}(A_{m new},0));
projected flow uses (K_0=H^{-1}M^	op A_{m new}M).
Both compare the same transported event state. Native time is dimensionless.

Exact matrix derivatives give the fourth-order Taylor polynomials

[
p_F(s)=-rac14+rac58s^2-rac{25}{96}s^4,qquad
p_P(s)=-rac14+rac38s^2-rac3{32}s^4.
]

Their midpoint is the FINITE rational threshold

[
m_4(s)=-rac14+rac12s^2-rac{17}{96}s^4.
]

The implementation takes rational nominal sample time (s) and rational scalar
reading (y). It returns FULL if (y>m_4(s)), PROJECTED if (y<m_4(s)),
and INDETERMINATE on equality. It rejects times outside
([1/240,1/120]) and floating-point inputs. The checked wrapper also rejects
negative declared error bounds or bounds exceeding the certificate.
The caller must establish the actual validity of the declared bounds.

## Prediction enclosure and continuous certificate

The event norm is (sqrt{237/80}), the readout functional norm is at most
(sqrt2), and each generator norm is at most 5. The real-time flow is an
isometry in the relevant ambient/event metric.
The integral Taylor remainder after degree 4 is therefore at most

[
R_4(s)le sqrt{237/40},rac{(5s)^5}{5!}
 < rac52rac{(1/24)^5}{5!}
 = rac1{382205952}=:R.
]

No exponential growth factor is needed: the bound uses isometry on the real
time interval, not a general matrix-exponential norm estimate.
Thus each exact nominal prediction belongs to
([p_h(s)-R,p_h(s)+R]), and its exact midpoint differs from (m_4(s))
by at most (R).

The v0.2 proof gives (W_F-W_Pge1/460800) throughout the sampling window.
For the declared combined actual-data error

[
B=78epsilon+15r+13
u+etalerac1{1000000},
]

the distance of either allowed observation from the polynomial threshold,
on its correct side, is at least

[
rac1{921600}-rac1{1000000}-R
 =rac{492407}{5971968000000}
 >rac1{13000000}>0.
]

This proves the classifier for EVERY rational nominal sample time in the
closed window and every observation satisfying the declared bound.
The prediction enclosure itself also holds for real times, but this particular
implementation accepts only exact Fraction times. A real sampling displacement
from the supplied rational nominal time belongs in (
u).
Sensor quantization/input conversion and any independent scalar reading
error belong in (eta). Fractions perform finite exact integer arithmetic;
there is no internal binary-floating midpoint rounding term.

The same simple generator-norm remainder after degree 3 is too large to
establish this particular error-budget certificate over the whole window.
That does not rule out a sharper lower-degree method.

## Executed checks

Run `python3 -B experiments/pachner-timing-budget/classifier.py`.

- The code reconstructs the source matrices and derives coefficients by forward
  state recurrence and a separate backward readout recurrence through order 8.
- All coefficients agree; the displayed degree-4 constants match exactly.
- At 257 rational sample times, degree-8 prediction intervals are contained
  in the declared degree-4 enclosures.
- At each time the two endpoints of each degree-4 enclosure expanded by
  the full scalar error budget classify correctly: 1,028 adversarial checks.
  Monotonicity covers interior readings at those sample times; the analytic
  proof above covers all sample times, rather than extrapolation from a grid.
- Equality returns INDETERMINATE. Invalid times, float inputs, negative errors,
  and over-budget declared errors are rejected.

These are constructor checks and a second computational recurrence, not
independent peer review or empirical replication.

## Reusable API

Load `classifier.py` as a Python module and pass `fractions.Fraction` values.
`prediction_intervals(s)` encloses nominal exact predictions.
`threshold(s)` returns the finite decision threshold.
`certified_classify(s,y,epsilon,r,nu,eta)` checks the supplied error budget
before classifying. It cannot infer errors, detect every unmodeled input,
or verify which dynamical law nature uses.

The certificate assumes the declared one-ball event, prepared apex amplitude,
instantaneous switch, fixed all-active continuation, signed reference frame,
generators/metric and clock convention. It gives no native mechanism selecting
the preparation or projection and no Klein-basin attraction theorem.
Physical promotion remains 0.
