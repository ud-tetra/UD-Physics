#!/usr/bin/env python3
"""Exact signed-S4 C7 irreps and minimal Fock/Kerr test; no quantum apparatus."""
import json,argparse
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
ss=[s for k in range(1,5) for s in combinations(range(4),k)]; ix={s:i for i,s in enumerate(ss)}
n=15
Z=lambda:[[F(0)]*n for _ in range(n)]
T=lambda a:[list(z) for z in zip(*a)]
M=lambda a,b:[[sum((u*v for u,v in zip(x,y)),F(0)) for y in T(b)] for x in a]
D=[Z() for i in range(3)]
for s in ss:
 if len(s)>1:
  for j in range(len(s)):D[len(s)-2][ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)
K=[[[d[i][j]-d[j][i] for j in range(n)] for i in range(n)] for d in D]
P=[[[-u/4 for u in x] for x in M(k,k)] for k in K]
assert [sum(p[i][i] for i in range(n)) for p in P]==[6,6,2]
J=[[sum(k[i][j] for k in K)/2 for j in range(n)] for i in range(n)]
def typ(p):
 v=set();d=[]
 for i in range(4):
  if i not in v:
   c=i;m=0
   while c not in v:v.add(c);c=p[c];m+=1
   d.append(m)
 return str(tuple(sorted(d,reverse=True)))
classrows={};counts={}
for perm in permutations(range(4)):
 R=Z()
 for s in ss:
  a=[perm[i] for i in s]
  sign=(-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
  R[ix[tuple(sorted(a))]][ix[s]]=sign
 for q in K+P+[J]:assert M(R,q)==M(q,R)
 row=tuple(int(sum(M(R,q)[i][i] for i in range(n))/2) for q in P)
 for q in P:assert sum(M(J,M(R,q))[i][i] for i in range(n))==0
 k=typ(perm);counts[k]=counts.get(k,0)+1
 if k in classrows:assert classrows[k]==row
 classrows[k]=row
expected={'(1, 1, 1, 1)':(3,3,1),'(2, 1, 1)':(1,-1,-1),
 '(2, 2)':(-1,-1,1),'(3, 1)':(0,0,1),'(4,)':(-1,1,-1)}
assert classrows==expected
orth=[[sum(F(counts[k],24)*classrows[k][i]*classrows[k][j] for k in expected) for j in range(3)] for i in range(3)]
assert orth==[[1,0,0],[0,1,0],[0,0,1]]
# Schur: three inequivalent complex irreps => Hermitian commutant real dim3.
def ladder(e,u):return [e*j+u*F(j*(j-1),2) for j in range(7)]
levels={}
for label,u in [('free',F(0)),('repulsive',F(1,4)),('softening_truncated',F(-1,4))]:
 a=ladder(F(5),u);diff=[a[i+1]-a[i] for i in range(6)]
 assert all(diff[i+1]-diff[i]==u for i in range(5))
 levels[label]={'U':str(u),'energies':list(map(str,a)),'adjacent_gaps':list(map(str,diff))}
# Finite bosonic commutator equals I_7 - 7|6><6|, not true CCR.
comm=[1]*6+[-6]
assert sum(comm)==0
res={'status':'PASS','evidence':['EXACT','CONDITIONAL','HYPOTHESIS','FAILED','OPEN'],
 'real_projector_ranks':[6,6,2],'complex_irrep_dimensions':[3,3,1],
 'S4_class_counts':counts,'characters':{k:list(v) for k,v in classrows.items()},
 'character_inner_product':[[str(v) for v in row] for row in orth],
 'Hermitian_commutant':'H=c1 P1+c2 P2+c3 P3; real dimension 3 under full S4 and J',
 'single_particle_levels_max':3,'Fock_extension':'new bosonic Hilbert/occupation rule NOT native',
 'illustrative_ladders':levels,'finite_Fock_commutator_diagonal':comm,
 'Kerr_U':'new independent coefficient; f12-f01=U, fitting measured values would be target exposure',
 'negative_Kerr_warning':'U<0 bare infinite Fock quadratic-number Hamiltonian unbounded below; truncated illustration only',
 'classical_null':'identical conventional bosonic/Kerr Hamiltonian yields identical results',
 'physical_action_time_port':'OPEN; no chi, tau0, transmon source, or measured raw f0j',
 'reopening':'source-selected quantum statistics, interaction and physical scales before heldout spectra'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(res,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'status':'PASS','characters':classrows,'irrep_test':'orthogonal','Fock_cases':list(levels)},sort_keys=True))
