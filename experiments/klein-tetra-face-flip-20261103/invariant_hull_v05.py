#!/usr/bin/env python3
"""Minimal dynamically invariant K4 carrier containing even-S4 seam interval image."""
from itertools import combinations
import sympy as S
import json
simp=[list(combinations(range(4),k)) for k in (1,2,3,4)]
off=(0,4,10,14);D=S.zeros(15)
for k in (1,2,3):
 for j,t in enumerate(simp[k]):
  for a in range(k+1):
   D[off[k-1]+simp[k-1].index(t[:a]+t[a+1:]),off[k]+j]=(-1)**a
A=D-D.T
assert D*D==S.zeros(15) and A**3==-4*A
F=S.zeros(15,3)
for i in (0,3):F[i,0]=1
for i in (1,2):F[i,1]=1
F[4+simp[1].index((0,2)),2]=1
F[4+simp[1].index((1,3)),2]=-1
assert F.rank()==3 and F.T*F==2*S.eye(3)
H=S.Matrix.hstack(*F.row_join(A*F).row_join(A*A*F).columnspace())
assert H.rank()==5
P=H*(H.T*H).inv()*H.T
assert P*A==A*P and P*F==F
assert (S.eye(15)-P)*A*H==S.zeros(15,5)
p=(3,2,1,0)
Rp=S.zeros(15)
for k in range(4):
 for j,t in enumerate(simp[k]):
  w=[p[v] for v in t]
  s=(-1)**sum(w[i]>w[jj] for i in range(len(w)) for jj in range(i+1,len(w)))
  Rp[off[k]+simp[k].index(tuple(sorted(w))),off[k]+j]=s
assert Rp*H==H and Rp*A==A*Rp and Rp.T*Rp==S.eye(15)
assert len((Rp-S.eye(15)).nullspace())==7
assert len((A*H).nullspace())==1
# On the selected invariant hull, topological twist with even S4 completion is -I.
Utw=-Rp
assert Utw*H==-H
for x in (H[:,0],H[:,1]+H[:,4]):
 assert (x.T*Utw*x)[0]==-(x.T*x)[0]
 assert (x.T*Rp*x)[0]==(x.T*x)[0]
out={'initial_even_equivariant_interval_rank':3,
     'minimal_A_invariant_K4_hull_rank':5,
     'even_S4_fixed_K4_chain_dimension':7,
     'hull_harmonic_dim':1,'hull_active_dim':4,
     'hull_projector_commutes_with_A':True,
     'global_twist_holonomy_on_hull':'-I5',
     'null_even_transport_on_hull':'+I5',
     'framed_K4_unit_metric_correlation':'<x,Utw x>=-||x||^2; null +||x||^2',
     'no_new_phase_or_coefficient':True,
     'readout_requires_physical_orientation_reference':True,
     'full_72_bulk_dynamic_intertwiner':'OPEN',
     'selected_even_extension':'ASSUMED, not fixed by seam geometry',
     'physical_promotion':0,'status':'PASS_EXACT_CONDITIONAL'}
print(json.dumps(out,indent=2,sort_keys=True))
