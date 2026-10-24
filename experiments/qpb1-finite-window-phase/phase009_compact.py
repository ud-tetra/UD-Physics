#!/usr/bin/env python3
"""Exact positive-quartic coefficient nonidentifiability; input sectors pinned to phase-008."""
from fractions import Fraction as F
from itertools import product
import argparse,json
from pathlib import Path
r0=(F(1,4),F(1,4),F(1,2))  # imported reference sector weights
r1=(F(2,3),F(0),F(1,3))  # different prepared carrier (vertex difference + top cell)
v=(F(1),F(-1),F(0))
def L(t):return [[(F(1) if i==j==2 else F(0))+t*v[i]*v[j] for j in range(3)] for i in range(3)]
def g(a,r):return tuple(F(1)+sum((a[i][j]*r[j] for j in range(3)),F(0)) for i in range(3))
def quartic(a,r):return sum((r[i]*a[i][j]*r[j] for i in range(3) for j in range(3)),F(0))
results=[]; grid=0
for t in map(F,['0','1/4','1/2','1','2']):
 a=L(t)
 assert a==[list(c) for c in zip(*a)]
 assert g(a,r0)==(1,1,F(3,2))
 assert quartic(a,r0)==F(1,4)
 for r in product([F(-1),F(0),F(1),F(2)],repeat=3):
  assert quartic(a,r)==r[2]**2+t*(r[0]-r[1])**2>=0
  grid+=1
 results.append({'t':str(t),'reference_g':list(map(str,g(a,r0))),'probe_g':list(map(str,g(a,r1)))})
assert results[0]['probe_g']==['1','1','4/3']
assert results[2]['probe_g']==['4/3','2/3','4/3']
# Sym(3) has six entries; the linear map L->Lr0 has rank three:
# its three diagonal variation columns are diag(r0), nonsingular.
assert r0[0]*r0[1]*r0[2]==F(1,32)
# L=E33+t vv^T is PSD for every real t>=0 and fixes Lr0, since v.r0=0.
assert sum((v[i]*r0[i] for i in range(3)),F(0))==0
summary={'status':'PASS','labels':['EXACT','CONDITIONAL','FIT','FAILED','OPEN'],
 'reference_r':list(map(str,r0)),'second_r':list(map(str,r1)),
 'family':'L(t)=E33+t*(1,-1,0)(1,-1,0)^T, t>=0',
 'energy':'H=||x||^2/2+(r^T L r)/4, r_k=x^T P_k x',
 'effective_gains':'g_i=1+sum_j L_ij*r_j',
 'positivity_identity':'r^T L(t) r=r3^2+t*(r1-r2)^2 >=0',
 'reference_map_rank':3,'symmetric_parameter_count':6,'kernel_dimension':3,
 'exact_grid_checks':grid,'examples':results,
 'one_prep_target':'g=(1,1,3/2) for all t>=0 (exposed, not predictive)',
 'alternate_prep':'t=0 gives (1,1,4/3); t=1/2 gives (4/3,2/3,4/3)',
 'linearization':'Original A at zero for every t; all sector supports are conserved',
 'physical_attribution':'FAILED: ordinary classical Hamiltonian with same Poisson A and H has identical dynamics',
 'source_selection':'OPEN; this family is an explicit exact counterexample to selection by listed symmetries/positivity/reference',
 'scope':'3-sector model; 15-register projectors and sign conventions verified in phase-008; no measured physics'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path)
 a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':summary['status'],'grid':grid,'rank':3,'kernel':3}))
