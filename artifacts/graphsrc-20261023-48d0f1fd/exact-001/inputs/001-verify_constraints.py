#!/usr/bin/env python3
"""Exact C3 source null tests and a replay of archived illustrative KC data."""
from fractions import Fraction as F
from pathlib import Path
import contextlib
import io
import json
import math
import runpy

ROOT = Path(__file__).resolve().parents[2]
CAP = ROOT / "artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures"
SRC = CAP / "2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956/verify_harmonic_source.py"
KC = CAP / "2026-10-22T224639Z-codex-graphite-material-projection-fcd6e90e-4531aa0e-8487-4d43-b0dd-cfe246d1b6b4/MATERIAL_PROJECTION_RESULTS.json"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SRC))
Ks, rank = source["Ks"], source["rank"]

reps = [1, 3, 7, 8]  # A1, A3, B0, B1; fixed A0 and B5 (=index 12).
perm = [4*k % 7 for k in range(7)] + [7+(4*k-1) % 7 for k in range(7)]
rot = [[F(0), F(-1)], [F(1), F(-1)]]  # J_2^{-T}; order three.

def mm(A, B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def transpose(A):
    return list(map(list, zip(*A)))

def rref(A):
    X = [[F(x) for x in row] for row in A]
    pivots = []
    r = 0
    for col in range(len(X[0])):
        pivot = next((i for i in range(r,len(X)) if X[i][col]),None)
        if pivot is None:
            continue
        X[r],X[pivot] = X[pivot],X[r]
        q = X[r][col]
        X[r] = [v/q for v in X[r]]
        for i in range(len(X)):
            if i != r and X[i][col]:
                q = X[i][col]
                X[i] = [a-q*b for a,b in zip(X[i],X[r])]
        pivots.append(col)
        r += 1
        if r == len(X):
            break
    return X, pivots

def kernel(A):
    X, pivots = rref(A)
    basis = []
    for free in (j for j in range(len(A[0])) if j not in pivots):
        v = [F(0)]*len(A[0])
        v[free] = F(1)
        for i,p in enumerate(pivots):
            v[p] = -X[i][free]
        basis.append(v)
    return basis

assert mm(rot,mm(rot,rot)) == [[1,0],[0,1]]
assert len(set(perm)) == 14 and sorted(perm) == list(range(14))
assert set([0,12]) == {v for v in range(14) if perm[v] == v}
assert len(set(reps + [perm[v] for v in reps] + [perm[perm[v]] for v in reps] + [0,12])) == 14
for K in Ks:
    assert [K[a][v] for a in range(2) for v in (0,12)] == [0]*4
    for v in range(14):
        assert [K[a][perm[v]] for a in range(2)] == [sum(rot[a][b]*K[b][v] for b in range(2)) for a in range(2)]

# Values on the four representatives parameterize every C3-equivariant map:
# the two fixed columns vanish and rotation determines the other eight columns.
A = [[Ks[i][a][v] for v in reps for a in range(2)] for i in range(7)]
L = kernel(A)
expected = [[0,1,0,0,0,0,1,0], [1,0,-1,0,1,-1,0,1]]
assert L == expected and rank(A) == 6
assert all(sum(A[i][j] for i in range(7)) == 0 for j in range(8))
assert mm(A,transpose(L)) == [[0,0] for _ in range(7)]
assert mm(L,transpose(L)) == [[2,0],[0,5]]
assert rank(L) == 2

# Counterexamples prove that the complement is available to C3 maps, rather
# than being imposed by rotation.  Fill each orbit from arbitrary rep values.
def equivariant_map(h):
    C = [[F(0)]*14 for _ in range(2)]
    for v in reps:
        x = [h[2*reps.index(v)+a] for a in range(2)]
        for _ in range(3):
            C[0][v],C[1][v] = x
            v = perm[v]
            x = [sum(rot[a][b]*x[b] for b in range(2)) for a in range(2)]
    return C

allowed = []
for i in range(8):
    h = [F(int(i==j)) for j in range(8)]
    C = equivariant_map(h)
    assert [C[a][v] for v in reps for a in range(2)] == h
    assert [C[a][perm[v]] for a in range(2) for v in range(14)] == [sum(rot[a][b]*C[b][v] for b in range(2)) for a in range(2) for v in range(14)]
    allowed.append([C[a][v] for a in range(2) for v in range(14)])
assert rank(allowed) == 8

# Replay only the already-published aligned KC cross-Hessian, no new KC run.
data = json.loads(KC.read_text())
a = math.sqrt(3)*1.42
basis = [[a,a/2],[0,a*math.sqrt(3)/2]]
R = [[8/7,3/7],[-3/7,5/7]]
swap = [[0,1],[1,0]]
Fmap = mm(mm(basis,R),swap)  # x_cart [Angstrom] = Fmap u_direct.
replay = []
for case in data["checks"]:
    cart = case["cross_hessian_mev_per_a2_per_upper_atom"]
    aligned = [[0.0]*14 for _ in range(2)]
    for site in range(2):
        for k in range(7):
            for component in range(2):
                aligned[component][site*7+(k+2)%7] = cart[component][site*7+k]
    direct = mm(transpose(Fmap),aligned)
    h = [direct[component][v] for v in reps for component in range(2)]
    residual = [sum(row[i]*h[i] for i in range(8)) for row in L]
    replay.append({"cutoff_angstrom":case["cutoff_a"],
                   "difference_step_angstrom":case["finite_difference_h_a"],
                   "constraint_residual_meV_per_angstrom_per_upper_atom":residual,
                   "published_full_map_relative_residual":case["best_offset_residual_norm"]})

print(json.dumps({"status":"PASS_EXACT_CONDITIONAL_AND_ARCHIVE_REPLAY",
                  "representative_site_indices":reps,
                  "representative_names":["A1","A3","B0","B1"],
                  "source_rank":rank(A),"equivariant_dimension":8,
                  "constraint_rows":[[int(x) for x in row] for row in L],
                  "constraint_gram":[[int(x) for x in row] for row in mm(L,transpose(L))],
                  "kernel_of_weight_map":"uniform weights",
                  "physical_alignment":"archived KC alignment offset 2; Cartesian-to-direct Fmap.T",
                  "material_replay":replay},indent=2))
