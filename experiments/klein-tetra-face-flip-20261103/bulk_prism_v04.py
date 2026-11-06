#!/usr/bin/env python3
"""Exact barycentric 72-tet Delta-complex for K x I. SymPy; no physical units."""
from itertools import combinations
from collections import Counter
from sympy import zeros
import json
T=[(0,1,2),(0,2,3)]
PAIRS=[((0,1),(3,2),0,1),((0,3),(2,1),1,0),((0,2),(0,2),0,1)]
class UF:
 def __init__(self):self.p={}
 def root(self,a):
  if a not in self.p:self.p[a]=a
  while self.p[a]!=a:
   self.p[a]=self.p[self.p[a]];a=self.p[a]
  return a
 def union(self,a,b):self.p[self.root(a)]=self.root(b)
def key(q,d,s):return(q,d,tuple(sorted(s)))
local={};objects={}
for q,t in enumerate(T):
 v={(a,k) for a in t for k in (0,1)}
 e={frozenset((a,b)) for k in (0,1) for a,b in combinations(sorted((a,k) for a in t),2)}
 e|={frozenset(((a,0),(a,1))) for a in t}
 f={frozenset((a,k) for a in t) for k in (0,1)}
 f|={frozenset(((a,0),(a,1),(bb,0),(bb,1))) for a,bb in combinations(t,2)}
 local[q]=[set(frozenset([a]) for a in v),e,f,{frozenset(v)}]
 assert list(map(len,local[q]))==[6,9,5,1]
 for d,L in enumerate(local[q]):
  for s in L:objects[key(q,d,s)]=frozenset(s)
simp=[{} for i in range(4)]
for q in (0,1):
 for face in local[q][2]:
  for edge in local[q][1]:
   if not edge.issubset(face):continue
   for v in edge:
    flag=(key(q,0,frozenset([v])),key(q,1,edge),key(q,2,face),key(q,3,next(iter(local[q][3]))))
    for i in range(4):
     for s in combinations(flag,i+1):simp[i][s]=q
assert list(map(len,simp))==[42,148,180,72]
uf=[UF() for i in range(4)]
for i in range(4):
 for s in simp[i]:uf[i].root(s)
for (a,bb),(c,d),qa,qb in PAIRS:
 sideA=frozenset(((a,0),(a,1),(bb,0),(bb,1)))
 sideB=frozenset(((c,0),(c,1),(d,0),(d,1)))
 trans={(a,k):(c,k) for k in (0,1)}
 trans.update({(bb,k):(d,k) for k in (0,1)})
 for dim in range(3):
  for flag in simp[dim]:
   if not all(q==qa and objects[(q,j,cell)].issubset(sideA) for q,j,cell in flag):continue
   mapped=tuple(key(qb,j,frozenset(trans[v] for v in objects[(q,j,cell)])) for q,j,cell in flag)
   assert mapped in simp[dim]
   assert all(objects[z].issubset(sideB) for z in mapped)
   uf[dim].union(flag,mapped)
Q=[sorted({uf[i].root(a) for a in simp[i]}) for i in range(4)]
fvec=list(map(len,Q))
assert fvec==[18,102,156,72],fvec
index=[{a:j for j,a in enumerate(Q[i])} for i in range(4)]
B={}
for dim in (1,2,3):
 m=zeros(fvec[dim-1],fvec[dim])
 for col,flag in enumerate(Q[dim]):
  for j in range(dim+1):
   face=flag[:j]+flag[j+1:]
   m[index[dim-1][uf[dim-1].root(face)],col]+=(-1)**j
 B[dim]=m
assert B[1]*B[2]==zeros(fvec[0],fvec[2])
assert B[2]*B[3]==zeros(fvec[1],fvec[3])
faceinc=Counter()
for tet in simp[3]:
 for face in combinations(tet,3):faceinc[uf[2].root(face)]+=1
assert Counter(faceinc.values())=={2:132,1:24}
bdry=[face for face,num in faceinc.items() if num==1]
bs=[]
for layer in (0,1):
 faces=[face for face in bdry if any(k==2 and len(objects[(q,k,s)])==3 and all(v[1]==layer for v in objects[(q,k,s)]) for q,k,s in face)]
 vs={uf[0].root((v,)) for face in faces for v in face}
 es={uf[1].root(e) for face in faces for e in combinations(face,2)}
 assert (len(vs),len(es),len(faces))==(6,18,12)
 bs.append([len(vs),len(es),len(faces)])
ranks=[B[i].rank() for i in (1,2,3)]
assert ranks==[17,84,72],ranks
assert fvec[0]-ranks[0]==1 and fvec[1]-ranks[0]-ranks[1]==1
result={'model':'Klein two-face Delta quotient x interval, 2 triangular prisms barycentrically subdivided','f_vector':fvec,'tetrahedra':72,'internal_facets_twice':132,'boundary_facets_once':24,'boundary_components_f_vector':bs,'Euler':0,'boundary_ranks_Q':ranks,'Betti_R':[1,1,0,0],'boundary_squared_zero':True,'note':'Delta-complex labeled simplices remain distinct even if their vertex sets coincide','physical_promotion':0,'status':'PASS_EXACT_CONDITIONAL'}
print(json.dumps(result,sort_keys=True,indent=2))
