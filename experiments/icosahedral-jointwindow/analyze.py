"""Deterministic strength coverage plus finite nonlinear housing-seeded budget."""
from pathlib import Path
import argparse,json,csv,copy,hashlib,time
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from linear import evaluate,model,system,mean_row,baseline_rms,parent,ROOT,T

LOW=.04;HIGH=.05;OUT=None
SOURCE=ROOT/'artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files'
PHYSICS=['primary','ratio_error','beta','cf','omega_h','housing_weights']
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def csvout(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def cases():
    old=[p for p in json.loads((SOURCE/'probes.json').read_text()) if p['group']!='challenge'];assert len(old)==20
    result=copy.deepcopy(old)
    for p in old:
        q=copy.deepcopy(p);q.update(id=p['id']+'-cf0',group='paired_cf0',cf=0.);result.append(q)
    for j,p in enumerate([old[1],old[6],old[11]]):
        for beta in [.005,.05]:
            for cf in [0.,.001]:
                q=copy.deepcopy(p);q.update(id=f'edge-p{j}-b{beta}-cf{cf}',group='added_boundary',beta=beta,cf=cf);result.append(q)
    nominal={'primary':{'m':[1.]*13,'g':[1.]*12,'k':[.4]*30},'ratio_error':[0.]*150,'omega_h':10.,'housing_weights':[1.]*30,'baseline_id':'nominal'}
    for beta in [.005,.05]:
        for cf in [0.,.001]:result.append({**copy.deepcopy(nominal),'id':f'uniform-b{beta}-cf{cf}','group':'uniform','beta':beta,'cf':cf})
    assert len(result)==56
    seen={}
    for p in result:
        key=hashlib.sha256(json.dumps({k:p[k] for k in PHYSICS},sort_keys=True,separators=(',',':')).encode()).hexdigest()
        p['coefficient_sha256']=key;p['canonical_id']=seen.setdefault(key,p['id'])
    extra=[{**copy.deepcopy(nominal),'id':f'limit-b{b}','group':'outside_lower_mass','beta':b,'cf':0.} for b in [.0005,.00005]]
    return result,extra

def linear_worker(item):
    p,nu=item;start=time.perf_counter();row,vec=evaluate(p,nu,vector=nu in [LOW,HIGH]);row['elapsed_seconds']=time.perf_counter()-start;return p['id'],row,vec

def union_intervals(intervals):
    result=[]
    for a,b in sorted(intervals):
        a=max(a,LOW);b=min(b,HIGH)
        if a>b:continue
        if result and a<=result[-1][1]+1e-13:result[-1][1]=max(b,result[-1][1])
        else:result.append([a,b])
    return result

def gaps(covered):
    result=[];left=LOW
    for a,b in covered:
        if a>left+1e-12:result.append([left,a])
        left=max(left,b)
    if left<HIGH-1e-12:result.append([left,HIGH])
    return result

def nonlinear(case,nu,phase,t,rtol=1e-10,atol=1e-12,alpha=.1,energy_factor=1.):
    m=model(case,nu);Ep=(1+m.g.sum())*.01/2;Eh=Ep/40000*energy_factor;scale=np.sqrt(2*Eh)
    initial=m.initial_augmented(alpha);initial[190:280]+=scale*phase[:90];initial[470:560]+=scale*phase[90:]
    assert abs(m.energy(initial)-((1+m.g.sum())*alpha*alpha/2+Eh))<2e-12
    sol=solve_ivp(m.ode,(0,T),initial,t_eval=t,method='DOP853',rtol=rtol,atol=atol);assert sol.success
    Y=sol.y.T;E=np.array([m.energy(y) for y in Y]);err=float(max(abs(E+Y[:,-1]-E[0]))/E[0]);assert err<1e-7
    H=Y[:,190:280].reshape(-1,30,3);HV=Y[:,470:560].reshape(-1,30,3)
    X=Y[:,1:40].reshape(-1,13,3);V=Y[:,281:320].reshape(-1,13,3);pm=m.m/m.R2
    P=(V*pm[None,:,None]).sum(1)+(HV*m.hm[None,:,None]).sum(1)
    L=(np.cross(X,V)*pm[None,:,None]).sum(1)+(np.cross(H,HV)*m.hm[None,:,None]).sum(1)
    dP=float(np.max(np.linalg.norm(P-P[0],axis=1)));dL=float(np.max(np.linalg.norm(L-L[0],axis=1)))
    assert dP<3e-11 and dL<3e-11
    info={'energy_balance_error':err,'total_P_drift':dP,'total_L_drift':dL,'initial_total_P_norm':float(np.linalg.norm(P[0])),
          'initial_total_L_norm':float(np.linalg.norm(L[0])),'housing_energy':float(Eh),'housing_energy_over_reference_pulse':float(Eh/Ep),
          'final_total_energy_fraction':float(E[-1]/E[0]),'maximum_housing_perturbation_initial':float(np.max(np.linalg.norm((scale*phase[:90]).reshape(30,3),axis=1)))}
    if alpha:
        measured=parent.readouts.metrics(m,t,Y[:,:40],Y[:,280:320]);measured['primary_linear_momentum_exchange']=measured.pop('linear_momentum_drift');measured['primary_angular_momentum_exchange']=measured.pop('angular_momentum_drift')
        info.update(parent.extra_metrics(m,Y,measured))
    return Y,info,E

def pulse_worker(item):
    case,nu,phase,base=item;_,info,_=nonlinear(case,nu,phase,np.linspace(0,T,2001))
    ret=info['mean_volume_rms']/base['mean_volume_rms'];shape=info['shell_shape_rms']/base['shell_shape_rms']
    row={'id':case['id'],'nu':nu,'beta':case['beta'],'cf':case['cf'],**info,'breathing_retention':ret,'shape_rms_ratio':shape,
         'passes_screen':bool(ret>=.8 and info['volume_signal_leakage']<=.05 and shape<=.5)}
    return case['id'],nu,row

def verify_integral(case,nu,row):
    m=model(case,nu);M,Q,k,D,A,B,raw,G=system(m);n=len(k);xp=np.zeros(2*n);q=np.zeros(280);q[0]=.1;xp[:n]=Q.T@(np.sqrt(M)*q)
    l=np.r_[mean_row(m)/np.sqrt(M)@Q,np.zeros(n)]
    def ode(t,y):
        v=y[n:2*n];return np.r_[A@y[:2*n],(l@y[:2*n])**2,(D@v)@(D@v)]
    sol=solve_ivp(ode,(0,T),np.r_[xp,0.,0.],method='DOP853',rtol=2e-11,atol=2e-13);assert sol.success
    rms=float(np.sqrt(sol.y[-2,-1]/T));Id=float(sol.y[-1,-1]);a=abs(rms-row['linear_pulse_rms']);b=abs(Id-row['trajectory_sensitivity_integral'])
    assert a<3e-8 and b<3e-7
    return {'id':case['id'],'nu':nu,'ODE_rms':rms,'rms_change':a,'ODE_sensitivity_integral':Id,'sensitivity_change':b}

def main(out):
    out.mkdir(parents=True,exist_ok=True);probes,extra=cases();dump(out/'cases.json',probes);dump(out/'limit_cases.json',extra)
    unique=[p for p in probes if p['id']==p['canonical_id']];lookup={p['id']:p for p in unique};by_id={p['id']:p for p in probes}
    nodes={};records=[];vectors={LOW:{},HIGH:{}};coverage=[];next_nodes=[LOW,HIGH,(LOW+HIGH)/2]
    with ProcessPoolExecutor(max_workers=2) as pool:
        while next_nodes:
            nu=next_nodes.pop(0);rows=[]
            futures={pool.submit(linear_worker,(p,nu)):p['id'] for p in unique}
            for f in as_completed(futures):
                id,row,vec=f.result();rows.append(row);records.append(row)
                if vec is not None:vectors[nu][id]=vec
            radius=min(r['joint_radius'] for r in rows);worst=max(rows,key=lambda r:r['worst_housing_energy_fraction']);low=min(rows,key=lambda r:r['all_phase_linear_retention_lower'])
            node={'nu':nu,'joint_radius':radius,'worst_housing_energy':worst['worst_housing_energy_fraction'],'worst_housing_id':worst['id'],
                  'minimum_all_phase_linear_retention':low['all_phase_linear_retention_lower'],'minimum_retention_id':low['id'],'all_nodes_pass':all(r['passes_node'] for r in rows)}
            nodes[nu]=node
            if radius>0:coverage.append([nu-radius,nu+radius])
            covered=union_intervals(coverage);missing=gaps(covered)
            print('NODE',node,'coverage',covered,flush=True);csvout(out/'linear.csv',sorted(records,key=lambda r:(r['nu'],r['id'])))
            dump(out/'coverage.json',{'status':'COVERED_NUMERICALLY' if not missing else 'OPEN','nodes':list(nodes.values()),'covered_intervals':covered,'uncovered_intervals':missing,
                                     'parameter_case_records':len(probes),'unique_parameter_sets':len(unique),'numerical_allowances':'explicit cushions; not verified interval arithmetic or continuous-parameter-box certificate'})
            if next_nodes:continue
            if not missing or len(nodes)>=17 or not node['all_nodes_pass']:break
            a,b=sorted(missing,key=lambda x:(-(x[1]-x[0]),x[0]))[0];mid=(a+b)/2
            assert all(abs(mid-u)>1e-12 for u in nodes);next_nodes=[mid]
    for nu,name in [(LOW,'low'),(HIGH,'high')]:np.savez_compressed(out/f'vectors-{name}.npz',**vectors[nu])
    # Additional smaller-mass limits cannot select or retune the interval.
    limit=[]
    for p in extra:
        for nu in [LOW,HIGH]:row,_=evaluate(p,nu);limit.append(row)
    dump(out/'limits.json',limit)
    verification=[]
    for p in [by_id['uniform-b0.005-cf0.0'],unique[0]]:
        row=next(r for r in records if r['id']==p['canonical_id'] and r['nu']==LOW);verification.append(verify_integral(p,LOW,row))
    dump(out/'integral_checks.json',verification)
    # Both endpoint strengths,32 specified records each,exact coefficient duplicates reused.
    pulse_cases=probes[:20]+probes[40:52];pulse_unique=list({p['canonical_id']:lookup[p['canonical_id']] for p in pulse_cases}.values())
    base=json.loads((SOURCE/'baselines.json').read_text());(out/'baselines.json').write_bytes((SOURCE/'baselines.json').read_bytes())
    measured={}
    with ProcessPoolExecutor(max_workers=2) as pool:
        jobs=[(p,nu,vectors[nu][p['id']],base[p['baseline_id']]) for nu in [LOW,HIGH] for p in pulse_unique]
        futures={pool.submit(pulse_worker,job):(job[0]['id'],job[1]) for job in jobs}
        for f in as_completed(futures):
            id,nu,row=f.result();measured[(id,nu)]=row;print('PULSE',id,nu,row['breathing_retention'],row['passes_screen'],flush=True)
    pulses=[]
    for nu in [LOW,HIGH]:
        for p in pulse_cases:
            row=measured[(p['canonical_id'],nu)].copy();row.update(id=p['id'],canonical_id=p['canonical_id'],group=p['group']);pulses.append(row)
    csvout(out/'pulses.csv',pulses)
    ring=[]
    for nu in [LOW,HIGH]:
        w=max([r for r in records if r['nu']==nu],key=lambda r:r['worst_housing_energy_fraction']);p=lookup[w['id']]
        for factor in [1.,.25]:
            Y,info,E=nonlinear(p,nu,vectors[nu][p['id']],np.linspace(0,T,2001),2e-12,1e-15,alpha=0.,energy_factor=factor)
            row={'id':p['id'],'nu':nu,'energy_factor':factor,'linear_energy_fraction':w['worst_housing_energy_fraction'],**info,
                 'nonlinear_vs_linear_energy_change':abs(info['final_total_energy_fraction']-w['worst_housing_energy_fraction'])}
            ring.append(row);csvout(out/f'ringdown-{nu}-{factor}.csv',[{'u':float(t),'energy_fraction':float(e/E[0]),'heat_fraction':float(h/E[0])} for t,e,h in zip(np.linspace(0,T,2001),E,Y[:,-1])])
    dump(out/'ringdowns.json',ring)
    worst=max(pulses,key=lambda r:r['volume_signal_leakage']);low=min(pulses,key=lambda r:r['breathing_retention']);refinements=[]
    for id,nu in dict.fromkeys([(worst['canonical_id'],worst['nu']),(low['canonical_id'],low['nu'])]):
        p=lookup[id];_,info,_=nonlinear(p,nu,vectors[nu][id],np.linspace(0,T,4001),2e-12,2e-14)
        row=measured[(id,nu)];ret=info['mean_volume_rms']/base[p['baseline_id']]['mean_volume_rms'];dr=abs(ret-row['breathing_retention']);dl=abs(info['volume_signal_leakage']-row['volume_signal_leakage'])
        assert dr<4e-6 and dl<4e-6
        refinements.append({'id':id,'nu':nu,'retention_change':dr,'mismatch_change':dl,'fine_retention':ret,'fine':info})
    cov=json.loads((out/'coverage.json').read_text());node_rows=list(nodes.values())
    # Strength covering inequalities yield conservative finite-case bounds on the entire interval.
    segments=[]
    endpoints=sorted({LOW,HIGH,*[max(LOW,u-r['joint_radius']) for u,r in nodes.items() if r['joint_radius']>0],*[min(HIGH,u+r['joint_radius']) for u,r in nodes.items() if r['joint_radius']>0]})
    for a,b in zip(endpoints,endpoints[1:]):
        centers=[r for r in node_rows if r['joint_radius']>0 and r['nu']-r['joint_radius']<=a+1e-12 and r['nu']+r['joint_radius']>=b-1e-12]
        if centers:segments.append({'lower':a,'upper':b,'covering_centers':[r['nu'] for r in centers]})
    dump(out/'coverage_segments.json',segments)
    summary={'status':'FINITE_CASE_WINDOW_PASS' if cov['status']=='COVERED_NUMERICALLY' and all(p['passes_screen'] for p in pulses) else 'OPEN_OR_FAILED',
             'numpy':np.__version__,'scipy':scipy.__version__,'strength_interval':[LOW,HIGH],'candidate_case_records':len(probes),'unique_parameter_sets':len(unique),
             'strength_nodes':len(nodes),'unique_full_linear_evaluations':len(records),'coverage':cov,'minimum_node_all_phase_linear_retention':min(r['all_phase_linear_retention_lower'] for r in records),
             'maximum_node_housing_energy':max(r['worst_housing_energy_fraction'] for r in records),'nonlinear_pulse_records':len(pulses),'distinct_nonlinear_pulse_trajectories':len(measured),
             'nonlinear_screen_passes':sum(r['passes_screen'] for r in pulses),'minimum_nonlinear_breathing_retention':min(r['breathing_retention'] for r in pulses),
             'maximum_nonlinear_hub_mismatch':max(r['volume_signal_leakage'] for r in pulses),'shape_rms_ratio_range':[min(r['shape_rms_ratio'] for r in pulses),max(r['shape_rms_ratio'] for r in pulses)],
             'maximum_pulse_energy_error':max(r['energy_balance_error'] for r in pulses),'maximum_total_P_drift':max(r['total_P_drift'] for r in pulses),'maximum_total_L_drift':max(r['total_L_drift'] for r in pulses),
             'minimum_sampled_strut_length':min(r['minimum_sampled_housing_strut_length'] for r in pulses),'minimum_sampled_oriented_cell_volume':min(r['minimum_oriented_cell_volume_ratio'] for r in pulses),
             'maximum_lyapunov_relative_residual':max(max(r['lyapunov_relative_residual'],r['sensitivity_lyapunov_relative_residual']) for r in records),
             'integral_checks':verification,'limits':limit,'ringdowns':ring,'refinements':refinements,
             'scope':'Analytic exact compliance/phase/strength inequalities. Numerical continuous-strength enclosure over finite parameter cases with disclosed cushions; no verified interval arithmetic or continuous uncertainty-box/nonlinear all-phase certificate. Physical tests UNSCORED.'}
    dump(out/'summary.json',summary);print('FINAL',json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
