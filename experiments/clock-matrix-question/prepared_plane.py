"""Exact prepared-plane quartic construction and transverse checks, stdlib only."""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
from math import prod
import json

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def poly_pow(a,n):
    out=[F(1)]
    for _ in range(n):out=poly_mul(out,a)
    return out

def mv(A,x):return [sum(a*b for a,b in zip(row,x)) for row in A]
def dot(x,y):return sum(a*b for a,b in zip(x,y))

def solve(columns,target):
    n=len(columns);a=[[col[i] for col in columns]+[target[i]] for i in range(len(target))]
    pivots=[];r=0
    for j in range(n):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r];z=a[r][j];a[r]=[x/z for x in a[r]]
        for k in range(len(a)):
            if k!=r and a[k][j]:
                z=a[k][j];a[k]=[x-z*y for x,y in zip(a[k],a[r])]
        pivots.append(j);r+=1
    feasible=not any(all(x==0 for x in row[:n]) and row[n]!=0 for row in a)
    x=[F(0)]*n
    if feasible:
        for i,j in enumerate(pivots):x[j]=a[i][-1]
    return r,feasible,x

def build():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)];n=15;ix={s:i for i,s in enumerate(cells)}
    d=[[F(0)]*n for _ in range(n)]
    for s in cells:
        if len(s)>1:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]]][ix[s]]=F((-1)**k)
    J=[[(d[i][j]-d[j][i])/2 for j in range(n)] for i in range(n)]
    v=[F(int(s==(1,))-int(s==(2,))) for s in cells];h=mv(J,v)
    assert mv(J,h)==[-x for x in v] and dot(v,v)==dot(h,h)==2 and dot(v,h)==0
    pairs=[(i,j) for i,j in combinations(range(n),2) if d[i][j] or d[j][i]]
    even=[{i:4} for i in range(n)]+[{i:2,j:2} for i,j in pairs]
    odd=[{i:1,j:3} for i,j in pairs]+[{i:3,j:1} for i,j in pairs]
    monomials=even+odd
    def field_column(m):
        grad=[]
        for j in range(n):
            pol=[F(m.get(j,0))]
            if pol[0]:
                for i,p in m.items():pol=poly_mul(pol,poly_pow([v[i],h[i]],p-int(i==j)))
            else:pol=[F(0)]*4
            grad.append(pol)
        return [sum(J[i][j]*grad[j][k] for j in range(n)) for i in range(n) for k in range(4)]
    cols=[field_column(m) for m in monomials]
    # Polynomial coefficients indexed p power, remaining degree is q power.
    target=[z for i in range(n) for z in (h[i],-v[i],h[i],-v[i])]
    return cells,J,v,h,monomials,cols,target

def run():
    cells,J,v,h,monos,cols,target=build()
    reports=[];solutions=[]
    for count,name in ((43,'even quartics'),(99,'all nearest-incidence quartics')):
        rank,ok,coeff=solve(cols[:count],target)
        reports.append({'family':name,'coefficient_count':count,'constraint_rank':rank,'unit_shift_feasible':ok,'homogeneous_null_dimension':count-rank})
        if ok:assert all(sum(coeff[j]*cols[j][i] for j in range(count))==target[i] for i in range(60))
        solutions.append(coeff)
    # Signed S4 Reynolds average of all99 monomials, then the same cubic constraint.
    lookup={tuple(sorted(m.items())):i for i,m in enumerate(monos)}
    averaged=[]
    for m in monos:
        avg=[F(0)]*99
        for perm in permutations(range(4)):
            out={};sgn=1
            for i,power in m.items():
                image=[perm[a] for a in cells[i]]
                inversions=sum(image[a]>image[b] for a in range(len(image)) for b in range(a+1,len(image)))
                sgn*=(-1)**(inversions*power)
                out[cells.index(tuple(sorted(image)))]=power
            avg[lookup[tuple(sorted(out.items()))]]+=F(sgn,24)
        averaged.append(avg)
    invariant_cols=[[sum(a*cols[j][k] for j,a in enumerate(avg)) for k in range(60)] for avg in averaged]
    irank,iok,_=solve(invariant_cols,target)
    ambient_avg_rank,_,_=solve(averaged,[F(0)]*99)
    assert not iok
    coeff=solutions[0]
    def gradient(m,x):
        out=[F(0)]*15
        for i,power in m.items():
            z=F(power)
            for j,n in m.items():z*=x[j]**(n-int(j==i))
            out[i]=z
        return out
    fixtures=0
    for q in (F(-2),F(-1,2),F(0),F(1),F(2)):
        for p in (F(-2),F(-1,2),F(0),F(1),F(2)):
            x=[q*a+p*b for a,b in zip(v,h)];I=q*q+p*p
            g=[sum(a*gradient(m,x)[i] for a,m in zip(coeff,monos)) for i in range(15)]
            dx=mv(J,g);expected=[I*z for z in mv(J,x)]
            assert g==[I*z for z in x]
            assert dx==expected and dot(x,dx)==0 and dot(g,dx)==0
            Q=sum(a*prod(x[i]**n for i,n in m.items()) for a,m in zip(coeff,monos))
            assert Q==I*I/2;fixtures+=1
    # One local coefficient error at the q=p=1 point: epsilon*x_1^2*x_01^2.
    x=[a+b for a,b in zip(v,h)]
    port={cells.index((1,)):2,cells.index((0,1)):2}
    err=mv(J,gradient(port,x))
    tangent=[(dot(v,err)*v[i]+dot(h,err)*h[i])/2 for i in range(15)]
    leakage=[a-b for a,b in zip(err,tangent)]
    leakage2=dot(leakage,leakage);assert leakage2>0
    sparse=[{'coefficient' :str(c),'powers':{str(cells[j]):p for j,p in m.items()}} for c,m in zip(solutions[0],monos) if c]
    return {'evidence':'EXACT_CONDITIONAL','plane_v':list(map(str,v)),'plane_h':list(map(str,h)),
            'clock_action':'I=q^2+p^2','target_shift':'deltaOmega=lambda I','families':reports,'signed_S4':{'invariant_energy_dimension':ambient_avg_rank,'projected_constraint_rank':irank,'unit_shift_feasible':iok},'direct_gradient_fixtures':fixtures,'coefficient_error':{'term':'epsilon*x_vertex1^2*x_edge01^2','point':'q=p=1','transverse_derivative_norm_squared':str(leakage2)+'*epsilon^2'},'sparse_unit_shift_solution':sparse,'physical_promotion':0}

if __name__=='__main__':
    result=run();Path(__file__).with_name('prepared_plane_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2,sort_keys=True))
