#!/usr/bin/env python3
"""Exact comparison of 72D twisted simplex and minimal CW skew generators.
Requires v0.6 standalone script sources in the same directory.
"""
import runpy,contextlib,io,json
from pathlib import Path
import sympy as s
P=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(P/'full_integral_bridge_v06.py'))
B=z['Bs'];d=z['target'];F=z['Sfin'];Q=z['Pfin']
def total(B,dims):
 off=[0]
 for v in dims:off.append(off[-1]+v)
 v=s.SparseMatrix(off[-1],off[-1],{})
 for k in range(1,len(dims)):
  blk=B[k] if isinstance(B,dict) else B[k-1]
  for i,j,c in s.SparseMatrix(blk).row_list():
   v[off[k-1]+i,off[k]+j]=c
 return v
Ds=total(B,[18,102,156,72]);Dc=total(d,[2,5,4,1])
As=Ds-Ds.T;Ac=Dc-Dc.T
Pmat=s.diag(*Q);Smat=s.diag(*F)
reverse=Ac*Pmat-Pmat*As
forward=As*Smat-Smat*Ac
def profile(A):
 v=[w for _,_,w in s.SparseMatrix(A).row_list() if w]
 return {'shape':list(A.shape),'nonzero_count':len(v),
         'Frobenius_squared':str(sum(x*x for x in v)),
         'rank_over_Q':int(A.rank())}
out={'source_metric':'unit Euclidean on twisted 348-coordinate simplex carrier',
     'target_metric':'unit Euclidean on 12-coordinate cellular carrier',
     'boundary_chain_intertwining':True,
     'reverse_skew_error':profile(reverse),
     'forward_skew_error':profile(forward),
     'skew_dynamical_intertwining':False,
     'warning':'integral chain equivalence does not imply metric-adjoint evolution equivalence',
     'physical_promotion':0,'status':'PASS_EXACT_NO_GO'}
assert out['reverse_skew_error']['Frobenius_squared']=='2842'
assert out['forward_skew_error']['Frobenius_squared']=='298'
assert out['reverse_skew_error']['rank_over_Q']==10
assert out['forward_skew_error']['rank_over_Q']==11
print(json.dumps(out,indent=2,sort_keys=True))
