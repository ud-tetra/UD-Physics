#!/usr/bin/env python3
"""Exact Q165 support jump and conditional reservoir for Pachner chain maps."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

source = Path(__file__).parents[1] / 'pachner-state-transport' / 'audit.py'
spec = importlib.util.spec_from_file_location('prior_state_transport', source)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def transpose(M):
    return [list(row) for row in zip(*M)]


def difference(A,B):
    return [[a-b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]


def identity(n):
    return [[Q(int(i==j)) for j in range(n)] for i in range(n)]


def quadratic(M,c):
    return sum(a*b for a,b in zip(c,prior.prior.mvec(M,c)))


def eigenspace_multiplicity(Qmat,eigenvalue):
    n=len(Qmat)
    return n-prior.prior.rank(difference(Qmat,
        [[Q(eigenvalue) if i==j else Q(0) for j in range(n)] for i in range(n)]))


def cell_owned_stock(S,tets,c):
    offsets=[sum(len(S[j]) for j in range(k)) for k in range(4)]
    incidence={simplex:sum(set(simplex).issubset(tet) for tet in tets)
               for k in range(4) for simplex in S[k]}
    assert all(v>=1 for v in incidence.values())
    total=Q(0)
    for tet in tets:
        for k in range(4):
            for j,sigma in enumerate(S[k]):
                if set(sigma).issubset(tet):
                    total+=c[offsets[k]+j]**2/incidence[sigma]
    return total


def audit_case(name,coords,old,new,boundary):
    shell,_,_=prior.prior.shell_and_volume(old,coords)
    O,N,Mo,fold,fnew=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo)
    Qmat=difference(prior.prior.mul(transpose(M),M),identity(len(M[0])))
    spectrum=({Q(0):14,Q(3):1} if name=='1-to-4' else
              {Q(0):19,Q(-1):2,Q(1,2):1,Q(3,2):1})
    assert sum(spectrum.values())==len(Qmat)
    assert all(eigenspace_multiplicity(Qmat,ev)==mult for ev,mult in spectrum.items())
    # Independent exact polynomial certificate: all roots are real and the
    # symmetric Qmat is diagonalizable in the unit coefficient metric.
    poly=identity(len(Qmat))
    for ev in spectrum:
        shifted=difference(Qmat,[[ev if i==j else Q(0)
                                   for j in range(len(Qmat))]
                                  for i in range(len(Qmat))])
        poly=prior.prior.mul(poly,shifted)
    assert all(x==0 for row in poly for x in row)
    assert prior.prior.rank(M)==(15 if name=='1-to-4' else 21)
    assert prior.prior.rank(Qmat)==(1 if name=='1-to-4' else 4)
    if name=='2-to-3':
        internal=next(f for f in O[2] if f not in shell)
        j=O[2].index(internal)
        col=[Mo[2][i][j] for i in range(len(N[2]))]
        assert sorted(abs(v) for v in col)==[Q(0)]*3+[Q(1,2)]*6
        assert sum(v*v for v in col)==Q(3,2)
        assert all(N[2][i] in shell for i,v in enumerate(col) if v)
    offsets=[sum(len(O[j]) for j in range(k)) for k in range(4)]
    examples={}
    for label,top in (('fundamental',fold),('opposite_top',
                       [fold[0],-fold[1]] if name=='2-to-3' else [])):
        if not top:continue
        c=[Q(0)]*len(Qmat)
        for j,v in enumerate(top):c[offsets[3]+j]=v
        mc=prior.prior.mvec(M,c)
        before=sum(v*v for v in c)
        after=sum(v*v for v in mc)
        delta=quadratic(Qmat,c)
        assert delta==after-before
        assert cell_owned_stock(O,O[3],c)==before
        assert cell_owned_stock(N,N[3],mc)==after
        reservoir_before=max(Q(0),delta)
        reservoir_after=reservoir_before-delta
        assert reservoir_after>=0 and before+reservoir_before==after+reservoir_after
        if label=='opposite_top':
            assert all(v==0 for v in mc)
            assert prior.prior.mvec(M,[-v for v in c])==mc
            assert quadratic(Qmat,[-v for v in c])==delta
        examples[label]=dict(before=str(before),after=str(after),delta=str(delta),
                             minimum_reservoir_before=str(reservoir_before),
                             reservoir_after=str(reservoir_after))
    return dict(move=name,old_chain_dim=len(Qmat),new_chain_dim=len(M),
                rank_M=prior.prior.rank(M),nullity_M=len(Qmat)-prior.prior.rank(M),
                delta_quadratic_rank=prior.prior.rank(Qmat),
                delta_eigenspaces={str(k):v for k,v in spectrum.items()},
                max_gain_per_unit_old_stock=str(max(spectrum)),
                min_delta_per_unit_old_stock=str(min(spectrum)),
                examples=examples,
                scalar_reservoir_restores_injectivity=False if name=='2-to-3' else None,
                internal_face_to_boundary_support=6 if name=='2-to-3' else 0)


def main():
    coords=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)]
    old=[(0,1,2,3)]
    new=[tuple(sorted((*f,4))) for f in combinations(range(4),3)]
    a=audit_case('1-to-4',coords,old,new,list(range(4)))
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    b=audit_case('2-to-3',coords,old,new,list(range(5)))
    assert a['examples']['fundamental']['delta']=='3'
    assert b['examples']['fundamental']['delta']=='1'
    assert b['examples']['opposite_top']['delta']=='-2'
    print(json.dumps({'source_base':'3026f7a673dbec6103aae2a68a20bb94b61b61ae',
                      'stock':'Q165 sum of squared simplex amplitudes',
                      'reservoir':'assumed scalar native stock; exact bookkeeping, not source-selected actuator',
                      'cases':[a,b]},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
