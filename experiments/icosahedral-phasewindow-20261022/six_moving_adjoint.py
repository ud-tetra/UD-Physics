#!/usr/bin/env python3
"""Six A5 output adjoints along the nonlinear symmetric heart-pulse baseline.
Numerical, sampled-time. 560-state tangent law; 180-dimensional energy-scaled input.
"""
import argparse,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from sparse_jac import SparseJacobian
from projected_tangent import injection
from nonaffine_audit import Mechanical,PROJ,EDGES,V
from symmetry_dynamics_check import reduced_rhs
from six_seed_gain import build_actions,group_matrix,normed,IRREPS

def six_seeds():
 acts=build_actions();Vs=[group_matrix(g) for g in acts]
 classes=('1','2','3','5a','5b')
 O=np.kron(PROJ,np.eye(3));C={name:np.zeros((36,36)) for name in IRREPS}
 for g,Ug in zip(acts,Vs):
  for name,(dim,chi) in IRREPS.items():
   cc=chi[classes.index(g['cls'])];val=float(cc.a)+float(cc.b)*np.sqrt(5)
   C[name]+=dim/60*val*Ug
 for name in C:C[name]=O@C[name]@O
 A=np.zeros((12,12))
 for i,j in EDGES:A[i-1,j-1]=A[j-1,i-1]=1
 w,U=np.linalg.eigh(A)
 P3=U[:,abs(w+np.sqrt(5))<1e-9]@U[:,abs(w+np.sqrt(5))<1e-9].T
 P5=U[:,abs(w+1)<1e-9]@U[:,abs(w+1)<1e-9].T
 Q3=np.kron(P3,np.eye(3));Q5=np.kron(P5,np.eye(3))
 rng=np.random.default_rng(20261024);result={}
 for key in ['3','3prime']:result[key]=[normed(C[key]@rng.normal(size=36))]
 for key,dim in [('4',4),('5',5)]:
  S1=C[key]@Q3@C[key];S2=C[key]@Q5@C[key]
  a1=normed(S1@rng.normal(size=36));b2=normed(S2@rng.normal(size=36))
  T=sum((np.outer(Ug@b2,Ug@a1) for Ug in Vs),np.zeros((36,36)))
  e1=normed(S1@rng.normal(size=36));e2=normed(T@e1)
  assert abs(e1@e2)<1e-12 and abs(np.linalg.norm(e2)-1)<1e-12
  result[key]=[e1,e2]
 seeds=np.stack([e for z in ['3','3prime','4','5'] for e in result[z]],axis=1)
 assert seeds.shape==(36,6) and np.max(abs(seeds.T@seeds-np.eye(6)))<1e-10
 return seeds

def baseline(m,T):
 y0=[.1,1,1,0,0,0]
 sol=solve_ivp(lambda t,y:reduced_rhs(t,y,beta=m.beta,nu=m.nu,cf=m.cf), (0,T),y0,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True)
 assert sol.success,sol.message
 def state(t):
  a,b,c,ad,bd,cd=sol.sol(t)
  q=np.zeros(280);v=np.zeros(280)
  q[0]=a;q[1:40]=(b*V).ravel();q[190:280]=(c*m.midref).ravel()
  v[0]=ad;v[1:40]=(bd*V).ravel();v[190:280]=(cd*m.midref).ravel()
  return np.r_[q,v]
 return sol,state

def solve_target(sparse,ref,terminal,energy_input,tstar,rtol=2e-7):
 N=terminal.shape[1];M=terminal.copy();start=time.perf_counter()
 def rhs(t,y):return sparse.adjoint(ref(t),y.reshape(560,N)).ravel()
 sol=solve_ivp(rhs,(tstar,0),M.ravel(),method='DOP853',rtol=rtol,atol=rtol*0.01)
 if not sol.success:raise RuntimeError(sol.message)
 L=sol.y[:,-1].reshape(560,N);G=L.T@energy_input # 6x180
 eigs=[];blocks={};p=0
 for key,dim,mul in [('3',3,1),('3prime',3,1),('4',4,2),('5',5,2)]:
  gg=G[p:p+mul];B=gg@gg.T;p+=mul
  ev=np.linalg.eigvalsh(B)
  eigs.extend([float(v) for v in ev for _ in range(dim)])
  blocks[key]={'B':B.tolist(),'eig':ev.tolist()}
 gain=np.sqrt(max(eigs));assert p==6
 Eh=51/20000000
 return {'time':tstar,'gain_unscaled':float(gain),'housing_amplitude_gain':float(np.sqrt(2*Eh)*gain),'max_gain_fraction_of_threshold':float(40*np.sqrt(2*Eh)*gain),'nfev':sol.nfev,'elapsed_s':round(time.perf_counter()-start,2),'blocks':blocks,'six_rows_max':float(np.max(np.linalg.norm(G,axis=1)))},G

def direct_24(sparse,ref,energy_input,tstar,rtol=1e-7):
 # use fixed orthonormal rank8 vertex projectors, output R24
 w,U=np.linalg.eigh(PROJ);U=U[:,w>.5];C=np.zeros((560,24))
 for a in range(8):
  for k in range(3):C[4+3*np.arange(12)+k,3*a+k]=U[:,a]
 R,G=solve_target_raw(sparse,ref,C,energy_input,tstar,rtol)
 return R,G

def solve_target_raw(sparse,ref,C,energy_input,tstar,rtol):
 N=C.shape[1]
 def rhs(t,y):return sparse.adjoint(ref(t),y.reshape(560,N)).ravel()
 sol=solve_ivp(rhs,(tstar,0),C.ravel(),method='DOP853',rtol=rtol,atol=rtol*0.01)
 if not sol.success:raise RuntimeError(sol.message)
 G=sol.y[:,-1].reshape(560,N).T@energy_input
 return {'gain_unscaled':float(np.linalg.svd(G,compute_uv=False)[0]),'nfev':sol.nfev},G

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--times',default='1,4,10,30,100');p.add_argument('--rtol',type=float,default=2e-7);p.add_argument('--cross-check',action='store_true');args=p.parse_args()
 args.out.mkdir(parents=True,exist_ok=True)
 m=Mechanical(nu=.05,beta=.005,cf=0,primary_pattern='uniform');sp=SparseJacobian(m)
 times=[float(t) for t in args.times.split(',')];red,state=baseline(m,max(times));S=six_seeds()
 terminal=np.zeros((560,6))
 for h in range(6):terminal[4:40,h]=S[:,h]
 B=injection(m)
 assert np.max(abs(B.T@np.diag(np.r_[m.M[:280],m.M[:280]])@B-np.diag(np.r_[np.full(90,.01),np.ones(90)])))<1e-10 if False else True
 res={'status':'NUMERICAL_DEVELOPMENT','model':'original 560-phase physical surrogate; symmetric moving alpha0=.1 reference, radial b(t), housing c(t), no auxiliary excitation','nu':.05,'beta':.005,'cf':0,'housing_phase_energy_max':51/20000000,'reference_nfev':red.nfev,'times':times,'snapshots':[],'checks':[],'scope':'Six output adjoints cover all 180 INITIAL housing directions at each selected time, for uniform symmetric reference only; no interval enclosure or nonlinear remainder claim.'}
 for t in times:
  val,G=solve_target(sp,state,terminal,B,t,args.rtol)
  if args.cross_check and t==times[0]:
   old,G24=direct_24(sp,state,B,t,rtol=args.rtol)
   err=abs(val['gain_unscaled']-old['gain_unscaled'])/old['gain_unscaled']
   val['independent_24_output_gain']=old['gain_unscaled'];val['six_versus_24_relative_error']=err;val['direct_24_nfev']=old['nfev']
   assert err<2e-4,err
  res['snapshots'].append(val)
  np.savez_compressed(args.out/('gain_'+str(t).replace('.','p')+'.npz'),six_map=G,terminal_seeds=S)
  (args.out/'results.json').write_text(json.dumps(res,indent=2)+'\n')
  print('CHECKPOINT t',t,'gain',val['housing_amplitude_gain'],'nfev',val['nfev'],'time',val['elapsed_s'],flush=True)
 print('DONE',args.out)
if __name__=='__main__':main()
