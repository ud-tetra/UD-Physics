#!/usr/bin/env python3
"""Exact SI charge/flux anchors vs noncompact tetrahedral LC phase map.

BIPM h and e are externally defined; native q0 and phase period are NOT.
All fitted/example coefficient choices are labeled model design, not data.
"""
import argparse
import json
import math
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path

h = Q(Decimal('6.62607015e-34'))
e = Q(Decimal('1.602176634e-19'))
phi0 = h / (2*e)
assert 2*e*phi0 == h

def rational_text(q):
    return str(q)

# q0=n*e and a proposed native period delta_alpha=2*pi*m.
# Phi=(A0/q0)*alpha and Phi0=h/(2e) then
# A0/hbar = n/(2*m).  This is a POSTULATED native phase map.
anchors=[]
for n,m in [(Q(2),Q(1)),(Q(1),Q(1)),(Q(2),Q(2)),(Q(2),Q(1,2)),(Q(4),Q(1))]:
    action_ratio = n/(2*m)
    assert 2*m*action_ratio/n == 1
    anchors.append({'q0_over_e':str(n),'native_delta_alpha_over_2pi':str(m),
                    'implied_A0_over_hbar_IF_PHASE_MAP_ASSUMED':str(action_ratio)})
assert anchors[0]['implied_A0_over_hbar_IF_PHASE_MAP_ASSUMED']=='1'
assert len(set(r['implied_A0_over_hbar_IF_PHASE_MAP_ASSUMED'] for r in anchors))>1

# Once q0=2e, native alpha=Josephson phase and A0=hbar are IMPOSED,
# the noncompact quadratic native oscillator maps to ordinary LC:
# E_C=hbar*uT/(8*tau), E_J=4*hbar*v/tau and omega0=2sqrt(uT*v)/tau.
# Check identity using exact dimensionless scaled coefficients uT,v,tau.
LC=[]
for ut,v,tau in [(Q(1),Q(1),Q(1)),(Q(2),Q(1,2),Q(3,2)),
                 (Q(3,4),Q(4,3),Q(7,5)),(Q(1,3),Q(3),Q(2))]:
    EC_over_hbar=ut/(8*tau)
    EJ_over_hbar=4*v/tau
    omega_squared=8*EC_over_hbar*EJ_over_hbar
    assert omega_squared==4*ut*v/tau**2
    LC.append({'uT':str(ut),'v':str(v),'tau_seconds_per_native_unit':str(tau),
               'EC_over_hbar_per_second':str(EC_over_hbar),
               'EJ_over_hbar_per_second':str(EJ_over_hbar),
               'omega0_squared_per_second2':str(omega_squared)})

# Noncompact source potential V/Escale=2v*alpha^2:
# exactly fails periodic descent alpha~alpha+2*pi for v>0;
# at alpha=0, V(alpha+2*pi)-V(alpha)=8*pi^2*v>0.
# Replacing with a periodic Josephson potential is an additional law.
# Even with fixed curvature K and exact physical q0/Phi0, the following
# positive periodic conventional family has freely varying nonlinearity:
# V_lambda=K/(1+4lambda)*[(1-cos alpha)+lambda*(1-cos 2alpha)].
# Curvature at origin V''(0)=K for ALL lambda>=0, while quartic and
# small-amplitude frequency shifts vary with lambda.
periodic=[]
for lam in [Q(0),Q(1,16),Q(1,8),Q(1,4),Q(1,2)]:
    normalized_first_harmonic=Q(1)/(1+4*lam)
    normalized_second_harmonic=lam/(1+4*lam)
    curvature=normalized_first_harmonic+4*normalized_second_harmonic
    fourth_derivative_over_curvature=-(1+16*lam)/(1+4*lam)
    amplitude_frequency_a2=fourth_derivative_over_curvature/16
    assert curvature==1
    periodic.append({'lambda':str(lam),
        'EJ1_over_fixed_curvature':str(normalized_first_harmonic),
        'EJ2_over_fixed_curvature':str(normalized_second_harmonic),
        'curvature_over_K':str(curvature),
        'quartic_fourth_derivative_over_K':str(fourth_derivative_over_curvature),
        'omega_over_omega0_a_squared_coefficient':str(amplitude_frequency_a2)})
assert periodic[0]['omega_over_omega0_a_squared_coefficient']=='-1/16'
assert periodic[-1]['omega_over_omega0_a_squared_coefficient']=='-3/16'

# Anchor-free physical calibration leaves the exact vector-001 h scale orbit.
# With q0, tau and physical Cinv,Linv fixed, U->sU, v->v/s,
# a->sa, A0->A0/s gives the same physical states. Numeric rationals merely
# check the general symbolic identities: s*(A0/s)=A0,
# (v/s)/(A0/s)=v/A0.
rescale=[]
for s in [Q(1,5),Q(1,2),Q(1),Q(2),Q(5)]:
    A0,ut,v,a = Q(7,3), Q(3,5),Q(5,3),Q(11,7)
    assert (A0/s)*(ut*s)==A0*ut
    assert (v/s)/(A0/s)==v/A0
    assert (A0/s)*(a*s)==A0*a
    rescale.append(str(s))

out={
 'status':'PASS', 'labels':['EXACT','CONDITIONAL','HYPOTHESIS','FIT','FAILED','OPEN'],
 'primary_sources':['https://www.bipm.org/en/measurement-units/si-defining-constants',
                    'https://www.nist.gov/ctl/rf-technology-division/superconductive-electronics-group/quantum-locking-ranges'],
 'exact_SI':{'h_Js':str(h),'e_C':str(e),'superconducting_flux_quantum_h_over_2e_Wb':str(phi0)},
 'scenario_anchor_dictionary':'q0=n*e; delta_alpha=2*pi*m; physical Phi=A0*alpha/q0; imposed flux period Phi0 then A0/hbar=n/(2*m)',
 'anchor_scenarios':anchors,
 'source_status':'Integrated K4 charge-field native a is NONCOMPACT and no alpha phase periodicity or quantum charge q0 is source-selected',
 'conditional_Josephson_import':'Choosing q0=2e, delta_alpha=2*pi and identifying native alpha with Josephson phase yields A0=hbar by definitions, not independent UD derivation',
 'LC_quadratic_dictionary':'under conditional Josephson mapping EC/hbar=uT/(8*tau), EJ/hbar=4*v/tau, omega0^2=8EC EJ/hbar^2=4uT*v/tau^2',
 'LC_exact_fixtures':LC,
 'compactness_failure':'Native positive quadratic cycle V=2v*alpha^2 is not periodic: V(alpha+2*pi)-V(alpha)=8*pi*v*alpha+8*pi^2*v; cannot descend to compact 2*pi phase',
 'periodic_family':'K/(1+4lambda)*[(1-cos alpha)+lambda*(1-cos 2alpha)], lambda>=0, fixed zero-phase curvature K, arbitrary higher harmonics',
 'periodic_examples':periodic,
 'native_scale_rescaling_samples':rescale,
 'native_scale_rescaling':'Without a native phase-period postulate, (U,v,a,A0,psi)->(sU,v/s,s*a,A0/s,s*psi) preserves all physical LC ports even when e,h,Phi0 are known',
 'standard_null':'ordinary superconducting Josephson/LC circuit with physical e,h and externally measured EJm and EC already gives exactly the conditional map',
 'independent_UD_prediction':'NONE: native phase period, charge unit, physical action and anharmonic higher harmonic coefficients not source-selected',
 'empirical_data':'NONE; BIPM exact constants and NIST Josephson law are external source anchors, not a new device measurement'
}
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','anchors':len(anchors),'LC_cases':len(LC),
                      'periodic_cases':len(periodic),'rescalings':len(rescale)},sort_keys=True))
