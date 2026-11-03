#!/usr/bin/env python3
"""Exact fixed-shell 1->4 and 2->3 Pachner boundary-response audit."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations
import json


def simplices(tetrahedra):
    return {k: sorted({c for tet in tetrahedra for c in combinations(tet, k+1)})
            for k in range(4)}


def boundary_matrix(higher, lower):
    index = {simplex: i for i, simplex in enumerate(lower)}
    mat = [[Q(0) for _ in higher] for _ in lower]
    for j, simplex in enumerate(higher):
        for omitted in range(len(simplex)):
            face = simplex[:omitted] + simplex[omitted+1:]
            mat[index[face]][j] = Q((-1)**omitted)
    return mat


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def rank(A):
    A = [row[:] for row in A]
    if not A:
        return 0
    row = 0
    for col in range(len(A[0])):
        pivot = next((j for j in range(row,len(A)) if A[j][col]),None)
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        v = A[row][col]
        A[row] = [x/v for x in A[row]]
        for j in range(len(A)):
            if j != row and A[j][col]:
                v = A[j][col]
                A[j] = [a-v*b for a,b in zip(A[j],A[row])]
        row += 1
    return row


def determinant3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def oriented_volume6(tet, coords):
    p0, *points = [coords[i] for i in tet]
    return determinant3(*[tuple(p[j]-p0[j] for j in range(3)) for p in points])


def shell_and_volume(tetrahedra, coords):
    incidences = Counter(f for tet in tetrahedra for f in combinations(tet,3))
    shell = {f for f,count in incidences.items() if count == 1}
    oriented_shell = Counter()
    total6 = 0
    for tet in tetrahedra:
        six = oriented_volume6(tet, coords)
        assert six != 0
        sign = 1 if six > 0 else -1
        total6 += abs(six)
        for i in range(4):
            face = tet[:i]+tet[i+1:]
            oriented_shell[face] += sign*(-1)**i
    oriented_shell = {face: value for face,value in oriented_shell.items() if value}
    assert set(oriented_shell) == shell
    assert set(oriented_shell.values()) <= {-1,1}
    return shell, oriented_shell, Q(total6,6)


def laplacian(edges, nv):
    L = [[Q(0) for _ in range(nv)] for _ in range(nv)]
    for a,b in edges:
        L[a][a] += 1; L[b][b] += 1
        L[a][b] -= 1; L[b][a] -= 1
    return L


def inverse(A):
    n = len(A)
    A = [row[:] + [Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot = next((j for j in range(col,n) if A[j][col]),None)
        assert pivot is not None
        A[col], A[pivot] = A[pivot], A[col]
        v = A[col][col]
        A[col] = [x/v for x in A[col]]
        for j in range(n):
            if j != col:
                v = A[j][col]
                A[j] = [a-v*b for a,b in zip(A[j],A[col])]
    return [row[n:] for row in A]


def response(L, boundary):
    interior = [i for i in range(len(L)) if i not in boundary]
    bb = [[L[i][j] for j in boundary] for i in boundary]
    if not interior:
        return bb
    bi = [[L[i][j] for j in interior] for i in boundary]
    ib = [[L[i][j] for j in boundary] for i in interior]
    ii = [[L[i][j] for j in interior] for i in interior]
    correction = mul(mul(bi,inverse(ii)),ib)
    return [[bb[i][j]-correction[i][j] for j in range(len(boundary))]
            for i in range(len(boundary))]


def dynamic_response(L, boundary, omega_squared):
    shifted = [[L[i][j]-(omega_squared if i==j else 0)
                for j in range(len(L))] for i in range(len(L))]
    return response(shifted,boundary)


def mvec(A, v):
    return [sum(a*x for a,x in zip(row,v)) for row in A]


def energy(A, v):
    return sum(x*y for x,y in zip(v,mvec(A,v)))/2


def automorphisms(tetrahedra, coords, boundary):
    tets = set(tetrahedra)
    n = len(coords)
    d2 = lambda a,b: sum((a[i]-b[i])**2 for i in range(3))
    valid = []
    for p in permutations(range(n)):
        if {tuple(sorted(p[i] for i in tet)) for tet in tets} != tets:
            continue
        if {p[i] for i in boundary} != set(boundary):
            continue
        if any(d2(coords[i],coords[j]) != d2(coords[p[i]],coords[p[j]])
               for i in range(n) for j in range(i+1,n)):
            continue
        valid.append(p)
    return valid


def check_complex(tets):
    S = simplices(tets)
    B1 = boundary_matrix(S[1],S[0])
    B2 = boundary_matrix(S[2],S[1])
    B3 = boundary_matrix(S[3],S[2])
    assert all(v == 0 for row in mul(B1,B2) for v in row)
    assert all(v == 0 for row in mul(B2,B3) for v in row)
    f = tuple(len(S[k]) for k in range(4))
    ranks = (rank(B1),rank(B2),rank(B3))
    betti = (f[0]-ranks[0], f[1]-ranks[0]-ranks[1],
             f[2]-ranks[1]-ranks[2],f[3]-ranks[2])
    assert betti == (1,0,0,0)
    assert f[1]-ranks[0] == ranks[1]  # ker B1 = im B2, no H1 charge
    return S, f, ranks, betti


def case(name, coords, old, new, boundary, expected):
    S0,f0,r0,b0 = check_complex(old)
    S1,f1,r1,b1 = check_complex(new)
    shell0,chain0,volume0 = shell_and_volume(old,coords)
    shell1,chain1,volume1 = shell_and_volume(new,coords)
    assert shell0 == shell1 and chain0 == chain1 and volume0 == volume1
    assert all(set(face) <= set(boundary) for face in shell0)
    # The same snapped shell coordinates and face boundary are retained.
    L0 = laplacian(S0[1],len(S0[0]))
    L1 = laplacian(S1[1],len(S1[0]))
    A0 = response(L0,boundary)
    A1 = response(L1,boundary)
    Z0 = dynamic_response(L0,boundary,Q(1))
    Z1 = dynamic_response(L1,boundary,Q(1))
    group0 = automorphisms(old,coords,boundary)
    group1 = automorphisms(new,coords,boundary)
    assert set(group0) == set(group1)
    for p in group0:
        ix = [boundary.index(p[i]) for i in boundary]
        for A in (A0,A1):
            assert all(A[ix[i]][ix[j]] == A[i][j]
                       for i in range(len(ix)) for j in range(len(ix)))
    diff = [[A1[i][j]-A0[i][j] for j in range(len(boundary))]
            for i in range(len(boundary))]
    assert diff == expected['difference']
    v = expected['probe']
    assert mvec(A0,v) == [expected['old_eigen']*x for x in v]
    assert mvec(A1,v) == [expected['new_eigen']*x for x in v]
    assert mvec(Z0,v) == [(expected['old_eigen']-1)*x for x in v]
    assert mvec(Z1,v) == [(expected['new_eigen']-1)*x for x in v]
    assert mvec(A0,[Q(1)]*len(boundary)) == [0]*len(boundary)
    assert mvec(A1,[Q(1)]*len(boundary)) == [0]*len(boundary)
    return dict(name=name,coordinates=coords,old_tetrahedra=old,new_tetrahedra=new,
                boundary_faces=sorted(shell0),boundary_f_vector=(len(boundary),
                    len({e for face in shell0 for e in combinations(face,2)}),len(shell0)),
                old_f=f0,new_f=f1,old_boundary_ranks=r0,new_boundary_ranks=r1,
                old_edge_cycle_dimension=f0[1]-r0[0],
                new_edge_cycle_dimension=f1[1]-r1[0],
                old_betti=b0,new_betti=b1,volume=str(volume0),
                automorphism_order=len(group0),old_response=[[str(x) for x in row] for row in A0],
                new_response=[[str(x) for x in row] for row in A1],
                difference=[[str(x) for x in row] for row in diff],
                dynamic_omega_squared=1,
                old_dynamic_response=[[str(x) for x in row] for row in Z0],
                new_dynamic_response=[[str(x) for x in row] for row in Z1],
                probe=v,old_probe_energy=str(energy(A0,v)),new_probe_energy=str(energy(A1,v)),
                old_probe_eigen=expected['old_eigen'],new_probe_eigen=expected['new_eigen'])


def main():
    tetra = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)]
    one4_old = [(0,1,2,3)]
    one4_new = [tuple(sorted((*face,4))) for face in combinations(range(4),3)]
    K4 = [[Q(3 if i==j else -1) for j in range(4)] for i in range(4)]
    one4 = case('1-to-4',tetra,one4_old,one4_new,list(range(4)),dict(
        difference=[[x/4 for x in row] for row in K4],
        probe=[1,-1,0,0],old_eigen=4,new_eigen=5))
    assert one4['old_f'] == (4,6,4,1) and one4['new_f'] == (5,10,10,4)
    assert one4['automorphism_order'] == 24 and one4['volume'] == '8/3'

    # Equator lies in x+y+z=0. Apices and all coordinates are exact integers.
    bipyramid = [(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    two3_old = [(0,1,2,3),(0,1,2,4)]
    two3_new = [(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    v = [0,0,0,1,-1]
    two3 = case('2-to-3',bipyramid,two3_old,two3_new,list(range(5)),dict(
        difference=[[Q(v[i]*v[j]) for j in range(5)] for i in range(5)],
        probe=v,old_eigen=3,new_eigen=5))
    assert two3['old_f'] == (5,9,7,2) and two3['new_f'] == (5,10,9,3)
    assert two3['automorphism_order'] == 12 and two3['volume'] == '3'
    assert (two3['old_probe_energy'],two3['new_probe_energy']) == ('3','5')
    print(json.dumps({'source_base':'046bfb6cc3d69122cd30028d1fbb4ff8b42a40d9',
                      'edge_weights':'unit, assumed model metric',
                      'cases':[one4,two3]},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
