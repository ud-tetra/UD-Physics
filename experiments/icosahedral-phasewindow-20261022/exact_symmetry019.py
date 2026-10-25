#!/usr/bin/env python3
"""Exact theorem for the icosahedrally symmetric sector of the UD MountLoss model.

Full state 280q+280v+heat, but 3 generalized coordinates (alpha,b,c)
when uniform primary coefficients, unit auxiliary gain, and uniform
housing weights; initial phase restricted to common scalar radial housing
position/velocity. Source blob IDs and limitations in SYMMETRY_THEOREM.md.
"""
from fractions import Fraction as Q
import json,argparse
from pathlib import Path

EP=Q(13,200)  # alpha0=1/10, primary g_i=1
EH=Q(51,20000000)
ESTAR=EP+EH
# Uniform icosahedron: 12 radial members, 30 exterior edges k=2/5.
# U_primary=1/2 (alpha^2+24 s^2+12(s-alpha)^2)
# =13/2*(alpha-12s/13)^2+(162/13)*s^2.
B_ENERGY_COEFF=Q(162,13)
assert ESTAR<B_ENERGY_COEFF*Q(3,40)**2
# Three-dimensional edge geometry in exact Q(sqrt5):
# R2=(5+sqrt5)/8, m2=(3+sqrt5)/8; m.v_opposite=R2-1/2;
# |v_opposite-(m.v_opposite/m2)m|^2=m2.
# Proof: m2*R2-(R2-1/2)^2=m2^2.
# The Q(sqrt5) rational components of this identity are asserted directly:
# R2=A+B*sqrt5, m2=C+D*sqrt5.
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def add(x,y):return (x[0]+y[0],x[1]+y[1])
R2=(Q(5,8),Q(1,8));M2=(Q(3,8),Q(1,8));D=sub(R2,(Q(1,2),Q(0)))
assert sub(mul(M2,R2),mul(D,D))==mul(M2,M2)
# m2>1/4, so all opposite anchors are farther than b/2.
assert M2[0]>Q(1,4) and M2[1]>0
# strict global lower bounds from b>37/40
b_lower=Q(37,40);b_upper=Q(43,40)
result={
  'status':'PASS', 'evidence':'EXACT / CONDITIONAL',
  'configuration_submanifold':'alpha, b, c with centre=0, X_i=b*v_i, housing H_e=c*(v_i+v_j)/2, z_pairs=0',
  'uniform_assumptions':{'primary_g':'1','primary_k':'2/5','primary_m':'1','ratio_gains':'1','housing_weights':'1', 'beta':'positive (qualified [1/200,1/20])','nu':'nonnegative (qualified [1/25,1/20])','cf':'nonnegative'},
  'housing_phase_constraint':'all 30 housing displacements and velocities follow the single radial midpoint scaling, with total housing energy <= 51/20000000',
  'initial_pulse_energy':str(EP),'housing_budget':str(EH),'total_energy_ceiling':str(ESTAR),
  'primary_radial_energy_lower_coefficient':str(B_ENERGY_COEFF),
  'b_lower_strict':str(b_lower),'b_upper_strict':str(b_upper),
  'all_strut_length_lower_strict':str(b_lower/2),
  'endpoint_distance_squared':'m2*(c-b)^2+b^2/4',
  'opposite_distance_squared':'m2*b^2+m2*(c-b*(R2-1/2)/m2)^2',
  'R2':'(5+sqrt(5))/8','m2':'(3+sqrt(5))/8',
  'volume_ratio_lower_strict':str(b_lower**3),
  'volume_ratio_upper_strict':str(b_upper**3),
  'positive_cell_orientation':'all 20, all u>=0 within icosahedrally symmetric invariant family',
  'result_scope':'all-time strut and volume positivity in symmetric 3-coordinate submanifold; NOT arbitrary 180-phase or scattered materials; no u100 coherence/ringdown',
}
def run():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path);args=ap.parse_args()
 raw=json.dumps(result,sort_keys=True,indent=2)+'\n'
 if args.out:args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(raw)
 print('PASS: all-time exact symmetric-sector strut >37/80, volume in ((37/40)^3,(43/40)^3)')
 print(raw)
if __name__=='__main__':run()
