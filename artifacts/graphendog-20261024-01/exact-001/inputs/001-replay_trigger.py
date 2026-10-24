#!/usr/bin/env python3
"""Exact orbit-trigger and masked-stock checks on three honeycomb quotients."""

import json
from fractions import Fraction as F


def check(m, n):
    N = m*m + m*n + n*n
    s1, s2 = m+n, n
    shifts = (0, s1, s2)
    q = next(q for q in range(1, N) if (q*s1+m)%N == 0
             and (q*s2+s1)%N == 0 and pow(q, 3, N) == 1)
    edges = [(t, r, (r-shifts[t])%N) for t in range(3) for r in range(N)]
    faces = [[(t*N+site%N, sign) for t,site,sign in
              ((0,r,1),(1,r+s1,-1),(2,r+s1,1),
               (0,r+s1-s2,-1),(1,r+s1-s2,1),(2,r,-1))]
             for r in range(N)]

    def rotate(x, y, z):
        X, Y, Z = [0]*(2*N), [0]*(3*N), [0]*N
        for r in range(N):
            X[q*r%N] = x[r]
            X[N+(q*r-s1)%N] = x[N+r]
            Z[(q*r-m)%N] = z[r]
        for e, (t,r,_) in enumerate(edges):
            Y[((t+1)%3)*N+q*r%N] = y[e]
        return X,Y,Z

    def generator(h, x, y, z):
        X, Y, Z = [0]*(2*N), [0]*(3*N), [0]*N
        for e, (_,r,b) in enumerate(edges):
            X[r] += h[e]*y[e]
            X[N+b] -= h[e]*y[e]
            Y[e] += h[e]*(x[N+b]-x[r])
        for f, terms in enumerate(faces):
            for e, sign in terms:
                Y[e] -= sign*z[f]
                Z[f] += sign*y[e]
        return X,Y,Z

    def strain(x, y):
        return [(x[N+b]-x[r])**2+y[e]**2
                for e,(_,r,b) in enumerate(edges)]

    def mask(x, y, threshold):
        return [int(u < threshold) for u in strain(x, y)]

    def stock(h, x, y, z):
        return sum(v*v for v in x)+sum(h[e]*v*v for e,v in enumerate(y)) \
               +sum(v*v for v in z)

    def stock_derivative(h, x, y, z):
        X,Y,Z = generator(h,x,y,z)
        left = 2*sum(a*b for a,b in zip(x,X)) \
               +2*sum(h[e]*a*b for e,(a,b) in enumerate(zip(y,Y))) \
               +2*sum(a*b for a,b in zip(z,Z))
        B2z = [0]*(3*N)
        for f, terms in enumerate(faces):
            for e, sign in terms:
                B2z[e] += sign*z[f]
        right = 2*sum((1-h[e])*y[e]*B2z[e] for e in range(3*N))
        assert left == right
        return left

    x0, y0, z0 = [1]+[0]*(2*N-1), [0]*(3*N), [0]*N
    assert rotate(x0,y0,z0) == (x0,y0,z0)
    low, high = mask(x0,y0,F(1,2)),mask(x0,y0,F(3,2))
    orbit = [0,N,2*N]
    assert [i for i,v in enumerate(low) if not v] == orbit
    assert all(high)
    assert generator(low,x0,y0,z0) == ([0]*(2*N),[0]*(3*N),[0]*N)

    # Every fixed C3-invariant mask makes the full 0/1/2 generator commute.
    for h in (low,high):
        dims=(2*N,3*N,N)
        for sector,dim in enumerate(dims):
            for i in range(dim):
                basis=[[0]*d for d in dims]
                basis[sector][i]=1
                assert generator(h,*rotate(*basis)) == rotate(*generator(h,*basis))

    # The threshold is equivariant for an arbitrary non-invariant integer state.
    xa=[(3*i+1)%5-2 for i in range(2*N)]
    ya=[(7*i+2)%5-2 for i in range(3*N)]
    za=[(2*i+1)%3-1 for i in range(N)]
    xa_r,ya_r,za_r=rotate(xa,ya,za)
    h=mask(xa,ya,F(5,2))
    h_r=rotate([0]*(2*N),h,[0]*N)[1]
    assert mask(xa_r,ya_r,F(5,2)) == h_r
    assert generator(h_r,xa_r,ya_r,za_r)==rotate(*generator(h,xa,ya,za))
    flow=stock_derivative(h,xa,ya,za)
    assert sum(a*b for a,b in zip(xa,generator(h,xa,ya,za)[0])) \
           +sum(a*b for a,b in zip(ya,generator(h,xa,ya,za)[1])) \
           +sum(a*b for a,b in zip(za,generator(h,xa,ya,za)[2])) == 0

    yw=[int(i in orbit) for i in range(3*N)]
    # A separate fixed-state switch with nonzero y: tau 5/2 -> 3/2.
    # It witnesses stock relabeling, not a dynamically derived threshold path.
    open_w=mask(x0,yw,F(5,2))
    closed_w=mask(x0,yw,F(3,2))
    assert all(open_w) and closed_w == low
    jump=stock(closed_w,x0,yw,z0)-stock(open_w,x0,yw,z0)
    assert jump == -3
    assert jump == sum((closed_w[e]-open_w[e])*yw[e]**2 for e in range(3*N))
    return {"mn":[m,n],"N":N,"C3_multiplier":q,
            "closed_at_threshold_half":orbit,
            "closed_at_threshold_three_halves":[],
            "low_threshold_seed_frozen":True,
            "full_generator_C3_commutation_both_masks":True,
            "state_dependent_threshold_equivariance":True,
            "full_norm_derivative":0,
            "masked_stock_flow_witness":flow,
            "three_edge_orbit_transition_masked_stock_jump":jump}


def main():
    rows=[check(m,n) for m,n in ((2,1),(3,1),(3,2))]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_EQUIVARIANT_TRIGGER_OBSTRUCTION",
                      "threshold_u":"(B1^T x)_e^2+y_e^2; h_e=1 iff u_e<tau",
                      "clock":"dimensionless native s; instantaneous fixed-state mask change",
                      "result":"C3-equivariant deterministic trigger cannot choose a unique edge from C3-fixed seed; harmonic readout remains zero",
                      "transition_law":"Delta S_tilde_H=sum_e (h_new-h_old)y_e^2; full norm has zero jump",
                      "physical_gate_or_friction_inferred":False,
                      "rows":rows},indent=2))


if __name__ == "__main__":
    main()
