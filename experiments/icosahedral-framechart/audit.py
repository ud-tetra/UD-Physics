#!/usr/bin/env python3
"""EXACT/CONDITIONAL icosahedral proper-frame readout chart, not 560-state flow.
The proof uses exact rational inequalities; numeric rotations are constructor tests.
"""
import argparse, json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

# Icosahedron vertices: unscaled edges 2; scale 1/2 gives shell edge 1.
phi=(1+math.sqrt(5))/2
X=np.array([(0,i,j*phi) for i in [-1,1] for j in [-1,1]]+
           [(i,j*phi,0) for i in [-1,1] for j in [-1,1]]+
           [(j*phi,0,i) for i in [-1,1] for j in [-1,1]],float)/2
R2=(5+math.sqrt(5))/8
c=4*R2
assert X.shape==(12,3) and np.linalg.norm(X.sum(axis=0))<1e-14
assert np.max(np.abs(X.T@X-c*np.eye(3)))<1e-14
assert abs(min(np.linalg.norm(X[i]-X[j]) for i in range(12) for j in range(i+1,12))-1)<1e-14

# Rigorous rational bounds: 7/2<=c<15/4, ||X||F=sqrt(3c)<27/8.
# For full 13-point error ||E||F<=r=9/250, shell centroid mu,
# Etilde=(E_shell-mu, E_hub-mu) satisfies ||Etilde||F<=sqrt(13/12)||E||F
# (linear centroid map); sqrt(13/12)<21/20.
# Ω=skew(X^T(E_shell-mu))/c: ||Ω||op=||Ω||F/sqrt(2)
# <=||E||F/sqrt(2c)<=2r/5<=9/625=:t.
# R=exp(-Ω) in SO(3). The frame chart is ((X+E_c)R-X,(E_hub-mu)R).
# Its linearization is (E_c-XΩ,E_hub-mu), annihilating rigid tangents.
# Since exp(t)-1-t<=t²/[2(1-t)] and exp(t)-1<=t/(1-t),
# ||chart(E)-linear(E)||F <= [ (27/8)*t²/2 + (21/20)*r*t ]/(1-t).
r=F(9,250);t=F(9,625);xf=F(27,8);ed=F(21,20)
bound=(xf*t*t/2+ed*r*t)/(1-t)
assert bound==F(5589,6160000) and bound<F(1,1000)
assert F(13,12)<ed*ed and F(45,4)<xf*xf

def skew(a):return (a-a.T)/2

def rotation(omega):
    # Rodrigues for exp(-omega), preserving exact proper rotation topologically.
    q=-omega
    theta=math.sqrt(max(0.,-np.trace(q@q)/2))
    if theta<1e-10:
        return np.eye(3)+q+q@q/2
    return np.eye(3)+(math.sin(theta)/theta)*q + ((1-math.cos(theta))/theta**2)*(q@q)

def outputs(E):
    mu=np.mean(E[:12],axis=0)
    Ec=E[:12]-mu
    O=skew(X.T@Ec)/c
    Q=rotation(O)
    nonlinear=np.vstack(((X+Ec)@Q-X,(E[12]-mu)@Q))
    linear=np.vstack((Ec-X@O,E[12]-mu))
    return nonlinear,linear,Q,O

rng=np.random.default_rng(314159)
max_error=0.;checks=0;max_orth=0.;max_linrigid=0.
for amp in (0.,.007,.02,.03500972,.036):
    for _ in range(24):
        E=rng.normal(size=(13,3))
        E*=amp/np.linalg.norm(E)
        new,lin,Q,O=outputs(E)
        error=float(np.linalg.norm(new-lin))
        assert error<=float(bound)+2e-13
        assert np.linalg.norm(lin[:12].mean(axis=0))<1e-13
        assert np.linalg.norm(skew(X.T@lin[:12]))<1e-12
        orth=float(np.linalg.norm(Q.T@Q-np.eye(3)))
        assert orth<2e-12 and np.linalg.det(Q)>0
        max_error=max(max_error,error);max_orth=max(max_orth,orth);checks+=1
for axis in np.eye(3):
    E=np.tile(axis,(13,1))*F(1,100).__float__()
    new,lin,_,_=outputs(E)
    assert np.linalg.norm(new)<2e-14 and np.linalg.norm(lin)<2e-14
    max_linrigid=max(max_linrigid,float(np.linalg.norm(lin)))
# Full pure SO(3) displacement chart is nonlinear but its first-order
# rigid tangent is annihilated; that motion is not discarded mechanically.
for theta in (.001,.01):
    O=skew(np.array([[0.,-theta,0],[theta,0,0],[0,0,0]]))
    Q=rotation(-O)
    E=np.vstack((X@Q-X,np.zeros((1,3))))
    new,lin,_,_=outputs(E)
    assert np.linalg.norm(lin)<5*theta**2 and np.linalg.norm(new)<5*theta**2
result={
 'status':'PASS','evidence':['EXACT','CONDITIONAL','NUMERICAL','OPEN'],
 'source_geometry':'Regular edge-one icosahedral shell, 12 points and central point; X^T X=cI3; c=(5+sqrt5)/2',
 'mechanical_scope':'READOUT ONLY on 13 primary positions; existing 280 configurations/560 phase variables and housing masses unchanged',
 'chart':'Subtract shell centroid mu from all 13 points, rotate by exp(-skew(X^T(E_shell-mu))/c)',
 'linearization':'(E_shell-mu-X*Omega,E_hub-mu), Omega=skew(X^T(E_shell-mu))/c; removes translation and infinitesimal shell rotation',
 'radius_assumption':'The *actual* full 13-primary displacement error E has Frobenius norm <=9/250=0.036 continuously; this is NOT verified for all trajectories',
 'analytic_chart_quadratic_upper_fraction':str(bound),
 'analytic_chart_quadratic_upper_float':float(bound),
 'threshold_check':'Chart-only nonlinear remainder <1/1000 in primary Frobenius units if actual radius<=0.036',
 'proof_bounding_constants':{'c_lower':'7/2','c_upper':'15/4','reference_Frob_upper':'27/8','centroid_map_upper':'21/20','rotation_norm_upper':'9/625'},
 'numerical_constructor':{'cases':checks,'max_chart_linear_difference':max_error,'max_rotation_orthogonality_error':max_orth,'translation_tangent_error':max_linrigid},
 'prior_exposed_tangent_raw_radius':0.03500972,
 'prior_exposed_aligned_procrustes_tangent_radius':0.0002420865,
 'comparison_caveat':'Prior Procrustes aligned tangent radius belongs to another chart and cannot simply be combined with this new chart bound; must repropagate/transform full 180-column tangent.',
 'unclosed_tube':['actual continuous primary radius for all housing phases','forced U(t,s) Green bound','uniform Hessian and nonlinear trajectory remainder','numerical reference defect','aligned mean-volume readout remainder','positive strut length domain and full-state norm'],
 'conventional_null':'Centroid subtraction and an SO(3) proper-frame readout are generic ordinary 3D mechanics, not uniquely UD',
 'physical_map':'Internal length ell0; no physical material/bath/clock calibration or empirical test'
}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','chart_bound':str(bound),'numeric_checks':checks},sort_keys=True))
