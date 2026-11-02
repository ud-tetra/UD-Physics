#!/usr/bin/env python3
"""Exact harmonic transfer under a supplied one-edge Q167-style pulse."""
from fractions import Fraction as F

H = ((1, 1), (-1, 1), (0, -2))


def quotient(m, n):
    N = m*m + m*n + n*n
    shifts = (0, m+n, n)
    edges = [(t, r, (r-shifts[t]) % N) for t in range(3) for r in range(N)]
    faces = [[(t*N+site % N, sign) for t, site, sign in
              ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
               (0,r+shifts[1]-shifts[2],-1),
               (1,r+shifts[1]-shifts[2],1),(2,r,-1))]
             for r in range(N)]
    return N, edges, faces


def apply(q, N, edges, faces, closed=None):
    nv, ne = 2*N, 3*N
    x, y, z = q[:nv], q[nv:nv+ne], q[nv+ne:]
    X, Y, Z = [F(0)]*nv, [F(0)]*ne, [F(0)]*N
    for e, (_, r, k) in enumerate(edges):
        mask = int(e != closed)
        X[r] += mask*y[e]
        X[N+k] -= mask*y[e]
        Y[e] += mask*(x[N+k]-x[r])
    for f, terms in enumerate(faces):
        for e, sign in terms:
            Y[e] -= sign*z[f]
            Z[f] += sign*y[e]
    return X+Y+Z


def harmonic_coordinates(q, N, edges):
    y = q[2*N:5*N]
    p = [sum(H[t][a]*y[e] for e, (t,_,_) in enumerate(edges))
         for a in range(2)]
    return (p[0]/(2*N), p[1]/(6*N))


def check(m, n):
    N, edges, faces = quotient(m,n)
    assert all(sum(r == i for _, r, _ in edges) == 3 for i in range(N))
    assert all(sum(k == i for _, _, k in edges) == 3 for i in range(N))
    assert all(sum(e == target for face in faces for e, _ in face) == 2
               for target in range(3*N))
    assert 2*216**2*N < 10000**2  # squared uniform Taylor-ratio bound
    q0 = [F(0)]*(6*N)
    q0[0] = F(1)
    assert harmonic_coordinates(q0,N,edges) == (0,0)
    results = []
    for t in range(3):
        # Edge (t,0) starts at A0. The mask closes only this supplied edge.
        closed = t*N
        q1 = apply(q0,N,edges,faces,closed)
        q2 = apply(q1,N,edges,faces,closed)
        q3 = apply(q2,N,edges,faces,closed)
        a1 = harmonic_coordinates(q1,N,edges)
        a2 = harmonic_coordinates(q2,N,edges)
        a3 = tuple(v/F(6) for v in harmonic_coordinates(q3,N,edges))
        expected = (F(H[t][0],2*N), F(H[t][1],6*N))
        assert a1 == expected and a2 == (0,0)
        assert a3 == tuple(-v/F(3) for v in a1)
        assert 2*N*a1[0]**2 + 6*N*a1[1]**2 == F(2,3*N)
        # After reopening, any complete state has constant U^T y.
        q_sample = [F((i%7)-3, i+1) for i in range(6*N)]
        assert harmonic_coordinates(apply(q_sample,N,edges,faces),N,edges) == (0,0)
        results.append((t, a1, a3))
    assert tuple(sum(r[1][a] for r in results) for a in range(2)) == (0,0)
    return N, results


if __name__ == "__main__":
    for m,n in ((2,1),(3,1),(3,2)):
        N, results = check(m,n)
        for t,a1,a3 in results:
            print(f"N={N} closed_class={t} a'(0)={a1} cubic={a3} stock_coeff=2/(3*{N})")
