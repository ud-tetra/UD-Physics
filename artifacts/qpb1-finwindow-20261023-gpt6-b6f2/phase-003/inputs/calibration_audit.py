#!/usr/bin/env python3
"""Short-time interferometric slope calibration: exact certificate plus probes.

Conditional 3-sector QPB model; not a hardware experiment.
"""
import argparse
import json
import math
import random
from fractions import Fraction as F
from itertools import product
from pathlib import Path

G0 = (F(1), F(1), F(3, 2))
R0 = (F(1,4), F(1,4), F(1,2))
EPS = F(1, 100)
H = F(1, 12)
E_COMPLEX = F(2, 10**6)
E_PROBE_TIME = F(1, 10**7)
E_STATE_REPEAT = F(5, 10**6)
E_GAIN_REPEAT = F(5, 10**6)
E_MAIN_TIME_READOUT = F(1, 10**5)
OMEGA_MAX = F(151, 50)
T_MAX = F(44, 7) + F(1, 100)
TRUNC = OMEGA_MAX**5 * H**4 / 480
FRINGE = 3 * (E_COMPLEX + OMEGA_MAX * E_PROBE_TIME) / H
REPEAT = 2 * OMEGA_MAX * E_STATE_REPEAT + 2 * E_GAIN_REPEAT
MAIN_CLOCK = OMEGA_MAX * E_MAIN_TIME_READOUT
KAPPA = T_MAX * (TRUNC + FRINGE + REPEAT) + MAIN_CLOCK
OLD_TOTAL = F(11101676085864605533, 1345612732743408915000)
NEW_TOTAL = OLD_TOTAL - F(1,1000) + KAPPA
assert OMEGA_MAX*H < 1
assert KAPPA < F(1,1000)
assert NEW_TOTAL < F(1,100)


def z(g, r, t):
    return sum(float(w)*complex(math.cos(2*float(x)*t),math.sin(2*float(x)*t))
               for x,w in zip(g,r))


def slope(g, r, h):
    return (z(g,r,h).imag-z(g,r,-h).imag)/(2*h)


def richardson(g, r, h):
    return (4*slope(g,r,h/2)-slope(g,r,h))/3


def oracle(g, r):
    return 2*sum(float(a*b) for a,b in zip(g,r))


def sample_case(g, r):
    h=float(H)
    s=richardson(g,r,h)
    bias=abs(s-oracle(g,r))
    assert bias<=float(TRUNC)+2e-13
    return bias

# Five deterministic gain values in three independent sectors, no zero error assumption.
gain_values=[-EPS,-EPS/2,F(0),EPS/2,EPS]
max_bias=0.0
for d in product(gain_values,repeat=3):
    g=tuple(a+b for a,b in zip(G0,d))
    max_bias=max(max_bias,sample_case(g,R0))

rng=random.Random(20261024)
max_bias_random=0.0
for _ in range(10000):
    g=tuple(a+F(str(rng.uniform(-float(EPS),float(EPS)))) for a in G0)
    weights=[rng.random() for k in range(3)]
    weights=[F(str(w/sum(weights))) for w in weights]
    weights[-1]=F(1)-sum(weights[:-1]);assert all(w>=0 for w in weights)
    max_bias_random=max(max_bias_random,sample_case(g,weights))

# Adversarial signs for the four calibration samples; each has complex error <= e.
# Four quadratures are reconstructable from ideal intensity differences.
for d in product((-float(E_COMPLEX),float(E_COMPLEX)),repeat=4):
    g=tuple(G0); r=R0; h=float(H)
    zp=z(g,r,h/2).imag+d[0]
    zm=z(g,r,-h/2).imag+d[1]
    Zp=z(g,r,h).imag+d[2]
    Zm=z(g,r,-h).imag+d[3]
    noisy=(4*((zp-zm)/h)-(Zp-Zm)/(2*h))/3
    assert abs(noisy-richardson(g,r,h))<=3*float(E_COMPLEX)/h+2e-13

# Model baseline and sensitivity if calibration is OMITTED.
T0=2*math.pi
no_cal={
    'unknown_mean_rate_uncertainty_phase_at_T0':float(2*T0*EPS),
    'untracked_main_time_jitter_phase':float(F(5,2)*F(1,100)),
}
assert no_cal['unknown_mean_rate_uncertainty_phase_at_T0']>0.1

result={
 'status':'PASS', 'evidence':['EXACT','CONDITIONAL','NUMERICAL'],
 'base':'QPB local 3-sector conserved time-independent generator',
 'estimator':'R=(4S(h/2)-S(h))/3, S(h)=[Im Z(h)-Im Z(-h)]/(2h)',
 'h_native':str(H), 'omega_max':str(OMEGA_MAX),
 'inputs':{'gain_abs_error':str(EPS),'probe_complex_noise_abs':str(E_COMPLEX),
   'probe_native_time_error':str(E_PROBE_TIME),'prep_repeat_state_norm':str(E_STATE_REPEAT),
   'gain_repeat_abs':str(E_GAIN_REPEAT),'main_native_time_metrology_error':str(E_MAIN_TIME_READOUT)},
 'conditional_bound':{'trunc_rate':str(TRUNC),'fringe_and_probe_timing_rate':str(FRINGE),
   'intershot_repeatability_rate':str(REPEAT),'main_clock_rad':str(MAIN_CLOCK),
   'kappa_phase_rad':str(KAPPA),'kappa_phase_decimal':float(KAPPA),
   'new_total_phase_rad':str(NEW_TOTAL),'new_total_phase_decimal':float(NEW_TOTAL)},
 'samples':{'five_cubed_gain_fixture':5**3,'random_gain_weight_probes':10000,
   'four_probe_sign_challenges':2**4,'max_trunc_bias_gain_grid':max_bias,
   'max_trunc_bias_random':max_bias_random},
 'untracked_baseline':no_cal,
 'validation_scope':'constructor checks; no external review; clock and phase-reference metrology assumed, not measured',
}
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--out',required=True,type=Path)
    args=p.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'kappa':float(KAPPA),'new_total':float(NEW_TOTAL),'checks':result['samples']}))
