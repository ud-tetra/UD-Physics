"""Constructor exact checks: complete connection, action, gauge and detuned rays.

Standard-library only. Analytic all-state proofs and trigonometric integrals are
in README.md; finite rational fixtures verify implementations, not universality.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    'action_helpers', ROOT / 'experiments/action-normalization-audit/audit.py')
alg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alg)
mm, mv, tr, dot = alg.mm, alg.mv, alg.tr, alg.dot
add, scale, rank = alg.add, alg.scale, alg.rank
vadd = lambda x, y: [a + b for a, b in zip(x, y)]
vs = lambda c, x: [c * a for a in x]
save = lambda p, x: p.write_text(json.dumps(x, indent=2) + '\n')


def carrier():
    simplices = [s for k in range(1, 5) for s in combinations(range(4), k)]
    ix = {s: i for i, s in enumerate(simplices)}
    d = alg.zero(15)
    for s in simplices:
        if len(s) > 1:
            for j in range(len(s)):
                d[ix[s[:j] + s[j+1:]]][ix[s]] = F((-1)**j)
    A = add(d, scale(tr(d), -1))
    J = scale(A, F(1, 2))
    P = scale(mm(A, A), F(-1, 4))
    E = alg.zero(15)
    for s in simplices:
        if len(s) == 2:
            E[ix[s]][ix[s]] = F(1)
    V = add(E, mm(mm(J, E), tr(J)))
    H = add(P, scale(V, -1))
    return simplices, A, J, P, E, V, H


def representation(simplices, perm):
    ix = {s: i for i, s in enumerate(simplices)}
    R = alg.zero(15)
    for j, s in enumerate(simplices):
        image = [perm[i] for i in s]
        inversions = sum(image[i] > image[k]
                         for i in range(len(s)) for k in range(i+1, len(s)))
        R[ix[tuple(sorted(image))]][j] = F((-1)**inversions)
    return R


def alpha(J, x, v):
    a = dot(x, x)
    if a <= 0:
        raise ValueError('Connection undefined at zero')
    return dot(mv(J, x), v) / a


def theta(J, x, v):
    return dot(mv(J, x), v) / 2


def curvature(J, x, u, v):
    a = dot(x, x)
    return (2 * dot(mv(J, u), v) / a
            - 2 * (dot(x, u) * dot(mv(J, x), v)
                   - dot(x, v) * dot(mv(J, x), u)) / a**2)


def directional_alpha(J, x, v, u):
    """Exact quotient-rule derivative D_u[alpha_x(v)], v constant."""
    a = dot(x, x)
    return dot(mv(J, u), v)/a - 2*dot(x, u)*dot(mv(J, x), v)/a**2


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    sources = json.loads((here / 'SOURCES.json').read_text())
    for s in sources['sources']:
        assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256']
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
    byid = {r['id']: r for r in ledger['rows']}
    assert all(byid[r['id']] == r for r in rows)
    simp, A, J, P, E, V, H = carrier()
    assert tr(A) == scale(A, -1) and mm(J, J) == scale(P, -1)
    assert mm(tr(J), J) == P and rank(P) == 14
    assert rank(V) == 12 and rank(H) == 2 and mm(V, H) == alg.zero(15)
    basis = [[F(i == j) for i in range(15)] for j in range(15)]
    active_basis = [mv(P, e) for e in basis]
    u = basis[simp.index((0, 1))]
    h = basis[simp.index((0, 1, 2, 3))]
    Ju, Jh = mv(J, u), mv(J, h)
    frame = [u, Ju, h, Jh]
    assert [[dot(x, y) for y in frame] for x in frame] == alg.eye(4)
    fixtures = [u, h, vadd(u, h)]
    fixtures += [mv(P, [F(((i+1)*(k+2)) % 11 - 5, k+1)
                        for i in range(15)]) for k in range(7)]
    assert all(dot(x, x) > 0 and mv(P, x) == x for x in fixtures)
    gauge_checks = 0
    curvature_checks = 0
    ranks = []
    for x in fixtures:
        jx = mv(J, x)
        a = dot(x, x)
        assert alpha(J, x, x) == 0 and alpha(J, x, jx) == 1
        assert theta(J, x, mv(A, x)) == a
        assert alpha(J, x, mv(A, x)) == 2
        # Rational U(1) rotations, time-dependent phase and radial scaling.
        for t in [F(-2), F(-1, 3), F(0), F(1, 2), F(3)]:
            c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
            R = add(scale(P, c), scale(J, s))
            for v in [u, h, mv(A, x)]:
                for rate in [F(-3, 2), F(0), F(2)]:
                    rad, drad = F(3, 2), F(-2, 3)
                    y = vs(rad, mv(R, x))
                    dy = vadd(vs(rad, mv(R, vadd(v, vs(rate, jx)))),
                              vs(drad, mv(R, x)))
                    assert alpha(J, y, dy) == alpha(J, x, v) + rate
                    assert theta(J, y, dy) == rad**2*(theta(J, x, v)+a*rate/2)
                    gauge_checks += 1
        Fmat = [[curvature(J, x, v, w) for w in active_basis]
                for v in active_basis]
        assert tr(Fmat) == scale(Fmat, -1) and rank(Fmat) == 12
        ranks.append(rank(Fmat))
        for v in active_basis:
            assert curvature(J, x, x, v) == curvature(J, x, jx, v) == 0
            for w in active_basis:
                assert curvature(J, x, v, w) == (
                    directional_alpha(J, x, w, v)-directional_alpha(J, x, v, w))
                curvature_checks += 1
    assert curvature(J, u, h, Jh) == 2
    assert mv(E, h) == mv(E, Jh) == [F(0)]*15
    symmetry_checks = 0
    for perm in permutations(range(4)):
        R = representation(simp, perm)
        assert mm(tr(R), R) == alg.eye(15)
        assert mm(R, J) == mm(J, R)
        assert mm(R, H) == mm(H, R) and mm(R, V) == mm(V, R)
        for x in fixtures:
            for v in [u, h]:
                assert alpha(J, mv(R, x), mv(R, v)) == alpha(J, x, v)
                assert curvature(J, mv(R, x), mv(R, v), mv(R, Ju)) == curvature(J, x, v, Ju)
                symmetry_checks += 1
    detuned = []
    rate_pairs = [(F(2), F(3)), (F(3), F(2)), (F(1, 3), F(7, 5))]
    for wv, wh in rate_pairs:
        G = mm(J, add(scale(V, wv), scale(H, wh)))
        assert tr(G) == scale(G, -1)
        assert mm(G, J) == mm(J, G)
        assert mm(G, V) == mm(V, G) and mm(G, H) == mm(H, G)
        for x in fixtures:
            av, ah = dot(mv(V, x), mv(V, x)), dot(mv(H, x), mv(H, x))
            a = av + ah
            r = ah/a
            assert a == dot(x, x)
            assert alpha(J, x, mv(G, x)) == (wv*av+wh*ah)/a
            assert theta(J, x, mv(G, x)) == (wv*av+wh*ah)/2
            delta = wh-wv
            T_over_pi = 2/abs(delta)
            endpoint_over_2pi = wv/abs(delta)
            int_alpha_over_2pi = (wv+delta*r)/abs(delta)
            hol_turns = endpoint_over_2pi-int_alpha_over_2pi
            assert hol_turns == -(1 if delta > 0 else -1)*r
            detuned.append({'omega_visible': str(wv), 'omega_hidden': str(wh),
                            'support': str(a), 'hidden_fraction': str(r),
                            'projective_period_over_pi': str(T_over_pi),
                            'holonomy_turns_mod1': str(hol_turns % 1),
                            'raw_action_over_pi': str((wv*av+wh*ah)*T_over_pi/2)})
    assert mm(J, add(scale(V, 2), scale(H, 2))) == A
    # Closed representative of a constant ray with gauge winding m.
    # alpha integral=2pi*m; beta integral=pi*m: beta exponential changes sign.
    loops = []
    for a in [F(1, 4), F(1), F(2), F(9, 4)]:
        for n in range(-3, 4):
            loops.append({'support': str(a), 'winding': n,
                          'raw_action_over_pi': str(a*n),
                          'connection_integral_over_2pi': n,
                          'projective_holonomy': '+1',
                          'half_connection_exponential': '+1' if n % 2 == 0 else '-1'})
    # Unit reference (u+h)/sqrt(2); proof uses norm bounds, not sampling.
    eps = F(1, 10)
    bound = (2*eps+eps**2)/(2*(1-eps)**2)
    lower, upper = F(1, 2)-bound, F(1, 2)+bound
    assert (bound, lower, upper) == (F(7, 54), F(10, 27), F(17, 27))
    assert F(1, 3) < lower <= upper < F(2, 3)
    try:
        alpha(J, [F(0)]*15, u)
    except ValueError:
        zero_rejected = True
    else:
        raise AssertionError('zero must be rejected')
    save(out/'connection.json', {'carrier_dimension': 15, 'active_rank': rank(P),
         'visible_rank': rank(V), 'hidden_rank': rank(H),
         'gauge_fixture_checks': gauge_checks, 'S4_readout_checks': symmetry_checks,
         'curvature_derivative_checks': curvature_checks, 'curvature_ranks': ranks,
         'hidden_plane_curvature_at_edge_state': '2', 'zero_rejected': zero_rejected,
         'CP1_flux_over_2pi': '1 (analytic patch calculation in README)',
         'normalization': 'alpha=<Jx,dx>/a=2Theta/a; alpha(Jx)=1'})
    save(out/'loops.json', {'native_loops': loops, 'detuned_loops': detuned,
         'detuned_law': 'G=J(omega_v P_visible+omega_h P_hidden), added hypothesis',
         'sign_convention': 'Hol=exp(i*(endpoint_phase-integral(alpha)))',
         'weight_rule': 'integer w; eta/2=w only on imposed unit-support physical phase map',
         'variable_support_small_gauge_witness': 'a=2+cos(t),chi=sin(t),0..2pi; Delta integral Theta=pi/2'})
    save(out/'robustness.json', {'reference': '(unit_edge01+unit_topcell)/sqrt(2)',
         'active_perturbation_norm_bound': str(eps),
         'hidden_fraction_error_bound': str(bound), 'hidden_fraction_interval': [str(lower), str(upper)],
         'holonomy_distance_from_one_lower_bound': 'sqrt(3)',
         'scope': 'all active perturbations in this ball; fixed nonzero detuning; ideal declared connection',
         'not_proved': ['physical phase readout', 'physical action scale', 'detuning selection',
                        'quantized -1 on a neighborhood', 'finite-time noise/measurement bound']})
    result = {'status': 'PASS', 'source_hashes': len(sources['sources']),
              'selected_source_rows': len(rows), 'active_visible_hidden_ranks': [14, 12, 2],
              'state_fixtures': len(fixtures), 'gauge_checks': gauge_checks,
              'S4_actions': 24, 'S4_readout_checks': symmetry_checks,
              'curvature_derivative_checks': curvature_checks,
              'curvature_rank': 12, 'native_loop_receipts': len(loops),
              'detuned_loop_receipts': len(detuned), 'exact_robustness_radius': str(eps),
              'physical_score': 'UNSCORED', 'physical_promotion': 0}
    save(out/'summary.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    main(parser.parse_args().out)
