#!/usr/bin/env python3
"""Frozen icosahedral nonlinear radial stress: selected phases, NOT all-ball."""
import argparse,sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.spatial.transform import Rotation
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"experiments/icosahedral-pulsetube"))
from jacobian import model
from variational import SOURCE
ARCH=ROOT/"artifacts/icosahedral-pulsetube-20261022-a1/pulsetube-001/files/compact_checkpoints.npz"
CASES={"limiting":("seed10422-0-boundary2","worst_fine"),"nominal":("uniform-b0.05-cf0.0","nominal_normal")}
def aligned(ref,x):
    e=x-ref;c=ref[1:].mean(0);shell=ref[1:]-c;hub=ref[0]-c
    mu=e[1:].mean(0);es=e[1:]-mu;eh=e[0]-mu
    G=shell.T@shell;A=shell.T@es;S=(A-A.T)/2
    omega=np.linalg.solve(np.trace(G)*np.eye(3)-G,2*np.array([S[2,1],S[0,2],S[1,0]]))
    Q=np.array([[0,-omega[2],omega[1]],[omega[2],0,-omega[0]],[-omega[1],omega[0],0]])
    R=Rotation.from_rotvec(-omega).as_matrix()
    nonlinear=np.vstack(((hub+eh)@R-hub,(shell+es)@R-shell))
    linear=np.vstack((eh-hub@Q,es-shell@Q))
    return np.linalg.norm(nonlinear),np.linalg.norm(nonlinear-linear)
def peak(t,x):
    i=int(np.argmax(x));return {"value":float(x[i]),"u":float(t[i])}
def run(which):
    cid,lab=CASES[which];c=next(x for x in json.loads((SOURCE/"cases.json").read_text()) if x["id"]==cid)
    m=model(c,.05);init=m.initial_augmented(.1)
    eps=np.sqrt(2*((1+m.g.sum())*.01/2/40000))
    with np.load(ARCH) as saved: W=saved[lab+"_final_tangent"];B=saved[lab+"_initial_injection"]
    assert W.shape==B.shape==(560,180)
    _,s,vt=np.linalg.svd(W[1:40],full_matrices=False)
    phase=vt[0];phase*=1 if phase[np.argmax(abs(phase))]>=0 else -1
    assert abs(eps*s[0]-({"limiting":.03500971996661153,"nominal":.03520937943792633}[which]))<2e-6
    t=np.linspace(0,100,401);opts=dict(t_eval=t,rtol=2e-11,atol=2e-14,method="DOP853")
    r=solve_ivp(m.ode,(0,100),init,**opts);assert r.success
    Yr=r.y.T;Xr=Yr[:,1:40].reshape(-1,13,3);vr=m.volumes(Yr[:,:40])
    dr=np.linalg.norm((Yr[:,1:40]-init[1:40]).reshape(401,39),axis=1)
    rows={};records={}
    for amp in [-1.,-.5,.5,1.]:
        y0=init.copy();y0[:560]+=amp*eps*(B@phase)
        expected=(1+m.g.sum())*.01/2*(1+amp*amp/40000)
        assert abs(m.energy(y0)-expected)<1e-11
        sol=solve_ivp(m.ode,(0,100),y0,**opts);assert sol.success
        Y=sol.y.T;X=Y[:,1:40].reshape(-1,13,3)
        raw=np.linalg.norm((X-Xr).reshape(401,39),axis=1)
        frame=np.array([aligned(Xr[i],X[i]) for i in range(401)])
        H=Y[:,190:280].reshape(-1,30,3)
        lengths=np.linalg.norm(H[:,m.housing_index]-X[:,m.anchor_index],axis=-1)
        vols=m.volumes(Y[:,:40]);delta_v=vols.mean(1)-vr.mean(1)
        energies=np.array([m.energy(z) for z in Y]);balance=max(abs(energies+Y[:,-1]-m.energy(y0)))/m.energy(y0)
        assert balance<1e-7
        pred=amp*eps*(W[1:40]@phase)
        rem=np.linalg.norm((X[-1]-Xr[-1]).ravel()-pred)
        rows[str(amp)]={"max_raw_relative":peak(t,raw),"max_aligned":peak(t,frame[:,0]),
          "max_chart_tail":peak(t,frame[:,1]),"min_strut":float(lengths.min()),
          "min_oriented_volume":float(vols.min()),
          "max_abs_mean_volume_change":float(max(abs(delta_v))),
          "inside_r0p036_on_samples":bool(max(raw)<=.036),
          "flow_endpoint_raw_remainder":float(rem),"energy_heat_error":float(balance),
          "nfev":sol.nfev,
          "decimation_step1_max_raw":float(max(raw[::4]))}
        records[str(amp)]=np.column_stack((t,raw,frame,dr,lengths.min(1),vols.min(1),delta_v)).tolist()
    return {"status":"NUMERICAL_SELECTED_PHASES_ONLY","case":cid,"phase_origin":"top singular vector final source W(100) primary rows",
     "phase_sha256":hashlib.sha256(phase.tobytes()).hexdigest(),"epsilon":float(eps),
     "reference_max":peak(t,dr),"reference_within_d0p05_on_samples":bool(max(dr)<=.05),
     "reference_nfev":r.nfev,"integrator":"DOP853 rtol2e-11 atol2e-14, 401 samples",
     "columns":["u","raw_relative","moving_SO3_aligned","chart_tail","reference_shift","min_strut","min_volume","mean_volume_change"],
     "summary":rows,"records":records,
     "scope":"Four target-exposed finite housing phase preparations, NOT full 180D ball nor continuous time interval proof"}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--case",choices=tuple(CASES),required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args()
 res=run(a.case);a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(res,sort_keys=True,indent=2)+"\n")
 print("ICO_RADIAL_SUMMARY:"+json.dumps({k:v for k,v in res.items() if k!="records"},sort_keys=True),flush=True)
