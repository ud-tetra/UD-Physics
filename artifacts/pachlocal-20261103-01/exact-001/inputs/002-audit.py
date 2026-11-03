#!/usr/bin/env python3
"""Exact conditional first-entry gate and metric-projected Pachner memory flow."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

source=Path(__file__).parents[1]/'pachner-interface-defect'/'audit.py'
spec=importlib.util.spec_from_file_location('iface',source)
iface=importlib.util.module_from_spec(spec)
spec.loader.exec_module(iface)
prior=iface.prior
lin=iface.lin


def scalar(A,v):
    return iface.dot(v,lin.mvec(A,v))


def inverse(A):
    n=len(A)
    work=[list(row)+list(unit) for row,unit in zip(A,iface.switch.identity(n))]
    for j in range(n):
        pivot=next((i for i in range(j,n) if work[i][j]),None)
        assert pivot is not None
        work[j],work[pivot]=work[pivot],work[j]
        factor=work[j][j]
        work[j]=[x/factor for x in work[j]]
        for i in range(n):
            if i!=j:
                factor=work[i][j]
                work[i]=[x-factor*y for x,y in zip(work[i],work[j])]
    assert [row[:n] for row in work]==iface.switch.identity(n)
    return [row[n:] for row in work]


def skew(A):
    return all(A[i][j]==-A[j][i] for i in range(len(A)) for j in range(len(A)))


def cap_stock(v,indices):
    return sum(v[i]**2 for i in indices)


def cap_derivative(v,dv,indices):
    return 2*sum(v[i]*dv[i] for i in indices)


def main():
    coords=[(1,-1,0),(0,1,-1),(-1,0,1),(1,1,1),(-1,-1,-1)]
    old=[(0,1,2,3),(0,1,2,4)]
    new=[(0,1,3,4),(1,2,3,4),(0,2,3,4)]
    shell,_,_=lin.shell_and_volume(old,coords)
    O,N,Mo,fold,_=prior.maps_case(coords,old,new,shell)
    M=prior.block_diag(Mo)
    n=len(M[0]);offs=[sum(len(O[j]) for j in range(k)) for k in range(4)]
    newoffs=[sum(len(N[j]) for j in range(k)) for k in range(4)]
    face=next(f for f in O[2] if f not in shell)
    x=offs[2]+O[2].index(face)
    b={offs[2]+j:Mo[2][N[2].index(f)][O[2].index(face)]
       for j,f in enumerate(O[2]) if f in shell}
    vf=[Q(0)]*n;vf[x]=Q(1)
    for i,bi in b.items():vf[i]=-bi
    vt=[Q(0)]*n
    for j,f in enumerate(fold):vt[offs[3]+j]=f*(1 if j==0 else -1)
    P=iface.add([[v/Q(5,2) for v in row] for row in iface.outer(vf,vf)],
                [[v/Q(2) for v in row] for row in iface.outer(vt,vt)])
    H=iface.add(lin.mul(iface.switch.transpose(M),M),P)
    G=iface.switch.difference(H,iface.switch.identity(n))
    assert iface.switch.eigenspace_multiplicity(G,Q(0))==21
    assert iface.switch.eigenspace_multiplicity(G,Q(1,2))==1
    assert iface.switch.eigenspace_multiplicity(G,Q(3,2))==1
    Hinv=inverse(H)
    assert lin.mul(H,Hinv)==iface.switch.identity(n)
    Ao=prior.skew_generator(O);An=prior.skew_generator(N)
    B=lin.mul(lin.mul(iface.switch.transpose(M),An),M)
    assert skew(B)
    K0=lin.mul(Hinv,B)
    K1=lin.mul(Hinv,iface.add(B,Ao))
    assert skew(lin.mul(H,K0)) and skew(lin.mul(H,K1))
    assert lin.rank(iface.switch.difference(K1,K0))>0
    assert iface.add(lin.mul(iface.switch.transpose(M),
                             iface.switch.difference(lin.mul(An,M),lin.mul(M,K0))),
                     [[-v for v in row] for row in lin.mul(P,K0)])==[[Q(0)]*n for _ in range(n)]
    residual_matrix=iface.switch.difference(lin.mul(An,M),lin.mul(M,K0))
    residual_rank=lin.rank(residual_matrix+lin.mul(P,K0))
    assert residual_rank==6
    witness_index=next(j for j in range(n) if
                       any(residual_matrix[i][j] for i in range(len(M))) or
                       any(lin.mul(P,K0)[i][j] for i in range(n)))
    witness=[Q(int(j==witness_index)) for j in range(n)]
    witness_residual=iface.snorm(lin.mvec(residual_matrix,witness))+iface.snorm(lin.mvec(P,lin.mvec(K0,witness)))
    assert witness_residual>0
    # Projected target flow (An M c,0) onto the event image T(c)=(Mc,Pc).
    # K0 is the unique least-squares projection under the *chosen* unit metric.
    # K1 is an equally local, symmetric H-skew alternative with no fitted data.
    group=lin.automorphisms(old,coords,list(range(5)))
    for permutation in group:
        R=prior.block_diag([prior.permutation_rep(O[k],permutation) for k in range(4)])
        assert lin.mul(K0,R)==lin.mul(R,K0)
        assert lin.mul(K1,R)==lin.mul(R,K1)
    oldcap=[offs[2]+O[2].index(f) for f in O[2] if f in shell]
    newcap=[newoffs[2]+N[2].index(f) for f in O[2] if f in shell]
    # Exact local first-entry preparation at t=0. Gdot<0 ensures a small
    # interval just before 0 is inadmissible and just after 0 is admissible.
    c=[Q(0)]*n;c[x]=Q(1);c[offs[1]+O[1].index((0,1))]=Q(1)
    R=scalar(G,c)
    gdot=2*iface.dot(lin.mvec(G,c),lin.mvec(Ao,c))
    assert R==Q(9,10) and gdot==Q(-3)
    oldstock=iface.snorm(c);newc=lin.mvec(M,c);mem=lin.mvec(P,c)
    assert iface.snorm(newc)+iface.snorm(mem)==oldstock+R
    oldcap0=cap_stock(c,oldcap);newcap0=cap_stock(newc,newcap)
    assert oldcap0==0 and newcap0==Q(3,2)
    old_d=cap_derivative(c,lin.mvec(Ao,c),oldcap)
    post_d0=cap_derivative(newc,lin.mvec(M,lin.mvec(K0,c)),newcap)
    post_d1=cap_derivative(newc,lin.mvec(M,lin.mvec(K1,c)),newcap)
    raw_target_d=cap_derivative(newc,lin.mvec(An,newc),newcap)
    correction=lin.mvec(An,newc)
    proj=lin.mvec(M,lin.mvec(K0,c))
    mem_d=lin.mvec(P,lin.mvec(K0,c))
    residual=iface.snorm([a-b for a,b in zip(correction,proj)])+iface.snorm(mem_d)
    assert residual>=0
    # The first-entry rule is degenerate for c=0 (G=Gdot=0) and absent for
    # reserves greater than the maximum G along a fixed-stock old orbit.
    assert scalar(G,[Q(0)]*n)==0
    # Exact spectral bound from the prior jump spectrum after kernel memory:
    # Gmax=(3/2)||c||² on this 2→3 ball.
    high_R=Q(3,2)*oldstock+Q(1)
    assert high_R>Q(3,2)*oldstock
    print(json.dumps({'source_base':'7c26ef783b0dccac998eb61c3dcb15c52d2cf746',
                      'model':'candidate first-entry R-G=0, Gdot<0; projected memory flow K0',
                      'generator':'H=I+G; K_lambda=H^-1(M^T Anew M + lambda Aold), lambda=0 or 1',
                      'symmetry_count':len(group),'H_rank':lin.rank(H),
                      'lambda_difference_rank':lin.rank(iface.switch.difference(K1,K0)),
                      'projection_residual_rank':residual_rank,
                      'projection_witness':{'old_basis_index':witness_index,
                                            'residual_norm_squared':str(witness_residual)},
                      'preparation':{'initial_amplitudes':{'internal_face_(0,1,2)':'1','edge_(0,1)':'1'},
                                     'R':str(R),'G':str(R),'Gdot':str(gdot),
                                     'old_total_stock':str(oldstock),
                                     'post_new_stock':str(iface.snorm(newc)),
                                     'post_memory_stock':str(iface.snorm(mem)),
                                     'post_reserve':'0'},
                      'cap_readout':{'old_pre_event':str(oldcap0),'new_post_event':str(newcap0),
                                     'jump':str(newcap0-oldcap0),
                                     'old_no_move_derivative':str(old_d),
                                     'projected_lambda0_derivative':str(post_d0),
                                     'projected_lambda1_derivative':str(post_d1),
                                     'raw_target_derivative':str(raw_target_d),
                                     'projection_residual_norm_squared':str(residual)},
                      'trigger_limits':{'zero_state':'degenerate G=Gdot=0',
                                        'high_reserve_no_crossing':str(high_R),
                                        'old_stock_bound':str(oldstock)}},indent=2,sort_keys=True))


if __name__=='__main__':main()
