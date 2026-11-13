"""Timestamp-weighted pilot interpolation with separate jitter and tag errors."""
from itertools import product
import json
import math
from pathlib import Path

from interleaved_reference import CURVATURE, SLOPE


JITTER = 1 / 20
TAG_ERROR = 1 / 100


def phase_error(half_spacing, jitter, tags, slope, curvature):
    left, right = -half_spacing + jitter[0], half_spacing + jitter[1]
    reported_left, reported_right = left + tags[0], right + tags[1]
    if not (left < 0 < right and reported_left < 0 < reported_right):
        raise ValueError("Both true and reported pilot times must bracket the science time")
    weight = reported_right / (reported_right - reported_left)
    return (slope * (weight * left + (1 - weight) * right)
            + curvature * (weight * left**2 + (1 - weight) * right**2) / 2)


def bound(h, eta):
    return SLOPE * eta + CURVATURE * ((h + JITTER)**2 + 2 * JITTER * eta) / 2


def replay(allowance):
    cases = []
    for eta in (0, TAG_ERROR):
        limit = math.sqrt(2 * (allowance - SLOPE * eta) / CURVATURE
                          - 2 * JITTER * eta) - JITTER
        trials = []
        for h in (1 / 4, 1 / 2):
            corners = product((-JITTER, JITTER), (-JITTER, JITTER),
                              (-eta, eta), (-eta, eta),
                              (-SLOPE, SLOPE), (-CURVATURE, CURVATURE))
            errors = [abs(phase_error(h, (a, b), (c, d), m, q))
                      for a, b, c, d, m, q in corners]
            assert max(errors) <= bound(h, eta) + 1e-15
            linear_only = max(abs(phase_error(h, j, e, SLOPE, 0))
                              for j in product((-JITTER, JITTER), repeat=2)
                              for e in product((-eta, eta), repeat=2))
            assert abs(linear_only - SLOPE * eta) < 1e-15
            trials.append({"half_spacing": h, "linear_only_max_rad": linear_only,
                           "quadratic_corner_max_rad": max(errors),
                           "certified_error_bound_rad": bound(h, eta),
                           "half_gap_guaranteed": bound(h, eta) <= allowance})
        assert trials[0]["half_gap_guaranteed"]
        assert trials[1]["half_gap_guaranteed"] == (eta == 0)
        cases.append({"timestamp_error_cap": eta, "maximum_sufficient_half_spacing": limit,
                      "trials": trials})
    try:
        phase_error(1 / 25, (JITTER, 0), (0, 0), SLOPE, CURVATURE)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid bracket accepted")
    return cases


if __name__ == "__main__":
    prior = json.loads(Path(__file__).with_name("interleaved_reference_results.json").read_text())
    print(json.dumps([{"order": row["order"], "cases": replay(row["per_detector_drift_allowance_rad"])}
                      for row in prior], indent=2))
