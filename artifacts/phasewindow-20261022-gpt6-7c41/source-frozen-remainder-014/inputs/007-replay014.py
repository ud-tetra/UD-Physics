#!/usr/bin/env python3
"""Complete finite nonlinear replay for one 8-subspace-selected phase, ± and ±half.
Each returned trajectory checkpoint is saved independently before continuing.
"""
from pathlib import Path
import argparse,json,csv,hashlib
import numpy as np
from source_case import FrozenMechanical,case,EXPECTED_SHA
from finite_check import calc

def main(inp,out,tol):
    out.mkdir(parents=True,exist_ok=True)
    vals=np.load(inp/'tangent_cache.npz',allow_pickle=False)
    grid=vals['grid'];phase=vals['phase'];base=vals['baseline'];tangent=vals['tangent'];Eh=float(vals['Eh']);P=vals['predictions']
    m=FrozenMechanical(nu=.05)
    assert case()['id']=='edge-p1-b0.005-cf0.0'
    result={'status':'NUMERICAL_SOURCE_MATCHED_FIVE_FINITE_DIRECTIONS', 'coefficient_sha256':EXPECTED_SHA,'phase_selection':'Maximum first-order projected norm over 8 frozen initial directions and 401 sampled times; not complete180-dimensional singular optimum', 'phase_direction_index':int(np.unravel_index(np.argmax(P),P.shape)[1]),'horizon':float(grid[-1]),'sample_count':len(grid),'Eh':Eh,'finite_rtol':tol,'finite':{}}
    traces={}
    for amp,label in [(0.,'reference'),(1.,'positive'),(-1.,'negative'),(.5,'half_positive'),(-.5,'half_negative')]:
        data,stats=calc(m,None if amp==0 else amp*phase,Eh,grid,tol)
        result['finite'][label]=stats
        traces[label]=data[:,2:38]
        np.savez_compressed(out/(label+'.npz'),grid=grid,Z=data[:,2:38],normZ=data[:,1],strut=data[:,-3],energy=data[:,-2],heat=data[:,-1])
        (out/'progress.json').write_text(json.dumps(result,indent=2)+'\n')
        print('FINITE',label,stats,flush=True)
    zr=traces['reference'];zp=traces['positive'];zn=traces['negative'];zhp=traces['half_positive'];zhn=traces['half_negative']
    f1=np.linalg.norm(zp-zr-tangent,axis=1);f2=np.linalg.norm(zn-zr+tangent,axis=1)
    h1=np.linalg.norm(zhp-zr-.5*tangent,axis=1);h2=np.linalg.norm(zhn-zr+.5*tangent,axis=1)
    full=np.maximum(f1,f2);half=np.maximum(h1,h2)
    result.update(max_selected_sampled_linearized_Z=float(P.max()),peak_time=float(grid[np.unravel_index(np.argmax(P),P.shape)[0]]),
                  maximum_observed_full_phase_remainder=float(full.max()),maximum_observed_half_phase_remainder=float(half.max()),
                  remainder_half_over_full=float(half.max()/full.max()),
                  max_odd_centered_difference_from_tangent=float(np.max(np.linalg.norm((zp-zn)/2-tangent,axis=1))),
                  max_even_difference_from_baseline=float(np.max(np.linalg.norm((zp+zn)/2-zr,axis=1))),
                  max_nonaffine_any_finite_phase=float(max(x['max_Z'] for x in result['finite'].values())),
                  min_sampled_strut=float(min(x['min_strut'] for x in result['finite'].values())),
                  max_energy_balance_error=float(max(x['balance_error'] for x in result['finite'].values())),
                  max_momentum_P_drift=float(max(x['P_drift'] for x in result['finite'].values())),
                  max_momentum_L_drift=float(max(x['L_drift'] for x in result['finite'].values())),
                  limits=['No nonlinear phase-ball uniformity: one postselected direction only.','No continuous-time validated integration error; 401 sampled instants.','Property case is source-matched but this case alone does not cover full parameter uncertainty box.','Original all-time nonlinear pulse orientation, strut safety, ringdown and breathing criteria OPEN.'])
    (out/'summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    with (out/'selected_remainder_trace.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['u','reference_Z','positive_Z','negative_Z','half_positive_Z','half_negative_Z','max_remainder_full','max_remainder_half'])
        for i,t in enumerate(grid):w.writerow([t,*[np.linalg.norm(x[i]) for x in [zr,zp,zn,zhp,zhn]],full[i],half[i]])
    print('DONE',json.dumps({k:result[k] for k in ['max_selected_sampled_linearized_Z','maximum_observed_full_phase_remainder','maximum_observed_half_phase_remainder','remainder_half_over_full','max_nonaffine_any_finite_phase','min_sampled_strut','max_energy_balance_error']},indent=2),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--rtol',type=float,default=2e-9);a=p.parse_args();main(a.input,a.out,a.rtol)
