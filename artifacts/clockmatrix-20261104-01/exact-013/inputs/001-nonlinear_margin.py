"""Rational checks for a finite nonlinear preparation margin."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from near_threshold import run as check_near_threshold


def run():
    prior = check_near_threshold()
    upper = F(prior['mu_window'][1])
    lower = F(prior['mu_star_open_bracket'][0])
    rho_max = upper/(2+upper)
    # Intra-half-period Euclidean logarithmic norm integrals.
    assert rho_max*(F(5,8)*F(22,7)+1) < F(9,4)
    assert rho_max*F(22,7)/4 < F(9,4)
    assert rho_max*F(3,4)*F(22,7) < 2
    x = F(9,4)
    exp_upper = sum(x**n/factorial(n) for n in range(17))
    exp_upper += x**17/factorial(17)/(1-x/18)
    assert exp_upper < 10
    assert F(11,4)**2 < 8

    # Uniform quadratic remainder on the tube around I=1.
    radius = F(1,1000)
    assert F(10,7)**2 > 2
    assert upper*(18*F(10,7)+6*radius) < 160

    # One native-time unit, using the finite number of half-returns.
    horizon = F(1)
    returns = 3
    assert (2+upper)*horizon < 3*returns  # pi > 3
    tangent_gain = 1+2*upper*horizon
    shear = F(prior['critical_shear_per_half_return'][1])
    discrete_gain = 1+shear*returns
    initial_gain = max(50,8*discrete_gain,tangent_gain)
    forcing_gain = max(500,64*discrete_gain,tangent_gain)
    assert (initial_gain,forcing_gain)==(50,500)
    epsilon = min(radius/(2*initial_gain),
                  1/(640*forcing_gain*initial_gain*horizon))
    error = F(4,3)*initial_gain*epsilon
    phase_tolerance = F(1,300000)
    assert 1-F(160)*forcing_gain*initial_gain*epsilon*horizon >= F(3,4)
    assert error < radius
    assert F(3,4)*error < phase_tolerance-phase_tolerance**3/6
    return {
        'evidence':'EXACT_CONDITIONAL',
        'mu_window_left_closed_right_open':[prior['mu_window'][0],str(lower)],
        'reference_action':'1',
        'native_horizon':str(horizon),
        'initial_linear_gain_bound':str(initial_gain),
        'two_time_linear_gain_bound':str(forcing_gain),
        'tube_radius':str(radius),
        'quadratic_remainder_bound':'160',
        'initial_error_budget':str(epsilon),
        'state_error_bound':str(error),
        'phase_error_strict_upper_rad':str(phase_tolerance),
        'physical_promotion':0,
    }


if __name__=='__main__':
    result = json.dumps(run(),indent=2)+'\n'
    Path(__file__).with_name('nonlinear_margin_results.json').write_text(result)
    print(result,end='')
