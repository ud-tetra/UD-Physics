"""Exact shared-receipt geometry and two-witness detection."""
from fractions import Fraction as F
from itertools import product
import json

G = ((F(-1,2),F(-1,5)),(-2,0),(1,F(-1,5)),(1,F(1,10)),(0,F(1,10)))
N = ((2,-5),(0,1),(1,5),(1,-10),(1,0))
B = tuple(F(z,20000) for z in (1457,1857,1457,2257,2257))
ETA = F(1,100)


def dot(n,z):
    return sum(a*b for a,b in zip(n,z))


def hw(n,radii):
    return sum(abs(dot(n,g))*r for g,r in zip(G,radii))


def h(k):
    return (1+ETA)**k-1+3*ETA**k


def delta(a,b):
    return 9*abs(a)*h(6)+abs(b)*(4*h(6)+5*h(8))


def run():
    points = ((1,0),(F(-1,2),1),(0,1),(-1,1),(1,1))
    def outputs(f):
        return tuple(sum(g[i]*f(u,v) for g,(u,v) in zip(G,points)) for i in range(2))
    def p(u,v):
        return 4*u*u*v*v*(u+F(1,2)*v)**2
    for f in (lambda u,v:u*u, lambda u,v:u*v, lambda u,v:v*v):
        assert outputs(f)==(0,0)
    assert outputs(p)==(1,1)
    assert outputs(lambda u,v:p(u,v)*(4-5*u*v)/9)==(1,0)
    assert {i for n in N for i,g in enumerate(G) if dot(n,g)==0}==set(range(5))
    vertices = [tuple(sum(g[i]*r for g,r in zip(G,signs)) for i in range(2))
                for signs in product(*[(-b,b) for b in B])]
    for n in N:
        assert max(abs(dot(n,v)) for v in vertices)==hw(n,B)
    def margin(a,b,aa=0,bb=0,extra=True):
        ds=delta(a,b)+delta(aa,bb) if extra else 0
        radii=tuple(2*r+ds for r in B)
        center=(a+b-aa-bb,a-aa)
        return max(abs(dot(n,center))-hw(n,radii) for n in N)
    half=F(1,2)
    m=[margin(half,0),margin(half,-half),margin(0,half,extra=False)]
    assert m[0]>0 and m[1]>0 and m[2]<0
    r=(F(2,5),F(1,20))
    assert all(abs(dot(n,r))<=hw(n,B) for n in [(1,0),(0,1)])
    assert dot((1,5),r)>hw((1,5),B)
    return {'supports':{str(n):str(hw(n,B)) for n in N},
            'half_witness_strip_margins':list(map(str,m)),
            'joint_only_example':list(map(str,r))}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
