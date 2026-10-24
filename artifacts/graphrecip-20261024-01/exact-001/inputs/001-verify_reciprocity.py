#!/usr/bin/env python3
"""Exact native reversal, even packet port, and reciprocal power checks."""

import json
from fractions import Fraction as Q


HARMONIC = ((1,1),(-1,1),(0,-2))  # sqrt(N) times prior M columns
DIRECTIONS = ((2,-1,-1),(0,1,-1))


def quotient(m, n):
    N = m*m+m*n+n*n
    shifts = (0,m+n,n)
    edges = [(t,r,(r-shifts[t]) % N) for t in range(3) for r in range(N)]
    return N, shifts, edges


def gradient(x, N, edges):
    return [x[N+b]-x[r] for _,r,b in edges]


def leading_even_response(m, n):
    N, shifts, edges = quotient(m,n)
    base = [0]*(2*N)
    base[0]=1
    packets=[]
    for d in DIRECTIONS:
        v=[0]*(2*N)
        for t in range(3):
            v[N+(-shifts[t]) % N]=d[t]
        packets.append(v)
    g0=gradient(base,N,edges)
    columns=[]
    for x in packets:
        gd=gradient(x,N,edges)
        # Q=2 sum_e h_e y_e^2 (B1^T x)_e;
        # y=s(g0+epsilon*gd)+O(s^3), x=x0+O(s^2).
        # d/d epsilon of the s^2 coefficient is 6 sum_e h_e*g0_e^2*gd_e.
        columns.append([sum(6*HARMONIC[t][a]*g0[e]**2*gd[e]
                            for e,(t,_,_) in enumerate(edges)) for a in range(2)])
    matrix=[[columns[j][i] for j in range(2)] for i in range(2)]
    assert matrix==[[18,-6],[18,18]]
    return {"N":N,"linear_packet_even_s2_matrix":matrix}


def power_witness():
    N, shifts, edges=quotient(2,1)
    nv,ne,nf=2*N,3*N,N
    faces=[[(t*N+site%N, sign) for t,site,sign in
            ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
             (0,r+shifts[1]-shifts[2],-1),
             (1,r+shifts[1]-shifts[2],1),(2,r,-1))] for r in range(N)]
    def apply(q):
        x,y,z=q[:nv],q[nv:nv+ne],q[nv+ne:]
        X,Y,Z=[Q(0)]*nv,[Q(0)]*ne,[Q(0)]*nf
        for e,(_,r,b) in enumerate(edges):
            X[r]+=y[e];X[N+b]-=y[e]
            Y[e]+=x[N+b]-x[r]
        for f,terms in enumerate(faces):
            for e,sign in terms:
                Y[e]-=sign*z[f];Z[f]+=sign*y[e]
        return X+Y+Z
    q=[Q(0)]*(nv+ne+nf)
    q[0],q[1],q[nv],q[nv+3],q[nv+ne]=Q(1,2),Q(-1,3),Q(2,5),Q(-1,7),Q(1,11)
    y=q[nv:nv+ne]
    u=[Q(1,3),Q(-2,7)]
    h=[Q(0)]*nv
    h[0],h[1],h[N]=Q(3,4),Q(-1,5),Q(2,9)
    hu=[sum(Q(HARMONIC[t][a],1)*u[a] for a in range(2))
        for t,_,_ in edges]
    gh=gradient(h,N,edges)
    energy_scale,lam,tau=Q(3),Q(2),Q(5)
    grad_q=[energy_scale*v for v in q]
    for e in range(ne):
        grad_q[nv+e]+=2*lam*y[e]*hu[e]*gh[e]
    qdot=[v/(energy_scale*tau) for v in apply(grad_q)]
    assert sum(grad_q[i]*qdot[i] for i in range(len(q)))==0
    # E_int is even in y^2 but the literal linear-y alternative is odd.
    even_term=sum(lam*y[e]**2*hu[e]*gh[e] for e in range(ne))
    odd_term=sum(lam*y[e]*hu[e]*gh[e] for e in range(ne))
    assert odd_term != 0 and even_term != 0
    assert sum(lam*(-y[e])**2*hu[e]*gh[e] for e in range(ne))==even_term
    assert sum(lam*(-y[e])*hu[e]*gh[e] for e in range(ne))==-odd_term
    grad_u=[u[a]+lam*sum(Q(HARMONIC[t][a])*y[e]**2*gh[e]
                          for e,(t,_,_) in enumerate(edges)) for a in range(2)]
    grad_h=[h[i] for i in range(nv)]
    for e,(_,r,b) in enumerate(edges):
        c=lam*y[e]**2*hu[e]
        grad_h[r]-=c;grad_h[N+b]+=c
    udot=[Q(2,3),Q(-1,4)]
    hdot=[Q(0)]*nv
    hdot[0],hdot[1]=Q(3,8),Q(-2,5)
    D=[Q(1),Q(2)]+[Q(0)]*(nv-2)
    hddot=[-grad_h[i]-D[i]*hdot[i] for i in range(nv)]
    lhs=(sum(grad_q[i]*qdot[i] for i in range(len(q)))
         +sum(grad_u[a]*udot[a] for a in range(2))
         +sum(grad_h[i]*hdot[i]+hdot[i]*hddot[i] for i in range(nv)))
    rhs=sum(grad_u[a]*udot[a] for a in range(2))-sum(D[i]*hdot[i]**2 for i in range(nv))
    assert lhs==rhs
    return {"N":N,"even_interaction":str(even_term),"odd_linear_y_interaction":str(odd_term),
            "power_lhs":str(lhs),"power_rhs":str(rhs),"loss":str(sum(D[i]*hdot[i]**2 for i in range(nv)))}


def main():
    rows=[leading_even_response(m,n) for m,n in ((2,1),(3,1),(3,2))]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_RECIPROCITY_GATE",
                      "leading_response":rows,"rational_power_witness":power_witness(),
                      "native_to_material_parameters_fixed":False,
                      "measured_graphite_force_predicted":False},indent=2))


if __name__=="__main__":
    main()
