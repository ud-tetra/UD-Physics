"""Exact finite replay of a candidate addressed, conservative parity tick.

No endpoint, measured constant, or physical event record enters this script.
"""
import itertools
import json
from collections import Counter

BITS = tuple(itertools.product((0, 1), repeat=3))
PERMS = tuple(itertools.permutations(range(3)))


def permute(bits, perm):
    return tuple(bits[perm[i]] for i in range(3))


def tick(theta, reserve, address):
    """Return (new theta, new reserve, verdict), with an immutable address."""
    assert theta in BITS and address in BITS and isinstance(reserve, int) and reserve >= 0
    if sum(address) != 1:
        return theta, reserve, "HOLD_ADDRESS"
    p = address.index(1)
    if theta[p] == 0 and reserve == 0:
        return theta, reserve, "HOLD_STOCK"
    out = list(theta)
    out[p] = 1 - out[p]
    return tuple(out), reserve + 2 * theta[p] - 1, "EVENT"


def main():
    # For a weight-preserving map, equivariance restricts each orbit image.
    # This avoids enumerating the 8^8 arbitrary functions directly.
    allowed = {}
    for theta in BITS:
        stabilizer = [g for g in PERMS if permute(theta, g) == theta]
        allowed["".join(map(str, theta))] = [
            "".join(map(str, target)) for target in BITS
            if sum(target) == sum(theta)
            and all(permute(target, g) == target for g in stabilizer)
        ]
        assert allowed["".join(map(str, theta))] == ["".join(map(str, theta))]

    counts = Counter()
    table = []
    for theta in BITS:
        for reserve in range(4):
            for address in BITS:
                endpoint, remaining, verdict = tick(theta, reserve, address)
                counts[verdict] += 1
                assert sum(endpoint) + remaining == sum(theta) + reserve
                if verdict == "EVENT":
                    assert tick(endpoint, remaining, address)[:2] == (theta, reserve)
                else:
                    assert (endpoint, remaining) == (theta, reserve)
                for g in PERMS:
                    lhs = tick(permute(theta, g), reserve, permute(address, g))
                    assert lhs == (permute(endpoint, g), remaining, verdict)
        for reserve in (0, 1):
            endpoint, remaining, verdict = tick(theta, reserve, (1, 0, 0))
            table.append({"theta": "".join(map(str, theta)), "reserve": reserve,
                          "endpoint": "".join(map(str, endpoint)),
                          "remaining": remaining, "verdict": verdict})
    assert sum(counts.values()) == 8 * 4 * 8
    print(json.dumps({"status": "EXACT_CONDITIONAL", "theta_only_allowed": allowed,
                      "checked_states": sum(counts.values()),
                      "covariance_checks": sum(counts.values()) * len(PERMS),
                      "verdict_counts": dict(sorted(counts.items())),
                      "one_hot_address_100_table": table,
                      "physical_promotion": 0}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
