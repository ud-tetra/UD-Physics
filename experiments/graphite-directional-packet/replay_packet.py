#!/usr/bin/env python3
"""Exact linear boundary-packet harmonic response in the full 0/1/2 carrier."""

import json
from fractions import Fraction as F
from math import comb, factorial


def family(m, n, max_order=17):
    N=m*m+m*n+n*n
    shifts=(0,m+n,n)
    edges=[(t,r,(r-shifts[t])%N) for t in range(3) for r in range(N)]
    faces=[]
    for r in range(N):
        faces.append([(t*N+site%N,sign) for t,site,sign in
                      ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
                       (0,r+shifts[1]-shifts[2],-1),
                       (1,r+shifts[1]-shifts[2],1),(2,r,-1))])

    def apply(x,y,z):
        X,Y,Z=[0]*(2*N),[0]*(3*N),[0]*N
        for e,(_,r,b) in enumerate(edges):
            X[r]+=y[e]
            X[N+b]-=y[e]
            Y[e]+=x[N+b]-x[r]
        for f,terms in enumerate(faces):
            for e,sign in terms:
                Y[e]-=sign*z[f]
                Z[f]+=sign*y[e]
        return X,Y,Z

    def rotate(x,y,z):
        s1,s2=shifts[1:]
        q=next(q for q in range(1,N) if (q*s1+m)%N==0
               and (q*s2+s1)%N==0 and pow(q,3,N)==1)
        X,Y,Z=[0]*(2*N),[0]*(3*N),[0]*N
        for r in range(N):
            X[q*r%N]=x[r]
            X[N+(q*r-s1)%N]=x[N+r]
            Z[(q*r-m)%N]=z[r]
        for e,(t,r,_) in enumerate(edges):
            Y[((t+1)%3)*N+q*r%N]=y[e]
        return X,Y,Z

    base=[1]+[0]*(2*N-1)
    # B-neighbors of A0 with externally supplied registered direction weights.
    dirs=((2,-1,-1),(0,1,-1))
    packets=[]
    for d in dirs:
        x=[0]*(2*N)
        for t in range(3):
            x[N+(-shifts[t])%N]=d[t]
        assert sum(x)==0
        packets.append(x)

    def derivatives(x):
        d=[(x,[0]*(3*N),[0]*N)]
        for _ in range(max_order):
            d.append(apply(*d[-1]))
        return d

    D0=derivatives(base)
    D=[derivatives(x) for x in packets]
    harmonic=((1,1),(-1,1),(0,-2))

    def project(y,g):
        return [sum(2*harmonic[t][a]*y[e]*g[e]
                    for e,(t,_,_) in enumerate(edges)) for a in range(2)]

    def grad(x):
        return [x[N+b]-x[r] for _,r,b in edges]

    orders=list(range(1,max_order+1,2))
    rows=[]
    for o in orders:
        cols=[]
        for d in D:
            v=[0,0]
            for k in range(1,o+1,2):
                factor=comb(o,k)
                p=project(D0[k][1],grad(d[o-k][0]))
                q=project(d[k][1],grad(D0[o-k][0]))
                v=[v[a]+factor*(p[a]+q[a]) for a in range(2)]
            cols.append([str(F(v[a],factorial(o))) for a in range(2)])
        rows.append([[cols[col][row] for col in range(2)] for row in range(2)])

    # A rotated boundary packet and its J readout must transform covariantly.
    for x,d in zip(packets,D):
        rx=rotate(x,[0]*(3*N),[0]*N)[0]
        dr=derivatives(rx)
        for k in range(max_order+1):
            assert dr[k]==rotate(*d[k])
    assert rotate(base,[0]*(3*N),[0]*N)[0]==base

    return {"mn":[m,n],"N":N,"input_direction_basis":[list(d) for d in dirs],
            "output_harmonic_basis":[[1,-1,0],[1,1,-2]],
            "orders":orders,"linear_epsilon_matrix_coefficients":rows,
            "C3_covariance_exact_derivatives_verified":True}


def main():
    rows=[family(m,n) for m,n in ((2,1),(3,1),(3,2))]
    orders=rows[0]["orders"]
    unequal=[o for i,o in enumerate(orders)
             if len({json.dumps(r["linear_epsilon_matrix_coefficients"][i]) for r in rows})>1]
    assert rows[0]["linear_epsilon_matrix_coefficients"][0]==[["-12","4"],["-12","-12"]]
    assert unequal[0]==9
    def matrix_diff(a,b,order):
        i=orders.index(order)
        return [[str(F(rows[a]["linear_epsilon_matrix_coefficients"][i][u][v])
                     -F(rows[b]["linear_epsilon_matrix_coefficients"][i][u][v]))
                 for v in range(2)] for u in range(2)]
    d7_13=matrix_diff(0,1,9)
    assert d7_13==[["1/630","-1/1890"],["1/630","1/630"]]
    assert all(matrix_diff(1,2,k)==[["0","0"],["0","0"]] for k in orders if k<13)
    d13_19=matrix_diff(1,2,13)
    assert d13_19==[["-73/16216200","73/48648600"],
                   ["-73/16216200","-73/16216200"]]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_DIRECTIONAL_PACKET_TAYLOR",
                      "packet":"x=e_A0+epsilon*sum_t d_t e_B(-shift_t), y=z=0; no edge gate",
                      "readout":"P=sqrt(N) M^T 2diag(y)B1^T x, linear in epsilon",
                      "first_quotient_dependent_order_checked":unequal[0] if unequal else None,
                      "N7_minus_N13_order9":d7_13,
                      "N13_minus_N19_order13":d13_19,
                      "physical_speed_or_friction_inferred":False,"rows":rows},indent=2))


if __name__=="__main__":
    main()
