"""Science-time pilot consistency and half-gap replay."""
import cmath
import json
import math
from pathlib import Path

from interleaved_reference import ERROR
from pilot_faults import assess
from shared_reference import tangent


def run(alignment, timing, calibration):
    gap = alignment["minimum_offset_gap_rad"]
    target = alignment["nominal_gap_rad"] / 2
    allowance = timing["per_detector_drift_allowance_rad"]
    science = calibration["science_magnitude_floor"]
    pilot = 10 * science
    alpha = math.asin(ERROR / pilot)
    admitted = assess(1, cmath.exp(0.01j), -1 / 4, 1 / 4, allowance, alpha)
    assert admitted[0] == "admitted"
    _, timing_cap, bracket_phase = admitted

    mismatch = 1 / 1000
    consistency_cap = timing_cap + mismatch + 2 * alpha
    checks = {}
    for name, phase in (("nominal", 1 / 200), ("hidden_turn", 1 / 200 + math.pi)):
        distances = []
        for sign in (-1, 1):
            monitor = tangent(pilot * cmath.exp(1j * (phase + sign * mismatch)), ERROR, sign)
            distances.append(abs(cmath.phase(monitor * cmath.exp(-1j * bracket_phase))))
        checks[name] = {"min_distance_rad": min(distances), "max_distance_rad": max(distances)}
    assert checks["nominal"]["max_distance_rad"] <= consistency_cap
    assert checks["hidden_turn"]["min_distance_rad"] > consistency_cap

    cases = []
    for mismatch in (0, 1 / 1000, 1 / 500):
        for hidden in (False, True):
            estimates = []
            for phase, sign in ((0, 1), (gap, -1)):
                drift = 1 / 200 + (math.pi if hidden and sign == -1 else 0)
                signal = tangent(science * cmath.exp(1j * (phase + drift)), ERROR, sign)
                monitor = tangent(pilot * cmath.exp(1j * (drift - sign * mismatch)), ERROR, -sign)
                estimates.append(signal / monitor)
            observed_gap = cmath.phase(estimates[1] * estimates[0].conjugate())
            expected = gap - 2 * (mismatch + math.asin(ERROR / science) + alpha)
            assert abs(observed_gap - expected) < 1e-14
            assert (observed_gap >= target) == (mismatch <= allowance)
            cases.append({"mismatch_each_rad": mismatch, "hidden_turn": hidden,
                          "worst_gap_rad": observed_gap, "half_gap_pass": observed_gap >= target})
    return {"consistency_cap_rad": consistency_cap, "monitor_checks": checks,
            "maximum_mismatch_each_rad": allowance, "target_half_gap_rad": target,
            "direct_reference_controls": cases}


if __name__ == "__main__":
    directory = Path(__file__).parent
    inputs = [json.loads((directory / f"{name}_results.json").read_text())[-1]
              for name in ("clock_alignment", "interleaved_reference", "shared_reference")]
    print(json.dumps(run(*inputs), indent=2))
