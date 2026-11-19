"""Exact six-receipt, three-residual overlap audit."""
import json
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from mixture_probe_replay import G, J, P, dot, ep, eta, points, value


def cross(a,b):
    return tuple(a[i-2]*b[i-1]-a[i-1]*b[i-2] for i in range(3))


def primitive(n):
    k = lcm(*(F(v).denominator for v in n))
    z = tuple(int(k*v) for v in n)
    g = gcd(*z)
    if g == 0:
        return None
    if next(v for v in z if v) < 0:
        g = -g
    return tuple(v//g for v in z)


def run():
    # Receipt order x,c,m,p,z,y; residual order S,T,R.
    g = tuple(col+(w,) for col,w in zip(G,(F(-1,2),1,1,0,0)))+((0,0,-2),)
    vs = points+((F(-1,2),1),)
    n = sorted({v for x,y in combinations(g,2) if (v:=primitive(cross(x,y)))})
    assert len(n)==10 and any(dot(v,col) for v in n for col in g)
    def response(poly):
        return tuple(sum(c[i]*value(poly,v) for c,v in zip(g,vs)) for i in range(3))
    for k in ((2,0),(1,1),(0,2)):
        assert response({k:1})==(0,0,0)
    pa,pb = response(P),response(J)
    assert (pa,pb)==((1,F(3321,625),1),(0,F(-4149,3125),1))
    B = [4*eta*sum(map(abs,v))+16*eta**2+F(1,32) for v in vs]
    D = [[ep(f,v)+3*ep(f,(0,0)) for v in vs] for f in (P,J)]
    rows = []
    for normal in n:
        w = [abs(dot(normal,col)) for col in g]
        rows.append((dot(normal,pa),dot(normal,pb),2*dot(w,B),*(dot(w,d) for d in D)))
    def overlap(a,b):
        return all(abs(u*a+v*b)<=h+da*abs(a)+db*abs(b) for u,v,h,da,db in rows)

    vertices=set()
    for sa,sb in product((-1,1),repeat=2):
        hs=[(-1,0,0),(0,-1,0)]
        for u,v,h,da,db in rows:
            hs.extend((q*u*sa-da,q*v*sb-db,h) for q in (-1,1))
        for (i,j,h),(k,l,s) in combinations(hs,2):
            d=i*l-j*k
            if d:
                x,y=(h*l-j*s)/d,(i*s-h*k)/d
                if all(a*x+b*y<=c for a,b,c in hs):
                    vertices.add((sa*x,sb*y))
    far=max(vertices,key=lambda z:(max(map(abs,z)),z))
    radius=max(map(abs,far))
    old=(F(11,100),F(1,2))
    grid=[(F(i,100),F(1,2)) for i in range(-50,51) if overlap(F(i,100),F(1,2))]
    assert not overlap(*old) and overlap(F(1,20),F(1,2))
    assert F(632,1000)<radius<F(633,1000)
    return {'facet_normal_count':len(n), 'vertex_count_with_axis_splits':len(vertices),
            'former_witness_overlap':overlap(*old),
            'half_b_grid_overlap':list(map(str,grid)),
            'radius':str(radius),'radius_display':float(radius),
            'maximizer':list(map(str,far)),
            'normal_rows':{str(k):list(map(str,v)) for k,v in zip(n,rows)}}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
