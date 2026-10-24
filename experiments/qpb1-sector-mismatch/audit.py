"""Uniform three-sector meter detuning with exact interval/scalar budgets.

Primary certificate is exact rational outward interval arithmetic, not a scan.
Binary64 closed solutions and exact digitized phase are separate cross-checks.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import cmath
import hashlib
import importlib.util
import json
import math

ROOT = Path(__file__).resolve().parents[2]
enc_spec = importlib.util.spec_from_file_location('sector_enclosure', Path(__file__).with_name('enclose.py'))
enc_module = importlib.util.module_from_spec(enc_spec); enc_spec.loader.exec_module(enc_module)
transfer_enclosure, polynomials, evaluate = enc_module.transfer_enclosure, enc_module.polynomials, enc_module.evaluate
spec = importlib.util.spec_from_file_location('proj', ROOT/'experiments/qpb1-projective-tolerance/audit.py')
proj = importlib.util.module_from_spec(spec); spec.loader.exec_module(proj)
meter, acq, window, alg = proj.meter, proj.acq, proj.window, proj.alg
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def serial(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {k: serial(v) for k, v in x.items()}
    if isinstance(x, list): return [serial(v) for v in x]
    return x


def budget(omega=F(11, 500), bits=26, divisor=32000000, extra_delta=F(1, 10**7)):
    parent = window.budget(); old = meter.limits(bits, divisor)
    T, H, M = parent['time_upper'], old['H'], 128
    attenuation = F(3, 2)*omega**2
    weight_l1 = attenuation/(2*(1-attenuation))
    coherence = 1-attenuation**2/(2*(1-attenuation)**2)
    filter_endpoint = F(2, 5)*omega+20*omega**3
    endpoint_spread = parent['halfspread_upper']+filter_endpoint
    speed_spread = F(13, 25)+2*omega
    step_spread = speed_spread*T/M
    endpoint_mean = 1-endpoint_spread**2/2
    link_mean = 1-step_spread**2/2
    ve, vl = coherence*endpoint_mean, coherence*link_mean
    endpoint_phase = endpoint_spread**3/(3*endpoint_mean)
    link_phase = M*step_spread**3/(3*link_mean)
    weight_phase = weight_l1*(endpoint_spread+speed_spread*T)
    structured = endpoint_phase+link_phase+weight_phase
    B = 8*(old['initial_meter_norm']+H*extra_delta*F(11, 10))
    smin = F(9, 10)*(1-attenuation)
    v, l = ve-4*B/smin, vl-4*B/smin
    chi = B/(smin-B)
    extra = 2*chi*(proj.q_upper(v, F(3, 20))+M*proj.q_upper(l, F(1, 25)))
    r, q = old['combined_raw_budget'], F(2, 2**bits)
    zeta = F(31, 2)*(r+q)/(smin-B)
    sensor = zeta/(v-zeta)+M*zeta/(l-zeta)
    total = structured+extra+sensor
    # Eight-fold inverseb0 bounds gain, timing and additive/reference errors.
    S = F(11, 10)+old['initial_meter_norm']
    gain = r/(24*S); jitter = r/(120*S*(1+gain))
    assert 8*S*gain+40*S*(1+gain)*jitter+r/3 == r
    assert F(151, 50)+omega+F(1, 4)+1+extra_delta < 5
    assert smin-B-4*(r+q) > F(4, 5)
    assert F(11, 10)+B+4*(r+q) < F(6, 5)
    assert F(11, 10)+B+r+q < 2
    assert v-zeta > F(99, 100) and l-zeta > F(999, 1000)
    assert F(173, 100)-total > F(17, 10)
    return {'bits': bits, 'sector_native_gain_radius': omega/2,
            'frequency_mismatch_radius': omega, 'constant_sector_errors_only': True,
            'attenuation': attenuation, 'weight_l1_bound': weight_l1,
            'coherence_lower': coherence, 'filter_endpoint_bound': filter_endpoint,
            'endpoint_halfspread': endpoint_spread, 'step_halfspread': step_spread,
            'phase_speed_halfspread': speed_spread,
            'endpoint_centered_phase': endpoint_phase, 'summed_link_centered_phase': link_phase,
            'weight_drift_phase': weight_phase, 'structured_phase': structured,
            'structured_endpoint_visibility': ve, 'structured_link_visibility': vl,
            'arbitrary_other_operator_budget': extra_delta,
            'initial_meter_norm': old['initial_meter_norm'], 'other_calibrated_norm_error': B,
            'other_phase': extra, 'combined_sensor_reference_budget': r,
            'relative_sensor_gain_budget': gain, 'native_channel_jitter_budget': jitter,
            'additive_reference_budget': r/3, 'sensor_overlap_error': zeta,
            'sensor_phase': sensor, 'total_phase': total,
            'observed_endpoint_floor': v-zeta, 'observed_link_floor': l-zeta,
            'phase_screen_passes': total < F(1, 250)}


def raw_polygon(coeffs):
    B = complex(*acq.overlap(coeffs[0], coeffs[-1])); B /= abs(B)
    for a, b in zip(coeffs, coeffs[1:]):
        z = complex(*acq.overlap(a, b)); B *= (z/abs(z)).conjugate()
    return B/abs(B)


def main(out):
    out.mkdir(parents=True, exist_ok=True); here = Path(__file__).resolve().parent
    src = json.loads((here/'SOURCES.json').read_text())['sources']
    assert all(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256'] for s in src)
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']
    byid = {r['id']: r for r in ledger}; assert all(byid[r['id']] == r for r in rows)
    enc = transfer_enclosure()
    assert enc['omega_domain'] == ['-11/500', '11/500']
    cert = budget(); assert cert['phase_screen_passes'] and cert['total_phase'] < F(1, 290)
    # A lower-resolution continuation is NOT certified by this error allocation.
    low = budget(bits=21, divisor=8000000)
    assert not low['phase_screen_passes']
    # Exact outward interval transfer vs a different closed-form implementation.
    _, pb = polynomials(); H = F(5107, 700); omega = F(11, 500)
    remainder = (omega*H)**6/(math.factorial(6)*(1-omega*H))
    closed_checks = []
    for j in range(80):
        t = 1+(H-1)*F(j, 79); w = omega*F((j*13) % 81-40, 40)
        terms = [evaluate(p, t) for p in pb]
        series = sum((1j*float(w))**r*float(v) for r, v in enumerate(terms))
        closed = meter.scalar_transfer(float(t), omega=float(w))[1]
        error = abs(series-closed)
        assert error <= float(remainder)+5e-14
        closed_checks.append(error)
    # Weighted-incidence preparation/domain fixtures: exact scalar inequalities.
    weight_checks = 0
    for r in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        for aa, bb in product([1-cert['attenuation'], F(1)], repeat=2):
            mean = r*aa+(1-r)*bb
            l1 = abs(r*aa/mean-r)+abs((1-r)*bb/mean-(1-r))
            assert l1 <= cert['weight_l1_bound']
            weight_checks += 1
    simp, A, J, P, anchors, Tmat, K, sectors = meter.carrier()
    mf = lambda M, x: [sum(float(a)*v for a, v in zip(row, x)) for row in M]
    dot = lambda a, b: sum(x*y for x, y in zip(a, b))
    ie, it = simp.index((0, 1)), simp.index((0, 1, 2, 3))
    ref = [(float(j == ie)+float(j == it))/math.sqrt(2) for j in range(15)]
    preparations = [ref]
    for target in [ie, it]: preparations += [[v+sgn*.1*float(j == target) for j, v in enumerate(ref)] for sgn in [-1, 1]]
    emax = float(cert['sector_native_gain_radius'])
    detunings = list(product([-emax, 0., emax], repeat=3))
    detunings += [(0., 0., .01), (0., .01, 0.), (.01, 0., 0.)]
    results = []; witness = None; common_nulls = []
    for prep, seed in enumerate(preparations):
        comp = [mf(pp, seed) for pp in sectors]; jc = [mf(J, v) for v in comp]
        support = dot(seed, seed); weights = [dot(seed, v)/support for v in comp]
        for gi, gains in enumerate([(1., 1., 1.5), (.99, 1.01, 1.49), (1.01, .99, 1.51)]):
            for di, detuning in enumerate(detunings):
                for ti, dt in enumerate([-.01, 0., .01]):
                    actualT = 2*math.pi+dt; codes = []; structured = []; actual = []; baseline = []
                    max_other = 0.; minimum_gain = 1.
                    direction = [-1, 0, 1][ti]
                    other = float(cert['arbitrary_other_operator_budget'])*direction
                    e0 = float(cert['initial_meter_norm'])*direction
                    for step in range(129):
                        tau = 1+actualT*step/128; b0 = meter.nominal_b(tau)
                        st = [0.]*15; ac = [0.]*15; base = [0.]*15
                        for k, (g, eps) in enumerate(zip(gains, detuning)):
                            rot = cmath.exp(2j*g*tau)
                            betas = meter.scalar_transfer(tau, omega=2*eps)[1]
                            omega_actual = 2*eps+other*((-1)**k)
                            aa, bb = meter.scalar_transfer(tau, omega=omega_actual)
                            z, zz = betas*rot/b0, bb*rot/b0
                            for q in range(15):
                                st[q] += z.real*comp[k][q]+z.imag*jc[k][q]
                                ac[q] += zz.real*comp[k][q]+zz.imag*jc[k][q]
                                base[q] += rot.real*comp[k][q]+rot.imag*jc[k][q]
                            if k == 2 and direction:
                                response = (aa+complex(-1, omega_actual)*bb/.25)*rot/b0
                                residual = [e0*float(q == it) for q in range(15)]; jr = mf(J, residual)
                                for q in range(15): ac[q] += response.real*residual[q]+response.imag*jr[q]
                        err = math.sqrt(sum((a-b)**2 for a, b in zip(ac, st))); max_other = max(max_other, err)
                        assert err < float(cert['other_calibrated_norm_error'])+5e-13
                        structured.append(mf(Tmat, st)); actual.append(mf(Tmat, ac)); baseline.append(mf(Tmat, base))
                        minimum_gain = min(minimum_gain, b0*math.sqrt(1-float(cert['attenuation'])))
                        noise = float(cert['combined_sensor_reference_budget'])
                        codes.append(acq.quantize([v+noise*((-1)**(step+q+di+ti)) for q, v in enumerate(ac)], 26))
                    result = acq.integer_phase(iter(codes), 26, anchors, A)
                    assert result['status'] == 'PASS'
                    qs, qa, qu = raw_polygon(structured), raw_polygon(actual), raw_polygon(baseline)
                    Q0 = cmath.exp(-2j*math.pi*weights[2])
                    struct_error = abs(cmath.phase(qs/Q0)); other_error = abs(cmath.phase(qa/qs))
                    angle = acq.display_phase(result['direction'])
                    sensor_error = abs(cmath.phase(cmath.exp(1j*angle)/qa))
                    total_error = abs(cmath.phase(cmath.exp(1j*angle)/Q0))
                    assert struct_error < float(cert['structured_phase'])+5e-11
                    assert other_error < float(cert['other_phase'])+5e-11
                    assert sensor_error < float(cert['sensor_phase'])+5e-11
                    assert total_error < float(cert['total_phase'])+5e-11
                    assert abs(cmath.exp(1j*angle)-1) > 1.7
                    if detuning[0] == detuning[1] == detuning[2]:
                        null_error = abs(cmath.phase(qs/qu)); assert null_error < 5e-12; common_nulls.append(null_error)
                    row = {'preparation': prep, 'gains': gi, 'detuning': list(detuning), 'window_error': dt,
                           'structured_phase_error': struct_error, 'other_phase_error': other_error,
                           'sensor_phase_error': sensor_error, 'total_phase_error': total_error,
                           'max_other_raw_error': max_other, 'meter_gain_lower_in_case': minimum_gain}
                    results.append(row)
                    if witness is None or total_error > witness['total_phase_error']:
                        witness = {**row, 'raw_snapshot_codes': codes, 'exact_phase_direction': list(result['direction'])}
    assert len(results) == 1350
    replay = acq.integer_phase(iter(witness['raw_snapshot_codes']), 26, anchors, A)
    assert list(replay['direction']) == witness['exact_phase_direction']
    # Outside-box control: qualified meter samples can still miss the phase target.
    bad = []
    for step in range(129):
        tau = 1+2*math.pi*step/128; b0 = meter.nominal_b(tau)
        z = [meter.scalar_transfer(tau, omega=2*eps)[1]*cmath.exp(2j*g*tau)/b0
             for g, eps in zip([1., 1., 1.5], [0., 0., .05])]
        # Reference seed has sector weights1/4,1/4,1/2; use fullcarrier formula.
        comp = [mf(pp, ref) for pp in sectors]; jc = [mf(J, v) for v in comp]
        vec = [sum(v.real*x[q]+v.imag*jx[q] for v, x, jx in zip(z, comp, jc)) for q in range(15)]
        bad.append(acq.quantize(vec, 26))
    bad_result = acq.integer_phase(iter(bad), 26, anchors, A)
    assert bad_result['status'] == 'PASS'
    bad_error = abs(cmath.phase(-cmath.exp(1j*acq.display_phase(bad_result['direction']))))
    assert bad_error > .004
    save(out/'enclosure.json', enc)
    save(out/'budget.json', serial({'evidence': 'EXACT_CONDITIONAL', 'protocol26': cert,
         'uncertified21_same_allocation': low, 'three_sector_box': '|epsilon_k|<=11/1000 independently,constant',
         'old_point_interior_margin': '1/1000 in maxnorm around(0,0,1/100)',
         'physical_promotion': 0}))
    save(out/'numerical.json', {'evidence': 'NUMERICAL_CONSTRUCTOR', 'integer_windows': len(results),
         'max_total_phase_error': max(r['total_phase_error'] for r in results),
         'max_structured_phase_error': max(r['structured_phase_error'] for r in results),
         'max_other_phase_error': max(r['other_phase_error'] for r in results),
         'common_null_checks': len(common_nulls), 'max_common_null_error': max(common_nulls),
         'closed_form_series_checks': len(closed_checks), 'max_series_display_difference': max(closed_checks),
         'out_of_box_control': {'hidden_detuning': .05, 'data_gates': 'PASS', 'phase_error': bad_error, 'phase_screen': 'FAIL'},
         'source': 'Binary64closedcoupledsolutions,notintervaltrajectoryvalidation;exactintegerprocessingafterdigitization',
         'representatives': results[:3]+results[-3:]})
    save(out/'integer_witness.json', witness)
    summary = {'status': 'PASS', 'source_hashes': len(src), 'literal_rows': len(rows),
               'exact_rational_time_cells': enc['time_cells'], 'sector_gain_radius': '11/1000',
               'arbitrary_other_operator_budget': '1/10000000', 'integer_windows': len(results),
               'exact_integer_witness_replay': 'PASS', 'exact_weight_fixtures': weight_checks,
               'closed_form_series_checks': len(closed_checks), 'common_null_checks': len(common_nulls),
               'total_phase_bound': '<1/290rad<1/250rad', 'endpoint_visibility': '>99/100',
               'link_visibility': '>999/1000', 'calibrated_ADC_bits': 26,
               'hardware': 'NOT_MEASURED', 'physical_promotion': 0}
    save(out/'summary.json', summary); print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
