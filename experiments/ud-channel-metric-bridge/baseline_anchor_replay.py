"""Exact uniform half-amplitude separation with independent coefficient anchors."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json

from seventh_probe_replay import SIX, EDGES, terms, quadratic_sample
from mixture_probe_replay import P, J, dot, value, eta
from three_probe_replay import cross, primitive
from continuum_overlap_replay import Q

UNIT = ((1,0,0),(0,1,0),(0,0,1))
B = [4*eta*sum(map(abs,v))+16*eta**2+F(1,32) for v in SIX]
T = [terms(v)+tuple((3*a,3*b) for a,b in terms((0,0))) for v in SIX]
DATA = [[value(p,z) for z in SIX] for p in (P,J)]


def contrasts(a):
    normals=set()
    for ix in combinations(range(len(a)),4):
        sub=[a[i] for i in ix]
        w=[(-1)**j*dot(v[0],cross(v[1],v[2]))
           for j in range(4) for v in [sub[:j]+sub[j+1:]]]
        n=primitive(tuple(w[ix.index(i)] if i in ix else 0 for i in range(len(a))))
        if n:
            normals.add(n)
    return sorted(normals)


def min_envelope(lines,lo,hi):
    # Lines sorted by slope; discard dominated equal slopes.
    high={}
    for a,b in lines:
        if b not in high or a>high[b]:
            high[b]=a
    hull=[]
    for b,a in sorted(high.items()):
        t=None
        while hull:
            c,d,start=hull[-1]
            t=(c-a)/(b-d)
            if start is None or t>start:
                break
            hull.pop()
        hull.append((a,b,t if hull else None))
    candidates={lo,hi}|{t for _,_,t in hull if t is not None and lo<t<hi}
    return min((max(a+b*t for a,b in lines),t) for t in candidates)


def brute_envelope(lines,lo,hi):
    points={lo,hi}
    for (a,b),(c,d) in combinations(lines,2):
        if b!=d and lo<(t:=(c-a)/(b-d))<hi:
            points.add(t)
    return min((max(a+b*t for a,b in lines),t) for t in points)


def certify(anchors):
    a=tuple(map(quadratic_sample,SIX))+tuple(UNIT[i] for i in anchors)
    rows=[]
    for w in contrasts(a):
        assert all(sum(c*v[j] for c,v in zip(w,a))==0 for j in range(3))
        q,n=w[:len(SIX)],w[len(SIX):]
        g=tuple(map(abs,q))
        rows.append((tuple(dot(q,s) for s in DATA), g, 4*dot(g,B), 4*sum(map(abs,n))))
    forms=[u for u,_,_,_ in rows]+[v for ts in T for v in ts]

    @lru_cache(None)
    def margins(d):
        D=[sum(abs(dot(v,d)) for v in ts) for ts in T]
        return tuple(abs(dot(u,d))-dot(g,D)-h for u,g,h,k in rows)

    best=None
    for start,end in EDGES:
        step=tuple(b-a for a,b in zip(start,end))
        def ray(t):
            return tuple(a+t*b for a,b in zip(start,step))
        cuts={F(0),F(1)}
        for u in forms:
            v,m=dot(u,start),dot(u,step)
            if m and 0 < (t:=-F(v)/m) < 1:
                cuts.add(t)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            lo,hi=F(0),F(1)
            left,right=margins(ray(l)),margins(ray(r))
            lines=[]
            for x,y,row in zip(left,right,rows):
                m=y-x
                den=row[-1]
                if den:
                    lines.append((x/den,m/den))
                elif m>0:
                    hi=min(hi,-x/m)
                elif m<0:
                    lo=max(lo,-x/m)
                elif x>0:
                    lo,hi=F(1),F(0)
            if lo>hi:
                continue
            d,t=min_envelope(lines,lo,hi)
            if best is None or d<best[0]:
                assert d==brute_envelope(lines,lo,hi)[0]
                best=(d,ray(l+t*(r-l)))
    d,v=best
    m=margins(v)
    assert all(x<=0 for x,row in zip(m,rows) if not row[-1])
    assert d==max(x/row[-1] for x,row in zip(m,rows) if row[-1])
    return dict(critical_radius=d,worst_unit_direction=v,contrasts=len(rows))


def run():
    out={str(ix):certify(ix) for ix in ((0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2))}
    for name,row in out.items():
        d=row['critical_radius']
        row['critical_radius_display']=float(d)
    for ix in ((0,),(1,),(2,)):
        assert out[str(ix)]['critical_radius']<0
    assert F(35,1000)<out['(0, 1)']['critical_radius']<F(36,1000)
    assert F(44,1000)<out['(0, 1, 2)']['critical_radius']<F(45,1000)
    assert max(out[str(ix)]['critical_radius'] for ix in ((0,2),(1,2))) < F(35,1000)
    out['fixed_pair_coefficient_radii']=[abs(Q[k])/2 for k in ((2,0),(1,1),(0,2))]
    return out


if __name__=='__main__':
    print(json.dumps(run(),indent=2,default=str))
