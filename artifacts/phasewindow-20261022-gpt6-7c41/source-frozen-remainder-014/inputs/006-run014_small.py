#!/usr/bin/env python3
"""Fixed archived source case: 8 prescribed directions, moving-tangent and finite remainder.
DEVELOPMENT / NUMERICAL; not an all-180-dimensional first-order singular-value calculation.
"""
import argparse, json, math, sys, time, csv
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P))
from source_case import FrozenMechanical,case,EXPECTED_SHA,SOURCE_COMMIT,SOURCE_BLOB,SOURCE_PATH
from nonaffine_audit import PROJ
from projected_tangent import MovingTangent,injection,projected_output
from finite_check import calc

def run(out,T=100.,n=401,nu=.05,rtol=2e-9,atol=3e-11,finite_rtol=3e-10,tangent_only=False):
    out.mkdir(exist_ok=True,parents=True)
    c=case();m=FrozenMechanical(nu=nu)
    y0,_=m.initial(phase='none'); L=MovingTangent(m)
    err=L.verify_jvp(y0[:560],b=3,eps=8e-7,seed=1929)
    assert err<4e-6,err
    Eh=(1+m.g.sum())*.01/2*1.5/40000;eps=np.sqrt(2*Eh)
    rng=np.random.default_rng(20261023)
    directions=[m.initial_gain_phase(Eh)]
    for _ in range(7):
        v=rng.normal(size=180);v/=np.linalg.norm(v);directions.append(v)
    A=np.column_stack(directions)
    assert np.max(abs(np.linalg.norm(A,axis=0)-1))<1e-12
    b=A.shape[1];I=injection(m)@A
    grid=np.linspace(0,T,n)
    init=np.r_[y0[:560],I.ravel()];now=time.perf_counter()
    sol=solve_ivp(lambda t,y:L.rhs(t,y,b),(0,T),init,t_eval=grid,method='DOP853',rtol=rtol,atol=atol)
    assert sol.success,sol.message
    baseline=[];predictions=[];tangents=[]
    for k,t in enumerate(grid):
        q=sol.y[:280,k]; W=sol.y[560:,k].reshape(560,b)
        z=(PROJ@q[4:40].reshape(12,3)).ravel()
        dw=eps*projected_output(W)
        baseline.append(z);tangents.append(dw)
        predictions.append(np.linalg.norm(z[:,None]+dw,axis=0))
    baseline=np.array(baseline);tangents=np.array(tangents);predictions=np.array(predictions)
    peak_indices=np.argmax(predictions,axis=0)
    response=[{'direction':j,'source':'initial-acceleration-SVD' if j==0 else f'frozen-rng-seed20261023-{j}', 'max_sampled_linearized_Z':float(predictions[peak_indices[j],j]),'at_u':float(grid[peak_indices[j]])} for j in range(b)]
    imax=np.unravel_index(np.argmax(predictions),predictions.shape)
    ph=A[:,imax[1]]
    # Immutable interim computation: save BEFORE expensive finite replay.
    np.savez_compressed(out/'tangent_cache.npz',grid=grid,directions=A,phase=ph,baseline=baseline,tangent=tangents[:,:,imax[1]],predictions=predictions,eps=eps,Eh=Eh)
    stage1={'status':'NUMERICAL_EIGHT_DIRECTIONS','source_case_id':c['id'],'source_coeff_sha256':EXPECTED_SHA,'nu':nu,'T':T,'samples':n,'jvp_error':float(err),'nfev':sol.nfev,'runtime_seconds':time.perf_counter()-now,'max_first_order_among_eight':float(predictions.max()),'peak_time':float(grid[imax[0]]),'peak_selected_direction':int(imax[1]),'max_baseline_Z':float(np.max(np.linalg.norm(baseline,axis=1))),'Eh':float(Eh)}
    (out/'stage1_summary.json').write_text(json.dumps(stage1,indent=2)+'\n')
    print('TANGENT_COMPLETE',json.dumps(stage1),flush=True)
    if tangent_only:return stage1
    # Actual nonlinear checks for phase selected from 8-dimensional directional set, both signs at full and half strength
    finite={};traces={}
    for amp,label in [(0.,'reference'),(1.,'positive'),(-1.,'negative'),(.5,'half_positive'),(-.5,'half_negative')]:
        trace,stats=calc(m,None if amp==0 else amp*ph,Eh,grid,finite_rtol)
        finite[label]=stats;traces[label]=trace
        print('FINITE',label,'Z',stats['max_Z'],'balance',stats['balance_error'],flush=True)
    zref=traces['reference'][:,2:38];zpos=traces['positive'][:,2:38];zneg=traces['negative'][:,2:38]
    zhp=traces['half_positive'][:,2:38];zhn=traces['half_negative'][:,2:38]
    direction_tangent=tangents[:,:,imax[1]]
    fn=lambda x:np.linalg.norm(x,axis=1)
    f1=fn(zpos-zref-direction_tangent);f2=fn(zneg-zref+direction_tangent)
    h1=fn(zhp-zref-.5*direction_tangent);h2=fn(zhn-zref+.5*direction_tangent)
    full=np.maximum(f1,f2);half=np.maximum(h1,h2)
    finite_drift=np.max(fn((zpos-zneg)/2-direction_tangent))
    report={'status':'SOURCE_MATCHED_FINITE_DEVELOPMENT','source_revision':SOURCE_COMMIT,'source_case_blob_sha1':SOURCE_BLOB,'source_case_id':c['id'],'source_coefficient_sha256':EXPECTED_SHA,
        'nu':nu,'beta':c['beta'],'cf':c['cf'],'E_h':Eh,'eps':eps,'initial_housing_phase_dimension':180,'tested_unit_phase_directions':b,
        'sample_count':n,'horizon':T,'directional_jvp_error':float(err),'tangent_nfev':sol.nfev,'tangent_runtime_seconds':time.perf_counter()-now,
        'directions':response,'largest_sampled_first_order_prediction_across_8_directions':float(predictions.max()),
        'selected_direction':int(imax[1]),'selected_sample_time':float(grid[imax[0]]),'selected_predicted_amplitude':float(predictions[imax]),
        'max_sampled_baseline_nonaffine':float(np.max(fn(baseline))),
        'finite':finite,'max_sampled_finite_selected_nonaffine':max(v['max_Z'] for v in finite.values()),
        'max_sampled_finite_Taylor_remainder_full_phase':float(max(full)),
        'max_sampled_finite_Taylor_remainder_half_phase':float(max(half)),
        'remainder_ratio_half_to_full':float(max(half)/max(full)),
        'max_sampled_selected_direction_odd_centered_tangent_error':float(finite_drift),
        'limitations':['Original full180-column source-matched calculation did not complete within tool timeout; not silently treated as verified.',
          'Only 8 prescribed initial-phase directions in linear moving-pulse calculation; not all180 gain.',
          'Finite nonlinear remainder measured for one post-selected direction at full/half energy; no uniform nonlinear Hessian remainder bound.',
          'Sampled times, unverified ODE truncation error; not interval integration or continuous-time bound.',
          'One frozen parameter case at nu=.05; no full tolerance box or full nonlinear u100 safety theorem.']}
    (out/'summary.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    np.save(out/'phase_directions_180x8.npy',A,allow_pickle=False)
    with (out/'directional_tangent.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['u','baseline_Z']+[f'dir{j}_firstorder_Z' for j in range(b)])
        for k,t in enumerate(grid):w.writerow([float(t),np.linalg.norm(baseline[k]),*predictions[k].tolist()])
    with (out/'selected_remainder_trace.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['u','baseline_Z','tangent_Z','positive_Z','negative_Z','half_positive_Z','half_negative_Z','full_pos_remainder','full_neg_remainder','half_pos_remainder','half_neg_remainder'])
        for i,t in enumerate(grid):w.writerow([t,np.linalg.norm(baseline[i]),np.linalg.norm(direction_tangent[i]),*[traces[key][i,1] for key in ['positive','negative','half_positive','half_negative']],f1[i],f2[i],h1[i],h2[i]])
    print('SUMMARY',json.dumps({k:report[k] for k in ['largest_sampled_first_order_prediction_across_8_directions','max_sampled_baseline_nonaffine','max_sampled_finite_selected_nonaffine','max_sampled_finite_Taylor_remainder_full_phase','max_sampled_finite_Taylor_remainder_half_phase','remainder_ratio_half_to_full']},indent=2),flush=True)
    return report
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--T',type=float,default=100);ap.add_argument('--samples',type=int,default=401);ap.add_argument('--nu',type=float,default=.05);ap.add_argument('--tangent-only',action='store_true')
    a=ap.parse_args();run(a.out,a.T,a.samples,a.nu,tangent_only=a.tangent_only)
