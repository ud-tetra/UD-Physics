"""Exact rational phase samples and K4 incidence checks for a one-hot root."""

import itertools
import json
from fractions import Fraction as Q

edges=list(itertools.combinations(range(4),2))
B=[[(-1 if i==a else 1 if i==b else 0) for a,b in edges] for i in range(4)]
L=[[sum(B[i][e]*B[j][e] for e in range(6)) for j in range(4)] for i in range(4)]
assert L==[[4*(i==j)-1 for j in range(4)] for i in range(4)]


def at_phase(c,h):
    x=[(Q(1)+3*c)/4]+[(Q(1)-c)/4]*3
    y=[h*B[0][e]/2 for e in range(6)]
    xd=[-3*h/2]+[h/2]*3
    yd=[c*B[0][e] for e in range(6)]
    assert xd==[-sum(B[i][e]*y[e] for e in range(6)) for i in range(4)]
    assert yd==[sum(B[i][e]*x[i] for i in range(4)) for e in range(6)]
    assert sum(v*v for v in x+y)==1
    J=[[2*B[i][e]*x[i]*y[e] for e in range(6)] for i in range(4)]
    assert [2*x[i]*xd[i] for i in range(4)]==[-sum(row) for row in J]
    assert [2*y[e]*yd[e] for e in range(6)]==[sum(J[i][e] for i in range(4)) for e in range(6)]
    return {'c':str(c),'h':str(h),'vertex':list(map(str,x)),
            'edge':list(map(str,y)),'root_minus_other':str(x[0]-x[1]),
            'root_stock_minus_other':str(x[0]**2-x[1]**2)}


def main():
    samples=[]
    # Rational parametrization of c=cos(2s), h=sin(2s).
    for t in (Q(0),Q(1,2),Q(1),Q(2)):
        c=(1-t*t)/(1+t*t)
        h=2*t/(1+t*t)
        assert c*c+h*h==1
        samples.append(at_phase(c,h))
    samples.append(at_phase(Q(-1),Q(0)))
    assert samples[2]['root_minus_other']=='0'
    assert samples[-1]['root_stock_minus_other']=='0'
    print(json.dumps({'incidence_laplacian':'4I-J','active_angular_frequency':2,
                      'first_equal_amplitude_time':'pi/4 dimensionless',
                      'full_period':'pi dimensionless',
                      'vertex_stock_plus_edge_stock':'1',
                      'rational_phase_samples':samples},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
