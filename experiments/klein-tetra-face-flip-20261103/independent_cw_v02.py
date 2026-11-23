#!/usr/bin/env python3
"""Independent orientation cover from group relator, not triangle incidences."""
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
# Klein presentation: <h,v | h v h^-1 v>. w1(h)=1 and w1(v)=0.
edges=[('h',0),('h',1),('v',0),('v',1)]
B1=S.zeros(2,4); B2=S.zeros(4,2)
for k,(name,origin) in enumerate(edges):
 end=(origin^1) if name=='h' else origin
 B1[origin,k]-=1;B1[end,k]+=1
for start in (0,1):
 sheet=start
 for token in 'hvHv':
  name=token.lower()
  if token.islower(): e=(name,sheet);sheet=sheet^1 if name=='h' else sheet;orient=1
  else:
   origin=sheet^1 if name=='h' else sheet
   e=(name,origin);sheet=origin;orient=-1
  B2[edges.index(e),start]+=orient
 assert sheet==start
assert B1*B2==S.zeros(2,2)
assert B1.rank()==1 and B2.rank()==1
assert B2==S.Matrix([[0,0],[0,0],[1,1],[1,1]])
assert abs(int(smith_normal_form(B2,domain=ZZ)[0,0]))==1
assert B2*S.Matrix([1,-1])==S.zeros(4,1)
# H1 cover is Z^2: one tree edge h0; independent cycle generators h1, v0,v1
# and a primitive relation v0+v1, hence torsion-free rank 2.
assert abs(int(smith_normal_form(S.Matrix([[1],[1]]),domain=ZZ)[0,0]))==1
# Base relation has abelianization 2*v=0, hence Z + Z/2Z.
assert abs(int(smith_normal_form(S.Matrix([[0],[2]]),domain=ZZ)[0,0]))==2
result={"method":"independent Schreier cellular presentation",
 "base":{"cell_counts":[1,2,1],"relator":"h v h^-1 v","H1_Z":"Z+Z/2Z","H2_Z":"0"},
 "orientable_cover":{"cell_counts":[2,4,2],"B1":[[int(z) for z in row] for row in B1.tolist()],"B2":[[int(z) for z in row] for row in B2.tolist()],
  "rank_B1":1,"rank_B2":1,"Euler":0,"H1_Z":"Z^2","H2_Z":"Z",
  "connected":True,"no_H1_torsion":True},
 "orientation":{"h":"sheet switch","v":"sheet preserve"},
 "torus_control":{"relator":"h v h^-1 v^-1","w1":"zero"},
 "status":"PASS_EXACT","physical_promotion":0}
print(json.dumps(result,indent=2,sort_keys=True))
