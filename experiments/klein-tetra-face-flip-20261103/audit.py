#!/usr/bin/env python3
"""Exact tetrahedron whole-face pairing and Klein two-triangle Delta-complex audit."""
from itertools import combinations,permutations
from collections import Counter
from math import gcd
from functools import reduce
import json

faces=[tuple(x for x in range(4) if x!=v) for v in range(4)]
edges=list(combinations(range(4),2))
class UF:
 def __init__(self,n):self.p=list(range(n))
 def find(self,x):
  while self.p[x]!=x:x=self.p[x]
  return x
 def join(self,a,b):self.p[self.find(a)]=self.find(b)
matchings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
profiles=Counter()
valid=[]
for m in matchings:
 for p in permutations(faces[m[0][1]]):
  for q in permutations(faces[m[1][1]]):
   uv,ue=UF(4),UF(6)
   for (a,b),dst in zip(m,(p,q)):
    src=faces[a]
    for v,w in zip(src,dst):uv.join(v,w)
    for i,j in combinations(range(3),2):
     ei=edges.index(tuple(sorted((src[i],src[j]))))
     ej=edges.index(tuple(sorted((dst[i],dst[j]))))
     ue.join(ei,ej)
   V=len({uv.find(i) for i in range(4)})
   E=len({ue.find(i) for i in range(6)})
   rep=[faces[m[0][0]],faces[m[1][0]]]
   counts=Counter(ue.find(edges.index(e)) for f in rep for e in combinations(f,2))
   sides=tuple(sorted(counts.values()))
   profiles[(V,E,sides)]+=1
   if sides==(2,2,2):valid.append((m,p,q))
assert sum(profiles.values())==108
assert len(valid)==0
# K: square ABCD cut into two oriented triangles ABC and ACD.
# Edges H=AB=DC, V=AD=CB (twist), X=AC. Integral B2 columns:
BK=((1,-1),(-1,-1),(-1,1))
# T: same square without twist, edge map H=AB=DC, V=AD=BC.
BT=((1,-1),(1,-1),(-1,1))
minors=[BK[i][0]*BK[j][1]-BK[j][0]*BK[i][1] for i,j in combinations(range(3),2)]
assert minors==[-2,0,-2] and reduce(gcd,map(abs,minors))==2
assert tuple(sum(BK[i]) for i in range(3))==(0,-2,0)
assert tuple(sum(BT[i]) for i in range(3))==(0,0,0)
# w1 loop character: H reverses local orientation, V preserves it.
w1=(1,0,1)
assert all(sum(BK[i][j]*w1[i] for i in range(3))%2==0 for j in range(2))
def mm(A,B):
 return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
F=((1,0),(0,-1)); Q=((0,-1),(1,0));Id=((1,0),(0,1))
assert mm(F,F)==Id and mm(mm(mm(F,Q),F),Q)==Id
assert mm(mm(F,Q),F)==((0,1),(-1,0))
out={
 "Klein_Delta_complex":{"V":1,"E":3,"F":2,"Euler":0,"B1":[[0,0,0]],"B2":[list(x) for x in BK],
  "rank_B2_Q":2,"rank_B2_F2":1,"Smith_nonzero":[1,2],"H1_Z":"Z + Z/2Z","H2_Z":"0",
  "boundary_of_sum_of_faces":[0,-2,0],"orientation_w1":{"H":1,"V":0,"X":1}},
 "tetra_shell":{"V":4,"E":6,"F":4,"Euler":2,"H1_Z":"0","H2_Z":"Z"},
 "whole_face_pairs":{"total":108,"closed_surface_2_incident_edge_cases":0,
  "patterns":[{"V":v,"E":e,"side_profile":list(p),"count":n}
  for (v,e,p),n in sorted(profiles.items())]},
 "torus_control":{"B2":[list(x) for x in BT],"rank_B2_Q":1,"H1_Z":"Z^2","H2_Z":"Z"},
 "O2_transport":{"twist":"reflection diag(1,-1)","phase":"R_pi/2","relation":"F R F^-1 R=I",
  "general_phase_angle":"undetermined; pi/2 exact fixture only"},
 "scope":"Delta-complex quotient requires a NEW gluing interface; not a standard 4-face tetrahedron simplicial structure",
 "physical_promotion":0,"status":"EXACT_PASS"
}
print(json.dumps(out,sort_keys=True,indent=2))
