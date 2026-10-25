#!/usr/bin/env python3
"""Exact stationary covariance and local three-edge source on finite quotients."""

import json
from fractions import Fraction as Q


HARMONIC=((1,1),(-1,1),(0,-2))  # sqrt(N) times the earlier M


def family(m,n,closed_edge=False):
    N=m*m+m*n+n*n
    shifts=(0,m+n,n)
    nv,ne,nf=2*N,3*N,N
    edges=[(t,r,(r-shifts[t])%N) for t in range(3) for r in range(N)]
    faces=[[(t*N+site%N,sign) for t,site,sign in
            ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
             (0,r+shifts[1]-shifts[2],-1),
             (1,r+shifts[1]-shifts[2],1),(2,r,-1))] for r in range(N)]
    mask=[1]*ne
    if closed_edge:
        mask[0]=0
    orbit=[t*N for t in range(3)]
    alpha=Q(1,2)
    theta=Q(3,5)
    stiffness=[Q(1)+alpha*int(e in orbit) for e in range(ne)]
    variance=[theta/k for k in stiffness]
    delta=theta/(1+alpha)-theta
    assert delta==Q(-1,5)

    # The uniform edge component cancels vertexwise: B1 M=0.
    for a in range(2):
        boundary=[0]*nv
        for t,r,b in edges:
            boundary[r]-=HARMONIC[t][a]
            boundary[N+b]+=HARMONIC[t][a]
        assert boundary==[0]*nv
    # sqrt(N) times S(w) in the previously fixed direct output basis.
    source=[[Q(0)]*nv for _ in range(2)]
    for e,(t,r,b) in enumerate(edges):
        for a in range(2):
            source[a][r]-=variance[e]*HARMONIC[t][a]
            source[a][N+b]+=variance[e]*HARMONIC[t][a]
    expected=[[Q(0)]*nv for _ in range(2)]
    for e in orbit:
        t,r,b=edges[e]
        assert r==0
        for a in range(2):
            expected[a][N+b]+=delta*HARMONIC[t][a]
    assert source==expected
    assert all(source[a][0]==0 for a in range(2))
    norm2=sum(v*v for row in source for v in row)
    assert norm2==8*delta*delta==Q(8,25)
    b0=edges[orbit[0]][2]
    b1=edges[orbit[1]][2]
    rank_minor=source[0][N+b0]*source[1][N+b1]-source[0][N+b1]*source[1][N+b0]
    assert rank_minor==2*delta*delta==Q(2,25)

    def apply(q):
        x,y,z=q[:nv],q[nv:nv+ne],q[nv+ne:]
        X,Y,Z=[Q(0)]*nv,[Q(0)]*ne,[Q(0)]*nf
        for e,(_,r,b) in enumerate(edges):
            X[r]+=mask[e]*y[e]
            X[N+b]-=mask[e]*y[e]
            Y[e]+=mask[e]*(x[N+b]-x[r])
        for f,terms in enumerate(faces):
            for e,sign in terms:
                Y[e]-=sign*z[f]
                Z[f]+=sign*y[e]
        return X+Y+Z

    dim=nv+ne+nf
    columns=[apply([Q(int(i==j)) for i in range(dim)]) for j in range(dim)]
    grades=[1]*nv+[-1]*ne+[1]*nf
    assert all(columns[j][i]==-columns[i][j] for i in range(dim) for j in range(dim))
    assert all((grades[i]+grades[j])*columns[j][i]==0
               for i in range(dim) for j in range(dim))
    # The isotropic canonical density is stationary: q^2 constant and
    # divergence trace A=0, regardless of the fixed contact mask.
    assert sum(columns[i][i] for i in range(dim))==0
    state=[Q((i%5)-2,i+3) for i in range(dim)]
    assert sum(state[i]*v for i,v in enumerate(apply(state)))==0
    metric=[Q(1)]*nv+stiffness+[Q(1)]*nf
    grad=[metric[i]*state[i] for i in range(dim)]
    flow=apply(grad)
    assert sum(grad[i]*flow[i] for i in range(dim))==0
    assert sum(metric[i]*columns[i][i] for i in range(dim))==0
    return {"N":N,"fixed_one_edge_mask":closed_edge,
            "isotropic_fixed_mask_covariance_uniform":True,
            "defect_alpha":str(alpha),"theta":str(theta),"delta":str(delta),
            "sqrtN_source_rank":2,"sqrtN_source_frobenius_squared":str(norm2),
            "sqrtN_source_rank_minor":str(rank_minor),
            "changed_energy_dynamics_conserves_energy":True}


def main():
    rows=[family(m,n,g) for m,n in ((2,1),(3,1),(3,2)) for g in (False,True)]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_EQUILIBRIUM_VARIANCE",
                      "cases":rows,
                      "physical_material_parameters_fixed":False,
                      "friction_or_seven_cell_selection_predicted":False},indent=2))


if __name__=="__main__":
    main()
