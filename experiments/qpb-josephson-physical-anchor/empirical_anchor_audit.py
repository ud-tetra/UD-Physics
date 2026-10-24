#!/usr/bin/env python3
"""Published APL 2022 joint fit: dimensional reconstruction, NOT held-out data."""
import argparse,json,math
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=42
h,e=D('6.62607015e-34'),D('1.602176634e-19')
Phi0=h/(2*e); pi=D(str(math.pi))
Ic,dI=D('8.36e-6'),D('0.08e-6')
f,df=D('13.28e9'),D('0.05e9')
c_spec=D('36.4') # fF/um2, same published fit
C=lambda i,nu:i/(2*pi*Phi0*nu*nu)
cen,lo,hi=C(Ic,f),C(Ic-dI,f+df),C(Ic+dI,f-df)
assert lo<cen<hi
assert abs(C(Ic,f)*2*pi*Phi0*f*f/Ic-1)<D('1e-40')
area=cen*D('1e15')/c_spec
naive=math.hypot(float(dI/Ic),float(2*df/f))*float(cen/D('1e-12'))
bias=[{'gamma':x,'model_GHz':float(f/D('1e9')*(1-D(x)**2).sqrt().sqrt())} for x in ['0','0.2','0.4','0.6','0.8']]
assert all(bias[i]['model_GHz']>bias[i+1]['model_GHz'] for i in range(4))
out={'status':'PASS','source_DOI':'10.1063/5.0082197','source_date':'2022-03-14',
     'source_measurement':'DC-bias plasma resonance, NOT zero-bias phase turning-amplitude series',
     'fit_f_GHz':'13.28 +/- 0.05','fit_Ic_uA':'8.36 +/- 0.08','fit_c_fF_um2':'36.4 +/- 0.04',
     'derived_C_pF':float(cen/D('1e-12')),
     'rectangular_pm_range_pF':[float(lo/D('1e-12')),float(hi/D('1e-12'))],
     'naive_uncorrelated_deltaC_pF_NOT_valid_fit_uncertainty':naive,
     'effective_area_um2_NOT_independently_measured':float(area),
     'bias_model_only_NOT_measured_rows':bias,
     'data_availability':'raw data from corresponding author on reasonable request; NOT acquired',
     'fit_covariance':'NOT_AVAILABLE; published f and Ic fitted together',
     'validation':'FAILED_HELDOUT: joint-fit-derived capacitance is circular; peak phase/amplitude data absent',
     'reference_correction':'PhysRevResearch.2.043091 includes Eq 13 theoretical amplitude-period relation, not empirical amplitude sweep',
     'evidence':['EMPIRICAL_SUMMARY','EXACT_IDENTITY','NUMERICAL_SENSITIVITY','OPEN'],
     'UD_comparison':'NOT_RUN: no calibrated and frozen UD physical map or held-out amplitude dataset'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True)
 a=ap.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'PASS','C_pF':out['derived_C_pF'],'heldout':False}))
