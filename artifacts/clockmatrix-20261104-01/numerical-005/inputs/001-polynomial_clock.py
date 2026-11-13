"""Replay the local polynomial current clock at common launch stock."""
from fractions import Fraction
import json

from tracked_current_clock import matched_probe


AMPLITUDES = (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))
LAUNCH_STOCK = 10**8


def run():
    reports = []
    for order, step in ((8, 1 / 4), (12, 1 / 8)):
        data = matched_probe(order, step, (12,), polynomial_stock=LAUNCH_STOCK,
                             phase_factors=tuple(float(a**4) for a in AMPLITUDES))
        rows = []
        for amplitude, axis, diagonal in zip(
                AMPLITUDES, data["axis"][-1]["ports"], data["diagonal"][-1]["ports"], strict=True):
            split = diagonal["phase_rad"] - axis["phase_rad"]
            rows.append({"amplitude": str(amplitude), "axis": axis, "diagonal": diagonal,
                         "diagonal_minus_axis_rad": split,
                         "split_over_amplitude_fourth_rad": split / float(amplitude**4)})
        reports.append({"order": order, "step": step, "rows": rows})
    return {"launch_stock_at_unit_amplitude": LAUNCH_STOCK, "replays": reports}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
