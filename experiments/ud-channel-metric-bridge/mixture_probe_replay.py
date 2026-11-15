"""Exact blind-region certificate for joint square and radial work."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from collections import defaultdict
import json

r = F(4,5)
eta = F(1,100)
points = ((1,0),(0,1),(-1,1),(1,1),(r,r))
G = ((F(-1,5),0),(F(-1,5),0),(F(1,10),0),(F(1,10),1),(0,-1/r**2))
N = ((1,0),(0,1),(10,-1))
P = {(4,2):4,(3,3):4,(2,4):1}
J = {(i,j):F(4*c,9) for (i,j),c in P.items()} | {
    (i+1,j+1):F(-5*c,9) for (i,j),c in P.items()}


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def value(poly,z):
    return sum(c*z[0]**i*z[1]**j for (i,j),c in poly.items())


def ep(poly,z):
    out = defaultdict(F)
    for (i,j),c in poly.items():
        for k,l in product(range(i+1),range(j+1)):
            out[k,l] += c*comb(i,k)*comb(j,l)*z[0]**(i-k)*z[1]**(j-l)
    return sum(abs(c)*eta**(k+l) for (k,l),c in out.items() if k+l)


def run():
    def response(poly):
        return tuple(sum(g[k]*value(poly,z) for g,z in zip(G,points))
                     for k in range(2))
    for k in ((2,0),(1,1),(0,2)):
        assert response({k:1}) == (0,0)
    pa,pb=response(P),response(J)
    assert (pa,pb)==((1,F(3321,625)),(0,F(-4149,3125)))
    B = [4*eta*sum(map(abs,z))+16*eta**2+F(1,32) for z in points]
    DP,DJ = [[ep(f,z)+3*ep(f,(0,0)) for z in points] for f in (P,J)]
    strips=[]
    for n in N:
        w = [abs(dot(n,g)) for g in G]
        strips.append((dot(n,pa),dot(n,pb),2*dot(w,B),dot(w,DP),dot(w,DJ)))

    def overlap(a,b):
        return all(abs(u*a+v*b)<=h+da*abs(a)+db*abs(b)
                   for u,v,h,da,db in strips)

    # Solve each sign cone exactly in coordinate magnitudes.
    vertices=[]
    for sa,sb in product((-1,1),repeat=2):
        inequalities=[(-1,0,0),(0,-1,0)]
        for u,v,h,da,db in strips:
            inequalities.extend((q*u*sa-da,q*v*sb-db,h) for q in (-1,1))
        # Bound first coordinate by the S strip and then second by T.
        assert strips[0][0]==1 and strips[0][1]==0
        h,da,db=strips[0][2:]
        u,v,h2,da2,db2=strips[1]
        assert 1-da>0 and abs(v)-db2 > (abs(u)+da2)*db/(1-da)
        for (i,j,h),(k,l,g) in combinations(inequalities,2):
            d=i*l-j*k
            if d:
                x,y=(h*l-j*g)/d,(i*g-h*k)/d
                if all(a*x+b*y<=c for a,b,c in inequalities):
                    vertices.append((sa*x,sb*y))
    radius=max(max(map(abs,z)) for z in vertices)
    witness=(F(11,100),F(1,2))
    assert overlap(*witness) and not overlap(F(1,2),0) and not overlap(0,F(1,2))
    assert F(722,1000) < radius < F(723,1000)
    print_data={'blind_box_radius':str(radius), 'radius_decimal_for_display':float(radius),
                'half_mixture_overlap':overlap(*witness),
                'pure_half_excluded':[not overlap(F(1,2),0),not overlap(0,F(1,2))],
                'strips':{str(n):[str(z) for z in s] for n,s in zip(N,strips)}}
    return print_data


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
