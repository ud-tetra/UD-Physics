"""Full180-column tangent flow along a nonlinear pulse, without state quotient."""
import argparse,json,csv,time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import scipy
from scipy.integrate import DOP853
from scipy.optimize import brentq
from scipy.linalg import eigh,norm as stable_norm
from jacobian import Linearization,model,ROOT
SOURCE=ROOT/'artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files'
IDS=['seed10422-0-boundary2','uniform-b0.05-cf0.0']

def volume_rows(m,y,W):
    X=y[1:40].reshape(13,3);Q=W[1:40].reshape(13,3,-1)
    a,b,c=[X[m.face[:,i]]-X[0] for i in range(3)]
    da,db,dc=[Q[m.face[:,i]]-Q[0] for i in range(3)]
    factor=m.sign/(6*m.vcell)
    dV=factor[:,None]*(np.einsum('fi,fip->fp',np.cross(b,c),da)+np.einsum('fi,fip->fp',np.cross(c,a),db)+np.einsum('fi,fip->fp',np.cross(a,b),dc))
    vol=factor*np.einsum('fi,fi->f',a,np.cross(b,c))
    return vol,dV

def momenta(L,y,W):
    p=y[:280][L.spatial];v=y[280:560][L.spatial];mass=L.M[L.spatial[:,0]]
    dp=W[:280][L.spatial].transpose(0,2,1);dv=W[280:][L.spatial].transpose(0,2,1)
    P=(mass[:,None,None]*dv).sum(0).T
    angular=np.cross(dp,v[:,None,:])+np.cross(p[:,None,:],dv)
    return P,(mass[:,None,None]*angular).sum(0).T

def minimize_rms(Q,c,base2,epsilon):
    lam,U=eigh((Q+Q.T)/2);assert lam[0]>-1e-10
    lam=np.maximum(lam,0.);z=U.T@c
    def phase(mult):return -epsilon*z/(epsilon*epsilon*lam+mult)
    hi=epsilon*np.linalg.norm(c)
    # This pulse cross-term requires the energy-ball boundary. If a future
    # case does not, use a pseudoinverse and check its residual explicitly.
    smallest=np.finfo(float).tiny
    if stable_norm(phase(smallest))<=1:
        mult=0.;a=U@phase(smallest)
    else:
        mult=brentq(lambda t:stable_norm(phase(t))-1,smallest,hi,xtol=1e-22,rtol=1e-13)
        a=U@phase(mult)
    stationarity=float(np.linalg.norm(epsilon*epsilon*Q@a+epsilon*c+mult*a))
    assert np.linalg.norm(a)<=1+1e-9 and stationarity<1e-11
    minimum=base2+2*epsilon*c@a+epsilon*epsilon*(a@Q@a)
    return float(np.sqrt(max(0.,minimum))),a,{'multiplier':float(mult),'phase_norm':float(np.linalg.norm(a)),'stationarity_residual':stationarity,'minimum_gram_eigenvalue':float(lam[0])}

def run(case,fine,out,objective=False):
    start=time.perf_counter();m=model(case,.05);L=Linearization(m);B=L.injection();y0=m.initial_augmented(.1)
    epsilon=np.sqrt(2*((1+m.g.sum())*.01/2/40000))
    rtol,atol=(5e-10,5e-12) if fine else (2e-9,2e-11);step=.05 if fine else .1
    times=np.linspace(0,100,round(100/step)+1);initial=np.r_[y0,B.ravel()]
    abs_error=np.r_[np.full(561,atol/100),np.full(B.size,atol)]
    def rhs(t,z):
        y=z[:561];W=z[561:].reshape(560,180)
        return np.r_[m.ode(t,y),L.apply(y,W).ravel()]
    solver=DOP853(rhs,0.,initial,100.,rtol=rtol,atol=abs_error)
    reference=[];hrows=[];rows=[];index=0;P0,L0=momenta(L,y0,B);maxP=maxL=0.
    max_primary=max_shape=max_mean_gradient=0.;min_cell_singular=float('inf');max_volume=0.;max_gradient_rigid=0.
    def sample(t,z):
        nonlocal maxP,maxL,max_primary,max_shape,max_mean_gradient,min_cell_singular,max_volume,max_gradient_rigid
        y=z[:561];W=z[561:].reshape(560,180);vol,dV=volume_rows(m,y,W)
        p=y[:280][L.spatial];d=p[L.i[42:]]-p[L.j[42:]];ell=np.linalg.norm(d,axis=1);n=d/ell[:,None]
        dW=W[:280][L.spatial];difference=dW[L.i[42:]]-dW[L.j[42:]]
        ellrow=np.einsum('fi,fip->fp',n,difference)
        rownorm=np.linalg.norm(ellrow,axis=1)
        spatialGram=np.einsum('fip,fjp->fij',difference,difference)
        vector_norm=np.sqrt(np.maximum(0.,np.linalg.eigvalsh(spatialGram)[:,-1]))
        P,angular=momenta(L,y,W);maxP=max(maxP,float(np.max(abs(P-P0))));maxL=max(maxL,float(np.max(abs(angular-L0))))
        # Additional diagnostics for the predeclared fine run. These do not
        # change the tangent ODE, trust-region phase, energy or thresholds.
        if fine:
            WP=W[1:40];primary=np.sqrt(max(0.,eigh(WP@WP.T,eigvals_only=True,subset_by_index=[38,38])[0]))
            max_primary=max(max_primary,float(primary))
            _,physical_gradient=volume_rows(m,y,np.eye(40));max_mean_gradient=max(max_mean_gradient,float(np.linalg.norm(physical_gradient.mean(0))))
            X=y[1:40].reshape(13,3);A=np.stack([X[m.face[:,j]]-X[0] for j in range(3)],axis=2)
            if objective:
                centered=X-X.mean(0);columns=[]
                for axis in np.eye(3):columns.append(np.tile(axis,13))
                for axis in np.eye(3):columns.append(np.cross(axis,centered).ravel())
                rigid=np.linalg.qr(np.column_stack(columns))[0]
                shape=WP-rigid@(rigid.T@WP)
                gain=np.sqrt(max(0.,eigh(shape@shape.T,eigvals_only=True,subset_by_index=[38,38])[0]))
                max_shape=max(max_shape,float(gain))
                max_gradient_rigid=max(max_gradient_rigid,float(np.max(abs(physical_gradient.mean(0)[1:40]@rigid))))
            min_cell_singular=min(min_cell_singular,float(np.linalg.svd(A,compute_uv=False)[:,-1].min()))
            max_volume=max(max_volume,float(np.max(abs(vol))))
        reference.append(y.copy());hrows.append(dV.mean(0));rows.append({'u':float(t),'base_mean_volume_signal':float(vol.mean()-1),
          'minimum_reference_strut_length':float(ell.min()),'maximum_initial_phase_strut_length_derivative_norm':float(rownorm.max()),
          'minimum_first_order_strut_length':float(np.min(ell-epsilon*rownorm)),
          'minimum_linearized_vector_distance_margin':float(np.min(ell-epsilon*vector_norm)),
          'minimum_reference_volume_ratio':float(vol.min()),'maximum_reference_volume_ratio':float(vol.max()),
          'minimum_first_order_cell_volume':float(np.min(vol-epsilon*np.linalg.norm(dV,axis=1))),
          'maximum_first_order_cell_volume':float(np.max(vol+epsilon*np.linalg.norm(dV,axis=1)))})
    sample(0.,initial);index=1
    while solver.status=='running':
        old=solver.t;solver.step();assert solver.status!='failed';dense=solver.dense_output()
        while index<len(times) and times[index]<=solver.t+1e-12:
            sample(times[index],dense(times[index]));index+=1
        if int(solver.t/10)>int(old/10):print('PROGRESS',case['id'],fine,round(solver.t,3),solver.nfev,flush=True)
    assert index==len(times);Y=np.array(reference);H=np.array(hrows);signal=np.array([r['base_mean_volume_signal'] for r in rows])
    weights=np.full(len(times),step/100);weights[[0,-1]]/=2
    Q=H.T@(weights[:,None]*H);c=H.T@(weights*signal);base2=float(signal@(weights*signal))
    rms,phase,trust=minimize_rms(Q,c,base2,epsilon)
    if case['baseline_id']=='nominal':
        _,b=m.collective(times,.1);baseline=float(np.sqrt(((1+b)**3-1)@(weights*((1+b)**3-1))))
        baseline_origin='exact nominal original undamped/no-housing collective solution, separate trapezoid'
    else:
        baseline=json.loads((SOURCE/'baselines.json').read_text())[case['baseline_id']]['mean_volume_rms'];baseline_origin='frozen original nonlinear baseline'
    max_differential_rms=float(epsilon*np.sqrt(eigh(Q,eigvals_only=True)[-1]))
    Wfinal=solver.y[561:].reshape(560,180);E=np.array([m.energy(y) for y in Y]);balance=float(np.max(abs(E+Y[:,-1]-E[0]))/E[0])
    assert balance<1e-8 and max(maxP,maxL)<2e-8
    stem=f"response-{case['id']}-"+('objective1' if objective else f'fine{int(fine)}')
    np.savez_compressed(out/(stem+'.npz'),u=times,reference=Y,mean_volume_derivative=H,volume_gram=Q,volume_cross=c,
                        adverse_phase=phase,initial_injection=B,final_tangent=Wfinal)
    with (out/(stem+'.csv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    result={'id':case['id'],'fine':fine,'nu':.05,'beta':case['beta'],'cf':case['cf'],'samples':len(times),'rtol':rtol,'atol_tangent':atol,'atol_reference':atol/100,
      'housing_energy':float(epsilon*epsilon/2),'housing_phase_coordinates':180,'elapsed_seconds':time.perf_counter()-start,'nfev':solver.nfev,
      'reference_mean_volume_rms':float(np.sqrt(base2)),'baseline_mean_volume_rms':baseline,'baseline_origin':baseline_origin,
      'reference_breathing_retention':float(np.sqrt(base2)/baseline),'maximum_first_order_volume_rms_perturbation':max_differential_rms,
      'triangle_first_order_retention_lower':float((np.sqrt(base2)-max_differential_rms)/baseline),
      'trust_region_first_order_minimum_rms':rms,'trust_region_first_order_retention_lower':rms/baseline,'trust_region':trust,
      'minimum_sampled_first_order_strut_length':min(r['minimum_first_order_strut_length'] for r in rows),
      'minimum_sampled_vector_distance_margin':min(r['minimum_linearized_vector_distance_margin'] for r in rows),
      'minimum_sampled_first_order_cell_volume':min(r['minimum_first_order_cell_volume'] for r in rows),
      'maximum_sampled_first_order_cell_volume':max(r['maximum_first_order_cell_volume'] for r in rows),
      'reference_energy_plus_heat_relative_error':balance,'tangent_P_invariance_error':maxP,'tangent_L_invariance_error':maxL,
      'evidence':'NUMERICAL first derivative of nonlinear flow, all180 initial housing tangent coordinates; sampled time/quadrature; no finite-energy-ball certificate'}
    if fine:
        linear_primary=epsilon*max_primary
        def remainder(r):
            z=2*(linear_primary+r)/min_cell_singular
            return max_mean_gradient*r+max_volume*(3*z*z+z*z*z)
        margin=rms-.8*baseline
        admissible=brentq(lambda r:remainder(r)-margin,0.,.1,xtol=1e-15) if remainder(0)<margin else 0.
        result['sampled_readout_remainder_budget']={
            'maximum_primary_position_derivative_operator_norm':max_primary,
            'linear_primary_position_radius':float(linear_primary),
            'minimum_reference_cell_singular_value':min_cell_singular,
            'maximum_reference_abs_cell_volume_ratio':max_volume,
            'maximum_mean_volume_gradient_norm':max_mean_gradient,
            'first_order_rms_margin_above_80percent':float(margin),
            'hypothetical_primary_flow_remainder_allowance':float(admissible),
            'meaning':'Numerical design requirement using sampled derivative/geometry maxima; NOT a certified nonlinear remainder bound.'}
        if objective:
            shape_radius=epsilon*max_shape
            def shape_remainder(r):
                z=2*(shape_radius+r)/min_cell_singular
                return max_mean_gradient*r+max_volume*(3*z*z+z*z*z)
            allowance=brentq(lambda r:shape_remainder(r)-margin,0.,.1,xtol=1e-15) if shape_remainder(0)<margin else 0.
            result['objective_readout_diagnostic']={
                'maximum_shape_position_derivative_operator_norm':max_shape,'linear_shape_position_radius':float(shape_radius),
                'maximum_mean_gradient_rigid_annihilation_error':max_gradient_rigid,
                'hypothetical_aligned_flow_remainder_allowance':float(allowance),
                'meaning':'Instantaneous rigid projection is the derivative of a proper Procrustes alignment chart. Readout diagnostic only; full560-state dynamics/energy unchanged. Nonlinear alignment-chart and Green/defect remainder bounds are still required.'}
    (out/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n');print('RESULT',json.dumps(result),flush=True);return result

def main(out,which):
    out.mkdir(parents=True,exist_ok=True);cases=json.loads((SOURCE/'cases.json').read_text());by={p['id']:p for p in cases}
    jobs=[(by[id],False,out) for id in IDS] if which=='normal' else [(by[IDS[0]],True,out,which=='objective')]
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(run,*job) for job in jobs]
        records=[f.result() for f in as_completed(futures)]
    (out/f'variational-{which}.json').write_text(json.dumps({'status':'DIFFERENTIAL_ANALYSIS_COMPLETE_NONLINEAR_TUBE_OPEN','numpy':np.__version__,'scipy':scipy.__version__,'records':records},indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);p.add_argument('--which',choices=['normal','fine','objective'],default='normal');a=p.parse_args();main(a.out,a.which)
