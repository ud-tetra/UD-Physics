"""Frozen joint probes with all90housing and150relative auxiliary coordinates."""
from pathlib import Path
import argparse,csv,json,math
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import eigh
from hardware import Hardware,Damped,readouts,ROOT


def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def csvout(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def norm_pattern(v):
    v=np.asarray(v,float);v=v-v.mean();return v/max(abs(v))


def cases():
    old=json.loads((ROOT/'artifacts/icosahedral-multiport-20261022-a1/multiport-001/files/properties.json').read_text())
    rng=np.random.default_rng(90247);ratio=[np.ones(150),-np.ones(150),np.where(np.arange(150)%2,1.,-1.),rng.choice([-1.,1.],150)]
    hpat=[norm_pattern(np.cos(np.arange(30))),norm_pattern(-np.cos(np.arange(30))),norm_pattern(np.where(np.arange(30)%2,1.,-1.)),norm_pattern(rng.uniform(-1,1,30))]
    result=[]
    def item(id,group,p,delta,beta,cf,omega,hw):
        return {'id':id,'group':group,'baseline_id':p['id'],'primary':{k:p[k] for k in ['m','g','k']},'ratio_error':list(map(float,delta)),
                'beta':float(beta),'cf':float(cf),'omega_h':float(omega),'housing_weights':list(map(float,hw))}
    for p in old:
        for j in range(4):result.append(item(p['id']+f'-boundary{j}','boundary',p,.01*ratio[j],.05,.001,10,1+.1*hpat[j]))
    for j in range(8):
        p={'id':f'interior{j}','m':(1+.05*rng.uniform(-1,1,13)).tolist(),'g':(1+.05*rng.uniform(-1,1,12)).tolist(),'k':(.4*(1+.05*rng.uniform(-1,1,30))).tolist()}
        result.append(item(p['id'],'interior',p,rng.uniform(-.01,.01,150),rng.uniform(.005,.05),rng.uniform(0,.001),10,1+.1*norm_pattern(rng.uniform(-1,1,30))))
    p=old[0]
    for name,e,beta,cf,om in [('ratio3pct',.03,.05,.001,10),('mass20pct',.01,.2,.001,10),('friction02',.01,.05,.02,10),('mount4',.01,.05,.001,4)]:
        result.append(item(name,'challenge',p,e*ratio[3],beta,cf,om,1+.1*hpat[3]))
    assert len(result)==24;return result


def run(model,t,rtol=1e-10,atol=1e-12):
    y0=model.initial_augmented(.1)
    sol=solve_ivp(model.ode,(0,float(t[-1])),y0,t_eval=t,method='DOP853',rtol=rtol,atol=atol)
    assert sol.success;Y=sol.y.T;x=Y[:,:40];v=Y[:,model.n:model.n+40]
    E=np.array([model.energy(y) for y in Y]);loss=Y[:,-1]
    err=float(max(abs(E+loss-E[0]))/E[0]);assert err<8e-8 and min(np.diff(loss))>-1e-10
    info=readouts.metrics(model,t,x,v)
    info['primary_linear_momentum_exchange']=info.pop('linear_momentum_drift');info['primary_angular_momentum_exchange']=info.pop('angular_momentum_drift')
    H=Y[:,190:model.n].reshape(-1,30,3);HV=Y[:,model.n+190:2*model.n].reshape(-1,30,3)
    points=x[:,1:].reshape(-1,13,3);PV=v[:,1:].reshape(-1,13,3);pm=model.m/model.R2
    P=np.sum(pm[None,:,None]*PV,axis=1)+np.sum(model.hm[None,:,None]*HV,axis=1)
    L=np.sum(np.cross(points,PV)*pm[None,:,None],axis=1)+np.sum(np.cross(H,HV)*model.hm[None,:,None],axis=1)
    driftP=float(np.max(np.linalg.norm(P-P[0],axis=1)));driftL=float(np.max(np.linalg.norm(L-L[0],axis=1)))
    assert driftP<2e-11 and driftL<2e-11
    mid=(points[:,model.edge[:,0]]+points[:,model.edge[:,1]])/2
    info.update(balance_relative_error=err,total_linear_momentum_drift=driftP,total_angular_momentum_drift=driftL,
                remaining_total_energy_fraction=float(E[-1]/E[0]),maximum_housing_lag_over_a=float(np.max(np.linalg.norm(H-mid,axis=2))),
                maximum_auxiliary_stroke=float(np.max(abs(Y[:,40:190]))))
    return Y,info


def make_model(case):return Hardware(beta=case['beta'],omega_h=case['omega_h'],cf=case['cf'],housing_weights=case['housing_weights'],ratio_error=case['ratio_error'],**case['primary'])

def worker(case):
    model=make_model(case);_,info=run(model,np.linspace(0,100,2001));return case['id'],info


def baselines(probes,t):
    old=list(csv.DictReader((ROOT/'artifacts/icosahedral-damping-20261022-a1/damping-001/files/campaign.csv').open()));result={}
    for p in probes:
        id=p['baseline_id']
        if id in result:continue
        row=next((r for r in old if r['property_id']==id and float(r['amplitude'])==.1 and float(r['cs'])==float(r['ce'])==0),None)
        if row:
            result[id]={k:float(row[k]) for k in ['mean_volume_rms','shell_shape_rms','hub_offset_rms_over_R']}
        else:
            _,_,info=readouts.run(Damped(cs=0,ce=0,**p['primary']),.1,t)
            result[id]={k:info[k] for k in ['mean_volume_rms','shell_shape_rms','hub_offset_rms_over_R']}
    return result


def force_checks():
    m=Hardware();rng=np.random.default_rng(441);x=m.initial[:40].copy();x[1:]+=rng.normal(size=39)*.003
    H=m.midpoints(m.ref)+rng.normal(size=(30,3))*.002;gp,gh,U=m.mount_force(x,H)
    dx=rng.normal(size=40);dx/=np.linalg.norm(dx);dH=rng.normal(size=(30,3));dH/=np.linalg.norm(dH);eps=1e-6
    fd=(m.mount_force(x+eps*dx,H+eps*dH)[2]-m.mount_force(x-eps*dx,H-eps*dH)[2])/(2*eps)
    gradient_error=float(abs(fd-gp@dx-np.sum(gh*dH)));points=x[1:].reshape(13,3);pf=gp[1:].reshape(13,3)
    force_error=float(np.linalg.norm(pf.sum(axis=0)+gh.sum(axis=0)))
    torque_error=float(np.linalg.norm(np.cross(points,pf).sum(axis=0)+np.cross(H,gh).sum(axis=0)))
    assert gradient_error<2e-10 and force_error<1e-14 and torque_error<1e-14
    # A direct independent assembly checks the added Rayleigh input-port loss.
    v=rng.normal(size=40)*.02;f,power=Damped.damping_force(m,x,v);_,rn,en=m.strain_geometry(x)
    pv=v[1:].reshape(13,3);sd=np.sum(rn*(pv[1:]-pv[0]),axis=1)/m.R
    ed=np.sum(en*(pv[m.edge[:,0]]-pv[m.edge[:,1]]),axis=1)
    manual=m.cf/10*np.sum(np.r_[sd,ed][m.pairs]**2)
    power_error=float(max(abs(v@f-power),abs(power-manual)));assert power_error<1e-15
    return {'mount_energy_gradient_error':gradient_error,'net_mount_force_error':force_error,'net_mount_torque_error':torque_error,'input_friction_power_error':power_error}


def symmetric(out,t):
    records=[]
    for beta,om,cf in [(.05,10,0),(.05,10,.001),(.2,10,0),(.05,4,0)]:
        m=Hardware(beta=beta,omega_h=om,cf=cf);M,K,C,rho=m.collective_matrices()
        sol=solve_ivp(lambda u,y:np.r_[y[3:],np.linalg.solve(M,-K@y[:3]-C@y[3:])],(0,100),[.1,0,0,0,0,0],t_eval=t,method='DOP853',rtol=2e-12,atol=2e-14)
        assert sol.success;Y,info=run(m,t);x=Y[:,:40];alpha,b,c=sol.y[:3]
        predicted=np.repeat(m.ref[None,:,:],len(t),axis=0);predicted[:,1:]*=(1+b[:,None,None])
        predH=m.midpoints(m.ref)[None,:,:]*(1+c[:,None,None])
        err=float(max(np.max(abs(x[:,0]-alpha)),np.max(abs(x[:,1:].reshape(-1,13,3)-predicted)),np.max(abs(Y[:,190:m.n].reshape(-1,30,3)-predH))))
        assert err<8e-9 and np.max(abs(Y[:,40:190]))<1e-10
        frequencies=np.sqrt(eigh(K,M,eigvals_only=True));parent=np.sqrt([8-np.sqrt(37),8+np.sqrt(37)])
        records.append({'beta':beta,'omega_h':om,'cf':cf,'rho':rho,'full_vs_collective_error':err,'conservative_angular_frequencies':frequencies.tolist(),
                        'low_mode_frequency_ratios':(frequencies[:2]/parent).tolist(),**info})
    dump(out/'symmetric.json',records);print('symmetric560phase checks PASS',flush=True);return records


def main(out):
    out.mkdir(parents=True,exist_ok=True);probes=cases();dump(out/'probes.json',probes);t=np.linspace(0,100,2001)
    base=baselines(probes,t);dump(out/'baselines.json',base);checks=force_checks();sym=symmetric(out,t)
    # Independent trajectories in two CPU processes;no LLM delegation or shared-output writes.
    measured={}
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures={pool.submit(worker,p):p['id'] for p in probes}
        for f in as_completed(futures):
            id,info=f.result();measured[id]=info;print('probe',id,info['volume_signal_leakage'],flush=True)
    rows=[]
    for case in probes:
        info=measured[case['id']];b=base[case['baseline_id']];ret=info['mean_volume_rms']/b['mean_volume_rms'];shape=info['shell_shape_rms']/b['shell_shape_rms'];hub=info['hub_offset_rms_over_R']/b['hub_offset_rms_over_R']
        rows.append({'id':case['id'],'group':case['group'],'beta':case['beta'],'omega_h':case['omega_h'],'cf':case['cf'],**info,
                     'mean_volume_rms_vs_original_undamped':ret,'shape_rms_vs_original_undamped':shape,'hub_rms_vs_original_undamped':hub,
                     'passes_80pct_5pct_50pct_screen':bool(ret>=.8 and info['volume_signal_leakage']<=.05 and shape<=.5)})
    csvout(out/'campaign.csv',rows)
    budget=[r for r in rows if r['group']!='challenge'];w=max(budget,key=lambda r:r['volume_signal_leakage']);case=next(p for p in probes if p['id']==w['id'])
    _,fine=run(make_model(case),np.linspace(0,100,4001),rtol=2e-12,atol=2e-14);delta=abs(fine['volume_signal_leakage']-w['volume_signal_leakage']);assert delta<3e-6
    report={'status':'PASS','numpy':np.__version__,'scipy':scipy.__version__,'state':'280configuration/560phase plusoneheat accumulator;all90housingcoordinatesretained',
            'proposed_budget':{'ratio':.01,'beta':.05,'cf':.001,'omega_h':10,'housing_relative_weight_variation':.1,'primary_property_tolerance':.05,'A0':.1,'window':[0,100]},
            'force_checks':checks,'budget_points':len(budget),'budget_screen_passes':sum(r['passes_80pct_5pct_50pct_screen'] for r in budget),
            'minimum_breathing_rms_retention':min(r['mean_volume_rms_vs_original_undamped'] for r in budget),
            'maximum_hub_volume_mismatch':max(r['volume_signal_leakage'] for r in budget),'maximum_shell_centroid_mismatch':max(r['shell_centroid_volume_signal_leakage'] for r in budget),
            'shape_rms_ratio_range':[min(r['shape_rms_vs_original_undamped'] for r in budget),max(r['shape_rms_vs_original_undamped'] for r in budget)],
            'maximum_housing_lag_over_a':max(r['maximum_housing_lag_over_a'] for r in budget),
            'challenges':[r for r in rows if r['group']=='challenge'],'maximum_energy_balance_error':max(r['balance_relative_error'] for r in rows+sym),
            'maximum_total_P_drift':max(r['total_linear_momentum_drift'] for r in rows+sym),'maximum_total_L_drift':max(r['total_angular_momentum_drift'] for r in rows+sym),
            'minimum_sampled_cell_volume_ratio':min(r['minimum_oriented_cell_volume_ratio'] for r in rows+sym),
            'refinement':{'id':w['id'],'coarse_volume_mismatch':w['volume_signal_leakage'],'fine':fine,'mismatch_change':delta},
            'limits':['20finitejointprobesarenota continuouswholeassemblytolerance-boxcertificate','Exactmoduleimpedanceanduniformhousingfrequencybounds have narrower hypotheses than joint probes','Midpointpickup/springmountisadefinedsurrogate;arbitrarycasing/routing/gearrotormodesnotmodeled','Nominalmodulemu,kappa,gammafixed;independentcomponent/mountstiffnesstolerances notcovered','No physical testorclock/energycalibrationexecuted;bench protocol remainsUNSCORED']}
    dump(out/'summary.json',report);print(json.dumps(report,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
