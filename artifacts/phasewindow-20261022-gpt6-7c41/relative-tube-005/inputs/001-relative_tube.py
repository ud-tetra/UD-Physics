#!/usr/bin/env python3
"""Exact conditional all-180-phase safety of original-alpha UD 3D model to u=9/10.

Source: unchanged MountLoss mechanics from ud-tetra/UD-Physics at
2b133c7889cde7aae9127d0c0fa2036c278884a9 (also earlier models).
All consequential numeric comparisons in this program are Fraction-exact.
The sine integral lemma is proved in PROOF.md (not by numerical grid).
"""
import argparse, json
from fractions import Fraction as F
from pathlib import Path

SOURCE_MAIN='2b133c7889cde7aae9127d0c0fa2036c278884a9'
PARENT_BRANCH='43412f65f5e64ec49223b1c713fb1649af3b29ba'
A0=F(1,10)
EH=F(51,20000000)
E=F(34,5)*A0**2+EH
MP_MIN=F(19,20)
MH_MIN=F(9,5000)
KH_MIN=F(9,50)
KE_MIN=F(19,50)
OMEGA=F(10)
NU_OVER_W_MAX=F(1,18)
VP_COARSE=F(2,5)
VH=F(9)
U0=F(3,50)
D0=F(1,180)
V=F(19,50)
COMBINED_INIT=F(41,5000)
T=F(9,10)

# Positive total energy, positive masses/mount stiffness, all phases.
assert E==F(1360051,20000000)
assert 2*E < MP_MIN*V**2
assert 2*E < MH_MIN*VH**2
assert 2*EH < MH_MIN*U0**2
assert 2*EH < KH_MIN*D0**2
assert 2*E < F(2,5)**2
assert 2*E < KE_MIN*F(3,5)**2
assert D0**2+(U0/OMEGA)**2 < COMBINED_INIT**2

# Moving-axis passive viscous force on a housing; four anchors. The bound
# is on (acceleration) |Fh|, and uses no fixed-direction assumption.
ACC=NU_OVER_W_MAX*4*(VH+VP_COARSE)
assert ACC==F(94,45)

# Exact trigonometric lemma: int_0^t |sin(10s)| ds <= (3/4)t.
# PROOF.md establishes it for all t>=0 by a one-period inequality,
# rational Taylor/tangent checks, and period decomposition.
# These rational comparisons certify the algebraic components:
assert F(4,5)-F(9,64)+(F(8,5)**5)/720 < F(3,4)
assert F(3,2)+F(13,15)*F(43,75)<F(2)
assert F(7,6)<F(6,5)
assert F(2) < F(3,4)*F(3) # Full sine periods (pi > 3).

# Green/Duhamel relative endpoint velocity coefficients:
# (1-cos theta)*A'_e-X'_i = -(1+cos theta)/2*X'_i
#                            +(1-cos theta)/2*X'_j,
# whose Euclidean coefficient norm = sqrt((1+cos(theta)^2)/2) <=1.
# Total PRIMARY kinetic energy 1/2*sum mp_i*|X'_i|^2 <= E
# makes the integrand <=sqrt(2E/mp_min)<V.
# For opposite-face anchor k the coefficient norm is
# sqrt(1+(1-cos(theta))^2/2)<=sqrt3. The reference distance
# from midpoint to endpoint is 1/2, to opposite face is sqrt3/2.
# Since the common additive terms B>=0 and the endpoint lower
# is positive, the opposite-face bound is strictly larger.
MAX_RAYLEIGH_ACCEL_CONTR=ACC/OMEGA*F(3,4)
assert MAX_RAYLEIGH_ACCEL_CONTR==F(47,300)
STRUT_LOWER=F(1,2)-COMBINED_INIT-(V+MAX_RAYLEIGH_ACCEL_CONTR)*T
assert STRUT_LOWER==F(11,1250)>0

# Star-incidence difference matrix [Xa-Xc,Xb-Xc,Xd-Xc] has norm 2.
# Therefore ||A'(t)||_F <= 2 sqrt(sum |X'_k|^2) < 2 V.
# Reference sigma_min(A_ref)=1/sqrt(2), hence
# ||A_ref^{-1}(A-A_ref)||_2 < 2 sqrt(2) V t.
# At t=T this is strictly < 97/100, by rational squaring.
DELTA2=F(2)*(F(2)*V*T)**2
D=F(97,100)
assert DELTA2<D**2 and D<1
VOL_LOW=(1-D)**3
VOL_HIGH=(1+D)**3
assert VOL_LOW==F(27,1000000)
assert VOL_HIGH==F(7645373,1000000)

RESULT={
 'status':'EXACT_CONDITIONAL_FINITE_TUBE',
 'source_main_revision':SOURCE_MAIN,
 'phase_branch_parent':PARENT_BRANCH,
 'question':'Original amplitude alpha=1/10, every allowed 180 housing phase, 3D nonlinear MountLoss: positive struts and cell orientations through u=9/10?',
 'model':'Unchanged 280-coordinate 560-phase 3D passive MountLoss; 120 moving central viscosity paths and 30 housings, reciprocal force and torque',
 'initial_conditions':'alpha0=1/10; primary and device states at reference/rest; any 180-coordinate housing displacement and velocity phase with Eh<=51/20000000',
 'qualified_parameter_box':'g,m in[19/20,21/20], k in[19/50,21/50], beta in[1/200,1/20], weights in[9/10,11/10] mean1, Omega=10, nu in[0,1/20], cf>=0, positive existing device settings and gains',
 'clock':'continuous dimensionless u, t0 not physically calibrated',
 'evidence':'EXACT / CONDITIONAL; no physical model identification; no ODE simulation needed for proof',
 'total_initial_energy_upper':str(E),
 'initial_housing_energy_upper':str(EH),
 'primary_velocity_Euclidean_upper':str(V),
 'housing_velocity_upper':str(VH),
 'housing_initial_velocity_upper':str(U0),
 'housing_initial_offset_upper':str(D0),
 'initial_oscillator_amplitude_upper':str(COMBINED_INIT),
 'moving_axis_viscous_acceleration_upper':str(ACC),
 'sin_absolute_average_global_upper':'3/4',
 'source_of_method':'Direct anchor-relative oscillator/Duhamel identity and kinetic-energy matrix-operator bound, rather than independent absolute primary and housing motions.',
 'all_phase_uniform_time_horizon':str(T),
 'all_120_housing_struts_strictly_gt':str(STRUT_LOWER),
 'all_spoke_strains_absolute_lt':'2/5',
 'all_edge_strains_absolute_lt':'3/5',
 'cell_relative_matrix_perturbation_strictly_lt':str(D),
 'all_20_oriented_cell_volume_ratios_strict_bounds':[str(VOL_LOW),str(VOL_HIGH)],
 'orientation_preserved':True,
 'global_solution_existence_through_horizon':True,
 'techniques':['exact integer/fraction inequalities','total primary kinetic energy norm','exact moving-midpoint Duhamel identity','global sine absolute-average inequality','operator-norm star-incidence bound','positive energy/passivity','ODE continuation'],
 'provenance_and_target_exposure':'Same previously exposed original amplitude and energy allowance; rational horizon 9/10 selected after deriving sufficient majorant (FIT/development), not an independent physical prediction.',
 'limitations':['All-time u100 nonlinear pulse, 80% breathing RMS, 5% volume mismatch, 50% housing energy ringdown remain OPEN','Time horizon is a conservative proof limit, not an observed collapse threshold','No hardware realization or physical clock/energy calibration','No interval ODE or independent physical replication'],
 'earlier':'Original 1/20 then 2/5 exact safety horizons; this extends to 9/10, an 18-fold improvement against original 1/20.',
 'strictness':'At t=0 actual normalized cell ratio is 1, strictly between fixed endpoints; all derived bounds are strict across the closed time interval.'
}

def main(out):
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(RESULT,indent=2,sort_keys=True)+'\n')
    print('PASS exact all-phase original pulse through',T,'struts >',STRUT_LOWER,'cell ratios in',VOL_LOW,VOL_HIGH)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();main(a.out)
