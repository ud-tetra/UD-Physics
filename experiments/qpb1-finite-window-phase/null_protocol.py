#!/usr/bin/env python3
"""UD phase-005: synthetic reference/null channel discrimination; no hardware data."""
import argparse
import cmath
import json
import math
import random
from fractions import Fraction as F
from pathlib import Path

G0=(1.0,1.0,1.5)
B_PREV=F(534794619424186500609612131837359,65106126461057096943360000000000000)
EPS_NULL=F(1,10000)
EPS_DIFF=F(1,2000)
B_NULL=B_PREV+EPS_DIFF+EPS_NULL/(1-EPS_NULL)
assert B_NULL < F(1,100)
TAIL_BOUND=16*math.exp(-7.5)
assert TAIL_BOUND < 0.01
# Rational proof: exp(15/2) > sum_0^11 (15/2)^k/k! > 1600.
from math import factorial
assert sum(F(15,2)**k/factorial(k) for k in range(12))>1600

def wrap(x):
    return math.atan2(math.sin(x),math.cos(x))

def zmodel(g,r,t):
    return sum(w*cmath.exp(2j*a*t) for w,a in zip(r,g))

def phase(z,d):
    return wrap(cmath.phase(z)-d)

def channels(z,theta,ds,dn,es=0j,en=0j,er=0j):
    signal=z*cmath.exp(1j*(theta+ds))+es
    null=cmath.exp(1j*(theta+dn))+en
    ref=cmath.exp(1j*theta)+er
    return signal,ref,null

rng=random.Random(20261024)
scenarios=(('no_injection',0,0),('common_reference',0,0),
           ('matched_differential',0.002,0.002),
           ('bounded_mismatch',0.002,0.0025),
           ('unmatched_differential',0.002,0))
seen={name:{'n':0,'max_abs_reference_bias':0.,'max_abs_null_bias':0.,'max_abs_null_bias_with_noise':0.} for name,_,_ in scenarios}
min_vis=1.0
exact_equal=0
for name,ds,dn in scenarios:
    for _ in range(1024):
        g=tuple(a+rng.uniform(-.01,.01) for a in G0)
        r3=.5+rng.uniform(-.0005,.0005)
        r1=.25+rng.uniform(-.0001,.0001)
        r=(r1,1-r1-r3,r3)
        t=2*math.pi+rng.uniform(-.01,.01)
        z=zmodel(g,r,t)
        d=2*t*sum(a*w for a,w in zip(g,r))
        truth=phase(z,d)
        theta=(.004 if name=='common_reference' else rng.uniform(-.006,.006))
        es=.001*cmath.exp(1j*rng.uniform(-math.pi,math.pi))
        en=.0001*cmath.exp(1j*rng.uniform(-math.pi,math.pi))
        a,b,c=channels(z,theta,ds,dn)
        noisy,_,noisy_null=channels(z,theta,ds,dn,es=es,en=en)
        refbias=wrap(phase(a/b,d)-truth)
        nullbias=wrap(phase(a/c,d)-truth)
        noisybias=wrap(phase(noisy/noisy_null,d)-truth)
        assert abs(refbias-ds)<1e-12
        assert abs(nullbias-(ds-dn))<1e-12
        assert abs(noisybias)<=abs(ds-dn)+(.001/(abs(z)-.001))+(.0001/(1-.0001))+1e-12
        # Standard three-frequency (non-UD) baseline gives identical complex
        # observables with the same frequencies, weights, and noise law.
        conventional=sum(w*cmath.exp(1j*(2*a)*t) for w,a in zip(r,g))
        assert z==conventional
        exact_equal+=1
        min_vis=min(min_vis,abs(z))
        row=seen[name]
        row['n']+=1
        for key,value in [('max_abs_reference_bias',refbias),('max_abs_null_bias',nullbias),('max_abs_null_bias_with_noise',noisybias)]:
            row[key]=max(row[key],abs(value))
assert exact_equal==5120 and min_vis>.99
assert seen['common_reference']['max_abs_null_bias']<1e-12
assert abs(seen['matched_differential']['max_abs_reference_bias']-.002)<1e-12
assert seen['matched_differential']['max_abs_null_bias']<1e-12
assert abs(seen['unmatched_differential']['max_abs_null_bias']-.002)<1e-12

result={
 'status':'PASS','labels':['EXACT','CONDITIONAL','NUMERICAL','FAILED','OPEN'],
 'reference':'ud-tetra/UD-Physics:phase-004 at commit 63c4f997b68563460b54af73b04105b3f15ab687',
 'design':'Randomized common-frame and differential phase injections on three channels: signal, independent phase reference, path-matched bypass/null',
 'observables':'S=Z exp(i(theta+delta_signal)); R=exp(i theta); N=exp(i(theta+delta_null))',
 'estimators':{'reference_only':'Arg(S/R)-D', 'path_null':'Arg(S/N)-D', 'control':'Arg(N/R)'},
 'exact_certificate':{
   'previous_combined_budget':str(B_PREV),'assumed_null_complex_error':str(EPS_NULL),
   'assumed_untracked_signal_null_differential_max':str(EPS_DIFF),
   'new_combined_budget':str(B_NULL),'new_budget_decimal':float(B_NULL),
   'remaining_screen_margin_decimal':float(F(1,100)-B_NULL),
   'monitor_sample_count_sufficient_under_iid_Bernoulli':24_000_000_000,
   'monitor_joint_failure_bound':TAIL_BOUND,
   'monitor_event_count_details':'two monitor channels x four phase settings x 3e9 trials each, 99% simultaneous complex-error <=1e-4; 16 exp(-7.5)<.01',
   'visibility_phase_invariance':'common theta cancels in S/N and S/R; differential delta_signal-delta_null survives S/N',
   'null_identifiability':'without independent bound on delta_signal-delta_null, extra physical phase and unmatched optical drift are observationally equivalent',
   'three_tone_identifiability':'conventional three-frequency model with omega_k=2g_k and weights r_k reproduces Z(t) identically for all t; model families observationally identical under same noise/controls'},
 'numerical':{'seed':20261024,'scenarios':seen,'total_trajectories':exact_equal,'minimum_visibility':min_vis,'conventional_baseline_equal_checks':exact_equal},
 'failure_case':'delta_signal=0.002,delta_null=0,reference theta arbitrary: path-null estimator retains exactly 0.002 rad bias despite matching fringe visibility',
 'scope':'synthetic design and conditional mathematical receiver; no lab acquisition, measured photon rates, native physical time, or independent physics test'
}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'samples':exact_equal,'budget':float(B_NULL),'tail':TAIL_BOUND,'min_visibility':min_vis},sort_keys=True))
