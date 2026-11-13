"""Tracked detector aperture sweep and deterministic phasor-error budget."""
import json
import math

from tracked_current_clock import matched_probe


RADII = (3, 6, 12)


def replay(order, step):
    matched = matched_probe(order, step, RADII)
    rows = []
    for index, radius in enumerate(RADII):
        a = matched["axis"][-1]["ports"][index]
        d = matched["diagonal"][-1]["ports"][index]
        split = d["phase_rad"] - a["phase_rad"]
        assert 0 < split < math.pi / 2
        fraction = math.sin(split / 4)
        rows.append({
            "radius": radius, "axis": a, "diagonal": d, "split_rad": split,
            "error_over_window_stock_each": fraction * min(a["contrast"], d["contrast"]),
            "error_over_total_stock_each": fraction * min(
                port["contrast"] * port["stock_fraction"] for port in (a, d)),
        })
    assert all(a["error_over_total_stock_each"] < b["error_over_total_stock_each"]
               for a, b in zip(rows, rows[1:]))
    return {"order": order, "step": step, "rows": rows}


if __name__ == "__main__":
    print(json.dumps([replay(8, 1 / 4), replay(12, 1 / 8)], indent=2))
