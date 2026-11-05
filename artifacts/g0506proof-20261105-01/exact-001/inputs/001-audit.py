#!/usr/bin/env python3
"""Exact restricted-scalar and action-unit identifiability witnesses."""
import json
from fractions import Fraction as Q
from pathlib import Path


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def rank(rows):
    M = [[Q(x) for x in row] for row in rows]
    if not M:
        return 0
    j = r = 0
    while j < len(M[0]) and r < len(M):
        pivot = next((i for i in range(r, len(M)) if M[i][j]), None)
        if pivot is None:
            j += 1; continue
        M[r], M[pivot] = M[pivot], M[r]
        f = M[r][j]; M[r] = [x/f for x in M[r]]
        for i in range(len(M)):
            if i != r:
                f = M[i][j]
                M[i] = [x-f*y for x, y in zip(M[i], M[r])]
        r += 1; j += 1
    return r


def fmt(x):
    return str(x)


def main():
    # O09: I=(1/2) sum a_i phi_i, with fixed amplitudes on this stratum.
    a = [Q(2), Q(3)]
    ell = [Q(1), Q(1)]
    phis = [[Q(1), Q(0)], [Q(0), Q(1)]]
    I = [dot(a, p)/2 for p in phis]
    L = [dot(ell, p) for p in phis]
    assert I == [1, Q(3,2)] and L == [1, 1]
    assert rank([a, ell]) == 2  # independent check: determinant -1
    assert a[0]*ell[1]-a[1]*ell[0] == -1
    a_restricted = [Q(2), Q(2)]
    k = Q(1)
    for p in [[Q(i), Q(j)] for i in range(-2, 3) for j in range(-2, 3)]:
        assert dot(a_restricted, p)/2 == k*dot(ell, p)
    # An amplitude-blind phase statistic fails as amplitudes vary.
    phase = [Q(1), Q(0)]
    assert dot(ell, phase) == 1
    assert (dot(a_restricted, phase)/2, dot([Q(4), Q(2)], phase)/2) == (1, 2)
    # Action-increment coordinates z_i=a_i*phi_i allow an amplitude-aware
    # candidate compression L=w.z. On the full space O09 is (1/2)*sum z_i.
    w_bad = [Q(1), Q(2)]
    z1, z2 = [Q(1),Q(0)], [Q(0),Q(1)]
    assert (dot(w_bad,z1),dot(w_bad,z2)) == (1,2)
    assert (sum(z1)/2,sum(z2)/2) == (Q(1,2),Q(1,2))
    assert rank([[Q(1),Q(1)],w_bad]) == 2
    w_good = [Q(3),Q(3)]
    k_good = Q(1,6)
    for z in [[Q(i),Q(j)] for i in range(-2,3) for j in range(-2,3)]:
        assert sum(z)/2 == k_good*dot(w_good,z)
    # Restricted diagonal subspace can admit a different scalar even for
    # unequal weights; the restriction must be independently sourced.
    for z in [[Q(i),Q(i)] for i in range(-2,3)]:
        assert sum(z)/2 == Q(1,3)*dot(w_bad,z)

    # O10/O14: dimension vectors in (M,L,T), native action v=(1,2,-1).
    v = [Q(1), Q(2), Q(-1)]
    length_time = [[Q(0),Q(1),Q(0)], [Q(0),Q(0),Q(1)]]
    energy_time = [[Q(1),Q(2),Q(-2)], [Q(0),Q(0),Q(1)]]
    assert rank(length_time) == 2 and rank(length_time+[v]) == 3
    assert rank(energy_time) == 2 and rank(energy_time+[v]) == 2
    assert [x+y for x,y in zip(*energy_time)] == v
    # Exact rescaling leaves dimensionless history fixed, moves A0 and eta.
    B0, a0, tau0, hbar = Q(5), Q(2), Q(3), Q(7)
    lam = Q(3,2)
    A0 = B0*a0*a0/tau0
    eta = A0/hbar
    A0b = lam*B0*a0*a0/tau0
    etab = A0b/hbar
    assert (A0,eta,A0b,etab)==(Q(20,3),Q(20,21),Q(10),Q(10,7))
    # If only beta=eta*k is read, two positive parameter pairs coincide.
    assert Q(2)*Q(1) == Q(1)*Q(2) == Q(2)
    # If O09 action I is separately measured on the native carrier and a
    # validated physical phase chi is available, eta=chi/I is identifiable.
    chi, I_measured = Q(6), Q(3)
    assert chi/I_measured == Q(2)

    result = {
        "base_references": "recovered UD ledger v0.85 G05/G06/O09/O10/O14/Q35/Q136/Q139/Q282/Q287/Q288; current Discovery base e400dfb",
        "g05_fixed_stratum": {"a": list(map(fmt,a)),"ell": list(map(fmt,ell)),
            "two_history_I": list(map(fmt,I)),"two_history_L": list(map(fmt,L)),
            "row_rank":rank([a,ell]),"determinant":-1,"scalar_exists":False},
        "g05_restricted_witness": {"a":list(map(fmt,a_restricted)),"ell":list(map(fmt,ell)),"k":fmt(k),
            "rational_grid_checks":25,"amplitude_blind_counterexample_I":["1","2"]},
        "g05_increment_compression": {"O09_increment_weights":["1/2","1/2"],
            "unequal_coarse_weights":["1","2"],"full_space_rank":2,"full_space_scalar_exists":False,
            "equal_coarse_weights":["3","3"],"full_space_k":"1/6",
            "diagonal_restricted_subspace_k_for_unequal_weights":"1/3"},
        "g06_anchor_rank": {"action_exponent":list(map(fmt,v)),"length_time_target_rank":rank(length_time+[v]),
            "length_time_anchor_rank":rank(length_time),"energy_time_target_rank":rank(energy_time+[v]),
            "energy_time_anchor_rank":rank(energy_time),"energy_plus_time_equals_action":True},
        "g06_scaling_witness": {"lambda":fmt(lam),"A0_before":fmt(A0),"A0_after":fmt(A0b),
            "eta_before":fmt(eta),"eta_after":fmt(etab)},
        "joint_product": {"beta":"2","parameter_pairs":[{"eta":"2","k":"1"},{"eta":"1","k":"2"}],
            "separate_native_I_and_validated_phase_identify_eta_when_I_nonzero":True},
        "scope":"restricted fixed-amplitude linear phase maps and declared monomial unit anchors; no Q136-to-O09 source map or physical phase bridge established",
        "physical_promotion":0
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
