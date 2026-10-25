#!/usr/bin/env python3
"""Exact uniform short-time tube for original-alpha UD 3D MountLoss.

Run: python3 shorttube.py --out result.json
All assertions use Fraction, no float or differential-equation integration.
This is a conditional statement about the repo's declared ideal passive law.
"""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

SOURCE_MAIN = "7ae79d882e44446c7b4aefd4fdbe9ee781b9bafe"
PHASE_PARENT = "0391afb4617db89690a5eaee9b5fc6c0ae3c9b70"

# Reference pulse alpha0=1/10, qualified m,g,k,beta,w,Omega,nu,cf.
A0 = Q(1,10)
BETA_MIN = Q(1,200)
W_MIN = Q(9,10)
NU_MAX = Q(1,20)
OMEGA = Q(10)
EH = Q(51,20000000)           # 1.5 * original Ep_ref/40000
E = Q(34,5) * A0*A0 + EH     # g_i<=21/20 for all 12 spokes
MP_MIN = Q(19,20)            # m_i/R^2>19/20 since R^2<1
MH_MIN = Q(9,5000)           # 2 beta w/(5R^2)>9/5000
KH_MIN = MH_MIN * OMEGA**2   # >9/50
KE_MIN = Q(19,50)

# Conservative strict speed/initial mount displacement majorants.
VP = Q(2,5)                # every primary 3D point speed, throughout domain
VH = Q(9)                  # every housing 3D point speed, throughout domain
V0H = Q(3,50)              # initial housing 3D speed
D0 = Q(1,180)              # initial housing-to-reference-midpoint offset
assert 2*E < MP_MIN*VP**2
assert 2*E < MH_MIN*VH**2
assert 2*EH < MH_MIN*V0H**2
assert 2*EH < KH_MIN*D0**2

# Each housing has exactly four central viscous paths; eta/m_h=nu/w_e.
# Damped rhs magnitude <=(nu/w_e) sum_a |n_a*(n_a dot(Vh-Va))|
FRICTION_FORCE_PER_H_MASS = (NU_MAX/W_MIN)*4*(VH+VP)
assert FRICTION_FORCE_PER_H_MASS == Q(94,45)

# Valid for all 0<=t before a positive-length-domain exit.
# Exactly solve housing oscillator with variable midpoint A(t), using
# |sin(10 tau)|<=min(10 tau,1), |cos|<=1.
# For 0<=t<=1/10:
#   |H(t)-A(0)| < D0 + V0H*t + 10^2 VP*t^3/6
#                  + (94/45)*t^2/2.
# For 1/10<=t:
#   |H(t)-A(0)| < D0 + V0H/10
#            + 10 VP*(t^2/2 -t/20+1/600)
#            + (94/45)/10*(t-1/20).
# Every primary anchor satisfies |X_a(t)-X_a(0)|<VP*t.
# Reference min |A_e(0)-X_a(0)|=1/2.
def lower_short(t):
    return Q(1,2)-D0-(V0H+VP)*t-Q(20,3)*t**3-Q(47,45)*t**2

def lower_long(t):
    return Q(1,2)-(Q(7,900)+Q(92,225)*t+Q(2)*t*t)

T_SWITCH = Q(1,10)
T_CERT = Q(2,5)
assert lower_short(T_SWITCH) == lower_long(T_SWITCH) == Q(647,1500)
assert lower_long(T_CERT) == Q(13,1500)>0
assert lower_long(Q(39,100)) == Q(257,9000)>Q(1,40)
assert lower_short(Q(0)) > lower_short(T_SWITCH)
# On [0,1/10] and [1/10,2/5] the rational polynomial lower bounds
# strictly decrease: derivatives all negative, so endpoint checks suffice.

# Primary members positive independently of the tube, via whole-energy storage:
# 0.5*sum(s_i^2+k_j e_j^2) <= E. Therefore |s_i|<2/5,
# |e_j|<3/5, guaranteeing noncollapsed spokes and exterior edges.
assert 2*E<Q(2,5)**2
assert 2*E<KE_MIN*Q(3,5)**2

# Every 3D primary point moves by <(2/5)t. Each of a cell's three
# centre-to-corner columns changes by <(4/5)t, so ||Delta A||_F <7t/5,
# as (4/5)*sqrt(3) <7/5. The exact reference sigma_min(A0)=1/sqrt2 >7/10.
assert Q(4,5)**2 * 3 < Q(7,5)**2
assert Q(7,10)**2 < Q(1,2)
# Thus ||A_ref^{-1}Delta A||_2 <2t, for all t in [0,T_CERT].
assert Q(2)*T_CERT==Q(4,5)<1
VOL_LOWER=(1-Q(2)*T_CERT)**3
VOL_UPPER=(1+Q(2)*T_CERT)**3
assert (VOL_LOWER,VOL_UPPER)==(Q(1,125),Q(729,125))

# Source-provided energy-sublevel obstruction at original amplitude remains.
# A configuration with one housing at an edge endpoint and nominal beta=.005
# costs U=1/(40 R^2)<1/36 < original Ep_nominal=13/200.
assert Q(1,36)<Q(13,200)

RESULT={
 "status":"EXACT_CONDITIONAL_ORIGINAL_AMPLITUDE_SHORT_TUBE",
 "question":"Do all 180 allowed initial housing phases retain strut lengths and oriented volumes to u=2/5 with original alpha0=1/10?",
 "source_main_revision":SOURCE_MAIN,
 "owning_phase_branch_parent":PHASE_PARENT,
 "geometry":"Euclidean 3D 13 primary points and 30 housings, unit outer edges; no Lorentzian map",
 "mechanics":"Unchanged MountLoss model, 280 position/560 phase, 120 current-axis reciprocal loss struts, positive kinetic/elastic energies, nonnegative viscous power",
 "parameter_box":"alpha0=1/10, beta in[1/200,1/20], w in[9/10,11/10], nu in[0,1/20], Omega=10, primary masses/g in[19/20,21/20], shell k in[19/50,21/50], cf>=0; reciprocal gains positive as parent",
 "initial_phase":"Reference primary/device configurations and velocities, alpha=1/10 and arbitrary 180 initial housing position/velocity phase at Eh<=3Ep_ref/80000",
 "clock":"continuous nondimensional u=t/t0; physical t0 uncalibrated",
 "target_exposure":"Original 0.1 amplitude and original E_h target known; horizon 2/5 selected after using these sufficient formulas (FIT/development horizon). No empirical data or validation set.",
 "energy_upper":str(E), "additional_initial_housing_energy_max":str(EH),
 "speed_bounds":{"primary_point_speed_lt":str(VP),"housing_point_speed_lt":str(VH),"housing_initial_speed_lt":str(V0H),"housing_initial_midpoint_offset_lt":str(D0)},
 "damping_acceleration_upper":str(FRICTION_FORCE_PER_H_MASS),
 "all_time_members_before_domain_exit":{"absolute_spoke_strain_lt":"2/5","absolute_edge_strain_lt":"3/5"},
 "strut_length_lower_at_u":{"0":str(lower_short(Q(0))),"1/10":str(lower_short(T_SWITCH)),"39/100":str(lower_long(Q(39,100))),"2/5":str(lower_long(T_CERT))},
 "all_phase_uniform_horizon":str(T_CERT),
 "all_housing_struts_length_gt_at_horizon":str(lower_long(T_CERT)),
 "all_oriented_cell_volume_ratio_between":[str(VOL_LOWER),str(VOL_UPPER)],
 "all_cell_orientation_preserved":True,
 "ode_solution_exists_through_horizon":True,
 "proof_scope":"All admitted housing initial phases and continuous qualified parameter box with nu<=1/20, including cf=0. Strict bounds for every u in[0,2/5]. Normalized lengths and volumes.",
 "comparison":"Earlier exact all-phase original pulse tube only through u=1/20 (same law, smaller E_h); new horizon is 8x. New extension does not use a Green matrix or restrict rigid momentum.",
 "not_proved":["all-time alpha=0.1 safety","u=100 nonlinear breathing >=80%","all-phase housing half-energy at u=100","actual material / clock identification","continuous full-parameter-box dynamical coherence"],
 "failure_preserved":"Original alpha=0.1 total-energy sublevel contains strut endpoint collapse witness of energy below nominal pulse; not a dynamically reached state.",
 "techniques":["exact rational inequalities","Duhamel oscillator solution and sine majorant","passivity/positive storage","3D Euclidean triangle inequality","Gram singular-value perturbation","ODE bootstrap continuation"],
 "verification":"Python Fraction assertions and independent symbolic algebra; constructor checks only, no interval ODE or empirical experiment"
}

def run(out):
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(RESULT,sort_keys=True,indent=2)+"\n")
    return RESULT

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    r=run(args.out)
    print("PASS original alpha 0.1 through u=2/5; 120 struts >",r["all_housing_struts_length_gt_at_horizon"], "all oriented cell volume ratios in",r["all_oriented_cell_volume_ratio_between"])
