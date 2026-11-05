"""Exact finite witnesses for the Q136/O09 and G06 carrier gates.

The universal claims are proved in README.md; these are reproducible checks.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def action(a, phase):
    return a * phase / 2


def main():
    # The phase variable is in units of an arbitrary fixed real angle.
    histories = [(F(1), F(2)), (F(2), F(2)), (F(3), F(-2))]
    amplitude_aware = []
    phase_only = []
    for a, phase in histories:
        i = action(a, phase)
        aware_sigma = (a * phase / 2, F(0), F(0))
        blind_sigma = (phase, F(0), F(0))
        assert sum(aware_sigma) == i
        amplitude_aware.append((i, sum(aware_sigma)))
        phase_only.append((i, sum(blind_sigma)))
    assert phase_only[0][1] == phase_only[1][1]
    assert phase_only[0][0] != phase_only[1][0]
    # A0=B0*a0^2/tau0; the native action and Q282 specific scale
    # are homogeneous of degree one in B0 and do not fix it.
    b, length, tick = F(3), F(2), F(5)
    a0 = b * length**2 / tick
    scaled = 7 * b * length**2 / tick
    assert scaled == 7 * a0
    assert scaled / 2 == 7 * (a0 / 2)
    # A projective Born readout of a scalar phase leaves rho unchanged;
    # this is the algebraic identity U rho U*=rho, checked by the proof.
    result = {
        "histories_a_phase": [[str(a), str(p)] for a, p in histories],
        "aware_action_and_Q136_sum": [[str(i), str(l)] for i, l in amplitude_aware],
        "phase_only_action_and_Q136_sum": [[str(i), str(l)] for i, l in phase_only],
        "phase_only_same_sum_different_action": True,
        "conditional_aware_kappa": "1",
        "conditional_fixed_support_phase_only_kappa": "a/2",
        "unit_rescaling": {"A0": str(a0), "A0_scaled": str(scaled), "factor": "7"},
        "source_selected_sigma_map": False,
        "independent_same_carrier_physical_anchor": False,
        "physical_promotion": 0,
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
