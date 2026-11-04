#!/usr/bin/env python3
"""Exact boundary-fixed, symmetry-equivariant Pachner chain transport audit."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

source = Path(__file__).parents[1] / 'pachner-boundary-observability' / 'audit.py'
spec = importlib.util.spec_from_file_location('prior_pachner_audit', source)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def zero(rows,cols):
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def eq(A,B):
    return len(A)==len(B) and all(a==b for a,b in zip(A,B))


def geometric_fundamental(tets,coords):
    return [Q(1 if prior.oriented_volume6(tet,coords)>0 else -1) for tet in tets]


def maps_case(coords,old,new,shell,alpha=None):
    O,N = prior.simplices(old),prior.simplices(new)
    Mo = []
    for k in range(4):
        Mo.append(zero(len(N[k]),len(O[k])))
    for k in (0,1,2):
        index = {s:i for i,s in enumerate(N[k])}
        for j,simplex in enumerate(O[k]):
            if simplex in index:
                Mo[k][index[simplex]][j] = Q(1)
    fold, fnew = geometric_fundamental(O[3],coords),geometric_fundamental(N[3],coords)
    if len(old)==1:  # 1->4: integral fundamental and identity on old boundary
        for j in range(len(new)):
            Mo[3][j][0] = fold[0]*fnew[j]
    else:  # 2->3: split total fundamental with alpha, 1-alpha
        alpha = Q(1,2) if alpha is None else Q(alpha)
        for j in range(len(new)):
            Mo[3][j][0] = fold[0]*alpha*fnew[j]
            Mo[3][j][1] = fold[1]*(1-alpha)*fnew[j]
        internal = next(f for f in O[2] if f not in shell)
        idx = O[2].index(internal)
        B3o = prior.boundary_matrix(O[3],O[2])
        B3n = prior.boundary_matrix(N[3],N[2])
        rhs = [sum(B3n[i][j]*Mo[3][j][0] for j in range(len(new)))
               for i in range(len(N[2]))]
        for j,f in enumerate(O[2]):
            if j != idx:
                for i in range(len(N[2])):
                    rhs[i] -= B3o[j][0]*Mo[2][i][j]
        pivot = B3o[idx][0]
        assert pivot in (-1,1)
        for i in range(len(N[2])):
            Mo[2][i][idx] = rhs[i]/pivot
    for k in (1,2,3):
        Bo = prior.boundary_matrix(O[k],O[k-1])
        Bn = prior.boundary_matrix(N[k],N[k-1])
        assert eq(prior.mul(Mo[k-1],Bo),prior.mul(Bn,Mo[k])), k
    assert prior.mvec(Mo[3],fold)==fnew  # relative degree +1
    return O,N,Mo,fold,fnew


def permutation_rep(simplices,p):
    index={s:i for i,s in enumerate(simplices)}
    M=zero(len(simplices),len(simplices))
    for j,s in enumerate(simplices):
        word=[p[i] for i in s]
        target=tuple(sorted(word))
        inversions=sum(word[i]>word[k] for i in range(len(word))
                       for k in range(i+1,len(word)))
        M[index[target]][j]=Q((-1)**inversions)
    return M


def equivariance(O,N,Mo,group):
    good=[]
    for p in group:
        holds=True
        for k in range(4):
            Ro=permutation_rep(O[k],p)
            Rn=permutation_rep(N[k],p)
            if not eq(prior.mul(Mo[k],Ro),prior.mul(Rn,Mo[k])):
                holds=False
        if holds:good.append(p)
    return len(good)


def skew_generator(S):
    sizes=[len(S[k]) for k in range(4)]
    offsets=[sum(sizes[:k]) for k in range(4)]
    A=zero(sum(sizes),sum(sizes))
    for k in (1,2,3):
        B=prior.boundary_matrix(S[k],S[k-1])
        for i in range(sizes[k-1]):
            for j in range(sizes[k]):
                A[offsets[k-1]+i][offsets[k]+j]=B[i][j]
                A[offsets[k]+j][offsets[k-1]+i]=-B[i][j]
    return A


def block_diag(Mo):
    nr=sum(len(m) for m in Mo)
    nc=sum(len(m[0]) for m in Mo)
    M=zero(nr,nc)
    r=c=0
    for m in Mo:
        for i,row in enumerate(m):
            for j,v in enumerate(row):
                M[r+i][c+j]=v
        r+=len(m);c+=len(m[0])
    return M


def intertwiner_failure(O,N,Mo):
    Ao,An=skew_generator(O),skew_generator(N)
    M=block_diag(Mo)
    lhs,rhs=prior.mul(An,M),prior.mul(M,Ao)
    return sum(a!=b for rowa,rowb in zip(lhs,rhs) for a,b in zip(rowa,rowb))


def weighted_laplacian(edges,nv,weights):
    L=zero(nv,nv)
    for a,b in edges:
        w=Q(weights(a,b))
        L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
    return L


def weighted_check(O,N,old_tets,new_tets,boundary):
    ao=prior.response(prior.laplacian(O[1],len(O[0])),boundary)
    extras=set(N[1])-set(O[1])
    assert len(extras)==(4 if len(old_tets)==1 else 1)
    data={}
    for g in ((Q(1),Q(2),Q(3)) if len(old_tets)==1 else (Q(0),Q(1),Q(2))):
        L=weighted_laplacian(N[1],len(N[0]),
                             lambda a,b: g if (a,b) in extras else 1)
        an=prior.response(L,boundary)
        delta=[[an[i][j]-ao[i][j] for j in range(len(boundary))]
               for i in range(len(boundary))]
        if len(old_tets)==1:
            assert delta==[[g*ao[i][j]/4 for j in range(4)] for i in range(4)]
        else:
            v=[0,0,0,1,-1]
            assert delta==[[g*v[i]*v[j] for j in range(5)] for i in range(5)]
        data[str(g)]=[[str(v) for v in row] for row in delta]
    return data


def main():
    cases=[]
    coords=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)]
    old=[(0,1,2,3)]
    new=[tuple(sorted((*f,4))) for f in combinations(range(4),3)]
    cases.append(('1-to-4',coords,old,new,list(range(4))))
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    cases.append(('2-to-3',coords,old,new,list(range(5))))
    out=[]
    for name,coords,old,new,boundary in cases:
        shell,_,_=prior.shell_and_volume(old,coords)
        O,N,M,fo,fn=maps_case(coords,old,new,shell)
        group=prior.automorphisms(old,coords,boundary)
        assert set(group)==set(prior.automorphisms(new,coords,boundary))
        good=equivariance(O,N,M,group)
        assert good==len(group)
        weighted=weighted_check(O,N,old,new,boundary)
        mismatch=intertwiner_failure(O,N,M)
        assert mismatch>0
        row=dict(move=name,group_order=len(group),equivariant_count=good,
                 coefficient_domain='Z' if all(v.denominator==1 for mat in M for line in mat for v in line) else 'Q',
                 denominators=sorted({v.denominator for mat in M for line in mat for v in line}),
                 relative_fundamental_old=[str(v) for v in fo],
                 relative_fundamental_new=[str(v) for v in fn],
                 old_top_stock=str(sum(v*v for v in fo)),new_top_stock=str(sum(v*v for v in fn)),
                 chain_map=[[[str(v) for v in line] for line in mat] for mat in M],
                 unit_metric_generator_mismatch_entries=mismatch,
                 response_delta_by_added_edge_weight=weighted)
        if name=='2-to-3':
            # Exact representation check behind the integer obstruction:
            # the S3 sign-isotypic top-chain image has dimension one.
            constraints=[]
            for p in group:
                if p[3]==3 and p[4]==4:
                    Ro=permutation_rep(O[3],p)
                    Rn=permutation_rep(N[3],p)
                    chi=Ro[0][0]
                    assert chi in (-1,1)
                    constraints.extend([[Rn[i][j]-(chi if i==j else 0)
                                         for j in range(3)] for i in range(3)])
            assert 3-prior.rank(constraints)==1
            swap=next(p for p in group if p[:3]==(0,1,2) and p[3:]==(4,3))
            assert prior.mvec(permutation_rep(N[3],swap),fn)==[-v for v in fn]
            assert permutation_rep(O[3],swap)==[[Q(0),Q(1)],[Q(1),Q(0)]]
            assert prior.mvec(permutation_rep(O[3],swap),fo)==[-v for v in fo]
            row['equator_S3_sign_subspace_dimension']=1
            O2,N2,anchored,_,_=maps_case(coords,old,new,shell,alpha=1)
            assert all(v.denominator==1 for mat in anchored for line in mat for v in line)
            assert equivariance(O2,N2,anchored,group)==6  # breaks apex exchange
            row['integral_anchor_equivariant_count']=6
            row['integral_anchor_top_map']=[[str(v) for v in line] for line in anchored[3]]
            assert Q(2) in {v.denominator for mat in M for line in mat for v in line}
        out.append(row)
    print(json.dumps({'source_base':'2207611450df9106adccaf8189a50734fef5a46b',
                      'transport_scope':'boundary identity, chain map, relative degree +1',
                      'unit_metric':'assumed; not preserved by transport',
                      'cases':out},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
