#!/usr/bin/env python3
"""Exact K4 1->4 ownership-current and candidate retention event audit; stdlib only."""
from fractions import Fraction as F
from itertools import combinations
import json

tetra=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
simplices=sorted({s for t in tetra for k in range(1,5) for s in combinations(t,k)},key=lambda s:(len(s),s))
weights={(s,t):F(1,sum(set(s).issubset(tt) for tt in tetra))
         for s in simplices for t in tetra if set(s).issubset(t)}
assert len(simplices)==29
assert all(sum((weights.get((s,t),F(0)) for t in tetra),F(0))==1 for s in simplices)
face=(0,1,4);cell=(0,1,2,4)
assert [weights[(face,t)] for t in tetra if (face,t) in weights]==[F(1,2),F(1,2)]
c={s:F(int(s in (face,cell))) for s in simplices}
def stock(c):
    return {t:sum((weights.get((s,t),F(0))*v*v for s,v in c.items()),F(0)) for t in tetra}
def incidence(s,t):
    if len(t)!=len(s)+1:return 0
    return sum((-1)**j for j in range(len(t)) if t[:j]+t[j+1:]==s)
def deriv_direct(c):
    d={}
    for s in simplices:
        dc=sum((incidence(s,t)*c[t] for t in simplices),F(0))-sum((incidence(t,s)*c[t] for t in simplices),F(0))
        d[s]=2*c[s]*dc
    return {t:sum((weights.get((s,t),F(0))*d[s] for s in simplices),F(0)) for t in tetra}
def deriv_current(c):
    d={t:F(0) for t in tetra}
    for s in simplices:
        for t in simplices:
            B=incidence(s,t)
            if B:
                J=-2*B*c[s]*c[t] # signed from lower simplex to upper simplex
                for cell0 in tetra:
                    d[cell0]+=(weights.get((t,cell0),F(0))-weights.get((s,cell0),F(0)))*J
    return d
direct=deriv_direct(c)
assert direct==deriv_current(c)
assert sum(direct.values())==0
assert direct[cell]==-1 and direct[(0,1,3,4)]==1
def event(engage):
    post=c.copy(); retained={t:F(0) for t in tetra}
    if engage:
        post[face]=F(0)
        for t in tetra:retained[t]=weights.get((face,t),F(0))
    before=sum(stock(c).values(),F(0))
    after=sum(stock(post).values(),F(0))+sum(retained.values(),F(0))
    assert before==after==2 and all(v>=0 for v in retained.values())
    return {"engage":engage,"before_total":str(before),"after_transport_stock":str(sum(stock(post).values(),F(0))),
            "retained_by_cell":{str(t):str(v) for t,v in retained.items()},
            "retained_total":str(sum(retained.values(),F(0))),"combined_total":str(after)}
result={"complex":"1-to-4 centroid K4 ball","f_vector":[5,10,10,4],
"shared_face":str(face),"face_multiplicity":2,"face_cell_weights":["1/2","1/2"],
"initial_nonzero_amplitudes":[str(face),str(cell)],
"cell_current_derivative":{str(k):str(v) for k,v in direct.items()},
"current_identity":"PASS","sum_cell_current_derivative":str(sum(direct.values(),F(0))),
"null_branch":event(False),"capture_branch":event(True),
"selection_status":"OPEN: both branches conserve stock; capture is an assumed one-way update",
"fixed_point_claim":"NO: retained stock persists only if reverse transfer is excluded as a separate assumption",
"physical_promotion":0}
print(json.dumps(result,indent=2,sort_keys=True))
