"""Exact conditional Q198-output/Q169-amplitude one-event lift audit.

The supplied endpoint is a parameter, not an implementation of Q198's
receipt-dependent admission or selector.
"""

import itertools
import json
from native_compare import INDEX, N, mv
from native_integral_event import matrix


def norm2(x):
    return sum(q * q for q in x)


def one_event(x, theta, capacity, endpoint, half_numerator):
    """Candidate product lift after an externally supplied accepted endpoint."""
    mu = sum(endpoint) - sum(theta)
    y = mv(half_numerator, x)
    assert all(q % 2 == 0 for q in y)
    return tuple(q // 2 for q in y), endpoint, capacity - 2 * mu


def main():
    a, aa, _ = matrix()
    hnum = [[2 * int(i == j) + aa[i][j] for j in range(N)]
            for i in range(N)]
    x = [0] * N
    x[INDEX[(0,)]] = 2
    assert mv(a, x) != [0] * N
    half_x = tuple(q // 2 for q in mv(hnum, x))
    assert half_x == (-1, 1, 1, 1) + (0,) * (N - 4)
    assert half_x != tuple(x)
    assert norm2(half_x) == norm2(x) == 4
    assert sum(half_x[:4]) == sum(x[:4]) == 2

    bit_words = list(itertools.product((0, 1), repeat=3))
    checked = 0
    for theta, endpoint in itertools.product(bit_words, repeat=2):
        mu = sum(endpoint) - sum(theta)
        # These are synthetic necessary-budget dimensions, not sourced
        # receipt spaces or a claim that Q198 admits this endpoint.
        dim_minus = max(mu, 0)
        dim_plus = max(-mu, 0)
        assert dim_minus - dim_plus == mu
        identity_lift = (tuple(x), endpoint, 10 - 2 * mu)
        half_lift = one_event(x, theta, 10, endpoint, hnum)
        assert identity_lift != half_lift
        assert identity_lift[1:] == half_lift[1:]
        assert all(norm2(y[0]) == 4 and sum(y[0][:4]) == 2
                   for y in (identity_lift, half_lift))
        checked += 1

    # HOLD is an explicitly added convention; INFEASIBLE has no successor.
    theta = (1, 0, 0)
    hold = (tuple(x), theta, 10)
    assert hold == (tuple(x), theta, 10)
    result = {
        "source": "ledger v0.85 Q169/Q170 and Q194-Q198/Q200/Q210",
        "amplitude_state": "C0+C1+C2+C3 of filled K4 over R, dimension 15",
        "parity_state": "separate theta in (Z/2)^3, not a readout derived from real amplitudes",
        "receipt_state": "pre-event r supplied externally; Q198(r)=endpoint/HOLD/INFEASIBLE not executed here",
        "additive_readout_no_go": "any additive map R^15 -> (Z/2)^3 is zero by 2-divisibility",
        "example_x": "2v0, quadratic stock 4, vertex sum 2",
        "two_amplitude_updates": ["E(0)x=x", "E(pi/2)x=-v0+v1+v2+v3"],
        "conditional_endpoint_pairs_checked": checked,
        "endpoint_pair_status": "synthetic necessary net-Hamming-budget labels, not Q198-admitted receipts",
        "Q196_capacity_update": "D'=D-2mu, mu=dim Lminus-dim Lplus; formal closure capacity, not energy",
        "scope": "one-event product lift C x Theta x D with supplied accepted receipt; no source map g or next receipt/environment update",
        "conclusion": "conditional conservative amplitude-sector lifts exist but are nonunique; no autonomous source-selected full-carrier lift",
        "physical_promotion": 0,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
