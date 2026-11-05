#!/usr/bin/env python3
"""v0.6: bounded affine channel calibration and event-anchored startup latch."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import product
from math import factorial
from pathlib import Path

p=Path(__file__).with_name('two_readout.py')
spec=importlib.util.spec_from_file_location('pair',p)
pair=importlib.util.module_from_spec(spec);spec.loader.exec_module(pair)
MAX_PHASE_STEP=Q(1,1000)

def calibration_bounds(epsilon,r,D,gamma_w,gamma_y,beta_w,beta_y,eta):
    values=(epsilon,r,D,gamma_w,gamma_y,beta_w,beta_y,eta)
    if any(not isinstance(x,Q) for x in values):
        raise TypeError('bounds must be fractions.Fraction')
    if any(x<0 for x in values):
        raise ValueError('bounds must be nonnegative')
    dyn=Q(91,2)*epsilon+Q(17,2)*r+3*D
    ew=gamma_w/4+(1+gamma_w)*dyn+beta_w+eta
    ey=gamma_y+(1+gamma_y)*dyn+beta_y+eta
    return ew,ey,dyn

class StartupLatch:
    """Step bounds/event anchor are externally certified, not inferred by this code."""
    def __init__(self,*,bounds):
        self.ew,self.ey,self.dyn=calibration_bounds(*bounds)
        if max(self.ew,self.ey)>pair.DELTA:
            raise ValueError('calibration/data budget exceeds per-channel certificate')
        self.status='NEEDS_EVENT'
        self.receipt=None
        self.samples=0

    def reset_at_event(self,w,y,receipt):
        if self.status!='NEEDS_EVENT':
            raise ValueError('one latch instance permits only one event anchor')
        if not isinstance(w,Q) or not isinstance(y,Q):
            raise TypeError('readings must be fractions.Fraction')
        if not isinstance(receipt,str) or not receipt:
            raise ValueError('event receipt identifier required')
        self.receipt=receipt
        if abs(w+Q(1,4))>pair.DELTA or abs(y)>pair.DELTA:
            self.status='INVALID_EVENT_ENVELOPE'
        else:
            self.status='ARMED'
        return self.status

    def observe(self,w,y,phase_step_bound):
        if self.status!='ARMED':
            return self.status
        if not isinstance(phase_step_bound,Q):
            raise TypeError('phase increment bound must be fractions.Fraction')
        if not Q(0)<=phase_step_bound<=MAX_PHASE_STEP:
            self.status='UNREGISTERED_STEP'
            return self.status
        if not isinstance(w,Q) or not isinstance(y,Q):
            raise TypeError('readings must be fractions.Fraction')
        self.samples+=1
        if y<pair.REFERENCE_WINDOW[0]:
            return 'WAITING'
        if y>pair.REFERENCE_WINDOW[1]:
            self.status='OVERSHOOT'
            return self.status
        self.status=pair.pair_classify(w,y,startup_registered=True)
        return self.status

def audit():
    delta=pair.DELTA;a,b=pair.REFERENCE_WINDOW
    # Inductive phase envelope before first observed reference crossing.
    assert a+delta+MAX_PHASE_STEP<Q(1,10)
    assert a+2*delta+2*MAX_PHASE_STEP<b
    assert delta<a
    example=(Q(1,10**9),Q(1,10**9),Q(1,10**8),
             Q(1,2000000),Q(1,2000000),Q(1,8000000),
             Q(1,8000000),Q(1,4000000))
    ew,ey,dyn=calibration_bounds(*example)
    assert dyn==Q(21,250000000)
    assert ew<=delta and ey<=delta
    assert ew==Q(292000021,500000000000000)
    assert ey==Q(479500021,500000000000000)
    # Test streams start at event phase zero. Only normalized phase increments,
    # not absolute time durations, are supplied to the latch.
    tail=Q(5,2)*Q(1,10)**13/factorial(13) # phase <=1/50
    assert tail<dyn
    streams=0;observations=0;max_samples=0
    for label,freq in [('FULL',5),('PROJECTED',3)]:
        for h in (MAX_PHASE_STEP,MAX_PHASE_STEP/2,MAX_PHASE_STEP/4):
            for signs in product((-1,1),repeat=6):
                gw,gy,bw,by,sw,sy=signs
                def measured(u):
                    w=-Q(1,4)*pair.cos_poly(freq,u)
                    y=pair.reference_poly(u)
                    # Choose extrema of gain, offset, dynamic error and noise.
                    # Reserve the nominal Taylor radius inside dynamic-error allowance.
                    wm=(1+gw*example[3])*(w+sw*(dyn-tail))+bw*example[5]+sw*example[7]
                    ym=(1+gy*example[4])*(y+sy*(dyn-tail))+by*example[6]+sy*example[7]
                    return wm,ym
                latch=StartupLatch(bounds=example)
                assert latch.reset_at_event(*measured(Q(0)),receipt='synthetic-event')=='ARMED'
                u=Q(0)
                for j in range(1,201):
                    # Includes pauses and variable scalar rates.
                    du=(Q(0),h/4,h/2,h)[j%4]
                    u+=du
                    assert u<Q(1,50)
                    outcome=latch.observe(*measured(u),phase_step_bound=h)
                    observations+=1
                    if outcome!='WAITING':
                        assert outcome==label
                        assert latch.observe(Q(100),Q(100),Q(100))==label # terminal latch
                        max_samples=max(max_samples,j)
                        streams+=1
                        break
                else:
                    raise AssertionError('advancing stream never reached admission')
    assert streams==384
    latch=StartupLatch(bounds=example)
    assert latch.observe(Q(0),Q(0),MAX_PHASE_STEP)=='NEEDS_EVENT'
    assert latch.reset_at_event(Q(-1,4),Q(0),'sample-event')=='ARMED'
    assert latch.observe(Q(-1,4),Q(0),MAX_PHASE_STEP+Q(1,10**9))=='UNREGISTERED_STEP'
    assert latch.observe(Q(-1,4),a,MAX_PHASE_STEP)=='UNREGISTERED_STEP'
    invalid=list(example);invalid[3]=Q(1)
    try: StartupLatch(bounds=tuple(invalid))
    except ValueError: pass
    else: raise AssertionError('over-budget gain accepted')
    result={
      'version':'v0.6','evidence':'EXACT_CONDITIONAL','physical_promotion':0,
      'source_commit':'9c3a12e0ce7d7d1662040b89a990349aa9ce2f97',
      'measurement_model':'w_m=(1+gW)*(W+eW)+bW+nW; y_m=(1+gY)*(Y+eY)+bY+nY',
      'dynamic_bound':'d=(91/2)epsilon+(17/2)r+3D',
      'per_channel_bounds':['gammaW/4+(1+gammaW)d+betaW+eta<=1/1000000',
                            'gammaY+(1+gammaY)d+betaY+eta<=1/1000000'],
      'phase_increment_upper_bound':str(MAX_PHASE_STEP),
      'startup_protocol':'event phase reset; first observed Y>=1/100; latched once; no rearming',
      'startup_induction_envelope':str(a+delta+MAX_PHASE_STEP),
      'first_crossing_observation_upper_bound':str(a+2*delta+2*MAX_PHASE_STEP),
      'example':dict(zip(['epsilon','r','D','gammaW','gammaY','betaW','betaY','eta'],map(str,example))),
      'example_dynamic_bound':str(dyn),
      'example_channel_errors':{'W':str(ew),'Y':str(ey)},
      'adversarial_streams':streams,'tested_observations':observations,
      'maximum_samples_before_latch_in_tests':max_samples,
      'exact_no_go':'finite reference snapshots with unbounded phase jumps cannot rule out hidden complete cycles',
      'limitations':['event anchor and phase-step certificates externally supplied',
         'no physical measurement of gains or offsets; bounds are conditional',
         'no liveness guarantee if scalar phase stalls forever',
         'relative channel timing, cross-talk, metric and event-map errors not separately estimated']}
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    audit()
