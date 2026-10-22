"""Exact audit of the image-labelled four-cell complex; standard library only."""
from fractions import Fraction
from itertools import combinations, permutations
import json


def zeros(n, m): return [[0] * m for _ in range(n)]
def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return list(map(list, zip(*a)))
def mul(a, b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def rank(a):
    a = [[Fraction(x) for x in row] for row in a]; i = 0
    for j in range(len(a[0])):
        k = next((k for k in range(i, len(a)) if a[k][j]), None)
        if k is None: continue
        a[i], a[k] = a[k], a[i]; v = a[i][j]; a[i] = [x/v for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                v = a[k][j]; a[k] = [x-v*y for x,y in zip(a[k], a[i])]
        i += 1
        if i == len(a): break
    return i

def complex_of(tops):
    return [sorted({s for t in tops for s in combinations(t,k+1)}) for k in range(max(map(len,tops)))]
def inspect(tops):
    c = complex_of(tops); sizes = list(map(len,c)); bs = []
    for k in range(1,len(c)):
        b = zeros(sizes[k-1], sizes[k]); idx = {s:i for i,s in enumerate(c[k-1])}
        for j,t in enumerate(c[k]):
            for i in range(k+1): b[idx[t[:i]+t[i+1:]]][j] = (-1)**i
        bs.append(b)
    for x,y in zip(bs,bs[1:]): assert all(v == 0 for row in mul(x,y) for v in row)
    rs = [0]+list(map(rank,bs))+[0]
    betti = [n-rs[k]-rs[k+1] for k,n in enumerate(sizes)]
    a = zeros(sum(sizes), sum(sizes)); offsets = [sum(sizes[:k]) for k in range(len(c))]
    for k,b in enumerate(bs,1):
        for i,row in enumerate(b):
            for j,v in enumerate(row): a[offsets[k-1]+i][offsets[k]+j] = v; a[offsets[k]+j][offsets[k-1]+i] = -v
    assert all(a[i][j] == -a[j][i] for i in range(len(a)) for j in range(len(a)))
    return c,bs,a,{'f':sizes,'dimension':sum(sizes),'boundary_ranks':rs[1:-1],'betti_Q':betti}

def main():
    tops = [(0,1,2,3),(0,1,2,4),(0,1,3,4),(0,2,3,4)]
    cap = (1,2,3,4); closed = tops+[cap]
    cases={'four_cells':tops,'closed_boundary':closed,'filled_4_simplex':[(0,1,2,3,4)],'graph_only':list(combinations(range(5),2))}
    data={}; matrices={}
    for name,ts in cases.items():
        c,bs,a,d=inspect(ts); data[name]=d;matrices[name]=(c,bs,a)
        assert c[1]==list(combinations(range(5),2))
    assert data['four_cells']['f']==[5,10,10,4] and data['four_cells']['betti_Q']==[1,0,0,0]
    assert data['closed_boundary']['f']==[5,10,10,5] and data['closed_boundary']['betti_Q']==[1,0,0,1]
    assert data['filled_4_simplex']['f']==[5,10,10,5,1] and data['filled_4_simplex']['betti_Q']==[1,0,0,0,0]
    assert data['graph_only']['betti_Q']==[1,6]
    shared={','.join(map(str,(i+1,j+1))): sorted(set(t)&set(u)) for (i,t),(j,u) in combinations(enumerate(tops),2)}
    exterior=[list(set(t)-{0}) for t in tops]
    assert sorted(map(tuple,map(sorted,exterior)))==list(combinations(range(1,5),3))
    automorphisms=[p for p in permutations(range(5)) if {tuple(sorted(p[v] for v in t)) for t in tops}==set(tops)]
    assert len(automorphisms)==24 and all(p[0]==0 for p in automorphisms)
    # The oriented closed cycle is cap minus the consistently oriented four-cell chain.
    c,bs,a=matrices['closed_boundary']; coeff=[(-1)**next(v for v in range(5) if v not in t) for t in c[3]]
    assert mul(bs[2],[[v] for v in coeff])==zeros(10,1)
    assert all(coeff[i] == matrices['filled_4_simplex'][1][3][i][0] for i in range(5))
    # Adding the missing facet restores a single frequency in the chosen H=I model.
    for name,zero in [('closed_boundary',2),('filled_4_simplex',1),('graph_only',7)]:
        a=matrices[name][2];m=[[-x for x in row] for row in mul(a,a)]
        assert mul(m,m)==[[5*x for x in row] for row in m]
        assert rank(m)==len(a)-zero
        data[name]['unit_metric_spectral_certificate']={'M':'-A^2','M^2=5M':True,'rank':rank(m),'zero_multiplicity':zero,'nonzero_frequency':'sqrt(5)'}
    data.update(shared_faces_by_cell_pair=shared,outer_faces=exterior,vertex_cell_incidence=[sum(v in t for t in tops) for v in range(5)],complex_automorphism_count=len(automorphisms),graph_automorphism_count=120,internal_cell_graph='K4',exterior_augmented_dual_graph='K5',status='PASS')
    return data

if __name__ == '__main__': print(json.dumps(main(),indent=2))
