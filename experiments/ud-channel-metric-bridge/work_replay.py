"""Exact symmetric work protocol on the centroid vertex sector."""
import json
from fractions import Fraction as Q


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def decompose(v):
    old=tuple(x+v[4]/4 for x in v[:4])
    return old,add(v,scale(-1,old+(Q(0),)))


def metric(t,x,y):
    px,qx=decompose(x)
    py,qy=decompose(y)
    return dot(px,py)+t*dot(qx,qy)


def run():
    x=(Q(1,2),)*4+(Q(0),)
    c=(Q(0),)*4+(Q(1),)
    y=decompose(c)[1]
    assert c==add(scale(Q(1,2),x),y)
    assert dot(y,y)==Q(5,4) and dot(x,y)==Q(-1,2)
    b=(Q(2,3),Q(-4,7),Q(3,5),Q(9,2),Q(-8,11))
    a,k=Q(3,7),Q(5,9)
    rows={}
    for t in map(Q,['1/4','1','2']):
        for name,H in [('family',lambda u,v:metric(t,u,v)),('uniform',dot)]:
            def work(v):
                # A signed reversible ramp from the same baseline, plus common
                # additive fixture offset. Sham removes it; reversal cancels drift
                # linear in the commanded displacement.
                def shot(s):
                    z=add(b,scale(s*a,v))
                    return k*(H(z,z)-H(b,b))/2+Q(17,8)
                return (shot(1)+shot(-1))/2-shot(0)
            rx,ry,rc=map(work,(x,y,c))
            mixed=rc-ry-rx/4
            assert rx==k*a*a/2
            assert ry/rx==Q(5,4)*(t if name=='family' else 1)
            assert mixed/rx==(0 if name=='family' else Q(-1,2))
            if name=='family':
                # An uncalibrated newborn amplitude multiplier g exactly
                # masquerades as a different t.
                g=Q(7,3)
                assert work(scale(g,y))/rx==Q(5,4)*t*g*g
            rows[f'{name} t={t}']=[str(z) for z in (ry/rx,rc/rx,mixed/rx)]
    return {'vectors':{'inherited':list(map(str,x)),'newborn':list(map(str,y)),
                       'centroid':list(map(str,c))},
            'columns':['newborn/control','centroid/control','mixed/control'],
            'exact_fixture':rows}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
