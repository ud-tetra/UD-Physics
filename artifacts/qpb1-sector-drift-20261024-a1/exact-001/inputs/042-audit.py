"""Lipschitz sector drift: rational certificate and numerical constructor checks.

The continuous-domain proof is in README.md; ODE checks are binary64 only.
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
spec = importlib.util.spec_from_file_location('constant_sector', ROOT/'experiments/qpb1-sector-mismatch/audit.py')
sm = importlib.util.module_from_spec(spec); spec.loader.exec_module(sm)
meter, acq, proj = sm.meter, sm.acq, sm.proj
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def budget(rate=F(1, 200000), bits=26):
    c = sm.budget(); O = F(11, 500); H = F(5107, 700); M = 128
    # Real Volterra kernel integral <=5/4+H/12<2. Separate parity is essential.
    J = F(2); delta = 2*rate*H
    assert F(5, 4)+H/12 < J
    X = 16*O*delta/(1-4*O**2)
    Y = 4*delta*(1+4*O**2)/(1-4*O**2)
    amp = 2*X+X**2+4*O*Y+Y**2
    real_floor = 1-4*O**2-X
    assert real_floor > 0
    phase_dev = (X+Y)/real_floor
    amin = 1-c['attenuation']-amp; amax = 1+amp
    width = amax-amin
    La = width/(2*amin); Ka = 1-width**2/(2*amin**2)
    D = c['endpoint_halfspread']+2*phase_dev
    d = c['step_halfspread']+2*phase_dev
    ve, vl = Ka*(1-D**2/2), Ka*(1-d**2/2)
    endpoint = D**3/(3*(1-D**2/2))
    links = M*d**3/(3*(1-d**2/2))
    weight = La*(D+M*d)
    structured = endpoint+links+weight
    smin = F(9, 10)*amin
    B = c['other_calibrated_norm_error']
    v, l = ve-4*B/smin, vl-4*B/smin
    eta = B/(smin-B)
    other = 2*eta*(proj.q_upper(v, F(3, 20))+M*proj.q_upper(l, F(1, 25)))
    r, q = c['combined_sensor_reference_budget'], F(2, 2**bits)
    zeta = F(31, 2)*(r+q)/(smin-B)
    sensor = zeta/(v-zeta)+M*zeta/(l-zeta)
    total = structured+other+sensor
    # Sensor timing allocation is unchanged: time-varying skew detuning adds no storage.
    S = F(11, 10)+c['initial_meter_norm']
    assert 8*S*c['relative_sensor_gain_budget']+40*S*(1+c['relative_sensor_gain_budget'])*c['native_channel_jitter_budget']+r/3 == r
    assert F(151, 50)+O+F(1, 4)+1+c['arbitrary_other_operator_budget'] < 5
    assert smin-B-4*(r+q) > F(4, 5)
    assert F(11, 10)*(1+amp)+B+4*(r+q) < F(6, 5)
    assert F(11, 10)*(1+amp)+B+r+q < 2
    return {'native_gain_lipschitz_rate': rate, 'frequency_lipschitz_rate': 2*rate,
            'native_gain_cap': O/2, 'frequency_cap': O, 'meter_time_upper': H,
            'native_gain_change_from_start': rate*H, 'frequency_change_from_start': delta,
            'kernel_integral_upper': J, 'real_transfer_difference': X,
            'imag_transfer_difference': Y, 'amplitude_squared_difference': amp,
            'phase_difference_from_frozen_initial': phase_dev,
            'amplitude_squared_lower': amin, 'amplitude_squared_upper': amax,
            'weight_l1_bound': La, 'coherence_lower': Ka,
            'endpoint_halfspread': D, 'link_halfspread': d,
            'endpoint_centered_phase': endpoint, 'summed_link_centered_phase': links,
            'weight_phase': weight, 'structured_phase': structured,
            'structured_endpoint_visibility': ve, 'structured_link_visibility': vl,
            'raw_active_norm_lower': smin, 'other_calibrated_norm_error': B,
            'other_operator_budget': c['arbitrary_other_operator_budget'],
            'initial_meter_norm': c['initial_meter_norm'], 'other_phase': other,
            'sensor_reference_budget': r, 'ADC_bits': bits, 'sensor_overlap_error': zeta,
            'sensor_phase': sensor, 'total_phase': total,
            'observed_endpoint_floor': v-zeta, 'observed_link_floor': l-zeta,
            'phase_screen_passes': total < F(1, 250),
            'visibility_screens_pass': v-zeta > F(99, 100) and l-zeta > F(999, 1000)}


def scalar_path(epsilon, T, substeps=32, extra=0., reset=0j):
    """Three independent 2x2 complex ODEs, RK4; samples at 1+j*T/128."""
    state = [1+0j, reset]*3
    def rhs(t, y):
        answer = []
        for k, e in enumerate(epsilon(t)):
            a, b = y[2*k:2*k+2]
            answer += [-b/4, a/4+complex(-1, 2*e+extra*((-1)**k))*b]
        return answer
    def advance(start, end, steps, y):
        h = (end-start)/steps
        for n in range(steps):
            t = start+n*h
            k1 = rhs(t, y)
            k2 = rhs(t+h/2, [v+h*z/2 for v, z in zip(y, k1)])
            k3 = rhs(t+h/2, [v+h*z/2 for v, z in zip(y, k2)])
            k4 = rhs(t+h, [v+h*z for v, z in zip(y, k3)])
            y = [v+h*(a+2*b+2*c+d)/6 for v, a, b, c, d in zip(y, k1, k2, k3, k4)]
        return y
    state = advance(0., 1., substeps*4, state)
    samples = [state]
    for j in range(128):
        state = advance(1+j*T/128, 1+(j+1)*T/128, substeps, state)
        samples.append(state)
    return samples


def profiles(rate, H):
    emax = .011; margin = rate*H/2
    out = []
    for signs in product([-1, 1], repeat=3):
        base = [s*(emax-margin) for s in signs]
        # Both monotone directions hit the amplitude cap at one endpoint.
        out.append(('ramp_'+''.join('p' if s > 0 else 'm' for s in signs),
                    lambda t, b=base, s=signs: [v+q*rate*(t-H/2) for v, q in zip(b, s)]))
    out += [('inward_boundary', lambda t: [emax-rate*t, -emax+rate*t, emax-rate*t]),
            ('tent_differential', lambda t: [emax-rate*min(t, H-t), -emax+rate*min(t, H-t), 0.]),
            ('sine_differential', lambda t: [emax-rate+rate*math.sin(t), -emax+rate-rate*math.sin(t), rate*math.cos(t)]),
            ('common_sine', lambda t: [emax-rate+rate*math.sin(t)]*3),
            ('common_ramp', lambda t: [-emax+rate*t]*3)]
    return out


def main(out):
    out.mkdir(parents=True, exist_ok=True); here = Path(__file__).resolve().parent
    src = json.loads((here/'SOURCES.json').read_text())['sources']
    assert all(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256'] for s in src)
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']
    byid = {r['id']: r for r in ledger}; assert all(byid[r['id']] == r for r in rows)
    enclosure = sm.transfer_enclosure()
    assert F(enclosure['normalized_coefficients_abs_upper'][1]) < 1
    cert = budget(); assert cert['total_phase'] < F(1, 260)
    assert cert['phase_screen_passes'] and cert['visibility_screens_pass']
    failed = budget(F(1, 100000)); assert not failed['phase_screen_passes']
    zero = budget(F(0)); parent = sm.budget()
    assert zero['total_phase'] == parent['total_phase']
    # Algebraic kernel constants: sqrt3 between 12/7 and7/4 is enough.
    assert F(12, 7)**2 < 3 < F(7, 4)**2
    # alpha=(2-sqrt3)/4>1/16; beta=(2+sqrt3)/4>9/10;
    # beta/(beta-alpha)<9/8 and alpha/(beta-alpha)<1/12.
    assert F(7, 4) == F(2)-4*F(1, 16)
    assert F(12, 7) > F(8, 5) and F(12, 7) > F(5, 3)
    simp, A, J, P, anchors, Tmat, K, sectors = meter.carrier()
    mf = lambda mat, x: [sum(float(a)*v for a, v in zip(row, x)) for row in mat]
    dot = lambda a, b: sum(x*y for x, y in zip(a, b))
    ie, it = simp.index((0, 1)), simp.index((0, 1, 2, 3))
    ref = [(float(j == ie)+float(j == it))/math.sqrt(2) for j in range(15)]
    preps = [ref]
    for target in [ie, it]: preps += [[v+s*.1*float(j == target) for j, v in enumerate(ref)] for s in [-1, 1]]
    H = float(cert['meter_time_upper']); rate = float(cert['native_gain_lipschitz_rate'])
    profs = profiles(rate, H); results = []; witness = None; nulls = []; comparisons = []
    max_X = max_Y = max_A = max_chi = 0.
    for pi, (name, eps) in enumerate(profs):
        for ti, dt in enumerate([-.01, 0., .01]):
            duration = 2*math.pi+dt
            path = scalar_path(eps, duration)
            direction = [-1, 0, 1][ti]
            other = direction*float(cert['other_operator_budget'])
            e0 = direction*float(cert['initial_meter_norm'])/1.1
            actual = scalar_path(eps, duration, extra=other, reset=complex(e0))
            if ti == 1 and pi in [0, 8, 9, 10, 11, 12]:
                finer = scalar_path(eps, duration, substeps=64)
                diff = max(abs(a-b) for ya, yb in zip(path, finer) for a, b in zip(ya, yb))
                # Piecewise-linear tent has a corner; RK4 is not fourth order there.
                assert diff < 2e-9
                comparisons.append({'profile': name, 'RK4_substep_doubling_difference': diff})
            for step, y in enumerate(path):
                tau = 1+duration*step/128; b0 = meter.nominal_b(tau)
                initial = eps(0.)
                for k in range(3):
                    z = y[2*k+1]/b0
                    frozen = meter.scalar_transfer(tau, omega=2*initial[k])[1]/b0
                    X, Y = abs((z-frozen).real), abs((z-frozen).imag)
                    AA = abs(abs(z)**2-abs(frozen)**2); chi = abs(cmath.phase(z/frozen))
                    assert X < float(cert['real_transfer_difference'])+2e-9
                    assert Y < float(cert['imag_transfer_difference'])+2e-9
                    assert AA < float(cert['amplitude_squared_difference'])+2e-9
                    assert chi < float(cert['phase_difference_from_frozen_initial'])+2e-9
                    max_X, max_Y, max_A, max_chi = max(max_X, X), max(max_Y, Y), max(max_A, AA), max(max_chi, chi)
            for prep, seed in enumerate(preps):
                comp = [mf(pp, seed) for pp in sectors]; jc = [mf(J, v) for v in comp]
                weights = [dot(seed, v)/dot(seed, seed) for v in comp]
                for gi, gains in enumerate([(1., 1., 1.5), (.99, 1.01, 1.49), (1.01, .99, 1.51)]):
                    codes = []; structured = []; changed = []; base = []; max_other = 0.
                    for step, (y, ya) in enumerate(zip(path, actual)):
                        tau = 1+duration*step/128; b0 = meter.nominal_b(tau)
                        rot = [cmath.exp(2j*g*tau) for g in gains]
                        z = [y[2*k+1]*rot[k]/b0 for k in range(3)]
                        za = [ya[2*k+1]*rot[k]/b0 for k in range(3)]
                        def combine(zz):
                            return [sum(v.real*x[q]+v.imag*jx[q] for v, x, jx in zip(zz, comp, jc)) for q in range(15)]
                        st, ac = combine(z), combine(za)
                        max_other = max(max_other, math.sqrt(sum((a-b)**2 for a, b in zip(ac, st))))
                        structured.append(mf(Tmat, st)); changed.append(mf(Tmat, ac)); base.append(mf(Tmat, combine(rot)))
                        noise = float(cert['sensor_reference_budget'])
                        codes.append(acq.quantize([v+noise*((-1)**(step+q+pi+ti)) for q, v in enumerate(ac)], 26))
                    assert max_other < float(cert['other_calibrated_norm_error'])+2e-9
                    result = acq.integer_phase(iter(codes), 26, anchors, A)
                    assert result['status'] == 'PASS'
                    qs, qa, qb = map(sm.raw_polygon, [structured, changed, base])
                    Q0 = cmath.exp(-2j*math.pi*weights[2]); angle = acq.display_phase(result['direction'])
                    errs = [abs(cmath.phase(qs/Q0)), abs(cmath.phase(qa/qs)), abs(cmath.phase(cmath.exp(1j*angle)/qa)), abs(cmath.phase(cmath.exp(1j*angle)/Q0))]
                    for v, key in zip(errs, ['structured_phase', 'other_phase', 'sensor_phase', 'total_phase']):
                        assert v < float(cert[key])+5e-9
                    assert abs(cmath.exp(1j*angle)-1) > 1.7
                    if name.startswith('common_'):
                        err = abs(cmath.phase(qs/qb)); assert err < 5e-12; nulls.append(err)
                    row = {'profile': name, 'preparation': prep, 'plant_gains': gi, 'window_error': dt,
                           'structured_phase_error': errs[0], 'other_phase_error': errs[1],
                           'sensor_phase_error': errs[2], 'total_phase_error': errs[3], 'other_raw_error': max_other}
                    results.append(row)
                    if witness is None or errs[-1] > witness['total_phase_error']:
                        witness = {**row, 'raw_snapshot_codes': codes, 'exact_phase_direction': list(result['direction'])}
    assert len(results) == len(profs)*3*5*3 == 585
    replay = acq.integer_phase(iter(witness['raw_snapshot_codes']), 26, anchors, A)
    assert list(replay['direction']) == witness['exact_phase_direction']
    # Independent evaluator for the constant limiting case.
    const = lambda t: [-.011, 0., .011]
    path = scalar_path(const, 2*math.pi)
    constant_diff = max(abs(y[2*k+1]-meter.scalar_transfer(1+2*math.pi*j/128, omega=2*const(0)[k])[1])
                        for j, y in enumerate(path) for k in range(3))
    assert constant_diff < 2e-11
    save(out/'budget.json', sm.serial({'evidence':'EXACT_CONDITIONAL', 'protocol26':cert,
         'doubled_rate_failed_sufficient_bound': failed, 'zero_rate_exact_parent_recovery':True}))
    save(out/'parent_enclosure.json', enclosure)
    save(out/'numerical.json', {'evidence':'NUMERICAL_CONSTRUCTOR', 'profiles':len(profs), 'integer_windows':len(results),
         'max_total_phase_error':max(r['total_phase_error'] for r in results),
         'max_real_transfer_difference':max_X, 'max_imag_transfer_difference':max_Y,
         'max_amplitude_squared_difference':max_A, 'max_frozen_phase_difference':max_chi,
         'common_time_varying_null_checks':len(nulls), 'max_common_null_error':max(nulls),
         'constant_closed_formula_difference':constant_diff, 'convergence_checks':comparisons,
         'trajectory_scope':'binary64RK4;notintervaltrajectoryvalidation;arbitraryerrornumericalsubsetcommuting',
         'norm_tolerance':2e-9,'phase_tolerance':5e-9,'representatives':results[:3]+results[-3:]} )
    save(out/'integer_witness.json', witness)
    summary = {'status':'PASS', 'source_hashes':len(src), 'literal_rows':len(rows),
         'parent_interval_cells':enclosure['time_cells'], 'native_gain_cap':'11/1000',
         'native_gain_lipschitz_rate':'1/200000', 'phase_bound':'<1/260rad<1/250rad',
         'endpoint_visibility':'>99/100','link_visibility':'>999/1000','ADC_bits':26,
         'integer_windows':len(results),'integer_witness_replay':'PASS', 'common_null_checks':len(nulls),
         'doubled_rate_sufficient_bound':'FAIL','hardware':'NOT_MEASURED','physical_promotion':0}
    save(out/'summary.json', summary); print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
