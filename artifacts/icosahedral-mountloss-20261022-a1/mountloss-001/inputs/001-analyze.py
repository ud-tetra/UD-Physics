"""Declared damping scan followed by exact-byte frozen joint development probes."""
from pathlib import Path
import argparse,csv,json,importlib.util
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import scipy
from scipy.linalg import null_space,expm,eigh,eigvals
from scipy.integrate import solve_ivp
from mountloss import MountLoss,Damped,readouts,ROOT

spec=importlib.util.spec_from_file_location('mount_parent_campaign',ROOT/'experiments/icosahedral-tolerances/analyze.py')
parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
OLD=ROOT/'artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files'
GRID=[0.,.005,.01,.02,.05,.1,.2,.5,1.]

def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def csvout(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def reduced_basis(m,M):
    cols=[];A=m.midpoints(m.ref)
    for u in np.eye(3):cols.append(np.r_[0.,np.tile(u,13),np.zeros(150),np.tile(u,30)])
    for u in np.eye(3):cols.append(np.r_[0.,np.cross(u,m.ref).ravel(),np.zeros(150),np.cross(u,A).ravel()])
    D=np.sqrt(M)[:,None]*np.column_stack(cols);q,_=np.linalg.qr(D,mode='complete')
    return q[:,6:],D

def hidden_phase(m,M,Q):
    N=np.zeros((12,30))
    for e,(i,j) in enumerate(m.edges):N[i-1,e]=N[j-1,e]=1
    S=np.kron(null_space(N*np.sqrt(m.hm)[None,:]),np.eye(3))
    assert S.shape==(90,54)
    U=np.zeros((m.n,54));U[190:]=S
    D=Q.T@U;Z=np.zeros_like(D)
    return np.block([[D/m.omega_h,Z],[Z,D]])

def linear_probe(m,save_vector=False):
    M,K,C=m.linear_matrices();Q,rigid=reduced_basis(m,M)
    assert max(np.max(abs(K@rigid)),np.max(abs(C@rigid)))<2e-12
    k=Q.T@K@Q;c=Q.T@C@Q;n=len(k);lam=eigh(k,eigvals_only=True)
    assert lam[0]>1e-3
    A=np.block([[np.zeros((n,n)),np.eye(n)],[-k,-c]])
    B=hidden_phase(m,M,Q);metric=np.block([[k,np.zeros_like(k)],[np.zeros_like(k),np.eye(n)]])
    assert np.max(abs(B.T@metric@B-np.eye(108)))<2e-12
    final=expm(100*A)@B;gram=final.T@metric@final;values,vectors=eigh((gram+gram.T)/2)
    assert values[-1]<1+2e-10
    poles=eigvals(A);slow=float(-max(poles.real))
    result={'nu':m.nu,'eta':m.eta,'worst_hidden_energy_fraction_u100':float(values[-1]),
            'least_nonrigid_decay_rate':slow,'min_nonrigid_stiffness':float(lam[0])}
    vector=None
    if save_vector:
        phase=B@vectors[:,-1];vector=np.r_[Q@phase[:n]/np.sqrt(M),Q@phase[n:]/np.sqrt(M)]
    return result,vector

def extra_metrics(m,Y,info):
    lengths=[]
    for y in Y[::10]:lengths.append(min(m.loss_geometry(y[:40],y[190:m.n].reshape(30,3))[1]))
    info['minimum_sampled_housing_strut_length']=float(min(lengths))
    assert min(lengths)>.05
    return info

def pulse(m,t,rtol=1e-10,atol=1e-12):
    Y,info=parent.run(m,t,rtol,atol);return Y,extra_metrics(m,Y,info)

def symmetric_baseline(t):
    m=MountLoss();_,b=m.collective(t,.1)
    return float(np.sqrt(np.trapezoid(((1+b)**3-1)**2,t)/(t[-1]-t[0])))

def scan_worker(nu):
    m=MountLoss(nu=nu);linear,_=linear_probe(m)
    t=np.linspace(0,100,2001);_,info=pulse(m,t)
    linear.update(nominal_breathing_retention=info['mean_volume_rms']/symmetric_baseline(t),
                  energy_balance_error=info['balance_relative_error'])
    linear['passes_joint_scan_gate']=bool(nu>0 and linear['worst_hidden_energy_fraction_u100']<=.5 and linear['nominal_breathing_retention']>=.8)
    return linear

def checks():
    m=MountLoss(nu=.02);rng=np.random.default_rng(31475)
    x=m.initial[:40].copy();x[0]=0;x[1:]+=rng.normal(0,.003,39)
    H=m.midpoints(m.ref)+rng.normal(0,.002,(30,3));v=rng.normal(0,.03,40);V=rng.normal(0,.03,(30,3))
    gp,gh,p=m.housing_loss(x,H,v,V);points=x[1:].reshape(13,3)
    force=float(np.linalg.norm(gp[1:].reshape(13,3).sum(0)+gh.sum(0)))
    torque=float(np.linalg.norm(np.cross(points,gp[1:].reshape(13,3)).sum(0)+np.cross(H,gh).sum(0)))
    power=float(abs(v@gp+np.sum(V*gh)-p))
    direction=rng.normal(size=130);eps=1e-6
    def R(w):return m.housing_loss(x,H,w[:40],w[40:].reshape(30,3))[2]/2
    w=np.r_[v,V.ravel()];fd=(R(w+eps*direction)-R(w-eps*direction))/(2*eps)
    gradient=float(abs(fd-np.r_[gp,gh.ravel()]@direction))
    assert max(force,torque,power,gradient)<1e-12
    # Compare the analytic full linear matrix to an odd finite-difference ODE derivative.
    M,K,C=m.linear_matrices();s=np.sqrt(M);q=rng.normal(size=280);vel=rng.normal(size=280)
    base=m.initial_augmented(0.);d=np.r_[q/s,vel/s,0.];eps=1e-6
    observed=(m.ode(0,base+eps*d)-m.ode(0,base-eps*d))/(2*eps)
    jac=float(np.max(abs(observed[280:560]*s+K@q+C@vel)))
    assert jac<2e-6
    local=m.collective_loss(0,0)-m.collective_matrices()[2]
    reduced=float(np.max(abs(local[1:,1:]/m.eta-np.array([[35,10],[10,5]]))))
    assert reduced<2e-12
    return {'force_error':force,'torque_error':torque,'power_error':power,'rayleigh_gradient_error':gradient,
            'linear_ode_matrix_error':jac,'reduced_reference_matrix_error':reduced}

def model(case,nu):return MountLoss(nu=nu,beta=case['beta'],omega_h=case['omega_h'],cf=case['cf'],housing_weights=case['housing_weights'],ratio_error=case['ratio_error'],**case['primary'])
def worker(item):
    case,nu=item;_,info=pulse(model(case,nu),np.linspace(0,100,2001));return case['id'],info

def ringdown(m,direction,out,name,epsilon=1e-4):
    initial=m.initial_augmented(0.);initial[:560]+=epsilon*direction
    t=np.linspace(0,100,2001)
    sol=solve_ivp(m.ode,(0,100),initial,t_eval=t,method='DOP853',rtol=2e-12,atol=1e-15);assert sol.success
    Y=sol.y.T;E=np.array([m.energy(y) for y in Y]);ratio=E/E[0]
    err=float(max(abs(E+Y[:,-1]-E[0]))/E[0]);assert err<2e-7
    csvout(out/(name+'.csv'),[{'u':float(u),'mechanical_energy_fraction':float(e),'heat_fraction':float(h/E[0])} for u,e,h in zip(t,ratio,Y[:,-1])])
    return {'id':name,'epsilon':epsilon,'final_energy_fraction':float(ratio[-1]),'energy_balance_error':err,
            'maximum_primary_displacement':float(np.max(abs(Y[:,:40]-m.initial_augmented(0.)[None,:40])))}

def symmetric_check(nu,out):
    m=MountLoss(nu=nu);t=np.linspace(0,100,2001);M,K,_,_=m.collective_matrices()
    def ode(u,y):return np.r_[y[3:],np.linalg.solve(M,-K@y[:3]-m.collective_loss(y[1],y[2])@y[3:])]
    sol=solve_ivp(ode,(0,100),[.1,0,0,0,0,0],t_eval=t,method='DOP853',rtol=2e-12,atol=2e-14);assert sol.success
    Y,info=pulse(m,t);a,b,c=sol.y[:3]
    points=m.ref[None,:,:]*(1+b[:,None,None]);H=m.midpoints(m.ref)[None,:,:]*(1+c[:,None,None])
    error=float(max(np.max(abs(Y[:,0]-a)),np.max(abs(Y[:,1:40].reshape(-1,13,3)-points)),np.max(abs(Y[:,190:280].reshape(-1,30,3)-H))))
    assert error<8e-9 and np.max(abs(Y[:,40:190]))<1e-10
    return {'full_vs_nonlinear_collective_error':error,**info}

def main(out):
    out.mkdir(parents=True,exist_ok=True);audit=checks();dump(out/'checks.json',audit);print('force/matrix checks PASS',audit,flush=True)
    scans=[]
    with ProcessPoolExecutor(max_workers=2) as pool:
        for row in pool.map(scan_worker,GRID):scans.append(row);print('scan',row,flush=True)
    csvout(out/'scan.csv',scans)
    good=[s for s in scans if s['passes_joint_scan_gate']]
    housing=[s for s in scans if s['nu']>0 and s['worst_hidden_energy_fraction_u100']<=.5]
    if not housing:dump(out/'selection.json',{'status':'FAILED_NO_HOUSING_GATE','scan':scans});return
    selected=(good or housing)[0];nu=selected['nu'];selection={'status':'PASS' if good else 'FAILED_JOINT_GATE','selected_nu':nu,'selected':selected,'selection_rule':'smallest declared nu meeting both gates; if none, smallest housing-gate nu to quantify failure'}
    dump(out/'selection.json',selection);print('SELECTION',selection,flush=True)
    # Exact-byte copies preserve provenance. Input cases and baselines are never regenerated.
    for f in ['probes.json','baselines.json']:(out/f).write_bytes((OLD/f).read_bytes())
    cases=json.loads((out/'probes.json').read_text());base=json.loads((out/'baselines.json').read_text());measured={}
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures={pool.submit(worker,(p,nu)):p['id'] for p in cases}
        for f in as_completed(futures):
            id,info=f.result();measured[id]=info;print('joint',id,info['volume_signal_leakage'],flush=True)
    rows=[]
    for case in cases:
        info=measured[case['id']];b=base[case['baseline_id']];ret=info['mean_volume_rms']/b['mean_volume_rms'];shape=info['shell_shape_rms']/b['shell_shape_rms']
        rows.append({'id':case['id'],'group':case['group'],'nu':nu,**info,'breathing_retention':ret,'shape_rms_ratio':shape,
                     'passes_screen':bool(ret>=.8 and info['volume_signal_leakage']<=.05 and shape<=.5)})
    csvout(out/'campaign.csv',rows);budget=[r for r in rows if r['group']!='challenge']
    worst=max(budget,key=lambda r:r['volume_signal_leakage']);low=min(budget,key=lambda r:r['breathing_retention'])
    refined=[]
    for id in dict.fromkeys([worst['id'],low['id']]):
        case=next(p for p in cases if p['id']==id);_,info=pulse(model(case,nu),np.linspace(0,100,4001),2e-12,2e-14)
        row=next(r for r in rows if r['id']==id);ret=info['mean_volume_rms']/base[case['baseline_id']]['mean_volume_rms']
        dL=abs(info['volume_signal_leakage']-row['volume_signal_leakage']);dr=abs(ret-row['breathing_retention'])
        assert dL<3e-6 and dr<3e-6
        refined.append({'id':id,'fine':info,'fine_retention':ret,'mismatch_change':dL,'retention_change':dr})
    sym=symmetric_check(nu,out);dump(out/'symmetric.json',sym)
    m=MountLoss(nu=nu);lin,vector=linear_probe(m,True);np.save(out/'worst_hidden_phase.npy',vector,allow_pickle=False)
    cycle=json.loads((OLD/'mount-modes.json').read_text());q=np.asarray(cycle['integer_edge_amplitudes']);d=np.zeros(560);d[190:280:3]=q
    ring=[ringdown(MountLoss(nu=0),d,out,'old-cycle-no-loss'),ringdown(m,d,out,'old-cycle-with-loss'),ringdown(m,vector,out,'worst-hidden-with-loss')]
    # Same finite housing phase added to the worst-budget alpha pulse; separate amended challenge.
    case=next(p for p in cases if p['id']==worst['id']);joint=model(case,nu);initial=joint.initial_augmented(.1);initial[:560]+=1e-4*vector
    sol=solve_ivp(joint.ode,(0,100),initial,t_eval=np.linspace(0,100,2001),method='DOP853',rtol=1e-10,atol=1e-12);assert sol.success
    Y=sol.y.T;info=readouts.metrics(joint,sol.t,Y[:,:40],Y[:,280:320]);E=np.array([joint.energy(y) for y in Y]);err=float(max(abs(E+Y[:,-1]-E[0]))/E[0]);assert err<8e-8
    seeded={'id':case['id']+'-housing-seed','housing_phase_scale':1e-4,'breathing_retention':info['mean_volume_rms']/base[case['baseline_id']]['mean_volume_rms'],
            'shape_rms_ratio':info['shell_shape_rms']/base[case['baseline_id']]['shell_shape_rms'],'energy_balance_error':err,**info}
    seeded['passes_screen']=bool(seeded['breathing_retention']>=.8 and info['volume_signal_leakage']<=.05 and seeded['shape_rms_ratio']<=.5)
    report={'status':'PASS' if all(r['passes_screen'] for r in budget) and good else 'FAILED_SCREEN','numpy':np.__version__,'scipy':scipy.__version__,
            'selection':selection,'checks':audit,'budget_points':len(budget),'budget_passes':sum(r['passes_screen'] for r in budget),
            'minimum_breathing_retention':min(r['breathing_retention'] for r in budget),'maximum_hub_volume_mismatch':max(r['volume_signal_leakage'] for r in budget),
            'shape_ratio_range':[min(r['shape_rms_ratio'] for r in budget),max(r['shape_rms_ratio'] for r in budget)],
            'maximum_energy_balance_error':max(r['balance_relative_error'] for r in rows+[sym]),'maximum_total_P_drift':max(r['total_linear_momentum_drift'] for r in rows+[sym]),
            'maximum_total_L_drift':max(r['total_angular_momentum_drift'] for r in rows+[sym]),'minimum_sampled_strut_length':min(r['minimum_sampled_housing_strut_length'] for r in rows+[sym]),
            'minimum_sampled_cell_volume':min(r['minimum_oriented_cell_volume_ratio'] for r in rows+[sym]),'refinements':refined,
            'ringdowns':ring,'selected_linear_hidden':lin,'seeded_pulse_challenge':seeded,'challenges':[r for r in rows if r['group']=='challenge'],
            'scope':'Exact passivity/force balance/local linear detection; finite nonlinear development campaign; no continuous box/global attraction/physical calibration claim.'}
    dump(out/'summary.json',report);print('FINAL',json.dumps(report,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
