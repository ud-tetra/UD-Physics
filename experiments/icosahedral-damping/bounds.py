"""Exact all-time length-domain bound and collective polynomial check."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math

def main(out):
    # Expand (r^2+13)(r^2+d*r+3)-12 using integer coefficients in r,d.
    a={(2,0):1,(0,0):13};b={(2,0):1,(1,1):1,(0,0):3};p={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():p[i+k,j+l]=p.get((i+k,j+l),0)+v*w
    p[0,0]-=12
    assert p=={(4,0):1,(3,1):1,(2,0):16,(1,1):13,(0,0):27}
    G=1+12*F(21,20);kmin=F(2,5)*F(19,20);A2=kmin/G
    assert G==F(68,5) and kmin==F(19,50) and A2==F(19,680)
    # Exact pair arithmetic in Q(sqrt37); independently check modal energy fractions.
    def mul(x,y):return (x[0]*y[0]+37*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def inv(x):
        den=x[0]**2-37*x[1]**2
        return (x[0]/den,-x[1]/den)
    for sign in [1,-1]:
        den=mul((F(-5),F(sign)),(F(-5),F(sign)));den=(den[0]+12,den[1])
        assert mul((F(6),F(0)),inv(den))==(F(1,4),sign*F(5,148))
    result={'status':'PASS','collective_characteristic_polynomial':'r^4+d*r^3+16*r^2+13*d*r+27',
            'weak_loss_low_amplitude_decay_per_d':'(1+5/sqrt37)/4','weak_loss_high_amplitude_decay_per_d':'(1-5/sqrt37)/4',
            'weak_loss_low_decay_per_ce':'(5/8)*(1+5/sqrt37)','soft_decay_per_ce':'(5+sqrt5)/16',
            'inequality_proof':'low per ce>5/8; soft per ce<1/2 because sqrt5<3; low common mode decays faster for infinitesimal edge loss',
            'domain_bound':{'g_box':'[19/20,21/20]','k_box':'[19/50,21/50]','Gmax':str(G),'kmin':str(kmin),
                            'amplitude_strict_upper':'sqrt(19/680)','amplitude_upper_approx':math.sqrt(float(A2)),
                            'radial_strain_bound':'sqrt(68/5)*|A0|','edge_strain_bound':'sqrt(680/19)*|A0|',
                            'proof':'E(u)<=E(0)=(1+sum g) A0^2/2; U>=sum s_i^2/2 and U>=sum k_ij e_ij^2/2. Strict amplitude bound keeps each radial and edge length positive for every time and every nonnegative axial loss.',
                            'scope':'Initial undeformed points,alpha=A0,all velocities zero; positive masses; ±5% g,k box; no cell-orientation or convexity guarantee. A0=1/5 probes exceed this certificate.'}}
    out.mkdir(parents=True,exist_ok=True);(out/'bounds.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
