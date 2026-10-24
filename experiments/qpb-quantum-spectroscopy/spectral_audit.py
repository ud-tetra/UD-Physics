#!/usr/bin/env python3
"""UD C7 direct-map level obstruction versus a conventional quantum transmon.

CONDITIONAL exact source algebra and separate illustrative NumPy charge-basis
truncation. Never equate the two Hilbert spaces or treat numerical rows as data.
"""
import argparse
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path


def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def tr(a):
    return [list(c) for c in zip(*a)]


def mul(a, b):
    bt = tr(b)
    return [[sum((x*y for x, y in zip(row, c)), F(0)) for c in bt]
            for row in a]


def rank(a):
    a = [list(row) for row in a]
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        i = next((i for i in range(r, m) if a[i][c]), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        p = a[r][c]
        a[r] = [v / p for v in a[r]]
        for j in range(r + 1, m):
            if a[j][c]:
                z = a[j][c]
                a[j] = [u - z*v for u, v in zip(a[j], a[r])]
        r += 1
        if r == m:
            break
    return r


simplices = [s for k in range(1, 5) for s in combinations(range(4), k)]
idx = {s:i for i, s in enumerate(simplices)}
D = [zero(15) for _ in range(3)]
for s in simplices:
    if len(s) > 1:
        for k in range(len(s)):
            D[len(s)-2][idx[s[:k]+s[k+1:]]][idx[s]] = F((-1)**k)
K = [[[d[i][j]-d[j][i] for j in range(15)] for i in range(15)] for d in D]
P = [[[-v/F(4) for v in row] for row in mul(k, k)] for k in K]
pranks = [rank(p) for p in P]
assert pranks == [6, 6, 2]
assert all(mul(P[i], P[j]) == zero(15) for i in range(3)
           for j in range(3) if i != j)
assert all(mul(p, p) == p for p in P)

# i=-J maps the native positive generator to H/hbar in physical time,
# conditional on an external physical action chi and clock tau0.
complex_multiplicities = [r//2 for r in pranks]
assert complex_multiplicities == [3, 3, 1]

def native_levels(g):
    return sorted([2*g[i] for i, m in enumerate(complex_multiplicities)
                   for _ in range(m)])

reference = native_levels((F(1), F(1), F(3, 2)))
generic = native_levels((F(1), F(5, 4), F(3, 2)))
assert reference == [F(2)]*6 + [F(3)]
assert len(set(reference)) == 2 and len(set(generic)) == 3
# Distinct f0j can never exceed #distinct eigenvalues-1 at any fixed g.

# A finite-dimensional exact canonical commutation relation fails by trace.
# A seven-charge cyclic shift also has an exact nonzero wrap-boundary defect.
N = 7
clock_numbers = list(range(-3, 4))
charge = zero(N)
shift = zero(N)
for k, n in enumerate(clock_numbers):
    charge[k][k] = F(n)
    shift[(k+1) % N][k] = F(1)
comm = mul(charge, shift)
back = mul(shift, charge)
comm = [[comm[i][j] - back[i][j] - shift[i][j]
         for j in range(N)] for i in range(N)]
assert sum(bool(v) for row in comm for v in row) == 1
assert comm[0][6] == -7
assert all((comm[i][j] == 0) for i in range(N) for j in range(N)
           if (i, j) != (0, 6))

# Separate conventional rotor quantum model, with independently ADDED
# infinite charge basis and externally given action scale. These are
# illustrative values only and not a comparison to measured spectra.
import numpy as np

def transmon(cutoff, EC_GHz=0.242, EJ1_GHz=15.0, EJ2_GHz=0.15):
    ns = np.arange(-cutoff, cutoff+1, dtype=float)
    h = np.diag(4*EC_GHz*ns**2)
    for j, ej in ((1,EJ1_GHz),(2,EJ2_GHz)):
        for k in range(len(ns)-j):
            h[k,k+j] -= ej/2
            h[k+j,k] -= ej/2
    e = np.linalg.eigvalsh(h)
    return [float(v-e[0]) for v in e[:7]]

models = {}
for harmonic in (False, True):
    key = 'conventional_harmonic_1pct' if harmonic else 'conventional_sine_only'
    e2 = 0.15 if harmonic else 0.0
    a, b = transmon(12, EJ2_GHz=e2), transmon(16, EJ2_GHz=e2)
    assert max(abs(x-y) for x,y in zip(a,b)) < 1e-7
    assert all(b[i] < b[i+1] for i in range(6))
    models[key] = {'f_0j_GHz_ILLUSTRATIVE_NOT_MEASURED': b,
                   'cutoff_12_vs_16_max_GHz': max(abs(x-y) for x,y in zip(a,b))}

result = {
 'status':'PASS', 'labels':['EXACT','CONDITIONAL','NUMERICAL','FAILED','OPEN'],
 'UD_source':'integrated qpb1-local-generators and qpb1-carrier-anchor at revision b4d2a9f15cda3b7d493a14bdba1d3f63604256d3',
 'carrier':'R15 harmonic real line plus real active rank14, with complex i=-J giving C7',
 'projector_real_ranks':pranks,
 'projector_complex_multiplicities':complex_multiplicities,
 'direct_quantum_dictionary':'ASSUMED: t_physical=tau0*s; i=-J; H_eff=(2*chi/tau0)*sum_k(g_k*Pi_k), external chi>0 action scale',
 'direct_reference_levels_in_energy_unit_2chi_over_tau0':['1']*6+['3/2'],
 'direct_reference_levels_in_unit_chi_over_tau0':[str(x) for x in reference],
 'distinct_native_reference_energies':len(set(reference)),
 'distinct_native_generic_energies_max':len(set(generic)),
 'max_distinct_nonzero_f0j_reference':len(set(reference))-1,
 'max_distinct_nonzero_f0j_any_three_gains':len(set(generic))-1,
 'finite_charge_rotor_defect':'for N=7 cyclic S, [Ncharge,S]-S=-7|-3><+3| (rank one); cannot get exact rotor shift without boundary',
 'finite_CCR_obstruction':'trace([Q,P])=0 versus trace(i*chi*I7)=7*i*chi !=0 for chi>0; exact canonical CCR requires new infinite degrees/domain',
 'published_physical_observables':'Willsch et al Nature Physics 2024 reports f0j j=1..6 and resonator shifts; standard rotor charge basis |n>, n in Z, with 4EC(n-ng)^2 - sum E_Jm cos(m phi) plus resonator',
 'conventional_design_parameters':{'EC_over_h_GHz':0.242,'EJ1_over_h_GHz':15.0,'EJ2_over_h_GHz_harmonic':0.15,'offset_charge':0,'physical_data_used':False},
 'conventional_illustrative_models':models,
 'source_data_status':'Measured f0j paper available, but Juelich raw spectroscopy/model files not acquired (external GitLab access challenge); no numerical held-out residuals',
 'failed_identification':'Direct fixed three-sector C7 Hamiltonian has at most 3 distinct energies, not 7 individually resolved transmon levels; no choice of gains, chi, tau0 changes this.',
 'not_a_universal_no_go':'Arbitrary Hermitian 7x7 matrices, nonlinear quantization, Fock/rotor extension, new ports and Hilbert spaces are different hypotheses with additional free choices.',
 'required_extra_inputs':['native quantum Hilbert/charge translation operator','source-selected physical chi and tau0','constitutive E_C and E_Jm or analogous dynamics','transmon/resonator coupling and measured readout','data access and heldout protocol'],
 'review':'Same assistant constructor; raw spectroscopy NOT_ACQUIRED; independent mathematical review NOT_RUN; experimental UD bridge NOT_EXECUTED'
}

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out',required=True,type=Path)
    args=ap.parse_args()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','ranks':pranks,'complex_multiplicities':complex_multiplicities,
                      'charge_boundary_defect':-7, 'models':list(models)},sort_keys=True))
