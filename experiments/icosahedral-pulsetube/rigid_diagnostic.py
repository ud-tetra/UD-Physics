"""One post-exposure frame diagnostic, chosen to maximize raw final motion."""
import argparse,json,csv,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from alignment import align,rigid_basis
from jacobian import model
from variational import SOURCE,IDS

def main(out):
    case=next(p for p in json.loads((SOURCE/'cases.json').read_text()) if p['id']==IDS[0]);m=model(case,.05)
    d=np.load(out/f'response-{IDS[0]}-fine0.npz');W=d['final_tangent'];B=d['initial_injection'];ref=d['reference'];t=d['u']
    _,singular,vt=np.linalg.svd(W[1:40],full_matrices=False);phase=vt[0]
    if phase[np.argmax(abs(phase))]<0:phase=-phase
    Eh=(1+m.g.sum())*.01/2/40000;eps=np.sqrt(2*Eh);initial=m.initial_augmented(.1);initial[:560]+=eps*(B@phase)
    sol=solve_ivp(m.ode,(0,100),initial,t_eval=t,method='DOP853',rtol=2e-11,atol=2e-14);assert sol.success
    Y=sol.y.T;X=Y[:,1:40].reshape(-1,13,3);Xref=ref[:,1:40].reshape(-1,13,3)
    aligned=[];angles=[];translations=[]
    for x,r in zip(X,Xref):
        a,R=align(x,r);aligned.append(a);angles.append(float(np.arccos(np.clip((np.trace(R)-1)/2,-1,1))))
        translations.append(float(np.linalg.norm(x.mean(0)-r.mean(0))))
    aligned=np.array(aligned);raw=np.linalg.norm((X-Xref).reshape(len(t),39),axis=1)
    shape=np.linalg.norm((aligned-Xref).reshape(len(t),39),axis=1)
    rigid=rigid_basis(Xref[-1]);direction=W[1:40]@phase;normal=direction-rigid@(rigid.T@direction)
    endpoint_remainder=(aligned[-1]-Xref[-1]).ravel()-eps*normal
    vol=m.volumes(Y[:,:40]);refvol=m.volumes(ref[:,:40]);signal=vol.mean(1)-1
    H=Y[:,190:280].reshape(-1,30,3);V=Y[:,281:320].reshape(-1,13,3);VH=Y[:,470:560].reshape(-1,30,3);mass=m.m/m.R2
    P=(mass[None,:,None]*V).sum(1)+(m.hm[None,:,None]*VH).sum(1)
    L=(mass[None,:,None]*np.cross(X,V)).sum(1)+(m.hm[None,:,None]*np.cross(H,VH)).sum(1)
    E=np.array([m.energy(y) for y in Y]);balance=float(np.max(abs(E+Y[:,-1]-E[0]))/E[0]);assert balance<1e-8
    dp=float(np.max(np.linalg.norm(P-P[0],axis=1)));dl=float(np.max(np.linalg.norm(L-L[0],axis=1)));assert max(dp,dl)<2e-11
    baseline=json.loads((SOURCE/'baselines.json').read_text())[case['baseline_id']]['mean_volume_rms']
    ell=np.linalg.norm(H[:,m.housing_index]-X[:,m.anchor_index],axis=2)
    result={'status':'FINITE_FRAME_DIAGNOSTIC_COMPLETE','id':case['id'],'phase_origin':'leading right singular vector of final primary-position tangent, post-exposure diagnostic',
      'phase_sha256':hashlib.sha256(phase.tobytes()).hexdigest(),'phase':phase.tolist(),
      'housing_energy':float(Eh),'predicted_final_raw_primary_position_radius':float(eps*singular[0]),
      'maximum_raw_primary_position_displacement':float(raw.max()),'maximum_aligned_primary_shape_displacement':float(shape.max()),
      'final_aligned_primary_shape_displacement':float(shape[-1]),'final_aligned_tangent_norm':float(eps*np.linalg.norm(normal)),
      'final_aligned_flow_remainder_norm':float(np.linalg.norm(endpoint_remainder)),
      'maximum_primary_centroid_translation':max(translations),'maximum_alignment_rotation_radians':max(angles),
      'maximum_mean_volume_change_from_reference':float(np.max(abs(vol.mean(1)-refvol.mean(1)))),
      'breathing_retention_coarse_grid':float(np.sqrt(np.trapezoid(signal*signal,t)/100)/baseline),
      'minimum_sampled_strut_length':float(ell.min()),'energy_plus_heat_relative_error':balance,'P_drift':dp,'L_drift':dl,
      'initial_P_norm':float(np.linalg.norm(P[0])),'initial_L_norm':float(np.linalg.norm(L[0])),
      'scope':'One finite phase demonstrates frame sensitivity of the ambient norm. It does not prove a uniform aligned nonlinear remainder; all mechanical states, housing kinetic energy and momenta retained.'}
    (out/'rigid_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
    with (out/'rigid_diagnostic.csv').open('w',newline='') as stream:
        names=['u','raw_primary_displacement','aligned_primary_shape_displacement','centroid_translation','rotation_radians'];w=csv.DictWriter(stream,fieldnames=names,lineterminator='\n');w.writeheader()
        for row in zip(t,raw,shape,translations,angles):w.writerow(dict(zip(names,map(float,row))))
    print(json.dumps({k:v for k,v in result.items() if k!='phase'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
