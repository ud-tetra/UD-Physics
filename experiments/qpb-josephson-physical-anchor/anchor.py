#!/usr/bin/env python3
"""Ideal Josephson physical anchor versus positive UD hidden-star quartic.
Source constraints from BIPM SI and PRX Quantum circuit review; no lab data.
"""
import argparse,json,math
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
h=Decimal('6.62607015e-34');e=Decimal('1.602176634e-19')
phi0_exact=F(h)/(2*F(e));phi0=float(phi0_exact);phibar=phi0/(2*math.pi)
Ic=1e-7;C=1e-13 # design choices, NOT measured
EJ=Ic*phibar;M=C*phibar**2
w0=math.sqrt(EJ/M);f0=w0/(2*math.pi);tau0=2/w0
T2=F(1,4)*F(1,4)
T4=F(1,4)*F(-1,48)+F(9,64)*F(1,16)
w2=-T2;w4=T2*T2-T4
assert (T2,T4,w2,w4)==(F(1,16),F(11,3072),F(-1,16),F(1,3072))
def agm(a,b):
 for _ in range(35):
  a,b=(a+b)/2,math.sqrt(a*b)
 return a
def independent_integral(a):
 k2=math.sin(a/2)**2;n=8192;step=math.pi/(2*n)
 s=0
 for i in range(n+1):
  z=i*step;f=(1-k2*math.sin(z)**2)**(-0.5)
  s+=(1 if i in (0,n) else 4 if i%2 else 2)*f
 K=s*step/3
 return math.pi/(2*K)
rows=[]
for a in (0,.2,.4,.6,1.):
 ratio=agm(1,math.cos(a/2))
 residual=abs(ratio-independent_integral(a))
 assert residual<1e-11
 if a:assert 0<ratio<1 and 1+a*a/16>1
 rows.append({'phase_peak_rad':a,'exact_model_ratio_float':ratio,'linear_ratio':1.,'positive_star_equal_slope_magnitude_toy':1+a*a/16,'series_4th':1-a*a/16+a**4/3072,'AGM_quadrature_difference':residual,'scenario_frequency_hz':f0*ratio})
result={'status':'PASS','labels':['EXACT','CONDITIONAL','NUMERICAL','HYPOTHESIS','FAILED','OPEN'],
'physical_sources':['https://www.bipm.org/en/measurement-units/si-defining-constants','https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040204','https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.043091'],
'physical_model':'I=Ic*sin(phi), V=(Phi0/2pi)*phi_dot, U=EJ*(1-cos(phi)), EJ=Ic*Phi0/(2pi)',
'SI_exact':{'h_Js':str(h),'e_C':str(e),'Phi0_Wb_exact_fraction':str(phi0_exact),'Phi0_Wb_decimal_approx':phi0},
'design_not_measurement':{'Ic_A':Ic,'total_C_F':C,'zero_bias':True,'ideal_no_loss':True},
'scenario':{'EJ_J':EJ,'equivalent_inertia_Cphi_bar_squared':M,'omega0_rad_s':w0,'f0_Hz':f0,'native_time_unit_seconds_if_linear_frequency_matched':tau0},
'exact_frequency':'w(a)/w0=pi/(2*K(sin(a/2)))=AGM(1,cos(a/2)); 0<=a<pi',
'series_exact':{'period_a2':str(T2),'period_a4':str(T4),'frequency_a2':str(w2),'frequency_a4':str(w4)},
'rows':rows,'tests':{'AGM_vs_quadrature':len(rows),'strict_softening_sign_cases':4,'exact_series_rationals':4},
'mapping_hypothesis':'r3=kappa*a^2 with kappa>0 and zero mapped to zero; physical JJ phase is NOT UD J-fiber phase',
'UD_positive_star':'w_UD(a)/w_UD(0)=1+lambda*kappa*a^2 with lambda>=0',
'conditional_incompatibility':'physical first amplitude coefficient -1/16 versus UD lambda*kappa>=0',
'backsolve_if_relaxed':'lambda*kappa=-1/16 from physical source; not selected by UD, negative bare quartic is not globally coercive',
'ordinary_null':'ideal classical Josephson pendulum explains full amplitude-frequency curve',
'limitations':['Ic,C illustrative and unmeasured','no experimental data or physical UD 15-port mapping','no damping/bias/noise/distributed modes','not a universal no-go for modified UD constitutive laws']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);v=p.parse_args()
 v.out.parent.mkdir(parents=True,exist_ok=True)
 v.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'status':'PASS','f0_Hz':f0,'checks':len(rows),'quartic_sign':'opposite'},sort_keys=True))
