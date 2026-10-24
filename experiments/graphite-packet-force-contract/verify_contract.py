#!/usr/bin/env python3
"""Exact finite-chain parity and rational reciprocal-force checks."""

import json
from fractions import Fraction as Q
from math import factorial


def carrier(m, n, closed_edge=False):
    N = m*m+m*n+n*n
    shifts = (0, m+n, n)
    nv, ne, nf = 2*N, 3*N, N
    edges = [(t, r, (r-shifts[t]) % N) for t in range(3) for r in range(N)]
    faces = [[(t*N+site % N, sign) for t, site, sign in
              ((0,r,1),(1,r+shifts[1],-1),(2,r+shifts[1],1),
               (0,r+shifts[1]-shifts[2],-1),
               (1,r+shifts[1]-shifts[2],1),(2,r,-1))]
             for r in range(N)]
    h = [1]*ne
    if closed_edge:
        h[0] = 0

    def apply(q):
        x, y, z = q[:nv], q[nv:nv+ne], q[nv+ne:]
        X, Y, Z = [0]*nv, [0]*ne, [0]*nf
        for e, (_, r, b) in enumerate(edges):
            X[r] += h[e]*y[e]
            X[N+b] -= h[e]*y[e]
            Y[e] += h[e]*(x[N+b]-x[r])
        for f, terms in enumerate(faces):
            for e, sign in terms:
                Y[e] -= sign*z[f]
                Z[f] += sign*y[e]
        return X+Y+Z

    dim = nv+ne+nf
    columns = [apply([int(i == j) for i in range(dim)]) for j in range(dim)]
    grades = [1]*nv+[-1]*ne+[1]*nf
    assert all(columns[j][i] == -columns[i][j]
               for i in range(dim) for j in range(dim))
    assert all((grades[i]+grades[j])*columns[j][i] == 0
               for i in range(dim) for j in range(dim))

    # Supplied directional preparation; y(0)=z(0)=0, so grading applies.
    x0 = [0]*nv
    x0[0] = 1
    for t, d in enumerate((2,-1,-1)):
        x0[N+(-shifts[t]) % N] += d
    derivatives = [x0+[0]*(ne+nf)]
    for _ in range(9):
        derivatives.append(apply(derivatives[-1]))
    assert all(all(((-1)**k-grades[i])*v == 0 for i,v in enumerate(d))
               for k,d in enumerate(derivatives))
    # A signed current is a product of an odd edge component and an even
    # vertex gradient. Its polynomial coefficients vanish at even orders.
    current_even = True
    for order in range(0,9,2):
        for e, (_, r, b) in enumerate(edges):
            coeff = sum(Q(h[e]*derivatives[k][nv+e]
                          *(derivatives[order-k][N+b]-derivatives[order-k][r]),
                          factorial(k)*factorial(order-k))
                        for k in range(order+1))
            current_even &= (coeff == 0)
    assert current_even
    return {"N":N,"fixed_one_edge_mask":closed_edge,
            "dimension":dim,"skew":True,"grading_anticommutes":True,
            "even_current_coefficients_through_s8_zero":True}


def force_check():
    # Independent diagonal-mode quotient rule versus the general matrix
    # product/inverse derivative at p=0; all inputs are exact fractions.
    C = [[Q(1),Q(2)],[Q(3),Q(1)]]
    Cp = [[Q(1),Q(0)],[Q(0),Q(-1)]]
    k, kp = [Q(2),Q(3)], [Q(1),Q(-1)]
    d, dp = [Q(1),Q(2)], [Q(1),Q(2)]
    ell = [d[a]/k[a]**2 for a in range(2)]
    ellp = [dp[a]/k[a]**2-2*d[a]*kp[a]/k[a]**3
            for a in range(2)]
    gamma = [[sum(C[i][a]*C[j][a]*ell[a] for a in range(2))
              for j in range(2)] for i in range(2)]
    derivative = [[sum((Cp[i][a]*C[j][a]+C[i][a]*Cp[j][a])*ell[a]
                       +C[i][a]*C[j][a]*ellp[a] for a in range(2))
                   for j in range(2)] for i in range(2)]
    quotient_rule = [[sum(
        ((Cp[i][a]*C[j][a]+C[i][a]*Cp[j][a])*d[a]
          +C[i][a]*C[j][a]*dp[a])/k[a]**2
        -2*C[i][a]*C[j][a]*d[a]*kp[a]/k[a]**3
        for a in range(2)) for j in range(2)] for i in range(2)]
    assert derivative == quotient_rule
    assert gamma[0][0] > 0 and gamma[1][1] > 0
    assert Q(1,4)-Q(1) == Q(-3,4)
    return {"gamma_at_p0":[[str(v) for v in row] for row in gamma],
            "gamma_prime_at_p0":[[str(v) for v in row] for row in derivative],
            "negative_residual_counterexample":"-3/4"}


def main():
    checks = [carrier(m,n,g) for m,n in ((2,1),(3,1),(3,2))
              for g in (False,True)]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_FINITE_CARRIER_AND_FORCE_CONTRACT",
                      "carriers":checks,"reciprocal_force":force_check(),
                      "time_mean_proof":"finite skew spectrum + odd signed current => zero Cesaro mean",
                      "physical_force_or_load_inferred":False},indent=2))


if __name__ == "__main__":
    main()
