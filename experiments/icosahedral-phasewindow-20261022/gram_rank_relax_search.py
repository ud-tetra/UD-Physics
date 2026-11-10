import numpy as np, json, time
from scipy.optimize import minimize
from pathlib import Path
from itertools import combinations
PHI=(1+np.sqrt(5))/2
VERT=np.array(sorted({tuple(np.asarray(v)/2) for a in [-1,1] for b in [-1,1] for v in [(0,a,b*PHI),(a,b*PHI,0),(b*PHI,0,a)]}))
RAD=np.linalg.norm(VERT[0]); EDGES=np.array([(i,j) for i,j in combinations(range(12),2) if abs(np.linalg.norm(VERT[i]-VERT[j])-1)<1e-10],dtype=int)
FS=[(i,j,k) for i,j,k in combinations(range(12),3) if all(tuple(sorted(e)) in set(map(tuple,EDGES)) for e in [(i,j),(i,k),(j,k)])];FACE=FS[0]
G=.95;K=.38
rng=np.random.default_rng(20261023)

def fungrad(x):
 n,d=x.shape;rho=np.linalg.norm(x,axis=1);diff=x[EDGES[:,0]]-x[EDGES[:,1]];ell=np.linalg.norm(diff,axis=1)
 if min(rho.min(),ell.min())<1e-9: return (1e10,np.zeros_like(x))
 s=rho/RAD-1;e=ell-1;alpha=G*s.sum()/(1+n*G)
 E=.5*(alpha*alpha+s@s+G*((s-alpha)@(s-alpha))+K*(e@e))
 grad=((1+G)*s-G*alpha)[:,None]*x/(rho[:,None]*RAD)
 ed=(K*e/ell)[:,None]*diff
 np.add.at(grad,EDGES[:,0],ed);np.add.at(grad,EDGES[:,1],-ed)
 return E,grad

def build(y,d):
 i,j,k=FACE;others=[v for v in range(12) if v!=k]
 x=np.zeros((12,d));x[others]=y[:11*d].reshape((11,d));p,q=y[-2:];x[k]=p*x[i]+q*x[j]
 return x,others

def fg(y,d):
 x,others=build(y,d);E,gr=fungrad(x); g=gr[others].copy();i,j,k=FACE
 g[others.index(i)]+=y[-2]*gr[k];g[others.index(j)]+=y[-1]*gr[k]
 return E,np.r_[g.ravel(),gr[k]@x[i],gr[k]@x[j]]

def seed(d,scale):
 x=np.zeros((12,d)); x[:,:3]=VERT
 if d>3:x[:,3:]=rng.normal(0,scale,(12,d-3))
 i,j,k=FACE
 pq=np.linalg.lstsq(x[[i,j]].T,x[k],rcond=None)[0]
 return np.r_[x[[v for v in range(12) if v!=k]].ravel(),pq]

if __name__=='__main__':
 report={'face':FACE,'upper_real_3d_min':.12442609483988,'pulse_energy':.06800255,'runs':[]}
 for d in (3,4,5,8,12):
  for scale in ([0.] if d==3 else [0.,.1,.5,1.]):
   start=time.monotonic()
   s=seed(d,scale)
   result=minimize(lambda y:fg(y,d),s,method='L-BFGS-B',jac=True,options={'ftol':1e-13,'gtol':5e-8,'maxiter':1800,'maxls':40})
   x,_=build(result.x,d);E,gr=fungrad(x)
   ev=np.linalg.eigvalsh(x@x.T)
   row={'dimension':d,'scale':scale,'energy':float(E),'success':bool(result.success),'iter':int(result.nit),'gradient':float(np.linalg.norm(result.jac)),'rank':int(np.sum(ev>1e-6)), 'elapsed':round(time.monotonic()-start,2)}
   report['runs'].append(row);print(row,flush=True)
   if E<report.get('best',{}).get('energy',np.inf):report['best']={**row,'X':x.tolist(),'p':float(result.x[-2]),'q':float(result.x[-1])}
 Path('/mnt/data/ud_barrier_continuation/relax_results.json').write_text(json.dumps(report,indent=2))
