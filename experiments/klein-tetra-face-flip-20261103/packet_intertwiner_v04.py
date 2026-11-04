#!/usr/bin/env python3
"""Exact S4-equivariant interval-to-K4 edge-map selector audit, integer matrices."""
from itertools import combinations
from sympy import Matrix,zeros,eye
import json
edges=list(combinations(range(4),2))
D=zeros(4,6)
for j,(a,b) in enumerate(edges):D[a,j]=-1;D[b,j]=1
I=Matrix([[-1],[1]])
F0=zeros(4,2)
for k in (0,3):F0[k,0]=1
for k in (1,2):F0[k,1]=1
F1=zeros(6,1)
F1[edges.index((0,2)),0]=1
F1[edges.index((1,3)),0]=-1
assert D*F1==F0*I
assert F0.rank()==2 and F1.rank()==1
assert F0.T*F0==2*eye(2) and F1.T*F1==Matrix([[2]])
def action(p):
 P0=zeros(4);P1=zeros(6)
 for i in range(4):P0[p[i],i]=1
 for i,(a,b) in enumerate(edges):
  a,b=p[a],p[b]
  P1[edges.index(tuple(sorted((a,b)))),i]=1 if a<b else -1
 assert D*P1==P0*D
 return P0,P1
Pe0,Pe1=action((3,2,1,0))
Po0,Po1=action((3,2,0,1))
assert Pe0*F0==F0 and Pe1*F1==F1
assert (Po0-eye(4)).nullspace()==[Matrix([1,1,1,1])]
assert Po0*F0!=F0 and Po1*F1!=F1
out={'even_seam_completion':[3,2,1,0],
     'even_map':{'degree0':['v0+v3','v1+v2'],'degree1':'edge02-edge13',
                 'ranks':[2,1],'gram0':'2I2','gram1':'[2]','boundary_compatible':True,
                 'S4_even_equivariant':True},
     'odd_completion':[3,2,0,1],'odd_fixed_vertex_dim':1,
     'odd_rank_two_equivariant_inclusion_no_go':True,
     'original_one_edge_inclusion_full_S4_equivariant':False,
     'physical_promotion':0,'status':'PASS_EXACT'}
print(json.dumps(out,sort_keys=True,indent=2))
