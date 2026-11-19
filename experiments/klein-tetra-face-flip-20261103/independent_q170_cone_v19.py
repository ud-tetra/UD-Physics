#!/usr/bin/env python3
"""Independent exact combinatorial proof of K4 shell-to-cone current mismatch."""
from itertools import combinations
import sympy as s
import json
V=(0,1,2,3)
old_shell=[t for k in (1,2,3) for t in combinations(V,k)]
born=[tuple(sorted((*t,4))) for t in old_shell]
assert len(old_shell)==14 and len(set(born))==14
# Native A=D-D.T: A_(new_cone,old_simplex)=(-1)^(dim(old)+1)
L=s.diag(*[(-1)**len(t) for t in old_shell])
assert L.T*L==s.eye(14)
# Parent top boundary gives one signed row on four outer triangles.
b=s.zeros(14,1)
for i,t in enumerate(old_shell):
 if len(t)==3:
  missing=next(j for j in V if j not in t)
  b[i]=s.Rational((-1)**missing,2)
assert b.dot(b)==1
L0=-2*b.T
M=L0.T*L0-L.T*L
assert M==4*b*b.T-s.eye(14)
assert M.eigenvals()=={s.Integer(3):1,s.Integer(-1):13}
print(json.dumps({'status':'PASS_EXACT_INDEPENDENT',
 'shell_grades':[4,6,4],'new_cone_count':14,'new_centroid_count':1,
 'new_cone_gram':'I14','old_removed_top_gram':'4bbT',
 'shared_acceleration_difference_eigenvalues':{'3':1,'-1':13},
 'physical_promotion':0},indent=2))
