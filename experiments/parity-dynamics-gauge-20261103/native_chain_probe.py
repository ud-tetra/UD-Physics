#!/usr/bin/env python3
"""Source-bound exact observability of QPB1 unit-metric K4 incidence flow.
Requires sympy; no empirical input. Reproduce: python3 native_chain_probe.py
"""
import itertools,json
import sympy as s
V=range(4)
faces=[list(itertools.combinations(V,k+1)) for k in range(4)]
off=[0,4,10,14]
D=s.zeros(15)
for k in (1,2,3):
 for j,t in enumerate(faces[k]):
  for i in range(k+1):
   u=t[:i]+t[i+1:]
   D[off[k-1]+faces[k-1].index(u),off[k]+j]=(-1)**i
A=D-D.T
C=s.zeros(6,15)
for i in range(6):C[i,4+i]=1
O=C
ranks=[O.rank()]
for k in range(1,16):
 O=O.col_join(C*A**k)
 ranks.append(O.rank())
 if ranks[-1]==15:break
AC=A[:,0:4]
D1=D[:4,4:10]
D2=D[4:10,10:14]
assert D*D==s.zeros(15)
assert A.T==-A
assert D1.rank()==3 and D2.rank()==3
v=s.zeros(15,1);v[0]=1
zero=s.zeros(15,1)
assert C*v == C*zero
assert C*A*v != C*A*zero
assert A**3+4*A==s.zeros(15)
assert C*A**2+4*C==s.zeros(6,15)
constant=s.zeros(15,1)
for i in range(4):constant[i]=1
top=s.zeros(15,1);top[14]=1
face=D*top
assert all(O*x==s.zeros(O.rows,1) for x in (constant,top,face))
assert s.Matrix.hstack(constant,top,face).rank()==3
assert ranks[-1]==12
print(json.dumps({'chain_dim':15,'f_vector':[4,6,4,1],'rank_D1':D1.rank(),'rank_D2':D2.rank(),'edge_readout_rank':C.rank(),'edge_observability_ranks_by_derivative':ranks,'edge_unobservable_dim':15-ranks[-1],'edge_evolution_closure':False,'witness_edge_readout':'same zero','witness_edge_derivative_0':[str(z) for z in C*A*zero],'witness_edge_derivative_vertex0':[str(z) for z in C*A*v],'source_status':'source-native unit-metric linear flow, not raw binary model','physical_promotion':0},indent=2))
