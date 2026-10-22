"""Independent spatial-momentum assembly of conserved rigid kinetic energy."""
from pathlib import Path
import argparse,json
import numpy as np
from linear import model,parent

def main(out):
    cases=[p for p in json.loads((out/'cases.json').read_text()) if p['id']==p['canonical_id']];rng=np.random.default_rng(78321);rows=[]
    for p in cases:
        m=model(p,.04);M,K,C=m.linear_matrices();_,raw=parent.reduced_basis(m,M);R,_=np.linalg.qr(raw)
        points=np.vstack([m.ref,m.midpoints(m.ref)]);mass=np.r_[m.m/m.R2,m.hm]
        V=np.zeros((43,3));V[13:]=rng.normal(0,.01,(30,3))
        v=np.zeros(280);v[190:]=V[13:].ravel();z=np.sqrt(M)*v
        projection=float(np.sum((R.T@z)**2)/2)
        total=mass.sum();centre=np.sum(mass[:,None]*points,axis=0)/total;r=points-centre
        P=np.sum(mass[:,None]*V,axis=0);L=np.sum(mass[:,None]*np.cross(r,V),axis=0)
        inertia=sum(w*((x@x)*np.eye(3)-np.outer(x,x)) for w,x in zip(mass,r))
        spatial=float(P@P/(2*total)+L@np.linalg.solve(inertia,L)/2)
        err=abs(projection-spatial);assert err<2e-15
        objective=float(max(np.max(abs(K@R)),np.max(abs(C@R))));assert objective<3e-12
        rows.append({'id':p['id'],'mass_projection_rigid_energy':projection,'Noether_spatial_rigid_energy':spatial,'absolute_change':err,'linear_rigid_kernel_residual':objective})
    report={'status':'PASS','parameter_sets':len(cases),'method':'independent centre-of-mass/inertia P,L kinetic formula vs mass-QR projection;seed78321',
            'maximum_energy_change':max(r['absolute_change'] for r in rows),'maximum_linear_rigid_kernel_residual':max(r['linear_rigid_kernel_residual'] for r in rows),'rows':rows}
    (out/'rigid_energy_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
