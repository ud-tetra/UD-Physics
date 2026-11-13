"""Outward-rounded direct propagator bounds and rational nonlinear gates."""
from fractions import Fraction as F
from pathlib import Path
import json

from stability_boundary import (
    BLOCKS, ONE, SCALE, STEPS, ZERO, fixed_pi, half_segment, mul, trig_tables,
)


def negate(interval):
    return -interval[1], -interval[0]


def inverse_det_one(matrix):
    a, b, c, d = matrix
    return d, negate(b), negate(c), a


def below_norm(matrix, cap):
    # Frobenius upper bound on the Euclidean operator norm.
    return sum(max(abs(lo),abs(hi))**2 for lo,hi in matrix) < (cap*SCALE)**2


def run():
    rho0 = F(31,41)
    mu_upper = F(77511,12500)
    rho_upper = mu_upper/(2+mu_upper)
    pi_lower, pi_upper = (F(x,SCALE) for x in fixed_pi())
    phase_end = F(21,8)*pi_upper
    assert F(21,8)*pi_lower > 2+mu_upper
    assert F(3,2)*rho_upper < F(6,5)
    assert F(6,5)*pi_upper/32 < F(1,8)
    step_gain = F(8,7)

    tables, dt = trig_tables()
    assert STEPS==16
    for block in BLOCKS:
        samples = [(ONE,ZERO,ZERO,ONE)]
        for k in range(84):
            table = tables[k%STEPS]
            if (k//STEPS)%2:
                table = [(negate(a),negate(b)) for a,b in table]
            local = half_segment(rho0,block,[table],dt)
            samples.append(mul(local,samples[-1]))
        inverses = [inverse_det_one(u) for u in samples]
        for i,u in enumerate(samples):
            assert below_norm(u,F(43,10))
            for v in inverses[:i+1]:
                assert below_norm(mul(u,v),F(11,2))

    initial_ref = F(43,10)*step_gain
    two_time_ref = F(11,2)*step_gain**2
    # Euclidean norm of J(B-Id) <= 5 follows from the block row sums.
    assert two_time_ref*5*(rho_upper-rho0)*phase_end < F(1,100)
    assert initial_ref*F(100,99) < 5
    assert two_time_ref*F(100,99) < 8
    assert 1+2*mu_upper < 14 and 1+mu_upper < 8

    phase_tolerance = F(1,300000)
    choices = {
        'isotropic':(F(1,3200000),F(1,3200000),F(1,200000)),
        'split':(F(1,8000000),F(1,120000),F(1,22000)),
    }
    certificates = {}
    for name,(tangent,normal,radius) in choices.items():
        assert radius < F(1,1000)
        feedback = 1280*radius**2
        tangent_error = 14*tangent+feedback
        normal_error = 5*normal+feedback
        assert tangent_error**2+normal_error**2<radius**2
        assert F(3,4)*tangent_error < phase_tolerance-phase_tolerance**3/6
        certificates[name] = {
            'tangent_initial_cap':str(tangent),
            'normal_initial_cap':str(normal),
            'state_tube_radius':str(radius),
            'tangent_error_cap':str(tangent_error),
            'normal_error_cap':str(normal_error),
        }
    return {
        'evidence':'EXACT_CONDITIONAL',
        'mu_interval':['31/5','77511/12500'],
        'native_horizon':'1',
        'normal_gain_phase_zero':'5',
        'normal_gain_two_time':'8',
        'phase_error_strict_upper_rad':str(phase_tolerance),
        'grid_nodes_per_block':85,
        'gate_options':certificates,
        'physical_promotion':0,
    }


if __name__=='__main__':
    result = json.dumps(run(),indent=2)+'\n'
    Path(__file__).with_name('anisotropic_margin_results.json').write_text(result)
    print(result,end='')
