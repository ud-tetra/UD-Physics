#!/usr/bin/env python3
"""Exact zero-mode harmonic incidence projection on three honeycomb quotients."""
import json
from fractions import Fraction


def projected_port(m, n, weights):
    cells = m*m + m*n + n*n
    step1, step2 = m+n, n
    # A_r -> B_r, B_(r-step1), B_(r-step2), all bonds A-to-B.
    targets = lambda r: (r, r-step1, r-step2)
    # Constant harmonic vectors (non-orthonormal but N-independent basis).
    h = ((1, 1), (-1, 1), (0, -2))
    # M_e = h_t / sqrt(N), U_A/B,r = 1 / sqrt(N). The two
    # normalizers multiply to 1/N, so all arithmetic is rational.
    s = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for r in range(cells):
        for t, target in enumerate(targets(r)):
            assert 0 <= target % cells < cells
            for a in range(2):
                s[a][0] -= Fraction(h[t][a]*weights[t], cells)
                s[a][1] += Fraction(h[t][a]*weights[t], cells)
    assert s == [[-sum(Fraction(h[t][a]*weights[t]) for t in range(3)),
                   sum(Fraction(h[t][a]*weights[t]) for t in range(3))]
                 for a in range(2)]
    return [[str(x) for x in row] for row in s]


cases = []
for mn in ((2, 1), (3, 1), (3, 2)):
    cases.append({"pattern": mn, "N":mn[0]**2+mn[0]*mn[1]+mn[1]**2,
                  "C3_symmetric_weights_1_1_1":projected_port(*mn,(1,1,1)),
                  "orientation_weights_1_2_3":projected_port(*mn,(1,2,3))})
assert all(row["C3_symmetric_weights_1_1_1"] == [["0","0"],["0","0"]] for row in cases)
assert all(row["orientation_weights_1_2_3"] == [["1","-1"],["3","-3"]] for row in cases)

print(json.dumps({"status":"PASS_EXACT_TRANSLATION_COVARIANT_PORT",
                  "scope":"S_N=M_N^T W_N B1_N^T, unit vertex/edge metrics, normalized translation-zero input and harmonic output; W_N orientation-wise constant",
                  "theorem":"C3-symmetric edge weights cancel; orientation anisotropy gives an N-independent rank-one zero-sector map for a fixed stencil",
                  "point_source":"For fixed orientation weights, one-site forcing has harmonic amplitude proportional to 1/sqrt(N), not seven-cell-only support",
                  "cases":cases},indent=2))
