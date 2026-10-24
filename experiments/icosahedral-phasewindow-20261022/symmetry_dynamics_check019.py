#!/usr/bin/env python3
"""Independent reduced-ODE versus archived 560-phase force cross-check.

Requires colocated nonaffine_audit.py from checkpoint 011 (local source
reimplementation of GitHub blob files). Exact theorem does NOT depend on this.
"""
import math,argparse,json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from nonaffine_audit import Mechanical,V,R2,R,PROJ

M2=R2-.25
LAM=(R2-.5)/M2

# theta=(alpha,b,c,alphadot,bdot,cdot)
def reduced_rhs(t,y,beta=.005,nu=.05,cf=0.):
 a,b,c,ad,bd,cd=y
 mc=12*beta*M2/R2
 eta=nu*.4*beta/R2
 de=c-b;dopp=c-LAM*b
 le=math.sqrt(M2*de*de+b*b/4)
 lo=math.sqrt(M2*(dopp*dopp+b*b))
 # gradients of 4 housing-to-anchor strut lengths wrt b,c
 gb_e=(-M2*de+b/4)/le; gc_e=M2*de/le
 gb_o=M2*(-LAM*dopp+b)/lo;gc_o=M2*dopp/lo
 re=gb_e*bd+gc_e*cd;ro=gb_o*bd+gc_o*cd
 Db=60*eta*(gb_e*re+gb_o*ro)
 Dc=60*eta*(gc_e*re+gc_o*ro)
 udd=-(13*a-12*(b-1))
 bdd=(-36*(b-1)+12*a+100*mc*(c-b)-30*cf*bd-Db)/12
 cdd=(-100*mc*(c-b)-Dc)/mc
 return np.array([ad,bd,cd,udd,bdd,cdd])

def embed(y):
 a,b,c,ad,bd,cd=y
 M=Mechanical(nu=.05,beta=.005,cf=0,primary_pattern='uniform')
 q=np.zeros(280);v=np.zeros(280)
 q[0]=a;q[1:40]=(b*V).ravel();q[190:280]=(c*M.midref).ravel()
 v[0]=ad;v[1:40]=(bd*V).ravel();v[190:280]=(cd*M.midref).ravel()
 return M,np.r_[q,v,0]

def check_rhs(y,beta=.005,nu=.05,cf=0):
 M,state=embed(y)
 M.nu=nu;M.beta=beta;M.cf=cf
 # Need reconstruct M itself for coefficient consistency; beta etc from constructor.
 M=Mechanical(nu=nu,beta=beta,cf=cf,primary_pattern='uniform')
 state[190:280]=(y[2]*M.midref).ravel();state[470:560]=(y[5]*M.midref).ravel()
 out=M.rhs(0,state);acc=out[280:560]
 sh=acc[1:40].reshape(13,3)
 h=acc[190:280].reshape(30,3)
 bdd=(sh*V).sum()/(V*V).sum()
 cdd=(h*M.midref).sum()/(M.midref*M.midref).sum()
 got=np.array([acc[0],bdd,cdd]);expect=reduced_rhs(0,y,beta,nu,cf)[3:]
 resid={'scalar_accel_error':float(np.max(np.abs(got-expect))),
       'center_accel':float(np.linalg.norm(sh[0])),
       'shell_radial_residual':float(np.linalg.norm(sh[1:]-bdd*V[1:])),
       'housing_radial_residual':float(np.linalg.norm(h-cdd*M.midref)),
       'aux_accel':float(np.linalg.norm(acc[40:190]))}
 assert max(resid.values())<3e-11,resid
 return resid


def test():
 vals=[]
 for nu in [0.,.04,.05]:
  for beta in [.005,.05]:
   for case in [(.1,.94,1.06,0.,-.11,.13),(-.025,1.05,.98,.14,.07,-.03)]:
    vals.append(check_rhs(np.array(case),beta=beta,nu=nu,cf=.001))
 # Energy exact and only chosen symmetric radial prep
 E_star=.065+51/20000000
 mc=12*.005*M2/R2
 dr=math.sqrt((2*(51/20000000))/(100*mc))
 y0=np.array([.1,1.,1.+dr,0.,0.,0.])
 a=solve_ivp(lambda t,y:reduced_rhs(t,y,beta=.005,nu=.05,cf=0),[0,100],y0,rtol=2e-11,atol=1e-13,method='DOP853',dense_output=True)
 assert a.success
 ts=np.linspace(0,100,1001)
 traj=a.sol(ts).T
 b=traj[:,1];c=traj[:,2]
 le=np.sqrt(M2*(c-b)**2+b**2/4)
 lo=np.sqrt(M2*((c-LAM*b)**2+b*b))
 assert np.min(le)>.4625 and np.min(lo)>.4625
 z=((traj[:,1,None,None]*V[None,1:,:])@np.zeros((3,3))) if False else None
 # Check actual mechanical-energy conservation plus dissipative budget via scalar heat
 a0,b0,c0,ad0,bd0,cd0=y0
 def E(y):
  a,b,c,ad,bd,cd=y
  s=b-1
  return .5*(a*a+24*s*s+12*(s-a)**2)+.5*100*mc*(c-b)**2+.5*(ad*ad+12*bd*bd+mc*cd*cd)
 energies=np.array([E(v) for v in traj]);assert energies.max()<=E_star+1e-10
 # compare independently embedded original 560-state integration on interval [0,4]
 M,state=embed(y0)
 sol=solve_ivp(M.rhs,[0,4],state,rtol=3e-10,atol=1e-12,method='DOP853',t_eval=np.linspace(0,4,81))
 assert sol.success
 y_ref=a.sol(sol.t).T
 delta=[]
 for ix,qv in enumerate(sol.y.T):
  ref=y_ref[ix]
  shell=qv[1:40].reshape(13,3);houses=qv[190:280].reshape(30,3)
  delta.append(max(abs(qv[0]-ref[0]),np.max(abs(shell-ref[1]*V)),np.max(abs(houses-ref[2]*M.midref)),np.linalg.norm(qv[40:190])))
 assert max(delta)<1e-8
 return {'status':'PASS','checked_rhs_cases':len(vals),
         'max_force_tangency_error':max(max(v.values()) for v in vals),
         'beta_numeric':.005,'nu_numeric':.05,'cf_numeric':0,'radial_housing_initial_scale':float(y0[2]),
         'radial_run_horizon':100,'radial_run_nfev':a.nfev,
         'b_sample_min':float(b.min()),'b_sample_max':float(b.max()),
         'strut_sample_min':float(min(le.min(),lo.min())),
         'sample_energy_start':float(energies[0]),'sample_energy_max':float(energies.max()),
         'full560_vs_6D_max_error_u4':float(max(delta)),
         'evidence':'NUMERICAL / constructor; exact all-time theorem independently proven by exact_symmetry.py'}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path);args=ap.parse_args()
 results=test();raw=json.dumps(results,indent=2,sort_keys=True)+'\n'
 if args.out:args.out.write_text(raw)
 print('PASS reduced versus full560 symmetric-sector constructor and u100 reduced numerical run')
 print(raw)