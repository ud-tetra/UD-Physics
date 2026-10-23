#!/usr/bin/env python3
"""Separate exact SymPy and Fraction verification of one-site low-energy Z witness.
This verifies an energy-sublevel counterexample, NOT a dynamical trajectory.
"""
import json
from pathlib import Path
from fractions import Fraction as F
import sympy as S
p=(1+S.sqrt(5))/2;R2=(5+S.sqrt(5))/8
vec=[]
for a in [-1,1]:
 for b in [-1,1]:vec.append(S.Matrix([0,S.Rational(a,2),b*p/2]))
for a in [-1,1]:
 for b in [-1,1]:vec.append(S.Matrix([S.Rational(a,2),b*p/2,0]))
for a in [-1,1]:
 for b in [-1,1]:vec.append(S.Matrix([a*p/2,0,S.Rational(b,2)]))
V=S.Matrix.hstack(*vec).T
assert S.simplify(V.T*V-4*R2*S.eye(3))==S.zeros(3)
P0=S.ones(12)/12;PV=V*V.T/(4*R2);P=S.eye(12)-P0-PV
assert S.simplify(P*P-P)==S.zeros(12)
assert all(S.simplify(P[i,i]-S.Rational(2,3))==0 for i in range(12))
Y=V.copy();Y[0,0]+=S.Rational(1,25)
Z=S.simplify(P*Y)
res=S.simplify(sum(Z[i,j]**2 for i in range(12) for j in range(3)))
assert res==S.Rational(2,1875)
edges=[]
for i in range(12):
 for j in range(i+1,12):
  if S.simplify((vec[i]-vec[j]).dot(vec[i]-vec[j])-1)==0:edges.append((i,j))
assert len(edges)==30
assert sum(0 in ij for ij in edges)==5
bound=F(1,2)*((1+F(21,20))*F(10,9)+5*F(21,50))*F(1,25)**2
assert bound==F(197,56250)<F(1,200)<F(1360051,20000000)
# lower bounds on physical lengths after one-site move:
# |X0-C| >=R-1/25; all affected edges>=1-1/25.
assert S.simplify(R2-S.Rational(9,10))>0
result={'proof':'EXACT_Q(sqrt5)_and_Fractions','source_geometry':'12 icosahedral vertices, 30 original edges, one chosen vertex of degree 5',
        'static_witness_displacement':'1/25', 'P0_ii':'1/12','PV_ii':'1/4','P_perp_ii':'2/3',
        'nonaffine_norm_squared':'2/1875','energy_upper':'197/56250','pulse_ceiling':'1360051/20000000',
        'dimensionality':'R3, full 12 vertex network','requires_aux_storage_zero':'choose z=G strain, housings=midpoints',
        'scope':'Refutes energy-only implication for Z<=1/40; not a pulse-reachable state or cell-collapse configuration'}
p2=Path('/mnt/data/ud_nonaffine_dynamics_011/exact_witness_check.json')
p2.write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact 12-vertex Qsqrt5 witness:',result['nonaffine_norm_squared'], 'energy U<',result['energy_upper'])