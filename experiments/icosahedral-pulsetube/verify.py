"""Directional finite differences and independent equilibrium matrix assembly."""
import json,argparse
from pathlib import Path
import numpy as np
from jacobian import Linearization,model,ROOT
SOURCE=ROOT/'artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files'

def main(out):
    out.mkdir(parents=True,exist_ok=True);cases=json.loads((SOURCE/'cases.json').read_text());by={p['id']:p for p in cases}
    rng=np.random.default_rng(237113);records=[]
    for id in ['seed10422-0-boundary2','uniform-b0.05-cf0.0']:
        m=model(by[id],.05);L=Linearization(m);y=m.initial_augmented(0.);M,Kn,Cn=m.linear_matrices()
        K,C=L.matrices(y);S=np.sqrt(M)
        dk=float(np.max(abs(K.toarray()/S[:,None]/S[None,:]-Kn)));dc=float(np.max(abs(C.toarray()/S[:,None]/S[None,:]-Cn)))
        assert max(dk,dc)<2e-12
        for mode in ['reference','moving_displaced']:
            y=m.initial_augmented(.1)
            if mode=='moving_displaced':
                y[:280]+=rng.normal(0,.002,280);y[280:560]+=rng.normal(0,.03,280)
            J=L.jacobian(y)
            for seed in range(3):
                d=rng.normal(size=560);d/=np.linalg.norm(d);dy=np.r_[d,0.];expected=J@d
                errors=[]
                for h in [1e-4,1e-5,1e-6]:
                    actual=(m.ode(0,y+h*dy)[:560]-m.ode(0,y-h*dy)[:560])/(2*h)
                    errors.append(float(np.max(abs(actual-expected))))
                assert min(errors)<2e-7
                records.append({'id':id,'state':mode,'direction':seed,'steps':[1e-4,1e-5,1e-6],'max_absolute_errors':errors})
        B=L.injection();q=B[:280];v=B[280:]
        energy_gram=q.T@K.toarray()@q+v.T@(M[:,None]*v)
        # K above is equilibrium from before the random-state loop.
        assert np.max(abs(energy_gram-np.eye(180)))<2e-12
        records.append({'id':id,'independent_reference_K_change':dk,'independent_reference_C_change':dc,'initial_energy_gram_identity_error':float(np.max(abs(energy_gram-np.eye(180))))})
    result={'status':'CONSTRUCTOR_JACOBIAN_CHECKS_PASS','records':records,
            'scope':'Full560-state analytic derivative; central finite difference uses original nonlinear ODE, equilibrium comparison uses separate pre-existing linear matrix assembly. Not independent peer review.'}
    (out/'jacobian_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
