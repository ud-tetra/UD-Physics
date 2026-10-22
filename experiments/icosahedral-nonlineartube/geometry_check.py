"""Independent representations: exact cell Gram and direct nonlinear witness energy."""
from pathlib import Path
from fractions import Fraction as F
import sys,argparse,json
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-mountloss'))
from mountloss import MountLoss
from model import ico

def main(out):
    m=MountLoss(beta=.005,cf=0.,nu=.04);Q=ico.Q5;R2=ico.dot(m.vertices[1],m.vertices[1]);one=Q(1)
    expected=[[R2 if i==j else R2-Q(F(1,2)) for j in range(3)] for i in range(3)]
    for face in m.faces:
        vectors=[m.vertices[i] for i in face]
        gram=[[ico.dot(x,y) for y in vectors] for x in vectors]
        assert gram==expected
        assert ico.det(*gram)==(Q(F(3,8),F(1,8)))**2
    assert (R2-Q(F(9,10))).sign()>0 and (one-R2).sign()>0
    # Avoid norm divisions exactly at the strut singularity: energy() depends
    # on mount displacement but never on strut direction; its continuous
    # extension is well-defined and compared with the exact expression.
    y=m.initial_augmented(0.);i,j=m.edges[0];H=y[190:280].reshape(30,3)
    H[0]=m.ref[i];U=m.energy(y);pred=1/(40*m.R2)
    assert abs(U-pred)<1e-15 and U<.065
    nearby=[]
    midpoint=(m.ref[i]+m.ref[j])/2
    for fraction in [.1,.01,.001,.0001]:
        H[0]=m.ref[i]+fraction*(midpoint-m.ref[i]);ell=min(m.loss_geometry(y[:40],H)[1]);energy=m.energy(y)
        assert energy<.065;nearby.append({'remaining_fraction_to_endpoint':fraction,'minimum_strut_length':float(ell),'energy':float(energy)})
    result={'status':'EXACT_GEOMETRY_AND_NUMERICAL_ENERGY_CHECK_PASS','exact_cell_gram_checks':20,
            'exact_geometry_field':'Q(sqrt5)','reference_gram_min_eigenvalue':'1/2',
            'direct_witness_energy':U,'formula_witness_energy':pred,'nominal_pulse_energy':.065,
            'near_singular_states':nearby,'scope':'Algebraic reference geometry verified exactly; direct model energy/witness checks float64; not a dynamical counterexample.'}
    out.mkdir(parents=True,exist_ok=True);(out/'geometry_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
