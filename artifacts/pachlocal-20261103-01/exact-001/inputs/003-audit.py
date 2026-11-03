#!/usr/bin/env python3
"""Exact finite switch dilation: kernel memory, positive port, and shell receipt."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

root = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location('switch', root / 'pachner-switch-ledger' / 'audit.py')
switch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(switch)
prior = switch.prior
lin = prior.prior


def outer(a, b):
    return [[x*y for y in b] for x in a]


def add(A, B):
    return [[a+b for a,b in zip(row,other)] for row,other in zip(A,B)]


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def snorm(c):
    return dot(c,c)


def audit_2_to_3():
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,Mo,fold,fnew=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo)
    n=len(M[0]); offsets=[sum(len(O[j]) for j in range(k)) for k in range(4)]
    new_offsets=[sum(len(N[j]) for j in range(k)) for k in range(4)]
    internal=next(f for f in O[2] if f not in shell)
    x_index=offsets[2]+O[2].index(internal)
    b={offsets[2]+j:Mo[2][N[2].index(f)][O[2].index(internal)]
       for j,f in enumerate(O[2]) if f in shell}
    # The old boundary face basis maps identically. Only six caps mix with x.
    assert sorted(abs(v) for v in b.values())==[Q(0)]*0+[Q(1,2)]*6
    vf=[Q(0)]*n
    vf[x_index]=Q(1)
    for i,bi in b.items(): vf[i]=-bi
    vt=[Q(0)]*n
    for j,f in enumerate(fold):vt[offsets[3]+j]=f*(1 if j==0 else -1)
    assert snorm(vf)==Q(5,2) and snorm(vt)==Q(2) and dot(vf,vt)==0
    assert all(v==0 for v in lin.mvec(M,vf)) and all(v==0 for v in lin.mvec(M,vt))
    P=add([[x/Q(5,2) for x in row] for row in outer(vf,vf)],
          [[x/Q(2) for x in row] for row in outer(vt,vt)])
    assert lin.mul(P,P)==P and lin.rank(P)==2
    assert all(v==0 for row in lin.mul(M,P) for v in row)
    assert lin.rank(M)==n-2
    stacked=M+P
    assert lin.rank(stacked)==n
    # Rational port coordinates; their positive stock metric is diag(1/10,1/4).
    tf=[Q(0)]*n
    tf[x_index]=Q(3)
    for i,bi in b.items():tf[i]=2*bi
    ts=[Q(0)]*n
    for j,f in enumerate(fold):ts[offsets[3]+j]=f
    G=add(lin.mul(switch.transpose(M),M),P)
    G=switch.difference(G,switch.identity(n))
    ports=add([[x/Q(10) for x in row] for row in outer(tf,tf)],
              [[x/Q(4) for x in row] for row in outer(ts,ts)])
    assert G==ports and lin.rank(G)==2
    group=lin.automorphisms(old,coords,list(range(5)))
    for permutation in group:
        blocks=[prior.permutation_rep(O[k],permutation) for k in range(4)]
        R=prior.block_diag(blocks)
        assert lin.mul(P,R)==lin.mul(R,P)
        assert lin.mul(G,R)==lin.mul(R,G)
    assert len(group)==12
    # An event inverse exists on its 23D image. Under the unchanged target
    # generator with frozen memory, that image need not remain invariant.
    Anew=prior.skew_generator(N)
    AM=lin.mul(Anew,M)
    T=M+P
    DT=AM+[[Q(0)]*n for _ in range(n)]
    tangent_rank=lin.rank([a+b for a,b in zip(T,DT)])
    assert tangent_rank>n
    # Exact shell stock receipt, distinct from a sourced Q170 event current.
    samples=[]
    for label,x,y,u,d in [('fundamental',0,0,1,1),
                          ('opposite_top',0,0,1,-1),
                          ('face_only',1,0,0,0),
                          ('face_kernel',1,-1,0,0)]:
        c=[Q(0)]*n
        c[x_index]=Q(x)
        if label=='face_kernel':
            for i,bi in b.items():c[i]=-bi
        elif label=='face_only':pass
        elif y:
            for i,bi in b.items():c[i]=Q(y)*bi
        c[offsets[3]]=Q(u)*fold[0]
        c[offsets[3]+1]=Q(d)*fold[1]
        mc=lin.mvec(M,c);kc=lin.mvec(P,c)
        shell_before=sum(c[i]**2 for i in b)
        shell_after=sum(mc[new_offsets[2]+N[2].index(f)]**2 for f in O[2] if f in shell)
        z=sum(bi*c[i] for i,bi in b.items())
        boundary_receipt=2*c[x_index]*z+Q(3,2)*c[x_index]**2
        supply=(3*c[x_index]+2*z)**2/Q(10)+(Q(u)+Q(d))**2/Q(4)
        assert shell_after-shell_before==boundary_receipt,(label,shell_before,shell_after,z,boundary_receipt)
        assert snorm(mc)+snorm(kc)-snorm(c)==supply
        samples.append(dict(label=label,old_stock=str(snorm(c)),new_stock=str(snorm(mc)),
                            memory_stock=str(snorm(kc)),support_obligation=str(supply),
                            shell_stock_jump=str(boundary_receipt)))
    return dict(old_dim=n,new_dim=len(M),rank_M=lin.rank(M),kernel_dim=2,
                memory_basis_norms=[str(snorm(vf)),str(snorm(vt))],
                positive_port_rank=lin.rank(G),port_metric=['1/10','1/4'],
                port_forms=['3*x+2*z','u+d'],z_definition='z=sum six b_i*y_i, b_i=+/-1/2',
                shell_jump='2*x*z+3*x^2/2',symmetry_count=len(group),
                target_flow_tangency_rank=tangent_rank,samples=samples)


def audit_1_to_4():
    coords=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(0,0,0)]
    old=[(0,1,2,3)]
    new=[tuple(sorted((*f,4))) for f in combinations(range(4),3)]
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,Mo,fold,_=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo)
    n=len(M[0]);top=sum(len(O[j]) for j in range(3))
    Qmat=switch.difference(lin.mul(switch.transpose(M),M),switch.identity(n))
    assert Qmat==[[Q(3) if i==j==top else Q(0) for j in range(n)] for i in range(n)]
    return dict(old_dim=n,new_dim=len(M),rank_M=lin.rank(M),kernel_dim=0,
                positive_port_rank=1,port_metric=['3'],port_forms=['a'],
                shell_jump='0',support_obligation='3*a^2')


def main():
    print(json.dumps({'source_base':'6c9f3b855169448d224d7c9f9badee02d4d5a1e3',
                      'evidence':'exact finite algebra, conditional support interface, no event law',
                      'one_to_four':audit_1_to_4(),'two_to_three':audit_2_to_3()},indent=2,sort_keys=True))


if __name__=='__main__':main()
