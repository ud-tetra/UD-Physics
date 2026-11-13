"""Wrapped pilot interpolation with explicit cycle ambiguity rejection."""
import cmath
from itertools import product
import json
import math
from pathlib import Path

from interleaved_reference import CURVATURE, ERROR, SLOPE
from timestamp_reference import JITTER, TAG_ERROR


def interpolate(left, right, r_left, r_right, cap, tag_cap=0):
    if not (r_left < -tag_cap <= tag_cap < r_right) or min(abs(left), abs(right)) == 0:
        raise ValueError("Invalid bracket or pilot")
    step = cmath.phase(right * left.conjugate())
    if abs(step) > cap or math.tau - abs(step) <= cap:
        raise ValueError("Inconsistent or ambiguous phase lift")
    right_weight = -r_left / (r_right - r_left)
    return cmath.phase(left) + right_weight * step


def run(science):
    pilot_angle = math.asin(ERROR / (10 * science))
    max_cap = max_error = raw_error = 0.0
    checks = 0
    for h, slope, curvature, j_l, j_r, e_l, e_r, n_l, n_r in product(
            (1 / 4, 9 / 20), (-SLOPE, SLOPE), (-CURVATURE, CURVATURE),
            (-JITTER, JITTER), (-JITTER, JITTER), (-TAG_ERROR, TAG_ERROR),
            (-TAG_ERROR, TAG_ERROR), (-pilot_angle, pilot_angle), (-pilot_angle, pilot_angle)):
        t_l, t_r = -h + j_l, h + j_r
        r_l, r_r = t_l + e_l, t_r + e_r
        cap = (SLOPE * (r_r - r_l + 2 * TAG_ERROR) + CURVATURE / 2
               * ((abs(r_l) + TAG_ERROR)**2 + (abs(r_r) + TAG_ERROR)**2)
               + 2 * pilot_angle)
        p_l = math.pi + slope * t_l + curvature * t_l**2 / 2 + n_l
        p_r = math.pi + slope * t_r + curvature * t_r**2 / 2 + n_r
        left, right = cmath.exp(1j * p_l), cmath.exp(1j * p_r)
        weight = -r_l / (r_r - r_l)
        expected = (1 - weight) * p_l + weight * p_r
        estimate = interpolate(left, right, r_l, r_r, cap, TAG_ERROR)
        error = abs(cmath.phase(cmath.exp(1j * (estimate - expected))))
        raw = (1 - weight) * cmath.phase(left) + weight * cmath.phase(right)
        raw_error = max(raw_error, abs(cmath.phase(cmath.exp(1j * (raw - expected)))))
        max_error = max(max_error, error)
        max_cap = max(max_cap, cap)
        checks += 1
    assert max_error < 1e-14 and max_cap < math.pi and raw_error > 3
    # Distinct admissible endpoint increments with identical pilot phasors.
    lifted = (3 * math.pi / 4, -5 * math.pi / 4)
    assert abs(cmath.exp(1j * lifted[0]) - cmath.exp(1j * lifted[1])) < 1e-14
    right = cmath.exp(1j * lifted[0])
    try:
        interpolate(1, right, -1, 1, 3 * math.pi / 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Ambiguous phase passed")
    assert abs((lifted[0] - lifted[1]) / 2 - math.pi) < 1e-14
    return {"wrapped_bracket_checks": checks, "maximum_pilot_step_cap_rad": max_cap,
            "maximum_lift_error_rad": max_error, "maximum_raw_average_error_rad": raw_error,
            "ambiguous_midpoint_gap_rad": math.pi}


if __name__ == "__main__":
    prior = json.loads(Path(__file__).with_name("shared_reference_results.json").read_text())
    print(json.dumps(run(prior[-1]["science_magnitude_floor"]), indent=2))
