#!/usr/bin/env python3
"""Exact integer/rational interface audit for source-bound QPB1 K4 flow.
Run: python3 experiments/parity-dynamics-gauge-20261103/interface_audit_v03.py
Dependency: sympy. All times in native dimensionless flow parameter.
"""
import itertools
import json
import sympy as S

simplices = [list(itertools.combinations(range(4), k)) for k in (1, 2, 3, 4)]
labels = [t for layer in simplices for t in layer]
index = {t: i for i, t in enumerate(labels)}
D = S.zeros(15)
for t in labels:
    if len(t) > 1:
        for a in range(len(t)):
            D[index[t[:a]+t[a+1:]], index[t]] += (-1)**a
A = D - D.T
assert D*D == S.zeros(15)
assert A.T == -A
assert A**3 == -4*A
# Exact exp(pi*A/2) by minimal polynomial, not floating exponentiation.
M = S.eye(15) + A*A/2
assert M*M == S.eye(15)
assert M.T*M == S.eye(15)
assert M*A == A*M
survivors, fixed = [], []
for z in range(1024):
    x = S.Matrix([(z >> i) & 1 for i in range(10)] + [0]*5)
    y = M*x
    if all(y[i] in (0,1) for i in range(10)) and all(y[i] == 0 for i in range(10,15)):
        survivors.append(z)
    if A*x == S.zeros(15,1):
        fixed.append(z)
assert survivors == [0,3,5,6,9,10,12,15]
assert fixed == [0,15]
# Confirm all survivors are vertex-only and have 3-bit opposite-edge parity 000.
assert all(z >> 4 == 0 for z in survivors)
assert M*S.eye(15)[:,0] == S.Matrix([-S.Rational(1,2)] + [S.Rational(1,2)]*3 + [0]*11)
print(json.dumps({
    "source_model": "QPB1 K4 15-dimensional real unit-metric incidence flow",
    "raw_binary_embedding": "first four vertex and six edge coordinates in {0,1}; remaining 5 chain coordinates zero",
    "sample_parameter": "u=pi/2, dimensionless",
    "halfstep_operator": "I + A^2/2",
    "binary_candidates": 1024,
    "halfstep_embedded_survivors": survivors,
    "survivor_count": len(survivors),
    "all_survivors_have_edge_bits_zero": True,
    "fixed_candidates": fixed,
    "source_flow_kernel_dimension": 15-A.rank(),
    "status": "EXACT CONDITIONAL; not a canonical binary register interface",
    "physical_promotion": 0
}, indent=2, sort_keys=True))
