"""Exact directional minimax for joint Taylor charge-error certificates."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json
from mixture_probe_replay import G, J, P, dot, ep, eta, points, value
from three_probe_replay import cross, primitive


def coeffs(poly,z):
    out=defaultdict(F)
    for (i,j),c in poly.items():
        for k,l in product(range(i+1),range(j+1)):
            if k+l:
                out[k,l]+=c*comb(i,k)*comb(j,l)*z[0]**(i-k)*z[1]**(j-l)*eta**(k+l)
    return {k:v for k,v in out.items() if v}


def run():
    g=tuple(col+(w,) for col,w in zip(G,(F(-1,2),1,1,0,0)))+((0,0,-2),)
    vs=points+((F(-1,2),1),)
    normals=sorted({v for x,y in combinations(g,2) if (v:=primitive(cross(x,y)))})
    assert len(normals)==10
    def response(poly):
        return tuple(sum(c[i]*value(poly,v) for c,v in zip(g,vs)) for i in range(3))
    pa,pb=map(response,(P,J))
    assert (pa,pb)==((1,F(3321,625),1),(0,F(-4149,3125),1))
    B=[4*eta*sum(map(abs,v))+16*eta**2+F(1,32) for v in vs]
    def terms(z):
        p,j=coeffs(P,z),coeffs(J,z)
        assert sum(map(abs,p.values()))==ep(P,z)
        assert sum(map(abs,j.values()))==ep(J,z)
        return [(p.get(k,0),j.get(k,0)) for k in sorted(p.keys()|j.keys())]
    zero=terms((0,0))
    terms_by_receipt=[terms(z)+[(3*a,3*b) for a,b in zero] for z in vs]
    rows=[]
    for n in normals:
        w=[abs(dot(n,col)) for col in g]
        rows.append(((dot(n,pa),dot(n,pb)),2*dot(w,B),w))
    def strip_scores(d):
        D=[sum(abs(dot(c,d)) for c in t) for t in terms_by_receipt]
        return tuple((abs(dot(u,d))-dot(w,D))/h for u,h,w in rows)

    # Central symmetry reduces the unit infinity-norm boundary to three edges.
    all_forms=[u for u,_,_ in rows]+sum(terms_by_receipt,[])
    best=None
    segments=0
    for start,end in [((-1,0),(-1,1)),((-1,1),(1,1)),((1,1),(1,0))]:
        step=tuple(b-a for a,b in zip(start,end))
        direction=lambda t:tuple(a+t*b for a,b in zip(start,step))
        cuts={F(0),F(1)}
        for c in all_forms:
            v,m=dot(c,start),dot(c,step)
            if m and 0 < (t:=-F(v)/m) < 1:
                cuts.add(t)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            segments+=1
            L,R=strip_scores(direction(l)),strip_scores(direction(r))
            assert strip_scores(direction((l+r)/2))==tuple((a+b)/2 for a,b in zip(L,R))
            lines=[(a,b-a) for a,b in zip(L,R)]
            candidates={F(0),F(1)}
            for (a,b),(c,d) in combinations(lines,2):
                if b!=d and 0 < (t:=(c-a)/(b-d)) < 1:
                    candidates.add(t)
            for t in candidates:
                score=max(a+t*b for a,b in lines)
                ray=direction(l+t*(r-l))
                if best is None or score<best[0]:
                    best=(score,ray)
    score,ray=best
    assert score==max(strip_scores(ray)) and score>0
    radius=1/score
    witness=(F(1,20),F(1,2))
    assert F(617,1000)<radius<F(618,1000)
    assert max(strip_scores(witness))<1
    return dict(segments=segments, radius=str(radius), radius_display=float(radius),
                maximizing_direction=list(map(str,ray)),
                half_witness_overlap=max(strip_scores(witness))<=1,
                half_witness_max_score=str(max(strip_scores(witness))))


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
