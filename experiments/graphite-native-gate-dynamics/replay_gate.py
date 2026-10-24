#!/usr/bin/env python3
"""Exact Taylor derivatives of a masked 0-1 contact in the full 0/1/2 torus."""

import json
from fractions import Fraction as F
from math import comb, factorial


def family(m, n, gate, max_order=17):
    size = m*m+m*n+n*n
    s1,s2=m+n,n
    edges=[]
    for t in range(3):
        for r in range(size):
            target=(r-(0,s1,s2)[t])%size
            edges.append((t,r,target))
    face_terms=[]
    for r in range(size):
        terms=((0,r,1),(1,r+s1,-1),(2,r+s1,1),
               (0,r+s1-s2,-1),(1,r+s1-s2,1),(2,r,-1))
        face_terms.append([(t*size+site%size,sign) for t,site,sign in terms])
    h=[1]*(3*size)
    if gate:
        h[0]=0  # close both vertex contacts of the same edge e(0,0)
    def apply(x,y,z):
        xx=[0]*(2*size)
        yy=[0]*(3*size)
        zz=[0]*size
        for e,(t,r,target) in enumerate(edges):
            a,b=r,size+target
            xx[a]+=h[e]*y[e]
            xx[b]-=h[e]*y[e]
            yy[e]+=h[e]*(x[b]-x[a])
        for f,terms in enumerate(face_terms):
            for e,sign in terms:
                yy[e]-=sign*z[f]
                zz[f]+=sign*y[e]
        return xx,yy,zz
    # The common quotient presentation admits a 120-degree rotation about A0.
    q_candidates=[q for q in range(1,size)
                  if (q*s1+m)%size==0 and (q*s2+s1)%size==0
                  and pow(q,3,size)==1]
    assert len(q_candidates)==1
    q=q_candidates[0]
    def rotate(x,y,z):
        xx=[0]*(2*size)
        yy=[0]*(3*size)
        zz=[0]*size
        for r in range(size):
            xx[(q*r)%size]=x[r]
            xx[size+(q*r-s1)%size]=x[size+r]
            zz[(q*r-m)%size]=z[r]
        for e,(t,r,_) in enumerate(edges):
            yy[((t+1)%3)*size+(q*r)%size]=y[e]
        return xx,yy,zz
    if not gate:
        # Basis check establishes commutation of the full linear generator
        # with the exact vertex/edge/face rotation, not only a sampled orbit.
        dims=(2*size,3*size,size)
        for sector,dim in enumerate(dims):
            for i in range(dim):
                basis=[[0]*d for d in dims]
                basis[sector][i]=1
                assert apply(*rotate(*basis))==rotate(*apply(*basis))
    x0=[0]*(2*size)
    x0[0]=1
    zero_y=[0]*(3*size)
    zero_z=[0]*size
    deriv=[(x0,zero_y,zero_z)]
    if not gate:
        assert rotate(*deriv[0])==deriv[0]
    for _ in range(max_order):
        deriv.append(apply(*deriv[-1]))
    # P(s)=sqrt(N) M^T J(s), J_e=2 y_e(B1_mask^T x)_e.
    hh=((1,1),(-1,1),(0,-2))
    derivative_coeff=[]
    for order in range(1,max_order+1,2):
        val=[0,0]
        for k in range(1,order+1,2):
            y=deriv[k][1]
            x=deriv[order-k][0]
            factor=2*comb(order,k)
            for e,(t,r,target) in enumerate(edges):
                term=factor*h[e]*y[e]*(x[size+target]-x[r])
                val[0]+=hh[t][0]*term
                val[1]+=hh[t][1]*term
        derivative_coeff.append([str(F(v,factorial(order))) for v in val])
    # Matrix skewness: a^T A b = -(A a)^T b on two exact test states.
    a=deriv[0]
    b=deriv[1]
    def dot(v,w):
        return sum(p*q for vv,ww in zip(v,w) for p,q in zip(vv,ww))
    assert dot(a,apply(*b))==-dot(apply(*a),b)
    assert all(pair==["0","0"] for pair in derivative_coeff) if not gate else derivative_coeff[0]==["-2","-2"]
    return {"mn":[m,n],"N":size,"gate":"one_closed_edge" if gate else "free",
            "C3_multiplier_q":q,"free_generator_C3_verified":not gate,
            "orders":list(range(1,max_order+1,2)),
            "sqrtN_harmonic_taylor_coefficients":derivative_coeff}


def main():
    patterns=((2,1),(3,1),(3,2))
    free=[family(m,n,False) for m,n in patterns]
    gated=[family(m,n,True) for m,n in patterns]
    orders=gated[0]["orders"]
    unequal=[orders[i] for i in range(len(orders))
             if len({tuple(row["sqrtN_harmonic_taylor_coefficients"][i])
                     for row in gated})>1]
    assert unequal[0]==7
    g7,g13,g19=gated
    def coeff(row,order):
        return F(row["sqrtN_harmonic_taylor_coefficients"][orders.index(order)][0])
    assert coeff(g7,7)-coeff(g13,7)==F(1,42)
    assert coeff(g13,7)==coeff(g19,7)
    assert coeff(g13,9)-coeff(g19,9)==F(13,22680)
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_MASKED_SOURCE_TAYLOR",
        "full_complex":"C0⊕C1⊕C2, original B2 retained under 0-1 contact mask",
        "first_quotient_dependent_order_checked":unequal[0] if unequal else None,
        "N7_minus_N13_order7_each_component":"1/42",
        "N13_minus_N19_order9_each_component":"13/22680",
        "free":free,"gated":gated,"physical_time_or_friction_inferred":False},indent=2))


if __name__=="__main__":
    main()
