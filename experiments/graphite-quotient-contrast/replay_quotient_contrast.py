#!/usr/bin/env python3
"""Exact honeycomb quotient ranks and published, scope-limited static contrasts."""
import json
from decimal import Decimal, getcontext
from fractions import Fraction


def rank(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        factor = a[pivot_row][col]
        a[pivot_row] = [v / factor for v in a[pivot_row]]
        for r in range(pivot_row + 1, rows):
            factor = a[r][col]
            if factor:
                a[r] = [a[r][c] - factor * a[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def quotient(m, n):
    nc = m * m + m * n + n * n
    s1, s2 = m + n, n
    # A_r to B_r, B_(r-s1), B_(r-s2); e(t,r) is an oriented A-to-B edge.
    e = lambda t, r: t * nc + r % nc
    b1 = [[0] * (3 * nc) for _ in range(2 * nc)]
    for r in range(nc):
        for t, target in enumerate((r, r - s1, r - s2)):
            b1[r][e(t, r)] = -1
            b1[nc + target % nc][e(t, r)] = 1
    b2 = [[0] * nc for _ in range(3 * nc)]
    for r in range(nc):
        # Oriented elementary hexagon; a direct boundary-square check follows.
        terms = ((0, r, 1), (1, r+s1, -1), (2, r+s1, 1),
                 (0, r+s1-s2, -1), (1, r+s1-s2, 1), (2, r, -1))
        for t, site, sign in terms:
            b2[e(t, site)][r] += sign
    assert all(sum(b1[i][k] * b2[k][j] for k in range(3*nc)) == 0
               for i in range(2*nc) for j in range(nc))
    r1, r2 = rank(b1), rank(b2)
    return {"mn": [m, n], "cells": nc, "chain_dimensions": [2*nc, 3*nc, nc],
            "ranks": [r1, r2], "betti": [2*nc-r1, 3*nc-r1-r2, nc-r2],
            "uniform_port_cancelled": True}


cases = [quotient(2, 1), quotient(3, 1), quotient(3, 2)]
for row in cases:
    assert row["ranks"] == [2*row["cells"]-1, row["cells"]-1]
    assert row["betti"] == [1, 2, 1]

getcontext().prec = 28
# Published rigid-layer values from Lebedeva et al., arXiv:2511.01338v1,
# Table 2 (PES amplitude) and Table 6 (first-harmonic ideal shear strength).
# These rounded source figures are data, not exact material constants.
df_amp21, df_amp31 = Decimal("0.347"), Decimal("0.027")  # micro-eV/atom
kc_amp21, kc_amp31 = Decimal("87.7"), Decimal("20.6")     # same article, cited KC
shear21, shear31 = Decimal("13900"), Decimal("6680")      # Pa
ratios = {"dft_rigid_corrugation_21_over_31": str(df_amp21/df_amp31),
          "dft_rigid_ideal_static_shear_21_over_31": str(shear21/shear31),
          "reported_kc_rigid_corrugation_21_over_31": str(kc_amp21/kc_amp31),
          "reported_kc_over_dft_corrugation_21": str(kc_amp21/df_amp21),
          "reported_kc_over_dft_corrugation_31": str(kc_amp31/df_amp31)}
print(json.dumps({"status":"PASS_EXACT_QUOTIENT_AND_SOURCE_ROUNDED_CONTRAST",
                  "source":"Lebedeva et al., arXiv:2511.01338v1, Tables 2 and 6 and text near Table 2; Chen et al. PRL 137, 166201 (2026), public abstract",
                  "exact_quotients":cases,
                  "source_values":{"dft_rigid_corrugation_micro_eV_per_atom":{"21":str(df_amp21),"31":str(df_amp31)},
                                   "reported_kc_rigid_corrugation_micro_eV_per_atom":{"21":str(kc_amp21),"31":str(kc_amp31)},
                                   "dft_derived_rigid_ideal_static_shear_Pa":{"21":str(shear21),"31":str(shear31)}},
                  "ratios_from_source_rounded_values":ratios,
                  "conditional_detection_window_for_common_transfer":"If F=alpha*tau with one positive alpha and shared force threshold T, 6680 Pa < T/alpha <= 13900 Pa permits (2,1) detection and (3,1) non-detection; no alpha or T is measured here."},indent=2))
