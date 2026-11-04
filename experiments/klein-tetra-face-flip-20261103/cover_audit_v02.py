#!/usr/bin/env python3
"""Exact Klein K4 face-patch seam, 2-sheet triangle cover and flat O2 transport."""
import itertools, json, math
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

TRIS=((0,1,2),(0,2,3))
# Per triangle, boundary side: tail,head,identified edge,orientation sign
SIDES={(0,0):(1,2,"v",-1),(0,1):(2,0,"x",-1),(0,2):(0,1,"h",1),
       (1,0):(2,3,"h",-1),(1,1):(3,0,"v",-1),(1,2):(0,2,"x",1)}
MATCH={z:[k for k,a in SIDES.items() if a[2]==z] for z in "hvx"}
class UF:
 def __init__(self,n):self.p=list(range(n))
 def root(self,i):
  while self.p[i]!=i:i=self.p[i]
  return i
 def union(self,i,j):self.p[self.root(i)]=self.root(j)

def lift():
 uf=UF(12)
 idx={(f,s,v):3*(2*f+s)+k for f,t in enumerate(TRIS) for s in (0,1) for k,v in enumerate(t)}
 pairs=[]
 for z,((f,k),(g,l)) in MATCH.items():
  a,b,_,sgn=SIDES[f,k];c,d,_,sgn2=SIDES[g,l]
  for s in (0,1):
   t=s if sgn!=sgn2 else 1-s
   rel=((a,d),(b,c)) if sgn!=sgn2 else ((a,c),(b,d))
   for v,w in rel:uf.union(idx[f,s,v],idx[g,t,w])
   pairs.append(((f,s,k),(g,t,l)))
 cls=sorted({uf.root(k) for k in range(12)})
 ids={u:i for i,u in enumerate(cls)}
 vimap={k:ids[uf.root(z)] for k,z in idx.items()}
 edges=[];seen=set()
 for pair in pairs:
  if pair[0] in seen:continue
  seen.update(pair);edges.append(pair)
 assert len(edges)==6 and len(seen)==12 and len(cls)==2
 B1=S.zeros(2,6);B2=S.zeros(6,4)
 for k,(aa,bb) in enumerate(edges):
  f,s,j=aa;a,b,_,sign=SIDES[f,j]
  B1[vimap[f,s,a],k]-=1;B1[vimap[f,s,b],k]+=1
  for ff,ss,ll in (aa,bb):
   rel=1 if SIDES[ff,ll][3]==sign else -1
   B2[k,2*ff+ss]+=rel
 assert B1*B2==S.zeros(2,4)
 return B1,B2,edges

B1,B2,edges=lift()
assert B1.rank()==1 and B2.rank()==3
sn=smith_normal_form(B2,domain=ZZ)
assert [abs(int(sn[i,i])) for i in range(3)]==[1,1,1]
assert B2.nullspace()==[S.Matrix([-1,1,-1,1])]
# Integral H1 torsion: express im B2 in fundamental cycle basis
cycles=B2[1:,:]
minors=[int(cycles.extract(rows,cols).det()) for rows in itertools.combinations(range(5),3)
        for cols in itertools.combinations(range(4),3)]
assert math.gcd(*[abs(v) for v in minors])==1
baseB2=S.Matrix([[1,-1],[-1,-1],[-1,1]])
assert baseB2.rank()==2
assert [abs(int(smith_normal_form(baseB2,domain=ZZ)[i,i])) for i in range(2)]==[1,2]
# Orientation character on base edges h,v,x, and its trivialization on cover
w=S.Matrix([1,0,1])
assert all(int(q)%2==0 for q in w.T*baseB2)
pull=S.Matrix([1 if SIDES[a[0],a[2]][2] in ("h","x") else 0 for a,_ in edges])
potential=S.Matrix([0,1])
assert all(int(q)%2==0 for q in pull-B1.T*potential)
# Exact flat O(2) seam on Klein fundamental group
F=S.diag(1,-1);R=S.Matrix([[0,-1],[1,0]]);X=R*F;I=S.eye(2)
assert F*R.inv()*X.inv()==I
assert F.inv()*R.inv()*X==I
assert F*R*F.inv()==R.inv()
assert int(F.det())==-1 and int(R.det())==1
assert F*F==I
for G in (F,R,X):assert int((G*F*G.inv()).det())==-1
result={
 "source":"two adjacent K4 face patches [012],[023]; new boundary edge gluing",
 "base":{"cells":[1,3,2],"Euler":0,"B2":baseB2.tolist(),
         "Smith":[1,2],"H1_Z":"Z + Z/2Z","H2_Z":"0","orientation_w1":[1,0,1]},
 "cover":{"cells":[2,6,4],"Euler":0,"B1":B1.tolist(),"B2":B2.tolist(),
          "rank_B1":1,"rank_B2":3,"Smith_B2":[1,1,1],
          "gcd_cycle_minors":1,"H1_Z":"Z^2","H2_Z":"Z",
          "pulled_back_w1":"exact modulo 2, 0-cochain=(0,1)"},
 "transport":{"U_h":"reflection F","U_v":"quarter rotation R, angle not selected",
              "U_x":"R F","face_holonomy":["I","I"],
              "det_twist_loop":-1,"det_twist_twice":1,
              "gauge_conjugation_invariant":True},
 "scope":"two-dimensional seam quotient of tetrahedral triangular face patches; not a closed 3D tetrahedral bulk or physical dynamics",
 "physical_promotion":0,"status":"PASS_EXACT_CONDITIONAL"
}
print(json.dumps(result,indent=2,sort_keys=True))
