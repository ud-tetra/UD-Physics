"""Synthetic packet builder and formal intake regression replay."""
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import tempfile

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


def check_timing_boundary(nominal):
    packet = deepcopy(nominal)
    packet["timing"]["uncertainty_ms"] = 0
    packet["timing"]["midpoint_times_ms"][-1] = "LAST_MIDPOINT"
    raw = json.dumps(packet)
    scorer = Path(__file__).with_name("bench_pair_intake.py")
    cases = (
        ("decimal just below", "31.9384765624999999999", True),
        ("exact timing limit", "31.9384765625", True),
        ("decimal just above", "31.9384765625000000001", False),
        ("rounded 0.977 microseconds", "31.938477", False),
    )
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory)/"packet.json"
        for label, timestamp, expected in cases:
            path.write_text(raw.replace('"LAST_MIDPOINT"', timestamp), encoding="utf-8")
            receipt = json.loads(subprocess.check_output([sys.executable, scorer, path]))
            assert receipt["gates"]["timing_loopback"] is expected, receipt
            assert Fraction(receipt["loopback_error_ms_exact"]) == Fraction(timestamp) - Fraction(511, 16)
            print(f"{label}: {receipt['status']}")


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
    check_timing_boundary(nominal)
