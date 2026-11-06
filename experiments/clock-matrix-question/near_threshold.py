"""Replay rational coefficient and gain margins near the certified first loss."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from stability_boundary import BLOCKS, bernstein_weights, enclose, half_segment, trig_tables


def run():
    left, right = F(31,5), F(621,100)
    rho = lambda mu: mu/(2+mu)
    start, end = rho(left), rho(right)
    width = end-start
    n = 8
    weights = bernstein_weights(n)
    derivative_cap = lambda k: 1024*F(55,7)**k/factorial(k)
    error = derivative_cap(n)*width**n
    derivative_error = (n*derivative_cap(n)*width**(n-1)
                        +derivative_cap(n+1)*width**n)
    slope_weights = [[(n-1)*(b-a)/width for a,b in zip(weights[k],weights[k+1])]
                     for k in range(n-1)]
    tables, dt = trig_tables()
    # Bounds on the entries of H in row-major order.
    boxes = (
        ((F(-4,3),F(-13,10)), (F(-13,10),F(-6,5)),
         (F(7,10),F(3,4)), (F(-3,40),F(-7,100))),
        ((F(17,20),F(7,8)), (F(-3,8),F(-7,20)),
         (F(9,10),F(19,20)), (F(3,4),F(4,5))),
        ((F(-1,1000),F(1,1000)), (F(-83,50),F(-33,20)),
         (F(3,5),F(5,8)), (F(-18,125),F(-143,1000))),
    )
    for block, expected in zip(BLOCKS, boxes):
        nodes = [half_segment(start+width*F(k,n-1),block,tables,dt) for k in range(n)]
        for j,(lo,hi) in enumerate(expected):
            coeffs = enclose([u[j] for u in nodes],weights)
            assert lo < min(a for a,b in coeffs)-error
            assert max(b for a,b in coeffs)+error < hi
    slope = enclose([u[0] for u in nodes],slope_weights)
    assert F(11,20) < min(a for a,b in slope)-derivative_error
    assert max(b for a,b in slope)+derivative_error < F(14,25)
    assert F(1,34)<2/(2+right)**2<2/(2+left)**2<F(1,33)

    # Verify the two noncritical blocks have sampled gain < 5.
    for a,b,c,d in boxes[:2]:
        ad_lower = min(x*y for x in a for y in d)
        minus_bc_lower = min(-x*y for x in b for y in c)
        off_upper = 2*max(abs(x*y) for x1,y1 in [(b,d),(a,c)] for x in x1 for y in y1)
        assert ad_lower>0 and minus_bc_lower>0
        assert off_upper**2<16*4*ad_lower*minus_bc_lower

    delta_max = right-left
    k_lo = F(11,20)*F(1,34)*F(143,1000)
    k_hi = F(14,25)*F(1,33)*F(18,125)
    B_lo,B_hi = F(47,100),F(12,25)
    _,b,c,d = boxes[-1]
    assert B_lo < 2*b[1]*d[1] < 2*b[0]*d[0] < B_hi
    assert 2*F(14,25)*F(1,33)*delta_max*c[1]<B_lo
    assert delta_max==F(1,100)
    assert B_lo**2>4*k_hi*F(47,10)**2
    assert B_hi**2<4*k_lo*(1-k_hi*delta_max)*(F(51,10)-F(1,10))**2
    assert 5**2*delta_max<F(47,10)**2

    # Intra-period gains from the Euclidean logarithmic norm.
    assert F(3,2)*end*F(22,7)<4 and F(11,4)**4<64
    assert F(3,4)*end*F(22,7)<2 and F(11,4)**2<8
    assert 64*5*F(1,10)<41 and 8*F(51,10)<41

    log_lo,log_hi = F(12,125),F(1,10)
    assert log_lo**2<4*k_lo/(1+k_hi*delta_max)
    assert 4*k_hi<log_hi**2
    assert F(1,4)<log_lo*(2+left)/F(22,7)
    assert log_hi*(2+right)/F(31,10)<F(27,100)
    return {
        'evidence':'EXACT_CONDITIONAL',
        'mu_window':[str(left),str(right)],
        'mu_star_open_bracket':['77511/12500','62009/10000'],
        'a_derivative_rho':[str(F(11,20)),str(F(14,25))],
        'abs_ad_over_distance':[str(k_lo),str(k_hi)],
        'critical_shear_per_half_return':[str(B_lo),str(B_hi)],
        'sampled_gain_times_sqrt_distance':['47/10','51/10'],
        'continuous_gain_times_sqrt_distance':['47/10','41'],
        'expanding_log_multiplier_over_sqrt_distance':[str(log_lo),str(log_hi)],
        'native_exponent_over_sqrt_distance':['1/4','27/100'],
        'physical_promotion':0,
    }


if __name__=='__main__':
    result = json.dumps(run(),indent=2)+'\n'
    Path(__file__).with_name('near_threshold_results.json').write_text(result)
    print(result,end='')
