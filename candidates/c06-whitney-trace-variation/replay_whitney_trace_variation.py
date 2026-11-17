"""Exact sector checks for lowest-order Whitney boundary-to-bulk lifts."""

from fractions import Fraction as F
from itertools import combinations
import json


def main():
    edges = list(combinations(range(4), 2))
    faces = list(combinations(range(4), 3))

    def gradient(i, j):
        return 2 * (F(i == j) - F(1, 4))

    def moment(i, j):
        return F(1 + (i == j), 20)

    def incidence(v, edge):
        return (v == edge[1]) - (v == edge[0])

    def face_sign(edge, face):
        return sum((-1) ** k for k in range(3) if edge == face[:k] + face[k + 1:])

    for i, j in edges:
        for k, l in edges:
            e, other = (i, j), (k, l)
            cut = F(sum(incidence(v, e) * incidence(v, other) for v in range(4)), 4)
            cycle = int(e == other) - cut
            curl = 4 * (gradient(i, k) * gradient(j, l) - gradient(i, l) * gradient(j, k))
            mass = (moment(i, k) * gradient(j, l) - moment(i, l) * gradient(j, k)
                    - moment(j, k) * gradient(i, l) + moment(j, l) * gradient(i, k))
            trace_mass = sum(F(6 * (e == other) - face_sign(e, f) * face_sign(other, f), 36)
                             for f in faces if set(e) <= set(f) and set(other) <= set(f))
            assert curl == 16 * cycle
            assert mass == F(1, 2) * cut + F(1, 5) * cycle
            assert trace_mass == F(1, 3) * cut + F(2, 9) * cycle
            assert mass + F(3, 160) * curl == F(1, 2) * (e == other)
            # The vertex mass has inverse 20 on the mean-zero incidence image.
            down = F(1, 2)**2 * 20 * (4 * cut)
            assert down == 20 * cut

    mv = (F(1, 2), F(1, 5))
    mb = (F(1, 3), F(2, 9))
    soft = []
    for v, b in zip(mv, mb):
        u = b / (v + b)
        assert v * u == b * (1 - u)
        soft.append(v * u**2 + b * (1 - u)**2)
    assert soft == [F(1, 5), F(2, 19)]
    print(json.dumps({
        "unit_side_hard_cut_cycle": list(map(str, mv)),
        "unit_side_boundary_cut_cycle": list(map(str, mb)),
        "unit_side_soft_cut_cycle": list(map(str, soft)),
        "unit_side_full_hodge_cut_cycle": ["20", "16"],
        "conditional_up_weight": "3/160",
    }, indent=2))


if __name__ == "__main__":
    main()
