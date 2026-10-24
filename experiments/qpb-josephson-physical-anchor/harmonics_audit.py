#!/usr/bin/env python3
"""Exact two-harmonic JJ softness sign and independent quadrature constructor.

The Willsch et al 2024 spectroscopy data are not imported or represented here.
"""
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path


def leading(q):
    """Frequency ratio = 1 + leading(q) * a^2 + O(a^4)."""
    assert 1 + 2*q > 0
    return -(1 + 8*q) / (16*(1 + 2*q))


def frequency_ratio(a, q, n=4096):
    """Period quadrature for zero-bias U(phi)=1-cos(phi)+q*(1-cos(phi)^2)."""
    q = float(q)
    if a == 0:
        return 1.0
    assert 0 < a < math.pi and 1 + 2*q > 0
    delta = math.pi / (2*n)
    total = 0.0
    for j in range(n+1):
        theta = j*delta
        if j == n:
            integrand = math.sqrt(2*a/(math.sin(a) + q*math.sin(2*a)))
        else:
            phi = a*math.sin(theta)
            gap = (2*math.sin((a+phi)/2)*math.sin((a-phi)/2)
                   *(1 + q*(math.cos(phi)+math.cos(a))))
            assert gap > 0
            integrand = a*math.cos(theta)/math.sqrt(gap)
        total += (1 if j in (0,n) else 4 if j % 2 else 2)*integrand
    quarter = (total*delta/3)/math.sqrt(2.0)
    return (math.pi/(2*quarter))/math.sqrt(1+2*q)


examples=[]
for q in (F(-1,4), F(-3,25), F(0), F(1,20)):
    c=leading(q)
    row={'I2_over_I1':str(q), 'leading_a_squared_coefficient':str(c),
         'zero_phase_curvature_in_I1_units':str(1+2*q),
         'ratio_a_0_2':frequency_ratio(0.2,q),
         'ratio_a_0_4':frequency_ratio(0.4,q)}
    examples.append(row)
assert leading(F(0)) == F(-1,16)
assert leading(F(-1,4)) == F(1,8)
assert leading(F(-1,8)) == 0
assert 0 < frequency_ratio(.4,F(-1,4)) - 1 < .03
assert frequency_ratio(.4,F(0)) < 1
assert abs(frequency_ratio(.4,F(0)) - math.cos(.4/2)) > 1e-3  # not simple cosine
assert abs(frequency_ratio(.4,F(0)) - 0.9900082042903813) < 2e-10
# For q=-1/4, U=(1-cos(phi))*(3-cos(phi))/4>=0; stable min at phi=0.
for cs in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
    U = 1-cs + F(-1,4)*(1-cs*cs)
    assert U == (1-cs)*(3-cs)/4 and U>=0

result={
 'status':'PASS',
 'labels':['EXACT','CONDITIONAL','NUMERICAL','EMPIRICAL_SOURCE','OPEN'],
 'physical_model':'I(phi)=I1*sin(phi)+I2*sin(2phi), q=I2/I1, I1>0, M>0',
 'potential_in_E1_units':'U(phi)=1-cos(phi)+q*(1-cos(phi)^2)',
 'stable_origin_condition':'1+2q>0',
 'first_nonlinear_coefficient':'frequency(a)/frequency(0)=1-[(1+8q)/(16*(1+2q))]*a^2+O(a^4)',
 'hardening_condition':'-1/2<q<-1/8; mathematical two-harmonic model, NOT measured parameter',
 'quartic_zero_condition':'q=-1/8; next-order amplitude terms unresolved by this sign test',
 'conventional_hardening_example':{'q':'-1/4','positive_bounded_potential':'(1-cos(phi))*(3-cos(phi))/4','leading_shift':'+1/8 a^2'},
 'sine_only_example':{'q':'0','leading_shift':'-1/16 a^2'},
 'numerical_quadrature_examples':examples,
 'published_dataset':{
    'paper':'Willsch et al., Observation of Josephson harmonics in tunnel junctions, Nature Physics 20, 815-821 (2024)',
    'paper_doi':'10.1038/s41567-024-02400-8',
    'correction_doi':'10.1038/s41567-024-02491-3',
    'dataset_doi':'10.26165/JUELICH-DATA/LGRHUH',
    'dataset_version':'V2 (landing metadata)',
    'dataset_landing_file':'README.txt, 97 bytes, points to external GitLab repository',
    'code_and_data_url':'https://jugit.fz-juelich.de/qip/josephson-harmonics',
    'raw_spectroscopy_bytes':'NOT_ACQUIRED: GitLab download blocked by automated-access verification',
    'measured_observable':'transmon multi-level transition spectroscopy, not classical turning-phase a versus omega(a)',
    'published_discrepancy':'f03 can differ >10 MHz from basic sinusoidal transmon model, imprecision on order 1 MHz',
    'higher_harmonics_observed':'source reports percent-level higher harmonics, not the chosen q=-1/4'
 },
 'heldout':'NOT_RUN: no calibrated classical amplitude-frequency pairs or frozen UD physical mapping',
 'previous_sign_claim':'VALID ONLY under sine-only Josephson and positive-star mapping; NOT a universal junction sign rule',
 'matched_null':'conventional Josephson harmonic CPR with adjustable I2 reproduces the hardening example; no new UD physical prediction',
 'verification':'exact rational leading term and positive potential; independent numerical period quadrature; outside scientific review NOT_RUN'
}

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','examples':len(examples),'harmonic_hardening':examples[0]['ratio_a_0_4']},sort_keys=True))
