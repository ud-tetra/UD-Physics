#!/usr/bin/env python3
"""Exact locality selector and native boundary-readout identifiability audit."""
import importlib.util
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

source=Path(__file__).parents[1]/'pachner-trigger-lift'/'audit.py'
spec=importlib.util.spec_from_file_location('trigger',source)
trigger=importlib.util.module_from_spec(spec)
spec.loader.exec_module(trigger)
iface=trigger.iface
prior=iface.prior
lin=iface.lin


def mat_add(A,B):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(A,B)]


def mat_scale(s,A):
    return [[s*x for x in row] for row in A]


def sub(A,B):
    return mat_add(A,mat_scale(-1,B))


def zeros(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def block_counts(K,A,O):
    offsets=[sum(len(O[k]) for k in range(i)) for i in range(4)]
    counts={}
    for k in range(3):
        lo,hi=offsets[k],offsets[k+1]
        a,b=offsets[k+1],(offsets[k+2] if k<2 else len(A))
        for label,i0,i1,j0,j1 in [('up',lo,hi,a,b),('down',a,b,lo,hi)]:
            counts[f'{k}{k+1}_{label}_changed']=sum(K[i][j]!=A[i][j] for i in range(i0,i1) for j in range(j0,j1))
            counts[f'{k}{k+1}_{label}_new_nonincidence']=sum(K[i][j]!=0 and A[i][j]==0 for i in range(i0,i1) for j in range(j0,j1))
    return counts


def main():
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,Mo,fold,_=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo)
    n=len(M[0]);o=[sum(len(O[k]) for k in range(i)) for i in range(4)]
    t=[sum(len(N[k]) for k in range(i)) for i in range(4)]
    internal=next(f for f in O[2] if f not in shell)
    x=o[2]+O[2].index(internal)
    b={o[2]+j:Mo[2][N[2].index(f)][O[2].index(internal)]
       for j,f in enumerate(O[2]) if f in shell}
    vf=[Q(0)]*n;vf[x]=Q(1)
    for i,bi in b.items():vf[i]=-bi
    vt=[Q(0)]*n
    for j,f in enumerate(fold):vt[o[3]+j]=f*(1 if j==0 else -1)
    P=mat_add(mat_scale(Q(2,5),iface.outer(vf,vf)),mat_scale(Q(1,2),iface.outer(vt,vt)))
    H=mat_add(lin.mul(iface.switch.transpose(M),M),P)
    Hi=trigger.inverse(H)
    Ao=prior.skew_generator(O);An=prior.skew_generator(N)
    # If both source 1<->2 incidence blocks were kept unmodified, H-skew
    # would require B2(I-H2)=0. Compute the exact obstruction independently
    # of any particular projected generator.
    B2=[[Ao[i][j] for j in range(o[2],o[3])] for i in range(o[1],o[2])]
    H2=[[H[i][j] for j in range(o[2],o[3])] for i in range(o[2],o[3])]
    defect=lin.mul(B2,sub(H2,iface.switch.identity(len(H2))))
    defect_rank=lin.rank(defect)
    assert defect_rank>0
    B=lin.mul(lin.mul(iface.switch.transpose(M),An),M)
    K0=lin.mul(Hi,B)
    # The additional Q173-type full-open old face/top block is a different
    # admissible skew source. Its coefficient mu is not supplied by Q173.
    C=zeros(n)
    for i in range(o[2],o[3]):
        for j in range(o[3],n):
            C[i][j]=Ao[i][j];C[j][i]=Ao[j][i]
    D=lin.mul(Hi,C)
    Kmu=mat_add(K0,D)
    assert trigger.skew(lin.mul(H,K0)) and trigger.skew(lin.mul(H,Kmu))
    assert lin.rank(D)>0
    group=lin.automorphisms(old,coords,list(range(5)))
    for permutation in group:
        R=prior.block_diag([prior.permutation_rep(O[k],permutation) for k in range(4)])
        assert lin.mul(D,R)==lin.mul(R,D)
    # The lambda-family of the previous note alters the intact vertex/edge
    # incidence coefficients by 1+lambda; preserving their source values
    # selects lambda=0 inside that particular one-parameter family.
    E=lin.mul(Hi,Ao)
    assert all(K0[i][j]==Ao[i][j] for i in range(o[0],o[1]) for j in range(o[1],o[2]))
    assert all(E[i][j]==Ao[i][j] for i in range(o[0],o[1]) for j in range(o[1],o[2]))
    assert all(K0[i][j]==Ao[i][j] for i in range(o[1],o[2]) for j in range(o[2],o[3]))
    assert all(D[i][j]==0 for i in range(o[0],o[2]) for j in range(o[1],o[3]))
    # Strict native Hasse support means no face/top coupling where old B3
    # has zero incidence. Six K0 entries violate this. The Q173 gate
    # perturbation cannot cancel any of these six entries for any mu.
    violations=[]
    for i in range(o[2],o[3]):
        for j in range(o[3],n):
            if Ao[i][j]==0 and K0[i][j]:
                assert D[i][j]==0
                violations.append(dict(face=list(O[2][i-o[2]]),top=list(O[3][j-o[3]]),
                                       K0=str(K0[i][j]),gate_perturbation=str(D[i][j])))
    assert len(violations)==6
    # Reuse the exact local inward-crossing preparation. Both K0 and Kmu
    # conserve H and preserve all 12 automorphisms and low-degree blocks.
    c=[Q(0)]*n;c[x]=1;c[o[1]+O[1].index((0,1))]=1
    cap=[t[2]+N[2].index(f) for f in O[2] if f in shell]
    oldcap=[o[2]+O[2].index(f) for f in O[2] if f in shell]
    y=lin.mvec(M,c)
    def slope(K):
        dy=lin.mvec(M,lin.mvec(K,c))
        return 2*sum(y[i]*dy[i] for i in cap)
    def curvature(K):
        dy=lin.mvec(M,lin.mvec(K,c))
        ddy=lin.mvec(M,lin.mvec(K,lin.mvec(K,c)))
        return 2*sum(dy[i]**2+y[i]*ddy[i] for i in cap)
    slopes=[slope(K0),slope(Kmu)]
    curvatures=[curvature(K0),curvature(Kmu)]
    # The two derivative jets are exact native readouts, no physical units.
    assert iface.dot(c,lin.mvec(H,c))==Q(29,10)
    # A bounded, declared search for a different exact prepared input where
    # the still-free gated face/top coefficient changes the cap readout.
    G=sub(H,iface.switch.identity(n))
    oldc=c
    options=[(k,sg) for k in list(b)+list(range(o[3],n)) for sg in (Q(1),Q(-1))]
    witness=None
    searched=0
    for additions in list((v,) for v in options)+list(combinations(options,2)):
        c=list(oldc)
        for k,sg in additions:c[k]+=sg
        searched+=1
        gdot=2*iface.dot(lin.mvec(G,c),lin.mvec(Ao,c))
        if gdot>=0:continue
        y=lin.mvec(M,c)
        ds=[slope(K0),slope(Kmu)]
        d2=[curvature(K0),curvature(Kmu)]
        if ds[0]!=ds[1] or d2[0]!=d2[1]:
            old_d=lin.mvec(Ao,c);old_dd=lin.mvec(Ao,old_d)
            old_slope=2*sum(c[i]*old_d[i] for i in oldcap)
            old_curvature=2*sum(old_d[i]**2+c[i]*old_dd[i] for i in oldcap)
            witness=dict(additions=[{'old_basis_index':k,
                                      'old_simplex':list(O[2][k-o[2]] if k<o[3] else O[3][k-o[3]]),
                                      'added_amplitude':str(sg)} for k,sg in additions],
                         reserve_at_crossing=str(iface.dot(c,lin.mvec(G,c))),
                         gain_derivative=str(gdot),K0_cap_derivative=str(ds[0]),
                         Kmu1_cap_derivative=str(ds[1]),
                         K0_cap_second_derivative=str(d2[0]),
                         Kmu1_cap_second_derivative=str(d2[1]),
                         old_no_move_cap_stock=str(sum(c[i]**2 for i in oldcap)),
                         post_event_cap_stock=str(sum(y[i]**2 for i in cap)),
                         old_no_move_cap_derivative=str(old_slope),
                         old_no_move_cap_second_derivative=str(old_curvature))
            break
    assert witness is not None
    print(json.dumps({'source_base':'d4b10ea6abeab50d5e1b74e8735fb98955c6e017',
                      'source_scope':'Q169/Q173 fixed-complex incidence and gated existing face/top coupling',
                      'family':'K_mu=H^-1(M^T Anew M + mu C23old); mu=0,1 audited',
                      'mu_difference_rank':lin.rank(D),'automorphism_count':len(group),
                      'lower_incidence_metric_obstruction_rank':defect_rank,
                      'K0_vs_Aold_blocks':block_counts(K0,Ao,O),
                      'Kmu_vs_Aold_blocks':block_counts(Kmu,Ao,O),
                      'strict_Hasse_violations':violations,
                      'prepared_cap_readout':{'jump':'3/2','K0_first_derivative':str(slopes[0]),
                                               'Kmu1_first_derivative':str(slopes[1]),
                                               'K0_second_derivative':str(curvatures[0]),
                                               'Kmu1_second_derivative':str(curvatures[1])},
                      'discriminating_search':{'declared_budget':len(options)+len(list(combinations(options,2))),
                                               'evaluated':searched,'base':'x=1, edge(0,1)=1',
                                               'candidate':'add one or two ±1 boundary face or top amplitudes',
                                               'first_witness':witness}},indent=2,sort_keys=True))


if __name__=='__main__':main()
