#!/usr/bin/env python3
"""Construct six A5-adapted output seeds and recover the full 180-phase
initial-acceleration gain from six dual response vectors.

This is a NUMERICAL constructor, NOT the u100 moving-time propagator.
"""
import argparse,json
from pathlib import Path
import numpy as np
from verify_group import build_actions
from exact_channels import IRREPS
from nonaffine_audit import Mechanical,PROJ,EDGES

def group_matrix(a):
 V=np.zeros((36,36))
 for old,new in enumerate(a['p']):V[3*new:3*new+3,3*old:3*old+3]=a['rt'].T
 return V

def normed(v):
 n=float(np.linalg.norm(v));assert n>1e-8;return v/n

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);a=parser.parse_args()
 acts=build_actions();Vs=[group_matrix(g) for g in acts]
 C={name:np.zeros((36,36)) for name in IRREPS}
 classes=('1','2','3','5a','5b')
 for g,V in zip(acts,Vs):
  for name,(dim,chi) in IRREPS.items():
   cc=chi[classes.index(g['cls'])];val=float(cc.a)+float(cc.b)*np.sqrt(5)
   C[name]+=dim/60*val*V
 O=np.kron(PROJ,np.eye(3))
 for name in C:C[name]=O@C[name]@O
 # Vertex adjacency divides the residual vertex representation 3' (eigen -sqrt5)
 # and 5 (eigen -1), hence it separates the two copies of 4 and 5.
 A=np.zeros((12,12))
 for i,j in EDGES:A[i-1,j-1]=A[j-1,i-1]=1
 wa,Ua=np.linalg.eigh(A)
 assert np.max(abs(np.sort(wa)-np.sort(np.r_[5,np.repeat(np.sqrt(5),3),np.repeat(-np.sqrt(5),3),np.repeat(-1,5)])))<1e-12
 P3prime=Ua[:,abs(wa+np.sqrt(5))<1e-9]@Ua[:,abs(wa+np.sqrt(5))<1e-9].T
 P5=Ua[:,abs(wa+1)<1e-9]@Ua[:,abs(wa+1)<1e-9].T
 Q3=np.kron(P3prime,np.eye(3));Q5=np.kron(P5,np.eye(3))
 # Correct orthogonal A5 isotypic projectors and ranks.
 assert all(abs(np.trace(C[key])-num)<1e-11 for key,num in [('1',0),('3',3),('3prime',3),('4',8),('5',10)])
 rng=np.random.default_rng(20261024)
 seeds={}
 for key in ['3','3prime']:
  v=normed(C[key]@rng.normal(size=36))
  seeds[key]=[v]
 for key,dim in [('4',4),('5',5)]:
  S1=C[key]@Q3@C[key];S2=C[key]@Q5@C[key]
  assert abs(np.trace(S1)-dim)<1e-10 and abs(np.trace(S2)-dim)<1e-10
  a1=normed(S1@rng.normal(size=36));b2=normed(S2@rng.normal(size=36))
  # Group-average |b2><a1| into an exact intertwiner modulo roundoff.
  T=sum((np.outer(V@b2,V@a1) for V in Vs),np.zeros((36,36)))
  assert np.linalg.norm(T)>1e-7
  e1=normed(S1@rng.normal(size=36))
  e2=normed(T@e1)
  assert np.linalg.norm(S2@e2-e2)<1e-10
  assert abs(np.dot(e1,e2))<1e-12
  # Schur: T^T T scalar on the rank-d source copy.
  source_eigs=np.linalg.eigvalsh(S1@T.T@T@S1)[-dim:]
  assert np.ptp(source_eigs)<1e-10*max(source_eigs)
  seeds[key]=[e1,e2]

 m=Mechanical(beta=.005,nu=.05,cf=0);m.initial_gain_phase(51/20000000)
 L=m.linear_initial_gain_matrix;assert L.shape==(36,180)
 sector_data={};six=[];eig_reconstructed=[]
 for key,dim in [('3',3),('3prime',3),('4',4),('5',5)]:
  es=seeds[key];six.extend(es)
  # Each e requires one reverse response vector L^T e, width 180.
  rs=[L.T@e for e in es]
  B=np.array([[np.dot(r1,r2) for r2 in rs] for r1 in rs])
  eigs=np.linalg.eigvalsh(B)
  assert min(eigs)>=-1e-16
  eig_reconstructed.extend(float(v) for v in eigs for _ in range(dim))
  sector_data[key]={'dimension':dim,'multiplicity':len(es),'B':B.tolist(),'eigenvalues':eigs.tolist(),'output_seed_norms':[float(np.linalg.norm(e)) for e in es],'response_norms':[float(np.linalg.norm(x)) for x in rs]}
 assert len(six)==6
 exact=np.linalg.eigvalsh(L@L.T)
 comp=np.sort(np.array(eig_reconstructed))
 positive=exact[-24:]
 err=float(np.max(abs(comp-positive)))
 gain_full=np.sqrt(exact[-1]);gain_six=np.sqrt(comp[-1]);rel=abs(gain_six-gain_full)/gain_full
 assert err<1e-17 and rel<1e-12,(err,rel)
 # Relative block Gram basis is aligned by construction; six rows suffice.
 result={'status':'PASS','evidence':'NUMERICAL_CONSTRUCTOR','preparation':'uniform reference b=c=1, alpha=0; beta=.005 nu=.05 cf=0; Eh=51/20000000','number_of_seed_directions':6,'phase_dimension':180,'output_dimension':24,'group':'rotational A5 60 elements','construction':'real central character projectors and separate adjacency(-sqrt5,-1) vertex modes; group averaged cross-copy intertwiners','sector_data':sector_data,'full180_gain':float(gain_full),'six_seed_gain':float(gain_six),'gain_relative_difference':float(rel),'max_eigenvalue_absolute_difference':err,'note':'Exact algebraic decomposition verified in exact_channels.py; numerical six-seed constructor at u=0 only, not a certified moving Green norm at u100.'}
 a.out.parent.mkdir(exist_ok=True,parents=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS six A5 output seeds reconstruct full 180-phase initial acceleration gain',gain_six,'rel_error',rel)
if __name__=='__main__':main()
