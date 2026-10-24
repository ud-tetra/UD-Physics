"""Exact bounds and separately labeled floating constructor cross-checks.

No empirical data. Snapshot phase uses endpoint/adjacent overlaps, not a
nominal-rate subtraction. General proofs and acquisition premises are in README.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import argparse
import cmath
import hashlib
import importlib.util
import json
import math
import random

ROOT = Path(__file__).resolve().parents[2]
sp = importlib.util.spec_from_file_location(
    'local', ROOT/'experiments/qpb1-local-generators/audit.py')
local = importlib.util.module_from_spec(sp)
sp.loader.exec_module(local)
phase, alg = local.phase, local.alg
mv, dot = alg.mv, alg.dot
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')
cmul = lambda z, w: (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
conj = lambda z: (z[0], -z[1])


def circle(t):
    return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def budget():
    eps, h, M = F(1, 100), F(1, 100), 128
    Tmax = F(44, 7)+h  # pi<22/7, proved by positive integral in README.
    D = h/2+2*eps*Tmax
    v = 1-D*D/2
    gain = D**3/(3*v)
    step = F(13, 25)*Tmax/M
    vl = 1-step*step/2
    discrete = M*step**3/(3*vl)
    ze, zl = F(1, 1000), F(1, 1000000)
    acquisition = ze/(v-ze)+M*zl/(vl-zl)
    total = gain+discrete+acquisition
    assert D == F(2291, 17500)
    assert v-ze > F(99, 100) and vl-zl > F(999, 1000)
    assert gain < F(1, 1000) and discrete < F(1, 1000)
    assert total < F(1, 250)
    assert F(173, 100)**2 < 3 and F(173, 100)-F(1, 250) > F(17, 10)
    return dict(gain_error=eps, timing_error=h, snapshot_links=M,
                time_upper=Tmax, halfspread_upper=D, visibility_lower=v,
                gain_phase_error=gain, step_halfspread_upper=step,
                link_visibility_lower=vl, discrete_phase_error=discrete,
                endpoint_overlap_error=ze, link_overlap_error=zl,
                acquisition_phase_error=acquisition, total_phase_error=total)


def finite_phase(endpoint, links, endpoint_floor=.99, link_floor=.999):
    """Streaming equivalent needs initial/previous/current state and one phasor."""
    if abs(endpoint) <= endpoint_floor or any(abs(z) <= link_floor for z in links):
        return None
    q = endpoint/abs(endpoint)
    for z in links:
        q *= (z/abs(z)).conjugate()
    return q/abs(q)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    sources = json.loads((here/'SOURCES.json').read_text())
    for s in sources['sources']:
        assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256']
    byid = {r['id']: r for r in json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())['rows']}
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    assert all(byid[r['id']] == r for r in rows)
    b = budget()
    # All rational moment fixtures supplement the general variance/Taylor proof.
    D = b['halfspread_upper']
    moment_checks = 0
    for i in range(9):
        for j in range(9-i):
            r = [F(i, 8), F(j, 8), F(8-i-j, 8)]
            for delta in product([-D, -D/2, F(0), D/2, D], repeat=3):
                mean = sum(a*t for a, t in zip(r, delta))
                e = [t-mean for t in delta]
                var = sum(a*t*t for a, t in zip(r, e))
                third = sum(a*abs(t)**3 for a, t in zip(r, e))
                assert sum(a*t for a, t in zip(r, e)) == 0
                assert var <= D*D and third <= 2*D*var
                moment_checks += 1
    simp, A, J, P, edge, visible, hidden = phase.carrier()
    K = [alg.zero(15) for _ in range(3)]
    for i, s in enumerate(simp):
        for j, t in enumerate(simp):
            if len(t) == len(s)+1 and A[i][j]:
                K[len(t)-2][i][j] = A[i][j]
                K[len(t)-2][j][i] = -A[i][j]
    sectors = [alg.scale(alg.mm(k, k), F(-1, 4)) for k in K]
    basis = [[F(i == j) for i in range(15)] for j in range(15)]
    u, top = basis[simp.index((0, 1))], basis[simp.index((0, 1, 2, 3))]
    frame = [basis[i] for i, s in enumerate(simp) if len(s) == 2]
    frame += [mv(J, x) for x in frame[:]]
    frame += [top, mv(J, top)]
    assert [[dot(x, y) for y in frame] for x in frame] == alg.eye(14)
    coh = lambda x, y: (dot(x, y), dot(mv(J, x), y))
    rot = lambda x, z: [z[0]*a+z[1]*c for a, c in zip(x, mv(J, x))]
    states = [u, [F(3, 5)*a+F(4, 5)*c for a, c in zip(u, top)],
              [F(3, 5)*a+F(4, 5)*c for a, c in zip(u, mv(J, top))],
              [F(4, 5)*a+F(3, 5)*c for a, c in zip(u, top)]]
    def bargmann(ys):
        v = coh(ys[0], ys[-1])
        for x, y in zip(ys, ys[1:]):
            v = cmul(v, conj(coh(x, y)))
        return v
    B0 = bargmann(states)
    gauge_exact = 0
    for ts in product([F(-2), F(-1, 3), F(0), F(1, 2), F(3)], repeat=4):
        assert bargmann([rot(x, circle(t)) for x, t in zip(states, ts)]) == B0
        gauge_exact += 1
    for perm in permutations(range(4)):
        R = phase.representation(simp, perm)
        assert bargmann([mv(R, x) for x in states]) == B0
    # Numeric campaign is an implementation check, not the continuous proof.
    jf = [[float(v) for v in row] for row in J]
    pf = [[[float(v) for v in row] for row in p] for p in sectors]
    mf = lambda m, x: [sum(a*t for a, t in zip(row, x)) for row in m]
    df = lambda x, y: sum(a*c for a, c in zip(x, y))
    cf = lambda x, y: complex(df(x, y), df(mf(jf, x), y))
    rf = lambda x, t: [math.cos(t)*a+math.sin(t)*c for a, c in zip(x, mf(jf, x))]
    reference = [(float(a)+float(c))/math.sqrt(2) for a, c in zip(u, top)]
    preparations = [reference]
    for x in frame:
        for sign in [-1, 1]:
            preparations.append([a+sign*.1*float(c) for a, c in zip(reference, x)])
    rng = random.Random(20261023)
    for _ in range(16):
        coeff = [rng.uniform(-1, 1) for _ in range(14)]
        norm = math.sqrt(sum(t*t for t in coeff))
        delta = [sum(t*float(v[i]) for t, v in zip(coeff, frame))/norm for i in range(15)]
        preparations.append([a+.1*c for a, c in zip(reference, delta)])
    M = b['snapshot_links']
    results = []
    min_endpoint = min_link = min_observed_endpoint = min_observed_link = 1.
    max_matrix_error = max_gauge_error = max_ideal_error = max_observed_error = 0.
    worst_observed_case = None
    acquisition_checks = 0
    for prep_id, prep in enumerate(preparations):
        norm = math.sqrt(df(prep, prep))
        y = [v/norm for v in prep]
        components = [mf(p, y) for p in pf]
        jcomponents = [mf(jf, x) for x in components]
        r = [df(y, x) for x in components]
        assert abs(sum(r)-1) < 2e-14
        assert float(F(10, 27))-2e-14 <= r[2] <= float(F(17, 27))+2e-14
        baseline = cmath.exp(-2j*math.pi*r[2])
        for offsets in product([-.01, 0., .01], repeat=3):
            gains = [1+offsets[0], 1+offsets[1], 1.5+offsets[2]]
            for time_error in [-.01, 0., .01]:
                T = 2*math.pi+time_error
                lam = [2*g*T for g in gains]
                mean = sum(a*t for a, t in zip(r, lam))
                yt = [sum(math.cos(t)*x[i]+math.sin(t)*jx[i]
                          for t, x, jx in zip(lam, components, jcomponents)) for i in range(15)]
                endpoint = cf(y, yt)
                analytic_z = sum(a*cmath.exp(1j*t) for a, t in zip(r, lam))
                max_matrix_error = max(max_matrix_error, abs(endpoint-analytic_z))
                ideal = endpoint/abs(endpoint)*cmath.exp(-1j*mean)
                zg = cf(rf(y, .37), rf(yt, -1.12))
                gauge_z = zg*cmath.exp(-1j*(mean-1.12-.37))
                max_gauge_error = max(max_gauge_error, abs(gauge_z-endpoint*cmath.exp(-1j*mean)))
                link = sum(a*cmath.exp(1j*t/M) for a, t in zip(r, lam))
                snapshot = finite_phase(endpoint, [link]*M)
                assert snapshot is not None
                ideal_err = abs(cmath.phase(ideal/baseline))
                sampled_err = abs(cmath.phase(snapshot/baseline))
                max_ideal_error = max(max_ideal_error, ideal_err)
                assert ideal_err <= float(b['gain_phase_error'])+5e-12
                assert sampled_err <= float(b['gain_phase_error']+b['discrete_phase_error'])+5e-12
                min_endpoint, min_link = min(min_endpoint, abs(endpoint)), min(min_link, abs(link))
                for ang in [k*math.pi/4 for k in range(8)]:
                    noisy_end = endpoint+.001*cmath.exp(1j*ang)
                    for direction in [1+0j, -1+0j, 1j, -1j]:
                        noisy_link = link+1e-6*direction*link/abs(link)
                        q = finite_phase(noisy_end, [noisy_link]*M)
                        assert q is not None
                        error = abs(cmath.phase(q/baseline))
                        assert error <= float(b['total_phase_error'])+5e-12
                        assert abs(q-1) > 1.7
                        if error > max_observed_error:
                            max_observed_error = error
                            worst_observed_case = {'preparation': prep_id, 'offsets': list(offsets),
                                'time_error': time_error, 'endpoint_noise_angle': ang,
                                'link_noise_direction': [direction.real, direction.imag], 'phase_error': error}
                        min_observed_endpoint = min(min_observed_endpoint, abs(noisy_end))
                        min_observed_link = min(min_observed_link, abs(noisy_link))
                        acquisition_checks += 1
                results.append({'preparation': prep_id, 'offsets': list(offsets),
                                'time_error': time_error, 'endpoint_visibility': abs(endpoint),
                                'link_visibility': abs(link), 'ideal_phase_error': ideal_err,
                                'snapshot_phase_error': sampled_err})
    assert max_matrix_error < 5e-12 and max_gauge_error < 5e-12
    # Independently form full 15-register snapshot overlaps for bounded drift.
    drift_records = []
    for trial in range(16):
        prep = preparations[trial]
        norm = math.sqrt(df(prep, prep)); y = [v/norm for v in prep]
        comp = [mf(p, y) for p in pf]; jc = [mf(jf, x) for x in comp]
        r = [df(y, x) for x in comp]
        T = 2*math.pi+[-.01, 0., .01][trial % 3]; dt = T/M
        angles = [0.]*3; ys = [y]; integral = 0.
        for j in range(M):
            gains = [base+.01*[-1, 0, 1][(j*(k+1)+trial+k) % 3]
                     for k, base in enumerate([1., 1., 1.5])]
            step_angles = [2*g*dt for g in gains]
            integral += sum(a*t for a, t in zip(r, step_angles))
            angles = [a+t for a, t in zip(angles, step_angles)]
            ys.append([sum(math.cos(t)*x[i]+math.sin(t)*jx[i]
                           for t, x, jx in zip(angles, comp, jc)) for i in range(15)])
        endpoint = cf(ys[0], ys[-1]); links = [cf(x, y1) for x, y1 in zip(ys, ys[1:])]
        q = finite_phase(endpoint, links); assert q is not None
        base_q = cmath.exp(-2j*math.pi*r[2])
        error = abs(cmath.phase(q/base_q))
        assert error <= float(b['gain_phase_error']+b['discrete_phase_error'])+5e-12
        ideal = endpoint/abs(endpoint)*cmath.exp(-1j*integral)
        assert abs(cmath.phase(q/ideal)) <= float(b['discrete_phase_error'])+5e-12
        drift_records.append({'trial': trial, 'full_state_snapshots': len(ys),
                              'visibility': abs(endpoint), 'phase_error': error})
    assert finite_phase(0j, [1+0j]*M) is None
    assert finite_phase(1+0j, [0j]+[1+0j]*(M-1)) is None
    assert finite_phase(.99+0j, [1+0j]*M) is None
    assert finite_phase(1+0j, [.999+0j]+[1+0j]*(M-1)) is None
    save(out/'certificate.json', {'evidence': 'EXACT_CONDITIONAL',
         'fractions': {k: str(v) for k, v in b.items()},
         'decimal_readability_only': {k: float(v) for k, v in b.items()},
         'moment_fixtures': moment_checks, 'exact_polygon_gauge_fixtures': gauge_exact,
         'S4_polygon_checks': 24, 'preparation_ball_radius': '1/10',
         'hidden_support_interval': ['10/27', '17/27'],
         'measured_phase_circular_error_bound': '1/250 rad relative to exp(-2pi*i*r_hidden)',
         'nontrivial_phase_chord_bound': '|Qhat-1|>17/10',
         'requirements': ['full active-carrier normalized snapshots', 'consistent complex/J overlap frame',
                          'bounded absolute complex overlap errors', 'bounded commuting gain drift and sample gaps'],
         'physical_score': 'UNSCORED', 'physical_promotion': 0})
    save(out/'numerical.json', {'evidence': 'NUMERICAL_CONSTRUCTOR', 'precision': 'standard-library binary64; no interval claim',
         'comparison_tolerance': 5e-12, 'preparations': len(preparations), 'constant_parameter_cases': len(results),
         'acquisition_error_cases': acquisition_checks, 'minimum_endpoint_visibility': min_endpoint,
         'minimum_link_visibility': min_link, 'minimum_observed_endpoint_visibility': min_observed_endpoint,
         'minimum_observed_link_visibility': min_observed_link, 'maximum_matrix_formula_error': max_matrix_error,
         'maximum_gauge_error': max_gauge_error, 'maximum_ideal_phase_error': max_ideal_error,
         'maximum_observed_phase_error': max_observed_error, 'worst_observed_case': worst_observed_case,
         'bounded_drift_cases': drift_records, 'representative_constant_cases': results[:4]+results[-4:],
         'capture_scope': 'Aggregate extrema, worst case and representative receipts; complete deterministic grid regenerated by audit'})
    save(out/'negative_controls.json', {'visibility_zero': 'Balanced visible/hidden reference at T=pi gives z=0 exactly; phase undefined',
         'nominal_correction_failure': 'Common gain error c at T=2pi shifts endpoint phase by4pi*c; actual correction cancels, nominal-only correction leaves first-order error',
         'nominal_correction_c': '1/100', 'nominal_only_phase_error_rad': 4*math.pi/100,
         'native_null': 'g1=g2=g3=1 gives ideal and exact snapshot Q=1 for any window with defined overlaps',
         'scope_limits': ['no arbitrary noncommuting/mode-mixing error certificate', 'no physical apparatus or clock calibration',
                          'finite phase is modulo2pi, not lifted action or winding reconstruction']})
    summary = {'status': 'PASS', 'source_hashes': len(sources['sources']), 'selected_rows': len(rows),
               'exact_moment_checks': moment_checks, 'exact_gauge_checks': gauge_exact, 'S4_checks': 24,
               'snapshots_per_window': M+1, 'numerical_constant_cases': len(results),
               'numerical_acquisition_cases': acquisition_checks, 'numerical_drift_cases': len(drift_records),
               'certified_phase_error_rad': '1/250', 'certified_observed_endpoint_visibility': '>99/100',
               'certified_observed_link_visibility': '>999/1000',
               'physical_score': 'UNSCORED', 'physical_promotion': 0}
    save(out/'summary.json', summary)
    print(json.dumps(summary))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
