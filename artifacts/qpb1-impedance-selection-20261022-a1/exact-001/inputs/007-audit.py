"""Reproducible source screening and exact dimensional/anchor checks.

Lexical coverage is not a semantic proof that no source law can exist.
No external apparatus data, hbar value or empirical fit is used.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'action', ROOT/'experiments/action-normalization-audit/audit.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
rank, dot = prior.rank, prior.dot


def save(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    sources = json.loads((HERE/'SOURCES.json').read_text())
    for source in sources['local_sources']:
        assert sha(ROOT/source['path']) == source['sha256']
    for source in sources['remote_sources']:
        if source['local'] is not None:
            p = ROOT/source['local']
            assert sha(p) == source['sha256'] and git_blob(p) == source['sha']
    excerpts = json.loads((HERE/'sources/MANUSCRIPT_EXCERPTS.json').read_text())
    assert len(excerpts) == 2
    for excerpt in excerpts:
        for section in excerpt['ranges']:
            assert len(section['text'].split('\n')) == section['last_line']-section['first_line']+1
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
    rows = ledger['rows']
    assert len(rows) == len({r['id'] for r in rows}) == ledger['typed_objects'] == 723
    byid = {row['id']:row for row in rows}
    terms = ['impedance','admittance','capacitance','inductance','permittivity','permeability',
             'coulomb','ampere','farad','henry','weber','ohm','volt','electromagnetic',
             'electric charge','elementary charge']
    hits = {term:[r['id'] for r in rows if re.search(r'\b'+re.escape(term)+r'\b',json.dumps(r),re.I)]
            for term in terms}
    charge_hits = [r['id'] for r in rows if re.search(r'\bcharge\b',json.dumps(r),re.I)]
    assert all(not ids for ids in hits.values())
    assert charge_hits == ['Q344','Q371','Q392']
    selected_ids = ['C06','O10','O14','O15','Q169','Q170','Q171','Q172','Q177','Q178','Q179',
                    'Q282','Q283','Q284','Q285','Q286','Q287','Q288','Q344','Q371','Q392','Q466','Q467']
    selected = json.loads((HERE/'SOURCE_ROWS.json').read_text())['selected_rows']
    assert selected == [byid[k] for k in selected_ids]
    assert byid['C06']['exact_form'] == '7/960'
    assert 'physical coupling interpretation is frozen' in byid['C06']['reconciliation_notes']
    assert byid['O10']['exact_form'] == 'A_0 = B_0 a_0^2 / tau_0'
    assert 'NUMERICAL VALUE OPEN' in byid['O14']['status']
    assert byid['Q287']['claim_bin'] == byid['Q288']['claim_bin'] == 'QUARANTINED_CANDIDATE'
    save(out/'source_screen.json', {'rows_screened':723,'electrical_terms':hits,'charge_alias_hits':charge_hits,
         'selected_rows_checked':len(selected),'scope':'Lexical screening and named row checks; not a global source theorem.'})
    # Dimension vectors ordered M,L,T,Q. Native three-unit columns have no charge row.
    mass = [F(1),F(0),F(0),F(0)]
    length = [F(0),F(1),F(0),F(0)]
    time = [F(0),F(0),F(1),F(0)]
    charge = [F(0),F(0),F(0),F(1)]
    action = [F(1),F(2),F(-1),F(0)]
    impedance = [F(1),F(2),F(-1),F(-2)]
    energy = [F(1),F(2),F(-2),F(0)]
    speed = [F(0),F(1),F(-1),F(0)]
    assert rank([mass,length,time]) == 3
    assert rank([mass,length,time,impedance]) == 4
    assert [action[i]-2*charge[i] for i in range(4)] == impedance
    # (rows, action certificate, unit-impedance certificate); absent certificates use a kernel witness.
    scenarios = [('charge',[charge],None,None),('charge_time',[charge,time],None,None),
        ('charge_time_speed',[charge,time,speed],None,None),
        ('charge_energy_time',[charge,energy,time],[F(0),F(1),F(1)],[F(-2),F(1),F(1)]),
        ('charge_unit_impedance',[charge,impedance],[F(2),F(1)],[F(0),F(1)]),
        ('four_independent_units',[charge,mass,length,time],[F(0),F(1),F(2),F(-1)],
                                                   [F(-2),F(1),F(2),F(-1)])]
    anchors = []
    for name, w, ca, cz in scenarios:
        item = {'family':name,'W':[[str(a) for a in row] for row in w],'rank':rank(w)}
        for label, target, coeff in [('action',action,ca),('unit_impedance',impedance,cz)]:
            identifiable = rank(w) == rank(w+[target])
            assert identifiable == (coeff is not None)
            if identifiable:
                product = [sum((coeff[j]*w[j][i] for j in range(len(w))),F(0)) for i in range(4)]
                assert product == target
                item[label] = {'identified':True,'certificate':[str(c) for c in coeff]}
            else:
                v = mass
                assert all(dot(row,v)==0 for row in w) and dot(target,v)==1
                item[label] = {'identified':False,'kernel_witness':[str(a) for a in v],
                               'target_log_change_per_parameter':'1'}
        anchors.append(item)
    save(out/'anchor_certificates.json', anchors)
    ratios = []
    for lam,q0,e,a0 in [(F(1),F(1),F(1),F(3)),(F(2),F(1),F(1),F(3)),
                       (F(1),F(2),F(1),F(5)),(F(3,7),F(5,2),F(4,3),F(7)),
                       (F(7,3),F(2,5),F(1),F(11,9)),(F(1,2),F(3),F(2),F(4))]:
        z = lam*a0/(q0*q0)
        amap = e*e*z
        assert amap/a0 == lam*(e/q0)**2
        ratios.append({'lambda':str(lam),'q0':str(q0),'e':str(e),'A0':str(a0),
                       'Z':str(z),'A_map_over_A0':str(amap/a0)})
    alpha_struct = F(7,960)
    pi_coefficient = 4*alpha_struct
    inverse_zeta_coefficient = 2/pi_coefficient
    assert pi_coefficient == F(7,240) and inverse_zeta_coefficient == F(480,7)
    assert pi_coefficient*4 < 2  # pi<4 proves the illustrative zeta1 result is not eta2
    assert 960 == 2**6*3*5 and 240 == 2**4*3*5
    save(out/'dimensional_results.json', {'dimensions_order':['M','L','T','Q'],
        'missing_charge_dimension_rank':[3,4],'lambda_charge_cases':ratios,
        'toy_alpha_compatibility':{'alpha_struct':str(alpha_struct),'eta_at_zeta1':str(pi_coefficient)+'*pi',
         'zeta_if_eta2_is_imposed':str(inverse_zeta_coefficient)+'/pi',
         'status':'Added hypotheses and inverse target requirement only; not a native prediction.'}})
    result = {'status':'PASS','ledger_rows_screened':len(rows),'selected_rows_checked':len(selected),
         'retained_remote_blob_checks':3,'anchor_families':len(anchors),'lambda_charge_fixtures':len(ratios),
         'impedance_selector':'NO_ADMITTED_LAW_IN_AUDITED_SOURCES','empirical_score':'UNSCORED',
         'physical_promotion':0,'scope':'Scoped source audit and exact dimensional/monomial model; not proof of global source absence.'}
    save(out/'summary.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', required=True, type=Path)
    main(p.parse_args().out)
