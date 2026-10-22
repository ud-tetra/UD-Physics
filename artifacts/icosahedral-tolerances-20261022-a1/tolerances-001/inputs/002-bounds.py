"""Exact fractional module-impedance and symmetric housing-frequency bounds."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math

def main(out):
    eps=F(1,100);cf=F(1,1000);zmin=F(1250,2329);zmax=F(625,362)
    # D(x)=4x²-175x+2500, x=omega² in[1,16];Dprime=8x-175<0.
    assert 8*16-175<0
    assert zmin==F(1250,4-175+2500) and zmax==F(1250,4*256-175*16+2500)
    common=cf/5+eps*eps*zmax;differential=(1-eps/2)**2*zmin;ratio=common/differential
    cross=eps/(1-eps/2);assert cross==F(2,199) and ratio<F(1,1000)
    # rho=(5+sqrt5)/10<3/4, parent lambda_high=8+sqrt37<15.
    assert F(5)<F(25,4) and F(37)<F(49)
    beta=F(1,20);omega2=F(100);mass_enlargement=beta*F(3,4)/(1-F(15)/omega2)
    assert mass_enlargement==F(3,68)
    lowratio=1/(1+mass_enlargement);assert lowratio==F(68,71)
    result={'status':'PASS','module':{'coordinates':'u_c=(y_a+y_b)/2,u_d=y_a-y_b;f_c=f_a+f_b,f_d=(f_a-f_b)/2',
            'impedance':'Z_port=Z(s)*v*v^T+(cf/10)*diag(2,1/2),v=(-delta,1+delta/2)',
            'Zcc':'delta²*Z+cf/5','Zcd=Zdc':'-delta*(1+delta/2)*Z','Zdd':'(1+delta/2)²*Z+cf/20',
            'band':'1<=omega<=4','delta_bound':str(eps),'cf_bound':str(cf),'ReZ_min':str(zmin),'ReZ_max':str(zmax),
            'ReZcc_upper':str(common),'ReZcc_upper_approx':float(common),'ReZdd_lower':str(differential),
            'dissipative_diagonal_ratio_upper':str(ratio),'dissipative_diagonal_ratio_approx':float(ratio),
            'normalized_cross_impedance_upper':str(cross),'scope':'bare reciprocal module;cf in[0,.001],|delta|<=.01,mu2/kappa50/gamma5;not whole-assembly coherence or added mounting inertia'},
            'housing':{'rho':'(5+sqrt5)/10','parent_collective_lambda_high_upper':'15','beta_upper':str(beta),'omega_h_lower':'10',
                       'frequency_ratio_lower_squared':str(lowratio),'frequency_ratio_lower':math.sqrt(float(lowratio)),
                       'maximum_frequency_downshift_fraction':1-math.sqrt(float(lowratio)),
                       'proof':'For uniform housing masses andideal mechanical symmetry,eliminate c belowOmega². Added collective dynamic inertia is beta*rho/(1-lambda/Omega²). The two low loaded eigenvalues are no larger than parent ones (Rayleigh trial c=b). Since parent lambda_high<15 andrho<3/4,their frequency ratios exceed sqrt(68/71) forbeta<=.05,Omega>=10.',
                       'scope':'undamped symmetric3-coordinate collective sector;ratios ideal,cf0;no nonuniform hardware mass guarantee;conservative housing is not dissipative'},
            'global':'Positive added housing/branch energies andinitiallyzero mount/branch strain preserve previouspositive-length energy certificate;doesnot certify coherence/orientation.'}
    out.mkdir(parents=True,exist_ok=True);(out/'bounds.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
