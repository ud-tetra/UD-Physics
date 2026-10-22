"""Exact rigidity and finite unconstrained 3D breathing/imperfection campaign."""
from pathlib import Path
import argparse
import csv
import json
import math
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from model import Model,exact_rigidity


def integrate_scalar(y,t):return float(np.trapezoid(y,t))


def run_nonlinear(model,t,initial=None,rtol=1e-10,atol=1e-12):
    initial=model.initial if initial is None else initial
    solution=solve_ivp(model.ode,(0,float(t[-1])),initial,t_eval=t,method='DOP853',rtol=rtol,atol=atol)
    assert solution.success
    x=solution.y[:40].T;v=solution.y[40:].T
    E=np.array([model.energy_force(p)[0] for p in x])+np.sum(v*v*model.mass,axis=1)/2
    error=float(max(abs(E-E[0]))/E[0]);assert error<3e-8
    volumes=model.volumes(x);y=volumes-1;pd=y-y.mean(axis=1,keepdims=True)
    signal=integrate_scalar(np.sum(y*y,axis=1),t)
    leakage=math.sqrt(integrate_scalar(np.sum(pd*pd,axis=1),t)/signal)
    rms=math.sqrt(integrate_scalar(y.mean(axis=1)**2,t)/(t[-1]-t[0]))
    point=x[:,1:].reshape(-1,13,3);velocity=v[:,1:].reshape(-1,13,3);m=model.m/model.R2
    shell_centre=point[:,1:].mean(axis=1)
    recentered=x.copy();recentered[:,1:4]=shell_centre
    shell_volumes=model.volumes(recentered);ys=shell_volumes-1;ps=ys-ys.mean(axis=1,keepdims=True)
    shell_leakage=math.sqrt(integrate_scalar(np.sum(ps*ps,axis=1),t)/integrate_scalar(np.sum(ys*ys,axis=1),t))
    centre_invariance=float(np.max(abs(shell_volumes.sum(axis=1)-volumes.sum(axis=1))))
    assert centre_invariance<3e-13
    centred=point[:,1:]-shell_centre[:,None,:]
    covariance=np.einsum('ni,tnj->tij',model.ref[1:],centred)
    u,sv,vh=np.linalg.svd(covariance)
    proper=np.linalg.det(u@vh)
    u[:,:,-1]*=proper[:,None];sv[:,-1]*=proper
    rotation=u@vh;scale=sv.sum(axis=1)/np.sum(model.ref[1:]**2)
    fitted=np.einsum('ni,tij->tnj',model.ref[1:],rotation)*scale[:,None,None]
    shell_error=np.linalg.norm(centred-fitted,axis=(1,2))/np.linalg.norm(model.ref[1:])
    hub=np.linalg.norm(point[:,0]-shell_centre,axis=1)/model.R
    P=np.sum(velocity*m[None,:,None],axis=1)
    L=np.sum(np.cross(point,velocity)*m[None,:,None],axis=1)
    geom=model.geometry_checks(x)
    assert geom['minimum_oriented_cell_volume_ratio']>0 and geom['maximum_support_halfspace_violation_sampled']<2e-10
    info={'volume_signal_leakage':leakage,'mean_volume_rms':rms,'relative_energy_error':error,
          'shell_centroid_volume_signal_leakage':shell_leakage,
          'maximum_shell_shape_error_after_rigid_scale_fit':float(max(shell_error)),
          'rms_hub_offset_over_R':math.sqrt(integrate_scalar(hub*hub,t)/(t[-1]-t[0])),
          'total_volume_centre_invariance_error':centre_invariance,
          'linear_momentum_drift':float(np.max(np.linalg.norm(P-P[0],axis=1))),
          'angular_momentum_drift':float(np.max(np.linalg.norm(L-L[0],axis=1))),**geom}
    return x,v,info


def variational(model,out):
    Q,N=model.transverse_basis();H0=Q.T@model.H0@Q
    eigen,V=np.linalg.eigh(H0)
    assert eigen[0]>0
    S=(V*np.sqrt(eigen))@V.T;invS=(V*(1/np.sqrt(eigen)))@V.T
    Tr=Q.T@model.Tr@Q;Te=Q.T@model.Te@Q;n=len(eigen)
    assert n==32
    times=np.array([20.,50.,100.,200.,400.])
    def ode(time,state):
        alpha,b=model.collective(time)
        H=H0+(2*b-alpha)/(1+b)*Tr+b/(1+b)*Te
        phi=state.reshape(2,n,2*n)
        return np.stack([S@phi[1],-(H@invS)@phi[0]]).ravel()
    sol=solve_ivp(ode,(0,400),np.eye(2*n).ravel(),t_eval=times,method='DOP853',rtol=2e-10,atol=2e-12)
    assert sol.success
    form=np.block([[np.zeros_like(invS),invS],[-invS,np.zeros_like(invS)]])
    records=[]
    for t,state in zip(times,sol.y.T):
        phi=state.reshape(2*n,2*n);u,s,vh=np.linalg.svd(phi)
        residual=float(np.linalg.norm(phi.T@form@phi-form)/np.linalg.norm(form))
        assert residual<2e-6
        records.append({'u':float(t),'maximum_reference_energy_amplitude_gain':float(s[0]),
                        'minimum_gain':float(s[-1]),'symplectic_relative_residual':residual})
    # Freeze a target-informed perturbation from the exposed u=100 propagator.
    phi100=sol.y[:,2].reshape(64,64);_,_,vh=np.linalg.svd(phi100);seed=vh[0]
    dx=Q@invS@seed[:32]/model.rootmass
    dv=Q@seed[32:]/model.rootmass
    return {'transverse_coordinates':32,'phase_coordinates':64,'metric':'equilibrium transverse energy norm, after removing2 collective and6 rigid coordinates',
            'records':records,'equilibrium_minimum_squared_shape_frequency':float(eigen[0]),
            'adversarial_selection':'leading right singular vector of exposed u100 propagator; design probe,not held-out prediction',
            'seed_dx':dx.tolist(),'seed_dv':dv.tolist()},dx,dv


def remove_momentum(model,state):
    state=state.copy();points=state[1:40].reshape(13,3);vel=state[41:].reshape(13,3)
    m=model.m/model.R2
    centre=(points*m[:,None]).sum(axis=0)/m.sum();r=points-centre
    vel-=(vel*m[:,None]).sum(axis=0)/m.sum()
    angular=np.sum(np.cross(r,vel)*m[:,None],axis=0)
    inertia=sum(m[i]*(np.dot(v,v)*np.eye(3)-np.outer(v,v)) for i,v in enumerate(r))
    omega=np.linalg.solve(inertia,angular);vel-=np.cross(np.tile(omega,(13,1)),r)
    state[41:]=vel.ravel();return state


def main(out):
    out.mkdir(parents=True,exist_ok=True);model=Model()
    exact=exact_rigidity(model);print('exact rigidity PASS',flush=True)
    Q,N=model.transverse_basis()
    full=np.linalg.eigvalsh(model.H0);assert sum(abs(full)<1e-10)==6 and full[6]>0
    # Hessian check at equilibrium against independently differentiated forces.
    rng=np.random.default_rng(9023);d=rng.normal(size=40);d/=np.linalg.norm(d)
    eps=1e-6;x0=model.initial[:40].copy();x0[0]=0
    fp=model.energy_force(x0+eps*d)[1];fm=model.energy_force(x0-eps*d)[1]
    numerical=(fp-fm)/(2*eps)
    K=model.H0*model.rootmass[:,None]*model.rootmass[None,:]
    hessian_error=float(max(abs(numerical-K@d)));assert hessian_error<2e-9
    phases=np.linspace(0,100,2001);minimum=1e9;leak=0.
    for time in phases:
        a,b=model.collective(time);H=model.H0+(2*b-a)/(1+b)*model.Tr+b/(1+b)*model.Te
        minimum=min(minimum,float(np.linalg.eigvalsh(Q.T@H@Q)[0]))
        leak=max(leak,float(np.linalg.norm(N.T@H@Q)))
    assert leak<1e-12
    # A conservative all-phase lower comparison (numerical here; exact certificate below).
    lower=model.H0-(8/59)*model.Tr-(1/59)*model.Te
    lower_gap=float(np.linalg.eigvalsh(Q.T@lower@Q)[0])
    print('shape lower gap',lower_gap,'sampled minimum',minimum,flush=True)
    var,dx,dv=variational(model,out);print('variational',var['records'],flush=True)
    (out/'variational.json').write_text(json.dumps(var,indent=2)+'\n')
    t=np.linspace(0,100,2001)
    x,v,base=run_nonlinear(model,t)
    a,b=model.collective(t);pred=np.repeat(model.ref[None,:,:],len(t),axis=0);pred[:,1:]*=(1+b[:,None,None])
    analytic_error=float(max(np.max(abs(x[:,0]-a)),np.max(abs(x[:,1:].reshape(-1,13,3)-pred))))
    assert analytic_error<5e-9
    rows=[];curve=np.column_stack([t,(1+b)**3,x[:,0],model.volumes(x).mean(axis=1)]);models={}
    for amplitude in [1e-6,1e-5,1e-4]:
        initial=model.initial+amplitude*np.r_[dx,dv];initial=remove_momentum(model,initial)
        xx,vv,info=run_nonlinear(model,t,initial)
        row={'campaign':'adversarial_initial_shape','epsilon':amplitude,'sample':0,**info,
             'mean_volume_rms_retention':info['mean_volume_rms']/base['mean_volume_rms']}
        rows.append(row);print('probe',amplitude,info['volume_signal_leakage'],flush=True)
    #16 seeded property probes; no continuous-box or statistical confidence claim.
    rng=np.random.default_rng(9023)
    for epsilon in [.01,.05]:
        for i in range(8):
            m=1+epsilon*rng.uniform(-1,1,13);g=1+epsilon*rng.uniform(-1,1,12);k=.4*(1+epsilon*rng.uniform(-1,1,30))
            imperfect=Model(g=g,m=m,k=k);xx,vv,info=run_nonlinear(imperfect,t)
            row={'campaign':'seeded_material_properties','epsilon':epsilon,'sample':i,**info,
                 'mean_volume_rms_retention':info['mean_volume_rms']/base['mean_volume_rms']}
            rows.append(row)
            models[(epsilon,i)]=imperfect
            if i==7:print('properties',epsilon,'complete',flush=True)
    refinements=[]
    for epsilon in [.01,.05]:
        w=max((r for r in rows if r['campaign']=='seeded_material_properties' and r['epsilon']==epsilon),key=lambda z:z['volume_signal_leakage'])
        fine=np.linspace(0,100,4001)
        _,_,info=run_nonlinear(models[(epsilon,w['sample'])],fine,rtol=2e-12,atol=2e-14)
        delta=abs(info['volume_signal_leakage']-w['volume_signal_leakage'])
        assert delta<2e-6
        refinements.append({'epsilon':epsilon,'sample':w['sample'],'coarse_leakage':w['volume_signal_leakage'],
                            'fine_leakage':info['volume_signal_leakage'],'difference':delta,
                            'fine_energy_relative_error':info['relative_energy_error']})
    summary={'status':'PASS','exact_rigidity':exact,'configuration':'free centre C plus12 spatial outer points and one scalar internal actuator alpha;40 coordinates/80 phase variables',
             'equilibrium':{'zero_modes':6,'positive_modes':34,'minimum_positive_squared_frequency':float(full[6]),
                            'hessian_force_difference_error':hessian_error,'eigenvalues_numerical':full.tolist()},
             'breathing':{'collective_squared_frequencies':['8-sqrt37','8+sqrt37'],'initial_alpha':.1,
                          'full80state_vs_analytic_error':analytic_error,'baseline_checks':base,
                          'sampled_transverse_minimum_squared_stiffness':minimum,
                          'conservative_transverse_lower_gap_numerical':lower_gap,
                          'collective_rigid_to_shape_leakage_norm':leak},
             'variational':var,'campaign':rows,'worst_probe_refinements':refinements,
             'numerics':{'numpy':np.__version__,'scipy':scipy.__version__,'dtype':'float64','method':'DOP853',
                         'nonlinear_window':[0,100],'nonlinear_samples':2001,'nonlinear_rtol':1e-10,'nonlinear_atol':1e-12,
                         'variational_window':[0,400],'variational_rtol':2e-10,'variational_atol':2e-12,
                         'property_seed':9023,'property_samples_per_tolerance':8},
             'limits':['Exact orbital equilibrium stability is separate from finite-amplitude breathing stability.',
                       'Positive instantaneous transverse stiffness does not preclude parametric instability.',
                       'Variational propagation and nonlinear imperfection probes are finite-window,constructor work.',
                       'All physical scales,material realization and native constitutive selection remain open.']}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with (out/'campaign.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    np.savetxt(out/'baseline.csv',curve,delimiter=',',header='u,analytic_volume_ratio,full3d_alpha,full3d_volume_ratio',comments='')
    print(json.dumps({k:v for k,v in summary.items() if k not in ['variational','campaign']},indent=2),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
