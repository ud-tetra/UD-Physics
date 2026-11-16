"""Generate and check the AW5 short-window digitization fixture."""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "aw5-hollow-star-intake"))
from intake_score import LIMITS, N, ROLES, blind_score, digest

SPAN = 4
MIN_CODE_VOLTAGE = -2
NOISE = Q(1, 2240)
GAP = Q(1, 280)


def budget(bits):
    return Q(SPAN, 2**bits) + 2 * NOISE <= GAP / 2


def quantize(value, bits):
    step = Q(SPAN, 2**bits)
    assert MIN_CODE_VOLTAGE <= value < MIN_CODE_VOLTAGE + SPAN
    index = round((value - MIN_CODE_VOLTAGE) / step)
    assert 0 <= index < 2**bits
    return MIN_CODE_VOLTAGE + index * step


def main():
    # At s=1 the common part of the sixth-order polynomial vanishes.
    hollow = -Q(1, 15) - Q(1, 210)
    filled = -Q(1, 12) + Q(1, 120)
    assert hollow - filled == GAP
    assert not budget(12) and budget(13)
    observed = quantize(hollow - NOISE, 13) - quantize(filled + NOISE, 13)
    assert observed >= GAP / 2

    reveal = {"nonce": "short-window-timing-negative-fixture", "roles": dict(zip(ROLES, "abc"))}
    times = [str(Q(k + 1, N)) for k in range(N)]
    packet = {
        "protocol": "AW5-ACQUISITION-v1",
        "evidence_mode": "SYNTHETIC",
        "role_commitment": digest(reveal),
        "centered_subgaussian": True,
        "independent_across_traces_and_samples": True,
        "traces": {
            key: {"times": times, "values": [0] * N,
                  "bounds": dict.fromkeys(LIMITS, 0) | {"dissipative": True}}
            for key in "abc"
        },
    }
    rejection = blind_score(packet)
    assert rejection["status"] == "INADMISSIBLE" and "timing gate" in rejection["reason"]
    print(json.dumps({
        "scope": "SYNTHETIC_BOUND_STRESS_ONLY",
        "native_time": "1", "certified_gap": str(GAP),
        "threshold": str(GAP / 2), "normalized_span": SPAN,
        "absolute_error_per_trace": str(NOISE),
        "adverse_analog_pair": [str(hollow), str(filled)],
        "minimum_bits_for_declared_budget": 13,
        "bit_budget_pass": {"12": budget(12), "13": budget(13)},
        "quantized_adverse_gap": str(observed),
        "frozen_grid_guard": rejection["status"],
        "frozen_grid_guard_reason": rejection["reason"],
        "physical_promotion": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
