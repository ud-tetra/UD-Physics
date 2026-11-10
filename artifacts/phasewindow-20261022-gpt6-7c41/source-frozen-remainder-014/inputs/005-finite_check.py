#!/usr/bin/env python3
"""UD projected phase sensitivity: symmetric finite-difference validation of
post-selected worst initial housing phase from the full moving-pulse tangent.
Finite development checks only, not proof for the phase ball.
"""
import argparse,json,time,sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonaffine_audit import Mechanical,PROJ,R2
from projected_tangent import injection

def calc(m,phase,Eh,grid,tol):
    y0,_=m.initial(phase='none')
    if phase is not None:
        d=injection(m)@phase*np.sqrt(2*Eh)
        y0[:560]+=d
    initE=m.energy if hasattr(m,'energy') else None
    Q=y0[:280];v=y0[280:560];f,p,E0,*_=m.forces(Q,v,energy=True)
    sol=solve_ivp(m.rhs,(float(grid[0]),float(grid[-1])),y0,rtol=tol,atol=tol*.01,method='DOP853',t_eval=grid)
    assert sol.success,sol.message
    trace=[];P0=None;L0=None;pd=[];ld=[]
    for t,ystate in zip(sol.t,sol.y.T):
        q=ystate[:280];vel=ystate[280:560];fr,p,E,ls,rho,edges=m.forces(q,vel,energy=True)
        pts=q[1:40].reshape(13,3);H=q[190:280].reshape(30,3)
        vs=vel[1:40].reshape(13,3);vh=vel[190:280].reshape(30,3)
        Mass=m.m/R2
        P=(Mass[:,None]*vs).sum(0)+(m.mh[:,None]*vh).sum(0)
        L=np.cross(pts,Mass[:,None]*vs).sum(0)+np.cross(H,m.mh[:,None]*vh).sum(0)
        if P0 is None:P0=P;L0=L
        pd.append(np.linalg.norm(P-P0));ld.append(np.linalg.norm(L-L0))
        Z=(PROJ@pts[1:]).ravel()
        trace.append([float(t),float(np.linalg.norm(Z)),*Z.tolist(),float(ls.min()),float(E),float(ystate[-1])])
    t=np.array(trace)
    err=np.max(abs(t[:,-2]+t[:,-1]-E0))/E0
    return t,{'nfev':sol.nfev,'max_Z':float(max(t[:,1])),'max_Z_at_u':float(t[np.argmax(t[:,1]),0]),'min_strut':float(min(t[:,-3])),
            'balance_error':float(err),'P_drift':float(max(pd)),'L_drift':float(max(ld)),'initial_E':float(E0),'final_E':float(t[-1,-2])}

def main():
    p=argparse.ArgumentParser();p.add_argument('--in-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--T',type=float,default=100);p.add_argument('--samples',type=int,default=401);p.add_argument('--rtol',type=float,default=3e-10)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    r=json.loads((args.in_dir/'summary.json').read_text());phase=np.load(args.in_dir/'worst_phase_at_peak.npy',allow_pickle=False)
    assert phase.shape==(180,) and abs(np.linalg.norm(phase)-1)<1e-10
    m=Mechanical(nu=r['nu'],beta=r['beta'],cf=r['cf'],primary_pattern=r['pattern'])
    T=args.T;grid=np.linspace(0,T,args.samples);Eh=r['Eh']
    traces={};infos={}
    for key,ph in [('reference',None),('positive',phase),('negative',-phase)]:
        trace,info=calc(m,ph,Eh,grid,args.rtol)
        traces[key]=trace;infos[key]=info
        print('FINITE',key,info,flush=True)
    # Finite central-difference perturbation of the 36-d Z projected vector.
    base=traces['reference'][:,2:38]
    centered=(traces['positive'][:,2:38]-traces['negative'][:,2:38])/2
    tangent_value=np.linalg.norm(centered,axis=1)
    bound_time=float(r['at_u']);i=int(np.argmin(abs(grid-bound_time)))
    worst_expected=float(r['housing_first_order_allowance_at_peak'])
    observed=float(tangent_value[i])
    relerr=abs(observed-worst_expected)/worst_expected
    summary={'status':'NUMERICAL_FINITE_POSTSELECTION', 'source_tangent_summary':r,'initial_phase_norm':float(np.linalg.norm(phase)),
             'finite':infos,'at_peak_time_sampled':float(grid[i]),'tangent_gain_at_peak':worst_expected,
             'finite_centered_gain_at_peak':observed,'relative_first_order_vs_centered_difference':float(relerr),
             'max_centered_directional_Znorm':float(max(tangent_value)),
             'max_abs_primary_Znorm_of_any_test':float(max([v['max_Z'] for v in infos.values()])),
             'interpretation':'One post-selected phase and its negative; not an all-phase nonlinear bound nor independent model verification.'}
    # Save trace as CSV with z norms, central difference and energy/heat only, not all raw 36 vectors.
    with (args.out/'finite_trace.csv').open('w') as f:
        f.write('u,reference_Z,positive_Z,negative_Z,half_difference_Znorm,positive_heat,negative_heat\n')
        for j,tt in enumerate(grid):f.write(','.join(f'{value:.16g}' for value in [tt,traces['reference'][j,1],traces['positive'][j,1],traces['negative'][j,1],tangent_value[j],traces['positive'][j,-1],traces['negative'][j,-1]])+'\n')
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('COMPLETE',summary['relative_first_order_vs_centered_difference'],flush=True)
if __name__=='__main__':main()
