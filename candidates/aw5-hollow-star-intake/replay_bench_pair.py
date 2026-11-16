"""Synthetic packet builder and formal intake regression replay."""
from copy import deepcopy

import numpy as np
from scipy.linalg import expm

from bench_pair_intake import H, TARGET, assess


def fixture():
    G = TARGET-np.eye(2)/32768
    M = expm(H*G)
    bias = np.array([1/100, -1/100])
    shots = {}
    for i, axis in enumerate(np.eye(2), 1):
        for sign, polarity in (("+", 1), ("-", -1)):
            start = axis*polarity
            shots[f"{sign}e{i}"] = [start.tolist(), (M@start+bias).tolist()]
    heldout = []
    for time, state in ((32, (0.4, -0.3)), (8, (-0.2, -0.1))):
        start = np.array(state)
        heldout.append({"time_native": time, "start": start.tolist(),
                        "end": (expm(time*G)@start).tolist(), "start_error": 2**-23,
                        "end_error": 2**-23, "numerical_allowance": 1e-10})
    return {
        "protocol": "AW5-PAIR-v1", "evidence": "SYNTHETIC", "shots": shots,
        "certificate": {
            "clock_reference": "synthetic shared clock", "endpoint_uncertainty": "synthetic bounds",
            "lti_scope": "synthetic constant generator",
            "loss_model": "synthetic common bleed plus face loss",
            "generator_norm_upper": 1.5, "delta_x": 2**-23, "delta_y": 2**-23,
            "map_numerical_allowance": 1e-12, "generator_numerical_allowance": 1e-10},
        "timing": {"midpoint_times_ms": ((np.arange(256)+0.5)/8).tolist(),
                   "uncertainty_ms": 2**-12},
        "heldout": heldout,
    }


def check(name, packet, expected, gate=None):
    result = assess(packet)
    assert result["status"] == expected, result
    if gate:
        assert not result["gates"][gate], result
    print(f"{name}: {expected}")


if __name__ == "__main__":
    nominal = fixture()
    check("nominal signed shots and held-out response", nominal, "PASS_CONDITIONAL")
    for gate in ("timing_loopback", "heldout"):
        bad = deepcopy(nominal)
        if gate == "timing_loopback":
            bad["timing"]["midpoint_times_ms"][-1] += 1/512
        else:
            bad["heldout"][0]["end"][0] += 1/100
        check(gate, bad, "FAIL_GATES", gate)
    bad = deepcopy(nominal)
    del bad["certificate"]["endpoint_uncertainty"]
    check("missing uncertainty reference", bad, "INADMISSIBLE")
    bad = deepcopy(nominal)
    bad["shots"]["+e2"], bad["shots"]["-e2"] = bad["shots"]["+e1"], bad["shots"]["-e1"]
    check("rank-deficient injection", bad, "INADMISSIBLE")
