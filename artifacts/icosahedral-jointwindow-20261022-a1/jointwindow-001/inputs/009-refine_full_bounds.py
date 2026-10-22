"""Strengthen the exposed full-housing enclosure with a dissipation inequality."""
from pathlib import Path
import argparse,csv,json
import numpy as np
from envelope import extreme

LOW=.04;HIGH=.05
def main(out):
    rows=list(csv.DictReader((out/'full_housing_linear.csv').open()));raw=json.loads((out/'full_housing_summary.json').read_text())
    result=[];radii={}
    for id in dict.fromkeys(r['id'] for r in rows):
        group=sorted([r for r in rows if r['id']==id],key=lambda r:float(r['nu']));nodes=[float(r['nu']) for r in group]
        values=[np.sqrt(float(r['worst_full_housing_energy_fraction']))+1e-6 for r in group]
        slopes=[min(100*float(r['strength_generator_norm']),np.sqrt(100*float(r['strength_generator_norm'])/(2*float(r['nu'])))) for r in group]
        for nu,value,L in zip(nodes,values,slopes):radii[nu]=min(radii.get(nu,np.inf),(np.sqrt(.5)-value)/L)
        h,at=extreme(nodes,values,slopes,True,True)
        result.append({'id':id,'continuous_strength_full_housing_energy_upper':h*h,'upper_at_nu':at})
    intervals=[]
    for nu,r in sorted(radii.items()):
        a=max(LOW,nu-r);b=min(HIGH,nu+r)
        if a>b:continue
        if intervals and a<=intervals[-1][1]+1e-13:intervals[-1][1]=max(b,intervals[-1][1])
        else:intervals.append([a,b])
    worst=max(result,key=lambda r:r['continuous_strength_full_housing_energy_upper'])
    old=json.loads((out/'envelopes.json').read_text());lower=old['minimum_all_phase_linear_retention_lower']['continuous_strength_all_phase_linear_retention_lower']
    covered=intervals==[[LOW,HIGH]]
    report={'status':'FULL_HOUSING_WINDOW_PASS' if covered and worst['continuous_strength_full_housing_energy_upper']<=.5 and lower>=.8 else 'OPEN_OR_FAILED',
            'exposure':'sharper analytic bound derived after observing coarse full-housing coverage gaps;no parameters,thresholds or trajectories changed',
            'raw_scope_audit_status':raw['status'],'strength_interval':[LOW,HIGH],'initial_housing_coordinates':90,'initial_phase_dimension':180,
            'parameter_sets':raw['parameter_sets'],'strength_nodes':len(raw['nodes']),'full_housing_matrix_evaluations':raw['matrix_evaluations'],
            'covered_intervals':intervals,'maximum_full_housing_energy_upper':worst,'minimum_all_phase_linear_breathing_lower':lower,
            'sharper_operator_lipschitz':'min(T*lambda_D,sqrt(T*lambda_D/(2*nu0))); unit energy-norm initial phase has E0=1/2 and nu0 integral(v^T Dv)<=1/2',
            'scope':'numeric continuous-strength enclosure over50 finite parameter sets,all180 initial housing phases,total energy includes conserved rigid kinetic part;not verified interval arithmetic or nonlinear/full-parameter-box certificate',
            'per_case':result}
    (out/'full_housing_refined.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='per_case'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
