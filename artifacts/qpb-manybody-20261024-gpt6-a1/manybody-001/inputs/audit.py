#!/usr/bin/env python3
"""Exact S4 symmetric-square / Kerr-coefficient nonselection audit; no physics fit."""
import argparse,json
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

def typ(p):
 seen=set();out=[]
 for i in range(4):
  if i not in seen:
   k,n=i,0
   while k not in seen:seen.add(k);k=p[k];n+=1
   out.append(n)
 return tuple(sorted(out,reverse=True))
classes={
 (1,1,1,1):(1,7,[1,1,2,3,3]),
 (2,1,1):(6,-1,[1,-1,0,1,-1]),
 (2,2):(3,-1,[1,1,2,-1,-1]),
 (3,1):(8,1,[1,1,-1,0,0]),
 (4,):(6,-1,[1,-1,0,-1,1])}
counts={k:0 for k in classes};sym={}
for p in permutations(range(4)):
 k=typ(p);counts[k]+=1;q=typ(tuple(p[p[i]] for i in range(4)))
 n=(classes[k][1]**2+classes[q][1]);assert n%2==0
 if k in sym:assert sym[k]==n//2
 sym[k]=n//2
assert counts=={k:v[0] for k,v in classes.items()}
assert sym=={(1,1,1,1):28,(2,1,1):4,(2,2):4,(3,1):1,(4,):0}
mult=[]
for j in range(5):
 n=sum(classes[k][0]*sym[k]*classes[k][2][j] for k in classes)
 assert n%24==0;mult.append(n//24)
assert mult==[3,1,3,4,2]
assert sum(a*b for a,b in zip(mult,[1,1,2,3,3]))==28
assert sum(m*m for m in mult)==39
# One-particle S4/J Hermitian commutant dim3; add 36 non-onebody directions.
examples=[]
for r in (F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(1)):
 e=F(2);U=r*e
 assert U>=0 and 2*e+U>=2*e
 examples.append({'U_over_epsilon':str(r),'two_hidden_energy_over_epsilon':str((2*e+U)/e)})
# OPTIONAL external mapping exp[-i(U/epsilon)*2pi]=i^k; k=1,3.
alias=[]
for k in (1,3):
 values=[F(j)-F(k,4) for j in range(1,5)]
 assert all((-4*v-k).denominator==1 and int(-4*v-k)%4==0 for v in values)
 alias.append({'primitive_k':k,'ratios':[str(v) for v in values]})
assert alias[0]['ratios'][0]=='3/4' and alias[1]['ratios'][0]=='1/4'
result={'status':'PASS','labels':['EXACT','CONDITIONAL','HYPOTHESIS','FAILED','OPEN'],
 'native_C7':'3+3prime+sign1prime; full signed S4, complex J; read-only source',
 'sym2_dim':28,'class_counts':{str(k):v for k,v in counts.items()},
 'sym2_character':{str(k):v for k,v in sym.items()},
 'irrep_names':['1','1prime','2','3','3prime'],'irrep_mult':mult,
 'hermitian_commutant_real_dim':39,'onebody_commutant_real_dim':3,
 'additional_two_particle_directions':36,
 'projector_interaction':'dGamma(h)+U*|hh><hh|, U>=0 is S4 invariant, source does not choose U',
 'positive_U_examples':examples,
 'optional_phase_map':'NEW premise exp(-i 2pi U/epsilon)=i^k at native s=pi with epsilon/chi=2; not source-derived',
 'phase_aliases':alias,
 'finite_pairing_scope':'UD D=Z4^2 perfect pairing, primitive k=1,3 not Hamiltonian; no S4-invariant scalar quadratic refinement',
 'conventional_null':'same two-boson projector/Kerr Hamiltonian produces identical readouts',
 'source_selection':'FAILED; even forcing primitive phase leaves two character classes and infinite energy aliases',
 'physical_status':'OPEN chi,tau0, boson statistics, physical source coupling, port and unused empirical spectra; no physical experiment'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'status':'PASS','mult':mult,'commutant':39,'aliases':alias},sort_keys=True))
