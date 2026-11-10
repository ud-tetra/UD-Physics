#!/usr/bin/env python3
"""Uniform symmetric reference: all-180 linearized *initial acceleration*
operator representation test, not time-propagated Green gain.
"""
import argparse,json
from pathlib import Path
import numpy as np
from verify_group import build_actions
from exact_channels import IRREPS,PHI,PSI
from nonaffine_audit import Mechanical,PROJ

def matrix_rep(a, count, indices):
 M=np.zeros((3*count,3*count))
 for old,new in enumerate(indices):
  M[3*new:3*new+3,3*old:3*old+3]=a['rt'].T
 return M

def main():
 pa=argparse.ArgumentParser();pa.add_argument('--out',type=Path,required=True);arg=pa.parse_args()
 eh=51/20000000
 m=Mechanical(nu=.05,beta=.005,cf=0)
 m.initial_gain_phase(eh)
 # Output 36 components, with 12 dimension-null affine modes.
 L=m.linear_initial_gain_matrix
 assert L.shape==(36,180)
 actions=build_actions()
 kernel=L@L.T
 maxerr=0.;maxcomm=0.
 projectors={name:np.zeros((36,36)) for name in IRREPS}
 clazz=['1','2','3','5a','5b']
 for a in actions:
  U90=matrix_rep(a,30,a['edge'])
  U=np.zeros((180,180));U[:90,:90]=U90;U[90:,90:]=U90
  V=matrix_rep(a,12,a['p'])
  maxerr=max(maxerr,float(np.max(np.abs(L@U-V@L))))
  maxcomm=max(maxcomm,float(np.max(np.abs(kernel@V-V@kernel))))
  for name,(dim,chi) in IRREPS.items():
   val=float(chi[clazz.index(a['cls'])].a)+float(chi[clazz.index(a['cls'])].b)*np.sqrt(5)
   projectors[name]+=dim/60*val*V
 assert maxerr<2e-14,(maxerr,maxcomm)
 assert maxcomm<2e-14
 plist=[]
 O=np.kron(PROJ,np.eye(3))
 for name,p in projectors.items():
  p=O@p@O
  assert np.max(np.abs(p@p-p))<1e-13
  assert np.max(np.abs(p-p.T))<1e-13
  eig=np.linalg.eigvalsh(p)
  expected={'1':0,'3':3,'3prime':3,'4':8,'5':10}[name]
  assert abs(np.trace(p)-expected)<1e-11
  plist.append(dict(irrep=name,projector_rank=expected,eigen_of_projected_gain=np.linalg.eigvalsh(p@kernel@p)[-expected:].tolist() if expected else [],trace_of_projected_gain=float(np.trace(p@kernel))))
 spectral=np.linalg.eigvalsh(kernel)
 positive=spectral[spectral>1e-16]
 assert len(positive)==24
 gain=float(np.sqrt(spectral[-1]))
 result={'status':'PASS','evidence':'NUMERICAL_CONSTRUCTOR','preparation':'uniform beta=.005 nu=.05 cf=0; symmetric reference rest state, only initial housing perturbation','energy_ball_radius':eh,'operator':'full 180 housing phases -> 36 projected shell acceleration components (rank 24), at initial instant only','shape':list(L.shape),'positive_eigenvalue_count':len(positive),'singular_gain_max_initial_acceleration':gain,'projected_sector_details':plist,'maximum_A5_intertwiner_error':maxerr,'maximum_commutator_error':maxcomm,'nonaffine_output_eigenvalues_ascending':positive.tolist(),'time_interval':'u=0 only','limitations':['This is a constructor check for the exact group-theoretic block constraint, not a bound on time-dependent Green propagation.','Source contains no uniform nonlinear remainder or u100 phase-ball theorem.']}
 arg.out.parent.mkdir(parents=True,exist_ok=True);arg.out.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS first-acceleration 180-phase operator A5 intertwinement: maxerror',maxerr,'gain',gain)
if __name__=='__main__':main()
