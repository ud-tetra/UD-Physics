"""Post-exposure Phase B; see AMENDMENT_v1.1.md. Preserve Phase A outputs."""
from pathlib import Path
from itertools import product
import argparse,json,math,importlib.util
import numpy as np
from scipy.linalg import eig,eigh
from scipy.integrate import solve_ivp
from network import Network
spec=importlib.util.spec_from_file_location('multiport_phaseA',Path(__file__).with_name('analyze.py'))
phaseA=importlib.util.module_from_spec(spec);spec.loader.exec_module(phaseA)
dump,csvout,run,readouts,ROOT=phaseA.dump,phaseA.csvout,phaseA.run,phaseA.readouts,phaseA.ROOT


def volume_rows(m):
    J=np.zeros((20,40))
    for n,face in enumerate(m.face):
        r=m.ref[face];a,b,c=r
        gs=np.array([np.cross(b,c),np.cross(c,a),np.cross(a,b)])*m.sign[n]/(6*m.vcell)
        for i,g in zip(face,gs):J[n,1+3*i:4+3*i]=g
        J[n,1:4]=-gs.sum(axis=0)
    return J


def linear_data(m,t):
    rigid=[]
    for a in np.eye(3):rigid.append(np.r_[0.,np.tile(a,13)])
    for a in np.eye(3):rigid.append(np.r_[0.,np.cross(np.tile(a,(13,1)),m.ref).ravel()])
    qr,_=np.linalg.qr(np.array(rigid).T*m.rootmass[:,None],mode='complete');Q=qr[:,6:]
    assert Q.shape==(40,34)
    Dfull=m.rows(m.initial[:40])/m.rootmass[None,:]@Q
    U,s,Vh=np.linalg.svd(Dfull,full_matrices=False);assert sum(s>1e-10)==32
    U=U[:,:32];D=U.T@Dfull;assert np.linalg.norm(U@D-Dfull)<1e-13
    H=Q.T@m.H0@Q;B=volume_rows(m)@ (Q/m.rootmass[:,None]);q0=Q.T@(m.rootmass*np.r_[1.,np.zeros(39)])
    lam,V=eigh(H);assert min(lam)>0
    base=V@(np.cos(np.sqrt(lam)[:,None]*t)*(V.T@q0)[:,None]);yb=B@base
    base_rms=math.sqrt(np.trapezoid(yb.mean(axis=0)**2,t)/(t[-1]-t[0]))
    return Q,U,D,H,B,q0,base_rms


def pulse(parameters,data,t):
    mu,k,g=[parameters[x] for x in ['mu','kappa','gamma']];Q,U,D,H,B,q0,base_rms=data
    n=66;K=np.block([[H+.1*k*D.T@D,-k*np.sqrt(.1/mu)*D.T],[-k*np.sqrt(.1/mu)*D,(k/mu)*np.eye(32)]])
    C=np.diag(np.r_[np.zeros(34),np.full(32,g/mu)]);A=np.block([[np.zeros((n,n)),np.eye(n)],[-K,-C]])
    init=np.r_[q0,np.zeros(32+n)];poles,V=eig(A);coef=np.linalg.solve(V,init)
    solution=(V@ (np.exp(poles[:,None]*t)*coef[:,None])).real;y=B@solution[:34]
    # Check spectral reconstruction of initial condition; avoids silent defective eigensolves.
    assert np.max(abs(solution[:,0]-init))<2e-9
    norm=np.trapezoid(np.sum(y*y,axis=0),t);p=y-y.mean(axis=0,keepdims=True)
    leak=math.sqrt(np.trapezoid(np.sum(p*p,axis=0),t)/norm)
    rms=math.sqrt(np.trapezoid(y.mean(axis=0)**2,t)/(t[-1]-t[0]))
    return {'volume_signal_leakage_linear':leak,'mean_volume_rms_retention_linear':rms/base_rms},A,solution


def main(out):
    props=json.loads((out/'properties.json').read_text());t=np.linspace(0,100,2001);prepared=[]
    for p in props:
        kw={k:p[k] for k in ['m','g','k']};model=Network(**kw);prepared.append((p['id'],kw,linear_data(model,t)))
    rows=[];best=None
    for mu,k,g in product([.2,2.,20.],[2.,10.,50.],[.5,5.,50.]):
        parameters={'mu':mu,'kappa':k,'gamma':g};details=[]
        for name,kw,data in prepared:
            info,_,_=pulse(parameters,data,t);details.append({'property_id':name,**info})
        worst=max(r['volume_signal_leakage_linear'] for r in details);ret=min(r['mean_volume_rms_retention_linear'] for r in details)
        row={**parameters,'maximum_volume_leakage_linear':worst,'minimum_rms_retention_linear':ret,'eligible_retention80':bool(ret>=.8)};rows.append(row)
        if ret>=.8 and (best is None or worst<best['maximum_volume_leakage_linear']):best=row
    assert best is not None;parameters={k:best[k] for k in ['mu','kappa','gamma']};csvout(out/'readout-scan.csv',rows);dump(out/'readout-selection.json',best)
    print('phaseB selection',best,flush=True)
    # Verify active-auxiliary reduction against unreduced linear point+150branch equations.
    name,kw,data=prepared[0];mod=Network(**parameters,**kw);Q,U,D,H,B,q0,base_rms=data
    info,A,reduced=pulse(parameters,data,np.array([0.,.7]));nr=mod.n
    J=mod.rows(mod.initial[:40]);K0=mod.H0*mod.rootmass[:,None]*mod.rootmass[None,:]
    K=np.block([[K0+.1*mod.kappa*J.T@J,-.1*mod.kappa*J.T],[-.1*mod.kappa*J,.1*mod.kappa*np.eye(150)]])
    mass=np.r_[mod.mass,np.full(150,.1*mod.mu)];C=np.diag(np.r_[np.zeros(40),np.full(150,.1*mod.gamma)])
    ini=np.zeros(2*nr);ini[0]=1.
    sol=solve_ivp(lambda u,z:np.r_[z[nr:],-(K@z[:nr]+C@z[nr:])/mass],(0,.7),ini,t_eval=[.7],method='DOP853',rtol=2e-12,atol=2e-14)
    assert sol.success
    xx=(Q/mod.rootmass[:,None])@reduced[:34,-1];zz=(U@reduced[34:66,-1])/math.sqrt(.1*mod.mu)
    reduction_error=float(max(abs(sol.y[:nr,-1]-np.r_[xx,zz])));assert reduction_error<3e-10
    # Independent finite-difference check of first-order geometric volume readout.
    rng=np.random.default_rng(57);direction=rng.normal(size=40);direction[0]=0;eps=1e-6
    reference=mod.initial[:40].copy();reference[0]=0
    fd=(mod.volumes(np.array([reference+eps*direction]))[0]-mod.volumes(np.array([reference-eps*direction]))[0])/(2*eps)
    volume_derivative_error=float(max(abs(fd-volume_rows(mod)@direction)));assert volume_derivative_error<2e-9
    old=list(__import__('csv').DictReader((ROOT/'artifacts/icosahedral-damping-20261022-a1/damping-001/files/campaign.csv').open()))
    rows=[];worst=None;symmetric=[]
    model=Network(**parameters)
    for amplitude in [.025,.1,.2]:
        x,v,si=run(model,amplitude,t);alpha,b=model.collective(t,amplitude)
        pred=np.repeat(model.ref[None,:,:],len(t),axis=0);pred[:,1:]*=1+b[:,None,None]
        err=float(max(np.max(abs(x[:,0]-alpha)),np.max(abs(x[:,1:].reshape(-1,13,3)-pred))))
        assert err<5e-9 and si['maximum_auxiliary_displacement']<1e-10
        symmetric.append({'amplitude':amplitude,'analytic_error':err,**si})
        for name,kw,data in prepared:
            mod=Network(**parameters,**kw);x,v,info=run(mod,amplitude,t)
            base=next(r for r in old if r['property_id']==name and float(r['amplitude'])==amplitude and float(r['cs'])==float(r['ce'])==0.)
            ret=info['mean_volume_rms']/float(base['mean_volume_rms']);shape=info['shell_shape_rms']/float(base['shell_shape_rms']);hub=info['hub_offset_rms_over_R']/float(base['hub_offset_rms_over_R'])
            row={'amplitude':amplitude,'property_id':name,**info,'mean_volume_rms_retention':ret,'shape_rms_ratio':shape,'hub_offset_rms_ratio':hub,
                 'passes_80pct_5pct_50pct_screen':bool(ret>=.8 and info['volume_signal_leakage']<=.05 and shape<=.5)};rows.append(row)
            if worst is None or info['volume_signal_leakage']>worst[0]:worst=(info['volume_signal_leakage'],amplitude,name,kw,info)
            print('phaseB nonlinear',amplitude,name,ret,info['volume_signal_leakage'],shape,flush=True)
    csvout(out/'readout-campaign.csv',rows)
    direction=np.array(json.loads((out/'ratio-direction.json').read_text()));ratio=[];_,b=model.collective(t,.1);analytic=readouts.rms((1+b)**3-1,t)
    for e in [.001,.01]:
        _,_,info=run(Network(**parameters,ratio_error=e*direction),.1,t);ratio.append({'maximum_ratio_error':e,**info,'mean_volume_rms_retention':info['mean_volume_rms']/analytic})
    _,amplitude,name,kw,coarse=worst;_,_,fine=run(Network(**parameters,**kw),amplitude,np.linspace(0,100,4001),True)
    delta=abs(fine['volume_signal_leakage']-coarse['volume_signal_leakage']);assert delta<3e-6
    summary={'status':'PASS','phase':'B:post-exposure readout-directed engineering selection','selected':best,'grid_evaluations':27,'unique_total_phaseA_plusB':53,
             'linear_reduction_error_vs_unreduced380phase':reduction_error,'volume_derivative_error':volume_derivative_error,
             'symmetric_checks':symmetric,'screen_pass_count':sum(r['passes_80pct_5pct_50pct_screen'] for r in rows),'campaign_points':9,
             'minimum_mean_volume_rms_retention':min(r['mean_volume_rms_retention'] for r in rows),
             'maximum_volume_leakage':max(r['volume_signal_leakage'] for r in rows),
             'maximum_shell_centroid_volume_leakage':max(r['shell_centroid_volume_signal_leakage'] for r in rows),
             'shape_rms_ratio_range':[min(r['shape_rms_ratio'] for r in rows),max(r['shape_rms_ratio'] for r in rows)],
             'maximum_hub_offset_rms_ratio':max(r['hub_offset_rms_ratio'] for r in rows),
             'maximum_energy_balance_relative_error':max(r['balance_relative_error'] for r in rows+symmetric+ratio),
             'minimum_sampled_volume_ratio':min(r['minimum_oriented_cell_volume_ratio'] for r in rows+symmetric+ratio),
             'maximum_P_drift':max(r['linear_momentum_drift'] for r in rows+symmetric+ratio),
             'maximum_L_drift':max(r['angular_momentum_drift'] for r in rows+symmetric+ratio),
             'ratio_error_checks':ratio,'refinement':{'amplitude':amplitude,'property_id':name,'coarse':coarse,'fine':fine,'volume_leakage_change':delta},
             'limits':['Amendment and all reused property points are exposed design data;no held-out prediction','Ideal reciprocal transmission and two-terminal inerter laws assumed;no built linkage,housing mass or parasitic friction test','Linear pulse selects a finite nonlinear campaign;no continuous-box guarantee','Energy/passivity and linear equilibrium asymptotic decay do not establish all-time nonlinear coherence']}
    dump(out/'readout-summary.json',summary);print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
