#!/usr/bin/env python3
"""Exact scalar-feedback port invariants and phase-obstruction test (stdlib only)."""
from fractions import Fraction as F
import json

def stock(r,y): return sum(t*t for t in (*r,*y))
def wedge(r,y): return r[0]*y[1]-r[1]*y[0]
def rhs(r,y):
    n=stock(r,y)
    g=sum(t*t for t in y)/n if n else F(0)
    return tuple(g*t for t in y),tuple(-g*t for t in r)
def derivatives(r,y):
    rd,yd=rhs(r,y)
    dn=2*sum(a*b for a,b in zip(r,rd))+2*sum(a*b for a,b in zip(y,yd))
    dd=rd[0]*y[1]+r[0]*yd[1]-rd[1]*y[0]-r[1]*yd[0]
    return dn,dd
cases=[
    ((F(0),F(0)),(F(1),F(0))),
    ((F(1),F(0)),(F(0),F(1))),
    ((F(1),F(1)),(F(2),F(-1))),
    ((F(1),F(0)),(F(1),F(0))),
    ((F(-1),F(0)),(F(1),F(0)))
]
for r,y in cases:
    assert derivatives(r,y)==(0,0)
    n=stock(r,y)
    if n:
        g=sum(t*t for t in y)/n
        assert 0<=g<=1
        assert sum(t*t for t in y)>=wedge(r,y)**2/n
def aligned(u,n=F(1)):
    """For r(0)=0, ||y(0)||²=n, tan(theta)=u, g=cos²theta."""
    source=n/(1+u*u)
    return n-source,source
times=[F(0),F(1),F(2),F(3),F(10),F(100)]
series={str(u):{"target":str(aligned(u)[0]),"source":str(aligned(u)[1])} for u in times}
assert series["1"]=={"target":"1/2","source":"1/2"}
assert series["10"]=={"target":"100/101","source":"1/101"}
assert wedge(cases[1][0],cases[1][1])==1
out={
 "source":"experiments/qpb1-source-reservoir/README.md v1.1 §§1-5",
 "carrier":"two R2 vectors in co-rotating matched top-cell/reservoir plane",
 "feedback":"CANDIDATE g=||y||²/N for N>0; g(0)=0, not source-selected",
 "update":"dr/du=g*y, dy/du=-g*r; native co-rotation factored out",
 "invariants":["N=||r||²+||y||²","D=r1*y2-r2*y1"],
 "no_go":"if D!=0 then ||y||² >= D²/N>0 under every scalar feedback g",
 "phase_generic":"D!=0 implies candidate g>=D²/N²>0, so continuous reciprocal exchanges do not latch",
 "aligned_initial_target_zero_exact_stock":series,
 "aligned_limit":"target->N and reservoir->0 only as u->infinity; no finite latching",
 "phase_cases":[{"r":list(map(str,r)),"y":list(map(str,y)),
                 "N":str(stock(r,y)),"D":str(wedge(r,y)),
                 "source_lower_bound":str(wedge(r,y)**2/stock(r,y)) if stock(r,y) else "0"}
                for r,y in cases],
 "null_control":"g=0: no transfer",
 "reversible_control":"fixed g>0: periodic transfer",
 "selection_status":"OPEN: stock feedback is a constitutive assumption",
 "physical_promotion":0,"checks":"PASS"}
print(json.dumps(out,indent=2,sort_keys=True))
