#!/usr/bin/env python3
"""Timing-budget audit v0.1; setup adapted from pinned Pachner trigger lift."""
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


def main(return_setup=False):
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
    if return_setup:
        return locals()
    rownorm=lambda A:max(sum(map(abs,row)) for row in A)
    assert rownorm(Ao)==rownorm(An)==5
    D=[row[:] for row in An]
    for i in range(len(N[0])):
        for j,e in enumerate(N[1],newoffs[1]):
            if e!=(0,1): D[i][j]=D[j][i]=Q(0)
    assert skew(D) and rownorm(D)==5
    J=lin.mul(Hinv,lin.mul(lin.mul(iface.switch.transpose(M),D),M))
    assert skew(lin.mul(H,J))
    # Matrix proof of event metric spectrum and stock.
    assert scalar(H,c)==Q(29,10)
    comm=iface.switch.difference(lin.mul(G,Ao),lin.mul(Ao,G))
    assert scalar(comm,c)==Q(-3)
    # Exact derivatives: all coordinates agree at orders 0 and 1.
    u=v=c
    derivatives=[]
    for k in range(4):
        a,b=lin.mvec(M,u),lin.mvec(M,v)
        if k<2: assert a==b
        derivatives.append((a[1]-a[0])-(b[1]-b[0]))
        u=lin.mvec(J,u);v=lin.mvec(K0,v)
    assert derivatives==[Q(0),Q(0),Q(2),Q(2)]
    # Strict inequalities checked by squaring positive rational bounds.
    assert Q(3,2)**2>2
    assert Q(7,4)**2>Q(29,10)
    assert Q(2)**2>Q(5,2)
    assert Q(12)**2>Q(5,2)*25*2
    assert Q(17)**2>2*144
    assert Q(13)**2>2*25*Q(7,4)**2
    # Nominal scalar crossing F=R-c^T Gc: F'=3 and |F''|<=300.
    a=Q(1,600);epsmax=Q(1,1000);dmax=Q(1,1000)
    assert 3-300*a==Q(5,2)
    assert Q(5,2)-45*epsmax-15*epsmax**2>2
    assert Q(5,2)*a>dmax
    assert dmax/2<a
    assert Q(3,2)*(3*epsmax+epsmax**2)<5*epsmax
    assert (2*epsmax+12*dmax/2)<Q(1,2) # selector stability
    assert Q(7,4)**2>(Q(29,10)+2*Q(7,4)*(2*epsmax+6*dmax)+(2*epsmax+6*dmax)**2)
    # Third-order remainder for difference of signed linear readouts.
    assert 105**2>(Q(2,6)*125)**2*Q(29,5)
    lo,hi=Q(1,420),Q(1,210)
    sep=lo**2/2
    assert 1-105*hi==Q(1,2)
    assert sep==Q(1,352800)
    budget=Q(1,800000)
    assert budget<sep/2
    example={'preparation_epsilon':Q(1,200000000),
             'reserve_error_r':Q(1,100000000),
             'sampling_jitter_nu':Q(1,100000000),
             'readout_error_eta':Q(1,4000000)}
    e,r,nu,eta=example.values()
    assert 78*e+15*r+13*nu+eta==Q(23,25000000)<budget
    assert r+5*e==Q(7,200000000)
    assert (r+5*e)/2==Q(7,400000000)
    # Any tuple satisfying the budget satisfies the coarse crossing domain.
    assert budget/78<epsmax
    assert budget/15+5*budget/78<dmax
    assert budget/13<Q(1,100000)
    assert lo>dmax/2+Q(1,100000)
    result={
      'version':'v0.1','evidence':'EXACT_CONDITIONAL','physical_promotion':0,
      'source_revision':'41da46f2f3f3dd25f794fbbb5dedc16ea00854d8',
      'row_norm_bounds':{'old':5,'new_all':5,'new_single':5},
      'nominal_crossing':{'reserve':str(R),'gdot':str(gdot),'interval':['-1/600','1/600']},
      'crossing_domain':'epsilon<=1/1000 and d=r+5epsilon<=1/1000',
      'crossing_bound':'unique inward zero on [-1/600,1/600]; |t_star|<=(r+5epsilon)/2',
      'vertex_contrast_difference_derivatives':list(map(str,derivatives)),
      'sample_window':list(map(str,(lo,hi))),
      'nominal_separation_lower_bound':str(sep),
      'joint_budget':'78epsilon+15r+13nu+eta<=1/800000',
      'example':{k:str(v) for k,v in example.items()},
      'example_budget_used':'23/25000000',
      'example_crossing_shift_bound':'7/400000000',
      'scope':'one local event; signed readout; fixed selected mask; projection assumed; preparation norm before event; jitter relative to nominal sample time',
      'tests':'rational identities and conservative analytic bound constants PASS'}
    print(json.dumps(result,indent=2))
    return result

if __name__=="__main__":
    main()
