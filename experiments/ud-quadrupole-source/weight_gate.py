"""Exact Q204 mask-to-P06 weight nonuniqueness witness; no new source law."""
import itertools
import json
from fractions import Fraction as Q
from audit import PERMS, THETA7, V, dot, dyad, MATCHINGS, perm_theta

PAIR = [[[sum(dyad(e)[i][j] for e in m) for j in V] for i in V]
        for m in MATCHINGS]
TENSOR = {t: [[sum(t[p] * PAIR[p][i][j] for p in range(3)) for j in V] for i in V]
          for t in THETA7}


def weights(mask, kind):
    assert mask in THETA7
    orbit = [t for t in THETA7 if sum(t) == sum(mask)]
    if kind == "delta":
        return {t: Q(int(t == mask)) for t in THETA7}
    if kind == "orbit":
        return {t: Q(int(t in orbit), len(orbit)) for t in THETA7}
    raise ValueError(kind)


def response(w):
    return [[sum(w[t] * TENSOR[t][i][j] for t in THETA7) for j in V] for i in V]


def main():
    rows = []
    checks = 0
    for mask in THETA7:
        a, b = weights(mask, "delta"), weights(mask, "orbit")
        assert sum(a.values()) == sum(b.values()) == 1
        assert all(z >= 0 for z in a.values()) and all(z >= 0 for z in b.values())
        ra, rb = response(a), response(b)
        assert dot(rb, rb) == 0
        for g in PERMS:
            for kind, w in (("delta", a), ("orbit", b)):
                shifted = {perm_theta(t, g): w[t] for t in THETA7}
                assert shifted == weights(perm_theta(mask, g), kind)
                checks += 1
        rows.append({"mask": "".join(map(str, mask)),
                     "delta_response_norm_sq": str(dot(ra, ra)),
                     "orbit_response_norm_sq": str(dot(rb, rb)),
                     "same_response": ra == rb})
    assert sum(not row["same_response"] for row in rows) == 6
    print(json.dumps({"status": "EXACT_CONDITIONAL_SOURCE_NONIDENTIFIABILITY",
                      "source": "Q204 three-bit latent receipt; mask-to-seven-state law unselected",
                      "rules": ["point mass at mask", "uniform on mask Hamming orbit"],
                      "common_constraints": "nonnegative weights, total one, S4 covariance, same mask input",
                      "inequivalent_masks": 6, "checked_masks": 7,
                      "covariance_checks": checks,
                      "results": rows, "physical_promotion": 0}, indent=2))


if __name__ == "__main__":
    main()
