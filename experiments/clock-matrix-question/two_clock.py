"""Two filled tetrahedra and a declared bridge; exact standard-library replay."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def charpoly(a):
    n=len(a); B=[[F(i==j) for j in range(n)] for i in range(n)]; out=[F(1)]
    for k in range(1,n+1):
        B=mm(a,B); c=-sum(B[i][i] for i in range(n))/k; out.append(c)
        for i in range(n): B[i][i]+=c
    return out
def replay(w):
    cells=[tuple(range(4)),tuple(range(4,8))]
    basis=[sorted(set(s for c in cells for s in combinations(c,k+1))) for k in range(4)]
    basis[1]=sorted(basis[1]+[(0,4)])
    simplices=sum(basis,[]); ix={s:i for i,s in enumerate(simplices)}; n=len(simplices)
    d=[[F(0) for _ in range(n)] for _ in range(n)]
    for s in simplices:
        if len(s)>1:
            for j in range(len(s)):
                d[ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)*(w if s==(0,4) else 1)
    assert all(x==0 for row in mm(d,d) for x in row)
    A=[[d[i][j]-d[j][i] for j in range(n)] for i in range(n)]
    assert all(A[i][j]==-A[j][i] for i in range(n) for j in range(n))
    clocks=[]
    for p,q in [(1,2),(5,6)]:
        v=[F(0)]*n;v[ix[(p,)]]=1;v[ix[(q,)]]=-1
        h=[x/2 for x in mv(A,v)]
        assert mv(A,h)==[-2*x for x in v]
        assert sum(x*x for x in v)==sum(x*x for x in h)==2
        assert h[ix[(0,4)]]==0
        clocks.append((v,h))
    assert all(sum(x*y for x,y in zip(u,v))==0 for u in clocks[0] for v in clocks[1])
    B1=[row[8:21] for row in d[:8]]; L=mm(B1,list(map(list,zip(*B1))))
    expected=poly_mul([F(1),F(0)],[F(1),-(4+2*w*w),2*w*w])
    for _ in range(5): expected=poly_mul(expected,[F(1),F(-4)])
    assert charpoly(L)==expected
    return {'bridge_boundary_weight':str(w),'bridge_Laplacian_weight':str(w*w),
            'f_vector':list(map(len,basis)),'carrier_dimension':n,
            'vertex_charpoly_descending':[str(x) for x in expected],
            'protected_clock_frequencies':['2','2'],'relative_rate':'1',
            'other_squared_frequencies_polynomial':f'lambda^2 - ({4+2*w*w}) lambda + ({2*w*w})'}
if __name__=='__main__':
    out={'evidence':'EXACT_CONDITIONAL','cases':[replay(w) for w in (F(0),F(1,2),F(1),F(2))],
         'unit_bridge_other_squared_frequencies':'3-sqrt(7), 3+sqrt(7)',
         'coupling_origin':'declared topology/weight; not source-selected physical interaction',
         'physical_time_map':'OPEN','physical_promotion':0}
    Path(__file__).with_name('two_clock_results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS: 4 exact bridge weights; boundary nilpotence, skewness, two independent clocks and characteristic polynomials')
