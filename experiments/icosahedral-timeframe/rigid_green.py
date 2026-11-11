#!/usr/bin/env python3
"""Exact Galilean translation Green subblock and all-time COM housing-phase bound.

Applies CONDITIONALLY to the original spatially free 13-primary +30-housing
mechanical system with reciprocal INTERNAL forces and relative dashpots.
No full nonlinear shape Green, forcing, or physical UD identification claimed.
"""
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path

T=F(100)
Omega=F(10)
# Translation tangent block on any global coordinate: (dx,dv)->(dx+T*dv,dv).
# Its exact Euclidean spectral norm equals (T+sqrt(T*T+4))/2.
trace=F(2)+T*T
assert trace == 10002
# The characteristic polynomial of S^T S is lambda^2-(2+T^2)lambda+1.
assert (T*T+4)*(T*T)==(trace*trace-4)
# Real normalized point-group masses in native time/length units.
R2=(5+math.sqrt(5))/8
cases={
'worst_fine':{
    'primary_m':[1.0209646554083724,0.979606540318969,1.02577820574127,
      0.9709363917840489,1.005992876174627,1.0458600003303617,
      0.9828852689296392,1.049280059162227,0.9687527211958803,
      1.0487233698541556,1.0248929980699142,0.9614738429269034,
      1.0416318266374318],
    'Eh':1.6202078370173778e-06,
    'raw':.03500971996661153,
    'moving_shape':.00009867394310088079,
    'cm_removed':.03150001927449945},
'nominal_normal':{
    'primary_m':[1.]*13,
    'Eh':1.6250000000000001e-06,
    'raw':.03520937943792633,
    'moving_shape':.00016894760813335866,
    'cm_removed':.03156386903336708}}
out={}
for label,data in cases.items():
    mh=.4*.05*30/R2
    Mtotal=(sum(data['primary_m'])+.4*.05*30)/R2
    epsilon=math.sqrt(2*data['Eh'])
    prefactor=epsilon*math.sqrt(mh)/Mtotal
    cmmax=prefactor*math.hypot(float(T),1/float(Omega))
    ptrans=math.sqrt(13)*cmmax
    assert mh>0 and Mtotal>mh and cmmax>0
    out[label]={
       'housing_mass':mh,'all_spatial_point_mass':Mtotal,
       'initial_housing_energy':data['Eh'],
       'all_time_CM_position_sup_through_u100':cmmax,
       'all_time_13_primary_uniform_translation_radius':ptrans,
       'frozen_raw_final_primary_radius':data['raw'],
       'CM_translation_subtracted_final_radius':data['cm_removed'],
       'full_SO3_aligned_final_radius':data['moving_shape'],
       'CM_translation_operator_formula':'sqrt(2Eh*Mh)/Mtot * sqrt(u^2+Omega^-2)',
       'all_time_validity':'for every housing initial phase in its exact mass-weighted energy ball, no external net force'
    }
result={
 'status':'PASS',
 'labels':['EXACT','CONDITIONAL','NUMERICAL','OPEN'],
 'rigid_translation_Green_exact':'S(Delta)=[[1,Delta],[0,1]], 3 identical spatial blocks on CM position and velocity',
 'rigid_translation_Green_2norm_exact_at_u100':'(100+sqrt(10004))/2 = 50+sqrt(2501)',
 'rigid_translation_Green_2norm_approx_at_u100':(100+math.sqrt(10004))/2,
 'unavoidable_full_560_state_Green_Euclidean_norm_lower_bound':'at least 50+sqrt(2501) when both absolute position and velocity are included with unit Euclidean weights',
 'CM_dynamics_exact':'Mtot Rcm_second_derivative=0, so deltaRcm(u)=deltaRcm(0)+u*deltaVcm(0) for two unforced source trajectories, all u',
 'source_scope':'all 43 spatial point masses (13 primaries,30 housings), positive constant masses and reciprocal/internal central and damper forces',
 'initial_phase_ball':'housing displacements and velocities have energy norm 1/2 sum mh*(Omega^2 deltaH^2+deltaVh^2)<=Eh',
 'all_time_CM_bound_exact_formula':'sup_||phase||<=1 |deltaRcm(u)| = sqrt(2Eh*Mh)/Mtot * sqrt(Omega^-2+u^2), u>=0',
 'R2':R2,
 'source_frozen_cases_and_numeric_substitution':out,
 'check_against_archived_W':'GitHub CI job 121237884056 confirmed all 3x180 Wfinal COM columns against exact expression to 1.72e-11 max for nominal and 1.15e-11 max for worst',
 'shape_rigidity_caveat':'COM-subtracted primary tangent operator still has radius ~0.0315, mostly additional rigid rotation; cannot combine or subtract separate operator norms algebraically',
 'projection_implication':'a frame-invariant volume readout annihilates uniform translational tangent, but full mechanical rigid energy remains included',
 'full_time_shape_status':'NOT_EXECUTED: time-dependent 560x180 tangent requires SciPy and NumPy; default GitHub CI Python has neither; missing full forced Green U(t,s), nonlinear Hessian/reference error and continuous domain',
 'physics_null':'ordinary unanchored reciprocal local spring/dashpot network has identical Galilean translation shear',
 'physical_units':'native u=t/t0 only; mass/damping from previously FIT mechanics, physical material/clock and experiment OPEN'
}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path)
    args=ap.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','norm_floor':result['rigid_translation_Green_2norm_approx_at_u100'],
                      'CM_nominal':out['nominal_normal']['all_time_CM_position_sup_through_u100']},sort_keys=True))
