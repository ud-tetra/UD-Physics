#!/usr/bin/env python3
"""EXACT/CONDITIONAL Hermite gate for the original symmetric UD 3D moving pulse.
A PASS does not validate any numerical moving-propagator premise.
Full local numerical reproduction sources: checkpoint 025 ZIP.
"""
from fractions import Fraction as F
from json import dumps

def bound(G, V, W, J):
    d = F(1,80)  # nearest distance on 4001-node u in [0,100] mesh
    return G + d*V + d*d*W/2 + d*d*d*J/6

def test():
    robust = bound(F(1,12500), F(7,10000), F(1,125), F(1))
    tight = bound(F(7,100000), F(61,100000), F(31,5000), F(1))
    assert robust == F(6889,76800000)
    assert tight == F(30119,384000000)
    assert F(1,40)-robust == F(1913111,76800000)
    assert F(1,40)-tight == F(9569881,384000000)
    assert robust < F(1,10000)
    d = F(1,80)
    v_robust = F(7,10000) + d*F(1,125) + d*d/2
    assert v_robust == F(281,320000) < F(1,1000)
    return {'status':'PASS_EXACT_CONDITIONAL_ONLY',
            'robust_g':str(robust),
            'tight_g':str(tight),
            'robust_v':str(v_robust),
            'remaining_to_one_fortieth':str(F(1,40)-robust),
            'unproved':['true-ODE 4001 nodal g,v,w bounds',
                        'true continuous operator jerk<=1',
                        'uniform nonlinear remainder and positive strut domain']}

if __name__=='__main__':
    print(dumps(test(), indent=2))
