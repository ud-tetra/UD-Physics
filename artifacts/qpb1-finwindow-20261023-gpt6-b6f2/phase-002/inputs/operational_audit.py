#!/usr/bin/env python3
"""Second-construction operational phase certificate; stdlib only, no empirical model."""
import argparse, json, math, random
from fractions import Fraction as F
from itertools import product
from pathlib import Path

G0=(1.,1.,1.5)
eps=F(1,100); dt=F(1,100); prep=F(1,2000)
noise=F(1,1000); cal=F(1,1000)
spread=dt+4*eps*(F(44,7)+dt)  # range of endpoint phase errors
visibility=1-spread**2/8
phase=spread**3/(6*(1-spread**2/2))
prep_phase=F(44,7)*prep
fringe_phase=noise/(visibility-noise)
total=prep_phase+phase+fringe_phase+cal
assert visibility>F(99,100) and total<F(1,100)

def check(g,r,t):
    z=sum(w*complex(math.cos(2*x*t),math.sin(2*x*t)) for x,w in zip(g,r))
    d=2*t*sum(x*w for x,w in zip(g,r))
    # Four balanced fringe intensities at analyzer angles 0, pi/2, pi, 3pi/2.
    intensity=lambda b:(1+(z*complex(math.cos(b),-math.sin(b))).real)/2
    z4=complex(intensity(0)-intensity(math.pi),
               intensity(math.pi/2)-intensity(3*math.pi/2))
    assert abs(z4-z)<3e-15
    target=-2*math.pi*(r[2]-.5)
    actual=math.atan2(math.sin(math.atan2(z.imag,z.real)-d-math.pi),
                      math.cos(math.atan2(z.imag,z.real)-d-math.pi))
    assert abs(actual-target)<float(phase)+2e-13
    assert abs(z)>=float(visibility)-2e-13
    # Max receiver noise rotation and independent calibration error.
    for rot in (0,math.pi/2,math.pi,3*math.pi/2):
        noisy=z+float(noise)*complex(math.cos(rot),math.sin(rot))
        diff=math.atan2(math.sin(math.atan2(noisy.imag,noisy.real)-d-math.pi-target),
                        math.cos(math.atan2(noisy.imag,noisy.real)-d-math.pi-target))
        assert abs(diff)+float(cal)<float(total)+2e-13
    return abs(z),abs(actual)

n=0; vmin=1.; pmax=0.
for da,db,dc,tau,r3 in product((-float(eps),0.,float(eps)),
                              (-float(eps),0.,float(eps)),
                              (-float(eps),0.,float(eps)),
                              (-float(dt),0.,float(dt)),
                              (.5-float(prep),.5,.5+float(prep))):
    g=tuple(x+y for x,y in zip(G0,(da,db,dc)))
    v,p=check(g,(.25,.75-r3,r3),2*math.pi+tau)
    n+=1; vmin=min(vmin,v); pmax=max(pmax,p)
random.seed(1729)
for _ in range(25000):
    g=tuple(x+random.uniform(-float(eps),float(eps)) for x in G0)
    t=2*math.pi+random.uniform(-float(dt),float(dt))
    r3=.5+random.uniform(-float(prep),float(prep))
    v,p=check(g,(.25,.75-r3,r3),t)
    vmin=min(vmin,v); pmax=max(pmax,p)
result={'status':'PASS','review':'same-assistant alternate derivation and implementation; external review NOT_RUN',
        'model':{'gain_errors':'1/100','time_error':'1/100 native unit',
                 'preparation_distance':'1/2000','complex_overlap_noise':'1/1000',
                 'dynamical_correction_error_rad':'1/1000'},
        'bounds':{'angular_spread':str(spread),'visibility_lower':str(visibility),
                  'phase_error_from_spread':str(phase),'preparation_phase':str(prep_phase),
                  'receiver_phase':str(fringe_phase),'total_radians':str(total),
                  'total_decimal':float(total)},
        'checks':{'structured':n,'seeded':25000,'sample_visibility_min':vmin,
                  'sample_unnoised_phase_error_max':pmax,'four_fringe_and_noise_directions':True}}
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
