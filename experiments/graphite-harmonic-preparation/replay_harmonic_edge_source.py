#!/usr/bin/env python3
"""Exact finite check of the prepared harmonic-square edge source."""
from fractions import Fraction as F

H = ((1, 1), (-1, 1), (0, -2))  # unnormalized harmonic basis


def check(m, n, a, b):
    N = m*m + m*n + n*n
    shifts = (0, m+n, n)
    edges = [(t, r, (r-shifts[t]) % N) for t in range(3) for r in range(N)]
    faces = [[(t*N+site % N, sign) for t, site, sign in
              ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
               (0,r+shifts[1]-shifts[2],-1),
               (1,r+shifts[1]-shifts[2],1),(2,r,-1))]
             for r in range(N)]
    for axis in range(2):
        boundary = [0]*(2*N)
        for t, r, k in edges:
            boundary[r] -= H[t][axis]
            boundary[N+k] += H[t][axis]
        assert boundary == [0]*(2*N)
        assert all(sum(sign*H[e//N][axis] for e, sign in f) == 0
                   for f in faces)
    y = [F(H[t][0]*a + H[t][1]*b) for t, _, _ in edges]
    w = [v*v for v in y]
    S = [[F(0) for _ in range(2*N)] for _ in range(2)]
    for e, (t, r, k) in enumerate(edges):
        for axis in range(2):
            S[axis][r] -= H[t][axis]*w[e]
            S[axis][N+k] += H[t][axis]*w[e]
    v = (F(4*a*b), F(2*(a*a-3*b*b)))
    for axis in range(2):
        assert S[axis] == [-v[axis]]*N + [v[axis]]*N
    # Native harmonic amplitude H^T y cannot be created from zero by ungated A.
    # Since B1 H=0 and B2^T H=0, H^T dy/ds=0 for every x,z.
    # A prepared y=H a has x=z=0 and dy/ds=dx/ds=dz/ds=0.
    assert any(v)
    return N, tuple(v), 2*N*sum(z*z for z in v)


if __name__ == "__main__":
    for m,n in ((2,1),(3,1),(3,2)):
        for a,b in ((1,0),(1,1),(2,-1)):
            N,v,frob2=check(m,n,a,b)
            print(f"N={N}, a=({a},{b}), v={v}, ||S||_F^2={frob2}")
