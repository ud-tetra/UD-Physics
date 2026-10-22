"""Exact finite-complex analysis; standard library only, unit chain metric."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb
import json


def zeros(n, m): return [[0] * m for _ in range(n)]
def ident(n): return [[int(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return list(map(list, zip(*a)))
def add(a, b, scale=1): return [[x + scale*y for x, y in zip(r, s)] for r, s in zip(a, b)]
def mul(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(r, c)) for c in bt] for r in a]
def rank(a):
    a = [[Q(x) for x in row] for row in a]
    i = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None: continue
        a[i], a[pivot] = a[pivot], a[i]
        value = a[i][j]; a[i] = [x/value for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                value = a[k][j]; a[k] = [x-value*y for x, y in zip(a[k], a[i])]
        i += 1
        if i == len(a): break
    return i
def complex_of(tops):
    return [sorted({f for t in tops for f in combinations(t, k+1)}) for k in range(4)]
def boundary(cells):
    maps = []
    for k in range(1, 4):
        b = zeros(len(cells[k-1]), len(cells[k]))
        lookup = {f:i for i, f in enumerate(cells[k-1])}
        for j, simplex in enumerate(cells[k]):
            for s in range(k+1):
                face = simplex[:s] + simplex[s+1:]
                if face in lookup: b[lookup[face]][j] = (-1)**s
        maps.append(b)
    return maps
def generator(cells):
    bs = boundary(cells); sizes = [len(c) for c in cells]
    offsets = [sum(sizes[:k]) for k in range(4)]; a = zeros(sum(sizes), sum(sizes))
    for k, b in enumerate(bs, start=1):
        for i, row in enumerate(b):
            for j, value in enumerate(row):
                a[offsets[k-1]+i][offsets[k]+j] = value
                a[offsets[k]+j][offsets[k-1]+i] = -value
    assert add(a, transpose(a)) == zeros(len(a), len(a))
    assert mul(bs[0], bs[1]) == zeros(sizes[0], sizes[2])
    assert mul(bs[1], bs[2]) == zeros(sizes[1], sizes[3])
    return a, bs
def flat(cells): return [s for degree in cells for s in degree]
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def analyze():
    parent = complex_of([(0,1,2,3)])
    tops = [tuple(sorted((4,) + face)) for face in combinations(range(4), 3)]
    full = complex_of(tops)
    exterior = [[s for s in degree if 4 not in s] for degree in full]; exterior[3] = []
    interior = [[s for s in degree if 4 in s] for degree in full]
    a, bs = generator(full); ap, _ = generator(parent); ar, br = generator(interior)
    assert [len(c) for c in full] == [5,10,10,4]
    assert [len(c) for c in interior] == [1,4,6,4]
    assert [rank(b) for b in bs] == [4,6,4]
    face_owners = {f:[t for t in tops if set(f) <= set(t)] for f in full[2]}
    assert sum(len(v)==1 for v in face_owners.values()) == 4
    assert sum(len(v)==2 for v in face_owners.values()) == 6
    for t in tops:
        assert sorted(len(face_owners[f]) for f in combinations(t,3)) == [1,2,2,2]
    assert all(len(set(t)&set(u))==3 for t,u in combinations(tops,2))
    # Explicit signed complement permutation, parent degree 3-q -> relative degree q.
    p = zeros(15,15); parent_index = {s:i for i,s in enumerate(flat(parent))}
    for i, simplex in enumerate(flat(interior)):
        subset = tuple(v for v in simplex if v != 4); q = len(subset)
        complement = tuple(v for v in range(4) if v not in subset)
        word = subset + complement
        parity = sum(word[j] > word[k] for j in range(4) for k in range(j+1,4))
        p[i][parent_index[complement]] = (-1)**(q*(q+1)//2 + parity)
    assert mul(p,transpose(p)) == ident(15)
    assert mul(mul(p,ap),transpose(p)) == ar
    def action(cells, permutation):
        index={s:i for i,s in enumerate(flat(cells))}; rho=zeros(len(index),len(index))
        for j,s in enumerate(flat(cells)):
            word=tuple(permutation[v] if v<4 else 4 for v in s)
            inversions=sum(word[k]>word[l] for k in range(len(word)) for l in range(k+1,len(word)))
            rho[index[tuple(sorted(word))]][j]=(-1)**inversions
        return rho
    for permutation in permutations(range(4)):
        sign=(-1)**sum(permutation[i]>permutation[j] for i in range(4) for j in range(i+1,4))
        lhs=mul(action(interior,permutation),p)
        rhs=[[sign*x for x in row] for row in mul(p,action(parent,permutation))]
        assert lhs==rhs  # Complement duality includes the orientation character.
    signs=[(-1)**(next(v for v in range(4) if v not in t)+1) for t in tops]
    coherent_full=[[x*signs[j] for j,x in enumerate(row)] for row in bs[2]]
    coherent_rel=[[x*signs[j] for j,x in enumerate(row)] for row in br[2]]
    j4=[[1]*4 for _ in range(4)]
    assert mul(transpose(coherent_rel),coherent_rel)==add([[4*x for x in row] for row in ident(4)],j4,-1)
    assert mul(transpose(coherent_full),coherent_full)==add([[5*x for x in row] for row in ident(4)],j4,-1)
    # Spectral certificates use symmetric -A^2 and integer polynomial identities.
    m = [[-x for x in row] for row in mul(a,a)]
    assert mul(mul(m,add(m,ident(29),-1)),add(m,ident(29),-5)) == zeros(29,29)
    trace = sum(m[i][i] for i in range(29)); m2 = mul(m,m)
    trace2 = sum(m2[i][i] for i in range(29))
    assert (trace,trace2,rank(m)) == (132,652,28)
    n5 = (trace2-trace)//20; n1 = trace-5*n5; n0=29-n1-n5
    assert (n0,n1,n5)==(1,2,26)
    mp = [[-x for x in row] for row in mul(ap,ap)]
    assert mul(mp,mp) == [[4*x for x in row] for row in mp]
    assert rank(mp)==14
    ff = flat(full); bi = [i for i,s in enumerate(ff) if 4 not in s]
    ii = [i for i,s in enumerate(ff) if 4 in s]
    coupling = [[a[i][j] for j in ii] for i in bi]
    assert rank(coupling)==14  # Relative dynamics is not an invariant full-system block.
    v = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)]
    def volume(t):
        rows = [[v[t[j]][d]-v[t[0]][d] for d in range(3)] for j in (1,2,3)]
        return Q(abs(det3(rows)),6)
    vp = volume((0,1,2,3)); volumes = [volume(t) for t in tops]
    assert vp==Q(8,3) and all(x==vp/4 for x in volumes)
    def sqdist(i,j): return sum((x-y)**2 for x,y in zip(v[i],v[j]))
    assert {sqdist(i,j) for i,j in combinations(range(4),2)}=={8}
    assert {sqdist(i,4) for i in range(4)}=={3}
    def area_squared(t):
        u=[v[t[1]][d]-v[t[0]][d] for d in range(3)]
        w=[v[t[2]][d]-v[t[0]][d] for d in range(3)]
        return Q(sum(x*x for x in u)*sum(x*x for x in w)-sum(x*y for x,y in zip(u,w))**2,4)
    assert area_squared((0,1,2))==12 and area_squared((0,1,4))==2
    assert area_squared((0,1,4))/area_squared((0,1,2))==Q(1,6)
    for vertex in v[:4]:
        linear=[[Q(i==j)-Q(vertex[i]*vertex[j],4) for j in range(3)] for i in range(3)]
        assert det3(linear)==Q(1,4)
        assert rank(add(linear,ident(3),-1))==1
        assert mul(add(linear,ident(3),-1),add(linear,[[Q(x,4) for x in row] for row in ident(3)],-1))==zeros(3,3)
    # Enumerate two recursive levels, independently checking count formulas.
    recursive = [(0,1,2,3)]; next_vertex=4; recursion=[]
    for level in range(3):
        counts = [len(x) for x in complex_of(recursive)]; n=4**level
        expected=[(n+11)//3,(4*n+14)//3,2*n+2,n]
        assert counts==expected
        if level:
            boundary_cells=sum(any(4 > max(face) for face in combinations(t,3)) for t in recursive)
            assert boundary_cells==4
        recursion.append({'level':level,'face_vector':counts,'equal_volume_fraction':str(Q(1,n))})
        refined=[]
        for t in recursive:
            for face in combinations(t,3): refined.append(tuple(sorted(face+(next_vertex,))))
            next_vertex+=1
        recursive=refined
    return {'scope':'Exact for labelled 1->4 central subdivision; unweighted Euclidean chain metric H=I for operators; no physical calibration.',
            'face_vector':[5,10,10,4],'boundary_face_vector':[4,6,4,0],
            'relative_face_vector':[1,4,6,4],'chain_dimensions':{'parent':15,'boundary':14,'relative':15,'full':29},
            'boundary_ranks':[4,6,4],'betti':[1,0,0,0],
            'outer_faces':4,'shared_faces':6,'dual_cell_graph':'K4',
            'geometry':{'parent_volume':str(vp),'child_volumes':list(map(str,volumes)),
                        'radial_over_outer_edge_squared':'3/8','inner_over_outer_face_area_squared':'1/6'},
            'signed_complement_intertwiner':p,'relative_equals_parent_skew_dynamics_up_to_P':True,
            'S4_duality':'rho_relative(g)*P = sign(g)*P*rho_parent(g), verified for all24 permutations',
            'cell_gram_operators':{'internal_faces':'4I-J','all_faces':'5I-J'},
            'characteristic_polynomials':{'parent_and_relative':'lambda*(lambda^2+4)^7','full':'lambda*(lambda^2+1)*(lambda^2+5)^13'},
            'full_squared_frequency_multiplicities':{'0':n0,'1':n1,'5':n5},
            'spectral_certificate':{'M_definition':'-A^2','M*(M-I)*(M-5I)':0,'trace_M':trace,'trace_M_squared':trace2},
            'boundary_interior_coupling_rank':rank(coupling),'relative_subspace_invariant_in_full_flow':False,
            'recursive_counts_checks':recursion,'status':'PASS'}


if __name__=='__main__': print(json.dumps(analyze(),indent=2))
