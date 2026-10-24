#!/usr/bin/env python3
"""Numerical, symmetry-reduced adjoint with piecewise cubic Jacobian interpolation.
Full Jacobian generated from unchanged source law on exact symmetric baseline.
No interval enclosure; convergence and midpoint defect diagnostics required.
"""
import sys,time,json,argparse
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
sys.path.insert(0,str(Path(__file__).resolve().parent))
from reduced_adjoint import construct
sys.path.insert(0,'/mnt/data/ud_longprop_023')
from six_moving_adjoint import Mechanical,SparseJacobian,baseline,injection


def setup(T,h):
 m=Mechanical(nu=.05,beta=.005,cf=0,primary_pattern='uniform');sp=SparseJacobian(m)
 basis,seeds=construct();baseline_sol,ref=baseline(m,T)
 B=injection(m);ts=np.linspace(0,T,int(round(T/h))+1);invM=1/m.M
 data={x['key']:{'A':[],'D':[]} for x in basis}
 tic=time.perf_counter()
 for i,t in enumerate(ts):
  K,C=sp.matrices(ref(t))
  for x in basis:
   Q=x['basis']
   A=Q.T@(K.T@(invM[:,None]*Q));D=Q.T@(C.T@(invM[:,None]*Q))
   data[x['key']]['A'].append(A);data[x['key']]['D'].append(D)
 print('ASSEMBLY',len(ts),'secs',round(time.perf_counter()-tic,3),flush=True)
 objects={}
 for x in basis:
  key=x['key'];A=np.stack(data[key]['A']);D=np.stack(data[key]['D']);objects[key]=(CubicSpline(ts,A,axis=0),CubicSpline(ts,D,axis=0))
 return (m,sp,basis,seeds,ref,B,ts,objects)

def solve_one(obj,B,ref,x,seeds,T,rtol):
 n=x['basis'].shape[1];ind=x['seed_indices'];col=seeds[:,ind];q=np.zeros((280,len(ind)));q[4:40]=col
 init=np.zeros((2*n,len(ind)));init[:n]=x['basis'].T@q
 csA,csD=obj; counter=[0]
 def rhs(t,arr):
  L=arr.reshape(2*n,len(ind)); counter[0]+=1
  return np.vstack([csA(t)@L[n:],-L[:n]+csD(t)@L[n:]]).ravel()
 s=time.perf_counter();sol=solve_ivp(rhs,(T,0),init.ravel(),method='DOP853',rtol=rtol,atol=rtol*.01)
 assert sol.success,sol.message
 L=sol.y[:,-1].reshape(2*n,len(ind));Q=x['basis'];G=np.vstack([Q@L[:n],Q@L[n:]]).T@B
 print('SOLVED',x['key'],'nfev',sol.nfev,'seconds',round(time.perf_counter()-s,2),flush=True)
 return G,{'sector':x['key'],'nfev':sol.nfev,'seconds':round(time.perf_counter()-s,2),'nvar':2*n*len(ind)}

def calc(T,h,rtol,out):
 started=time.perf_counter();m,sp,bs,seeds,ref,B,ts,objects=setup(T,h)
 error={'grid_h':h,'rtol':rtol,'T':T,'status':'NUMERICAL_NOT_VALIDATED','sectors':[]}
 rng=np.random.default_rng(999)
 # Jacobian interpolation defects at off-grid points, maximum absolute and relative to norm of actual.
 diffA=[];diffD=[]
 for tm in np.arange(0.371*h,T,5.73*h):
  if tm>T:break
  K,C=sp.matrices(ref(tm));invM=1/m.M
  for x in bs:
   Q=x['basis'];A=Q.T@(K.T@(invM[:,None]*Q));D=Q.T@(C.T@(invM[:,None]*Q));intA,intD=objects[x['key']]
   diffA.append(np.max(np.abs(A-intA(tm))));diffD.append(np.max(np.abs(D-intD(tm))))
 error['max_interpolation_entrywise_K']=max(diffA);error['max_interpolation_entrywise_C']=max(diffD)
 print('OFF-GRID DEFECT',error['max_interpolation_entrywise_K'],error['max_interpolation_entrywise_C'],flush=True)
 blocks={};Gfull=np.zeros((6,180));eig=[]
 for x in bs:
  G,info=solve_one(objects[x['key']],B,ref,x,seeds,T,rtol);ind=x['seed_indices'];Gfull[ind]=G
  ev=np.linalg.eigvalsh(G@G.T);blocks[x['key']]=ev.tolist();eig+=list(np.repeat(ev,x['d']));error['sectors'].append(info)
 error['gain_unscaled']=float(np.sqrt(max(eig)));error['housing_gain']=float(np.sqrt(2*51/20000000)*np.sqrt(max(eig)))
 error['blocks']=blocks;error['elapsed_sec']=round(time.perf_counter()-started,3)
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(error,indent=2)+'\n');np.savez_compressed(out.with_suffix('.npz'),six_map=Gfull)
 print('FINAL GAIN',error['housing_gain'],'seconds',error['elapsed_sec'],flush=True)
 return error
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--T',type=float,default=100);ap.add_argument('--h',type=float,default=.2);ap.add_argument('--rtol',type=float,default=1e-9);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 calc(a.T,a.h,a.rtol,a.out)
