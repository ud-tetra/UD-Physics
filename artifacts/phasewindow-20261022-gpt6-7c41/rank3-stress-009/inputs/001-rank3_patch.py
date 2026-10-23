#!/usr/bin/env python3
"""EXACT rank-three partial-patch obstruction + icosahedron spectral stress.
Physical 12-vertex global energy barrier remains OPEN. Requires SymPy.
"""
import argparse,json
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
from pathlib import Path
import sympy as S

phi=(1+S.sqrt(5))/2
vertices=[]
for a in (-1,1):
 for b in (-1,1):
  vertices.extend([S.Matrix([0,a,b*phi])/2,S.Matrix([a,b*phi,0])/2,S.Matrix([b*phi,0,a])/2])
vertices.sort(key=lambda v:tuple(float(z) for z in v))
assert len(vertices)==12
V=S.Matrix.hstack(*vertices).T
R2=(5+S.sqrt(5))/8
assert S.simplify(V.T*V-4*R2*S.eye(3))==S.zeros(3)
A=S.zeros(12);edges=[]
for i,j in combinations(range(12),2):
 if S.simplify((vertices[i]-vertices[j]).dot(vertices[i]-vertices[j])-1)==0:
  A[i,j]=A[j,i]=1;edges.append((i,j))
assert len(edges)==30
faces=[tuple(t) for t in combinations(range(12),3)
       if all(A[i,j]==1 for i,j in combinations(t,2))]
assert len(faces)==20 and faces[0]==(0,1,2)
assert S.simplify(A*V-S.sqrt(5)*V)==S.zeros(12,3)
lam=S.Symbol("lam")
assert S.expand(A.charpoly(lam).as_expr()-(lam-5)*(lam+1)**5*(lam**2-5)**3)==0
Omega=S.sqrt(5)*S.eye(12)-A+(5-S.sqrt(5))/12*S.ones(12)
assert S.simplify(Omega*V)==S.zeros(12,3)
assert S.simplify(Omega*S.ones(12,1))==S.zeros(12,1)

def rt(q,d=10**9):
 assert q>0
 lo=F(isqrt(q.numerator*d*d//q.denominator),d)
 hi=lo+F(1,d)
 assert lo*lo<=q<hi*hi
 return lo,hi

def run(w):
 d=int(w["coordinate_denominator"])
 ids=list(map(int,w["original_vertex_ids"]))
 assert ids==list(range(9))
 X={int(i):tuple(F(int(t),d) for t in v) for i,v in w["free_coordinates"].items()}
 dep=w["dependent_face_vertex"]
 assert dep["id"]==2
 p=F(dep["p_numerator"],dep["p_denominator"])
 q=F(dep["q_numerator"],dep["q_denominator"])
 X[2]=tuple(p*X[0][k]+q*X[1][k] for k in range(3))
 assert S.Matrix([list(X[i]) for i in [0,1,2]]).det()==0
 assert S.Matrix([list(X[i]) for i in ids]).rank()==3
 e=[(i,j) for i,j in edges if i in X and j in X]
 assert len(e)==18
 radius_lo=F(9510565,10000000);radius_hi=F(9510566,10000000)
 assert radius_lo**2<R2<radius_hi**2
 alpha=F(w["alpha_numerator"],w["alpha_denominator"])
 total=alpha*alpha
 for i in ids:
  n=sum(z*z for z in X[i]);lo,hi=rt(n)
  slow=lo/radius_hi-1;shigh=hi/radius_lo-1
  total+=max(slow**2,shigh**2)
  total+=F(19,20)*max((slow-alpha)**2,(shigh-alpha)**2)
 for i,j in e:
  n=sum((X[i][k]-X[j][k])**2 for k in range(3))
  lo,hi=rt(n)
  total+=F(19,50)*max((lo-1)**2,(hi-1)**2)
 E=total/2
 assert E<F(1,20)<F(1360051,20000000)
 return {"evidence":"EXACT/CONDITIONAL","full_global_barrier":"OPEN",
  "partial_vertex_count":9,"partial_edge_count":18,
  "face_flat":"EXACT","patch_configuration_rank":3,
  "patch_energy_bound":"U9 < 1/20 < 1360051/20000000",
  "patch_energy_upper_float":float(E),
  "stress_charpoly":"(lam-5)(lam+1)^5(lam²-5)^3",
  "stress_inequality":"Omega >= (1+sqrt5)*(I-P0-PV) >= 0",
  "flat_3D_face_condition":"tr(YT Omega Y)>=(1+sqrt5)*sigma_min(VF B+1 tT)^2",
  "note":"Partial network has omitted positive springs. No full 12-vertex below-budget counterexample."}

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--witness",required=True)
 p.add_argument("--out",required=True)
 a=p.parse_args()
 result=run(json.loads(Path(a.witness).read_text()))
 Path(a.out).parent.mkdir(parents=True,exist_ok=True)
 Path(a.out).write_text(json.dumps(result,indent=2)+"\n")
 print("PASS rank3 partial patch and exact icosahedral adjacency/stress",result["patch_energy_upper_float"])
