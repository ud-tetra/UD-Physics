#!/usr/bin/env python3
"""Exact constructor check of the seven-orbit port and a passive-bath witness."""
from fractions import Fraction as F
from pathlib import Path
import contextlib
import io
import json
import runpy

ROOT = Path(__file__).resolve().parents[2]
CAP = ROOT / "artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures"
CARRIER = CAP / "2026-10-22T211409Z-codex-graphite-honeycomb-5e20b9a6-101b-4fce-8c91-a1d4070ba2d8/verify_honeycomb_h1.py"
SOURCE = CAP / "2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956/verify_harmonic_source.py"
with contextlib.redirect_stdout(io.StringIO()):
    carrier = runpy.run_path(str(CARRIER))
    source = runpy.run_path(str(SOURCE))
mm, trans, rank = (carrier[x] for x in ("mm", "trans", "rank"))
Ks, Q, G = (source[x] for x in ("Ks", "Q", "G"))

def inv2(A):
    a, b = A[0]
    c, d = A[1]
    det = a*d-b*c
    assert det != 0
    return [[d/det, -b/det], [-c/det, a/det]]

def psd2(A):
    return A == trans(A) and A[0][0] >= 0 and A[1][1] >= 0 and A[0][0]*A[1][1]-A[0][1]**2 >= 0

w = [F(0), F(1), F(-1)] + [F(0)]*4
S = [[sum(w[i]*Ks[i][a][v] for i in range(7)) for v in range(14)] for a in range(2)]
alpha = sum(w[i]*Q[i][j]*w[j] for i in range(7) for j in range(7))
A = mm(S, trans(S))
assert alpha == F(5, 2) and A == [[alpha*x for x in row] for row in G]
assert rank(S) == 2 and psd2(A)
assert [[sum(Ks[i][a][v] for i in range(7)) for v in range(14)] for a in range(2)] == [[0]*14 for _ in range(2)]

R = mm(trans(S), inv2(A))  # 14 x 2 exact right inverse
assert mm(S, R) == [[1, 0], [0, 1]]
targets = {"zero": [[0,0],[0,0]], "isotropic": [[1,0],[0,1]],
           "anisotropic": [[2,1],[1,3]], "rank_one": [[1,2],[2,4]]}
for name, T in targets.items():
    assert psd2(T)
    L = mm(mm(R,T),trans(R))  # 14 x 14 PSD because T is PSD
    assert mm(mm(S,L),trans(S)) == T, name

print(json.dumps({"status":"PASS_EXACT_CONDITIONAL_CONSTRUCTOR_CHECK",
                  "source":"archived seven-orbit port at the repository revision",
                  "weights":[str(x) for x in w], "alpha":str(alpha),
                  "source_rank":rank(S), "source_gram":[[str(x) for x in row] for row in A],
                  "right_inverse":"S R = I_2",
                  "passive_targets_recovered":list(targets),
                  "uniform_source":"zero"}, indent=2))
