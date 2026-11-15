"""Exact symmetric probe and uncertainty receipt."""
from fractions import Fraction as Q
from itertools import product
import json

X, C, P, M, Y = (1,0), (0,1), (1,1), (-1,1), (Q(-1,2),1)


def signal(f):
    return (f(*P)+f(*M)-2*f(*X)-2*f(*C))/10


def witness(u,v):
    return 4*u*u*v*v*(u+Q(1,2)*v)**2


def run():
    def old(f):
        return f(*M)+f(*C)-2*f(*Y)-f(*X)/2
    for f in (lambda u,v:Q(u*u), lambda u,v:Q(u*v), lambda u,v:Q(v*v)):
        assert signal(f)==old(f)==0
    assert [witness(*z) for z in (P,M,X,C,Y)]==[9,1,0,0,0]
    assert signal(witness)==old(witness)==1
    blind=lambda u,v:witness(u,v)*(4-5*u*v)/9
    assert signal(blind)==0 and old(blind)==1
    eta=Q(1,100)
    a=4*eta+16*eta**2+Q(1,32)
    b=8*eta+16*eta**2+Q(1,32)
    lo,hi=[f([sum(Q(k,10)*v for k,v in zip((1,1,-2,-2),e))
                     for e in product((-b,b),(-b,b),(-a,a),(-a,a))]) for f in (min,max)]
    assert hi==-lo==Q(5171,100000)
    endpoint=9*((1+eta)**6-1+3*eta**6)
    alt=hi+Q(3,10)*endpoint
    margin=Q(1,2)-hi-alt
    assert margin>0
    return {k:str(v) for k,v in dict(axis=a,corner=b,null_radius=hi,
                half_departure_radius=alt,guaranteed_margin=margin).items()}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
