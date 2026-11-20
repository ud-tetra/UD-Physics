#!/usr/bin/env python3
"""v0.5: two simultaneous boundary readouts with a shared unknown scalar clock."""
import importlib.util
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

DELTA=Q(1,1000000)
REFERENCE_WINDOW=(Q(1,100),Q(1,80))
THRESHOLD=Q(1,115200)

def residual(w,y):
    return 16*w*w+Q(5,4)*y*y-1

def pair_classify(w,y,*,startup_registered=False):
    """Requires error <=DELTA per channel and common first-quarter scalar phase."""
    if not isinstance(w,Q) or not isinstance(y,Q):
        raise TypeError('readings must be fractions.Fraction')
    if not startup_registered:
        return 'INDETERMINATE_BRANCH'
    if not REFERENCE_WINDOW[0]<=y<=REFERENCE_WINDOW[1]:
        return 'OUTSIDE_REFERENCE_WINDOW'
    if abs(w)>Q(1,4)+DELTA:
        return 'OUTSIDE_MODEL_ENVELOPE'
    z=residual(w,y)
    if z>THRESHOLD:
        return 'PROJECTED'
    if z<THRESHOLD:
        return 'FULL'
    return 'INDETERMINATE'

def certified_pair(w,y,epsilon,r,D,eta,*,startup_registered=False):
    """D is cumulative operator error after removing the shared scalar rate."""
    errors=(epsilon,r,D,eta)
    if any(not isinstance(x,Q) for x in errors):
        raise TypeError('bounds must be fractions.Fraction')
    if any(x<0 for x in errors):
        raise ValueError('bounds must be nonnegative')
    if Q(91,2)*epsilon+Q(17,2)*r+3*D+eta>DELTA:
        raise ValueError('two-channel error budget exceeded')
    return pair_classify(w,y,startup_registered=startup_registered)

def load():
    p=Path(__file__).with_name('audit.py')
    spec=importlib.util.spec_from_file_location('timing',p)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    return a,a.main(return_setup=True)

def rm(l,A):
    return [sum(l[i]*A[i][j] for i in range(len(A))) for j in range(len(A))]

def cos_poly(freq2,u):
    return sum(Q((-freq2)**k,factorial(2*k))*u**(2*k) for k in range(7))

def reference_poly(u):
    return 2*sum(Q((-5)**k,factorial(2*k+1))*u**(2*k+1) for k in range(6))

def audit():
    a,d=load()
    cp=d['c'][:];cp[3]+=Q(1,4)
    for name,A,state in [('FULL',d['An'],a.lin.mvec(d['M'],cp)),
                         ('PROJECTED',d['K0'],cp)]:
        W=[Q(int(i==4)-int(i==3)) for i in range(27)]
        Y=[Q(int(i==1)-int(i==0)) for i in range(27)]
        if name=='PROJECTED':
            W=[d['M'][4][j]-d['M'][3][j] for j in range(23)]
            Y=[d['M'][1][j]-d['M'][0][j] for j in range(23)]
        freq=5 if name=='FULL' else 3
        assert rm(rm(W,A),A)==[-freq*x for x in W]
        assert rm(rm(Y,A),A)==[-5*x for x in Y]
        assert sum(x*y for x,y in zip(W,state))==Q(-1,4)
        assert sum(x*y for x,y in zip(rm(W,A),state))==0
        assert sum(x*y for x,y in zip(Y,state))==0
        assert sum(x*y for x,y in zip(rm(Y,A),state))==2
        # Check scalar recurrence coefficients through degree 12 against matrix rows.
        for k in range(13):
            wc=sum(x*y for x,y in zip(W,state))/factorial(k)
            yc=sum(x*y for x,y in zip(Y,state))/factorial(k)
            assert wc==(Q(-1,4)*Q((-freq)**(k//2),factorial(k)) if k%2==0 else 0)
            assert yc==(2*Q((-5)**((k-1)//2),factorial(k)) if k%2 else 0)
            W=rm(W,A);Y=rm(Y,A)
    # Ideal Y on first rising quarter: Y<=2u and Y>=4u/pi>u.
    ideal_y_min,ideal_y_max=Q(1,120),Q(1,60)
    assert REFERENCE_WINDOW[0]-DELTA>ideal_y_min
    assert REFERENCE_WINDOW[1]+DELTA<ideal_y_max
    assert ideal_y_max<Q(1,10)
    # R_P=sin^2(sqrt(5)u)-sin^2(sqrt(3)u).
    # |fourth derivative|<=8*(25+9)=272; lower bound >=u^2 on u<=1/10.
    assert Q(272,24)==Q(34,3)
    assert 2-Q(34,3)*Q(1,10)**2>1
    gap=Q(1,240)**2
    assert gap==Q(1,57600)==2*THRESHOLD
    error=(8+Q(1,24))*DELTA+Q(69,4)*DELTA**2
    assert error<THRESHOLD
    margin=THRESHOLD-error
    # Unknown scalar rate may be arbitrary, so no nominal-time/jitter term.
    example=(Q(1,200000000),Q(1,100000000),Q(1,50000000),Q(1,4000000))
    used=sum(x*y for x,y in zip((Q(91,2),Q(17,2),3,1),example))
    assert used==Q(249,400000000)<DELTA
    # Coarse pre-event crossing and Duhamel hypotheses follow from joint bound.
    assert 2*DELTA/91<Q(1,1000)
    assert 2*DELTA/17+10*DELTA/91<Q(1,1000)
    assert DELTA/3<Q(1,100)
    # Degree12 nominal enclosures only generate test observations;
    # runtime classifier itself uses no trigonometric approximation.
    tail=Q(5,2)*Q(1,2)**13/factorial(13)
    checks=0
    for k in range(257):
        u=Q(1,190)+(Q(1,170)-Q(1,190))*Q(k,256)
        y=reference_poly(u)
        for name,freq in [('FULL',5),('PROJECTED',3)]:
            w=-Q(1,4)*cos_poly(freq,u)
            assert w+DELTA+tail<0 and y-DELTA-tail>0
            # All rectangle extrema occur at corners because signs are fixed.
            for ws in (-1,1):
                for ys in (-1,1):
                    wm=w+ws*(DELTA+tail);ym=y+ys*(DELTA+tail)
                    assert pair_classify(wm,ym,startup_registered=True)==name
                    checks+=1
    assert pair_classify(Q(-1,4),Q(0),startup_registered=True)=='OUTSIDE_REFERENCE_WINDOW'
    assert pair_classify(Q(-1,4),Q(1,100))=='INDETERMINATE_BRANCH'
    try: certified_pair(Q(-1,4),Q(1,100),Q(1),Q(0),Q(0),Q(0),startup_registered=True)
    except ValueError: pass
    else: raise AssertionError('over-budget declaration accepted')
    result={
      'version':'v0.5','evidence':'EXACT_CONDITIONAL','physical_promotion':0,
      'source_commit':'3434916ad00ffc63bf84180cabc93fa8e15dc635',
      'readouts':{'W':'x4-x3','Y':'x1-x0'},
      'exact_signals':{'FULL_W':'-cos(sqrt(5)u)/4','PROJECTED_W':'-cos(sqrt(3)u)/4',
                       'BOTH_Y':'2sin(sqrt(5)u)/sqrt(5)'},
      'clock_invariant_residual':'R=16W^2+(5/4)Y^2-1',
      'full_residual':'0 for every phase',
      'projected_residual':'sin^2(sqrt(5)u)-sin^2(sqrt(3)u)',
      'nominal_projected_gap_lower_bound':str(gap),
      'observed_reference_window':list(map(str,REFERENCE_WINDOW)),
      'per_channel_error_bound':str(DELTA),
      'residual_error_bound':str(error),
      'decision_threshold':str(THRESHOLD),
      'residual_classification_margin':str(margin),
      'sufficient_joint_budget':'(91/2)epsilon+(17/2)r+3D+eta<=1/1000000',
      'example_budget_used':str(used),
      'phase_registration':'first rising reference quarter, 0<=u<=pi/(2sqrt(5))',
      'allowed_clock':'arbitrary common nonnegative scalar rate v(t); u=integral v; no absolute calibration',
      'operator_error':'D=int norm(E) after extracting scalar rate; metric and event map fixed',
      'adversarial_enclosure_corner_checks':checks,'phase_grid_points':257,
      'limitations':['two readouts simultaneous or channel phase mismatch included in eta',
         'first-quarter registration must be supplied; later cycles not certified',
         'zero progress produces no reference-window admission',
         'independent channel gains, metric/event-map changes and native probe selection open']}
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    audit()
