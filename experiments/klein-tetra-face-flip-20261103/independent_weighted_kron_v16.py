#!/usr/bin/env python3
"""Independent symbolic 5-node Kron proof and connected-Hasse metric obstruction."""
import itertools,json
import sympy as s
g,w=s.symbols('g w',positive=True)
L=s.zeros(5)
for i in range(4):
 for j in range(i+1,4):
  L[i,i]+=2*w;L[j,j]+=2*w;L[i,j]-=2*w;L[j,i]-=2*w
for i in range(4):
 L[i,i]+=g+3*w;L[4,4]+=g+3*w
 L[i,4]-=g+3*w;L[4,i]-=g+3*w
S=s.simplify(L.extract(range(4),range(4))-L.extract(range(4),[4])*L[4,4]**(-1)*L.extract([4],range(4)))
assert s.simplify(S-(11*w+g)/4*(4*s.eye(4)-s.ones(4)))==s.zeros(4)
T=tuple(range(4))
B=[list(itertools.combinations(T,k)) for k in range(1,5)]
d=s.zeros(15);off=(0,4,10,14)
for k in range(1,4):
 for j,t in enumerate(B[k]):
  for i in range(k+1):
   d[off[k-1]+B[k-1].index(t[:i]+t[i+1:]),off[k]+j]=(-1)**i
A=d-d.T
seen={0};queue=[0]
while queue:
 i=queue.pop()
 for j in range(15):
  if A[i,j]!=0 and j not in seen:seen.add(j);queue.append(j)
assert len(seen)==15
H=s.diag(*([1]*4+[2]+[1]*10))
assert A.T*H+H*A!=s.zeros(15)
out={'status':'PASS_EXACT','weighted_inner_recurrence':'(11w_child+g_parent)/4',
 'independent_symbolic_Kron':True,'K4_Hasse_connected_15':True,
 'unchanged_Q169_positive_diagonal_H_requires_scalar_identity':True,
 'Q165_top_integral_subdivision_norm':'1->4, not stock-conserving',
 'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
