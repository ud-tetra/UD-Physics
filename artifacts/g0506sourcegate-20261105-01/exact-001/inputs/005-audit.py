"""Exact four-site-to-Hodge candidate and source-unit counterexamples.

All checks use integer/rational coefficients; the phase examples are signs.
"""
from itertools import combinations, permutations
from pathlib import Path
from fractions import Fraction as R
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "g0506-step-kernel-unitgate"))
from audit import trans, mul, vec, rank, dot  # exact rational helpers from merged predecessor


def zeros(m, n): return [[R(0) for _ in range(n)] for _ in range(m)]
def add(a, b): return [[x + y for x, y in zip(u, v)] for u, v in zip(a, b)]
def scale(a, k): return [[k * x for x in row] for row in a]
def cols(vs): return trans(vs)
def same(a, b): return a == b
def mvec(a, v): return vec(a, v)


def main():
    cells = [c for k in range(1, 5) for c in combinations(range(4), k)]
    loc = {c: i for i, c in enumerate(cells)}
    n = len(cells)
    D = []
    for k in range(1, 4):
        d = zeros(n, n)
        for c in cells:
            if len(c) == k + 1:
                for j in range(len(c)):
                    d[loc[c[:j] + c[j + 1:]]][loc[c]] = R((-1) ** j)
        D.append(d)
    K = [add(d, scale(trans(d), -1)) for d in D]
    A = add(add(K[0], K[1]), K[2])
    J = scale(A, R(1, 2))
    P = [scale(mul(k, k), R(-1, 4)) for k in K]
    assert [rank(p) for p in P] == [6, 6, 2]
    assert mul(mul(A, A), A) == scale(A, -4)

    # P0 is the mean-zero projection of a real four-site scalar field.
    P0 = zeros(n, n)
    for i in range(4):
        for j in range(4):
            P0[i][j] = R(1 if i == j else 0) - R(1, 4)
    V = [row[:4] for row in P0]
    JV = mul(J, V)
    F = [u + v for u, v in zip(V, JV)]  # (u,v) -> P0 u + J P0 v
    assert rank(F) == 6
    assert mul(P[0], F) == F
    assert mul(P[1], F) == zeros(n, 8) and mul(P[2], F) == zeros(n, 8)
    B = zeros(8, 8)
    for i in range(4):
        B[i][i + 4] = R(-2)
        B[i + 4][i] = R(2)
    assert mul(F, B) == mul(A, F)  # only under the imported z'=2iz update

    # Pullback of the directed Hasse step: q(Fz,Fw)=1/2 Im <P0z,P0w>.
    Q = scale(mul(trans(F), mul(A, F)), R(-1, 4))
    expected = zeros(8, 8)
    for i in range(4):
        for j in range(4):
            expected[i][j + 4] = P0[i][j] / 2
            expected[i + 4][j] = -P0[i][j] / 2
    assert Q == expected and add(Q, trans(Q)) == zeros(8, 8)
    for perm in permutations(range(4)):
        S = zeros(n, n)
        for c, i in loc.items():
            im = [perm[v] for v in c]
            inversions = sum(im[a] > im[b] for a in range(len(im)) for b in range(a + 1, len(im)))
            S[loc[tuple(sorted(im))]][i] = R((-1) ** inversions)
        T = zeros(8, 8)
        for i in range(4):
            T[perm[i]][i] = T[perm[i] + 4][i + 4] = R(1)
        assert mul(S, F) == mul(F, T) and mul(S, A) == mul(A, S)

    def z(u):
        return [R(v) for v in u] + [R(0)] * 4

    uniform = z([R(1, 2)] * 4)
    balanced = z([R(1, 2), R(-1, 2), R(1, 2), R(-1, 2)])
    one_flip = z([R(1, 2)] * 3 + [R(-1, 2)])
    support = lambda w: dot(vec(F, w), vec(F, w))
    assert [support(w) for w in (uniform, balanced, one_flip)] == [0, 1, R(3, 4)]
    assert all(sum(w[i] ** 2 + w[i + 4] ** 2 for i in range(4)) == 1
               for w in (uniform, balanced, one_flip))
    # Naive packet phase-area is nonzero on a common-phase turn, while the
    # mean-zero Hodge image and its action vanish.
    quarter = [v / 2 for v in vec(B, uniform)]
    naive_q = sum(uniform[i] * quarter[i + 4] - uniform[i + 4] * quarter[i]
                  for i in range(4)) / 2
    assert naive_q == R(1, 2) and dot(uniform, vec(Q, quarter)) == 0
    assert dot(balanced, vec(Q, [v / 2 for v in vec(B, balanced)])) == R(1, 2)

    result = {
        "status": "EXACT_CONDITIONAL_CANDIDATE_PASS",
        "carrier_ranks": [rank(p) for p in P], "source_map_rank": rank(F),
        "visible_sector_ranks": [rank(mul(p, F)) for p in P],
        "signed_S4_actions": 24,
        "same_total_burden_support_examples": ["0", "1", "3/4"],
        "common_phase_naive_q": str(naive_q), "common_phase_Hodge_q": "0",
        "finite_step": "q(Fz,Fw)=Im< P0z,P0w >/2; endpoint alias remains",
        "conditional_dynamics": "z'=2 i z implies x'=Ax; source does not select z or update",
        "source_status": "NO_PACKET_TO_HODGE_OR_ABSOLUTE_UNIT_RULE_FOUND_IN_SCOPED_SOURCES",
        "physical_promotion": 0,
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "rank": rank(F),
                      "sectors": result["visible_sector_ranks"]}))


if __name__ == "__main__":
    main()
