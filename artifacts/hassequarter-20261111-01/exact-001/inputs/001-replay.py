"""Exact local integer Hasse quarter-turn candidate on one filled K4."""
import itertools
import json

EDGES = tuple(itertools.combinations(range(4), 2))
PERMS = tuple(itertools.permutations(range(4)))


def stock(state):
    v, e, _ = state
    return sum(x * x for x in v) + sum(x * x for x in e)


def flags(state):
    v, e, hard = state
    return [(i, k) for k, (a, b) in enumerate(EDGES) if hard[k] and e[k]
            for i in (a, b) if v[i]]


def tick(state):
    """F(state) returns (updated state, verdict), no inferred physical time."""
    v, e, hard = state
    assert len(v) == 4 and len(e) == len(hard) == 6
    assert all(h in (0, 1) for h in hard)
    found = flags(state)
    if len(found) != 1:
        return state, "HOLD_ZERO" if not found else "HOLD_TIE"
    i, k = found[0]
    s = -1 if i == EDGES[k][0] else 1  # B1_(i,e), ascending edge orientation
    vv, ee = list(v), list(e)
    vv[i], ee[k] = -s * e[k], s * v[i]
    return (tuple(vv), tuple(ee), hard), "EVENT"


def transform(state, g):
    v, e, hard = state
    vv, ee, hh = [0] * 4, [0] * 6, [0] * 6
    for i in range(4):
        vv[g[i]] = v[i]
    for k, (i, j) in enumerate(EDGES):
        x, y = g[i], g[j]
        target = EDGES.index(tuple(sorted((x, y))))
        ee[target] = e[k] if x < y else -e[k]
        hh[target] = hard[k]
    return tuple(vv), tuple(ee), tuple(hh)


def main():
    cases, covariance = 0, 0
    for k, (i, j) in enumerate(EDGES):
        for selected in (i, j):
            for a in (-2, -1, 1, 2):
                for b in (-2, -1, 1, 2):
                    v, e, hard = [0] * 4, [0] * 6, [0] * 6
                    v[selected], e[k], hard[k] = a, b, 1
                    state = tuple(v), tuple(e), tuple(hard)
                    assert flags(state) == [(selected, k)]
                    assert tick(state)[1] == "EVENT"
                    assert stock(tick(state)[0]) == stock(state)
                    orbit = [state]
                    for _ in range(4):
                        new, verdict = tick(orbit[-1])
                        assert verdict == "EVENT" and stock(new) == stock(state)
                        orbit.append(new)
                    assert orbit[4] == orbit[0] and orbit[2] != orbit[0]
                    assert orbit[1][0][selected] ** 2 - a * a == b * b - a * a
                    for g in PERMS:
                        lhs = tick(transform(state, g))
                        rhs = transform(tick(state)[0], g), "EVENT"
                        assert lhs == rhs
                        covariance += 1
                    cases += 1
    v, e, hard = (1, 0, 0, 0), (2, 0, 0, 0, 0, 0), (0,) * 6
    assert tick((v, e, hard))[1] == "HOLD_ZERO"
    assert tick(((1, 1, 0, 0), e, (1, 0, 0, 0, 0, 0)))[1] == "HOLD_TIE"
    assert tick(((0,) * 4, e, (1, 0, 0, 0, 0, 0)))[1] == "HOLD_ZERO"
    sample = ((1, 0, 0, 0), (2, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0))
    path = [sample]
    for _ in range(4):
        path.append(tick(path[-1])[0])
    print(json.dumps({"status": "EXACT_CONDITIONAL_CANDIDATE",
                      "sample_signed_pair": [[s[0][0], s[1][0]] for s in path],
                      "sample_vertex_stock": [s[0][0] ** 2 for s in path],
                      "hold_baseline_vertex_stock": [1] * 5,
                      "sample_total_stock": stock(sample),
                      "event_preparations": cases,
                      "signed_s4_covariance_checks": covariance,
                      "hold_checks": 3, "physical_promotion": 0}, indent=2))


if __name__ == "__main__":
    main()
