"""Proper-frame geometry for readout; does not remove mechanical states/energy."""
import argparse,json
from pathlib import Path
import numpy as np
from jacobian import model,ROOT
from variational import SOURCE,IDS

def rigid_basis(X):
    centered=X-X.mean(0);columns=[np.tile(axis,13) for axis in np.eye(3)]
    columns.extend(np.cross(axis,centered).ravel() for axis in np.eye(3))
    return np.linalg.qr(np.column_stack(columns))[0]

def align(X,reference):
    """Row-vector convention: centered X @ R, with det R=+1."""
    u,s,vt=np.linalg.svd((X-X.mean(0)).T@(reference-reference.mean(0)))
    correction=np.diag([1.,1.,np.linalg.det(u@vt)])
    rotation=u@correction@vt
    return (X-X.mean(0))@rotation+reference.mean(0),rotation

def main(out):
    case=next(p for p in json.loads((SOURCE/'cases.json').read_text()) if p['id']==IDS[0]);m=model(case,.05)
    rng=np.random.default_rng(319477);X=m.ref.copy();X+=rng.normal(0,.002,X.shape);basis=rigid_basis(X)
    direction=rng.normal(size=(13,3));direction/=np.linalg.norm(direction)
    tangent=direction.ravel()-basis@(basis.T@direction.ravel());errors=[]
    for step in [1e-3,1e-4,1e-5]:
        xp,_=align(X+step*direction,X);xm,_=align(X-step*direction,X)
        errors.append({'step':step,'derivative_error':float(np.linalg.norm((xp-xm).ravel()/(2*step)-tangent))})
    assert errors[-1]['derivative_error']<2e-8
    axis=np.array([.2,.4,-.3]);axis/=np.linalg.norm(axis);theta=.31
    cross=np.array([[0.,-axis[2],axis[1]],[axis[2],0.,-axis[0]],[-axis[1],axis[0],0.]])
    R=np.eye(3)+np.sin(theta)*cross+(1-np.cos(theta))*(cross@cross)
    moved=X@R+np.array([.4,-.2,.1]);aligned,rotation=align(moved,X)
    assert np.linalg.det(rotation)>.999999999999 and np.max(abs(aligned-X))<2e-15
    x=np.r_[0.,X.ravel()];z=np.r_[0.,moved.ravel()]
    vol_error=float(np.max(abs(m.volumes(x[None,:])-m.volumes(z[None,:]))));assert vol_error<2e-14
    # Three hub-relative columns have star difference matrix S: SS^T=I+11^T.
    S=np.column_stack([-np.ones(3),np.eye(3)]).astype(int)
    assert np.array_equal(S@S.T,np.eye(3,dtype=int)+np.ones((3,3),dtype=int))
    result={'status':'CONSTRUCTOR_ALIGNMENT_CHECKS_PASS','finite_difference_errors':errors,
            'proper_rotation_det':float(np.linalg.det(rotation)),'rigid_transform_volume_error':vol_error,
            'star_difference_operator_norm_exact':'2; SS^T=I+11^T has eigenvalues4,1,1',
            'scope':'Readout frame geometry and tangent projector; no mechanical state or kinetic energy removed. No uniform nonlinear chart remainder bound.'}
    out.mkdir(parents=True,exist_ok=True);(out/'alignment_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
