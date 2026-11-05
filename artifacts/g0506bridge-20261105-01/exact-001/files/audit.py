"""Exact parity witness and seven-mode LC pullback, without physical fitting."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def mm(a, b):
    return [[sum((u * v for u, v in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def tr(a):
    return list(map(list, zip(*a)))


def rank(a):
    a = [r[:] for r in a]
    k = 0
    for j in range(len(a[0])):
        p = next((p for p in range(k, len(a)) if a[p][j]), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        f = a[k][j]
        a[k] = [v / f for v in a[k]]
        for i in range(len(a)):
            if i != k:
                f = a[i][j]
                a[i] = [v - f * w for v, w in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def main():
    simplices = [s for k in range(1, 5) for s in combinations(range(4), k)]
    ix = {s: i for i, s in enumerate(simplices)}
    d = [[F(0)] * 15 for _ in range(15)]
    for s in simplices:
        for j in range(len(s)):
            if len(s) > 1:
                d[ix[s[:j] + s[j + 1:]]][ix[s]] = F((-1)**j)
    A = [[d[i][j] - d[j][i] for j in range(15)] for i in range(15)]
    P = [[-v / 4 for v in r] for r in mm(A, A)]
    assert mm(P, P) == P and rank(P) == 14
    J = [[v / 2 for v in r] for r in A]
    assert mm(J, J) == [[-v for v in r] for r in P]

    # One orthonormal J-plane has native (u',v')=(-2v,2u).
    # Seven identical planes realize the active 14-dimensional space.
    A14 = [[F(0)] * 14 for _ in range(14)]
    M = [[F(0)] * 14 for _ in range(14)]
    K = [[F(0)] * 14 for _ in range(14)]
    L, C, phi = F(1), F(1), F(3, 2)  # arbitrary exact fixture values
    Z, tau = F(1), F(2)
    A0 = phi * phi / Z
    for j in range(7):
        k = 2*j
        A14[k][k+1], A14[k+1][k] = -2, 2
        M[k][k], M[k+1][k+1] = phi, -phi/Z  # (Phi,Q)
        K[k][k+1], K[k+1][k] = 1/C, -1/L
    KM = mm(K, M)
    MA = [[v/tau for v in r] for r in mm(M, A14)]
    assert KM == MA
    G = [[F(i == j) for j in range(14)] for i in range(14)]  # L=C=1
    B = mm(tr(M), mm(G, M))
    assert B == [[F(2*A0/tau) if i == j else F(0) for j in range(14)] for i in range(14)]
    assert A0 == F(9, 4)
    # Symmetrized canonical one-form evaluated at x=(u,v), dx=(du,dv).
    x = [F(0)]*14
    dx = [F(0)]*14
    x[0], dx[1] = F(2, 3), F(5, 4)
    z = [sum(M[i][j]*x[j] for j in range(14)) for i in range(14)]
    dz = [sum(M[i][j]*dx[j] for j in range(14)) for i in range(14)]
    theta = F(1,2)*(x[0]*dx[1]-x[1]*dx[0])
    canonical = F(1,2)*(z[1]*dz[0]-z[0]*dz[1])
    assert canonical == A0*theta
    # For energy and physical period, product identifies A0*a after unit
    # native support has been assigned: E=A0*a/tau, T_state=pi*tau.
    a = sum(v*v for v in x)
    energy = F(1,2)*sum(v*v for v in z)
    assert energy == A0*a/tau and energy*tau/a == A0

    # Parity: a scalar path density depending on x only, integrated with
    # positive unsigned path measure, contributes equally in reverse.
    even, odd = F(2,3), F(5,4)
    forward, reverse = even+odd, even-odd
    assert (forward+reverse)/2 == even
    assert (forward-reverse)/2 == odd
    assert forward != -reverse
    result = {
        "status": "EXACT_CONDITIONAL_MODEL_PASS",
        "native_active_rank": rank(P),
        "fixture": {"modes":7,"L_H":"1 fixture unit","C_F":"1 fixture unit","Z":"1 fixture ohm","tau0":"2 fixture seconds","Phi_star":"3/2 fixture weber","A0":"9/4 fixture joule-second","KM_equals_MA_over_tau":True,"MTGM_equals_2A0_over_tau_I":True,"canonical_pullback":True},
        "parity_witness": {"even":"2/3","odd":"5/4","forward":str(forward),"reverse":str(reverse),"target_odd_requires_even_zero":True},
        "empirical_certificate":"BLOCKED_NO_MEASUREMENTS_OR_SOURCE_CORRESPONDENCE",
        "physical_promotion":0
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":result["status"],"native_active_rank":14,"empirical_certificate":result["empirical_certificate"]}))


if __name__ == "__main__":
    main()
