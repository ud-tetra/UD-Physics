#!/usr/bin/env python3
from itertools import combinations,permutations
from sympy import zeros,eye
import json
S=[list(combinations(range(4),k)) for k in (1,2,3,4)]
offset=[0,4,10,14]
d=zeros(15)
for k in (1,2,3):
 for j,t in enumerate(S[k]):
  for i in range(k+1):
   s=t[:i]+t[i+1:]
   d[offset[k-1]+S[k-1].index(s),offset[k]+j]=(-1)**i
assert d*d==zeros(15)
a=d-d.T
cases=[]
for p in permutations(range(4)):
 if p[0]!=3 or p[1]!=2:continue
 U=zeros(15)
 for k in range(4):
  for j,t in enumerate(S[k]):
   w=[p[i] for i in t]
   sign=(-1)**sum(w[i]>w[z] for i in range(len(w)) for z in range(i+1,len(w)))
   U[offset[k]+S[k].index(tuple(sorted(w))),offset[k]+j]=-sign
 assert U.T*U==eye(15) and U*d==d*U and U*a==a*U
 assert U**4==eye(15)
 cases.append({'vertex_map':list(p),'combined_top_sign':int(U[14,14]),
               'order':next(n for n in (1,2,3,4) if U**n==eye(15))})
assert len(cases)==2 and {q['combined_top_sign'] for q in cases}=={1,-1}
print(json.dumps({'edge_map':'01 -> 32','cases':cases,
  'both_commute_K4_boundary':True,'both_commute_K4_generator':True,
  'orientation_character':-1,'unique_packet_top_sign':False,
  'physical_promotion':0},indent=2))
