"""Reconstruct scalar-lane transport from oriented incidence stock currents."""
import json
import numpy as np

from directional_packet import DIRECTIONS, dispersion
from isospectral_clock import replay


def bond_stock_flow(tail, head, edge):
    """Return the two signed vertex-to-edge Hasse currents."""
    return 2 * np.real(np.conj(tail) * edge), -2 * np.real(np.conj(head) * edge)


def currents(k, omega):
    vector = [0, 0, 0]
    for displacement in DIRECTIONS:
        head = np.exp(1j * sum(a * b for a, b in zip(k, displacement)))
        edge = -1j * (head - 1) / omega
        tail_flow, head_flow = bond_stock_flow(1, head, edge)
        for j, step in enumerate(displacement):
            # Half-edge displacement and total mode stock two.
            vector[j] += step * (tail_flow - head_flow) / 4
    return vector


def probe(k, probability):
    omega, group = dispersion(k)
    current = currents(k, omega)
    difference = max(float(np.max(abs(a - b))) for a, b in zip(current, group))
    assert difference < 1e-12
    reversed_current = currents(tuple(-axis for axis in k), omega)
    assert max(float(np.max(abs(a + b))) for a, b in zip(current, reversed_current)) < 1e-12
    mean = np.array([np.sum(probability * a) for a in current])
    speed = np.sqrt(np.dot(mean, mean) / 2 - mean.sum()**2 / 8)
    return {"normalized_current": mean.tolist(), "current_norm": float(speed),
            "max_current_minus_group_component": difference}


def run():
    controls = []
    for parity in ((1, 0, 0), (1, 1, 1)):
        flows = []
        for displacement in DIRECTIONS:
            head = (-1)**sum(a * b for a, b in zip(parity, displacement))
            flows.extend(bond_stock_flow(1, head, -1j * (head - 1) / 4))
        assert all(flow == 0 for flow in flows)
        controls.append({"pi_character": parity, "zero_incidence_currents": len(flows)})
    rows = [replay(order, probe) for order in (8, 16)]
    for row in rows:
        assert row["diagonal"]["probe"]["current_norm"] - row["axis"]["probe"]["current_norm"] > 0.14
    return {"zero_speed_controls": controls, "quadrature": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
