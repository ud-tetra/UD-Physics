"""Exact rational witnesses for conditional source zero and loss-slope freedom.

The general proof is in README.md. This script checks a finite, passive
two-coordinate example without importing physical graphite parameters.
"""

import json
from fractions import Fraction as Q


def run():
    # Arbitrary positive stiffness and loss, unit lateral/internal coupling.
    k = (Q(2), Q(3))
    d0 = (Q(5), Q(7))
    gamma0 = tuple(d / (ki * ki) for d, ki in zip(d0, k))
    assert gamma0 == (Q(5, 4), Q(7, 9))

    # D_s(P) = exp(s(P-P0)) D0; at P0 the derivative of Gamma is s Gamma0.
    slopes = {}
    for s in (Q(-2), Q(0), Q(3)):
        derivative = tuple(s * g for g in gamma0)
        slopes[str(s)] = [str(x) for x in derivative]
    assert slopes["-2"] == ["-5/2", "-14/9"]
    assert slopes["3"] == ["15/4", "7/3"]

    # If C = kappa_current * C_tilde with kappa_current=0, Gamma=0.
    current_source = Q(0)
    assert all(current_source * current_source * g == 0 for g in gamma0)
    return {
        "status": "PASS_EXACT_NATIVE_SOURCE_GATE_WITNESS",
        "ledger_scope": "Q22 zero current; Q23-Q26 source open; Q76-Q84 dimensionless phase maps conditional",
        "kappa_current": "0",
        "conditional_current_only_response": ["0", "0"],
        "independent_coupling_gamma_at_P0": [str(g) for g in gamma0],
        "load_derivatives_for_s": slopes,
        "proof_family": "D_s(P)=exp(s*(P-P0))*D0(P), Gamma_s(P0)=Gamma0(P0), Gamma_s_prime(P0)=Gamma0_prime(P0)+s*Gamma0(P0)",
        "scope": "exact algebraic witness; not a graphite fit, material coefficient or UD prediction",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
