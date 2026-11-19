#!/usr/bin/env python3
"""Exact graded cellular map C(K;rho) tensor C(I) to C(K;rho) tensor C(K4)."""
from itertools import combinations
from sympy import Matrix,zeros
import json
KD=[1,2,1];ID=[2,1];PD=[4,6,4,1]
KB=[None,Matrix([[-2,0]]),zeros(2,1)]
IB=[None,Matrix([[-1],[1]])]
PB=[None,zeros(4,6),zeros(6,4),zeros(4,1)]
for j,(a,b) in enumerate(combinations(range(4),2)):
 PB[1][a,j]=-1;PB[1][b,j]=1
for j,t in enumerate(combinations(range(4),3)):
 for k in range(3):
  e=tuple(t[x] for x in range(3) if x!=k)
  PB[2][list(combinations(range(4),2)).index(e),j]=(-1)**k
for k in range(4):PB[3][k,0]=(-1)**k
assert PB[1]*PB[2]==zeros(4,4) and PB[2]*PB[3]==zeros(6,1)
def tensor(d1,d2,b1,b2):
 levels=[[(p,q,i,j) for p in range(len(d1)) for q in range(len(d2)) if p+q==n for i in range(d1[p]) for j in range(d2[q])] for n in range(len(d1)+len(d2)-1)]
 ix=[{x:i for i,x in enumerate(l)} for l in levels]
 out=[]
 for n in range(1,len(levels)):
  mat=zeros(len(levels[n-1]),len(levels[n]))
  for j,(p,q,i,k) in enumerate(levels[n]):
   if p:
    for a in range(d1[p-1]):mat[ix[n-1][p-1,q,a,k],j]+=b1[p][a,i]
   if q:
    for a in range(d2[q-1]):mat[ix[n-1][p,q-1,i,a],j]+=(-1)**p*b2[q][a,k]
  out.append(mat)
 return levels,out
S,dS=tensor(KD,ID,KB,IB)
T,dT=tensor(KD,PD,KB,PB)
f={0:zeros(4,2),1:zeros(6,1)}
f[0][0,0]=1;f[0][1,1]=1;f[1][0,0]=1
assert PB[1]*f[1]==f[0]*IB[1]
M=[]
for n,level in enumerate(S):
 ix={x:i for i,x in enumerate(T[n])};mat=zeros(len(T[n]),len(level))
 for k,(p,q,i,j) in enumerate(level):
  for v in range(PD[q]):
   if f[q][v,j]:mat[ix[p,q,i,v],k]=f[q][v,j]
 M.append(mat)
for n in range(1,len(S)):
 assert dT[n-1]*M[n]==M[n-1]*dS[n-1]
for n in range(1,len(dS)):
 assert dS[n-1]*dS[n]==zeros(dS[n-1].rows,dS[n].cols)
assert [len(x) for x in S]==[2,5,4,1]
assert [len(x) for x in T]==[4,14,20,15,6,1]
assert [x.rank() for x in M]==[2,5,4,1]
assert all((-1)*mat==mat*(-1) for mat in M)
out={'domain':'cellular K x I with pulled back orientation rho','target':'twisted Klein CW tensor full K4 chain','domain_dims':[2,5,4,1],'target_dims':[4,14,20,15,6,1],'graded_chain_map_ranks':[2,5,4,1],'chain_map_exact':True,'holonomy_rho_h_equivariant':True,'not_checked':'explicit 72-Delta-simplex to cellular chain approximation; evolution/metric intertwiner','physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
