"""Dropout admission and wrapped endpoint identifiability controls."""
import cmath
import json
import math
from pathlib import Path

from interleaved_reference import CURVATURE, ERROR, SLOPE
from timestamp_reference import TAG_ERROR
from wrapped_reference import interpolate


def assess(left, right, r_left, r_right, allowance, pilot_angle):
    if left is None or right is None or not r_left < -TAG_ERROR < TAG_ERROR < r_right:
        return "missing_or_invalid_bracket", None
    right_weight = -r_left / (r_right - r_left)
    left_extent, right_extent = -r_left + TAG_ERROR, r_right + TAG_ERROR
    timing_error = (SLOPE * TAG_ERROR + CURVATURE / 2
                    * ((1 - right_weight) * left_extent**2 + right_weight * right_extent**2))
    if timing_error > allowance:
        return "timing_budget_exceeded", timing_error
    step_cap = (SLOPE * (left_extent + right_extent)
                + CURVATURE / 2 * (left_extent**2 + right_extent**2) + 2 * pilot_angle)
    try:
        estimate = interpolate(left, right, r_left, r_right, step_cap, TAG_ERROR)
    except ValueError:
        return "phase_increment_rejected", timing_error
    return "admitted", timing_error, estimate


def run(allowance, science):
    pilot_angle = math.asin(ERROR / (10 * science))
    rows = []
    for name, left, right, r_right in (
        ("nominal", 1, cmath.exp(0.01j), 1 / 4),
        ("drop_no_replacement", 1, None, 1 / 4),
        ("drop_near_replacement", 1, cmath.exp(0.02j), 3 / 4),
        ("drop_far_replacement", 1, cmath.exp(0.03j), 5 / 4),
        ("visible_excess_drift", 1, cmath.exp(0.1j), 1 / 4),
    ):
        rows.append((name, *assess(left, right, -1 / 4, r_right, allowance, pilot_angle)))
    assert [row[1] for row in rows] == [
        "admitted", "missing_or_invalid_bracket", "admitted",
        "timing_budget_exceeded", "phase_increment_rejected",
    ]
    hidden = assess(1, cmath.exp(1j * (0.01 + math.tau)), -1 / 4, 1 / 4,
                    allowance, pilot_angle)
    assert hidden[0] == "admitted"
    assert abs(hidden[2] - rows[0][-1]) < 1e-14
    midpoint_bias = (0.01 + math.tau) / 2 - hidden[2]
    assert abs(midpoint_bias - math.pi) < 1e-14
    return {"fault_controls": rows, "hidden_extra_turn_admission": hidden[0],
            "hidden_turn_midpoint_error_rad": midpoint_bias}


if __name__ == "__main__":
    directory = Path(__file__).parent
    prior = json.loads((directory / "interleaved_reference_results.json").read_text())[-1]
    calibration = json.loads((directory / "shared_reference_results.json").read_text())[-1]
    print(json.dumps(run(prior["per_detector_drift_allowance_rad"],
                         calibration["science_magnitude_floor"]), indent=2))
