#!/usr/bin/env python3
"""Sample the frozen MountLoss 560x180 tangent with moving-reference SO(3) readout.

REQUIRES complete UD-Physics checkout, NumPy and SciPy. This is not a
validated ODE/interval enclosure and does not alter the original source law.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import DOP853

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-pulsetube'))
from jacobian import Linearization,model
from variational import SOURCE


def moving_projection(y,W):
    X=y[1:40].reshape(13,3)
    P=W[1:40,:].reshape(13,3,-1)
    h=X[0]-X[1:].mean(axis=0)
    shell=X[1:]-X[1:].mean(axis=0)
    E=P[1:]-P[1:].mean(axis=0)
    Ehub=P[0]-P[1:].mean(axis=0)
    G=shell.T@ shell
    M=np.trace(G)*np.eye(3)-G
    A=np.einsum('ij,ikp->jkp',shell,E)
    S=(A-A.swapaxes(0,1))/2
    cross=2*np.stack([S[2,1],S[0,2],S[1,0]],axis=0)
    omega=np.linalg.solve(M,cross)
    skew=np.zeros((3,3,W.shape[1]))
    skew[0,1]=-omega[2];skew[1,0]=omega[2]
    skew[0,2]=omega[1];skew[2,0]=-omega[1]
    skew[1,2]=-omega[0];skew[2,1]=omega[0]
    shell_shape=E-np.einsum('ij,jkp->ikp',shell,skew)
    hub_shape=Ehub-np.einsum('j,jkp->kp',h,skew)
    return np.concatenate((hub_shape.reshape(3,-1),shell_shape.reshape(36,-1)))


def run(case_name,horizon,step,rtol,atol):
    cases=json.loads((SOURCE/'cases.json').read_text())
    case=next(c for c in cases if c['id']==case_name)
    m=model(case,.05);L=Linearization(m);B=L.injection()
    epsilon=np.sqrt(2*((1+m.g.sum())*.01/2/40000))
    reference=m.initial_augmented(.1)
    z=np.r_[reference,B.ravel()]
    atol_full=np.r_[np.full(561,atol/100),np.full(B.size,atol)]
    def rhs(t,z):
        y=z[:561];W=z[561:].reshape(560,180)
        return np.r_[m.ode(t,y),L.apply(y,W).ravel()]
    solver=DOP853(rhs,0.,z,horizon,rtol=rtol,atol=atol_full)
    times=np.linspace(0,horizon,round(horizon/step)+1)
    initial_primary=reference[1:40].copy()
    records=[]
    def sample(t,z):
        y=z[:561];W=z[561:].reshape(560,180)
        P=W[1:40,:]
        moving=moving_projection(y,W)
        raw=epsilon*np.linalg.svd(P,compute_uv=False)[0]
        shape=epsilon*np.linalg.svd(moving,compute_uv=False)[0]
        reference_shift=np.linalg.norm(y[1:40]-initial_primary)
        records.append({'u':float(t),'reference_displacement':float(reference_shift),
                        'linearized_raw_radius':float(raw),
                        'linearized_moving_shape_radius':float(shape),
                        'moving_framechart_ref_d_condition':bool(reference_shift<=.011)})
    sample(0,z);index=1
    while solver.status=='running':
        solver.step()
        if solver.status=='failed':raise RuntimeError('Original DOP853 solver failed')
        dense=solver.dense_output()
        while index<len(times) and times[index]<=solver.t+1e-11:
            sample(times[index],dense(times[index]));index+=1
    assert index==len(times)
    return {'status':'NUMERICAL_SAMPLED_ONLY','case':case_name,'nu':.05,
            'frozen_initial_housing_epsilon':float(epsilon),
            'sampling_step':step,'rtol':rtol,'atol_tangent':atol,
            'nfev':solver.nfev,'records':records,
            'max_sampled_raw_radius':max(r['linearized_raw_radius'] for r in records),
            'max_sampled_moving_shape_radius':max(r['linearized_moving_shape_radius'] for r in records),
            'max_sampled_reference_shift':max(r['reference_displacement'] for r in records),
            'scope':'No continuous-time enclosure, no forced U(t,s), no nonlinear flow Hessian/remainder, no physical calibration'}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--case',default='seed10422-0-boundary2')
    p.add_argument('--horizon',type=float,default=100)
    p.add_argument('--step',type=float,default=.5)
    p.add_argument('--rtol',type=float,default=5e-10)
    p.add_argument('--atol',type=float,default=5e-12)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();assert a.horizon>0 and a.step>0
    result=run(a.case,a.horizon,a.step,a.rtol,a.atol)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k.startswith('max_sampled') or k in ('status','case','nfev')},sort_keys=True))
