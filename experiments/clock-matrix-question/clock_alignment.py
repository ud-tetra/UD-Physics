"""Terminal aperture displacement sweep and complex gain controls."""
from itertools import product
import json
import numpy as np

from tracked_current_clock import matched_probe


def run():
    offsets = [(0, 0, 0)] + [offset for offset in product(range(-2, 3), repeat=3)
                             if any(offset)]
    reports = []
    for order, step in ((8, 1 / 4), (12, 1 / 8)):
        data = matched_probe(order, step, (12,), offsets)
        axis, diagonal = (data[key][-1]["ports"] for key in ("axis", "diagonal"))
        nominal = diagonal[0]["phase_rad"] - axis[0]["phase_rad"]
        low = min(diagonal, key=lambda p: p["phase_rad"])["phase_rad"] - max(
            axis, key=lambda p: p["phase_rad"])["phase_rad"]
        assert low > nominal / 2
        trials = []
        for cap in (0, 1 / 400, 1 / 160):
            measured = []
            for ports, sign in ((axis, 1), (diagonal, -1)):
                observed = []
                for p, amplitude in product(ports, (9 / 10, 11 / 10)):
                    signal = p["stock_fraction"] * p["contrast"] * np.exp(1j * p["phase_rad"])
                    observed.append(amplitude * np.exp(1j * sign * cap) * signal)
                measured.append(observed)
            gap = min(np.angle(measured[1])) - max(np.angle(measured[0]))
            assert abs(gap - (low - 2 * cap)) < 1e-14
            minimum_signal = min(min(abs(v) for v in channel) for channel in measured)
            spare = max(0, gap - nominal / 2)
            trials.append({"phase_cap_each_rad": cap, "worst_gap_rad": float(gap),
                           "retains_half_nominal": bool(gap >= nominal / 2),
                           "common_additive_budget_per_total_stock": float(
                               minimum_signal * np.sin(spare / 2))})
        assert trials[1]["retains_half_nominal"] and trials[2]["worst_gap_rad"] < 0
        reports.append({"order": order, "step": step, "offsets_per_channel": len(offsets),
                        "nominal_gap_rad": nominal, "minimum_offset_gap_rad": low,
                        "offset_margin_consumed_rad": nominal - low,
                        "min_stock_fraction": min(p["stock_fraction"] for p in axis + diagonal),
                        "gain_trials": trials})
    return reports


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
