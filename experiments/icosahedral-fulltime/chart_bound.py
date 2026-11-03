#!/usr/bin/env python3
"""Exact rational moving SO3 readout bound at reference displacement d=1/20.

This is a conditional chart bound only, not a proof of a nonlinear trajectory tube.
"""
from fractions import Fraction as F
from pathlib import Path
import json,argparse
r=F(9,250); d=F(1,20); cmin=F(18,5)
refop=F(191,100); reffrob=F(331,100)
center=F(25,24); invroot2=F(71,100)
# Proven by 11/5<sqrt5<9/4 and rational squares.
assert F(11,5)**2<5<F(9,4)**2
assert cmin<(5+F(11,5))/2 + F(1,10000)  # lower c=3.618...
assert (5+F(9,4))/2<refop**2 and 3*(5+F(9,4))/2<reffrob**2
assert F(13,12)<center**2 and F(1,2)<invroot2**2
Gmin=cmin-2*refop*d-d*d
assert Gmin>0
t=invroot2*(refop+d)*r/Gmin
B=((reffrob+center*d)*t*t/2+center*r*t)/(1-t)
assert t<1 and B==F(245802834179,264666314250000)
assert B<F(1,1000)
result={"status":"PASS","evidence":["EXACT","CONDITIONAL","NUMERICAL_SOURCE","OPEN"],
"reference_condition":"||Yref(t)-Yequil||_F <= 1/20=0.05, actual full-time continuum NOT verified",
"relative_condition":"||Yactual(t)-Yref(t)||_F <= 9/250=0.036, NOT verified for nonlinear phase ball",
"reference_radius":"1/20","relative_radius":"9/250",
"bound_fraction":str(B),"bound_float":float(B),"threshold":"<1/1000",
"Gram_lower":str(Gmin),"Omega_upper":str(t),"rational_constants":{"c_lower":str(cmin),"ref_operator":str(refop),"ref_Frobenius":str(reffrob),"centroid":str(center),"inv_sqrt2":str(invroot2)},
"source_observed_sampled_reference_max":{"limiting":.03944037550681534,"nominal":.046676592620305025},
"critical_scope":"The chart theorem holds only if both antecedents hold at all target times; sampled DOP853 reference values cannot certify continuous bounds or actual nonlinear perturbation tube."}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps(result,sort_keys=True))
