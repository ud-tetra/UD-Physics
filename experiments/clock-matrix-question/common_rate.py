"""Exact constructor checks for common-rate classification and a posited Hamiltonian."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json

def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def scale(a,s): return [[s*x for x in row] for row in a]
def add(*aa): return [[sum(a[i][j] for a in aa) for j in range(len(aa[0]))] for i in range(len(aa[0]))]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def run():
    basis=[list(combinations(range(4),k+1)) for k in range(4)]
    cells=sum(basis,[]); ix={s:i for i,s in enumerate(cells)};n=len(cells)
    Ds=[]
    for degree in range(1,4):
        d=[[F(0)]*n for _ in range(n)]
        for s in basis[degree]:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]]][ix[s]]=F((-1)**k)
        Ds.append(d)
    Ks=[[[d[i][j]-d[j][i] for j in range(n)] for i in range(n)] for d in Ds]
    A=add(*Ks);J=scale(A,F(1,2));Ps=[scale(mm(k,k),F(-1,4)) for k in Ks]
    for i in range(3):
        assert mm(Ps[i],Ps[i])==Ps[i]
        for j in range(3):
            if i!=j:assert all(x==0 for row in mm(Ks[i],Ks[j]) for x in row)
    ranks=[int(sum(p[i][i] for i in range(n))) for p in Ps];assert ranks==[6,6,2]
    tuples=list(product((F(-1),F(0),F(1),F(2)),repeat=3))
    for gains in tuples:
        G=add(*(scale(k,g) for k,g in zip(Ks,gains)))
        common=(G==scale(A,gains[0]))
        assert common==(gains[0]==gains[1]==gains[2])
    # Positive metric: a nonzero environment block cannot disappear at second order.
    C=[[F(1),F(2)],[F(-2),F(1)]]
    Ct=list(map(list,zip(*C)));CCt=mm(C,Ct)
    assert CCt==[[F(5),F(0)],[F(0),F(5)]]
    x=[F(0)]*n;x[ix[(1,)]]=1;x[ix[(2,)]]=-1
    y=[v/2 for v in x]
    assert mv(add(*Ps),x)==x and mv(add(*Ps),y)==y
    IL,IR=dot(x,x)/2,dot(y,y)/2
    rates=[]
    for g in (F(0),F(1,2),F(1),F(2)):
        ol,orr=2+g*IR,2+g*IL
        gx=[ol*v for v in x];gy=[orr*v for v in y]
        dx,dy=mv(J,gx),mv(J,gy)
        assert dot(x,dx)==dot(y,dy)==0
        assert dot(gx,dx)+dot(gy,dy)==0
        assert dx==[ol/2*v for v in mv(A,x)]
        rates.append({'g_assumed':str(g),'I_L':str(IL),'I_R':str(IR),
                      'omega_L':str(ol),'omega_R':str(orr),'ratio':str(ol/orr)})
    return {'evidence':'EXACT_CONDITIONAL','sector_ranks':ranks,'gain_triples_checked':len(tuples),
            'oriented_common_rate_condition':'g1=g2=g3=r>0',
            'environment_curvature_control':[['5','0'],['0','5']],
            'posited_nonlinear_H':'2(I_L+I_R)+g I_L I_R','nonlinear_controls':rates,
            'native_g_selection':'OPEN','physical_promotion':0}
if __name__=='__main__':
    Path(__file__).with_name('common_rate_results.json').write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
    print('PASS: 64 exact gain triples, tetrahedral projectors, second-order leakage and four nonlinear Hamiltonian controls')
