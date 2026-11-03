#!/usr/bin/env python3
"""Exact rational 2->3 new-carrier current and transverse-port audit."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

root=Path(__file__).parents[1]
spec=importlib.util.spec_from_file_location('local',root/'pachner-locality-port'/'audit.py')
local=importlib.util.module_from_spec(spec);spec.loader.exec_module(local)
trigger=local.trigger; iface=local.iface; prior=local.prior; lin=local.lin

def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(x) for x in zip(*A)]
def scale(s,A): return [[s*x for x in row] for row in A]
def minus(A,B): return [[a-b for a,b in zip(row,br)] for row,br in zip(A,B)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))

def main():
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,Mo,fold,_=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo); n=len(M[0]);m=len(M)
    assert (n,m,lin.rank(M))==(23,27,21)
    oo=[sum(len(O[k]) for k in range(i)) for i in range(4)]
    internal=next(f for f in O[2] if f not in shell)
    x=oo[2]+O[2].index(internal)
    vf=[Q(0)]*n; vf[x]=Q(1)
    for f in O[2]:
        if f in shell:
            vf[oo[2]+O[2].index(f)]=-Mo[2][N[2].index(f)][O[2].index(internal)]
    vt=[Q(0)]*n
    for j,f in enumerate(fold): vt[oo[3]+j]=f*(1 if j==0 else -1)
    L=[vf,vt]
    W=[[Q(2,5),Q(0)],[Q(0),Q(1,2)]]
    # Ambient new-complex plus two static memory coordinates, with a
    # separately declared positive memory metric. T has old-coordinate domain.
    T=M+L
    J=eye(m)+[[Q(0)]*m+row for row in W]
    for row in J[:m]: row.extend([Q(0),Q(0)])
    H=lin.mul(lin.mul(transpose(T),J),T)
    assert H==local.mat_add(lin.mul(transpose(M),M),
                 local.mat_add(scale(Q(2,5),iface.outer(vf,vf)),scale(Q(1,2),iface.outer(vt,vt))))
    Hi=trigger.inverse(H)
    An=prior.skew_generator(N)
    A=[row+[Q(0),Q(0)] for row in An]+[[Q(0)]*(m+2) for _ in range(2)]
    assert lin.mul(transpose(A),J)==scale(-1,lin.mul(J,A))
    # Exact new-carrier Q166 continuity: every oriented Hasse pair has equal
    # and opposite quadratic-stock contributions, with no source at a vertex.
    graph={i:set() for i in range(m)}
    for i in range(m):
        for j in range(m):
            if An[i][j]: graph[i].add(j)
    seen=set(); comps=[]
    for i in graph:
        if i in seen: continue
        stack=[i];seen.add(i);component=[]
        while stack:
            k=stack.pop();component.append(k)
            for j in graph[k]-seen:seen.add(j);stack.append(j)
        comps.append(component)
    assert len(comps)==1
    # Pi is J-orthogonal projection onto T(Q^23); R is the unavoidable
    # transverse discrepancy for any continuation confined to that image.
    Pi=lin.mul(lin.mul(T,Hi),lin.mul(transpose(T),J))
    assert lin.mul(Pi,Pi)==Pi and lin.mul(Pi,T)==T
    R=minus(lin.mul(A,T),lin.mul(Pi,lin.mul(A,T)))
    assert lin.mul(transpose(T),lin.mul(J,R))==[[Q(0)]*n for _ in range(n)]
    K=lin.mul(Hi,lin.mul(transpose(T),lin.mul(J,lin.mul(A,T))))
    assert minus(lin.mul(A,T),lin.mul(T,K))==R
    assert lin.mul(transpose(K),H)==scale(-1,lin.mul(H,K))
    rank=lin.rank(R)
    assert rank>0
    # Deterministic first nonzero old basis witness in ascending chain order.
    w=next(j for j in range(n) if any(row[j] for row in R))
    degree=next(k for k in range(4) if oo[k]<=w<(oo[k+1] if k<3 else n))
    c=[Q(0)]*n;c[w]=Q(1)
    r=lin.mvec(R,c)
    assert any(r)
    born_edge=len(N[0])+N[1].index((3,4))
    assert w==N[0].index((3,)) and born_edge==14
    assert all(v==0 for v in M[born_edge])
    assert An[born_edge][w]==Q(1) and r[born_edge]==Q(1)
    residual_norm=dot(r,lin.mvec(J,r))
    assert residual_norm>0
    # Norm conservation fixes only a tangential inner product, not R:
    # <Tc,Rc>_J=0, while the full free A flow leaves the event image.
    assert dot(lin.mvec(T,c),lin.mvec(J,r))==0
    # The two memory rows are a kernel record (up to their fixed norms), but
    # their units are unselected by Q169, which acts only on the new complex.
    assert lin.rank(L)==2
    print(json.dumps({
        'source_base':'5295ab317a1013e27296c20d44e8ee6a06784fba',
        'spaces':{'old':n,'new':m,'memory':2,'ambient':m+2},
        'new_hasse_components':list(map(len,comps)),
        'diagonal_metric_selector':'For fixed nonzero Q169 incidence coefficients and diagonal positive D, D-skew forces d_i=d_j along every Hasse edge; connected new graph => D_new=d I. Boundary normalization d=1 selects I_new. Isolated memory weights remain unconstrained.',
        'transverse_residual_rank':rank,
        'transverse_nonzero_rows':sum(any(row) for row in R),
        'witness':{'old_basis_index':w,'old_basis_simplex':list(O[degree][w-oo[degree]]),'residual_squared_J':str(residual_norm),
                   'born_new_edge':list(N[1][born_edge-len(N[0])]),
                   'born_edge_derivative':str(An[born_edge][w]),
                   'born_edge_stock_leading_coefficient':'1*tau^2',
                   'new_residual_nonzero':[(i,str(v)) for i,v in enumerate(r[:m]) if v],
                   'memory_residual_nonzero':[(i,str(v)) for i,v in enumerate(r[m:]) if v]},
        'identities':{'TtJT=H':True,'projection_idempotent':True,
                      'Anew_T_minus_T_K=R':True,'Tt_J_R=0':True,
                      'K_H_skew':True,'event_image_invariant':False}},indent=2,sort_keys=True))

if __name__=='__main__': main()
