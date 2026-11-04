#!/usr/bin/env python3
"""Exact overlay-gate and born-edge Taylor audit for the snapped 2->3 case."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

source=Path(__file__).parents[1]/'pachner-current-metric'/'audit.py'
spec=importlib.util.spec_from_file_location('current',source)
current=importlib.util.module_from_spec(spec); spec.loader.exec_module(current)
prior=current.prior; lin=current.lin

def zeros(n): return [[Q(0)]*n for _ in range(n)]
def mvec(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]
def skew(A): return all(A[i][j]==-A[j][i] for i in range(len(A)) for j in range(i+1,len(A))) and all(A[i][i]==0 for i in range(len(A)))

def main():
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    assert set(old+new)==set(combinations(range(5),4))
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,_,_,_=prior.maps_case(coords,old,new,shell)
    U=[sorted(set(O[k])|set(N[k])) for k in range(4)]
    offsets=[sum(len(U[k]) for k in range(i)) for i in range(4)]
    full=[(k,s) for k,degree in enumerate(U) for s in degree]
    idx={key:i for i,key in enumerate(full)}
    okeys={(k,s) for k in range(4) for s in O[k]}
    nkeys={(k,s) for k in range(4) for s in N[k]}
    old_only=sorted(okeys-nkeys)
    new_only=sorted(nkeys-okeys)
    assert list(map(len,U))==[5,10,10,5] and len(full)==30
    assert len(old_only)==3 and len(new_only)==7
    assert old_only==[(2,(0,1,2)),(3,(0,1,2,3)),(3,(0,1,2,4))]
    assert (1,(3,4)) in new_only
    def lift(basis,A):
        labels=[(k,s) for k in range(4) for s in basis[k]]
        B=zeros(len(full))
        for i,row in enumerate(A):
            for j,v in enumerate(row):
                if v:B[idx[labels[i]]][idx[labels[j]]]=v
        return B
    Ao=lift(O,prior.skew_generator(O))
    An=lift(N,prior.skew_generator(N))
    assert skew(Ao) and skew(An)
    D=[[b-a for a,b in zip(ar,br)] for ar,br in zip(Ao,An)]
    # G(tau) = Ao+tau^p D, p=0 is the instantaneous new-side switch.
    # All choices are skew and Hasse-local on the abstract union carrier.
    v=idx[(0,(3,))]; edge=idx[(1,(3,4))]
    assert not any(Ao[edge]) and An[edge][v]==Q(1)
    out={}
    for p in (0,1,2):
        order=8
        coeff=[[Q(0)]*len(full) for _ in range(order+1)]
        coeff[0][v]=Q(1)
        for n in range(order):
            rhs=mvec(Ao,coeff[n])
            if n>=p:
                rhs=[x+y for x,y in zip(rhs,mvec(D,coeff[n-p]))]
            coeff[n+1]=[x/Q(n+1) for x in rhs]
        first=next(n for n,x in enumerate(coeff) if x[edge])
        amp=coeff[first][edge]
        assert first==p+1 and amp==Q(1,p+1)
        # Coefficient of tau^q in norm is zero for q>0 by skewness.
        norm_coeff=[sum(sum(coeff[i][j]*coeff[q-i][j] for j in range(len(full))) for i in range(q+1)) for q in range(order+1)]
        assert norm_coeff[0]==1 and all(x==0 for x in norm_coeff[1:])
        out[str(p)]={'gate':f'tau^{p}', 'edge_first_order':first,'edge_first_coefficient':str(amp),
                     'edge_stock_first_order':2*first,'edge_stock_first_coefficient':str(amp*amp)}
    # The post-switch native generator leaves the three old-only simplices
    # exactly frozen; a finite internal stock becomes an unobserved record.
    assert all(not any(An[idx[key]]) and all(row[idx[key]]==0 for row in An) for key in old_only)
    internal=idx[(2,(0,1,2))]
    u=[Q(0)]*len(full);u[internal]=Q(1)
    assert mvec(An,u)==[Q(0)]*len(full)
    # New-only and old-only amplitudes are different typed state components;
    # Q165 conservation cannot set the three old-only amplitudes to zero.
    print(json.dumps({'source_base_remote':'ecd0949a6f03eb30680e432409b7dc8c1742a76f',
       'source_base_local_checkout':'20efe0f7784aedc24130f2f0883324fea6eb9d04',
       'overlay_type':'abstract union = boundary complex of 4-simplex, not a geometric common refinement',
       'union_f_vector':[len(x) for x in U], 'union_euler':sum((-1)**k*len(x) for k,x in enumerate(U)),
       'old_only':[{'degree':k,'simplex':list(s)} for k,s in old_only],
       'new_only':[{'degree':k,'simplex':list(s)} for k,s in new_only],
       'born_edge':list(U[1][edge-offsets[1]]),
       'prepared_old_vertex':list(U[0][v]),
       'gates':out,
       'no_switch_gate':'g(tau)=0: born-edge amplitude and stock identically zero',
       'frozen_old_face_witness':{'simplex':[0,1,2],'initial_stock':'1',
          'new_restricted_readout':'0','post_switch_derivative':'0'},
       'identity':'For any prescribed real g(tau), A_g=(1-g)Ao+g An is skew on the unit overlay and has Hasse support in the union; its native quadratic stock is conserved. The source ledger specifies no g update or old-only reset.'},indent=2,sort_keys=True))

if __name__=='__main__':main()
