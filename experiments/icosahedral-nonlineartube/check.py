"""Fresh constructor ODE checks of exposed phases; never an all-phase proof."""
from pathlib import Path
import sys,argparse,json,csv,hashlib
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import scipy
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-mountloss'))
from mountloss import MountLoss
SOURCE=ROOT/'artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files'

def make_model(p,nu):
    return MountLoss(nu=nu,beta=p['beta'],omega_h=p['omega_h'],cf=p['cf'],
                     housing_weights=p['housing_weights'],ratio_error=p['ratio_error'],**p['primary'])

def run(job):
    p,nu,phase,alpha,fine=job;m=make_model(p,nu);Ep=(1+m.g.sum())*.01/2;Eh=Ep/40000
    initial=m.initial_augmented(alpha);initial[190:280]+=np.sqrt(2*Eh)*phase[:90]
    initial[470:560]+=np.sqrt(2*Eh)*phase[90:]
    E0=m.energy(initial);assert abs(E0-((1+m.g.sum())*alpha**2/2+Eh))<1e-12
    t=np.linspace(0,100,4001);rtol,atol=(5e-12,5e-15) if fine else (2e-11,2e-14)
    sol=solve_ivp(m.ode,(0,100),initial,t_eval=t,method='DOP853',rtol=rtol,atol=atol)
    assert sol.success;Y=sol.y.T;E=np.array([m.energy(y) for y in Y]);vol=m.volumes(Y[:,:40])
    X=Y[:,1:40].reshape(-1,13,3);H=Y[:,190:280].reshape(-1,30,3)
    V=Y[:,281:320].reshape(-1,13,3);VH=Y[:,470:560].reshape(-1,30,3)
    pm=m.m/m.R2;P=(V*pm[None,:,None]).sum(1)+(VH*m.hm[None,:,None]).sum(1)
    L=(np.cross(X,V)*pm[None,:,None]).sum(1)+(np.cross(H,VH)*m.hm[None,:,None]).sum(1)
    ell=np.linalg.norm(H[:,m.housing_index]-X[:,m.anchor_index],axis=2)
    mounts=H-(X[:,m.edge[:,0]]+X[:,m.edge[:,1]])/2
    strain=np.linalg.norm(X[:,1:]-X[:,0,None,:],axis=2)/m.R-1
    edge=np.linalg.norm(X[:,m.edge[:,0]]-X[:,m.edge[:,1]],axis=2)-1
    row={'id':p['id'],'nu':nu,'alpha':alpha,'fine':fine,'initial_energy':E0,'housing_energy':Eh,
         'rtol':rtol,'atol':atol,'nfev':sol.nfev,'samples':len(t),
         'final_energy_fraction':float(E[-1]/E0),
         'relative_energy_plus_heat_error':float(max(abs(E+Y[:,-1]-E0))/E0),
         'initial_P_norm':float(np.linalg.norm(P[0])),'initial_L_norm':float(np.linalg.norm(L[0])),
         'P_drift':float(np.max(np.linalg.norm(P-P[0],axis=1))),
         'L_drift':float(np.max(np.linalg.norm(L-L[0],axis=1))),
         'minimum_sampled_strut_length':float(ell.min()),'minimum_sampled_oriented_volume_ratio':float(vol.min()),
         'maximum_sampled_oriented_volume_ratio':float(vol.max()),
         'maximum_sampled_mount_displacement':float(np.max(np.linalg.norm(mounts,axis=2))),
         'maximum_sampled_spoke_strain':float(np.max(abs(strain))),
         'maximum_sampled_edge_strain':float(np.max(abs(edge))),
         'mean_volume_rms':float(np.sqrt(np.trapezoid((vol.mean(1)-1)**2,t)/100)),
         'evidence':'NUMERICAL sampled trajectory; not verified integration or all-phase test'}
    if not alpha:
        assert row['minimum_sampled_strut_length']>987/2000
        assert row['minimum_sampled_oriented_volume_ratio']>39/40
        assert row['maximum_sampled_oriented_volume_ratio']<41/40
    else:
        early=t<=.05
        assert ell[early].min()>1/40
        assert vol[early].min()>.729 and vol[early].max()<1.331
        if p['baseline_id']=='nominal':
            _,b=m.collective(t,.1)
            base_rms=float(np.sqrt(np.trapezoid(((1+b)**3-1)**2,t)/100))
            row['baseline_origin']='nominal undamped/no-housing exact collective b(u); numerical trapezoid on 4001 points'
        else:
            base_rms=json.loads((SOURCE/'baselines.json').read_text())[p['baseline_id']]['mean_volume_rms']
            row['baseline_origin']='unchanged frozen nonlinear tolerance baseline'
        row['baseline_mean_volume_rms']=base_rms
        row['nonlinear_breathing_retention']=row['mean_volume_rms']/base_rms
    assert row['relative_energy_plus_heat_error']<2e-7
    assert max(row['P_drift'],row['L_drift'])<1e-10
    trace=[{'u':float(t[i]),'energy_fraction':float(E[i]/E0),'minimum_strut':float(ell[i].min()),
            'minimum_volume_ratio':float(vol[i].min()),'maximum_volume_ratio':float(vol[i].max()),
            'mean_volume_ratio':float(vol[i].mean())} for i in range(0,len(t),20)]
    return row,trace

def main(out):
    out.mkdir(parents=True,exist_ok=True);cases=json.loads((SOURCE/'cases.json').read_text());by={p['id']:p for p in cases}
    low='edge-p1-b0.005-cf0.0';high='uniform-b0.05-cf0.0';breath='seed10422-0-boundary2'
    vectors={nu:np.load(SOURCE/('vectors-low.npz' if nu==.04 else 'vectors-high.npz')) for nu in [.04,.05]}
    jobs=[];origins=[]
    for nu in [.04,.05]:
        full=np.load(SOURCE/f'full_housing_worst_phase-{nu}.npy')
        jobs.extend([(by[low],nu,vectors[nu][low],0.,False),(by[high],nu,full,0.,False)])
    for id,fine in [(breath,False),(high,False),(breath,True)]:
        phase=vectors[.05][id] if id==breath else np.load(SOURCE/'full_housing_worst_phase-0.05.npy')
        jobs.append((by[id],.05,phase,.1,fine))
    for p,nu,phase,alpha,fine in jobs:
        origins.append({'id':p['id'],'nu':nu,'alpha':alpha,'fine':fine,'phase_float64_sha256':hashlib.sha256(phase.tobytes()).hexdigest(),
                        'coefficient_sha256':p['coefficient_sha256'],'housing_energy_fraction_of_reference_pulse':'1/40000'})
    (out/'preparations.json').write_text(json.dumps(origins,indent=2)+'\n')
    records=[]
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(run,j) for j in jobs]
        for f in as_completed(futures):
            row,trace=f.result();records.append(row);print(json.dumps(row),flush=True)
            name=f"trace-{row['id']}-{row['nu']}-a{row['alpha']}-fine{int(row['fine'])}.csv"
            with (out/name).open('w',newline='') as stream:
                w=csv.DictWriter(stream,fieldnames=list(trace[0]),lineterminator='\n');w.writeheader();w.writerows(trace)
    records.sort(key=lambda r:(r['alpha'],r['id'],r['nu'],r['fine']))
    normal=next(r for r in records if r['id']==breath and not r['fine'])
    fine=next(r for r in records if r['id']==breath and r['fine'])
    refinement={k:abs(normal[k]-fine[k]) for k in ['nonlinear_breathing_retention','minimum_sampled_strut_length','mean_volume_rms']}
    assert max(refinement.values())<1e-6
    summary={'status':'CONSTRUCTOR_CHECKS_PASS','numpy':np.__version__,'scipy':scipy.__version__,
             'records':records,'refinement_changes':refinement,
             'scope':'Four housing-only exposed phases, two full-pulse phases, one tolerance refinement. Samples support implementation consistency; exact continuous-box all-phase claims come only from bounds.py and README proof.'}
    (out/'checks.json').write_text(json.dumps(summary,indent=2)+'\n');print('CHECKS_COMPLETE',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
