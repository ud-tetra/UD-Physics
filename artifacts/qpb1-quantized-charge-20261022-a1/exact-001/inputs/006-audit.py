"""Exact conditional charge/impedance and finite covariance checks; no empirical data."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    'passive', ROOT / 'experiments/qpb1-passive-port/audit.py')
passive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(passive)
scale, mm, mv, dot = passive.scale, passive.mm, passive.mv, passive.dot


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def matrix_strings(matrix):
    return [[str(v) for v in row] for row in matrix]


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    fixtures = [(F(1), F(1,2), F(1)), (F(3,2), F(1,3), F(5,4)),
                (F(7,5), F(2,7), F(11,9)), (F(2,3), F(3,5), F(4,3)),
                (F(5,4), F(7,8), F(2,5)), (F(9,7), F(1,9), F(7,3))]
    scales = [F(1,3), F(1,2), F(1), F(2), F(7,3)]
    e = F(2,5)  # abstract charge coefficient, not SI elementary-charge data
    impedance = []
    for c0, cc, z in fixtures:
        c = [[c0+cc, -cc], [-cc, c0+cc]]
        ell = scale(c, z*z)
        w = scale(passive.inv2(c), 1/z)
        wbar, kappa = w[0]
        g, tau = 2*kappa/wbar, 2/wbar
        reference = z*e
        action = e*e*z
        charge = [F(0), e]
        energy = dot(charge, mv(passive.inv2(c), charge))/2
        assert action == reference*reference/z == 2*energy/wbar
        assert 0 < g < 2
        for s in scales:
            zs, cs, ls = s*z, scale(c, 1/s), scale(ell, s)
            ws = scale(passive.inv2(cs), 1/zs)
            assert ls == scale(cs, zs*zs) and ws == w
            assert 2*ws[0][1]/ws[0][0] == g and 2/ws[0][0] == tau
            assert zs*e == s*reference and e*e*zs == s*action
            es = dot(charge, mv(passive.inv2(cs), charge))/2
            assert es == s*energy
            # Independently recheck the full physical/native generator map.
            gp, _ = passive.physical(passive.inv2(cs), passive.inv2(ls))
            transform = passive.transform(zs*e, zs)
            assert mm(gp, transform) == scale(mm(transform, passive.native(g)), 1/tau)
            impedance.append({'C0':str(c0), 'Cc':str(cc), 'Z':str(z), 's':str(s),
                'charge':str(e), 'scaled_C':matrix_strings(cs), 'scaled_L':matrix_strings(ls),
                'W':matrix_strings(ws), 'g':str(g), 'tau0':str(tau),
                'action_before':str(action), 'action_after':str(e*e*zs),
                'energy_ratio':str(es/energy), 'generator_map':'PASS'})
    squeezed = []
    for chi in [F(1), F(2,3), F(7,5)]:
        for t in [F(1,4), F(1,2), F(1), F(2), F(4)]:
            u, v = chi*t/2, chi/(2*t)
            assert u*v == chi*chi/4
            excess = u+v-chi
            assert excess == chi*(t-1)**2/(2*t) >= 0
            squeezed.append({'chi':str(chi), 't':str(t), 'u':str(u), 'v':str(v),
                'covariance_action':str(u+v), 'excess_over_vacuum':str(excess)})
    correlated = []
    chi = F(1)
    for u, covariance, noise in [(F(1,2),F(0),F(0)),(F(1),F(1,2),F(0)),
                                  (F(2),F(-1,3),F(2,5)),(F(3,4),F(0),F(1))]:
        v = (covariance*covariance+chi*chi/4)/u+noise
        det = u*v-covariance*covariance
        assert u>0 and v>0 and det>=chi*chi/4
        assert (u+v)**2 >= chi*chi+4*covariance*covariance
        correlated.append({'u':str(u),'v':str(v),'c':str(covariance),'chi':str(chi),
                           'determinant':str(det),'covariance_action':str(u+v)})
    displacements = []
    chi = F(3,7)
    for z in [F(1,3),F(1,2),F(1),F(2),F(7,3)]:
        omega = F(5,2)
        c, ell = 1/(z*omega), z/omega
        var_phi, var_q = chi*z/2, chi/(2*z)
        energy = (e*e+var_q)/(2*c)+var_phi/(2*ell)
        mean_n = e*e*z/(2*chi)
        assert energy == chi*omega*(mean_n+F(1,2))
        assert 2*energy/omega == e*e*z+chi
        assert 2*(energy-chi*omega/2)/omega == e*e*z
        displacements.append({'Z':str(z),'chi':str(chi),'charge_mean':str(e),
            'mean_occupation':str(mean_n),'total_action_proxy':str(2*energy/omega),
            'excess_action_proxy':str(2*(energy-chi*omega/2)/omega)})
    number_states = []
    # Integer occupation algebra only; no finite-dimensional truncation of the CCR.
    for n in range(6):
        aa_dagger, a_dagger_a = F(n+1), F(n)
        assert aa_dagger-a_dagger_a == 1
        q2_coefficient = (aa_dagger+a_dagger_a)/2
        phi2_coefficient = q2_coefficient
        total = q2_coefficient+phi2_coefficient
        excess = total-1
        assert total == 2*n+1 and excess == 2*n
        number_states.append({'n':n, 'mean_Q':'0', 'total_action_over_chi':str(total),
                              'vacuum_subtracted_action_over_chi':str(excess)})
    # Cauchy-Schwarz forbids a zero-variance charge state at finite conjugate variance.
    assert F(0)*F(100) < F(1,4)
    dump(out/'impedance_scaling.json', impedance)
    dump(out/'quantum_moments.json', {'squeezed':squeezed,'correlated':correlated,
                                      'displaced_vacua':displacements,'number_states':number_states})
    summary = {'status':'PASS','evidence':'EXACT / CONDITIONAL',
        'impedance_comparisons':len(impedance),'squeezed_cases':len(squeezed),
        'correlated_cases':len(correlated),'displacement_cases':len(displacements),
        'number_state_cases':len(number_states),'empirical_score':'UNSCORED','physical_promotion':0,
        'scope':'Finite exact fixtures accompany the general proofs in README; no apparatus or universal action scale selected.'}
    dump(out/'summary.json', summary)
    print(json.dumps(summary))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    main(parser.parse_args().out)
