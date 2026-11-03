#!/usr/bin/env python3
"""Same-runtime high-precision cross-check; not independent peer review."""
import json,sys
from pathlib import Path
from itertools import combinations
import sympy as S
import numpy as np
w=json.loads(Path(sys.argv[1]).read_text())
d=w["coordinate_denominator"]
x={int(i):S.Matrix([S.Rational(v,d) for v in row]) for i,row in w["free_coordinates"].items()}
dep=w["dependent_face_vertex"]
p=S.Rational(dep["p_numerator"],dep["p_denominator"])
q=S.Rational(dep["q_numerator"],dep["q_denominator"])
x[2]=p*x[0]+q*x[1]
assert S.Matrix.hstack(x[0],x[1],x[2]).det()==0
assert S.Matrix.hstack(*(x[i] for i in sorted(x))).rank()==3
phi=(1+S.sqrt(5))/2
v=[]
for a in (-1,1):
 for b in (-1,1):
  v.extend((S.Matrix([0,a,b*phi])/2,S.Matrix([a,b*phi,0])/2,S.Matrix([b*phi,0,a])/2))
v.sort(key=lambda z:tuple(float(y) for y in z))
edges=[(i,j) for i,j in combinations(range(12),2) if S.simplify((v[i]-v[j]).dot(v[i]-v[j])-1)==0]
ee=[(i,j) for i,j in edges if i in x and j in x]
R=S.sqrt((5+S.sqrt(5))/8)
alpha=S.Rational(w["alpha_numerator"],w["alpha_denominator"])
s=[S.sqrt(z.dot(z))/R-1 for z in x.values()]
e=[S.sqrt((x[i]-x[j]).dot(x[i]-x[j]))-1 for i,j in ee]
E=(alpha**2+sum(a*a for a in s)+S.Rational(19,20)*sum((a-alpha)**2 for a in s)+S.Rational(19,50)*sum(a*a for a in e))/2
assert len(ee)==18 and S.N(E,40)<S.Rational(1,20)
A=np.zeros((12,12))
for i,j in edges:A[i,j]=A[j,i]=1
expected=np.array([-np.sqrt(5)]*3+[-1]*5+[np.sqrt(5)]*3+[5])
assert np.max(abs(np.linalg.eigvalsh(A)-expected))<1e-12
print("PASS same-runtime numeric/SymPy check U9=",S.N(E,25))
