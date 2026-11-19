"""Exact certification of seventh-work finalists; no NumPy dependency."""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
import json

from mixed_taylor_replay import coeffs
from mixture_probe_replay import P, J, points, value, dot, eta
from three_probe_replay import cross, primitive

SIX = points+((F(-1,2),1),)
EDGES = (((-1,0),(-1,1)),((-1,1),(1,1)),((1,1),(1,0)))


def quadratic_sample(z):
    x,y=z
    return x*x,x*y,y*y


def contrasts(sites):
    A=tuple(map(quadratic_sample,sites))
    ns=set()
    for idx in combinations(range(len(A)),4):
        sub=[A[i] for i in idx]
        w=[(-1)**j*dot(v[0],cross(v[1],v[2]))
           for j in range(4) for v in [sub[:j]+sub[j+1:]]]
        n=primitive(tuple(w[idx.index(i)] if i in idx else 0 for i in range(len(A))))
        if n:
            ns.add(n)
    assert all(all(sum(n[i]*A[i][j] for i in range(len(A)))==0
                   for j in range(3)) for n in ns)
    return sorted(ns)


@lru_cache(None)
def terms(z):
    p,j=coeffs(P,z),coeffs(J,z)
    return tuple((p.get(k,0),j.get(k,0)) for k in sorted(p.keys()|j.keys()))


def certify(sites):
    zterms=tuple((3*a,3*b) for a,b in terms((0,0)))
    T=[terms(z)+zterms for z in sites]
    Pvals,Jvals=([value(poly,z) for z in sites] for poly in (P,J))
    B=[4*eta*sum(map(abs,v))+16*eta**2+F(1,32) for v in sites]
    rows=[]
    for n in contrasts(sites):
        w=tuple(map(abs,n))
        rows.append(((dot(n,Pvals),dot(n,Jvals)),2*dot(w,B),w))
    assert all(h>0 for _,h,_ in rows)

    @lru_cache(None)
    def scores(d):
        D=[sum(abs(dot(c,d)) for c in ts) for ts in T]
        return tuple((abs(dot(u,d))-dot(w,D))/h for u,h,w in rows)

    forms=[u for u,_,_ in rows]+[c for ts in T for c in ts]
    opt=None
    segments=0
    for start,end in EDGES:
        step=tuple(b-a for a,b in zip(start,end))
        def d(t):
            return tuple(a+t*b for a,b in zip(start,step))
        cuts={F(0),F(1)}
        for c in forms:
            v,m=dot(c,start),dot(c,step)
            if m and 0 < (t:=-F(v)/m) < 1:
                cuts.add(t)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            segments+=1
            L,R=scores(d(l)),scores(d(r))
            lines=[(a,b-a) for a,b in zip(L,R)]
            trials={F(0),F(1)}
            for (a,b),(c,e) in combinations(lines,2):
                if b!=e and 0 < (t:=(c-a)/(b-e)) < 1:
                    trials.add(t)
            for t in trials:
                m=max(a+t*b for a,b in lines)
                if opt is None or m<opt[0]:
                    opt=(m,d(l+t*(r-l)))
    m,ray=opt
    assert m==max(scores(ray)) and m>0
    return dict(radius=1/m, ray=ray, segments=segments, contrast_count=len(rows),
                old_half_score=max(scores((F(1,20),F(1,2)))),
                worst_half_score=m/2)


def run():
    candidates=[(F(-5,8),F(1)),(F(-3,5),F(1)),(F(-13,20),F(1)),
                (F(-23,40),F(1)),(F(7,8),F(3,4)),(F(9,10),F(29,40))]
    results={str(tuple(map(str,z))):certify(SIX+(z,)) for z in candidates}
    results['six_control']=certify(SIX)
    assert results['six_control']['radius']==F(6288871753696320200000000000,10180223594200285859314975003)
    best=min(candidates,key=lambda z:results[str(tuple(map(str,z)))]['radius'])
    champion=results[str(tuple(map(str,best)))]
    assert best==(F(-5,8),1) and F(603,1000)<champion["radius"]<F(604,1000)
    assert all(results[str(tuple(map(str,z)))]["old_half_score"]<1 for z in candidates)
    return {'best_exact_finalist':list(map(str,best)), 'results':results}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,default=str))
