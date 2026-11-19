#!/usr/bin/env python3
"""Rational homological simplicial-to-cellular comparison; NOT canonical subdivision."""
import runpy,json
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parent
src=runpy.run_path(str(P/'twisted_72_boundary_v05.py'))
cell=runpy.run_path(str(P/'bulk_bridge_v04.py'))
Bs=src['boundary'];dC=cell['dS'];embed=cell['M'];d60=cell['dT']
ns=[18,102,156,72];nc=[2,5,4,1]
Phi=[S.zeros(nc[i],ns[i]) for i in range(4)]
norms=[]
for k in (1,2):
 # Orthogonal harmonic generators over Q in the chosen unit Euclidean metrics
 h=(Bs[k].col_join(Bs[k+1].T)).nullspace()
 t=(dC[k-1].col_join(dC[k].T)).nullspace()
 assert len(h)==len(t)==1
 h,t=h[0],t[0]
 Phi[k]=t*h.T/(h.dot(h))
 assert Phi[k]*h==t
 norms.append({'degree':k,'source_harmonic_norm_squared':str(h.dot(h)),
               'cellular_harmonic_norm_squared':str(t.dot(t))})
for k in (1,2,3):
 assert dC[k-1]*Phi[k]==Phi[k-1]*Bs[k]
 assert d60[k-1]*embed[k]*Phi[k]==embed[k-1]*Phi[k-1]*Bs[k]
assert [x.rank() for x in Phi]==[0,1,1,0]
assert [(embed[k]*Phi[k]).rank() for k in range(4)]==[0,1,1,0]
out={'model':'twisted 72-Delta -> minimal twisted CW KxI -> prior 60D CWxK4',
     'coefficient_field':'Q', 'selected_metric':'unit Euclidean coordinate metric',
     'formula':'Phi_k=t_k*h_k^T/(h_k^T*h_k) for k=1,2; Phi0=Phi3=0',
     'harmonic_norms':norms,
     'map_grades':[0,1,1,0], 'composition_ranks':[0,1,1,0],
     'chain_map_exact':True,'H1_H2_rational_isomorphism':True,
     'geometric_subdivision_retraction':False,
     'integral_torsion_H0_preserved':False,
     'canonical_under_source':'NO: chosen unit metric and harmonic representatives',
     'dynamics_intertwiner':'not established','physical_promotion':0,
     'status':'PASS_EXACT_NONCANONICAL'}
print(json.dumps(out,indent=2,sort_keys=True))
