"""Exact fractions and typed mean-volume gradient for the joint-window bounds."""
from fractions import Fraction as F
from pathlib import Path
import sys,argparse,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-mountloss'))
from mountloss import MountLoss
from model import ico

COMPLIANCE=F(930,2513)
def main(out):
    m=MountLoss();Q=ico.Q5;zero=Q(0);R2=ico.dot(m.vertices[1],m.vertices[1]);vc=Q(F(1,16),F(1,48))
    gradient=[[zero]*3 for _ in range(13)]
    for f in m.faces:
        a,b,c=[m.vertices[i] for i in f];sign=ico.det(a,b,c).sign()
        for i,v in zip(f,[ico.cross(b,c),ico.cross(c,a),ico.cross(a,b)]):
            for axis in range(3):gradient[i][axis]+=sign*v[axis]/(120*vc);gradient[0][axis]-=sign*v[axis]/(120*vc)
    assert gradient[0]==[zero]*3
    for i in range(1,13):assert gradient[i]==[v/(4*R2) for v in m.vertices[i]]
    g=F(19,20);k=F(19,50);kaa=1+12*g;kab=-12*g;kbb=12*(1+g)+30*k
    static=9*kaa/(kaa*kbb-kab*kab);assert static==COMPLIANCE
    # sqrt5<9/4 => smallest housing Gram eigenvalue >1/4.
    assert F(9,4)**2>5
    nu_lo=F(1,25);nu_hi=F(1,20);dlo=nu_lo/F(4)/F(11,10);dhi=2*nu_hi/F(9,10)
    assert dlo==F(1,110) and dhi==F(1,9)
    x=100*dlo;poly=1+x+x*x/2+x*x*x/6
    bound=(20+dhi)/(20-dhi)/poly
    assert bound==F(722733,1749367) and bound<F(1,2)
    Epmax=F(17,250);Ehmax=Epmax/40000;Emax=Epmax+Ehmax
    assert Ehmax==F(17,10000000) and Emax==F(680017,10000000)
    # R²<1. beta>=1/200,w>=9/10 => hm>9/5000,kh>9/50.
    h2=2*Ehmax/F(9,50);v2=2*Ehmax/F(9,5000)
    assert h2==F(17,900000)<F(1,200)**2
    assert v2==F(17,9000)<F(1,20)**2
    assert 2*Emax<F(3,8)**2 and 2*Emax/F(19,50)<F(3,5)**2
    record={'status':'EXACT_PASS','coefficient_field':'Q(sqrt5) geometry; Q fractions',
            'linear_mean_volume_gradient':'l_alpha=l_C=0; l_Xi=r_i/(4R²); exact derivative of average normalized cell volume at reference',
            'minimum_property_collective_stiffness':[[str(kaa),str(kab)],[str(kab),str(kbb)]],
            'uniform_static_mean_volume_compliance_upper':str(static),
            'all_phase_linear_readout_bound':'RMS(delta mean volume)<=sqrt(2 E_h *930/2513); all positive masses and allowed g,k,any nonnegative losses',
            'housing_energy_budget':'E_h<=E_p/40000,E_p=(1+sum g)*(.1)²/2',
            'maximum_initial_total_energy':str(Emax),
            'initial_domain_all_phase_bounds':{'housing_displacement_over_ell0':'<1/200','housing_velocity_over_ell0_per_u':'<1/20','housing_strut_length_over_ell0':'>99/200'},
            'primary_length_bounds_while_flow_exists':{'radial_length_over_R':'>5/8','shell_edge_length_over_ell0':'>2/5','scope':'energy bound while the model remains in its housing-strut domain;not a housing-strut noncollapse/global-existence theorem'},
            'fixed_primary_strength_interval':[str(nu_lo),str(nu_hi)],'fixed_primary_damping_range':[str(dlo),str(dhi)],
            'fixed_primary_u100_energy_upper':str(bound),'fixed_primary_u100_energy_upper_decimal':float(bound),
            'bound_proof':'For d in[dlo,dhi], oscillator energy gain<=((20+dhi)/(20-dhi))*exp(-100dlo). exp(10/11)>1+10/11+(10/11)²/2+(10/11)³/6=9773/3993.',
            'scope':'fixed-primary equilibrium-linear / beta-to-zero housing limit for energy fraction; compliance/readout inequality for full linear assembly. Exact initial-domain/primary-length energy bounds are separate. None proves finite-beta nonlinear box coherence or housing-strut noncollapse.'}
    out.mkdir(parents=True,exist_ok=True);(out/'bounds.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
