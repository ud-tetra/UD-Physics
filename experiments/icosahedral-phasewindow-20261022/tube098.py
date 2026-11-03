#!/usr/bin/env python3
"""Exact Fraction verification of full phase-space finite safety at t=49/50.

This is a sufficient theorem for the previously specified UD MountLoss surrogate;
it does not execute the full 560-state ODE or prove the u=100 performance tests.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json

E_H=F(51,20000000)
A0=F(1,10)
E_MAX=F(34,5)*A0*A0+E_H
M_PRIMARY=F(19,20)
R2_UP=F(181,200)
M_HOUSING=F(9,5000)
K_HOUSING=F(9,50)
OMEGA=F(10)
NU_W_UP=F(1,18)
T=F(49,50)
PRIMARY_NORM=F(9,25)
HOUSING_SPEED=F(35,4)
HOMOGENEOUS=F(1,180)
SINE_INTEGRAL=F(79,125)
D=F(499,500)

# 25 sqrt(5)<56 proves R^2=(5+sqrt5)/8 <181/200.
assert 5*625 <56*56
assert E_MAX==F(1360051,20000000)
assert 2*E_MAX*R2_UP/M_PRIMARY<PRIMARY_NORM**2
assert 2*E_MAX/M_HOUSING<HOUSING_SPEED**2
# Positive spoke and exterior-edge potential each bounded by E.
assert 2*E_MAX<F(2,5)**2
assert 2*E_MAX/F(19,50)<F(3,5)**2
# The initial housing oscillator amplitude shares one *combined* energy budget.
# kh=m_h omega^2, so sqrt(|D|^2+(|H'(0)|/omega)^2)<=sqrt(2 E_h/kh).
assert 2*E_H/K_HOUSING<HOMOGENEOUS**2

# For x=10T=49/5, with 3*pi<x<4*pi and pi>3,
# r=x-3*pi satisfies 0<r<4/5. cos r>=1-r^2/2>=17/25.
# Therefore int_0^T |sin(10s)| ds = (6+1-cos r)/10 <=79/125.
assert OMEGA*T==F(49,5)
assert OMEGA*T-F(9)==F(4,5)  # r is STRICTLY smaller, since 3*pi>9
assert (F(6)+F(1)-(F(1)-F(4,5)**2/F(2)))/OMEGA==SINE_INTEGRAL

ACC=NU_W_UP*4*(HOUSING_SPEED+PRIMARY_NORM)
VISCOUS_ERR=ACC/OMEGA*SINE_INTEGRAL
STRUT=F(1,2)-HOMOGENEOUS-PRIMARY_NORM*T-VISCOUS_ERR
assert STRUT==F(3853,281250)>F(1,100)>0
# For opposite-face anchors, the norm of coefficients <=sqrt3 times the
# endpoint vector-velocity norm. Their initial separation is sqrt3/2;
# the same homogeneous and damper corrections enter, so endpoint dominates.
assert F(1,2)-PRIMARY_NORM*T>0

# Each oriented cell matrix has star-incidence operator norm 2 and
# sigma_min(reference)=1/sqrt2. Therefore ||Aref^-1 Delta A||<2sqrt2 vT.
SQUARED=F(8)*PRIMARY_NORM**2*T**2
assert SQUARED==F(388962,390625)<D*D<1
VOL_MIN=(1-D)**3
VOL_MAX=(1+D)**3
assert VOL_MIN==F(1,125000000)
assert VOL_MAX==F(997002999,125000000)

RESULT={
    'status':'EXACT_CONDITIONAL_FINITE_SAFETY',
    'run':'relative-tube-006',
    'source_base_revision':'127c5fb995cdd218fecc479bccec8ed7a2c2bad0',
    'source_branch_parent':'782cd7fb93e0001bd6bb159857d85e09f1fc4100',
    'model':'Unchanged original 280-coordinate 560-phase 3D passive MountLoss with 120 current-direction viscosity struts',
    'reference_Eh_bound':str(E_H),
    'initial_pulse_alpha':str(A0),
    'total_initial_energy_upper':str(E_MAX),
    'all_housing_initial_phase_dim':180,
    'coefficient_domain':'Q and Q(sqrt5) reference, continuous real dynamics',
    'qualified_box':'m,g in[19/20,21/20],k in[19/50,21/50],beta in[1/200,1/20],housing weights[9/10,11/10],Omega=10,nu in[0,1/20],cf>=0; positivity of original device parameters',
    'reference_R2_strict_upper':str(R2_UP),
    'shared_primary_velocity_norm_upper':str(PRIMARY_NORM),
    'housing_velocity_upper':str(HOUSING_SPEED),
    'housing_initial_oscillator_combined_amplitude_upper':str(HOMOGENEOUS),
    'integral_sine_abs_up_to_T_upper':str(SINE_INTEGRAL),
    'moving_axis_damping_acceleration_upper':str(ACC),
    'max_viscous_displacement_bound':str(VISCOUS_ERR),
    'time_horizon':str(T),
    'all_120_strut_length_lower':str(STRUT),
    'cell_relative_perturbation_squared_upper':str(SQUARED),
    'cell_relative_operator_upper':str(D),
    'all20_cell_orientations_positive':True,
    'oriented_volume_ratio_interval_strict':[str(VOL_MIN),str(VOL_MAX)],
    'positive_member_strut_domain_exists_through_T':True,
    'all_spoke_absolute_strains_strictly_below':'2/5',
    'all_edge_absolute_strains_strictly_below':'3/5',
    'failed_extension_T_equals_one':'The same kinetic star-incidence bound gives squared relative cell error 648/625>1 at u=1; it cannot certify cell orientation there (not a dynamical counterexample).',
    'evidence':'EXACT/CONDITIONAL mathematical proof in unchanged surrogate; not physical observation',
    'target_exposure':'Horizon 49/50 and rational majorants selected after previous 9/10 certificate and the exposed u100 target; development not independent prediction',
    'checks':'Fraction arithmetic in source; separate symbolic check of reference Gram/eigenvalues and sine identity; no full model numerical integration',
    'limitations':['No u100 nonlinear certification','No >=80% breathing RMS guarantee','No housing-energy half-life guarantee','No physical calibration/native constitutive selection','Positive cell orientation is not convexity or coherent breathing','Must preserve claim isolation and run repository validators']
}

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--out',type=Path,required=True)
    p=a.parse_args().out
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(RESULT,indent=2,sort_keys=True)+'\n')
    print('PASS: exact finite safety through',T,'struts >',STRUT,'volumes >',VOL_MIN)

if __name__=='__main__':main()
