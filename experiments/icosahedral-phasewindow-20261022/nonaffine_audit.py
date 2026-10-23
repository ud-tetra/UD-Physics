#!/usr/bin/env python3
"""UD Discovery: full 560-state icosahedral passive surrogate and Z readout.
Independent reimplementation of source code inspected at GitHub blob IDs in README.
Constructor check, NOT independently replicated physical evidence.
"""
import argparse, json, time, math, hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh, svd
PHI=(1+math.sqrt(5))/2
R2=(5+math.sqrt(5))/8
R=math.sqrt(R2)
# 12 vertices, edge1, icosahedron orientation conventional
X=[]
for a in [-1,1]:
 for b in [-1,1]:X.append((0.,a/2,b*PHI/2))
for a in [-1,1]:
 for b in [-1,1]:X.append((a/2,b*PHI/2,0.))
for a in [-1,1]:
 for b in [-1,1]:X.append((a*PHI/2,0.,b/2))
X=np.array(X)
D=X[:,None,:]-X[None,:,:]
EDGES=np.array([(i+1,j+1) for i in range(12) for j in range(i+1,12) if abs(np.linalg.norm(D[i,j])-1)<1e-12],dtype=int)
assert X.shape==(12,3) and EDGES.shape==(30,2) and np.max(np.abs(np.sum(X*X,axis=1)-R2))<1e-14
faces=[(i,j,k) for i in range(1,13) for j in range(i+1,13) for k in range(j+1,13) if all(((min(a,b),max(a,b)) in set(map(tuple,EDGES))) for a,b in [(i,j),(i,k),(j,k)])]
assert len(faces)==20
edge_pairs=[]
for i in range(30):
 for j in range(i+1,30):
  if set(EDGES[i])&set(EDGES[j]):edge_pairs.append((i+12,j+12))
assert len(edge_pairs)==120
pairs=np.array([(i-1,j-1) for i,j in EDGES.tolist()]+edge_pairs)
# proper indexing housings h=0..29, anchor indices 0..12
anchors=np.array([(h,int(k)) for h,(i,j) in enumerate(EDGES) for k in [i,j]+sorted([next(k for k in f if k not in (i,j)) for f in faces if i in f and j in f])]);assert anchors.shape==(120,2)
HIDX=anchors[:,0]; AIDX=anchors[:,1]
I=EDGES[:,0];J=EDGES[:,1]
V=np.vstack([np.zeros((1,3)),X]); assert abs(np.linalg.norm(V[I[0]]-V[J[0]])-1)<1e-12
P0=np.ones((12,12))/12; PV=X@X.T/(4*R2)
PROJ=np.eye(12)-P0-PV
assert np.linalg.norm(PROJ@X)<1e-13 and np.linalg.norm(PROJ@PROJ-PROJ)<1e-13

def exact_static_witness():
 # displacement exactly 1/25 along unit coordinate; PV_ii=1/4, P0_ii=1/12.
 delta=F(1,25); projected2=delta*delta*F(2,3)
 assert projected2>F(1,1600)
 # At most one spoke extension (triangle inequality) and five incident edges:
 # 1/R2<10/9, maximum g=21/20, k=21/50 (and alpha=0)
 energy_up=F(1,2)*((1+F(21,20))*F(10,9)+5*F(21,50))*delta*delta
 assert energy_up<F(1,200) and energy_up<F(1360051,20000000)
 Y=X.copy();Y[0,0]+=float(delta)
 z=np.linalg.norm(PROJ@Y)
 assert abs(z**2-float(projected2))<1e-14
 return {'displacement':str(delta),'nonaffine_norm_squared_exact':str(projected2),
         'nonaffine_norm_numeric':z,'nonaffine_threshold':1/40,
         'conservative_energy_upper_rational':str(energy_up),
         'source_count_affected_spokes':1,'source_count_affected_edges':5,
         'interpretation':'Exact low-energy full 3D state outside proposed Z ball; not a dynamically reachable state from designated pulse.'}

class Mechanical:
 def __init__(self,nu=.05,beta=.005,cf=0,primary_pattern='uniform',housing_phase='none',phase_energy_multiplier=1,seed=10422):
  self.nu=nu;self.beta=beta;self.cf=cf;self.rng=np.random.default_rng(seed)
  self.m=np.ones(13);self.g=np.ones(12);self.k=np.full(30,.4)
  self.hw=np.ones(30);self.gain=np.ones(150)
  if primary_pattern=='adverse':
   # deterministic qualified ±5% patterns, ±1% reciprocal gains, ±10% housing weights; exposed test design not prior frozen property set
   self.m=1+.05*self.rng.choice([-1.,1.],13)
   self.g=1+.05*self.rng.choice([-1.,1.],12)
   self.k=.4*(1+.05*self.rng.choice([-1.,1.],30))
   self.gain=1+.01*self.rng.choice([-1.,1.],150)
   raw=self.rng.choice([-1.,1.],30).astype(float);raw-=raw.mean();raw/=max(abs(raw));self.hw=1+.1*raw
  self.M=np.r_[1.,np.repeat(self.m/R2,3),np.full(150,.1*2),np.repeat(.4*beta*self.hw/R2,3)]
  self.mh=.4*beta*self.hw/R2;self.kh=self.mh*100
  self.eta=nu*.4*beta/R2
  self.n=280;self.beta=beta
  self.cs=cf/2;self.ce=4*cf/5
  self.G=np.zeros((150,42));ind=np.arange(150);self.G[ind,pairs[:,0]]=1;self.G[ind,pairs[:,1]]=-self.gain
  self.U=np.zeros((561,))
  self.midref=(V[I]+V[J])/2
  self.pattern=primary_pattern
 def initial(self,alpha=.1,energy_multiplier=1,phase='none',seed=10422):
  q=np.zeros(280);q[0]=alpha;q[1:40]=V.ravel();q[190:280]=self.midref.ravel()
  v=np.zeros(280)
  # distribute housing perturbation exclusively in housing phase energy metric
  Ep=(1+sum(self.g))*.01/2;Eh=Ep/40000*1.5*energy_multiplier
  if phase!='none':
   rng=np.random.default_rng(seed);a=self.initial_gain_phase(Eh) if phase=='initial-gain' else rng.normal(size=180)
   if phase=='position':a[90:]=0
   if phase=='velocity':a[:90]=0
   a/=np.linalg.norm(a)
   q[190:280]+=np.sqrt(2*Eh)*a[:90]/(10*np.sqrt(np.repeat(self.mh,3)))
   v[190:280]+=np.sqrt(2*Eh)*a[90:]/np.sqrt(np.repeat(self.mh,3))
  self.phase_energy_budget=Eh
  return np.r_[q,v,0.],Eh if phase!='none' else 0.
 def initial_gain_phase(self,Eh):
  """Frozen first-derivative maximum of initial nonaffine acceleration.
  Uses 180 analytic, energy-normalized housing displacement/velocity columns.
  This is local-time NUMERICAL/FIT; not an all-phase u100 bound.
  """
  mat=np.zeros((36,180));scale=math.sqrt(2*Eh)
  for h,(i,j) in enumerate(EDGES):
   for k in range(3):
    displacement=np.zeros((13,3));displacement[i,k]+=self.kh[h]/2/(self.m[i]/R2)
    displacement[j,k]+=self.kh[h]/2/(self.m[j]/R2)
    mat[:,3*h+k]=(PROJ@displacement[1:]).ravel()*scale/(10*math.sqrt(self.mh[h]))
  n=(self.midref[HIDX]-V[AIDX]);n=n/np.linalg.norm(n,axis=1)[:,None]
  for row,(h,a) in enumerate(anchors):
   nn=np.outer(n[row],n[row]);
   for k in range(3):
    if a>0:
     displ=np.zeros((13,3));displ[a,:]=self.eta*nn[:,k]/(self.m[a]/R2)
     mat[:,90+3*h+k]+=(PROJ@displ[1:]).ravel()*scale/math.sqrt(self.mh[h])
  u,s,v=svd(mat,full_matrices=False)
  self.gain_singular_value=float(s[0]);self.linear_initial_gain_matrix=mat
  return v[0]
 def geometry(self,q):
  alpha=q[0];xp=q[1:40].reshape((13,3));z=q[40:190];H=q[190:280].reshape((30,3))
  r=xp[1:]-xp[0];rho=np.linalg.norm(r,axis=1);rn=r/rho[:,None]
  s=rho/R-1
  d=xp[I]-xp[J];ell=np.linalg.norm(d,axis=1);en=d/ell[:,None];e=ell-1
  y=np.r_[s,e];err=self.G@y-z
  mid=(xp[I]+xp[J])/2;mount=H-mid
  strut=H[HIDX]-xp[AIDX];ls=np.linalg.norm(strut,axis=1);sn=strut/ls[:,None]
  return alpha,xp,z,H,rho,rn,s,d,ell,en,e,err,mid,mount,sn,ls
 def forces(self,q,v,energy=False):
  alpha,xp,z,H,rho,rn,s,d,ell,en,e,err,mid,mount,sn,ls=self.geometry(q)
  grad=np.zeros((13,3));tensions=self.G.T@(.1*50*err)
  gf=((s+self.g*(s-alpha)+tensions[:12])/R)[:,None]*rn
  grad[1:]+=gf;grad[0]-=gf.sum(axis=0)
  ef=(self.k*e+tensions[12:])[:,None]*en
  np.add.at(grad,I,ef);np.add.at(grad,J,-ef)
  gh=self.kh[:,None]*mount
  np.add.at(grad,I,-gh/2);np.add.at(grad,J,-gh/2)
  # axial spoke, edge damping with reciprocal forces
  pv=v[1:40].reshape(13,3);hv=v[190:280].reshape(30,3)
  sd=np.einsum('ij,ij->i',rn,pv[1:]-pv[0])/R
  ed=np.einsum('ij,ij->i',en,pv[I]-pv[J]);
  fd=(self.cs*sd/R)[:,None]*rn
  grad[1:]+=fd;grad[0]-=fd.sum(axis=0)
  fe=(self.ce*ed)[:,None]*en
  np.add.at(grad,I,fe);np.add.at(grad,J,-fe)
  rates=np.einsum('ij,ij->i',sn,hv[HIDX]-pv[AIDX]);damp=(self.eta*rates)[:,None]*sn
  np.add.at(grad,AIDX,-damp);np.add.at(gh,HIDX,damp)
  g_alpha=alpha+np.sum(self.g*(alpha-s))
  grad_q=np.r_[g_alpha,grad.ravel(),-50*.1*err,gh.ravel()]
  # relative port auxiliary restoring: z''=(kappa err-gamma zdot)/mu
  grad_q[40:190]=-50*.1*err
  caux=np.zeros_like(v);caux[40:190]=.1*5*v[40:190]
  full_grad=grad_q+caux
  powers=(.1*5*np.dot(v[40:190],v[40:190])+self.cs*np.dot(sd,sd)+self.ce*np.dot(ed,ed)+self.eta*np.dot(rates,rates))
  if energy:
   elastic=.5*(alpha*alpha+np.sum(s*s)+np.dot(self.g,(s-alpha)**2)+np.dot(self.k,e**2))+.5*.1*50*np.dot(err,err)+.5*np.dot(self.kh,np.sum(mount*mount,axis=1))
   ke=.5*np.dot(self.M,v*v)
   return full_grad,powers,elastic+ke,ls,rho,ell
  return full_grad,powers
 def rhs(self,t,state):
  n=280;q=state[:n];v=state[n:2*n]
  g,p=self.forces(q,v)
  return np.r_[v,-g/self.M,p]
 def read(self,ts,Y):
  vals=[]
  for state in Y:
   q=state[:280];v=state[280:560];grad,p,E,ls,rho,ell=self.forces(q,v,True)
   shell=q[1:40].reshape(13,3)[1:];Z=PROJ@(shell-shell.mean(axis=0))
   vals.append([float(np.linalg.norm(Z)),float(E),float(ls.min()),float(rho.min()),float(ell.min()),float(state[-1]),float(np.linalg.norm(grad))])
  return np.array(vals)
 def simulate(self,case,until=100,n_samples=501,rtol=2e-8,atol=2e-10):
  y0,Eh=self.initial(phase=case)
  v0=self.read([0],[y0])[0]
  if case=='initial-gain':
   ybase,_=self.initial(phase='none'); abase=self.rhs(0,ybase)[281:320].reshape(13,3)[1:]
   acase=self.rhs(0,y0)[281:320].reshape(13,3)[1:]
   self.gain_initial_acc_norm=float(np.linalg.norm(PROJ@(acase-abase)))
  sol=solve_ivp(self.rhs,(0,until),y0,method='DOP853',rtol=rtol,atol=atol,t_eval=np.linspace(0,until,n_samples))
  assert sol.success,sol.message
  t=sol.t;Y=sol.y.T;Rout=self.read(t,Y)
  e0=Rout[0,1]
  balance=np.max(np.abs(Rout[:,1]+Rout[:,5]-e0))/e0
  imax=int(np.argmax(Rout[:,0]));idx=int(np.argmin(Rout[:,2]))
  return {'case':case,'nu':self.nu,'beta':self.beta,'cf':self.cf,'property_pattern':self.pattern,'duration_u':float(until),'initial_phase_energy':Eh,'declared_phase_energy_ceiling':self.phase_energy_budget,
          'max_nonaffine_fro':Rout[imax,0],'at_u':float(t[imax]),'exceeds_1_over_40':bool(Rout[imax,0]>1/40),
          'max_ratio_to_threshold':float(Rout[imax,0]*40), 'initial_gain_singular_value':getattr(self,'gain_singular_value',None),'initial_gain_direct_acceleration_difference':getattr(self,'gain_initial_acc_norm',None), 'minimum_strut_sampled':float(Rout[idx,2]),'min_primary_radial':float(Rout[:,3].min()),
          'min_edge_length':float(Rout[:,4].min()),'energy_heat_balance_relative_error':float(balance),
          'initial_energy':float(e0),'final_energy':float(Rout[-1,1]),'sample_count':len(t),
          'solver_rtol':rtol,'solver_atol':atol,'nfev':sol.nfev,'elapsed_s':0,'trace':list(zip(map(float,t),map(float,Rout[:,0]),map(float,Rout[:,2])))}

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--until',type=float,default=50.);p.add_argument('--samples',type=int,default=501);p.add_argument('--cases',default='uniform-none,uniform-random,adverse-random');p.add_argument('--rtol',type=float,default=2e-8);p.add_argument('--atol',type=float,default=2e-10);a=p.parse_args()
 a.out.mkdir(parents=True,exist_ok=True)
 exact=exact_static_witness();(a.out/'exact_static_witness.json').write_text(json.dumps(exact,indent=2)+'\n')
 results=[]
 for key in a.cases.split(','):
  pattern,phase=key.split('-',1);m=Mechanical(nu=.05,beta=.005 if pattern=='adverse' else .05,cf=0,primary_pattern=pattern)
  start=time.perf_counter();r=m.simulate(phase,a.until,a.samples,a.rtol,a.atol);r['elapsed_s']=round(time.perf_counter()-start,2)
  samples=r.pop('trace')
  import csv
  with (a.out/(key+'_trace.csv')).open('w',newline='') as f:
   w=csv.writer(f);w.writerow(['u','Z_frobenius','minimum_strut']);w.writerows(samples)
  results.append(r);print(key,'Z=',r['max_nonaffine_fro'],'time=',r['at_u'],'balance=',r['energy_heat_balance_relative_error'],'nfev=',r['nfev'],flush=True)
 assert all(v['energy_heat_balance_relative_error']<3e-6 for v in results)
 summary={'status':'NUMERICAL_CONSTRUCTOR_ONLY','model':'Standalone reimplementation of imported MountLoss force law: 280 config / 560 phase plus heat; all 120 current-axis viscous pairs',
          'source_revision':'a4ae75dd55cd2b691c811c4d6eeae1367fcba015','static_witness':exact,'simulations':results,
          'scope':'finite initial housing phase realizations, plus optimization of first-order initial acceleration over 180 phase directions; neither certifies all-phase u100 or continuous property box; original u100 certificate remains OPEN'}
 (a.out/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('DONE',a.out)
if __name__=='__main__':main()