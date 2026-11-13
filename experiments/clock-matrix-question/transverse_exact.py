"""Exact weak-coupling transverse certificate and nonlinear readout window."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(*aa):return [[sum(a[i][j] for a in aa) for j in range(15)] for i in range(15)]
def sc(a,c):return [[c*x for x in row] for row in a]
def eye():return [[F(i==j) for j in range(15)] for i in range(15)]
def rank(a):
    a=[row[:] for row in a];r=0
    for j in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r];z=a[r][j];a[r]=[x/z for x in a[r]]
        for k in range(r+1,len(a)):
            z=a[k][j]
            if z:a[k]=[x-z*y for x,y in zip(a[k],a[r])]
        r+=1
    return r

def run():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)];ix={s:i for i,s in enumerate(cells)}
    d=[[F(0)]*15 for _ in range(15)]
    for s in cells:
        if len(s)>1:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]]][ix[s]]=F((-1)**k)
    J=[[(d[i][j]-d[j][i])/2 for j in range(15)] for i in range(15)]
    v=[F(int(i==1)-int(i==2)) for i in range(15)];h=[sum(a*b for a,b in zip(row,v)) for row in J]
    harmonic=[F(1,2)]*4+[F(0)]*11
    PN=[[F(i==j)-harmonic[i]*harmonic[j]-(v[i]*v[j]+h[i]*h[j])/2 for j in range(15)] for i in range(15)]
    def Hess(q,p):
        a=[[F(0)]*15 for _ in range(15)]
        for i in (1,2):a[i][i]=3*q*q+p*p
        for e in ((0,1),(0,2),(1,2),(1,3),(2,3)):a[ix[e]][ix[e]]=q*q+3*p*p
        for i,e,sgn in ((1,(0,1),-1),(1,(1,2),1),(1,(1,3),1),(2,(0,2),-1),(2,(1,2),-1),(2,(2,3),1)):
            a[i][ix[e]]=a[ix[e]][i]=sgn*q*p
        return a
    Bc,Bs=Hess(F(1),F(0)),Hess(F(0),F(1));Bx=add(Hess(F(1),F(1)),sc(Bc,-1),sc(Bs,-1))
    T=mm(mm(PN,add(sc(add(mm(J,add(sc(Bc,3),Bs)),mm(add(Bc,sc(Bs,3)),J),mm(mm(J,Bx),J),Bx),F(1,8)),sc(J,-1))),PN)
    ident=eye();T2=mm(T,T)
    nulls={'zero':15-rank(T),'plus3/8':15-rank(add(T,sc(ident,F(-3,8)))),'minus3/8':15-rank(add(T,sc(ident,F(3,8)))),'plus1/4':15-rank(add(T,sc(ident,F(-1,4)))),'minus1/4':15-rank(add(T,sc(ident,F(1,4)))),'imaginary_pair':15-rank(add(T2,ident))}
    assert nulls=={'zero':3,'plus3/8':1,'minus3/8':1,'plus1/4':3,'minus1/4':3,'imaginary_pair':4}
    poly=mm(mm(T,add(T2,sc(ident,F(-9,64)))),mm(add(T2,sc(ident,F(-1,16))),add(T2,ident)))
    assert all(x==0 for row in poly for x in row)
    assert mm(PN,PN)==PN and rank(PN)==12
    assert mm(mm(PN,J),PN)==mm(J,PN)
    # e^(4/3)<4: finite rational series plus a geometric upper bound for the tail.
    x=F(4,3);term=F(1);s=term
    for k in range(1,16):term*=x/k;s+=term
    nxt=term*x/16;upper=s+nxt/(1-x/17)
    assert upper<4
    # pi<22/7 bounds one-orbit exponent143*pi/344 by4/3.
    assert F(143*22,344*7)<F(4,3)
    # asin(1/(1024 sqrt2))<1/1000 via 1/sqrt2<3/4 and sinz>=z-z^3/6.
    z=F(1,1000)
    assert F(3,4096)<z-z**3/6
    return {'evidence':'EXACT_CONDITIONAL','transverse_dimension':12,'averaged_generator_eigenspace_dimensions':nulls,
            'averaged_minimal_polynomial':'t(t^2-9/64)(t^2-1/16)(t^2+1)',
            'zero_eigenspace_scope':'three excluded tangent/harmonic coordinates; no transverse zero',
            'weak_coupling_multiplier':'-[1+(3*pi/8)rho+O(rho^2)]; unstable for sufficiently small rho>0',
            'native_growth_exponent':'3*mu/8+O(mu^2), mu=lambda I',
            'finite_window':{'reference_I':'1','lambda':'1/64','reference_initial':'q=1,p=0','initial_error_norm_max':'1/4096','both_energy_max':'33/16','duration':'128*pi/129 native parameter units','state_error_norm_bound':'<1/1024','phase_error_bound':'<1/1000 rad','nonlinear_L_bound':'13*lambda*R^2','exponential_growth_bound':'exp(143*pi/344)<4'},
            'physical_promotion':0}
if __name__=='__main__':
    r=run();Path(__file__).with_name('transverse_exact_results.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
