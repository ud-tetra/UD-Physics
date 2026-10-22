"""Scope audit, matched-grid refinement and compact archival checkpoints."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from variational import IDS

def load(out,name):return json.loads((out/name).read_text())
def dump(out,name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')

def main(out):
    normal=load(out,'variational-normal.json');fine=load(out,'variational-fine.json')['records'][0]
    objective=load(out,'variational-objective.json')['records'][0];adverse=load(out,'adverse_checks.json');rigid=load(out,'rigid_diagnostic.json')
    a=np.load(out/f'response-{IDS[0]}-fine0.npz');b=np.load(out/f'response-{IDS[0]}-fine1.npz');c=np.load(out/f'response-{IDS[0]}-objective1.npz')
    refinement={
      'reference_state_max_change_at_matching_times':float(np.max(abs(a['reference']-b['reference'][::2]))),
      'mean_volume_derivative_max_change_at_matching_times':float(np.max(abs(a['mean_volume_derivative']-b['mean_volume_derivative'][::2]))),
      'final_full_tangent_max_change':float(np.max(abs(a['final_tangent']-b['final_tangent']))),
      'phase_vector_change':float(np.linalg.norm(a['adverse_phase']-b['adverse_phase'])),
      'first_order_rms_change_including_quadrature':abs(normal['records'][next(i for i,r in enumerate(normal['records']) if r['id']==IDS[0])]['trust_region_first_order_minimum_rms']-fine['trust_region_first_order_minimum_rms']),
      'objective_diagnostic_repeat_same_reference':bool(np.array_equal(b['reference'],c['reference'])),
      'objective_diagnostic_repeat_same_tangent':bool(np.array_equal(b['final_tangent'],c['final_tangent']))}
    assert refinement['final_full_tangent_max_change']<2e-6
    assert refinement['mean_volume_derivative_max_change_at_matching_times']<2e-6
    assert refinement['objective_diagnostic_repeat_same_reference'] and refinement['objective_diagnostic_repeat_same_tangent']
    assert len(adverse['records'])==7 and min(r['breathing_retention'] for r in adverse['records'])>.8
    zero=next(r for r in adverse['records'] if r['amplitude_factor']==0.)
    assert zero['maximum_full_state_difference_from_augmented_reference']<1e-8
    raw=objective['sampled_readout_remainder_budget'];shape=objective['objective_readout_diagnostic']
    def det_remainder(radius):
        z=2*radius/raw['minimum_reference_cell_singular_value']
        return raw['maximum_reference_abs_cell_volume_ratio']*(3*z*z+z*z*z)
    diagnostic={'raw_primary_linear_radius':raw['linear_primary_position_radius'],
                'raw_radius_determinant_remainder_bound':det_remainder(raw['linear_primary_position_radius']),
                'shape_primary_linear_radius':shape['linear_shape_position_radius'],
                'shape_radius_determinant_remainder_bound':det_remainder(shape['linear_shape_position_radius']),
                'first_order_rms_margin_above_80percent':raw['first_order_rms_margin_above_80percent'],
                'sample_based_aligned_flow_remainder_allowance':shape['hypothetical_aligned_flow_remainder_allowance'],
                'meaning':'Conditional readout design budgets from sampled numerical constants; neither raw nor aligned flow is certified.'}
    assert diagnostic['raw_radius_determinant_remainder_bound']>diagnostic['first_order_rms_margin_above_80percent']
    assert diagnostic['shape_radius_determinant_remainder_bound']<diagnostic['first_order_rms_margin_above_80percent']
    audit={'status':'OPEN_NOT_VALIDATED','horizon':100,'initial_housing_energy_fraction':'1/40000',
      'exact_conditional_criterion':'A+beta+C*r²<r, full positive state norm, positive continuous length domain; projected/aligned remainder controls volume',
      'slots':{'analytic_full_jacobian':'DERIVED_AND_CONSTRUCTOR_CHECKED','initial_housing_energy_injection':'NORMALIZED_AND_CHECKED',
      'moving_pulse_U_t0_B':'NUMERICAL_180_COLUMNS_ONLY','forced_Green_U_ts':'NOT_ENCLOSED','uniform_nonlinear_remainder':'NOT_ENCLOSED',
      'reference_defect_and_initial_error':'NOT_ENCLOSED','continuous_time_domain_margins':'SAMPLED_ONLY',
      'readout_Gram_and_quadrature_error':'REFINED_FLOATING_NOT_ENCLOSED','alignment_chart_nonlinear_remainder':'NOT_ENCLOSED'},
      'scalar_radii_inequality_evaluation':'NOT_POSSIBLE_WITH_VALIDATED_BOUNDS_CURRENTLY_AVAILABLE',
      'readout_design_diagnostic':diagnostic,
      'not_evidence_for_missing_bounds':['KKT residual','energy balance','solver tolerance','tangent P/L conservation','finite directional residual scaling','sampled frame projection'],
      'next_discriminant':'Enclose the full forced Green and nonlinear/chart remainder in a frame-aware block norm for the limiting case. Validate an aligned primary flow remainder below1/1000 before attempting the inherited80% screen. The1/1000 is a conservative design target within the numerical allowance, not a new pass threshold.'}
    # Archive selected sufficient evidence, without bulk augmented trajectory arrays.
    packed={}
    raw_files=[]
    for name,label in [(f'response-{IDS[0]}-fine0.npz','worst_normal'),(f'response-{IDS[1]}-fine0.npz','nominal_normal'),(f'response-{IDS[0]}-fine1.npz','worst_fine')]:
        data=np.load(out/name)
        for key in ['volume_gram','volume_cross','adverse_phase','final_tangent','initial_injection']:
            packed[label+'_'+key]=data[key]
        packed[label+'_reference_initial']=data['reference'][0];packed[label+'_reference_final']=data['reference'][-1]
        raw_files.append({'filename':name,'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest(),'bytes':(out/name).stat().st_size,
                          'archived':False,'reproduction':'variational.py; compact phase/Gram/final-tangent subset archived'})
    np.savez_compressed(out/'compact_checkpoints.npz',**packed)
    assert (out/'compact_checkpoints.npz').stat().st_size<10*1024*1024
    raw_objective=out/f'response-{IDS[0]}-objective1.npz'
    raw_files.append({'filename':raw_objective.name,'sha256':hashlib.sha256(raw_objective.read_bytes()).hexdigest(),'bytes':raw_objective.stat().st_size,'archived':False,'reproduction':'variational.py --which objective; matched reference/tangent repeat checked'})
    dump(out,'refinement_checks.json',refinement);dump(out,'certificate_audit.json',audit);dump(out,'uncaptured_intermediates.json',raw_files)
    summary={'status':'MOVING_PULSE_DIFFERENTIAL_MILESTONE_NONLINEAR_BALL_OPEN','parameter_sets':2,'strengths':[.05],
      'full_mechanical_phase_variables':560,'initial_housing_phase_coordinates':180,
      'normal_variational_records':normal['records'],'fine_variational_record':fine,'objective_diagnostic':objective['objective_readout_diagnostic'],
      'refinement':refinement,'finite_adverse_preparations':7,'finite_post_exposure_frame_diagnostics':1,
      'minimum_observed_adverse_breathing_retention':min(r['breathing_retention'] for r in adverse['records']),
      'maximum_adverse_mean_volume_taylor_residual_rms':max(r['mean_volume_taylor_residual_rms'] for r in adverse['records']),
      'directional_residual_scaling':adverse['scaling'],'frame_diagnostic':{k:v for k,v in rigid.items() if k!='phase'},
      'certificate_status':audit['status'],'scope':'Exact analytic Jacobian/conditional tube and geometric readout implications; floating first-order all-phase problem at two exposed parameter sets; finite nonlinear phases only. No u100 nonlinear phase-ball/continuous-parameter certificate; no physical promotion.'}
    dump(out,'milestone.json',summary);print(json.dumps({'status':summary['status'],'refinement':refinement,'readout_budget':diagnostic,'compact_bytes':(out/'compact_checkpoints.npz').stat().st_size},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
