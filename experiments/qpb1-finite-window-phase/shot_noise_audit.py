#!/usr/bin/env python3
"""QPB phase-004: shot-count sufficiency & untracked phase-frame drift.

Exact probability inequalities for independent Bernoulli four-phase receiver,
with numerical evaluations only of exp and time conversions. No lab data.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from math import exp, log, sqrt, ceil, factorial
import json
from pathlib import Path
import argparse

getcontext().prec=45
eta=Fraction(2,10**6)
alpha=Fraction(1,100)
per_setting=7_400_000_000_000
number_settings=8 # four analyzer settings at two calibration delays
union_upper=16*exp(-float(per_setting*eta**2/4))
assert union_upper < float(alpha)
# Fully rational certificate: exp(37/5) exceeds its 13th Taylor sum >1600.
# Consequently 16*exp(-37/5) < 16/1600 = 0.01, without float rounding.
exp_lower=sum(Fraction(37,5)**k/factorial(k) for k in range(14))
assert exp_lower > 1600
required_real=4*log(16/float(alpha))/float(eta**2)
assert per_setting>=ceil(required_real)
shots_total=number_settings*per_setting
# Each of 8 intensity sample means has |error| <= eta/(2 sqrt(2));
# Hoeffding + union implies both complex probes |Z_est-Z|<=eta.
# This is a sufficient, intentionally conservative budget, not an optimal lower bound.
prev_kappa=Fraction(699576281715419,725760000000000000)
prev_total=Fraction(534794619424186500609612131837359,65106126461057096943360000000000000)
T_max=Fraction(44,7)+Fraction(1,100)
margin=Fraction(1,1000)-prev_kappa
rate_margin=margin/T_max
assert margin>0
# Coherent unknown phase shift between probe and main measurements adds directly
# to the corrected phase; the general deterministic bound becomes previous+|shift|.
phase_shift=Fraction(2,1000)
new_uncertified_budget=prev_total+phase_shift
assert new_uncertified_budget>Fraction(1,100)
# Estimate (not a guarantee) contrast at the two probe times in nominal model.
# This only sets the expected counts; probability guarantee is worst-case over p.
res={
 'status':'PASS',
 'labels':['EXACT','CONDITIONAL','NUMERICAL','OPEN'],
 'carrier':'Three-frequency conserved local UD toy; ideal independent Bernoulli four-step fringes',
 'model':{
  'analyzer_phases':['0','pi/2','pi','3pi/2'],
  'probes':['h=1/12','h/2=1/24'],
  'probe_complex_error_budget':str(eta),
  'joint_failure_probability_ceiling':str(alpha),
  'iid_Bernoulli_assumption':True,
  'single_setting_photons_or_events':per_setting,
  'number_of_settings':number_settings,
  'total_independent_binary_events':shots_total,
  'Hoeffding_union_tail':'P_fail<=16*exp(-m*eta^2/4)',
  'sufficient_m_continuous_decimal':required_real,
  'tail_probability_evaluated':union_upper,
  'exact_failure_certificate':'sum_{k=0}^{13}(37/5)^k/k! > 1600 implies 16 exp(-37/5) < 1/100',
  'nominal_detection_rate_examples_events_per_second':[100_000_000,1_000_000_000],
  'total_acquisition_hours_illustrative':[shots_total/(rate*3600) for rate in [100_000_000,1_000_000_000]],
 },
 'exact_drift':{
  'previous_calibration_bound_radians':str(prev_kappa),
  'unused_calibration_margin_radians':str(margin),
  'nominal_max_window_native':str(T_max),
  'allowed_unbudgeted_reference_ramp_radians_per_native_time':str(rate_margin),
  'allowed_ramp_decimal':float(rate_margin),
  'adversarial_reference_step_radians':str(phase_shift),
  'joint_budget_with_step_radians':str(new_uncertified_budget),
  'joint_budget_with_step_decimal':float(new_uncertified_budget),
  'visibility_unchanged_under_reference_step':True,
  'measured_probe_phase_shift':0,
  'reference_step_only_at_main_endpoint':True,
 },
 'counterexample':'Unknown reference phase step of 0.002 rad at main readout changes corrected holonomy by 0.002 rad while all probe fringes and visibilities remain otherwise unchanged. No device-only data can separate this from an extra phase without reference calibration.',
 'conditions_not_verified':['physical UD carrier access','reference phase stability','shot rate and losses','IID photons/events','phase steps accurately spaced','state/gain repeatability','native clock conversion'],
 'evidence_notes':'Exact algebra and Hoeffding inequality for the stated estimator; exp/log and durations are numerical evaluations. Same-context constructor audit, not independent external reviewer or experiment.'
}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
 args=p.parse_args();args.out.parent.mkdir(parents=True,exist_ok=True)
 args.out.write_text(json.dumps(res,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'PASS': True,'shots':shots_total,'tail':union_upper,'drift_rate_max':float(rate_margin),'phase_budget_with_bias':float(new_uncertified_budget)},sort_keys=True))
