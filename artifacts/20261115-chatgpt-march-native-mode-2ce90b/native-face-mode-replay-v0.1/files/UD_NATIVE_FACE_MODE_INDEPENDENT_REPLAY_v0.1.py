#!/usr/bin/env python3
"""Independent stdlib-only exact replay of K4 face-gate covariance and dynamics."""
from itertools import product, combinations
from fractions import Fraction as F
import json
from pathlib import Path

def checks(N, faces):
    S=list(product((0,1),repeat=N))
    def A(state, face):
        x,y,z=[state[i] for i in face]
        return 0 if x==y==z else 1
    def phi(state):return [F(A(state,f))-F(3,4) for f in faces]
    d=len(faces)
    mean=[sum((F(A(s,faces[i])) for s in S),F(0))/len(S) for i in range(d)]
    assert all(x==F(3,4) for x in mean)
    cov=[[sum((phi(s)[i]*phi(s)[j] for s in S),F(0))/len(S)
          for j in range(d)] for i in range(d)]
    cgraph=[[F(len(set(combinations(faces[i],2)) & set(combinations(faces[j],2))),16)
             for j in range(d)] for i in range(d)]
    assert cov==cgraph
    q=1-F(4,N)
    for state in S:
        current=phi(state)
        nextsum=[F(0) for _ in range(d)]
        for vertex in range(N):
            flip=list(state);flip[vertex]=1-flip[vertex]
            for i,v in enumerate(phi(flip)):nextsum[i]+=v/F(N)
        assert nextsum==[q*a for a in current]
    if N==4 and d==4:
        admitted=[s for s in S if all(A(s,f) for f in faces)]
        assert len(admitted)==6
        assert all(sum(s)==2 for s in admitted)
        for s in admitted:
            for v in range(N):
                t=list(s);t[v]^=1
                assert not all(A(t,f) for f in faces)
    return {'vertices':N,'faces':d,'q':str(q),'cov':[[str(x) for x in row] for row in cov],
       'independent_exact_enumeration': 'PASS','conditional_transition': 'PASS'}

K4=list(combinations(range(4),3))
Glued=sorted(set(combinations([0,1,2,3],3))|set(combinations([0,1,2,4],3)))
result=[checks(4,K4),checks(5,K4),checks(5,Glued)]
assert result[0]['cov']==result[1]['cov']
assert result[0]['q']=='0' and result[1]['q']=='1/5'
print(json.dumps({'result':'PASS','cases':result,'isolated_vertex_control':'PASS'},indent=2))
