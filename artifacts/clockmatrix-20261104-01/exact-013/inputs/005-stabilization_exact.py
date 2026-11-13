"""Exact Hamiltonian spectral certificate for the eta=1 local penalty candidate."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import json

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def sc(a,c):return [[c*x for x in row] for row in a]
def add(*aa):return [[sum(a[i][j] for a in aa) for j in range(len(aa[0][0]))] for i in range(len(aa[0]))]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def null(a):
    a=[row[:] for row in a];piv=[];r=0;n=len(a[0])
    for j in range(n):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];z=a[r][j];a[r]=[x/z for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                z=a[k][j]
                if z:a[k]=[x-z*y for x,y in zip(a[k],a[r])]
        piv.append(j);r+=1
    basis=[]
    for free in range(n):
        if free in piv:continue
        x=[F(0)]*n;x[free]=1
        for i,j in enumerate(piv):x[j]=-a[i][free]
        basis.append(x)
    return tr(basis)
def definite_pivots(a):
    a=[r[:] for r in a];out=[]
    for k in range(len(a)):
        z=a[k][k];assert z;out.append(z)
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):a[i][j]-=a[i][k]*a[k][j]/z
    assert all(x>0 for x in out) or all(x<0 for x in out)
    return out

def run():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)];ix={s:i for i,s in enumerate(cells)};n=15
    d=[[F(0)]*n for _ in range(n)]
    for s in cells:
        if len(s)>1:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]]][ix[s]]=F((-1)**k)
    J=[[(d[i][j]-d[j][i])/2 for j in range(n)] for i in range(n)]
    v=[F(int(i==1)-int(i==2)) for i in range(n)];h=[r[1]-r[2] for r in J];z=[F(1,2)]*4+[F(0)]*11
    P=[[F(i==j)-z[i]*z[j]-(v[i]*v[j]+h[i]*h[j])/2 for j in range(n)] for i in range(n)]
    def Hess(q,p):
        B=[[F(0)]*n for _ in range(n)]
        for i in (1,2):B[i][i]=3*q*q+p*p
        for e in ((0,1),(0,2),(1,2),(1,3),(2,3)):B[ix[e]][ix[e]]=q*q+3*p*p
        for i,e,s in ((1,(0,1),-1),(1,(1,2),1),(1,(1,3),1),(2,(0,2),-1),(2,(1,2),-1),(2,(2,3),1)):B[i][ix[e]]=B[ix[e]][i]=s*q*p
        return B
    inactive=[0,3,10,11,12,13];active_edges=[ix[e] for e in ((0,1),(0,2),(1,2),(1,3),(2,3))]
    terms=[]
    for i in inactive:
        neighbors=[e for e in active_edges if d[i][e] or d[e][i]]
        w=sum(h[e]**2 for e in neighbors);assert w>0
        for e in neighbors:terms.append((i,e,F(1)/(2*w)))
    assert len(terms)==14
    # At qv+ph all inactive coordinates vanish: added gradient0, added Hess=p^2 D6.
    for q,p in ((F(1),F(0)),(F(0),F(1)),(F(1,2),F(3,2))):
        extra=[F(0)]*n
        for i,e,b in terms:extra[i]+=2*b*(p*h[e])**2
        assert extra==[p*p if i in inactive else 0 for i in range(n)]
    Bc=Hess(F(1),F(0));Bs=Hess(F(0),F(1));Bx=add(Hess(F(1),F(1)),sc(Bc,-1),sc(Bs,-1))
    for i in inactive:Bs[i][i]+=1
    T=mm(mm(P,add(sc(add(mm(J,add(sc(Bc,3),Bs)),mm(add(Bc,sc(Bs,3)),J),mm(mm(J,Bx),J),Bx),F(1,8)),sc(J,-1))),P)
    K=sc(mm(J,T),-1);assert K==tr(K)
    assert mm(P,P)==P and mm(P,T)==T and mm(T,P)==T
    T2=mm(T,T);freqs=[F(19,256),F(35,64),F(3,64)];reports=[]
    for f in freqs:
        basis=null(add(T2,sc(eye(n),f)))
        gram=mm(mm(tr(basis),K),basis);piv=definite_pivots(gram)
        reports.append({'frequency_squared':str(f),'real_subspace_dimension':len(basis[0]),'Krein_sign':'positive' if piv[0]>0 else 'negative','LDL_pivots':list(map(str,piv))})
    assert [r['real_subspace_dimension'] for r in reports]==[2,4,6]
    assert [r['Krein_sign'] for r in reports]==['positive','negative','positive']
    poly=T
    for f in freqs:poly=mm(poly,add(T2,sc(eye(n),f)))
    assert all(x==0 for row in poly for x in row)
    return {'evidence':'EXACT_CONDITIONAL','eta':'1 inverse-designed','positive_penalty_terms':[{'inactive_register':str(cells[i]),'active_edge':str(cells[e]),'coefficient':str(b)} for i,e,b in terms],
            'penalty_gradient_on_W':'zero','penalty_Hessian_on_W':'p^2 D6','average_annihilator':'t(t^2+19/256)(t^2+35/64)(t^2+3/64)',
            'transverse_blocks':reports,'weak_positive_conclusion':'all transverse Floquet multipliers unit modulus and semisimple for sufficiently small positive mu; endpoint not certified',
            'nonlinear_orbital_stability':'OPEN','native_parameter_selection':'OPEN','physical_promotion':0}
if __name__=='__main__':
    out=run();Path(__file__).with_name('stabilization_exact_results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
