#!/usr/bin/env python3
"""Exact K4 discriminant charge and finite Weyl source-selection audit.

Source-grounded D=Z^3/(4I-11^T)Z^3; S4 acts on integral
zero-sum vertex charges. All arithmetic integers, modulo four and Fractions.
No native physical charge/Hamiltonian interpretation is claimed.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

L = [[3 if i == j else -1 for j in range(3)] for i in range(3)]
Lin = [[F(1 + (i == j), 4) for j in range(3)] for i in range(3)]
assert all(sum(L[i][k] * Lin[k][j] for k in range(3)) == (i == j)
           for i in range(3) for j in range(3))
assert (L[0][0] * (L[1][1]*L[2][2]-L[1][2]*L[2][1])
        -L[0][1] * (L[1][0]*L[2][2]-L[1][2]*L[2][0])
        +L[0][2] * (L[1][0]*L[2][1]-L[1][1]*L[2][0])) == 16


def label(t):
    return tuple(int(sum(Lin[i][j] * t[j] for j in range(3)) * 4) % 4
                 for i in range(3))

reps = {}
for t in product(range(4), repeat=3):
    reps.setdefault(label(t), t)
D = sorted(reps)
assert len(D) == 16
zero = label((0, 0, 0))
assert zero == (0, 0, 0)


def act(t, perm):
    rho = tuple(t) + (-sum(t),)
    out = [0] * 4
    for i, v in enumerate(rho):
        out[perm[i]] = v
    return label(out[:3])

perms = list(permutations(range(4)))
actions = {}
for p in perms:
    f = [act(reps[d], p) for d in D]
    assert set(f) == set(D)
    actions[p] = f
# S4 action is well-defined on quotient for any alternate t representative.
for t in product(range(4), repeat=3):
    for p in perms:
        assert act(t, p) == actions[p][D.index(label(t))]

orbit_sets = set()
for d in D:
    orbit_sets.add(frozenset(actions[p][D.index(d)] for p in perms))
orbits = sorted(orbit_sets, key=lambda o: (len(o), sorted(o)))
assert [len(o) for o in orbits] == [1, 3, 12]
assert orbits[0] == frozenset([zero])
orders = {}
for d in D:
    orders[d] = next(n for n in (1, 2, 4) if all((n*z) % 4 == 0 for z in d))
assert [set(orders[d] for d in o) for o in orbits] == [{1}, {2}, {4}]
# Any scalar group charge q:D->Z or R is zero (4-torsion -> torsion-free).
# The S4 invariant character group D^hat is zero: perfect invariant pairing,
# fixed points of the D action consist only of zero.


def pairing(d, e):
    a, b = reps[d], reps[e]
    x = sum(F(a[i]) * Lin[i][j] * b[j] for i in range(3) for j in range(3))
    return int(4*x) % 4

for p in perms:
    for d in D:
        for e in D:
            assert pairing(d, e) == pairing(act(reps[d], p), act(reps[e], p))
assert all((pairing(d, e) - pairing(e, d)) % 4 == 0 for d in D for e in D)
character_checks = 0
for d in D:
    vals = [pairing(d, e) for e in D]
    counts = Counter(vals)
    if d == zero:
        assert counts[0] == 16
    else:
        assert counts[0] == counts[2] and counts[1] == counts[3]
    character_checks += 1
# The same orthogonality implies the finite translations and modulations
# form a full matrix algebra; a commuting Hamiltonian is scalar.
# But S4 alone allows at least one independent diagonal energy per orbit.
# Use one representative of arbitrary invariant quadratic 'energy' from
# diagonal values v0, v2, v4; all v2/v4 nonnegative preserve positivity.
examples=[]
for e2,e4 in [(0,0),(1,1),(1,2),(2,1),(2,2),(1,3)]:
    vals={d: (0 if orders[d] == 1 else e2 if orders[d] == 2 else e4) for d in D}
    assert min(vals.values()) >= 0
    assert all(vals[d] == vals[act(reps[d],p)] for p in perms for d in D)
    examples.append({'E2':e2,'E4':e4,'level_multiplicities':
                     {str(e):sum(v==e for v in vals.values()) for e in sorted(set(vals.values()))}})
# Scalar Weyl-central H can have just one eigenvalue; S4 diagonal sector
# potentials have 3 separate parameters and a free physical energy scale.
output = {
 'status':'PASS','labels':['EXACT','CONDITIONAL','HYPOTHESIS','FAILED','OPEN'],
 'source_group':'D=Z^3/(4I3-ones)Z^3 = Z4 x Z4, K4 reduced Laplacian det16',
 'det_reduced_laplacian':16,'finite_charge_label_count':len(D),
 'signed_S4_actions':len(perms),'S4_orbit_sizes':[len(o) for o in orbits],
 'S4_orbit_orders':[list(set(orders[d] for d in o))[0] for o in orbits],
 'perfect_pairing_char_orthogonality_checks':character_checks,
 'pairing_S4_invariant_checks':len(perms)*len(D)*len(D),
 'scalar_charge_additive_D_to_Z':'ONLY_ZERO since exponent4 and Z torsion-free',
 'S4_invariant_U1_characters':'ONLY_TRIVIAL via invariant perfect pairing and fixed D={0}',
 'finite_Weyl_full_translation_and_modulation_commutant':'C*I16; no nontrivial Hamiltonian if full Weyl symmetry imposed',
 'S4_invariant_diagonal_H':'v0*P_order1+v2*P_order2+v4*P_order4, independent real coefficients; scalar offset v0 unphysical',
 'positive_diagonal_energy_examples':examples,
 'physical_charge_scale':'OPEN q0; D charges are finite coset tags not additive integer physical electric charge',
 'physical_action_clock':'OPEN chi/tau0 and physical conjugate phase or current law',
 'conventional_null':'ordinary K4 chip-firing/discrete electric-network discriminant and finite Heisenberg representation identical',
 'independent_prediction':'NONE; positive S4-invariant energy gap and physical coupling ratios not source-selected',
 'source_limits':'integrated finite pairing, charge field, loop history and impedance audits are read-only; no physical quantum quantization rule supplied'
}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);v=a.parse_args()
    v.out.parent.mkdir(parents=True,exist_ok=True)
    v.out.write_text(json.dumps(output,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','orbits':output['S4_orbit_sizes'], 'pair_checks':output['pairing_S4_invariant_checks']},sort_keys=True))
