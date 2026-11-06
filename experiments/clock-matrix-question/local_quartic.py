"""Exact polynomial classification controls; newly authored, no external packages."""
from fractions import Fraction as F
from itertools import combinations
from collections import deque
from pathlib import Path
import json
from random import Random

N=14
ZERO=(0,)*N

def plus(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def times(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            key=tuple(x+y for x,y in zip(u,v))
            out[key]=out.get(key,F(0))+c*d
    return {k:v for k,v in out.items() if v}

def power(a,n):
    out={ZERO:F(1)}
    for _ in range(n):out=times(out,a)
    return out

def coordinate(i):
    t=list(ZERO);t[i]=1
    return {tuple(t):F(1)}

def rank(columns):
    pivots={}
    for col in columns:
        a=dict(col)
        while a:
            k=min(a)
            if k not in pivots:
                v=a[k];pivots[k]={u:w/v for u,w in a.items()};break
            v=a[k]
            a=plus(a,{u:-v*w for u,w in pivots[k].items()})
    return len(pivots)

def rank_mod(rows,p):
    # Independent dense row elimination on evaluation values, rather than coefficients.
    a=[list(row) for row in rows];r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],p-2,p);a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,len(a)):
            k=a[i][j]%p
            if k:a[i]=[(u-k*v)%p for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def run():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)]
    n=len(cells);assert n==15
    graph=[[] for _ in cells]
    for i,j in combinations(range(n),2):
        if abs(len(cells[i])-len(cells[j]))==1 and (set(cells[i])<set(cells[j]) or set(cells[j])<set(cells[i])):
            graph[i].append(j);graph[j].append(i)
    distances=[]
    for i in range(n):
        d=[99]*n;d[i]=0;q=deque([i])
        while q:
            v=q.popleft()
            for w in graph[v]:
                if d[w]==99:d[w]=d[v]+1;q.append(w)
        distances.append(d)
    assert max(map(max,distances))==4
    # Active hyperplane: x_3=-x_0-x_1-x_2, all nonvertex registers independent.
    xs=[coordinate(i) for i in range(3)]
    xs.append({k:-v for k,v in plus(plus(xs[0],xs[1]),xs[2]).items()})
    xs.extend(coordinate(i) for i in range(3,14))
    assert len(xs)==15
    norm2={}
    for x in xs:norm2=plus(norm2,power(x,2))
    target=power(norm2,2)
    reports=[]
    for radius in range(1,5):
        pairs=[(i,j) for i,j in combinations(range(n),2) if distances[i][j]<=radius]
        columns=[power(x,4) for x in xs]
        columns.extend(times(power(xs[i],a),power(xs[j],4-a)) for i,j in pairs for a in (1,2,3))
        r=rank(columns);aug=rank(columns+[target]);kernel=len(columns)-r
        reports.append(dict(radius=radius,allowed_pairs=len(pairs),monomial_count=len(columns),restriction_rank=r,restriction_kernel_dimension=kernel,augmented_radial_rank=aug,nonzero_radial_representable=(aug==r)))
    assert reports[0]['monomial_count']==99 and reports[0]['restriction_rank']==99
    assert reports[0]['augmented_radial_rank']==100
    assert [r['nonzero_radial_representable'] for r in reports]==[False,False,False,True]
    # Pairwise-distance cutoff4 is complete and reproduces norm^4 exactly.
    expanded={}
    for i in range(n):
        expanded=plus(expanded,power(xs[i],4))
        for j in range(i+1,n):
            expanded=plus(expanded,{k:2*v for k,v in times(power(xs[i],2),power(xs[j],2)).items()})
    assert expanded==target
    # Independent exact finite-field evaluation certificate for the central rank100.
    prime=1009
    assert all(prime%d for d in range(2,32))
    rng=Random(20261105);rows=[]
    local_pairs=[(i,j) for i,j in combinations(range(n),2) if distances[i][j]==1]
    for _ in range(120):
        z=[rng.randrange(prime) for _ in range(14)]
        x=z[:3]+[-sum(z[:3])%prime]+z[3:]
        row=[pow(v,4,prime) for v in x]
        row.extend(pow(x[i],a,prime)*pow(x[j],4-a,prime)%prime for i,j in local_pairs for a in (1,2,3))
        row.append(pow(sum(v*v for v in x),2,prime));rows.append(row)
    eval_rank=rank_mod(rows,prime);assert eval_rank==100
    opposite=(cells.index((0,1)),cells.index((2,3)))
    assert distances[opposite[0]][opposite[1]]==4
    return dict(evidence='EXACT_CONDITIONAL',active_constraint='sum of four vertex amplitudes=0',active_dimension=14,hasse_edges=sum(map(len,graph))//2,hasse_diameter=4,locality_class='homogeneous quartic monomials supported on one register or one distance-bounded pair',distance_sweep=reports,nearest_incidence_uniform_quartic_dimension=0,minimal_pair_distance_for_nonzero_radial=4,opposite_edge_witness=['01','23'],independent_evaluation_certificate={'field_prime':prime,'seed':20261105,'points':120,'augmented_rank':eval_rank,'scope':'second constructor implementation; not independent review'},native_coefficient_selection='OPEN',physical_promotion=0)

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('local_quartic_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
