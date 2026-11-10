#!/usr/bin/env python3
"""Exact conditional moving SO3 chart bound with post-exposure d=.070.

This is geometry only: neither reference nor relative 180-phase nonlinear
continuous-time displacement conditions are derived from the mechanical ODE.
"""
import argparse,json
from fractions import Fraction as Q
from pathlib import Path
r=Q(9,250)
d=Q(7,100)
c_lower=Q(18,5)
ref_op=Q(191,100)
ref_frob=Q(331,100)
cent=Q(25,24)
inv_root_two=Q(71,100)
# All these inequalities bound the source regular golden-ratio shell.
assert Q(11,5)**2 < 5 < Q(9,4)**2
assert c_lower <= (5+Q(11,5))/2
assert (5+Q(9,4))/2 < ref_op**2
assert 3*(5+Q(9,4))/2 < ref_frob**2
assert Q(13,12)<cent**2 and Q(1,2)<inv_root_two**2
G=c_lower-2*ref_op*d-d*d
rotation=inv_root_two*(ref_op+d)*r/G
B=((ref_frob+cent*d)*rotation*rotation/2+cent*r*rotation)/(1-rotation)
assert G>0 and 0<rotation<1
assert B < Q(1,1000)
result={"status":"PASS","evidence":["EXACT","CONDITIONAL","OPEN"],
"reference_Frobenius_radius_assumed":str(d),
"actual_nonlinear_relative_Frobenius_radius_assumed":str(r),
"source_reference_maximum_sampled_0p25":{"limiting":0.050392408410262046,"nominal":0.05109022585379984},
"G_lower_bound":str(G),"skew_operator_bound":str(rotation),
"nonlinear_SO3_chart_remainder_upper_fraction":str(B),
"nonlinear_SO3_chart_remainder_upper_float":float(B),
"threshold_met":"<1/1000 only IF BOTH actual displacement radius premises hold",
"scope":"NO full-time reference enclosure, no nonlinear 180-phase ball radius proof, no forced Green/Hessian, no volume or physical UD promotion",
"selection_origin":"d=.070 chosen AFTER earlier d=.050 was contradicted by u9.25 numerical reference samples"}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True))
