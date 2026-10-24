#!/usr/bin/env python3
"""Exact cyclic honeycomb harmonic projection and registry/source correlation."""
import json
from fractions import Fraction

H = ((1, 1), (-1, 1), (0, -2))  # columns h1,h2; fixed nonorthonormal basis


def port(m, n, weights, vertex_a, vertex_b):
    """Return sqrt(N)*M^T W B1^T x for M_{r,t,a}=h[t][a]/sqrt(N)."""
    size = m*m + m*n + n*n
    assert len(weights) == 3 and all(len(w) == size for w in weights)
    assert len(vertex_a) == len(vertex_b) == size
    shifts = (0, m+n, n)
    return [sum(Fraction(H[t][a] * weights[t][r]) *
                (vertex_b[(r-shifts[t]) % size] - vertex_a[r])
                for t in range(3) for r in range(size)) for a in range(2)]


def family(m, n):
    size = m*m + m*n + n*n
    # Every bond direction has equal spatial mean 2+1/N, but a site can be anisotropic.
    weights = [[2 + int(r == t) for r in range(size)] for t in range(3)]
    ones = [1] * size
    zeros = [0] * size
    uniform = port(m, n, weights, zeros, ones)
    point = port(m, n, weights, [int(r == 0) for r in range(size)], zeros)
    # Positive weights with exactly equal means; signed zero-mean vertex source.
    corr = [[2 + (int(r == 0) - int(r == 1) if t == 0 else 0)
             for r in range(size)] for t in range(3)]
    aligned = [int(r == 0) - int(r == 1) for r in range(size)]
    displaced = [int(r == 2) - int(r == 3) for r in range(size)]
    return {"mn": [m, n], "N": size,
            "engineered_character_match_p2_k5": (2 + 5) % size == 0,
            "equal_means": [str(Fraction(sum(row), size)) for row in weights],
            "uniform_B_force_times_sqrtN": [str(v) for v in uniform],
            "A_point_force_times_sqrtN": [str(v) for v in point],
            "aligned_zero_mean_force_times_sqrtN": [str(v) for v in port(m,n,corr,aligned,zeros)],
            "displaced_zero_mean_force_times_sqrtN": [str(v) for v in port(m,n,corr,displaced,zeros)]}


rows = [family(m,n) for m,n in ((2,1),(3,1),(3,2))]
assert all(row["uniform_B_force_times_sqrtN"] == ["0","0"] for row in rows)
assert all(row["A_point_force_times_sqrtN"] == ["-1","-1"] for row in rows)
assert all(row["aligned_zero_mean_force_times_sqrtN"] == ["-2","-2"] for row in rows)
assert all(row["displaced_zero_mean_force_times_sqrtN"] == ["0","0"] for row in rows)
assert [row["engineered_character_match_p2_k5"] for row in rows] == [True,False,False]
print(json.dumps({"status":"PASS_EXACT_REGISTRY_SOURCE_CORRELATION",
                  "normalization":"listed vectors are sqrt(N) times the harmonic projection for unnormalized integer vertex inputs; h basis is fixed across N",
                  "cases":rows},indent=2))
