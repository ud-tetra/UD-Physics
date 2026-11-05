#!/usr/bin/env python3
"""v0.4: fixed-metric post-event generator and activation-ramp robustness."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj

cl=module('classifier',Path(__file__).with_name('classifier.py'))
a=module('timing',Path(__file__).with_name('audit.py'))

def total_budget(epsilon,r,nu,eta,kappa,ell):
    errors=(epsilon,r,nu,eta,kappa,ell)
    if any(not isinstance(x,Q) for x in errors):
        raise TypeError('all declared bounds must be fractions.Fraction')
    if any(x<0 for x in errors):
        raise ValueError('bounds must be nonnegative')
    return 78*epsilon+15*r+13*nu+eta+Q(3,100)*kappa+30*ell

def robust_classify(s,y,epsilon,r,nu,eta,kappa,ell):
    if total_budget(epsilon,r,nu,eta,kappa,ell)>cl.BUDGET:
        raise ValueError('post-event robust budget exceeded')
    return cl.classify(s,y)

def rowmul(l,A):
    return [sum(l[i]*A[i][j] for i in range(len(A))) for j in range(len(A))]

def audit():
    d=a.main(return_setup=True)
    cp=d['c'][:];cp[3]+=Q(1,4)
    new=a.lin.mvec(d['M'],cp)
    lf=[Q(int(i==4)-int(i==3)) for i in range(27)]
    lp=[d['M'][4][j]-d['M'][3][j] for j in range(23)]
    for A,l,freq2,state in [(d['An'],lf,5,new),(d['K0'],lp,3,cp)]:
        assert rowmul(rowmul(l,A),A)==[-freq2*x for x in l]
        assert sum(x*y for x,y in zip(l,state))==Q(-1,4)
        assert sum(x*y for x,y in zip(rowmul(l,A),state))==0
    # Thus W_F=-cos(sqrt(5)t)/4 and W_P=-cos(sqrt(3)t)/4.
    # Full-rate multiplier v with v^2=3/5 makes this scalar readout identical.
    rate_square=Q(3,5)
    assert 5*rate_square==3
    # Constant no-evolution ramp is another exact unrestricted-ramp counterexample.
    # Duhamel bound: D<=kappa/100+10ell; D<=1/100 implies exp(D)<=100/99<6/5.
    assert Q(100,99)<Q(6,5)
    assert Q(5,2)*Q(6,5)==3
    assert Q(1,120)+Q(1,2000)+Q(1,100000)<Q(1,100)
    example=(Q(1,200000000),Q(1,100000000),Q(1,100000000),
             Q(1,4000000),Q(1,1000000),Q(1,1000000000))
    used=total_budget(*example)
    assert used==Q(49,50000000)<cl.BUDGET
    D=example[4]/100+10*example[5]
    assert D==Q(1,50000000)
    assert cl.BUDGET/3<Q(1,100)
    # Same 1,028 worst-case endpoint checks, now bound includes generator/ramp effects.
    checked=0
    for k in range(257):
        s=cl.WINDOW[0]+(cl.WINDOW[1]-cl.WINDOW[0])*Q(k,256)
        for label,(lo,hi) in cl.prediction_intervals(s).items():
            for y in (lo-used,hi+used):
                assert robust_classify(s,y,*example)==label
                checked+=1
    for errors in [example[:-1]+(Q(1),),example[:-1]+(Q(-1),)]:
        try: robust_classify(cl.WINDOW[0],Q(0),*errors)
        except ValueError: pass
        else: raise AssertionError('invalid uncertainty tuple accepted')
    result={
      'version':'v0.4','evidence':'EXACT_CONDITIONAL','physical_promotion':0,
      'source_commit':'5549d2b077313eebe776850aa6aae8f70fd0729f',
      'exact_scalar_laws':{'FULL':'-cos(sqrt(5)*s)/4','PROJECTED':'-cos(sqrt(3)*s)/4'},
      'no_go':'unknown full-rate multiplier sqrt(3/5) aliases this single boundary readout with projected unit-rate flow at all times',
      'perturbation_domain':'post-event only; common fixed ambient metric; fixed event map and pre-event generator',
      'ramp_family':'B_actual(t)=B_h+(1-rho(t))*(B_off-B_h)+E(t)',
      'assumptions':['B_h and B_off skew in the fixed metric, norms <=5',
                     '0<=rho<=1; integral(1-rho)<=ell through the horizon',
                     'E may be non-skew; operator norm <=kappa',
                     'both hypotheses individually satisfy declared bounds',
                     'pre-event/crossing assumptions remain those of v0.2'],
      'time_horizon_upper_bound':'1/100 after actual event',
      'operator_mismatch_integral_bound':'D<=kappa/100+10ell',
      'extra_scalar_error_bound':'3D',
      'sufficient_budget':'78epsilon+15r+13nu+eta+3kappa/100+30ell<=1/1000000',
      'example':dict(zip(['epsilon','r','nu','eta','kappa','ell'],map(str,example))),
      'example_budget_used':str(used),'example_D_bound':str(D),
      'linear_ramp_duration_example':'2/1000000000; integrated deficit=1/1000000000',
      'adversarial_endpoint_checks':checked,
      'limitations':['gate acts after the instantaneous event transport; no cross-topology ramp modeled',
          'metric changes, unknown clock calibration, and pre-event generator errors excluded',
          'certificate is conservative and conditional, not measured tolerance',
          'externally supplied error/ramp bounds are not inferred by classifier']}
    print(json.dumps(result,indent=2));return result

if __name__=='__main__':
    audit()
