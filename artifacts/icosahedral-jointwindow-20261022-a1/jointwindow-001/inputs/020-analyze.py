"""Model-scoped passive damping tradeoff; see PROTOCOL.md before interpretation."""
from pathlib import Path
from fractions import Fraction as F
import argparse,csv,json,math
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from damping import Damped,ico


def dump(path,data):path.write_text(json.dumps(data,indent=2)+'\n')
def csvout(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def integral(y,t):return float(np.trapezoid(y,t))
def rms(y,t):return math.sqrt(integral(y*y,t)/(t[-1]-t[0]))


def exact_soft(model):
    Q=ico.Q5;z=Q(0);one=Q(1);R2=ico.dot(model.vertices[1],model.vertices[1]);lam=Q(F(1,4),F(1,20))
    # Physical-coordinate matrices, avoiding square roots in mass normalization.
    Bs=[];Be=[]
    for i in range(1,13):
        r=[z]*40
        for a in range(3):r[1+3*i+a]=model.vertices[i][a]/R2;r[1+a]=-model.vertices[i][a]/R2
        Bs.append(r)
    for i,j in model.edges:
        r=[z]*40;v=ico.sub(model.vertices[i],model.vertices[j])
        for a in range(3):r[1+3*i+a]=v[a];r[1+3*j+a]=-v[a]
        Be.append(r)
    alpha=[one]+[z]*39;Bg=[]
    for r in Bs:
        v=r.copy();v[0]=-one;Bg.append(v)
    K=[[z]*40 for _ in range(40)]
    for r,w in [(alpha,one)]+[(r,one) for r in Bs+Bg]+[(r,Q(F(2,5))) for r in Be]:
        nz=[i for i,x in enumerate(r) if x!=z]
        for i in nz:
            for j in nz:K[i][j]+=w*r[i]*r[j]
    mass=[one]+[one/R2]*39
    A=[[K[i][j]-(lam*mass[i] if i==j else z) for j in range(40)] for i in range(40)]
    def rank(rows):
        a=[r.copy() for r in rows];p=0
        for j in range(40):
            ix=next((i for i in range(p,len(a)) if a[i][j]!=z),None)
            if ix is None:continue
            a[p],a[ix]=a[ix],a[p];d=a[p][j];a[p]=[x/d for x in a[p]]
            for i in range(p+1,len(a)):
                d=a[i][j]
                if d!=z:a[i]=[x-d*y for x,y in zip(a[i],a[p])]
            p+=1
            if p==len(a):break
        return p
    base=rank(A);aug=rank(A+Bs+[alpha]);assert base==aug==35
    assert lam/Q(F(2,5))==R2
    Kfloat=np.array([[float(x) for x in row] for row in K]);M=np.array(list(map(float,mass)))
    assert np.max(abs(Kfloat/np.sqrt(M[:,None]*M[None,:])-model.H0))<3e-14
    return {'status':'PASS','field':'Q(sqrt5)','lambda_soft':'(5+sqrt5)/20','R2':'(5+sqrt5)/8',
            'rank_K_minus_lambda_M':base,'rank_after_radial_and_alpha_rows':aug,'soft_eigenspace_dimension':5,
            'conclusion':'Entire soft eigenspace has alpha=0 and Bs*x=0; Be^T Be*x=R2*M*x. Hence zddot+ce*R2*zdot+lambda_soft*z=0 exactly at equilibrium, independent of cs.',
            'underdamped_modal_envelope':'exp(-ce*R2*u/2); valid ce < 2*sqrt(lambda_soft)/R2',
            'matrix_float_crosscheck_maxerror':float(np.max(abs(Kfloat/np.sqrt(M[:,None]*M[None,:])-model.H0)))}


def metrics(model,t,x,v):
    volumes=model.volumes(x);y=volumes-1;p=y-y.mean(axis=1,keepdims=True)
    signal=integral(np.sum(y*y,axis=1),t)
    points=x[:,1:].reshape(-1,13,3);vel=v[:,1:].reshape(-1,13,3);centre=points[:,1:].mean(axis=1)
    rec=x.copy();rec[:,1:4]=centre;ys=model.volumes(rec)-1;ps=ys-ys.mean(axis=1,keepdims=True)
    centred=points[:,1:]-centre[:,None,:];cov=np.einsum('ni,tnj->tij',model.ref[1:],centred)
    U,sv,Vh=np.linalg.svd(cov);proper=np.linalg.det(U@Vh);U[:,:,-1]*=proper[:,None];sv[:,-1]*=proper
    fitted=np.einsum('ni,tij->tnj',model.ref[1:],U@Vh)*(sv.sum(axis=1)/np.sum(model.ref[1:]**2))[:,None,None]
    shape=np.linalg.norm(centred-fitted,axis=(1,2))/np.linalg.norm(model.ref[1:])
    hub=np.linalg.norm(points[:,0]-centre,axis=1)/model.R;mass=model.m/model.R2
    P=np.sum(vel*mass[None,:,None],axis=1);L=np.sum(np.cross(points,vel)*mass[None,:,None],axis=1)
    geom=model.geometry_checks(x)
    assert geom['minimum_oriented_cell_volume_ratio']>0 and geom['maximum_support_halfspace_violation_sampled']<2e-10
    return {'volume_signal_leakage':math.sqrt(integral(np.sum(p*p,axis=1),t)/signal),
            'shell_centroid_volume_signal_leakage':math.sqrt(integral(np.sum(ps*ps,axis=1),t)/integral(np.sum(ys*ys,axis=1),t)),
            'mean_volume_rms':rms(y.mean(axis=1),t),'shell_shape_rms':rms(shape,t),'hub_offset_rms_over_R':rms(hub,t),
            'linear_momentum_drift':float(np.max(np.linalg.norm(P-P[0],axis=1))),
            'angular_momentum_drift':float(np.max(np.linalg.norm(L-L[0],axis=1))),**geom}


def run(model,A0,t,refine=False):
    initial=np.r_[model.initial,0.];initial[0]=A0
    sol=solve_ivp(model.ode_loss,(0,float(t[-1])),initial,t_eval=t,method='DOP853',rtol=2e-12 if refine else 1e-10,atol=2e-14 if refine else 1e-12)
    assert sol.success;x=sol.y[:40].T;v=sol.y[40:80].T;loss=sol.y[80]
    E=np.array([model.energy_force(a)[0] for a in x])+np.sum(v*v*model.mass,axis=1)/2
    err=float(np.max(abs(E+loss-E[0]))/E[0]);assert err<4e-8 and min(np.diff(loss))>-1e-10
    return x,v,{'balance_relative_error':err,'remaining_energy_fraction':float(E[-1]/E[0]),**metrics(model,t,x,v)}


def main(out):
    out.mkdir(parents=True,exist_ok=True);model=Damped();exact=exact_soft(model);dump(out/'exact-soft.json',exact)
    print('exact soft tangential eigenspace PASS',flush=True)
    # A second force implementation (strain Jacobian) checks signs, power and central reactions.
    rng=np.random.default_rng(1004);x=model.initial[:40].copy();x[1:]+=rng.normal(size=39)*.002;v=rng.normal(size=40)*.02
    check=Damped(cs=.02,ce=.03);B,D=check.strain_rows(x);f,power=check.damping_force(x,v)
    force_error=float(max(abs(f-(.02*B.T@B+.03*D.T@D)@v)));power_error=float(abs(v@f-power))
    assert force_error<1e-15 and power_error<1e-15
    # Verify exact symmetric reduction against the complete free point equations at arbitrary a,b,velocities.
    a,b,ad,bd=.07,-.01,-.03,.02;p=check.ref.copy();p[1:]*=1+b
    vv=np.r_[ad,(check.ref*bd).ravel()];state=np.r_[a,p.ravel(),vv,0.];dy=check.ode_loss(0,state)
    collective=check.collective_matrix()@np.array([a,b,ad,bd]);expect=np.r_[collective[2],(check.ref*collective[3]).ravel()]
    reduction_error=float(max(abs(dy[40:80]-expect)));assert reduction_error<2e-14
    t=np.linspace(0,100,2001);base=model.damped_collective(t);base_rms=rms((1+base[1])**3-1,t)
    scan=[]
    for cs in [0.,.005,.02]:
        for j in range(121):
            ce=j/1000.;mod=Damped(cs=cs,ce=ce);y=mod.damped_collective(t)
            retention=rms((1+y[1])**3-1,t)/base_rms;soft=math.exp(-ce*model.R2*50)
            poles=np.linalg.eigvals(mod.collective_matrix());rates=sorted(-p.real for p in poles if p.imag>0)
            scan.append({'cs':cs,'ce':ce,'mean_volume_rms_retention':retention,'soft_envelope_at_100':soft,
                         'slow_collective_pole_decay':float(min(rates)),'fast_collective_pole_decay':float(max(rates)),
                         'passes_80_50_screen':bool(retention>=.8 and soft<=.5)})
    csvout(out/'design-scan.csv',scan);eligible=[r for r in scan if r['soft_envelope_at_100']<=.5]
    protected=[r for r in scan if r['mean_volume_rms_retention']>=.8]
    # Small-loss derivatives are explicitly asymptotic, not finite-coefficient bounds.
    lo=8-math.sqrt(37);hi=8+math.sqrt(37)
    derivatives={name:6/(12+(3-lam)**2) for name,lam in [('low',lo),('high',hi)]}
    # Recover exposed worst sample7 exactly from the separately reset prior property generator.
    old=np.random.default_rng(9023);props=[]
    for eps in [.01,.05]:
        for i in range(8):
            m=1+eps*old.uniform(-1,1,13);g=1+eps*old.uniform(-1,1,12);k=.4*(1+eps*old.uniform(-1,1,30))
            if eps==.05 and i==7:props.append(('exposed-previous-7',dict(m=m,g=g,k=k)))
    fresh=np.random.default_rng(10422)
    for i in range(2):props.append((f'seed10422-{i}',dict(m=1+.05*fresh.uniform(-1,1,13),g=1+.05*fresh.uniform(-1,1,12),k=.4*(1+.05*fresh.uniform(-1,1,30)))))
    dump(out/'properties.json',[{'id':name,**{k:v.tolist() for k,v in kw.items()}} for name,kw in props])
    rows=[];worst=None;maxbaseline=0.
    for A0 in [.025,.1,.2]:
        # Symmetric full3D check at each amplitude and each tested coefficient pair.
        for cs,ce in [(0.,0.),(0.,.005),(0.,.02),(.02,.02)]:
            mod=Damped(cs=cs,ce=ce);xx,vv,info=run(mod,A0,t);yy=mod.damped_collective(t,A0)
            pred=np.repeat(mod.ref[None,:,:],len(t),axis=0);pred[:,1:]*=(1+yy[1,:,None,None])
            error=float(max(np.max(abs(xx[:,0]-yy[0])),np.max(abs(xx[:,1:].reshape(-1,13,3)-pred))))
            assert error<5e-9;maxbaseline=max(maxbaseline,error)
        for name,kw in props:
            matched=None
            for cs,ce in [(0.,0.),(0.,.005),(0.,.02),(.02,.02)]:
                mod=Damped(cs=cs,ce=ce,**kw);xx,vv,info=run(mod,A0,t)
                if matched is None:matched=info.copy()
                row={'amplitude':A0,'property_id':name,'cs':cs,'ce':ce,**info,
                     'mean_volume_rms_retention':info['mean_volume_rms']/matched['mean_volume_rms'],
                     'shape_rms_ratio':info['shell_shape_rms']/matched['shell_shape_rms'],
                     'hub_offset_rms_ratio':info['hub_offset_rms_over_R']/matched['hub_offset_rms_over_R']}
                rows.append(row)
                if ce>0 and (worst is None or info['volume_signal_leakage']>worst[0]):worst=(info['volume_signal_leakage'],A0,name,cs,ce,kw,info)
            print('nonlinear',A0,name,'PASS',flush=True)
    csvout(out/'campaign.csv',rows)
    _,A0,name,cs,ce,kw,oldinfo=worst
    _,_,refined=run(Damped(cs=cs,ce=ce,**kw),A0,np.linspace(0,100,4001),True)
    refinement={'amplitude':A0,'property_id':name,'cs':cs,'ce':ce,'original':oldinfo,'refined':refined,
                'leakage_change':abs(refined['volume_signal_leakage']-oldinfo['volume_signal_leakage'])}
    assert refinement['leakage_change']<3e-6
    groups=[]
    for cs,ce in [(0.,0.),(0.,.005),(0.,.02),(.02,.02)]:
        rr=[r for r in rows if r['cs']==cs and r['ce']==ce]
        groups.append({'cs':cs,'ce':ce,'points':len(rr),'maximum_volume_leakage':max(r['volume_signal_leakage'] for r in rr),
                       'minimum_mean_volume_rms_retention':min(r['mean_volume_rms_retention'] for r in rr),
                       'maximum_shape_rms_ratio':max(r['shape_rms_ratio'] for r in rr),
                       'minimum_shape_rms_ratio':min(r['shape_rms_ratio'] for r in rr),
                       'maximum_hub_offset_rms_ratio':max(r['hub_offset_rms_ratio'] for r in rr)})
    result={'status':'PASS','numpy':np.__version__,'scipy':scipy.__version__,'exact_soft':exact,
            'energy_identity':'dE/du=-cs*sum(sdot^2)-ce*sum(edot^2)',
            'collective_equations':'alpha_ddot+13alpha-12b=0; b_ddot+(cs+5ce/2)b_dot+3b-alpha=0',
            'exact_preservation_obstruction':'For nontrivial common breathing R=(6cs+15ce)*bdot^2; nonnegative independent dashpots protect it identically only if cs=ce=0.',
            'small_loss_pole_derivative_per_d':derivatives,
            'soft_envelope_half_threshold_ce':2*math.log(2)/(100*model.R2),
            'linear_scan':{'points':len(scan),'screen_pass_count':sum(r['passes_80_50_screen'] for r in scan),
                           'best_retention_while_halving_soft':max(eligible,key=lambda r:r['mean_volume_rms_retention']),
                           'smallest_soft_envelope_while_retaining80pct':min(protected,key=lambda r:r['soft_envelope_at_100'])},
            'nonlinear_groups':groups,'nonlinear_points':len(rows),'symmetric_full3d_checks':12,
            'maximum_symmetric_solution_error':maxbaseline,'force_jacobian_error':force_error,'force_power_error':power_error,
            'collective_reduction_error':reduction_error,'matrix_exponential_check':float(max(abs(model.damped_collective(np.array([1.7]))[:,0]-expm(model.collective_matrix()*1.7)@np.array([.1,0,0,0])))),
            'maximum_energy_balance_relative_error':max(r['balance_relative_error'] for r in rows),
            'minimum_sampled_volume_ratio':min(r['minimum_oriented_cell_volume_ratio'] for r in rows),
            'maximum_P_drift':max(r['linear_momentum_drift'] for r in rows),'maximum_L_drift':max(r['angular_momentum_drift'] for r in rows),
            'refinement':refinement,'limitations':['363 sampled coefficient points,not a continuous feasibility theorem','36 property/amplitude/loss points,not a tolerance-box guarantee','Soft envelope is a linear equilibrium modal pole measure,not finite-amplitude worst-case energy gain','Shape/hub RMS ratios are matched integrated readouts;normalized mismatch can rise as mean signal decays','No sustained drive,physical calibration,native constitutive identification or material implementation demonstrated']}
    dump(out/'summary.json',result)
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
