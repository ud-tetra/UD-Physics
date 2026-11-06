"""Distinguish equal-frequency packets using the longer incidence edges."""
from fractions import Fraction as F
import json
import numpy as np

from directional_packet import DIRECTIONS
from isospectral_clock import replay


LONG_EDGES = [d for d in DIRECTIONS if sum(d) == 2]


def probe(k, probability):
    symbol = sum(2 * (1 - np.cos(sum(a * b for a, b in zip(k, d))))
                 for d in LONG_EDGES)
    contrast = np.sum(probability * np.exp(2j * symbol * 12 / 128))
    return {
        "mean_long_edge_symbol": float(np.sum(probability * symbol)),
        "phase_residual_at_12_rad": float(np.angle(contrast) / 2),
        "contrast_at_12": float(abs(contrast)),
    }


def run():
    a = 4 * (1 - F(-93, 125))
    d = 6 * (1 - (2 * F(3, 5)**2 - 1))
    assert d - a == F(88, 125)
    central_split = (d - a) * 12 / 128
    assert central_split == F(33, 500)
    # At pi-sign characters every sine vanishes, so both group velocities are zero.
    stationary = []
    for parity in ((1, 0, 0), (1, 1, 1)):
        def laplacian(directions):
            return 4 * sum(sum(a * b for a, b in zip(parity, d)) % 2
                           for d in directions)

        stationary.append((laplacian(DIRECTIONS), laplacian(LONG_EDGES)))
    assert stationary == [(16, 8), (16, 0)]
    rows = [replay(order, probe) for order in (8, 16)]
    for row in rows:
        row["packet_phase_split_at_12_rad"] = (
            row["diagonal"]["probe"]["phase_residual_at_12_rad"]
            - row["axis"]["probe"]["phase_residual_at_12_rad"]
        )
        assert 0.065 < row["packet_phase_split_at_12_rad"] < 0.067
    return {"central_long_edge_symbols": [str(a), str(d)],
            "central_phase_split_at_12_rad": str(central_split),
            "stationary_frequency_squared_and_symbol": stationary, "quadrature": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
