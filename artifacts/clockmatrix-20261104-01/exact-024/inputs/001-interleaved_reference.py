"""Deterministic timing budgets and sharp synthetic drift controls."""
import cmath
import json
import math
from pathlib import Path

from shared_reference import tangent


SLOPE, CURVATURE, SKEW = 1 / 50, 1 / 100, 1 / 100
ERROR = 1 / 40_000_000


def replay(alignment, calibration):
    gap = alignment["minimum_offset_gap_rad"]
    target = alignment["nominal_gap_rad"] / 2
    science = calibration["science_magnitude_floor"]
    pilot = 10 * science
    angular_noise = math.asin(ERROR / science) + math.asin(ERROR / pilot)
    drift_allowance = (gap - target) / 2 - angular_noise
    assert drift_allowance > SLOPE * SKEW + CURVATURE * SKEW**2 / 2
    delayed_limit = 2 * drift_allowance / (
        SLOPE + math.sqrt(SLOPE**2 + 2 * CURVATURE * drift_allowance)) - SKEW
    bracket_limit = math.sqrt(
        2 * (drift_allowance - SLOPE * SKEW) / CURVATURE - SKEW**2)

    def trial(delay, bracket):
        times = (SKEW - delay, SKEW + delay) if bracket else (SKEW + delay,)
        measured = []
        for phase, sign in ((0, 1), (gap, -1)):
            # Independent opposite drift trajectories attain the differential bound.
            def drift(time):
                return -sign * (SLOPE * time + CURVATURE * time**2 / 2)

            signal = tangent(science * cmath.exp(1j * phase), ERROR, sign)
            references = [tangent(pilot * cmath.exp(1j * (0.73 + drift(t))),
                                  ERROR, -sign) for t in times]
            measured.append(cmath.phase(signal) - sum(map(cmath.phase, references)) / len(times))
        observed_gap = measured[1] - measured[0]
        penalty = (SLOPE * SKEW + CURVATURE * (delay**2 + SKEW**2) / 2 if bracket
                   else SLOPE * (delay + SKEW) + CURVATURE * (delay + SKEW)**2 / 2)
        assert abs(observed_gap - (gap - 2 * (penalty + angular_noise))) < 1e-14
        return {"bracket": bracket, "nominal_delay": delay, "worst_gap_rad": observed_gap,
                "retains_half_nominal": observed_gap >= target}

    trials = [trial(delay, bracket) for delay in (1 / 20, 1 / 4, 3 / 5)
              for bracket in (False, True)]
    assert [t["retains_half_nominal"] for t in trials] == [True, True, False, True, False, False]
    return {"order": alignment["order"], "target_gap_rad": target,
            "per_detector_drift_allowance_rad": drift_allowance,
            "maximum_nominal_one_sided_delay": delayed_limit,
            "maximum_bracket_half_spacing": bracket_limit, "trials": trials}


if __name__ == "__main__":
    directory = Path(__file__).parent
    alignment, calibration = [json.loads((directory / f"{name}_results.json").read_text())
                              for name in ("clock_alignment", "shared_reference")]
    print(json.dumps([replay(a, b) for a, b in zip(alignment, calibration, strict=True)], indent=2))
