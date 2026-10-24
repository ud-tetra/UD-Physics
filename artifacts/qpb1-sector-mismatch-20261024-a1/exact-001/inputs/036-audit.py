"""Projective polygon variation: exact certificates and numerical constructors."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import cmath
import hashlib
import importlib.util
import json
import math
import random

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('meter', ROOT/'experiments/qpb1-meter-coupling/audit.py')
meter = importlib.util.module_from_spec(spec); spec.loader.exec_module(meter)
acq, window, alg = meter.acq, meter.window, meter.alg
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def J(v):
    return [a for q, p in zip(v[::2], v[1::2]) for a in (p, -q)]


def h(v, w):
    return acq.overlap(v, w)


def vadd(v, w):
    return [a+b for a, b in zip(v, w)]


def vsub(v, w):
    return [a-b for a, b in zip(v, w)]


def vscale(a, v):
    return [a*b for b in v]


def zdiv(v, z):
    a, b = z; den = a*a+b*b
    return [F(a*x-b*y, den) for x, y in zip(v, J(v))]


def imratio(z, w):
    a, b = z; c, d = w
    return F(b*c-a*d, c*c+d*d)


def variation(vs, ws):
    def edge(i, j):
        return imratio(tuple(a+b for a, b in zip(h(ws[i], vs[j]), h(vs[i], ws[j]))), h(vs[i], vs[j]))
    return edge(0, len(vs)-1)-sum(edge(j, j+1) for j in range(len(vs)-1))


def gradients(vs):
    z = [h(a, b) for a, b in zip(vs, vs[1:])]; end = h(vs[0], vs[-1])
    ans = [vsub(zdiv(vs[1], z[0]), zdiv(vs[-1], end))]
    for j in range(1, len(vs)-1):
        ans.append(vsub(zdiv(vs[j+1], z[j]), zdiv(vs[j-1], (z[j-1][0], -z[j-1][1]))))
    ans.append(vsub(zdiv(vs[0], (end[0], -end[1])), zdiv(vs[-2], (z[-1][0], -z[-1][1]))))
    return ans


def q_upper(visibility, c):
    # sqrt(x)<=(x+c^2)/(2c), c>0, applied to sqrt(1-v^2)/v.
    return (1-visibility*visibility+c*c)/(2*c*visibility)


def certificate(bits, divisor, delta):
    parent = window.budget(); old = meter.limits(bits, divisor)
    H = old['H']; smin, smax = F(9, 10), F(11, 10)
    common = F(13, 4000)
    common_signal = F(1, 8)-H*common
    assert common_signal > F(1, 10)
    B = 10*(old['initial_meter_norm']+H*delta*smax)
    chi = B/(smin-B)
    endpoint = parent['visibility_lower']-4*B/smin
    link = parent['link_visibility_lower']-4*B/smin
    assert 0 < link < 1 and 0 < endpoint < 1
    qe, ql = q_upper(endpoint, F(3, 20)), q_upper(link, F(1, 25))
    polygon = 2*chi*(qe+128*ql)
    sensor = old['combined_raw_budget']; halfstep = F(2, 2**bits)
    zeta = F(31, 2)*(sensor+halfstep)/(smin-B)
    acquisition = zeta/(endpoint-zeta)+128*zeta/(link-zeta)
    total = parent['gain_phase_error']+parent['discrete_phase_error']+polygon+acquisition
    model_overlap_error = 4*B/smin
    independent_model = model_overlap_error/(parent['visibility_lower']-model_overlap_error)+128*model_overlap_error/(parent['link_visibility_lower']-model_overlap_error)
    independent_total = parent['gain_phase_error']+parent['discrete_phase_error']+independent_model+acquisition
    assert total < F(1, 250)
    assert endpoint-zeta > F(99, 100) and link-zeta > F(999, 1000)
    assert smin-B-4*(sensor+halfstep) > F(4, 5)
    assert smax+B+4*(sensor+halfstep) < F(6, 5)
    assert smax+B+sensor+halfstep < 2
    assert F(173, 100)-total > F(17, 10)
    S = smax+old['initial_meter_norm']
    eps_gain = sensor/(30*S)
    jitter = sensor/(150*S*(1+eps_gain))
    assert 10*S*eps_gain+50*S*(1+eps_gain)*jitter+sensor/3 == sensor
    assert F(151, 50)+F(2, 1000)+2*delta/6+F(1001, 4000)+4*delta/3+F(1001, 1000)+delta/3 < 5
    return {'bits': bits, 'delta_differential': delta, 'old_operator_bound': old['delta_operator'],
            'operator_bound_ratio': delta/old['delta_operator'], 'H': H,
            'common_reference_operator_difference': common,
            'common_meter_signal_lower': common_signal, 'initial_meter_norm': old['initial_meter_norm'],
            'calibrated_model_error_B': B, 'homotopy_speed': chi,
            'endpoint_homotopy_floor': endpoint, 'link_homotopy_floor': link,
            'endpoint_gradient_q_upper': qe, 'link_gradient_q_upper': ql,
            'polygon_phase_bound': polygon, 'postcalibration_sensor_budget': sensor,
            'independent_overlap_model_bound': independent_model,
            'same_budget_independent_overlap_total': independent_total,
            'relative_readout_gain_error': eps_gain, 'native_channel_jitter': jitter,
            'calibrated_additive_reference_budget': sensor/3,
            'normalized_sensor_overlap_error': zeta, 'sensor_phase_bound': acquisition,
            'total_phase_bound': total, 'observed_endpoint_floor': endpoint-zeta,
            'observed_link_floor': link-zeta,
            'original_raw_model_budget_retained': False}


def main(out):
    out.mkdir(parents=True, exist_ok=True); here = Path(__file__).resolve().parent
    src = json.loads((here/'SOURCES.json').read_text())['sources']
    assert all(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256'] for s in src)
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']
    byid = {r['id']: r for r in ledger}; assert all(byid[r['id']] == r for r in rows)
    rng = random.Random(20261024); exact_checks = 0; fd = []
    def unit():
        t = [F(rng.randint(-3, 3), 7) for _ in range(13)]; n = sum(a*a for a in t)
        return [(1-n)/(1+n)]+[2*a/(1+n) for a in t]
    def arg_polygon(vs):
        zs = [complex(*h(a, b)) for a, b in zip(vs, vs[1:])]
        zz = complex(*h(vs[0], vs[-1])); ans = zz/abs(zz)
        for z in zs: ans *= (z/abs(z)).conjugate()
        return ans
    for trial in range(100):
        vs = [unit() for _ in range(6)]
        if any(h(a, b) == (0, 0) for a, b in zip(vs, vs[1:])) or h(vs[0], vs[-1]) == (0, 0): continue
        ws = [[F(rng.randint(-3, 3), 5) for _ in range(14)] for _ in vs]
        gs = gradients(vs)
        assert variation(vs, ws) == sum(h(g, w)[1] for g, w in zip(gs, ws))
        for g, v in zip(gs, vs):
            assert h(v, g) == (0, 0)  # Radial and vertical phase directions annihilated.
        vertical = [vadd(vscale(F(j+1, 3), v), vscale(F(j-2, 5), J(v))) for j, v in enumerate(vs)]
        assert variation(vs, vertical) == 0
        # Squared gradient triangle bound, using exact rational q^2 values.
        ee = h(vs[0], vs[-1]); endq2 = (1-ee[0]**2-ee[1]**2)/(ee[0]**2+ee[1]**2)
        q2 = []
        for a, b in zip(vs, vs[1:]):
            z = h(a, b); sq = z[0]**2+z[1]**2; q2.append((1-sq)/sq)
        adj = [(q2[0], endq2)]+list(zip(q2, q2[1:]))+[(q2[-1], endq2)]
        for g, (a, b) in zip(gs, adj): assert sum(x*x for x in g) <= 2*(a+b)
        if trial < 20:
            vf = [[float(x) for x in v] for v in vs]; wf = [[float(x) for x in w] for w in ws]
            step = 1e-6
            plus = [[x+step*w for x, w in zip(v, dv)] for v, dv in zip(vf, wf)]
            minus = [[x-step*w for x, w in zip(v, dv)] for v, dv in zip(vf, wf)]
            numerical = cmath.phase(arg_polygon(plus)/arg_polygon(minus))/(2*step)
            error = abs(numerical-float(variation(vs, ws)))
            assert error < 2e-6; fd.append(error)
        exact_checks += 1
    profiles = [certificate(26, 32000000, F(1, 1000000)), certificate(21, 8000000, F(1, 5000000))]
    assert profiles[0]['total_phase_bound'] < F(1, 400)
    assert profiles[0]['operator_bound_ratio'] > 11413 and profiles[1]['operator_bound_ratio'] > 570
    assert all(p['same_budget_independent_overlap_total'] > F(1, 250) for p in profiles)
    # Larger differential box fails a sufficient visibility/phase certificate;
    # this is not a universal obstruction or an empirical boundary.
    failed = False
    try: certificate(21, 8000000, F(1, 1000000))
    except AssertionError: failed = True
    assert failed
    simp, A, JJ, P, anchors, T, K, sectors = meter.carrier()
    mf = lambda M, x: [sum(float(a)*v for a, v in zip(row, x)) for row in M]
    dot = lambda a, b: sum(x*y for x, y in zip(a, b))
    i, top = simp.index((0, 1)), simp.index((0, 1, 2, 3))
    ref = [(float(j == i)+float(j == top))/math.sqrt(2) for j in range(15)]
    preparations = [ref]
    for target in [i, top]: preparations += [[v+sgn*.1*float(j == target) for j, v in enumerate(ref)] for sgn in [-1, 1]]
    results = []; witness = None
    for p in profiles:
        bits = p['bits']; delta = float(p['delta_differential']); r = float(p['postcalibration_sensor_budget'])
        e0 = float(p['initial_meter_norm'])
        for prep, seed in enumerate(preparations):
            comp = [mf(pp, seed) for pp in sectors]; jc = [mf(JJ, v) for v in comp]
            norm2 = dot(seed, seed); weights = [dot(seed, v)/norm2 for v in comp]
            for gi, gains in enumerate([(1., 1., 1.5), (.99, 1.01, 1.49), (1.01, .99, 1.51)]):
                for common_id, (ck, cd, cg) in enumerate([(0., 0., 0.), (.001, .001, .001), (-.001, -.001, -.001), (.001, -.001, .001)]):
                    kappa, gamma = .25*(1+ck), 1+cd
                    for trial, direction in enumerate([0, -1, 1]):
                        eps = [direction*delta*.5*((-1)**k) for k in range(3)]
                        actualT = 2*math.pi+[-.01, 0., .01][trial]
                        codes = []; model_states = []; ideal_states = []
                        max_model_error = 0.; minimum_signal = 1.
                        for step in range(129):
                            tau = 1+actualT*step/128
                            nominal_beta = meter.scalar_transfer(tau, kappa, gamma, 2*cg)[1]
                            gain = abs(nominal_beta); minimum_signal = min(minimum_signal, gain)
                            observed = [0.]*15; ideal = [0.]*15
                            beta_phase = nominal_beta/gain
                            for k, g in enumerate(gains):
                                aa, bb = meter.scalar_transfer(tau, kappa, gamma, 2*(cg+eps[k]))
                                rot = cmath.exp(2j*g*tau); z = bb*rot/gain; zz = beta_phase*rot
                                for j in range(15):
                                    observed[j] += z.real*comp[k][j]+z.imag*jc[k][j]
                                    ideal[j] += zz.real*comp[k][j]+zz.imag*jc[k][j]
                            # Initial residual along the top seed plane; exact norm<=e0.
                            if direction:
                                aa, bb = meter.scalar_transfer(tau, kappa, gamma, 2*(cg+eps[2]))
                                d = complex(-gamma, 2*(cg+eps[2])); response = (aa+d*bb/kappa)*cmath.exp(2j*gains[2]*tau)/gain
                                initial = [direction*e0*float(j == top) for j in range(15)]
                                ji = mf(JJ, initial)
                                for j in range(15): observed[j] += response.real*initial[j]+response.imag*ji[j]
                            model_error = math.sqrt(sum((a-b)**2 for a, b in zip(observed, ideal)))
                            max_model_error = max(max_model_error, model_error)
                            assert model_error <= float(p['calibrated_model_error_B'])+5e-13
                            model_states.append(mf(T, observed)); ideal_states.append(mf(T, ideal))
                            noisy = [v+r*((-1)**(step+j+common_id+trial)) for j, v in enumerate(observed)]
                            codes.append(acq.quantize(noisy, bits))
                        result = acq.integer_phase(iter(codes), bits, anchors, A)
                        assert result['status'] == 'PASS'
                        angle = acq.display_phase(result['direction'])
                        model_Q, ideal_Q = arg_polygon(model_states), arg_polygon(ideal_states)
                        model_phase_error = abs(cmath.phase(model_Q/ideal_Q))
                        sensor_phase_error = abs(cmath.phase(cmath.exp(1j*angle)/model_Q))
                        assert model_phase_error <= float(p['polygon_phase_bound'])+5e-11
                        assert sensor_phase_error <= float(p['sensor_phase_bound'])+5e-11
                        error = abs(cmath.phase(cmath.exp(1j*(angle+2*math.pi*weights[2]))))
                        assert error <= float(p['total_phase_bound'])+5e-11
                        assert abs(cmath.exp(1j*angle)-1) > 1.7
                        row = {'bits': bits, 'preparation': prep, 'gains': gi, 'common_profile': common_id,
                               'differential_direction': direction, 'max_model_error': max_model_error,
                               'minimum_reference_meter_gain': minimum_signal, 'phase_error_rad': error}
                        row['model_phase_error_rad'] = model_phase_error
                        row['sensor_phase_error_rad'] = sensor_phase_error
                        results.append(row)
                        if witness is None or error > witness['phase_error_rad']:
                            witness = {**row, 'raw_snapshot_codes': codes, 'exact_phase_direction': list(result['direction'])}
    assert len(results) == 360
    assert max(x['max_model_error'] for x in results) > F(9, 320000000)
    replay = acq.integer_phase(iter(witness['raw_snapshot_codes']), witness['bits'], anchors, A)
    assert list(replay['direction']) == witness['exact_phase_direction']
    def serial(x):
        if isinstance(x, F): return str(x)
        if isinstance(x, dict): return {k: serial(v) for k, v in x.items()}
        if isinstance(x, list): return [serial(v) for v in x]
        return x
    save(out/'certificate.json', serial({'evidence': 'EXACT_CONDITIONAL', 'profiles': profiles,
         'common_control_bounds': 'absolute common gain detuning<=1/1000;relative common port/damping<=1/1000',
         'gradient': 'dF=sum Im h(g_j,dv_j);h(v_j,g_j)=0',
         'polygon_bound': '2chi*(q_endpoint+sumq_links)', 'amendment': 'Model/differential error has a separate phase budget; old raw-amplitude/strict-overlap requirement is not retained',
         'physical_promotion': 0}))
    save(out/'gradient.json', {'evidence': 'EXACT_CONDITIONAL', 'exact_derivative_fixtures': exact_checks,
         'radial_and_vertical_annihilation': 'PASS', 'squared_gradient_bounds': 'PASS',
         'finite_difference_cross_checks': len(fd), 'max_binary64_derivative_error': max(fd),
         'failed_larger_21bit_sufficient_certificate': True})
    save(out/'numerical.json', {'evidence': 'NUMERICAL_CONSTRUCTOR', 'cases': len(results),
         'max_phase_error_rad': max(x['phase_error_rad'] for x in results),
         'max_model_error': max(x['max_model_error'] for x in results),
         'max_model_phase_error_rad': max(x['model_phase_error_rad'] for x in results),
         'max_sensor_phase_error_rad': max(x['sensor_phase_error_rad'] for x in results),
         'minimum_reference_gain': min(x['minimum_reference_meter_gain'] for x in results),
         'source': 'Binary64 closed coupled-mode paths; exact integer processing after digitization; not interval or empirical validation',
         'representative_cases': results[:4]+results[-4:]})
    save(out/'integer_witness.json', witness)
    summary = {'status': 'PASS', 'source_hashes': len(src), 'literal_rows': len(rows),
               'exact_polygon_gradient_fixtures': exact_checks, 'radial_vertical_null': 'PASS',
               'numerical_derivative_cross_checks': len(fd), 'integer_windows': len(results),
               'exact_integer_witness_replay': 'PASS', 'common_meter_signal_lower': '>1/10',
               'phase26_delta': '1/1000000', 'phase21_delta': '1/5000000',
               'phase26_total_bound': '<1/400rad', 'phase21_total_bound': '<1/250rad',
               'operator_bound_improvement': ['>11413','>570'],
               'old_raw_model_budget_retained': False, 'hardware': 'NOT_MEASURED', 'physical_promotion': 0}
    save(out/'summary.json', summary); print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
