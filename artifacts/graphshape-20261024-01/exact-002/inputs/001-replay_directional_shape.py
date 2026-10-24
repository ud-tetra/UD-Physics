"""Exact rational replay of a conditional three-wave passive graphite null.

No DFT or kinetic force measurement is loaded. All identities are within the
equal independent Debye-mode model of graphite-2d-relaxation.
"""

import json
from fractions import Fraction as Q


def add(a, b):
    return tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return tuple(out)


def deriv(a):
    return tuple(i * a[i] for i in range(1, len(a)))


def neg(a):
    return tuple(-x for x in a)


def directional_power(x, squared_cosines):
    return sum((c / (1 + x * c) for c in squared_cosines), Q(0))


def run():
    # Ascending polynomial coefficients: R=N/(2D).
    n, d = (8, 10, 3), (4, 5, 1)
    assert add(n, neg(tuple(2 * t for t in d))) == (0, 0, 1)
    # Remove trailing zero after subtraction before comparing derivatives.
    derivative_num = add(mul(deriv(n), d), neg(mul(n, deriv(d))))
    assert derivative_num[:3] == (0, 8, 5)
    assert all(t == 0 for t in derivative_num[3:])

    samples = {}
    for x in (Q(0), Q(1, 4), Q(1), Q(4), Q(100)):
        parallel = directional_power(x, (Q(1), Q(1, 4), Q(1, 4)))
        rotated = directional_power(x, (Q(3, 4), Q(3, 4), Q(0)))
        ratio = parallel / rotated
        expected = (x + 2) * (3 * x + 4) / (2 * (x + 1) * (x + 4))
        assert ratio == expected
        samples[str(x)] = str(ratio)

    x = Q(1)
    k = x * x * (5 * x + 8) / ((x + 1) * (x + 4) * (3 * x * x + 10 * x + 8))
    assert k == Q(13, 210)
    r_prime_at_one = x * (5 * x + 8) / (2 * (x + 1) ** 2 * (x + 4) ** 2)
    assert Q(1) / (2 * x * r_prime_at_one) == Q(100, 13)
    return {
        "status": "PASS_EXACT_DIRECTIONAL_SHAPE",
        "source_model": "three equal independent passive first-star relaxers, per upper atom",
        "variable": "x=(g_N*abs(v)*eta/kappa)^2",
        "normalized_power_axis": "f0=1/(1+x)+2/(4+x)",
        "normalized_power_30deg": "f30=6/(4+3*x)",
        "ratio": "R=(x+2)*(3*x+4)/(2*(x+1)*(x+4))",
        "ratio_minus_one": "x^2/(2*(x+1)*(x+4))",
        "ratio_derivative": "x*(5*x+8)/(2*(x+1)^2*(x+4)^2)",
        "limits": {"x=0": "1", "x=infinity": "3/2"},
        "samples": samples,
        "log_sensitivity_x_at_one": str(k),
        "log_sensitivity_speed_or_tau_at_one": str(2 * k),
        "inverse_equation": "(3-2*r)*x^2-10*(r-1)*x-8*(r-1)=0, unique nonnegative root for 1<=r<3/2",
        "dlog_tau_dR_at_x_one": "100/13, fixed g and v",
        "load_identity": "d_P ln R=2*K(x)*(d_P ln g_N+d_P ln tau), fixed speed",
        "cross_index_if_shared_tau": "R_13(v)=R_7(sqrt(13/7)*v), star axis registered",
        "scope": "dissipated power only; C>0 and same contact/readout along both directions; not graphite measurement or UD residual",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
