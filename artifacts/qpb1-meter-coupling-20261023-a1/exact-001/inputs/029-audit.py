"""Local signed samples -> exact integer overlap/phase; conditional sensor model.

All post-digitization gates and phase-direction products are exact integers.
Analytic sensor/normalization bounds are separate from floating trajectories.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import gcd
from pathlib import Path
import argparse
import cmath
import hashlib
import importlib.util
import json
import math
import random

ROOT = Path(__file__).resolve().parents[2]
sp = importlib.util.spec_from_file_location('window', ROOT/'experiments/qpb1-finite-window/audit.py')
window = importlib.util.module_from_spec(sp); sp.loader.exec_module(window)
phase, alg = window.phase, window.alg
mv, mm, dot, tr = alg.mv, alg.mm, alg.dot, alg.tr
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def channel_map():
    simp, A, J, P, edge, visible, hidden = phase.carrier()
    anchors = [i for i, s in enumerate(simp) if len(s) == 2]+[simp.index((0, 1, 2, 3))]
    T = []
    for i in anchors:
        T += [[F(j == i) for j in range(15)], J[i][:]]
    return simp, A, J, P, anchors, T


def decode(codes, anchors, A):
    if len(codes) != 15 or any(type(c) is not int for c in codes):
        raise ValueError('15 signed integer register codes required')
    result = []
    for i in anchors:
        result += [2*codes[i], sum(int(a)*c for a, c in zip(A[i], codes))]
    return result


def overlap(a, b):
    C = S = 0
    for i in range(0, 14, 2):
        q, p, u, v = a[i], a[i+1], b[i], b[i+1]
        C += q*u+p*v; S += p*u-q*v
    return C, S


def norm2(a):
    return sum(x*x for x in a)


def multiply(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def reduce_direction(z):
    d = gcd(abs(z[0]), abs(z[1]))
    if not d:
        raise ValueError('zero phase direction')
    return z[0]//d, z[1]//d


def visible(C, S, N1, N2, numerator, denominator):
    return denominator**2*(C*C+S*S) > numerator**2*N1*N2


def support_ok(a, bits):
    # Coefficient unit u=2^(1-bits); required observed norm in(4/5,6/5).
    N = norm2(a); den2 = 2**(2*bits-2)
    return 16*den2 < 25*N < 36*den2


def integer_phase(raw_snapshots, bits, anchors, A):
    """Streaming integer phase direction; accepts an iterable of129snapshots."""
    limit = 2**(bits-1)
    first = previous = None
    B = (1, 0); max_bits = 1; count = 0
    for codes in raw_snapshots:
        count += 1
        if count > 129:
            raise ValueError('certificate requires129snapshots')
        if any(c < -limit or c >= limit for c in codes):
            return {'status': 'SATURATED', 'direction': None}
        b = decode(codes, anchors, A)
        if not support_ok(b, bits):
            return {'status': 'LOW_SUPPORT', 'direction': None}
        if first is None:
            first = b
        else:
            C, S = overlap(previous, b)
            if not visible(C, S, norm2(previous), norm2(b), 999, 1000):
                return {'status': 'LOW_VISIBILITY', 'direction': None}
            B = reduce_direction(multiply(B, (C, -S)))
            max_bits = max(max_bits, abs(B[0]).bit_length(), abs(B[1]).bit_length())
        previous = b
    if count != 129:
        raise ValueError('certificate requires129snapshots')
    C, S = overlap(first, previous)
    if not visible(C, S, norm2(first), norm2(previous), 99, 100):
        return {'status': 'LOW_VISIBILITY', 'direction': None}
    B = reduce_direction(multiply((C, S), B))
    max_bits = max(max_bits, abs(B[0]).bit_length(), abs(B[1]).bit_length())
    return {'status': 'PASS', 'direction': B, 'maximum_component_bits': max_bits}


def display_phase(z):
    """Optional binary64 display only; exact output remains the integer pair."""
    shift = max(0, max(abs(z[0]).bit_length(), abs(z[1]).bit_length())-800)
    return math.atan2(float(F(z[1], 2**shift)), float(F(z[0], 2**shift)))


def quantize(values, bits):
    step = F(4, 2**bits)
    return [round(F(v)/step) for v in values]  # Exact nearest-even for supplied rationals.


def profile(bits, error_divisor):
    parent = window.budget(); smin = F(9, 10)
    raw_error = smin/error_divisor
    halfstep = F(2, 2**bits)
    a = raw_error+halfstep
    # sqrt(15)<31/8 since960<961; overlap error <=4sqrt(15)*a/smin.
    zeta = F(31, 2)*a/smin
    acq = zeta/(parent['visibility_lower']-zeta)+128*zeta/(parent['link_visibility_lower']-zeta)
    total = parent['gain_phase_error']+parent['discrete_phase_error']+acq
    return {'sensor_bits': bits, 'raw_sensor_plus_reference_error': raw_error,
            'half_quantizer_step': halfstep, 'raw_total_error': a,
            'normalized_overlap_error': zeta, 'phase_error_bound': total,
            'observed_endpoint_lower': parent['visibility_lower']-zeta,
            'observed_link_lower': parent['link_visibility_lower']-zeta,
            'strict_parent_link_budget_passes': zeta <= F(1, 1000000),
            'overall_phase_budget_passes': total < F(1, 250),
            'raw_memory_words': 45, 'raw_memory_bits': 45*bits,
            'phase_component_signed_bit_bound': 129*(2*bits+4)+1}


def main(out):
    out.mkdir(parents=True, exist_ok=True); here = Path(__file__).resolve().parent
    sources = json.loads((here/'SOURCES.json').read_text())
    for s in sources['sources']:
        assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256']
    byid = {r['id']: r for r in json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']}
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    assert all(byid[r['id']] == r for r in rows)
    simp, A, J, P, anchors, T = channel_map()
    assert mm(T, tr(T)) == alg.eye(14) and mm(tr(T), T) == P
    assert alg.rank(T) == 14 and alg.rank(T[:12]) == 12
    assert alg.rank(T[:-1]) == alg.rank(T[:12]+T[13:]) == 13
    supports = []
    for k, i in enumerate(anchors):
        assert sum(v != 0 for v in T[2*k+1]) == 4
        assert all(not v or A[i][j] != 0 for j, v in enumerate(T[2*k+1]))
        supports.append({'anchor': list(simp[i]), 'q_register': list(simp[i]),
                         'p_terms': [{'register': list(simp[j]), 'coefficient': str(v)}
                                     for j, v in enumerate(T[2*k+1]) if v]})
    # Complete matrix identities plus rational local-decoding fixtures.
    rng = random.Random(20261023)
    exact_checks = symmetry_checks = 0
    fixtures = [[rng.randint(-8, 8) for _ in range(15)] for _ in range(100)]
    for a, b in zip(fixtures, fixtures[1:]+fixtures[:1]):
        da, db = decode(a, anchors, A), decode(b, anchors, A)
        assert [F(v, 2) for v in da] == mv(T, list(map(F, a)))
        assert mv(tr(T), [F(v, 2) for v in da]) == mv(P, list(map(F, a)))
        C, S = overlap(da, db)
        pa, pb = mv(P, list(map(F, a))), mv(P, list(map(F, b)))
        assert F(C, 4) == dot(pa, pb) and F(S, 4) == dot(mv(J, pa), pb)
        assert F(norm2(da), 4) == dot(pa, pa)
        exact_checks += 1
    for perm in permutations(range(4)):
        R = phase.representation(simp, perm)
        a, b = fixtures[0], fixtures[1]
        ar, br = [int(v) for v in mv(R, a)], [int(v) for v in mv(R, b)]
        assert overlap(decode(ar, anchors, A), decode(br, anchors, A)) == overlap(decode(a, anchors, A), decode(b, anchors, A))
        symmetry_checks += 1
    # Identical complete stocks cannot recover overlap even with known reference.
    i, j = simp.index((0, 1)), simp.index((0, 2))
    plus = [F(k == i)+F(k == j) for k in range(15)]
    minus = [F(k == i)-F(k == j) for k in range(15)]
    assert [x*x for x in plus] == [x*x for x in minus]
    assert dot(plus, minus) == dot(mv(J, plus), minus) == 0
    assert dot(plus, plus) == dot(minus, minus) == 2
    strict, reallocated = profile(26, 32000000), profile(21, 8000000)
    fail_strict, fail_overall = profile(25, 32000000), profile(20, 8000000)
    assert strict['strict_parent_link_budget_passes'] and strict['phase_error_bound'] < F(1, 500)
    assert not fail_strict['strict_parent_link_budget_passes']
    assert reallocated['overall_phase_budget_passes'] and not reallocated['strict_parent_link_budget_passes']
    assert not fail_overall['overall_phase_budget_passes']
    for p in [strict, reallocated]:
        assert p['observed_endpoint_lower'] > F(99, 100) and p['observed_link_lower'] > F(999, 1000)
        assert F(11, 10)+p['raw_total_error'] < 2
        assert F(9, 10)-4*p['raw_total_error'] > F(4, 5)
        assert F(11, 10)+4*p['raw_total_error'] < F(6, 5)
    # Exact nearest-even quantizer at boundaries/ties, including negative values.
    quantizer_checks = 0
    for bits in [20, 21, 25, 26]:
        step = F(4, 2**bits)
        for n in range(-10, 11):
            for f in [F(-1, 2), F(-1, 3), F(0), F(1, 3), F(1, 2)]:
                v = (n+f)*step; q = quantize([v], bits)[0]
                assert abs(q*step-v) <= step/2
                quantizer_checks += 1
    # Integer strict visibility comparisons exercise exact equality rejection.
    assert not visible(99, 0, 100, 100, 99, 100)
    assert not visible(999, 0, 1000, 1000, 999, 1000)
    # Binary64 trajectory generation; integer acquisition pipeline exact thereafter.
    jf = [[float(v) for v in row] for row in J]
    kblocks = [alg.zero(15) for _ in range(3)]
    for ii, s in enumerate(simp):
        for jj, t in enumerate(simp):
            if len(t) == len(s)+1 and A[ii][jj]:
                kblocks[len(t)-2][ii][jj] = A[ii][jj]; kblocks[len(t)-2][jj][ii] = -A[ii][jj]
    sectors = [alg.scale(mm(k, k), F(-1, 4)) for k in kblocks]
    pf = [[[float(v) for v in row] for row in p] for p in sectors]
    mf = lambda m, x: [sum(a*v for a, v in zip(row, x)) for row in m]
    df = lambda x, y: sum(a*v for a, v in zip(x, y))
    u = [float(k == i) for k in range(15)]
    top = [float(s == (0, 1, 2, 3)) for s in simp]
    ref = [(a+b)/math.sqrt(2) for a, b in zip(u, top)]
    frame = T; preparations = [ref]
    for f in frame:
        preparations += [[a+sign*.1*float(v) for a, v in zip(ref, f)] for sign in [-1, 1]]
    numerical = []; witness = None
    for p in [strict, reallocated]:
        bits = p['sensor_bits']; sensor = float(p['raw_sensor_plus_reference_error'])
        for prep_id, x in enumerate(preparations):
            for trial in range(4):
                comp = [mf(pp, x) for pp in pf]; jc = [mf(jf, xx) for xx in comp]
                a = df(x, x); weights = [df(x, xx)/a for xx in comp]
                Tactual = 2*math.pi+[-.01, 0., .01, .01][trial]
                angles = [0.]*3; states = []
                for step in range(129):
                    if step:
                        gains = [base+.01*[-1, 0, 1][(step*(k+1)+trial+k) % 3]
                                 for k, base in enumerate([1., 1., 1.5])]
                        angles = [t+2*g*Tactual/128 for t, g in zip(angles, gains)]
                    states.append([sum(math.cos(t)*v[z]+math.sin(t)*jv[z]
                                       for t, v, jv in zip(angles, comp, jc)) for z in range(15)])
                codes = []
                for step, state in enumerate(states):
                    noisy = [v+sensor*[-1, 1][(step+z+trial) % 2] for z, v in enumerate(state)]
                    codes.append(quantize(noisy, bits))
                output = integer_phase(codes, bits, anchors, A)
                assert output['status'] == 'PASS'
                angle = display_phase(output['direction'])
                baseline = -2*math.pi*weights[2]
                error = abs(cmath.phase(cmath.exp(1j*(angle-baseline))))
                assert error < float(p['phase_error_bound'])+5e-11
                assert abs(cmath.exp(1j*angle)-1) > 1.7
                assert output['maximum_component_bits'] < p['phase_component_signed_bit_bound']
                numerical.append({'bits': bits, 'preparation': prep_id, 'profile': trial,
                                  'phase_error_display_rad': error,
                                  'maximum_component_bits': output['maximum_component_bits']})
                if witness is None or error > witness['phase_error_display_rad']:
                    witness = {**numerical[-1], 'raw_snapshot_codes': codes,
                               'exact_phase_direction': list(output['direction'])}
    # Deterministic qualification failures.
    bits = 26; test = quantize(ref, bits)
    assert integer_phase([[0]*15]*129, bits, anchors, A)['status'] == 'LOW_SUPPORT'
    bad = [test[:] for _ in range(129)]; bad[0][0] = 2**(bits-1)
    assert integer_phase(bad, bits, anchors, A)['status'] == 'SATURATED'
    orthogonal = [v/math.sqrt(2) for v in minus]
    bad = [quantize([v/math.sqrt(2) for v in plus], bits) for _ in range(128)]
    bad.append(quantize(orthogonal, bits))
    assert integer_phase(iter(bad), bits, anchors, A)['status'] == 'LOW_VISIBILITY'
    replay = integer_phase(iter(witness['raw_snapshot_codes']), witness['bits'], anchors, A)
    assert list(replay['direction']) == witness['exact_phase_direction']
    save(out/'channels.json', {'evidence': 'EXACT', 'rank': 14, 'edge_only_rank': 12,
         'one_hidden_channel_omitted_rank': 13, 'T_Ttranspose': 'I14', 'Ttranspose_T': 'P',
         'local_channels': supports, 'coefficient_order': 'q01,p01,...,q23,p23,q_top,p_top',
         'normalization': 'sum(q^2+p^2)=||P x||^2; harmonic support separate',
         'overlap': 'C=sum(q u+p v);S=sum(p u-q v); divide by active norms'})
    profiles = {}
    for label, p in [('STRICT_A', strict), ('REALLOCATED_B', reallocated),
                     ('STRICT_25_INSUFFICIENT_BOUND', fail_strict), ('REALLOCATED_20_INSUFFICIENT_BOUND', fail_overall)]:
        profiles[label] = {k: (str(v) if isinstance(v, F) else v) for k, v in p.items()}
    save(out/'precision.json', {'evidence': 'EXACT_CONDITIONAL', 'range': '[-2,2)',
         'profiles': profiles, 'sensor_memory_model': 'Signed simultaneous calibrated raw register values;bit-exact digital reference storage;optional bounded decoded-memory errors included in raw prequantization budget',
         'insufficient_bound_meaning': 'Conservative certificate fails, not a universal impossibility theorem',
         'physical_sensor_accuracy': 'NOT_MEASURED', 'physical_score': 'UNSCORED', 'physical_promotion': 0})
    save(out/'integer_witness.json', witness)
    save(out/'numerical.json', {'evidence': 'NUMERICAL_CONSTRUCTOR_SOURCE_AND_DISPLAY',
         'cases': len(numerical), 'arithmetic_after_digitization': 'EXACT_INTEGER',
         'source': 'Binary64 synthetic trajectories and imposed bounded sensor errors; not interval or empirical validation',
         'maximum_display_phase_error': max(x['phase_error_display_rad'] for x in numerical),
         'representative_cases': numerical[:4]+numerical[-4:]})
    summary = {'status': 'PASS', 'source_hashes': len(sources['sources']), 'selected_rows': len(rows),
               'channel_rank': 14, 'edge_only_rank': 12, 'local_quadratures': 7,
               'exact_decode_overlap_fixtures': exact_checks, 'S4_checks': symmetry_checks,
               'exact_quantizer_fixtures': quantizer_checks, 'integer_windows': len(numerical),
               'exact_integer_witness_replay': 'PASS', 'negative_controls': ['LOW_SUPPORT', 'SATURATED', 'LOW_VISIBILITY'],
               'strict_sensor_bits': 26, 'reallocated_sensor_bits': 21,
               'strict_phase_bound_rad': '<1/500', 'reallocated_phase_bound_rad': '<1/250',
               'physical_sensor_accuracy': 'NOT_MEASURED', 'physical_score': 'UNSCORED', 'physical_promotion': 0}
    save(out/'summary.json', summary); print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
