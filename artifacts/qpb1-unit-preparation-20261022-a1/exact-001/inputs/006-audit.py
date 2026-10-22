"""Exact unit-preparation countermodels; hypothetical models, no physical data."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse, importlib.util, json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('prior', ROOT/'experiments/action-normalization-audit/audit.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
mm, mv, dot, scale, add, tr, zero = prior.mm, prior.mv, prior.dot, prior.scale, prior.add, prior.tr, prior.zero


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + '\n')


def interval(C, V, omega):
    """Positive deterministic interval enclosure, not a coverage certificate."""
    pairs = [(F(lo), F(hi)) for lo, hi in (C, V, omega)]
    if any(not 0 < lo <= hi for lo, hi in pairs):
        raise ValueError('Positive ordered intervals required')
    (cl, ch), (vl, vh), (wl, wh) = pairs
    return cl*vl*vl/wh, ch*vh*vh/wl


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    simplices = [s for k in range(1, 5) for s in combinations(range(4), k)]
    ix = {s: i for i, s in enumerate(simplices)}
    d = zero(15)
    for s in simplices:
        if len(s) > 1:
            for j in range(len(s)):
                d[ix[s[:j]+s[j+1:]]][ix[s]] = F((-1)**j)
    A = add(d, scale(tr(d), -1)); J = scale(A, F(1, 2))
    P = scale(mm(A, A), F(-1, 4))
    e = [F(0)]*15; e[ix[(0, 1)]] = F(1)
    f = mv(J, e)
    assert mv(P, e) == e and dot(e, e) == dot(f, f) == 1
    assert any(v.denominator != 1 for v in f)
    assert mv(J, f) == [-v for v in e]
    rational_supports = [F(1, n*n) for n in range(1, 13)]
    assert all(a > b for a, b in zip(rational_supports, rational_supports[1:]))
    strobe = scale(prior.eye(15), -1)
    assert mm(strobe, strobe) == prior.eye(15) and mv(strobe, e) != e
    lattice = {
        'integer_branch': 'Assume Lambda=Z15 intersect imP. Nonzero squared norm is an integer >=1; active edge e attains1.',
        'quarter_phase_image_Je': [str(v) for v in f],
        'quarter_phase_leaves_integer_lattice': True,
        'rational_support_sequence': [str(a) for a in rational_supports],
        'rational_proof': 'e/n belongs to the active rational carrier for every positive integer n, so positive supports have infimum0 and no minimum.',
        'continuous_lattice_no_go': 'A continuous path in a discrete lattice is constant. Nonzero active A motion cannot remain in Lambda for all times.',
        'stroboscopic_alternative': {'native_step': 'pi/2', 'phase_step': 'pi', 'active_update': '-I', 'register': 'Z/2Z', 'nonzero_orbit_length': 2,
            'scope': 'Sampled active states only; continuous path still leaves Lambda. No physical tick or action scale follows.'}}
    save(out/'lattice_selection.json', lattice)

    # Integer preparation events do not require a lattice-valued trajectory.
    cell_seed = [F(0)]*15; cell_seed[ix[(0, 1, 2, 3)]] = F(1)
    cell_quadrature = mv(J, cell_seed)
    assert mv(P, cell_seed) == cell_seed
    assert dot(cell_seed, cell_seed) == dot(cell_quadrature, cell_quadrature) == 1
    assert dot(cell_seed, cell_quadrature) == 0
    phase_pairs = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)),
                   (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
                   (F(5, 13), F(12, 13)), (F(-5, 13), F(12, 13))]
    kicks = []
    for c, s in phase_pairs:
        assert c*c+s*s == 1
        x = [c*u+s*v for u, v in zip(cell_seed, cell_quadrature)]
        after = [u+v for u, v in zip(x, cell_seed)]
        assert dot(x, x) == 1 and dot(after, after) == 2+2*c
        assert dot(after, after)-dot(x, x) == 1+2*dot(x, cell_seed)
        kicks.append({'cos_phase': str(c), 'sin_phase': str(s), 'support_after_two_unit_kicks': str(dot(after, after))})
    save(out/'event_preparation.json', {
        'rule': 'Assume an external preparation/reset x=0 followed by x_plus=e_cell. Subsequent continuous real Hodge flow has support1.',
        'status': 'ADDED_SOURCE_HYPOTHESIS',
        'lattice_obstruction_scope': 'A lattice restriction only at preparation does not conflict with continuous real motion afterward.',
        'general_injection_balance': 'Delta_a=||u||^2+2<x,u>; for a unit cell kick, Delta_a=1+2*x_cell.',
        'two_kick_cases': kicks,
        'scope': 'Event count is not additive support without extra orthogonality/phase/source conditions. Reset,source energy,phase reference and physical kick magnitude are not derived.'})

    feedback_checks = 0
    gamma = F(3, 7)
    for a0 in [F(1, 16), F(1, 4), F(1), F(4)]:
        k = 1/a0 - 1
        for z in [F(1), F(1, 2), F(1, 8)]:
            a = 1/(1+k*z)
            derivative = 2*gamma*k*z/(1+k*z)**2
            assert derivative == 2*gamma*a*(1-a)
            assert min(a0, 1) <= a <= max(a0, 1)
            feedback_checks += 1
    for q, p in [(F(1, 2), F(0)), (F(2), F(0)), (F(3, 5), F(4, 5)), (F(1, 3), F(2, 3))]:
        a = q*q+p*p
        dq, dp = -2*p+gamma*(1-a)*q, 2*q+gamma*(1-a)*p
        assert 2*(q*dq+p*dp) == 2*gamma*a*(1-a)
        assert q*dp-p*dq == 2*a
        feedback_checks += 1
    save(out/'feedback_selection.json', {
        'model': 'On active sector, x_prime=A*x+gamma*(1-||x||^2)*x; gamma>0 is an added feedback law.',
        'support_equation': 'a_prime=2*gamma*a*(1-a)',
        'solution_for_a0_positive': 'a(s)=1/[1+(1/a0-1)*exp(-2*gamma*s)]',
        'positive_support_limit': '1', 'zero_state': 'fixed and not attracted to support1',
        'phase_rate': '2', 'exact_checks': feedback_checks,
        'scope': 'Conditional added nonlinear, nonconservative source/sink model; not imported native dynamics. Native norm selection does not determine physical L.'})

    # Ideal isolated single-mode LC equations: Phi_dot=Q/C, Q_dot=-Phi/ell.
    families = []; map_checks = 0
    for C, V, w in [(F(1), F(1), F(2)), (F(3, 2), F(2, 3), F(5, 4)),
                    (F(7, 5), F(11, 9), F(13, 7)), (F(2, 7), F(3, 5), F(4, 3))]:
        ell = 1/(C*w*w); Phi_ref = V/w
        action = C*V*V/w; E = C*V*V/2
        T = [[Phi_ref, F(0)], [F(0), -C*w*Phi_ref]]
        native = [[F(0), -w], [w, F(0)]]
        physical = [[F(0), 1/C], [-1/ell, F(0)]]
        assert mm(physical, T) == mm(T, native)
        assert action == C*w*Phi_ref*Phi_ref == 2*E/w
        for X, Y, dX, dY in [(F(1), F(0), F(0), F(1)), (F(2, 3), F(4, 5), F(5, 7), F(6, 11))]:
            Phi, Q = Phi_ref*X, -C*w*Phi_ref*Y
            dPhi, dQ = Phi_ref*dX, -C*w*Phi_ref*dY
            assert (Q*dPhi-Phi*dQ)/2 == action*(X*dY-Y*dX)/2
            assert Q*Q/(2*C)+Phi*Phi/(2*ell) == E*(X*X+Y*Y)
        ratios=[]
        for r in [F(1, 2), F(1), F(2), F(3)]:
            voltage = r*V
            assert C*voltage*voltage/w == r*r*action
            # Fixed map: preparation Phi=0,Q=C*r*V corresponds to X=0,Y=-r.
            assert (-(C*voltage)/(C*w*Phi_ref))**2 == r*r
            ratios.append({'voltage_ratio': str(r), 'support_under_fixed_map': str(r*r), 'loop_action_ratio': str(r*r)})
            map_checks += 1
        families.append({'C': str(C), 'ell': str(ell), 'omega': str(w), 'precharge_V_ref': str(V),
                         'Phi_ref': str(Phi_ref), 'E_ref': str(E), 'J_LC': str(action), 'controls': ratios})
    # Physical-unit exponent order M,L,T,I. Capacitance is not mass.
    cap = (-1, -2, 4, 2); volt = (1, 2, -3, -1); freq = (0, 0, -1, 0)
    units = tuple(cap[i]+2*volt[i]-freq[i] for i in range(4))
    assert units == (1, 2, -1, 0) and cap != (1, 0, 0, 0)
    lo, hi = interval(('99/100', '101/100'), ('999/1000', '1001/1000'), ('199/100', '201/100'))
    assert lo <= F(1, 2) <= hi
    for C in [F(99, 100), F(101, 100)]:
        for V in [F(999, 1000), F(1001, 1000)]:
            for w in [F(199, 100), F(201, 100)]:
                assert lo <= C*V*V/w <= hi
    for bad in [(('0','1'),('1','1'),('1','1')), (('1','1'),('2','1'),('1','1'))]:
        try:
            interval(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid interval admitted')
    target_action = F(7, 11)
    voltage_squared_from_target = target_action*F(2)/F(3)
    assert F(3)*voltage_squared_from_target/F(2) == target_action
    save(out/'lc_preparation.json', {'families': families, 'preparation_ratio_checks': map_checks,
         'action_units_M_L_T_I': units, 'interval_example_J_s': [str(lo), str(hi)],
         'interval_vertex_checks': 8, 'invalid_interval_controls': 2,
         'target_backsolve_identity': 'If V_ref^2=J_target*omega/C, then J_LC=J_target by construction; inadmissible as independent test.',
         'empirical_status': 'NOT_EXECUTED_UNSCORED',
         'scope': 'Exact ideal single-mode classical equations and conditional one-active-plane map. Not a measured circuit, full C7 implementation or quantum identification.'})
    summary = {'status': 'EXACT_CONDITIONAL_UNIT_PREPARATION_AUDIT_PASS',
        'lattice': 'Minimum1 only after a new integer-amplitude restriction; incompatible with nonstatic continuous active flow.',
        'event_preparation': 'Integer unit preparation at reset can coexist with later real flow; repeated unit kicks have phase-dependent support, not additive event count.',
        'feedback': 'Added nonlinear law selects native support1 for a0>0 but leaves physical unit scale open.',
        'physical_preparation': 'Independent chosen precharge V_ref gives J_LC=C*V_ref^2/omega in the ideal classical map.',
        'universality_control': 'With V_ref fixed, doubling actual preparation voltage multiplies support and loop action by4; the map scale remains fixed. Choosing a new reference voltage instead defines a different map scale proportional to V_ref^2.',
        'readout': 'Voltage/current resolve classical phase. They are not fixed isolated Born effects on the normalized intrinsic C7 ray.',
        'next_discriminant': 'Source a native-to-physical preparation law that fixes the unit reference and remains consistent across voltage/amplitude interventions, or explicitly limit the bridge to a calibrated analogue.',
        'physical_promotion': 0, 'empirical_status': 'UNSCORED', 'independent_review': 'NOT_PERFORMED'}
    save(out/'results.json', summary)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--out', type=Path, required=True)
    main(p.parse_args().out)
