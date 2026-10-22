"""Disclosed post-campaign extension from54 dark modes to all90 housing modes."""
from pathlib import Path
import argparse,json,csv,importlib.util
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
from scipy.linalg import expm,eigh
from linear import model,system,parent,T
spec=importlib.util.spec_from_file_location('jointwindow_campaign',Path(__file__).with_name('analyze.py'))
campaign=importlib.util.module_from_spec(spec);spec.loader.exec_module(campaign)
LOW,HIGH=campaign.LOW,campaign.HIGH
union_intervals,gaps,nonlinear,csvout,dump=campaign.union_intervals,campaign.gaps,campaign.nonlinear,campaign.csvout,campaign.dump

def evaluate_full(item):
    p,nu=item;m=model(p,nu);M,Q,k,D,A,_,_,G=system(m);n=len(k)
    U=np.zeros((280,90));U[190:]=np.eye(90);Uq=Q.T@U;Z=np.zeros_like(Uq)
    B=np.block([[Uq/m.omega_h,Z],[Z,Uq]])
    # Global rigid velocities carry real kinetic energy. They do not decay and
    # must be added back after quotienting the nonrigid propagator.
    _,rigid=parent.reduced_basis(m,M);R,_=np.linalg.qr(rigid);Rh=R[190:]
    conserved=np.zeros((180,180));conserved[90:,90:]=Rh@Rh.T
    assert np.max(abs(B.T@G@B+conserved-np.eye(180)))<3e-12
    F=expm(T*A);FB=F@B;gram=FB.T@G@FB+conserved;values,V=eigh((gram+gram.T)/2)
    rho=float(values[-1]);ld=float(eigh(D,eigvals_only=True)[-1])*(1+1e-9);radius=(np.sqrt(.5)-np.sqrt(rho)-1e-6)/(T*ld)
    assert rho<=1+3e-9
    phase=None
    if nu in [LOW,HIGH]:
        s=np.repeat(np.sqrt(m.hm),3);phase=np.r_[V[:90,-1]/(m.omega_h*s),V[90:,-1]/s]
    return {'id':p['id'],'nu':nu,'worst_full_housing_energy_fraction':rho,'strength_generator_norm':ld,'ringdown_radius':float(radius),
            'max_rigid_velocity_energy_fraction':float(eigh(conserved[90:,90:],eigvals_only=True)[-1]),'passes_node':bool(rho<=.5)},phase

def main(out):
    allcases=json.loads((out/'cases.json').read_text());cases=[p for p in allcases if p['id']==p['canonical_id']];lookup={p['id']:p for p in cases}
    old=json.loads((out/'coverage.json').read_text());queue=sorted(r['nu'] for r in old['nodes']);records=[];nodes=[];intervals=[];vectors={LOW:{},HIGH:{}}
    with ProcessPoolExecutor(max_workers=2) as pool:
        while queue:
            nu=queue.pop(0);rows=[]
            for r,phase in pool.map(evaluate_full,[(p,nu) for p in cases]):
                rows.append(r);records.append(r)
                if phase is not None:vectors[nu][r['id']]=phase
            radius=min(r['ringdown_radius'] for r in rows);w=max(rows,key=lambda r:r['worst_full_housing_energy_fraction'])
            nodes.append({'nu':nu,'radius':radius,'worst_energy':w['worst_full_housing_energy_fraction'],'worst_id':w['id']})
            if radius>0:intervals.append([nu-radius,nu+radius])
            covered=union_intervals(intervals);missing=gaps(covered);print('FULL_NODE',nodes[-1],covered,flush=True)
            csvout(out/'full_housing_linear.csv',sorted(records,key=lambda r:(r['nu'],r['id'])))
            if queue:continue
            if not missing or len(nodes)>=17 or not all(r['passes_node'] for r in rows):break
            a,b=sorted(missing,key=lambda x:(-(x[1]-x[0]),x[0]))[0];queue=[(a+b)/2]
    ring=[]
    for nu in [LOW,HIGH]:
        w=max((r for r in records if r['nu']==nu),key=lambda r:r['worst_full_housing_energy_fraction']);p=lookup[w['id']]
        phase=vectors[nu][p['id']];np.save(out/f'full_housing_worst_phase-{nu}.npy',phase,allow_pickle=False)
        Y,info,E=nonlinear(p,nu,phase,np.linspace(0,T,2001),2e-12,1e-15,alpha=0.)
        ring.append({'id':p['id'],'nu':nu,'linear_energy_fraction':w['worst_full_housing_energy_fraction'],**info,
                     'nonlinear_vs_linear_change':abs(info['final_total_energy_fraction']-w['worst_full_housing_energy_fraction'])})
        csvout(out/f'full-housing-ringdown-{nu}.csv',[{'u':float(t),'energy_fraction':float(e/E[0]),'heat_fraction':float(h/E[0])} for t,e,h in zip(np.linspace(0,T,2001),E,Y[:,-1])])
    report={'status':'COVERED_NUMERICALLY' if not missing else 'OPEN_OR_FAILED','exposure':'post-campaign scope extension;no retuning;not independent validation',
            'initial_housing_coordinates':90,'initial_phase_dimension':180,'rigid_kinetic_energy':'retained in energy Gram; no zero-momentum assumption',
            'parameter_sets':len(cases),'nodes':nodes,'matrix_evaluations':len(records),'covered_intervals':covered,'uncovered_intervals':missing,'ringdowns':ring,
            'scope':'numerical continuous-strength full-housing enclosure for finite parameter family;two nonlinear full-housing phases only;no continuous uncertainty-box/nonlinear all-phase theorem'}
    dump(out/'full_housing_summary.json',report);print('FULL_FINAL',json.dumps(report,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
