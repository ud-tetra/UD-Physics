#!/usr/bin/env python3
"""Independent exact five-vertex star-Kron recursion audit."""
import json
import sympy as s
w=s.symbols('w',nonnegative=True)
L=s.zeros(5)
# Four child tetrahedra: each old-old edge in two, each radial in three.
for i in range(4):
 for j in range(i+1,4):
  q=2*w
  L[i,i]+=q;L[j,j]+=q;L[i,j]-=q;L[j,i]-=q
for i in range(4):
 q=1+3*w
 L[i,i]+=q;L[4,4]+=q;L[i,4]-=q;L[4,i]-=q
K=s.simplify(L[:4,:4]-L[:4,4:5]*L[4:5,4:5].inv()*L[4:5,:4])
assert s.simplify(K-(11*w+1)/4*(4*s.eye(4)-s.ones(4)))==s.zeros(4)
for n in range(1,10):
 a=(s.Rational(11,4)**(n-1)-1)/7
 b=(s.Rational(11,4)**n-1)/7
 assert s.simplify((11*a+1)/4-b)==0
print(json.dumps({'status':'PASS_EXACT','old_edge_child_incidence':2,
 'radial_edge_child_incidence':3,'central_star_unit_weight':1,
 'derived_inner_recursion':'(11w+1)/4','closed_response':'(6+(11/4)^n)/7'},
 indent=2,sort_keys=True))
