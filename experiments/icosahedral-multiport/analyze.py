"""Full auxiliary-mode design and nonlinear probes; see PROTOCOL.md."""
from pathlib import Path
from itertools import product
import argparse,csv,importlib.util,json,math,sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import eigvals
from network import Network
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-damping'))
spec=importlib.util.spec_from_file_location('multiport_readouts',ROOT/'experiments/icosahedral-damping/analyze.py')
readouts=importlib.util.module_from_spec(spec);spec.loader.exec_module(readouts)


def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def csvout(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)


def linear_scan(out):
    rows=[];selected=None
    for mu,kappa,gamma in product([.002,.02,.2],[.1,.5,2.],[.02,.1,.5]):
        model=Network(mu=mu,kappa=kappa,gamma=gamma);K,C,D=model.normal_matrices();n=len(K)
        # All150 auxiliary coordinates retained,including unforced cycle modes.
        A=np.block([[np.zeros((n,n)),np.eye(n)],[-K,-C]])
        poles=eigvals(A);rate=float(-max(poles.real));assert rate>1e-8
        row={'mu':mu,'kappa':kappa,'gamma':gamma,'minimum_decay_rate':rate,
             'maximum_pole_modulus':float(max(abs(poles))),'transverse_configuration_dimension':n,'transverse_phase_dimension':2*n}
        rows.append(row)
        if selected is None or rate>selected['minimum_decay_rate']:selected=row
    csvout(out/'linear-scan.csv',rows);dump(out/'selection.json',selected)
    print('selected',selected,flush=True);return {k:selected[k] for k in ['mu','kappa','gamma']},selected


def check_forces(model):
    rng=np.random.default_rng(1520);x=model.initial[:40].copy();x[1:]+=rng.normal(size=39)*.003
    z=rng.normal(size=150)*.002;v=rng.normal(size=40)*.03;w=rng.normal(size=150)*.03
    f,error,U=model.port_force(x,z);D=model.rows(x);direct=model.weight*model.kappa*D.T@error
    force_error=float(max(abs(f-direct)));gradient=[];eps=1e-6
    direction=rng.normal(size=40);direction/=np.linalg.norm(direction)
    fd=(model.port_force(x+eps*direction,z)[2]-model.port_force(x-eps*direction,z)[2])/(2*eps)
    grad_error=float(abs(fd-f@direction))
    # Spring rate = force input power - force output power; viscous loss positive.
    energy_rate=float(f@v-model.weight*model.kappa*error@w)
    independent=float(model.weight*model.kappa*error@(D@v-w))
    power_error=abs(energy_rate-independent)
    # Geometric reactions remain central: net force/torque vanish at arbitrary geometry.
    point=x[1:].reshape(13,3);pf=f[1:].reshape(13,3)
    P=float(np.linalg.norm(pf.sum(axis=0)));L=float(np.linalg.norm(np.cross(point,pf).sum(axis=0)))
    assert force_error<2e-15 and grad_error<1e-9 and power_error<1e-15 and P<1e-15 and L<1e-15
    return {'force_jacobian_error':force_error,'directional_energy_gradient_error':grad_error,'power_identity_error':power_error,
            'net_port_force_error':P,'net_port_torque_error':L}


def run(model,A0,t,refine=False):
    initial=model.initial_augmented(A0)
    sol=solve_ivp(model.ode,(0,float(t[-1])),initial,t_eval=t,method='DOP853',rtol=2e-12 if refine else 1e-10,atol=2e-14 if refine else 1e-12)
    assert sol.success;Y=sol.y.T;x=Y[:,:40];v=Y[:,model.n:model.n+40]
    E=np.array([model.energy(y) for y in Y]);loss=Y[:,-1];err=float(max(abs(E+loss-E[0]))/E[0])
    assert err<4e-8 and min(np.diff(loss))>-1e-10
    measured=readouts.metrics(model,t,x,v)
    return x,v,{'balance_relative_error':err,'remaining_total_energy_fraction':float(E[-1]/E[0]),
                'maximum_auxiliary_displacement':float(np.max(abs(Y[:,40:model.n]))),**measured}


def main(out):
    out.mkdir(parents=True,exist_ok=True);parameters,selected=linear_scan(out);model=Network(**parameters)
    checks=check_forces(model);t=np.linspace(0,100,2001);symmetric=[]
    for A0 in [.025,.1,.2]:
        x,v,info=run(model,A0,t);alpha,b=model.collective(t,A0)
        pred=np.repeat(model.ref[None,:,:],len(t),axis=0);pred[:,1:]*=(1+b[:,None,None])
        error=float(max(np.max(abs(x[:,0]-alpha)),np.max(abs(x[:,1:].reshape(-1,13,3)-pred))))
        assert error<5e-9 and info['maximum_auxiliary_displacement']<1e-10
        symmetric.append({'amplitude':A0,'full_vs_parent_analytic_error':error,**info})
    print('symmetric checks PASS',flush=True)
    property_source=ROOT/'artifacts/icosahedral-damping-20261022-a1/damping-001/files/properties.json'
    properties=json.loads(property_source.read_text())
    old=list(csv.DictReader((ROOT/'artifacts/icosahedral-damping-20261022-a1/damping-001/files/campaign.csv').open()))
    rows=[];worst=None
    for A0 in [.025,.1,.2]:
        for prop in properties:
            name=prop['id'];kw={k:prop[k] for k in ['m','g','k']};mod=Network(**parameters,**kw)
            x,v,info=run(mod,A0,t)
            matched=next(r for r in old if r['property_id']==name and float(r['amplitude'])==A0 and float(r['cs'])==float(r['ce'])==0.)
            retention=info['mean_volume_rms']/float(matched['mean_volume_rms'])
            shape=info['shell_shape_rms']/float(matched['shell_shape_rms']);hub=info['hub_offset_rms_over_R']/float(matched['hub_offset_rms_over_R'])
            row={'amplitude':A0,'property_id':name,**info,'mean_volume_rms_retention':retention,'shape_rms_ratio':shape,'hub_offset_rms_ratio':hub,
                 'passes_80pct_5pct_50pct_screen':bool(retention>=.8 and info['volume_signal_leakage']<=.05 and shape<=.5)}
            rows.append(row)
            if worst is None or info['volume_signal_leakage']>worst[0]:worst=(info['volume_signal_leakage'],A0,name,kw,info)
            print('nonlinear',A0,name,retention,info['volume_signal_leakage'],shape,flush=True)
    csvout(out/'campaign.csv',rows)
    # Keep complete property bytes as a declared captured input rather than regenerate them.
    dump(out/'properties.json',properties)
    rng=np.random.default_rng(713);direction=rng.uniform(-1,1,150);dump(out/'ratio-direction.json',direction.tolist());ratio=[]
    alpha,b=model.collective(t,.1);analytic_rms=readouts.rms((1+b)**3-1,t)
    for epsilon in [.001,.01]:
        mod=Network(**parameters,ratio_error=epsilon*direction);x,v,info=run(mod,.1,t)
        ratio.append({'maximum_ratio_error':epsilon,**info,'mean_volume_rms_retention':info['mean_volume_rms']/analytic_rms})
    _,A0,name,kw,coarse=worst;_,_,fine=run(Network(**parameters,**kw),A0,np.linspace(0,100,4001),True)
    refinement={'amplitude':A0,'property_id':name,'coarse':coarse,'fine':fine,
                'volume_leakage_change':abs(fine['volume_signal_leakage']-coarse['volume_signal_leakage'])}
    assert refinement['volume_leakage_change']<3e-6
    result={'status':'PASS','numpy':np.__version__,'scipy':scipy.__version__,'selected':selected,'linear_grid_points':27,
            'coordinates':{'primary':40,'auxiliary':150,'total':190,'phase':380,'dissipation_bookkeeping':1},
            'energy_identity':'Eprime=-(gamma/10)*sum zdot²;E includes all150 finite auxiliary masses and springs',
            'force_checks':checks,'symmetric_checks':symmetric,'campaign_points':9,
            'screen_pass_count':sum(r['passes_80pct_5pct_50pct_screen'] for r in rows),
            'minimum_mean_volume_rms_retention':min(r['mean_volume_rms_retention'] for r in rows),
            'maximum_hub_volume_leakage':max(r['volume_signal_leakage'] for r in rows),
            'maximum_shell_centroid_volume_leakage':max(r['shell_centroid_volume_signal_leakage'] for r in rows),
            'shape_rms_ratio_range':[min(r['shape_rms_ratio'] for r in rows),max(r['shape_rms_ratio'] for r in rows)],
            'maximum_hub_offset_rms_ratio':max(r['hub_offset_rms_ratio'] for r in rows),
            'maximum_balance_relative_error':max(r['balance_relative_error'] for r in rows+symmetric+ratio),
            'minimum_sampled_cell_volume_ratio':min(r['minimum_oriented_cell_volume_ratio'] for r in rows+symmetric+ratio),
            'maximum_P_drift':max(r['linear_momentum_drift'] for r in rows+symmetric+ratio),
            'maximum_L_drift':max(r['angular_momentum_drift'] for r in rows+symmetric+ratio),
            'ratio_error_checks':ratio,'refinement':refinement,
            'limits':['Ideal reciprocal differential transmissions are assumed;manufactured mechanism,housing/routing masses and parasitic common loss untested',
                      'Exact local transverse equilibrium decay does not prove global/finite-amplitude attraction',
                      '9exposed finite development points do not certify a continuous tolerance box',
                      'Selected grid maximizes equilibrium spectral decay,not nonlinear readout;no held-out/physical prediction',
                      'Transmission ratio errors break exact common cancellation even when reciprocal and passive']}
    dump(out/'summary.json',result);print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
