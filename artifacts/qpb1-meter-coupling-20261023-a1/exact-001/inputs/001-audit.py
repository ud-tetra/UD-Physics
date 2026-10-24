"""Balanced classical local meter: exact identities/bounds, numerical sources.

No physical instrument, quantum copying law, or empirical tolerance imported.
Post-digitization phase processing uses the previous exact integer decoder.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import cmath
import hashlib
import importlib.util
import json
import math
import random

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('acq', ROOT/'experiments/qpb1-overlap-acquisition/audit.py')
acq = importlib.util.module_from_spec(spec); spec.loader.exec_module(acq)
alg, phase, window = acq.alg, acq.phase, acq.window
mm, mv, tr, dot = alg.mm, alg.mv, alg.tr, alg.dot
add, scale = alg.add, alg.scale
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def carrier():
    simp, A, J, P, anchors, T = acq.channel_map()
    K = [alg.zero(15) for _ in range(3)]
    for i, s in enumerate(simp):
        for j, t in enumerate(simp):
            if len(t) == len(s)+1 and A[i][j]:
                K[len(t)-2][i][j] = A[i][j]
                K[len(t)-2][j][i] = -A[i][j]
    sectors = [scale(mm(k, k), F(-1, 4)) for k in K]
    return simp, A, J, P, anchors, T, K, sectors


def combine(coeffs, mats):
    return [[sum(c*m[i][j] for c, m in zip(coeffs, mats)) for j in range(15)] for i in range(15)]


def meter_matrix(G, E, coupling, damping):
    """x'=Gx-Km, m'=(G+E)m+Kx-Dm; K,D diagonal15vectors."""
    L = alg.zero(30)
    for i in range(15):
        for j in range(15):
            L[i][j] = G[i][j]; L[15+i][15+j] = G[i][j]+E[i][j]
        L[i][15+i] = -coupling[i]; L[15+i][i] = coupling[i]
        L[15+i][15+i] -= damping[i]
    return L


def limits(bits, divisor):
    parent = acq.profile(bits, divisor)
    r = parent['raw_sensor_plus_reference_error']; H = 1+window.budget()['time_upper']
    smax = F(11, 10)
    initial_meter = r/40
    actual_norm = smax+initial_meter
    delta = r/(40*H*smax)
    gain = r/(40*actual_norm)
    jitter = r/(40*actual_norm*(1+gain)*5)
    answer = {'bits': bits, 'combined_raw_budget': r, 'H': H,
              'delta_operator': delta, 'meter_gain_error_per_sector': delta/6,
              'relative_port_error': 4*delta/3, 'relative_damping_error': delta/3,
              'relative_readout_gain_error': gain, 'native_channel_jitter': jitter,
              'initial_meter_norm': initial_meter, 'reset_native_duration': 64,
              'reset_port_leak_upper': initial_meter/(4*smax),
              'actual_combined_norm_upper': actual_norm,
              'calibrated_additive_noise': r/5, 'inverse_nominal_meter_gain_upper': F(8),
              'phase_bound_rad': parent['phase_error_bound'],
              'strict_parent_link_budget_passes': parent['strict_parent_link_budget_passes']}
    assert 2*(delta/6)+F(1, 4)*(4*delta/3)+delta/3 == delta
    assert F(151, 50)+2*delta/6+F(1, 4)*(1+4*delta/3)+(1+delta/3) < 5
    pieces = [8*initial_meter, 8*H*smax*delta, 8*actual_norm*gain,
              8*actual_norm*(1+gain)*5*jitter, r/5]
    assert pieces == [r/5]*5 and sum(pieces) == r
    assert smax/F(2**32)+2*answer['reset_port_leak_upper']*smax < initial_meter
    answer['five_raw_error_contributions'] = pieces
    return answer


def scalar_transfer(t, kappa=.25, gamma=1., omega=0.):
    """Exact formula evaluated in binary64 for constant scalar parameters."""
    d = complex(-gamma, omega)
    root = cmath.sqrt(d*d/4-kappa*kappa)
    sinc = cmath.sinh(root*t)/root if root else t
    pref = cmath.exp(d*t/2)
    return pref*(cmath.cosh(root*t)-d*sinc/2), pref*kappa*sinc


def nominal_b(t):
    return scalar_transfer(t)[1].real


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    sources = json.loads((here/'SOURCES.json').read_text())['sources']
    assert all(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256'] for s in sources)
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    byid = {r['id']: r for r in json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']}
    assert all(byid[r['id']] == r for r in rows)
    simp, A, J, P, anchors, T, K, sectors = carrier()
    G = combine([F(1), F(1), F(3, 2)], K)
    L = meter_matrix(G, alg.zero(15), [F(1, 4)]*15, [F(1)]*15)
    loss = alg.zero(30)
    for i in range(15, 30): loss[i][i] = -2
    assert add(L, tr(L)) == loss
    assert alg.rank([[P[i % 15][j % 15] if (i < 15) == (j < 15) else F(0)
                      for j in range(30)] for i in range(30)]) == 28
    assert sum(L[i][j] != 0 for i in range(30) for j in range(i+1, 30)) == 71
    # Polynomial intertwining identity, with independent coefficient fixtures.
    intertwining = 0
    for a, b in [(F(1), F(0)), (F(0), F(1)), (F(2, 3), F(-3, 7))]:
        R = [[(a if i < 15 else b)*F(i % 15 == j) for j in range(15)] for i in range(30)]
        Rp = [[(-b/4 if i < 15 else a/4-b)*F(i % 15 == j) for j in range(15)] for i in range(30)]
        assert mm(L, R) == add(mm(R, G), Rp)
        intertwining += 1
    # Common J detuning remains a complex scalar response on every active plane.
    E = scale(J, F(2, 5)); Lc = meter_matrix(G, E, [F(1, 4)]*15, [F(1)]*15)
    ar, ai, br, bi = F(2, 3), F(-1, 5), F(3, 7), F(1, 9)
    real_map = lambda a, b: add(scale(P, a), scale(J, b))
    R = real_map(ar, ai)+real_map(br, bi)
    Rp = real_map(-br/4, -bi/4)+real_map(ar/4-br-F(2, 5)*bi, ai/4-bi+F(2, 5)*br)
    assert mm(Lc, R) == add(mm(R, G), Rp)
    # Nonuniform but balanced local ports retain passivity.
    c = [F(1, 4)*(1+F((i % 3)-1, 100)) for i in range(15)]
    d = [1+F((i % 5)-2, 100) for i in range(15)]
    Ln = meter_matrix(G, combine([F(1, 100), F(-1, 100), F(0)], K), c, d)
    lossn = alg.zero(30)
    for i in range(15): lossn[15+i][15+i] = -2*d[i]
    assert add(Ln, tr(Ln)) == lossn
    symmetry = 0
    for perm in permutations(range(4)):
        R = phase.representation(simp, perm)
        assert mm(R, G) == mm(G, R)
        symmetry += 1  # Scalar port/damping blocks commute with every R.
    # Generic rational polygon: independent complex gains cancel to a positive scale.
    rng = random.Random(20261023); gauge_checks = 0
    for _ in range(50):
        states = [mv(P, [F(rng.randint(-3, 3), 5) for _ in range(15)]) for _ in range(5)]
        beta = [(F(rng.randint(1, 4), 3), F(rng.randint(-3, 3), 5)) for _ in states]
        changed = [[a*x+b*y for x, y in zip(v, mv(J, v))] for v, (a, b) in zip(states, beta)]
        def polygon(vs):
            coeff = [mv(T, v) for v in vs]
            B = acq.overlap(coeff[0], coeff[-1])
            for x, y in zip(coeff, coeff[1:]):
                C, S = acq.overlap(x, y); B = acq.multiply(B, (C, -S))
            return B
        B, C = polygon(states), polygon(changed)
        positive = math.prod(a*a+b*b for a, b in beta)
        assert C == (positive*B[0], positive*B[1]) and positive > 0
        gauge_checks += 1
    # Uniform nominal meter response >1/8 throughout tau in[1,H].
    H = 1+window.budget()['time_upper']
    endpoint1 = F(55, 384)
    exp_taylor = 1-F(5, 8)+F(5, 8)**2/2-F(5, 8)**3/6
    endpointH = F(1, 4)*exp_taylor*F(127, 128)
    assert 7 < H < F(15, 2) and exp_taylor == F(1627, 3072)
    assert min(endpoint1, endpointH) > F(1, 8)
    profiles = [limits(26, 32000000), limits(21, 8000000)]
    assert profiles[0]['phase_bound_rad'] < F(1, 500)
    assert profiles[1]['phase_bound_rad'] < F(1, 250)
    # Binary64 synthetic closed solutions with sector-dependent meter errors.
    mf = lambda m, x: [sum(float(a)*v for a, v in zip(row, x)) for row in m]
    df = lambda x, y: sum(a*b for a, b in zip(x, y))
    i = simp.index((0, 1)); itop = simp.index((0, 1, 2, 3))
    ref = [(float(z == i)+float(z == itop))/math.sqrt(2) for z in range(15)]
    preparations = [ref]
    for target in [i, itop]:
        preparations += [[v+sign*.1*float(z == target) for z, v in enumerate(ref)] for sign in [-1, 1]]
    results = []; witness = None
    for p in profiles:
        bits = p['bits']; gain = float(p['relative_readout_gain_error']); jitter = float(p['native_channel_jitter'])
        eta = float(p['meter_gain_error_per_sector']); ec = float(p['relative_port_error']); ed = float(p['relative_damping_error'])
        noise = float(p['calibrated_additive_noise'])
        initial_meter = float(p['initial_meter_norm'])
        for prep, seed in enumerate(preparations):
            comp = [mf(pp, seed) for pp in sectors]; jc = [mf(J, v) for v in comp]
            support = df(seed, seed); weights = [df(seed, v)/support for v in comp]
            for gi, gains in enumerate([(1., 1., 1.5), (.99, 1.01, 1.49), (1.01, .99, 1.51)]):
                for trial in range(4):
                    sign = [0, 1, -1, 1][trial]
                    detuning = [sign*eta*((-1)**(k+trial)) for k in range(3)]
                    kap, gam = .25*(1+sign*ec), 1+sign*ed
                    residual = [sign*initial_meter*float(q == itop) for q in range(15)]
                    rc = [mf(pp, residual) for pp in sectors]; jr = [mf(J, v) for v in rc]
                    actualT = 2*math.pi+[-.01, 0., .01, .01][trial]
                    def state(t, meter=True):
                        ans = [0.]*15
                        for k in range(3):
                            aa, bb = scalar_transfer(t, kap, gam, 2*detuning[k])
                            z = (bb if meter else 1)*cmath.exp(2j*gains[k]*t)
                            for q in range(15): ans[q] += z.real*comp[k][q]+z.imag*jc[k][q]
                            if meter:
                                zz = (aa+complex(-gam, 2*detuning[k])*bb/kap)*cmath.exp(2j*gains[k]*t)
                                for q in range(15): ans[q] += zz.real*rc[k][q]+zz.imag*jr[k][q]
                        return ans
                    codes = []; max_raw = 0.
                    for step in range(129):
                        tau = 1+actualT*step/128; b0 = nominal_b(tau)
                        ideal = state(tau, False)
                        if sign:
                            early, late = state(tau-jitter), state(tau+jitter)
                            observed = [(1+gain*(-1)**(q+trial))*(early if q % 2 else late)[q]/b0+noise*(-1)**(step+q+trial) for q in range(15)]
                        else:
                            observed = [v/b0 for v in state(tau)]
                        err = max(abs(a-b) for a, b in zip(observed, ideal)); max_raw = max(max_raw, err)
                        assert err <= float(p['combined_raw_budget'])+5e-13
                        codes.append(acq.quantize(observed, bits))
                    result = acq.integer_phase(iter(codes), bits, anchors, A)
                    assert result['status'] == 'PASS'
                    angle = acq.display_phase(result['direction'])
                    phase_error = abs(cmath.phase(cmath.exp(1j*(angle+2*math.pi*weights[2]))))
                    assert phase_error < float(p['phase_bound_rad'])+5e-11
                    assert abs(cmath.exp(1j*angle)-1) > 1.7
                    row = {'bits': bits, 'preparation': prep, 'gains': gi, 'error_profile': trial,
                           'max_calibrated_raw_error': max_raw, 'phase_error_rad': phase_error}
                    results.append(row)
                    if witness is None or phase_error > witness['phase_error_rad']:
                        witness = {**row, 'raw_snapshot_codes': codes, 'exact_phase_direction': list(result['direction'])}
    # Separate full30-state RK4 implementation cross-checks the scalar solution.
    edges = [(i, j, float(L[i][j])) for i in range(30) for j in range(30) if L[i][j]]
    def rhs(z):
        ans = [0.]*30
        for i, j, v in edges: ans[i] += v*z[j]
        return ans
    def rk4(z, h):
        a = rhs(z); b = rhs([x+h*v/2 for x, v in zip(z, a)])
        c = rhs([x+h*v/2 for x, v in zip(z, b)]); d = rhs([x+h*v for x, v in zip(z, c)])
        return [x+h*(v+2*w+2*y+zz)/6 for x, v, w, y, zz in zip(z, a, b, c, d)]
    rk_records = []
    for steps in [2048, 4096]:
        z = ref+[0.]*15; duration = 3.; h = duration/steps
        for _ in range(steps): z = rk4(z, h)
        aa, bb = scalar_transfer(duration)
        comp = [mf(pp, ref) for pp in sectors]; jc = [mf(J, v) for v in comp]
        u = [sum(math.cos(2*g*duration)*v[q]+math.sin(2*g*duration)*jv[q] for g, v, jv in zip([1, 1, 1.5], comp, jc)) for q in range(15)]
        exact_display = [aa.real*v for v in u]+[bb.real*v for v in u]
        error = max(abs(a-b) for a, b in zip(z, exact_display))
        assert error < 2e-10
        assert sum(v*v for v in z) < sum(v*v for v in ref)
        rk_records.append({'steps': steps, 'maximum_coordinate_error': error})
    # Real meter cancellation fails when a differential sector has another rate.
    failure = []
    for eps in [0., .01, .05]:
        snapshots = [[scalar_transfer(tau, omega=2*eps*(k == 2))[1]*cmath.exp(2j*g*tau)
                      for k, g in enumerate([1., 1., 1.5])]
                     for tau in [1+2*math.pi*j/128 for j in range(129)]]
        m0, m1 = snapshots[0], snapshots[-1]
        endpoint = sum(w*z.conjugate()*v for w, z, v in zip([.25, .25, .5], m0, m1))
        denom = math.sqrt(sum(w*abs(z)**2 for w, z in zip([.25, .25, .5], m0))*sum(w*abs(z)**2 for w, z in zip([.25, .25, .5], m1)))
        q = endpoint/abs(endpoint)
        for x, y in zip(snapshots, snapshots[1:]):
            link = sum(w*z.conjugate()*v for w, z, v in zip([.25, .25, .5], x, y))
            q *= (link/abs(link)).conjugate()
        failure.append({'hidden_meter_gain_error': eps, 'endpoint_visibility': abs(endpoint)/denom,
                        'phase_difference_from_matched_rad': abs(cmath.phase(-q))})
    assert failure[0]['endpoint_visibility'] > 1-1e-14 and failure[1]['endpoint_visibility'] < 1-1e-7
    assert failure[1]['phase_difference_from_matched_rad'] > 1e-6
    assert failure[1]['phase_difference_from_matched_rad'] < .004
    assert failure[2]['phase_difference_from_matched_rad'] > .004
    assert nominal_b(0.) == 0.  # Reset meter supplies no instantaneous initial phase.
    replay = acq.integer_phase(iter(witness['raw_snapshot_codes']), witness['bits'], anchors, A)
    assert list(replay['direction']) == witness['exact_phase_direction']
    def serial(x):
        if isinstance(x, F): return str(x)
        if isinstance(x, dict): return {k: serial(v) for k, v in x.items()}
        if isinstance(x, list): return [serial(v) for v in x]
        return x
    save(out/'model.json', {'evidence': 'EXACT_CONDITIONAL', 'state_dimension': 30, 'active_dimension': 28,
         'undirected_offdiagonal_pairs': 71, 'intercarrier_ports': 15,
         'law': "x'=Gx-kappa*m;m'=Gm+kappa*x-gamma*m", 'energy_balance': "d(||x||^2+||m||^2)/2ds=-gamma||m||^2",
         'matched_factorization': 'x=a(s)U(s)seed;m=b(s)U(s)seed',
         'common_J_detuning': 'x=complex_scalar_a*U*seed;m=complex_scalar_b*U*seed; same projective ray when nonzero',
         'finite_window_nominal_meter_lower': '>1/8 on tau[1,5107/700]',
         'lower_endpoint_proof': [str(endpoint1), str(endpointH)],
         'meter_copying': 'Attenuated classical storage transfer; no physical quantum copying or unloaded unit-gain duplicate'})
    save(out/'tolerances.json', serial({'evidence': 'EXACT_CONDITIONAL', 'profiles': profiles,
         'operator_bound': 'delta<=2eps_g+(1/4)eps_c+eps_d',
         'raw_error_bound': '8e0+8H*smax*delta+8S*eps_a+8S*(1+eps_a)*5*j+nu;S=smax+e0',
         'scope': 'Conservative sufficient bound; no optimality or necessity; known nominal scalar calibration and bound on unmodeled meter load assumed',
         'physical_accuracy': 'NOT_MEASURED', 'physical_promotion': 0}))
    save(out/'numerical.json', {'evidence': 'NUMERICAL_CONSTRUCTOR', 'cases': len(results),
         'max_phase_error_rad': max(r['phase_error_rad'] for r in results),
         'max_calibrated_raw_error': max(r['max_calibrated_raw_error'] for r in results),
         'binary64_source_and_display_only': True, 'post_digitization': 'EXACT_INTEGER',
         'representative_cases': results[:4]+results[-4:], 'full30_RK4_cross_check': rk_records,
         'differential_hidden_rate_control': failure})
    save(out/'integer_witness.json', witness)
    summary = {'status': 'PASS', 'source_hashes': len(sources), 'literal_rows': len(rows),
               'state_dimension': 30, 'active_dimension': 28, 'local_ports': 15,
               'intertwining_fixtures': intertwining, 'common_complex_intertwining': 'PASS',
               'S4_actions': symmetry, 'exact_gauge_polygons': gauge_checks,
               'integer_windows': len(results), 'integer_witness_replay': 'PASS',
               'negative_controls': ['reset_zero_meter_unobservable', 'differential_hidden_detuning_breaks_exact_cancellation', 'out_of_budget_hidden_detuning_exceeds_phase_screen'],
               'full30_RK4_cross_checks': len(rk_records), 'nominal_meter_lower': '>1/8',
               'strict_phase_bound': '<1/500rad', 'amended_phase_bound': '<1/250rad',
               'physical_score': 'UNSCORED', 'physical_promotion': 0}
    save(out/'summary.json', summary); print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
