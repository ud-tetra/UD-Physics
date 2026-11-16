"""Exact Bernstein certificate of receipt-box overlap on the unit charge box."""
from fractions import Fraction as F
from math import comb
from itertools import product
import json

from mixture_probe_replay import P, J, eta

A, B = F(1,25), F(1,2)
Q = {(2,0):F(27,200),(1,1):F(-29,200),(0,2):F(1,20)}
RATIO = F(19,20)
DEG = 6  # degree elevation to a common tensor-product basis
MAX_DEPTH = 12


def polynomial(sign_u, sign_residual):
    out = {(0,0):2*RATIO*(16*eta**2+F(1,32)),
           (1,0):8*RATIO*eta,(0,1):8*RATIO*eta}
    for scale, poly in [(A,P),(B,J),(-1,Q)]:
        for (i,j),c in poly.items():
            out[i,j] = out.get((i,j),0)+sign_residual*sign_u**i*scale*c
    return out


def power_to_bernstein(p):
    assert all(0<=i<=DEG and 0<=j<=DEG for i,j in p)
    return [[sum(c*F(comb(k,i),comb(DEG,i))*F(comb(l,j),comb(DEG,j))
                 for (i,j),c in p.items() if k>=i and l>=j)
             for l in range(DEG+1)] for k in range(DEG+1)]


def transpose(a):
    return list(zip(*a))


def split_1d(c):
    rows=[list(c)]
    while len(rows[-1])>1:
        rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
    return tuple(r[0] for r in rows),tuple(r[-1] for r in reversed(rows))


def split(a, axis):
    seq=transpose(a) if axis==0 else a
    left,right=map(list,zip(*(split_1d(r) for r in seq)))
    return (transpose(left),transpose(right)) if axis==0 else (left,right)


def certify(a,depth=0):
    floor=min(map(min,a))
    if floor>0:
        return 1,depth,floor
    assert depth<MAX_DEPTH
    out=[certify(b,depth+1) for b in split(a,depth%2)]
    return sum(r[0] for r in out),max(r[1] for r in out),min(r[2] for r in out)


def evaluate(p,u,v):
    return sum(c*u**i*v**j for (i,j),c in p.items())


def bernstein_value(a,u,v):
    def w(i,t):
        return comb(DEG,i)*t**i*(1-t)**(DEG-i)
    return sum(c*w(i,u)*w(j,v) for i,row in enumerate(a) for j,c in enumerate(row))


def run():
    assert eta==F(1,100)
    assert max(abs(A),abs(B))==F(1,2)
    # The two quadratic baselines I and I+Q are admissible even if one
    # also imposes positive definiteness and the stiffness row-sum cap.
    x,y,t=1+Q[2,0],1+Q[0,2],Q[1,1]/2
    assert x*y>t*t and max(x,y)+abs(t)<2
    result={}
    for u,res in product((-1,1),repeat=2):
        p=polynomial(u,res)
        b=power_to_bernstein(p)
        x,y=F(2,7),F(5,9)
        assert evaluate(p,x,y)==bernstein_value(b,x,y)
        left,right=split(b,0)
        assert bernstein_value(left,x,y)==evaluate(p,x/2,y)
        assert bernstein_value(right,x,y)==evaluate(p,(1+x)/2,y)
        low,high=split(b,1)
        assert bernstein_value(low,x,y)==evaluate(p,x,y/2)
        assert bernstein_value(high,x,y)==evaluate(p,x,(1+y)/2)
        n,d,h=certify(b)
        result[f'{u:+d},{res:+d}']=dict(leaves=n,depth=d,bernstein_floor=str(h))
    return dict(a=str(A),b=str(B),ratio=str(RATIO),cells=result)


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
