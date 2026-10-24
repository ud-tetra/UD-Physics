"""Exact rational enclosure of the scalar meter transfer on a continuous box.

Intervals round OUTWARD on a rational grid; no binary64 in the certificate.
Time Taylor tails and detuning-series tails are bounded analytically.
"""
from fractions import Fraction as F
from math import factorial

GRID = 10**12


def down(x):
    x = F(x)
    return F((x.numerator*GRID)//x.denominator, GRID)


def up(x):
    return -down(-F(x))


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = down(lo), up(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = box(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-box(other)

    def __rsub__(self, other):
        return box(other)+-self

    def __mul__(self, other):
        other = box(other)
        v = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = box(other)
        assert other.lo*other.hi > 0, 'division interval containszero'
        return self*I(1/other.hi, 1/other.lo)

    def __pow__(self, power):
        assert power >= 0
        if power == 2:
            return I(0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2), max(self.lo**2, self.hi**2))
        ans = I(1)
        for _ in range(power): ans = ans*self
        return ans

    def absmax(self):
        return max(abs(self.lo), abs(self.hi))

    def record(self):
        return [str(self.lo), str(self.hi)]


def box(x):
    return x if isinstance(x, I) else I(x)


def polynomials(order=100, detuning_order=5):
    a = [F(1)]+[F(0)]*detuning_order; b = [F(0)]*(detuning_order+1)
    pa = [[] for _ in a]; pb = [[] for _ in b]
    for n in range(order+1):
        for r in range(detuning_order+1):
            pa[r].append(a[r]/factorial(n)); pb[r].append(b[r]/factorial(n))
        a, b = [-v/4 for v in b], [a[r]/4-b[r]+(b[r-1] if r else 0) for r in range(detuning_order+1)]
    return pa, pb


def evaluate(poly, t):
    ans = F(0)
    for c in reversed(poly): ans = ans*t+c
    return ans


def transfer_enclosure(cells=512, omega=F(11, 500)):
    H = F(5107, 700); order = 100
    assert F(9, 4)*H < 17
    point_tail = F(3**17*17**(order+1), factorial(order+1))
    assert point_tail < F(1, 10**18)
    pa, pb = polynomials(order)
    second = []
    for r in range(6):
        t = F(25, 16)*H**r/factorial(r)
        if r >= 1: t += F(5, 2)*H**(r-1)/factorial(r-1)
        if r >= 2: t += H**(r-2)/factorial(r-2)
        second.append(t)
    def point(t, radius=F(0)):
        av = [evaluate(p, t) for p in pa]; bv = [evaluate(p, t) for p in pb]
        dv = [av[r]/4-bv[r]+(bv[r-1] if r else 0) for r in range(6)]
        B = []; D = []
        for r in range(6):
            er = point_tail+(abs(dv[r])+F(9, 4)*point_tail)*radius+second[r]*radius**2/2
            B.append(I(bv[r]-er, bv[r]+er))
            erd = F(9, 4)*point_tail+second[r]*radius
            D.append(I(dv[r]-erd, dv[r]+erd))
        return B, D
    start, _ = point(F(1)); f_start = start[1]/start[0]
    assert f_start.lo > F(2, 5) and f_start.hi < F(1, 2)
    x = omega*H; C6 = H**6/(factorial(6)*(1-x)); rho6 = C6*omega**6
    C5 = H**5/(factorial(5)*(1-x)); rho5 = C5*omega**5
    amplitude_tail_coefficient = 64*(2+rho6)*C6*omega**4
    coeff_abs = [F(0)]*6; rate_abs = {k: F(0) for k in (1, 3, 5, 7, 9)}
    amp_lo, amp_hi = F(1000), F(-1000)
    fend_lo, fend_hi = F(1000), F(-1000)
    worst_lo = worst_hi = None; summaries = []
    radius = (H-1)/(2*cells)
    for j in range(cells):
        mid = 1+(2*j+1)*radius
        B, D = point(mid, radius)
        assert B[0].lo > F(1, 8)
        for r in range(6): coeff_abs[r] = max(coeff_abs[r], (B[r]/B[0]).absmax())
        sq = B[0]**2
        coeff = {}
        for n in (2, 4, 6, 8, 10):
            total = I(0)
            for r in range(6):
                s = n-r
                if 0 <= s < 6: total += [1, 0, -1, 0][(r-s) % 4]*B[r]*B[s]
            coeff[n] = total/sq
        amp = coeff[2]
        for n in (4, 6, 8, 10): amp += coeff[n]*I(0, omega**(n-2))
        amp += I(-amplitude_tail_coefficient, amplitude_tail_coefficient)
        if amp.lo < amp_lo: amp_lo, worst_lo = amp.lo, j
        if amp.hi > amp_hi: amp_hi, worst_hi = amp.hi, j
        for n in rate_abs:
            total = I(0)
            for r in range(6):
                s = n-r
                if 0 <= s < 6: total += [0, 1, 0, -1][(r-s) % 4]*D[r]*B[s]
            rate_abs[n] = max(rate_abs[n], (total/sq).absmax())
        if mid+radius >= F(699, 100):
            f = B[1]/B[0]; fend_lo = min(fend_lo, f.lo); fend_hi = max(fend_hi, f.hi)
        if j in (0, cells-1): summaries.append({'cell': j, 'time': [str(mid-radius), str(mid+radius)], 'amplitude_coefficient': amp.record()})
    # The quotient (|beta|^2/b0^2-1)/omega^2 lies in this interval,
    # including omega=0 by continuous extension.
    assert amp_lo > F(-3, 2) and amp_hi < 0, ('amplitude', float(amp_lo), float(amp_hi))
    assert fend_lo > F(7, 10) and fend_hi < F(4, 5), ('endf', float(fend_lo), float(fend_hi))
    assert max(fend_hi-f_start.lo, f_start.hi-fend_lo) < F(2, 5)
    c0, c1, c2, c3, c4, c5 = coeff_abs
    real_floor = 1-omega**2*c2-omega**4*c4-8*rho6
    assert real_floor > 0
    y_over_omega = (c1+omega**2*c3+omega**4*c5+8*C6*omega**5)/real_floor
    phase_cubic = (c3+c1*c2+omega**2*(c5+c1*c4)+8*(1+c1*omega)*C6*omega**3)/real_floor+y_over_omega**3/3
    assert phase_cubic < 10, ('phasecubic', float(phase_cubic))
    derivative_tail = F(5, 4)*rho6+omega*rho5
    numerator_tail = derivative_tail+(F(5, 4)+omega+derivative_tail)*rho6
    attenuation = F(3, 2)*omega**2
    rate_coefficient = (sum(v*omega**(n-1) for n, v in rate_abs.items())+64*numerator_tail/omega)/(1-attenuation)
    assert rate_coefficient < 2, ('rate', float(rate_coefficient))
    return {'evidence': 'EXACT_RATIONAL_INTERVAL', 'time_cells': cells, 'time_domain': ['1', str(H)],
            'omega_domain': [str(-omega), str(omega)], 'outward_grid_denominator': GRID,
            'time_taylor_order': order, 'detuning_taylor_degree': 5,
            'time_taylor_point_error_formula': '3^17*17^101/101!',
            'time_taylor_point_error_verified_below': '1/1000000000000000000',
            'time_taylor_point_error_upper': str(up(point_tail)),
            'parametric_tail_rho6_upper': str(up(rho6)),
            'amplitude_omega2_coefficient': [str(amp_lo), str(amp_hi)],
            'amplitude_worst_cells': [worst_lo, worst_hi],
            'f_start': f_start.record(), 'f_end_on_699_100_to_H': [str(fend_lo), str(fend_hi)],
            'normalized_coefficients_abs_upper': list(map(str, coeff_abs)),
            'normalized_phase_rate_coefficients': {str(k): str(v) for k, v in rate_abs.items()},
            'phase_cubic_coefficient_upper': str(up(phase_cubic)),
            'phase_rate_over_omega_upper': str(up(rate_coefficient)),
            'proved_constants': {'amplitude_coefficient': '3/2', 'endpoint_f_difference': '2/5', 'phase_cubic': '10', 'phase_rate': '2'},
            'endpoint_cell_records': summaries}
