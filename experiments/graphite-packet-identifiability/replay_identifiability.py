#!/usr/bin/env python3
"""Exact formal matrix inversion/quotient ratios of the prior packet replay."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path


def mat(rows):
    return [[F(v) for v in row] for row in rows]


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]


def neg(a):
    return [[-v for v in row] for row in a]


def inverse(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det
    return [[a[1][1]/det,-a[0][1]/det],
            [-a[1][0]/det,a[0][0]/det]],det


def invseries(b):
    c0,_=inverse(b[0])
    c=[c0]
    for n in range(1,len(b)):
        acc=mat([[0,0],[0,0]])
        for k in range(1,n+1):
            acc=add(acc,mul(b[k],c[n-k]))
        c.append(neg(mul(c0,acc)))
    return c


def product(a,b):
    return [sum_mats([mul(a[k],b[n-k]) for k in range(n+1)])
            for n in range(min(len(a),len(b)))]


def sum_mats(ms):
    z=mat([[0,0],[0,0]])
    for m in ms:
        z=add(z,m)
    return z


def render(m):
    return [[str(v) for v in row] for row in m]


def main():
    source=Path(__file__).resolve().parents[1]/"graphite-directional-packet"/"replay_packet.py"
    spec=importlib.util.spec_from_file_location("packet_source",source)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    data=[mod.family(m,n) for m,n in ((2,1),(3,1),(3,2))]
    b=[[mat(m) for m in row["linear_epsilon_matrix_coefficients"]] for row in data]
    m1=b[0][0]
    m1inv,det=inverse(m1)
    assert det==192 and render(m1inv)==[["-1/16","-1/48"],["1/16","-1/16"]]
    assert all(row[0]==m1 for row in b)

    ratios=[product(b[0],invseries(b[1])),product(b[1],invseries(b[2]))]
    identity=mat([[1,0],[0,1]])
    zero=mat([[0,0],[0,0]])
    assert all(r[0]==identity for r in ratios)
    assert all(v==zero for v in ratios[0][1:4])
    assert ratios[0][4]==mat([[F(-1,7560),0],[0,F(-1,7560)]])
    assert all(v==zero for v in ratios[1][1:6])
    assert ratios[1][6]==mat([[F(73,194594400),0],[0,F(73,194594400)]])
    # Verify the inverse convolution coefficient by coefficient, not just the lead term.
    for row in b:
        inv=invseries(row)
        check=product(row,inv)
        assert check[0]==identity and all(v==zero for v in check[1:])
    print(json.dumps({
        "evidence":"EXACT_CONDITIONAL_PACKET_IDENTIFIABILITY",
        "M1":render(m1),"det_M1":str(det),"inverse_M1":render(m1inv),
        "series_variable":"t=s^2; L_N=s B_N(t)",
        "ratio_L7_L13_inverse_coeff_t4":render(ratios[0][4]),
        "ratio_L13_L19_inverse_coeff_t6":render(ratios[1][6]),
        "ratio_L7_L13_inverse_through_t8":[render(v) for v in ratios[0]],
        "ratio_L13_L19_inverse_through_t8":[render(v) for v in ratios[1]],
        "single_quotient_locally_invertible_for_small_nonzero_s":True,
        "common_packet_and_clock_required_for_cross_quotient_ratio":True,
        "physical_force_or_friction_inferred":False
    },indent=2))


if __name__=="__main__":
    main()
