#!/usr/bin/env python3
"""Numerical potential barrier exploration for a flat icosahedral centre-face cell.

This is a development search, NOT a rigorous global minimization. Original
MountLoss constitutive energy minimized analytically over alpha and device/housing
storage at reference. Main branch 467e2208... unchanged mechanics source.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

PHI=(1+np.sqrt(5))/2
VERT=np.array(sorted({tuple(np.asarray(v)/2) for a in [-1,1] for b in [-1,1]
                      for v in [(0,a,b*PHI),(a,b*PHI,0),(b*PHI,0,a)]}))
RAD=np.linalg.norm(VERT[0]);assert np.allclose(np.linalg.norm(VERT,axis=1),RAD)
EDGES=np.array([(i,j) for i,j in combinations(range(12),2)
                if abs(np.linalg.norm(VERT[i]-VERT[j])-1)<1e-10],dtype=int)
EDGESET=set(map(tuple,EDGES))
FACES=[(i,j,k) for i,j,k in combinations(range(12),3)
       if (i,j) in EDGESET and (j,k) in EDGESET and (i,k) in EDGESET]
assert len(VERT)==12 and len(EDGES)==30 and len(FACES)==20
FACE=FACES[0]
G=.95
K=.38
N=12

def fungrad(y):
    x=y.reshape(N,3)
    rho=np.linalg.norm(x,axis=1)
    d=x[EDGES[:,0]]-x[EDGES[:,1]]
    ell=np.linalg.norm(d,axis=1)
    if min(rho.min(),ell.min())<1e-9:
        return (1e10, np.zeros_like(y))
    s=rho/RAD-1
    e=ell-1
    alpha=G*s.sum()/(1+N*G)  # exact minimization of scalar heart variable
    E=.5*(alpha**2+s@s+G*((s-alpha)@(s-alpha))+K*(e@e))
    deriv=((1+G)*s-G*alpha)[:,None]*x/(rho[:,None]*RAD)
    edge=(K*e/ell)[:,None]*d
    np.add.at(deriv,EDGES[:,0],edge)
    np.add.at(deriv,EDGES[:,1],-edge)
    return float(E),deriv.reshape(-1)

def det_grad(y):
    x=y.reshape(N,3)
    i,j,k=FACE
    a,b,c=x[[i,j,k]]
    d=float(np.linalg.det(np.array([a,b,c])))
    grad=np.zeros_like(x)
    grad[i]=np.cross(b,c)
    grad[j]=np.cross(c,a)
    grad[k]=np.cross(a,b)
    return d, grad.ravel()

def flat_seed(base,i):
    x=base.copy()
    k=FACE[i%3]
    j=[a for a in FACE if a!=k]
    u=x[j].T
    x[k]=u@np.linalg.lstsq(u,x[k],rcond=None)[0]
    return x

def optimize_lagrange(seed):
    result=minimize(fungrad,seed.ravel(),jac=True,method='SLSQP',
      constraints=[{'type':'eq','fun':lambda y:det_grad(y)[0],
                    'jac':lambda y:det_grad(y)[1]}],
      options={'maxiter':550,'ftol':2e-13})
    en,grad=fungrad(result.x)
    det,jac=det_grad(result.x)
    scale=np.dot(grad,jac)/np.dot(jac,jac)
    kkt=float(np.linalg.norm(grad-scale*jac))
    return dict(energy=en,det=det,kkt=kkt,success=bool(result.success),
                iterations=int(result.nit),x=result.x.reshape(12,3))

def optimize_parameterized(x):
    # An independent no-constraint parameterization: make third face vertex
    # p*a+q*b. All other 11 vertices remain freely variable.
    i,j,k=FACE
    idx=[h for h in range(12) if h!=k]
    u=x[idx].ravel()
    ab=x[[i,j]].T
    pq=np.linalg.lstsq(ab,x[k],rcond=None)[0]
    init=np.r_[u,pq]
    def recover(t):
        y=np.zeros((12,3))
        y[idx]=t[:33].reshape(11,3)
        y[k]=t[-2]*y[i]+t[-1]*y[j]
        return y
    def obj(t):
        y=recover(t)
        en,der=fungrad(y.ravel())
        dz=der.reshape(12,3)
        g=dz[idx].copy()
        g[idx.index(i)]+=t[-2]*dz[k]
        g[idx.index(j)]+=t[-1]*dz[k]
        gp=np.array([dz[k]@y[i],dz[k]@y[j]])
        return en,np.r_[g.ravel(),gp]
    ans=minimize(obj,init,method='L-BFGS-B',jac=True,options={'ftol':1e-14,'gtol':1e-9,'maxiter':2000,'maxls':60})
    X=recover(ans.x)
    E,gr=fungrad(X.ravel());c,J=det_grad(X.ravel())
    lam=(gr@J)/(J@J)
    return dict(energy=E,det=c,kkt=float(np.linalg.norm(gr-lam*J)),success=bool(ans.success),
                iterations=int(ans.nit),x=X)

def run(nrandom):
    rng=np.random.default_rng(20261022)
    seeds=[flat_seed(VERT,k) for k in range(3)]
    for a in [0.3,0.7,1.4]:
        for j in range(3):
            x=VERT.copy()+rng.normal(0,a*.1,(12,3))
            seeds.append(flat_seed(x,j))
    for z in range(nrandom):
        scale=[.1,.25,.45][z%3]
        x=VERT.copy()+rng.normal(0,scale,(12,3))
        seeds.append(flat_seed(x,z))
    scans=[]
    for idx,x in enumerate(seeds):
        out=optimize_lagrange(x)
        if not out['success'] or abs(out['det'])>1e-7 or out['kkt']>2e-4:
            print('BAD',idx,out['success'],out['energy'],out['det'],out['kkt'])
        scans.append({k:v for k,v in out.items() if k!='x'})
        scans[-1]['id']=idx
        scans[-1]['x']=out['x']
    valid=[r for r in scans if abs(r['det'])<1e-7 and r['kkt']<2e-4]
    worst=min(valid,key=lambda x:x['energy'])
    independently=optimize_parameterized(worst['x'])
    x=worst['x'];rho=np.linalg.norm(x,axis=1);rad=rho/RAD-1
    L=np.linalg.norm(x[EDGES[:,0]]-x[EDGES[:,1]],axis=1)
    alpha=G*rad.sum()/(1+N*G)
    # All housing locations can sit at shell-edge midpoints with zero mount energy.
    # Device extensions can be set equal to their corresponding port differences,
    # giving zero extra auxiliary storage. Need four-anchor directions nonzero.
    mid=(x[EDGES[:,0]]+x[EDGES[:,1]])/2
    min_strut=np.inf
    for h,(i,j) in enumerate(EDGES):
        adjacent=[f for f in FACES if i in f and j in f]
        assert len(adjacent)==2
        anchors=[i,j]+[next(t for t in f if t not in (i,j)) for f in adjacent]
        min_strut=min(min_strut,*[np.linalg.norm(mid[h]-x[k]) for k in anchors])
    pulse=(1+12*1.05)*(.1**2)/2 + 51/20_000_000
    report={
     'status':'NUMERICAL_DEVELOPMENT_NOT_GLOBAL_PROOF',
     'reference_source_commit':'467e2208fba9da086535bd5b8a6a07f6d6f8e08b',
     'question':'How much assumed conservative primary energy is needed to flatten one centre-face cell, allowing all 12 shell vertices and scalar alpha to relax?',
     'model':'Original icosahedral length energy, g_i=0.95, k_e=0.38 throughout; optimize alpha analytically; device and housing stored energy minimized at zero; centre fixed by translation invariance.',
     'source_exposure':'Original amplitude 0.1, total energy threshold, icosahedral model and failure witness exposed; numeric search post-hoc, not held-out.',
     'search':{'starts':len(scans),'random_starts':nrandom,'rng_seed':20261022,'objective':'minimize exact physical length-strain potential given one flat oriented cell determinant=0','algorithm':'SLSQP with analytic objective/Jacobian and equality derivative','independent_method':'L-BFGS-B with face vector coplanarity enforced by reparametrization'},
     'reference_geometry':{'vertices':12,'edges':30,'faces':20,'cell_face':list(FACE),'circumradius':RAD},
     'best_numerical_slsqp':{'energy':worst['energy'],'constraint_abs_residual':abs(worst['det']),'stationarity_tangent_residual':worst['kkt'],'id':worst['id'],'optimized_alpha':alpha,'minimum_strut_length':min_strut,'max_abs_spoke_strain':float(np.max(abs(rad))),'max_abs_edge_strain':float(np.max(abs(L-1)))},
     'independent_parameterized_solution':{k:v for k,v in independently.items() if k!='x'},
     'energy_baseline':{'original_alpha_pulse_upper_total_initial_energy':pulse,'candidate_over_baseline':worst['energy']/pulse},
     'all_runs':[{k:v for k,v in r.items() if k!='x'} for r in scans],
     'limitations':['Only local numerical minimizers; no global minimization, interval proof, or certificate excluding lower-energy collapse configurations.','Does not prove all-time cell orientation for the actual pulse.','A conservative energy sublevel already contains some housing-strut singularities, so full-system safety cannot follow solely from energy even if cell orientation were proved.','Uniform minimal g,k selected as lower bound; 120 strut dynamics, original physical time/calibration and empirical responses not derived.'],
     'next_discriminant':'Derive and validate a certified lower bound on global icosahedral length-strain energy at any zero oriented cell determinant; compare with 0.06800255. Or obtain PR44 forced-Green recovery for nonlinear u100 certificate.'
    }
    return report, worst['x']

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--starts',type=int,default=60)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    data,config=run(args.starts)
    (args.out/'barrier_results.json').write_text(json.dumps(data,indent=2)+'\n')
    np.savetxt(args.out/'candidate_flat_vertices.csv',config,delimiter=',',header='x,y,z',comments='')
    print(json.dumps({'status':data['status'],'best':data['best_numerical_slsqp'],'independent':data['independent_parameterized_solution'],'threshold':data['energy_baseline']},indent=2))
