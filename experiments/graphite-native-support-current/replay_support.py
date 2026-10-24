#!/usr/bin/env python3
"""Exact native 0↔1 support-current and formal honeycomb harmonic-port replay."""

import itertools
import json
from fractions import Fraction as F


def tetra_witness():
    edges = list(itertools.combinations(range(4), 2))
    b = [[0 for _ in edges] for _ in range(4)]
    for e, (i, j) in enumerate(edges):
        b[i][e], b[j][e] = -1, 1
    x = [1, 0, 0, 0]
    y = [int(edge == (0, 1)) for edge in edges]
    dx = [-sum(b[i][e]*y[e] for e in range(6)) for i in range(4)]
    dy = [sum(b[i][e]*x[i] for i in range(4)) for e in range(6)]
    flow = [[2*b[i][e]*x[i]*y[e] for e in range(6)] for i in range(4)]
    dq0 = [2*x[i]*dx[i] for i in range(4)]
    dq1 = [2*y[e]*dy[e] for e in range(6)]
    assert dq0 == [-sum(row[e] for e in range(6)) for row in flow]
    assert dq1 == [sum(flow[i][e] for i in range(4)) for e in range(6)]
    assert sum(dq0)+sum(dq1) == 0
    assert flow[0][0] == -2
    # A change of chain basis orientation changes both B column and y_e sign.
    flipped = [row[:] for row in b]
    for row in flipped:
        row[0] *= -1
    yflip = y[:]
    yflip[0] *= -1
    assert [[2*flipped[i][e]*x[i]*yflip[e] for e in range(6)]
            for i in range(4)] == flow
    # Arbitrary symmetric positive traffic activity is invisible to Q24.
    f = F(flow[0][0])
    traffic = []
    for activity in (F(1), F(3)):
        forward, reverse = activity+f/2, activity-f/2
        assert forward >= 0 and reverse >= 0
        assert (forward-reverse)/2 == f/2 == -1
        traffic.append([str(forward), str(reverse)])
    return {"edges": edges, "vertex_stock_derivative": dq0,
            "edge_stock_derivative": dq1,
            "oriented_contact_current": flow[0][0],
            "positive_traffic_pairs_for_two_activities": traffic,
            "q24_coefficient_eta_one_route_plus_one": "-1",
            "chain_orientation_invariant": True}


def honeycomb_witness(m, n):
    size=m*m+m*n+n*n
    shifts=(0,m+n,n)
    h=((1,1),(-1,1),(0,-2))
    x_a=[int(r==0) for r in range(size)]
    x_b=[0]*size
    weights=[[1+int(t==0 and r==0) for r in range(size)]
             for t in range(3)]
    def projection(weights):
        # sqrt(N)*M^T J, with J=2 diag(weights) B1^T x.
        return [2*sum(h[t][a]*weights[t][r]*
                      (x_b[(r-shifts[t])%size]-x_a[r])
                      for t in range(3) for r in range(size))
                for a in range(2)]
    uniform=projection([[1]*size for _ in range(3)])
    selected=projection(weights)
    assert uniform==[0,0]
    assert selected==[-2,-2]
    # Directly test the matrix identity 2 S(w)x = M^T J by a second summation.
    eflow=[2*weights[t][r]*
           (x_b[(r-shifts[t])%size]-x_a[r])
           for t in range(3) for r in range(size)]
    direct=[sum(eflow[t*size+r]*h[t][a]
                for t in range(3) for r in range(size)) for a in range(2)]
    assert direct==selected
    return {"mn":[m,n], "N":size,
            "sqrtN_times_uniform_harmonic_pairing":uniform,
            "sqrtN_times_local_contrast_harmonic_pairing":selected,
            "formal_weight_is_signed_edge_amplitude_not_material_stiffness":True}


def main():
    print(json.dumps({"evidence":"EXACT_CONDITIONAL_NATIVE_SUPPORT_CURRENT",
        "tetrahedron":tetra_witness(),
        "honeycomb_quotients":[honeycomb_witness(m,n)
                              for m,n in ((2,1),(3,1),(3,2))],
        "graphite_force_or_load_predicted":False},indent=2))


if __name__=="__main__":
    main()
