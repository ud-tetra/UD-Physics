"""Exact synthetic replay of independently calibrated charge/work channels."""
from fractions import Fraction as F
from itertools import product
import json

N = 32
ETA = F(1,100)
WSTAR = F(1,2)  # a=C*=T=1 in the normalized test
LIMIT = WSTAR/32
PREP = WSTAR*(6*ETA+16*ETA**2)
COMMANDS = {'x':(1,0), 'y':(F(-1,2),1), 'c':(0,1)}
ARMS = {'candidate':((1,F(1,2)),(F(1,2),F(3,2))),
        'uniform':((1,0),(0,1)),
        'boundary':((1,F(1,4)),(F(1,4),1))}


def mv(K,x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in K)


def simulate(K, perturb, sensor, vg, ig, leak, skew):
    # Normalized ramp q(s)=s q_f. Terminal drive also supplies a shunt
    # current leak*V(s). The work ADC pairs V(s+skew) with I(s).
    shots={}
    for label,v in COMMANDS.items():
        shots[label]={}
        for sign in (-1,0,1):
            q=tuple(sign*(1+perturb)*z for z in v)
            V=mv(K,q)
            charge=tuple((1+sensor)*z for z in q)
            work=F(0)
            for j in range(N):
                s=F(2*j+1,2*N)
                work+=sum((1+vg)*(s+skew)*u*(1+ig)*(z+leak*s*u)
                          for z,u in zip(q,V))/N
            shots[label][sign]=(charge,work)
    return shots


def classify(shots, charge_gain, voltage_gain, current_gain, leak, skew):
    # Inputs are observations and independently supplied absolute bounds.
    if any(v is None for v in (charge_gain,voltage_gain,current_gain,leak,skew)):
        return 'ABSTAIN_MISSING_CERTIFICATE',{}
    assert all(0<=g<1 for g in (charge_gain,voltage_gain,current_gain))
    assert leak>=0 and skew>=0
    if skew>F(1,2*N):
        return 'ABSTAIN_SAMPLE_ALIGNMENT',{}
    charge_bound=max(abs(z-sign*v)+abs(z)*charge_gain/(1-charge_gain)
                     for k,cmd in COMMANDS.items()
                     for sign,(qhat,_) in shots[k].items()
                     for z,v in zip(qhat,cmd))
    if charge_bound>ETA:
        return 'ABSTAIN_CHARGE',{'charge_bound':charge_bound}
    # Given the charge certificate, all |q_f,i| <= 1+ETA; the scoped
    # fixtures have max row sum |K|<=2. Use worst-case raw work errors.
    V=2*(1+ETA)
    I=1+ETA+leak*V
    gain=voltage_gain+current_gain+voltage_gain*current_gain
    loss=2*leak*V**2/3
    quad=2*leak*V**2/(12*N*N)
    timing=2*V*I*skew
    gain_error=2*V*I*(1+skew)*gain
    # One signed-average receipt less one sham; bound each by the same
    # per-shot error even though the zero-reset synthetic sham is exact.
    work_bound=2*(loss+quad+timing+gain_error)
    out={'charge_bound':charge_bound,'work_bound':work_bound}
    if work_bound>LIMIT:
        return 'ABSTAIN_WORK_BUDGET',out
    work={k:(r[-1][1]+r[1][1])/2-r[0][1] for k,r in shots.items()}
    S=work['c']-work['y']
    rad=2*(PREP+work_bound)
    out.update(work_x=work['x'],work_y=work['y'],work_c=work['c'],
               discriminant=S,interval_low=S-rad,interval_high=S+rad)
    return ('CANDIDATE_SIGN' if S-rad>0 else
            'UNIFORM_SIGN' if S+rad<0 else 'ABSTAIN_SIGN'),out


def run():
    good=(F(1,500),F(1,1000),F(1,10000),F(-1,10000),
          F(1,10000),F(1,10000))
    def bounds(p):
        return tuple(abs(v) for v in p[1:])
    scenarios=[]
    # Finite corner grid; each nuisance sign changes independently.
    for name in ('candidate','uniform'):
        for signs in product((-1,1),repeat=5):
            p=tuple(a*b for a,b in zip(good,signs+(1,)))
            scenarios.append((name,p,bounds(p),
                         'CANDIDATE_SIGN' if name=='candidate' else 'UNIFORM_SIGN'))
    # Each injected fault carries its actual worst-case calibration bound.
    for idx,amp,reason in [(0,F(1,25),'CHARGE'),(1,F(1,20),'CHARGE'),
             (2,F(1,20),'WORK_BUDGET'),(4,F(1,20),'WORK_BUDGET'),
             (5,F(1,100),'WORK_BUDGET'),(5,F(1,32),'SAMPLE_ALIGNMENT')]:
        p=list(good)
        p[idx]=amp
        for name in ('candidate','uniform'):
            scenarios.append((name,tuple(p),bounds(p),'ABSTAIN_'+reason))
    scenarios.append(('candidate',good,(None,)+bounds(good)[1:],
                      'ABSTAIN_MISSING_CERTIFICATE'))
    scenarios.append(('boundary',good,bounds(good),'ABSTAIN_SIGN'))
    results=[]
    for arm,p,cert,expected in scenarios:
        observed,d=classify(simulate(ARMS[arm],*p),*cert)
        assert observed==expected,(arm,p,expected,observed)
        if 'interval_low' in d:
            K=ARMS[arm]
            exact=WSTAR*(K[0][1]-F(1,4))
            assert d['interval_low']<=exact<=d['interval_high']
        results.append({'arm':arm,'nuisances':list(map(str,p)),
                        'certificates':[str(x) if x is not None else None for x in cert],
                        'result':observed,**{k:str(v) for k,v in d.items()}})
    return results


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
