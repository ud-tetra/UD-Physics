"""Consolidated milestone index; preserves the raw and refined scope-audit files."""
from pathlib import Path
import argparse,json,csv,hashlib

def main(out):
    load=lambda name:json.loads((out/name).read_text())
    old=load('summary.json');full=load('full_housing_refined.json');raw=load('full_housing_summary.json');bounds=load('bounds.json')
    assert old['status']=='FINITE_CASE_WINDOW_PASS' and full['status']=='FULL_HOUSING_WINDOW_PASS'
    pulses=list(csv.DictReader((out/'pulses.csv').open()));assert len(pulses)==64 and sum(r['passes_screen']=='True' for r in pulses)==64
    assert len(set((r['canonical_id'],r['nu']) for r in pulses))==58
    assert all(abs(float(r['housing_energy_over_reference_pulse'])-1/40000)<1e-15 for r in pulses)
    root=Path(__file__).resolve().parents[2];source=root/'artifacts/icosahedral-tolerances-20261022-a1/tolerances-001/files'
    original=[p for p in json.loads((source/'probes.json').read_text()) if p['group']!='challenge'];cases=load('cases.json');fields=['primary','ratio_error','beta','cf','omega_h','housing_weights']
    assert all({k:p[k] for k in fields}=={k:q[k] for k in fields} for p,q in zip(original,cases[:20]))
    assert (out/'baselines.json').read_bytes()==(source/'baselines.json').read_bytes()
    hashes={name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in ['probes.json','baselines.json']}
    r={'status':'FULL_HOUSING_LINEAR_WINDOW_AND_NONLINEAR_ENDPOINT_PASS','base_revision':'92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa',
       'strength_interval':['1/25','1/20'],'qualified_beta_interval':['1/200','1/20'],'housing_energy_fraction':'<=1/40000 of reference alpha=.1 pulse',
       'parameter_records':56,'unique_parameter_sets':50,'full_housing_initial_directions':90,'full_housing_initial_phase_dimension':180,
       'continuous_strength_energy_upper':full['maximum_full_housing_energy_upper']['continuous_strength_full_housing_energy_upper'],
       'continuous_strength_all_phase_linear_breathing_lower':full['minimum_all_phase_linear_breathing_lower'],
       'nonlinear_endpoint_records':64,'distinct_nonlinear_pulses':58,'endpoint_screen_passes':64,
       'minimum_nonlinear_breathing_retention_coarse':old['minimum_nonlinear_breathing_retention'],
       'minimum_nonlinear_breathing_retention_fine':min(r['fine_retention'] for r in old['refinements']),
       'maximum_hub_mismatch_fine':max(r['fine']['volume_signal_leakage'] for r in old['refinements']),
       'full_housing_nonlinear_ringdown_fractions':[r['final_total_energy_fraction'] for r in raw['ringdowns']],
       'exact_static_compliance_upper':bounds['uniform_static_mean_volume_compliance_upper'],
       'exact_fixed_primary_linear_energy_upper':bounds['fixed_primary_u100_energy_upper'],
       'exact_initial_housing_domain':bounds['initial_domain_all_phase_bounds'],
       'old_sector_linear_evaluations':old['unique_full_linear_evaluations'],'full_housing_linear_evaluations':raw['matrix_evaluations'],
       'raw_full_housing_audit_status':raw['status'],'raw_status_reason':'coarse interpolation exhausted17-nodecap withgaps;allnodes passed;sharper proven inequality closescoverage on same saved values',
       'original_input_sha256':hashes,'checks':'original20 physics sets and frozen nonlinear baseline bytes unchanged;64 records/58 unique trajectories and energy ratios verified',
       'limitations':['finite50-parameter family;not continuous uncertainty-box coverage','linear all-phase and continuous-strength inequalities evaluated numerically;not verified interval arithmetic','nonlinear checks are finite endpoint phases;no nonlinear all-phase/domain theorem','120 massless struts/ideal routing and uncalibrated units;physical tests UNSCORED;mainline promotion0']}
    (out/'milestone.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
