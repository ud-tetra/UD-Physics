#!/usr/bin/env python3
"""Exact rational checks for a proposed flow-typed Q24 completion and face null."""

import json
from fractions import Fraction as F


def q24(eta, wij, wji, xi):
    """Signed route: Xi_ij=xi, Xi_ji=-xi."""
    return eta * xi * (wij - wji) / 2


def torus_face(m, n):
    size = m*m + m*n + n*n
    s1, s2 = m+n, n
    def edge(t, r):
        return t*size + r % size
    # One oriented hexagonal face in the prior quotient-family convention.
    f = [0]*(3*size)
    for t, site, sign in ((0,0,1),(1,s1,-1),(2,s1,1),
                          (0,s1-s2,-1),(1,s1-s2,1),(2,0,-1)):
        f[edge(t, site)] += sign
    # Every face is a cycle, and the two constant harmonic edge columns have
    # zero pairing with each face boundary. All operations are exact integers.
    vertices = [0]*(2*size)
    for r in range(size):
        for t, target in enumerate((r,r-s1,r-s2)):
            vertices[r] -= f[edge(t,r)]
            vertices[size+target % size] += f[edge(t,r)]
    h1, h2 = (1,-1,0), (1,1,-2)
    proj = [sum(f[edge(t,r)]*h[t] for t in range(3) for r in range(size))
            for h in (h1,h2)]
    assert all(x == 0 for x in vertices) and proj == [0,0]
    assert sum(abs(x) for x in f) == 6
    # A global zero-divergence direction can have a nonzero harmonic pairing.
    global_h1 = [h1[t] for t in range(3) for _ in range(size)]
    assert sum(global_h1[i]*global_h1[i] for i in range(3*size)) == 2*size
    return {"mn":[m,n],"N":size,"local_face_nonzero_edges":6,
            "face_divergence":vertices,"harmonic_pairing":proj,
            "global_h1_self_pairing":2*size}


def main():
    a,b,eta,xi=F(2),F(1),F(1),F(1)
    # A reversible two-state chain may have unequal bare rates.
    p0,p1=b/(a+b),a/(a+b)
    t01,t10=p0*a,p1*b
    assert t01==t10==F(2,3)
    assert q24(eta,t01,t10,xi)==0
    assert q24(eta,a,b,xi)==F(1,2)
    # Three-state ring: clockwise rate a, reverse rate b, uniform p.
    p=[F(1,3)]*3
    dp=[p[(i-1)%3]*a+p[(i+1)%3]*b-p[i]*(a+b) for i in range(3)]
    assert dp==[0]*3
    traffic_plus,traffic_minus=a/3,b/3
    current=traffic_plus-traffic_minus
    assert current==F(1,3)
    assert q24(eta,traffic_plus,traffic_minus,xi)==F(1,6)
    cases=[torus_face(m,n) for m,n in ((2,1),(3,1),(3,2))]
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_TRAFFIC_AND_FACE_WITNESS",
        "two_state":{"p":[str(p0),str(p1)],"traffic":[str(t01),str(t10)],
                     "flux_typed_q24":str(q24(eta,t01,t10,xi)),
                     "bare_rate_q24_spurious_equilibrium":str(q24(eta,a,b,xi))},
        "three_state_ring":{"p":[str(v) for v in p],"dp":[str(v) for v in dp],
            "directed_traffic":[str(traffic_plus),str(traffic_minus)],
            "net_current":str(current),"flux_typed_q24":str(q24(eta,traffic_plus,traffic_minus,xi))},
        "honeycomb_local_face":cases,"graphite_material_fit":False},indent=2))


if __name__=="__main__":
    main()
