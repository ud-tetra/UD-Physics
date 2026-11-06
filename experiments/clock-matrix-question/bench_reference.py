"""Exact-rational arithmetic gate for the proposed simultaneous-reference bench."""
from dataclasses import dataclass, replace
from fractions import Fraction as F
import json


@dataclass(frozen=True)
class ChannelBounds:
    science_floor: F
    pilot_floor: F
    science_error: F
    pilot_error: F
    path_phase: F
    drift_rate: F
    time_skew: F

    def phase_bound(self):
        if (min(self.science_floor, self.pilot_floor) <= 0
                or min(self.science_error, self.pilot_error, self.path_phase,
                       self.drift_rate, self.time_skew) < 0
                or self.science_error >= self.science_floor
                or self.pilot_error >= self.pilot_floor):
            raise ValueError("Invalid channel envelope")
        return (self.path_phase + self.drift_rate * self.time_skew
                + self.science_error / (self.science_floor - self.science_error)
                + self.pilot_error / (self.pilot_floor - self.pilot_error))


def evaluate(gap_floor, target, channels):
    if not 0 < target <= gap_floor or len(channels) != 2:
        raise ValueError("Invalid differential acceptance criterion")
    residual = gap_floor - sum(channel.phase_bound() for channel in channels)
    return {"gap_lower_bound_rad": str(residual), "gap_lower_bound_decimal_rad": float(residual),
            "arithmetic_pass": residual >= target}


def replay():
    gap_floor, target = F(11779967, 10**9), F(5889984, 10**9)
    base = ChannelBounds(F(19444, 10**9), F(194440, 10**9), F(1, 40000000),
                         F(1, 40000000), F(1, 1000), F(1, 50), F(0))
    skew_cap = ((gap_floor - target) / 2 - base.phase_bound()) / base.drift_rate
    cases = {
        "aligned": (base, base),
        "both_skew_1_over_50": (replace(base, time_skew=F(1, 50)),) * 2,
        "both_skew_3_over_100": (replace(base, time_skew=F(3, 100)),) * 2,
        "one_channel_weak_pilot": (base, replace(base, pilot_floor=base.science_floor / 4)),
    }
    results = {label: evaluate(gap_floor, target, pair) for label, pair in cases.items()}
    assert [r["arithmetic_pass"] for r in results.values()] == [True, True, False, False]
    try:
        evaluate(gap_floor, target, (base, replace(base, pilot_floor=base.pilot_error)))
    except ValueError:
        pass
    else:
        raise AssertionError("Pilot floor equal to error was accepted")
    return {"status": "SYNTHETIC_ONLY", "symmetric_skew_cap_native": str(skew_cap),
            "symmetric_skew_cap_native_decimal": float(skew_cap), "controls": results}


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2))
