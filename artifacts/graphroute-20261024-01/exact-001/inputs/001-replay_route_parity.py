#!/usr/bin/env python3
"""Exact rational witness for the conditional Q24 route-parity identity.

This is a model check, not a graphite material simulation. No force data enter.
"""

import json
from fractions import Fraction as F


def candidate(eta, wij, wji, xij, xji):
    return eta * (wij * xij + wji * xji) / 2


def main():
    eta, w0, a, xi = F(7, 2), F(2), F(3), F(5)
    # u is the dimensionless velocity; evaluate the polynomial at exact points.
    observations = {}
    for u in (F(-1, 2), F(0), F(1, 2)):
        wij, wji = w0 + a * u, w0 - a * u
        assert wij > 0 and wji > 0
        c = candidate(eta, wij, wji, xi, -xi)
        assert c == eta * a * xi * u
        # C=(c,2c), K=diag(2,3), D=diag(5,7): gamma=C K^-1 D K^-1 C^T.
        gamma = c * c * (F(5, 4) + F(28, 9))
        assert gamma >= 0
        assert gamma == F(1730925, 144) * u * u
        observations[str(u)] = {
            "c": str(c), "gamma": str(gamma), "force_minus_gamma_times_u": str(-gamma * u)
        }
    # An exchange-even route is a distinct branch: reciprocal weights can couple.
    even_route = candidate(eta, w0, w0, xi, xi)
    assert even_route == 35
    # Simultaneous reversal of both directed-odd factors yields an even candidate.
    odd_odd = candidate(eta, F(4), F(2), xi, -xi)
    assert odd_odd == eta * xi
    print(json.dumps({
        "evidence": "EXACT_CONDITIONAL_WITNESS",
        "odd_route_reciprocal_zero": str(candidate(eta, w0, w0, xi, -xi)),
        "odd_route_odd_weight": observations,
        "even_route_reciprocal_nonzero": str(even_route),
        "odd_odd_nonzero": str(odd_odd),
        "material_force_measured": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
