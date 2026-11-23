#!/usr/bin/env python3
"""Typed UD Planck-length dressing gate v1.2. Exact arithmetic; no physical prediction.

CODATA 2022 lP = 1.616255(18) x10^-35 m from NIST.
A bare SI reference 1e-35 m is CHOSEN, not independently derived in UD.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
import json
getcontext().prec=40
r=F(13,8); p=F(1616255,1000000); sigma=F(18,1000000)
d=p/r;z=d-1
assert d==F(323251,325000) and z==F(-1749,325000)
assert sigma/r==F(9,812500)
assert (r-p)/sigma==F(2915,6)
def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
cases=[]
for name,factor,status in [
 ('none',F(1),'arbitrary unit anchor'),
 ('bVF_27_32',F(27,32),'wrong type: quarantined 7D transfer weight'),
 ('r_retain_185_192',F(185,192),'wrong type: packet retention fraction')]:
 v=r*factor
 cases.append({'name':name,'factor':str(factor),'length_coefficient_exact':str(v),
   'relative_difference_percent':str(100*(dec(v)/dec(p)-1)),'provenance':status})
assert cases[1]['length_coefficient_exact']=='351/256'
result={
 'native_ratio':'13/8','native_type':'first-level unweighted parity-label mean of squared refinement leakage',
 'dressing_rule_historical':'Qobs=Q0(1+z_Q); no z_length supplied',
 'physical_unit_anchor':'10^-35 m CHOSEN for diagnostic; not derived',
 'codata_2022_coefficient':str(p),'codata_1sigma_coefficient':str(sigma),
 'bare_sigma_difference':str((r-p)/sigma),
 'dressing_needed_from_exposed_target':str(d),'z_needed_from_exposed_target':str(z),
 'one_sigma_dressing_tolerance':str(sigma/r),
 'controls':cases,
 'no_go':'Dimensionless state counts and ratios cannot determine an absolute length without an independent SI anchor',
 'finite_floor':'N1=192 count only; 1->4 recursion allows 4^n cells; no source-selected physical termination',
 'Planck_length_prediction_established':False,'physical_promotion':0}
print(json.dumps(result,indent=2,sort_keys=True))
