#!/usr/bin/env python3
"""All-time continuous dense numerical screen using A5 reduced forward fundamental matrices.
No rigorous interval error enclosure: coefficient cubic interpolation and DOP853.
"""
import sys,time,json,argparse
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
sys.path.insert(0,str(Path(__file__).resolve().parent))
from interpolated_reduced import setup

Eh=51/20000000
EPS=np.sqrt(2*Eh)

def make_fundamental(x,B,obj,T,rtol):
 Q=x['basis'];r=Q.shape[1];m=2*r
 # project full 560 phase injection to multiplicity slice
 F=np.vstack([Q.T@B[:280],Q.T@B[280:]])
 Aq,Ac=obj;start=time.perf_counter()
 def rhs(t,y):
  W=y.reshape(m,m)
  return np.vstack([W[r:],-Aq(t).T@W[:r]-Ac(t).T@W[r:]]).ravel()
 # A_q from adjoint = Q.T K^T M^-1 Q, but forward Q.T M^-1 K Q = A_q.T
 # Here mass commutes projector; valid.
 sol=solve_ivp(rhs,(0,T),np.eye(m).ravel(),method='DOP853',dense_output=True,rtol=rtol,atol=rtol*.01)
 assert sol.success,sol.message
 outrows=np.zeros((len(x['seed_indices']),m))
 for i,sidx in enumerate(x['seed_indices']):
  out=np.zeros(280);out[4:40]=seeds[:,sidx]
  outrows[i,:r]=out@Q
 return dict(sol=sol,F=F,O=outrows,Q=Q,elapsed=time.perf_counter()-start,sector=x['key'],rank=r,nfev=sol.nfev)

def response(one,t,obj=None):
 m=2*one['rank'];r=one['rank'];A=one['sol'].sol(t).reshape(m,m)@one['F'];O=one['O'];Op=O@A
 # derivative of output = velocity projection. output acceleration = -(K q + C v)/M
 Ovel=O.copy();Ovel[:,:r]=0;Ovel[:,r:]=O[:,:r]
 Ov=Ovel@A
 if obj is None:return Op,Ov
 r=one["rank"];As,Ds=obj
 outacc=one["O"][:,:r]@(-As(t).T@A[:r]-Ds(t).T@A[r:])
 return Op,Ov,outacc

def run(T=100,h=.1,rtol=1e-9,sample=0.2,out=None):
 global seeds
 start=time.perf_counter();m,sp,bs,seeds,ref,B,ts,objs=setup(T,h)
 sols={};info=[]
 for x in bs:
  one=make_fundamental(x,B,objs[x['key']],T,rtol)
  info.append({key:one[key] for key in ['sector','rank','nfev','elapsed']})
  print('FUNDAMENTAL',info[-1],flush=True)
  sols[x['key']]=one
 times=np.unique(np.r_[np.arange(0,T+sample*.4,sample),np.array([0,1,2,4,6,10,20,40,70,80,90,100])[np.array([0,1,2,4,6,10,20,40,70,80,90,100])<=T]])
 rows=[];max_g=(-1,0);max_v=(-1,0);max_w=(-1,0)
 for t in times:
  gp=[];vp=[];wp=[]
  for x in bs:
   P,V,W=response(sols[x['key']],float(t),objs[x['key']]);gp+=list(np.repeat(np.linalg.eigvalsh(P@P.T),x['d']));vp+=list(np.repeat(np.linalg.eigvalsh(V@V.T),x['d']));wp+=list(np.repeat(np.linalg.eigvalsh(W@W.T),x['d']))
  g=float(EPS*np.sqrt(max(gp)));v=float(EPS*np.sqrt(max(vp)));w=float(EPS*np.sqrt(max(wp)))
  rows.append([float(t),g,v,w]);max_g=max(max_g,(g,float(t)));max_v=max(max_v,(v,float(t)));max_w=max(max_w,(w,float(t)))
 print('MAX',max_g,max_v,max_w,'seconds',time.perf_counter()-start,flush=True)
 result=dict(status='NUMERICAL_DEVELOPMENT_NOT_INTERVAL',T=T,h=h,rtol=rtol,sample=sample,peak_g=max_g,peak_v=max_v,peak_w=max_w,info=info,elapsed=time.perf_counter()-start,nodes=rows)
 if out:
  out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
  np.savetxt(out.with_suffix('.csv'),np.array(rows),delimiter=',',header='u,position_gain,velocity_gain,acceleration_gain',comments='')
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--T',type=float,default=100);ap.add_argument('--h',type=float,default=.1);ap.add_argument('--rtol',type=float,default=1e-9);ap.add_argument('--sample',type=float,default=.25);ap.add_argument('--out',type=Path,required=True)
 a=ap.parse_args();run(a.T,a.h,a.rtol,a.sample,a.out)
