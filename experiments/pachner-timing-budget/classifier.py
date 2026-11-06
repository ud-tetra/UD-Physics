#!/usr/bin/env python3
"""Finite rational classifier v0.3 for the declared all-active apex probe."""
import importlib.util
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

WINDOW=(Q(1,240),Q(1,120))
COEFF={
    'FULL':(Q(-1,4),Q(0),Q(5,8),Q(0),Q(-25,96)),
    'PROJECTED':(Q(-1,4),Q(0),Q(3,8),Q(0),Q(-3,32))}
BUDGET=Q(1,1000000)
REMAINDER=Q(1,382205952)

def check_time(s):
    if not isinstance(s,Q):
        raise TypeError('sample time must be fractions.Fraction')
    if not WINDOW[0]<=s<=WINDOW[1]:
        raise ValueError('sample time outside certified window')

def polynomial(coeff,s):
    value=Q(0)
    for c in reversed(coeff):
        value=value*s+c
    return value

def prediction_intervals(s):
    """Nominal exact-model prediction enclosures; exclude preparation/readout errors."""
    check_time(s)
    return {name:(polynomial(c,s)-REMAINDER,polynomial(c,s)+REMAINDER)
            for name,c in COEFF.items()}

def threshold(s):
    check_time(s)
    return Q(-1,4)+s*s/2-Q(17,96)*s**4

def classify(s,reading):
    """Guarantee only under v0.2 preparation, generator, clock and error assumptions."""
    check_time(s)
    if not isinstance(reading,Q):
        raise TypeError('reading must be fractions.Fraction')
    delta=reading-threshold(s)
    if delta>0:
        return 'FULL'
    if delta<0:
        return 'PROJECTED'
    return 'INDETERMINATE'

def certified_classify(s,reading,epsilon,r,nu,eta):
    """Check declared bounds; their validity remains the caller's responsibility."""
    errors=(epsilon,r,nu,eta)
    if any(not isinstance(x,Q) for x in errors):
        raise TypeError('error bounds must be fractions.Fraction')
    if any(x<0 for x in errors):
        raise ValueError('error bounds must be nonnegative')
    if sum(a*b for a,b in zip((78,15,13,1),errors))>BUDGET:
        raise ValueError('declared error budget exceeds certificate')
    return classify(s,reading)

def forward_coeff(A,v,l,degree,mvec):
    out=[]
    for k in range(degree+1):
        out.append(sum(x*y for x,y in zip(l,v))/factorial(k))
        v=mvec(A,v)
    return out

def dual_coeff(A,v,l,degree):
    # Separate scalar-derivative algorithm: propagate the readout row, not the state.
    out=[]
    for k in range(degree+1):
        out.append(sum(x*y for x,y in zip(l,v))/factorial(k))
        l=[sum(l[i]*A[i][j] for i in range(len(A))) for j in range(len(A))]
    return out

def audit():
    p=Path(__file__).with_name('audit.py')
    spec=importlib.util.spec_from_file_location('timing',p)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    d=a.main(return_setup=True)
    c=d['c'][:];c[3]+=Q(1,4)
    z=a.lin.mvec(d['M'],c)
    lf=[Q(int(i==4)-int(i==3)) for i in range(len(z))]
    lp=[d['M'][4][j]-d['M'][3][j] for j in range(23)]
    coeff8={}
    for name,A,v,l in [('FULL',d['An'],z,lf),('PROJECTED',d['K0'],c,lp)]:
        f=forward_coeff(A,v,l,8,a.lin.mvec)
        b=dual_coeff(A,v,l,8)
        assert f==b
        assert tuple(f[:5])==COEFF[name]
        coeff8[name]=b
    # Integral Taylor remainder: no floating point or exp() estimate.
    assert Q(5,2)**2>2*Q(237,80)
    assert REMAINDER==Q(5,2)*Q(1,24)**5/factorial(5)
    coarse3=Q(5,2)*Q(1,24)**4/factorial(4)
    half_gap=Q(1,921600)
    assert coarse3+BUDGET>half_gap
    assert REMAINDER+BUDGET<half_gap
    slack=half_gap-BUDGET-REMAINDER
    assert slack==Q(492407,5971968000000)>Q(1,13000000)
    radius8=Q(5,2)*Q(1,24)**9/factorial(9)
    checks=0
    for k in range(257):
        s=WINDOW[0]+(WINDOW[1]-WINDOW[0])*Q(k,256)
        interval=prediction_intervals(s)
        assert threshold(s)==sum(polynomial(c,s) for c in COEFF.values())/2
        for name in COEFF:
            center=polynomial(coeff8[name],s)
            lo,hi=interval[name]
            assert lo<=center-radius8<=center+radius8<=hi
            # Entire certified noisy enclosure classified correctly by monotonicity.
            for y in (lo-BUDGET,hi+BUDGET):
                assert classify(s,y)==name
                checks+=1
        assert classify(s,threshold(s))=='INDETERMINATE'
    for s in (Q(0),WINDOW[0]-Q(1,10**8),WINDOW[1]+Q(1,10**8)):
        try: classify(s,Q(0))
        except ValueError: pass
        else: raise AssertionError('out-of-window time accepted')
    for s,y in [(0.005,Q(0)),(WINDOW[0],0.0)]:
        try: classify(s,y)
        except TypeError: pass
        else: raise AssertionError('floating input accepted without explicit quantization')
    example=(Q(1,200000000),Q(1,100000000),Q(1,100000000),Q(1,4000000))
    s=WINDOW[0]
    assert certified_classify(s,polynomial(COEFF['FULL'],s),*example)=='FULL'
    for errors in [(Q(-1),Q(0),Q(0),Q(0)),(Q(0),Q(0),Q(0),2*BUDGET)]:
        try: certified_classify(s,Q(0),*errors)
        except ValueError: pass
        else: raise AssertionError('invalid declared error budget accepted')
    result={
      'version':'v0.3','evidence':'EXACT_CONDITIONAL','physical_promotion':0,
      'source_commit':'b2a8abbc3ea24d6aeb6b75d3c644c054d4a6cedf',
      'sample_window':list(map(str,WINDOW)),
      'nominal_prediction_coefficients':{k:list(map(str,v)) for k,v in COEFF.items()},
      'nominal_prediction_radius':str(REMAINDER),
      'threshold':'-1/4+s^2/2-17s^4/96',
      'joint_error_budget':'78epsilon+15r+13nu+eta<=1/1000000',
      'uniform_classification_slack_lower_bound':str(slack),
      'grid_sample_times':257,'adversarial_enclosure_endpoint_checks':checks,
      'coefficient_crosscheck':'forward state vs backward readout recurrences, orders 0..8',
      'scope':'one signed +1/4 apex probe; rational nominal time; all-active instantaneous continuation; exact input parsing; error bounds externally guaranteed',
      'limitations':['supplied error bounds are not estimated by classifier',
          'arbitrary out-of-model readings may receive a label; label is not model validation',
          'binary floating point and measurement quantization require separate bounds',
          'original unmodified witness remains exactly blind']}
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    audit()
