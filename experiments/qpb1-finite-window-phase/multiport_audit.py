#!/usr/bin/env python3
"""Exact 15-port tetrahedral incidence and one-bond perturbation audit."""
import argparse,json
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
s=[q for k in range(1,5) for q in combinations(range(4),k)]; ix={q:i for i,q in enumerate(s)}; n=15
def Z():return [[F(0) for j in range(n)] for i in range(n)]
def T(a):return [list(x) for x in zip(*a)]
def A(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def S(x,a):return [[x*y for y in row] for row in a]
def M(a,b):
 bt=T(b);return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in bt] for row in a]
def I():
 a=Z()
 for i in range(n):a[i][i]=F(1)
 return a
D=[Z() for k in range(3)]
for q in s:
 if len(q)>1:
  for j in range(len(q)):
   D[len(q)-2][ix[q[:j]+q[j+1:]]][ix[q]]=F((-1)**j)
K=[A(d,S(-1,T(d))) for d in D]; P=[S(F(-1,4),M(k,k)) for k in K]
assert all(M(K[i],K[j])==Z() for i in range(3) for j in range(3) if i!=j)
assert all(M(k,M(k,k))==S(-4,k) for k in K)
for p in permutations(range(4)):
 r=Z()
 for q in s:
  image=[p[v] for v in q]; inv=sum(x>y for i,x in enumerate(image) for y in image[i+1:])
  r[ix[tuple(sorted(image))]][ix[q]]=F((-1)**inv)
 assert M(T(r),r)==I() and all(M(r,k)==M(k,r) for k in K)
c=ix[(0,1,2,3)]; faces=[ix[tuple(v for v in range(4) if v!=j)] for j in range(4)]
edges=[i for i,q in enumerate(s) if len(q)==2]; verts=[i for i,q in enumerate(s) if len(q)==1]
assert [K[2][f][c] for f in faces]==[1,-1,1,-1]
assert [P[2][f][c] for f in faces]==[0,0,0,0] and P[2][c][c]==1
fixtures=0
for g in [(F(1),F(1),F(3,2)),(F(2),F(3),F(5)),(F(1,2),F(7,5),F(8,3))]:
 G=Z()
 for gain,k in zip(g,K):G=A(G,S(gain,k))
 q=I()
 for order in range(13):
  if order:q=M(q,G)
  assert all(q[i][c]==0 for i in edges+verts)
  assert [q[f][c] for f in faces]==([F((-1)**j)*g[2]*(-4*g[2]*g[2])**((order-1)//2) for j in range(4)] if order%2 else [0]*4)
  fixtures+=1
f0=faces[0];B=Z();B[f0][c]=1;B[c][f0]=-1
G=A(A(K[0],K[1]),S(F(3,2),K[2]));J=S(F(1,2),A(A(K[0],K[1]),K[2]))
for eps in [F(-1,3),F(-1,10),F(1,10),F(1,3)]:
 E=A(G,S(eps,B));q=M(E,E)
 assert [E[f][c] for f in faces]==[F(3,2)+eps,F(-3,2),F(3,2),F(-3,2)]
 assert all(q[e][c]/2==eps*D[1][e][f0]/2 for e in edges)
 assert M(E,J)!=M(J,E)
edge_coeff={str(s[e]):str(D[1][e][f0]/2) for e in edges if D[1][e][f0]}
result={'status':'PASS','method':'exact fractions; 15-register oriented tetrahedron','signed_S4_permutations':24,'gain_sets':3,'taylor_coefficients':fixtures,'single_bond_defect_fixtures':4,
 'cell_to_face_incidence':[1,-1,1,-1],'top_to_edges_all_t':0,'top_to_vertices_all_t':0,
 'uniform_transfer':'U(face_j,cell)=(-1)^j sin(2g3 t)/2; U(cell,cell)=cos(2g3 t)',
 'defect':'G_eps=G+eps B, B(face0,cell)=1, B(cell,face0)=-1',
 'edge_cell_t2_coefficient_per_eps':edge_coeff,'S4_and_J_under_defect':'BROKEN',
 'classical_null':'A 15-port conventional real skew network with same G and ports has identical exp(tG) for all t.',
 'evidence':'EXACT/CONDITIONAL constructor; no physical port map or unique UD attribution'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);args=ap.parse_args()
 args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True))
