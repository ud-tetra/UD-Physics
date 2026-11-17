"""Exact centered moments, curl forms, and bulk Whitney mass on regular simplices."""

from fractions import Fraction as F
from itertools import combinations
import json


def gyration(dimension):
    n = dimension + 1
    moments = F(1, n * (n + 1))
    # Vertices e_i/sqrt(2); centered vertex inner products are (delta_ij-1/n)/2.
    return sum(moments * (1 + (i == j)) * (F(i == j) - F(1, n)) / 2
               for i in range(n) for j in range(n))


def main():
    assert gyration(2) == F(1, 12)
    assert gyration(3) == F(3, 40)
    face_weight = gyration(2) / 4
    bulk_weight = (gyration(3) - gyration(3) / 3) / 4
    assert (face_weight, bulk_weight) == (F(1, 48), F(1, 80))

    edges = list(combinations(range(4), 2))
    faces = list(combinations(range(4), 3))
    boundaries = [{face[:k] + face[k+1:]: (-1) ** k for k in range(3)}
                  for face in faces]

    def gram(i, j):
        return 2 * (F(i == j) - F(1, 4))

    def moment(i, j):
        return F(1 + (i == j), 20)

    for e, (i, j) in enumerate(edges):
        for f, (k, l) in enumerate(edges):
            cycle_gram = sum(row.get((i, j), 0) * row.get((k, l), 0)
                             for row in boundaries)
            cut_gram = 4 * (e == f) - cycle_gram
            bulk_curl = 4 * (gram(i, k) * gram(j, l) - gram(i, l) * gram(j, k))
            bulk_mass = (moment(i, k) * gram(j, l) - moment(i, l) * gram(j, k)
                         - moment(j, k) * gram(i, l) + moment(j, l) * gram(i, k))
            assert bulk_curl == 4 * cycle_gram
            assert bulk_mass == F(1, 8) * cut_gram + F(1, 20) * cycle_gram
            assert bulk_mass + F(3, 160) * bulk_curl == F(1, 2) * (e == f)

    assert F(8, 9) + face_weight * F(64, 3) == F(4, 3)
    assert F(1, 5) + bulk_weight * 16 == F(2, 5) != F(1, 2)
    print(json.dumps({
        "face_weight": str(face_weight), "bulk_weight": str(bulk_weight),
        "face_sum_curl_cycle": "64/3", "bulk_curl_cycle": "16",
        "bulk_mass_cut_cycle": ["1/2", "1/5"],
        "bulk_after_one_rotational_copy": ["1/2", "2/5"],
        "bulk_equalizing_added_curl_weight": "3/160",
    }, indent=2))


if __name__ == "__main__":
    main()
