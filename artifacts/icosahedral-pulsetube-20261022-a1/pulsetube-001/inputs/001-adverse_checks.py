"""Finite-amplitude tests of predeclared adverse phases; not a ball enclosure."""
import argparse,json,csv,hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
from scipy.integrate import solve_ivp
from jacobian import model,ROOT
from variational import SOURCE,IDS

def run(job):
    case,amp,out=job;m=model(case,.05);data=np.load(out/f"response-{case['id']}-fine0.npz")
    a=data['adverse_phase'];B=data['initial_injection'];ref=data['reference'];time=data['u'];H=data['mean_volume_derivative'];WF=data['final_tangent']
    Eh=(1+m.g.sum())*.01/2/40000;epsilon=np.sqrt(2*Eh);initial=m.initial_augmented(.1);initial[:560]+=amp*epsilon*(B@a)
    Ep=(1+m.g.sum())*.01/2;assert abs(m.energy(initial)-(Ep+amp*amp*Eh))<1e-12
    t=np.linspace(0,100,4001);sol=solve_ivp(m.ode,(0,100),initial,method='DOP853',t_eval=t,rtol=2e-11,atol=2e-14)
    assert sol.success;Y=sol.y.T;YC=Y[::4];assert len(YC)==len(ref)==1001
    vol=m.volumes(Y[:,:40]);refvol=m.volumes(ref[:,:40]);signal=vol.mean(1)-1;refsignal=refvol.mean(1)-1
    first=refsignal+amp*epsilon*(H@a);residual=signal[::4]-first
    E=np.array([m.energy(y) for y in Y]);balance=float(np.max(abs(E+Y[:,-1]-E[0]))/E[0]);assert balance<1e-8
    X=Y[:,1:40].reshape(-1,13,3);V=Y[:,281:320].reshape(-1,13,3)
    housing=Y[:,190:280].reshape(-1,30,3);VH=Y[:,470:560].reshape(-1,30,3);mass=m.m/m.R2
    P=(mass[None,:,None]*V).sum(1)+(m.hm[None,:,None]*VH).sum(1)
    L=(mass[None,:,None]*np.cross(X,V)).sum(1)+(m.hm[None,:,None]*np.cross(housing,VH)).sum(1)
    ell=np.linalg.norm(housing[:,m.housing_index]-X[:,m.anchor_index],axis=2)
    dP=float(np.max(np.linalg.norm(P-P[0],axis=1)));dL=float(np.max(np.linalg.norm(L-L[0],axis=1)));assert max(dP,dL)<2e-11
    if case['baseline_id']=='nominal':
        _,b=m.collective(t,.1);baseline=float(np.sqrt(np.trapezoid(((1+b)**3-1)**2,t)/100))
    else:baseline=json.loads((SOURCE/'baselines.json').read_text())[case['baseline_id']]['mean_volume_rms']
    true_rms=float(np.sqrt(np.trapezoid(signal*signal,t)/100))
    coarse_rms=float(np.sqrt(np.trapezoid(signal[::4]**2,time)/100));pred_rms=float(np.sqrt(np.trapezoid(first*first,time)/100))
    flow_error=YC[-1,:560]-ref[-1,:560]-amp*epsilon*(WF@a)
    row={'id':case['id'],'amplitude_factor':amp,'housing_energy':float(Eh*amp*amp),'phase_sha256':hashlib.sha256(a.tobytes()).hexdigest(),
         'mean_volume_rms':true_rms,'breathing_retention':true_rms/baseline,'first_order_predicted_rms_on_matching_grid':pred_rms,
         'actual_rms_on_matching_grid':coarse_rms,'actual_minus_first_order_rms':coarse_rms-pred_rms,
         'mean_volume_taylor_residual_rms':float(np.sqrt(np.trapezoid(residual*residual,time)/100)),
         'maximum_mean_volume_taylor_residual':float(np.max(abs(residual))),
         'final_primary_position_flow_remainder_norm':float(np.linalg.norm(flow_error[1:40])),
         'final_housing_position_flow_remainder_norm':float(np.linalg.norm(flow_error[190:280])),
         'maximum_full_state_difference_from_augmented_reference':float(np.max(abs(YC-ref))),
         'minimum_sampled_strut_length':float(ell.min()),'minimum_sampled_oriented_cell_volume':float(vol.min()),
         'maximum_sampled_oriented_cell_volume':float(vol.max()),'energy_plus_heat_relative_error':balance,
         'P_drift':dP,'L_drift':dL,'initial_P_norm':float(np.linalg.norm(P[0])),'initial_L_norm':float(np.linalg.norm(L[0])),
         'rtol':2e-11,'atol':2e-14,'samples':4001,'evidence':'NUMERICAL finite exposed phase; not worst-case nonlinear ball search or enclosure'}
    stem=f"adverse-{case['id']}-amp{amp}"
    with (out/(stem+'.csv')).open('w',newline='') as stream:
        columns=['u','mean_volume_signal','reference_signal','first_order_prediction','taylor_residual']
        w=csv.DictWriter(stream,fieldnames=columns,lineterminator='\n');w.writeheader()
        for i in range(len(time)):w.writerow(dict(zip(columns,[float(time[i]),float(signal[4*i]),float(refsignal[i]),float(first[i]),float(residual[i])])))
    (out/(stem+'.json')).write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True);return row

def main(out,workers):
    by={p['id']:p for p in json.loads((SOURCE/'cases.json').read_text())};jobs=[(by[id],a,out) for id in IDS for a in [1.,-1.,.5]]+[(by[IDS[0]],0.,out)]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures=[pool.submit(run,j) for j in jobs];rows=[f.result() for f in as_completed(futures)]
    rows.sort(key=lambda r:(r['id'],r['amplitude_factor']));scaling=[]
    for id in IDS:
        full=next(r for r in rows if r['id']==id and r['amplitude_factor']==1.)
        half=next(r for r in rows if r['id']==id and r['amplitude_factor']==.5)
        scaling.append({'id':id,'quarter_energy_to_full_energy_mean_volume_residual_ratio':half['mean_volume_taylor_residual_rms']/full['mean_volume_taylor_residual_rms'],
                        'meaning':'Directional amplitude scaling, not a uniform Hessian bound.'})
    (out/'adverse_checks.json').write_text(json.dumps({'status':'FINITE_PHASE_CHECKS_COMPLETE_TUBE_OPEN','records':rows,'scaling':scaling},indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);p.add_argument('--workers',type=int,default=2);a=p.parse_args();main(a.out,a.workers)
