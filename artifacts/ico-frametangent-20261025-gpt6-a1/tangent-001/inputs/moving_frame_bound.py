"""Exact conditional moving-reference SO(3) chart bound for source ico3D model.
The archived reference offset .011 is a numeric endpoint precondition, NOT a
validated continuous-time envelope; relative actual perturbation .036 is OPEN.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import argparse
r=F(9,250)
d=F(11,1000)
op=F(39,20) # sqrt(c0)<39/20 because c0=(5+sqrt5)/2<15/4
full=F(27,8) # ||X0||F=sqrt(3 c0)<27/8
cent=F(21,20) # sqrt(13/12)<21/20
lower=F(7,2)-2*op*d-d*d
assert lower>0
# For Gram Gref=Xref.T Xref, its λ_min>=lower.
# M=tr Gref*I-Gref has λ_min>=2lower; vector norm of
# skew(Xref.T Ecentered) <= ||Xref||op ||E||F / sqrt(2).
# Use 1/sqrt(2)<3/4 for rational majorant.
t=F(3,4)*(op+d)*r/lower
assert t<1
# Reference relative hub/shell vector is bounded by ||Y0||F + cent*d.
B=((full+cent*d)*t*t/2+cent*r*t)/(1-t)
assert B==F(93325499434647,94141337114624000)
assert B<F(1,1000)
result={'status':'PASS','labels':['EXACT','CONDITIONAL','NUMERICAL','OPEN'],
 'baseline_displacement_condition':'||Yref - Y0||F<=11/1000 at a considered time (only endpoint source data checked numerically)',
 'actual_relative_perturbation_condition':'||Yactual - Yref||F<=9/250, NOT proven uniformly or for nonlinear flow',
 'orientation':'proper SO3, shell-centroid-subtracted 13-primary layout',
 'reference_gram_lambda_min_rational':str(lower),
 'omega_operator_norm_rational':str(t),
 'nonlinear_chart_remainder_upper_fraction':str(B),
 'nonlinear_chart_remainder_upper_float':float(B),
 'threshold_strict':'<1/1000 at time where BOTH displacement assumptions hold',
 'scope':'generic 3D moving-reference chart; not a flow-invariant tube, Green estimate, volume remainder or UD-specific signature',
 'constants':{'r':str(r),'d':str(d),'reference_op_bound':str(op),'reference_full_Frob_bound':str(full),'centroid_map_bound':str(cent)}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps(result,sort_keys=True))
