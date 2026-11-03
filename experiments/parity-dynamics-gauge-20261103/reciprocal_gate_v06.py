#!/usr/bin/env python3
"""v0.6 exact reciprocal-port null/release/latch controls; stdlib only."""
from fractions import Fraction as Q
import json
cases=[('0','0'),('pi/6','1/4'),('pi/4','1/2'),
       ('pi/2','1'),('pi','0'),('3pi/2','1'),('2pi','0')]
rows=[]
for label,square in cases:
    a=Q(square); assert 0<=a<=1
    rows.append({'u':label,'constant_coupling_target':str(a),
                 'constant_coupling_reservoir':str(1-a),
                 'null_target':'0',
                 'switched_off_target':str(a) if label in ('0','pi/6','pi/4') else '1'})
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(2)),Q(0))
             for j in range(2)] for i in range(2)]
def v2(M,v):
    return [sum((M[i][k]*v[k] for k in range(2)),Q(0))
            for i in range(2)]
I=[[Q(1),Q(0)],[Q(0),Q(1)]]
for co,si in [(Q(3,5),Q(4,5)),(Q(0),Q(1)),(Q(1),Q(0)),(Q(-1),Q(0))]:
    M=[[co,si],[-si,co]]
    Mt=[[co,-si],[si,co]]
    assert mm(M,Mt)==I
    for r,y in [(Q(0),Q(1)),(Q(1),Q(1)),(Q(-1),Q(1)),(Q(2),Q(3))]:
        r1,y1=v2(M,(r,y))
        assert r*r+y*y==r1*r1+y1*y1
assert Q(cases[0][1])==Q(cases[4][1])==0
assert Q(cases[3][1])==1
out={'source':'experiments/qpb1-source-reservoir/README.md v1.1 §§1-5',
     'preparation':'r0=0, incoming y0=(1,0); g=1 reciprocal control',
     'transport':'matched rotating-frame r=sin(u), y=cos(u)',
     'units':'native dimensionless u; no physical clock',
     'exact_fixtures':rows,'rational_orthogonal_fixture_checks':'PASS',
     'phase_counterexamples':{'old_target_same_source_at_pi_over_4':'2',
                              'old_target_opposite_source_at_pi_over_4':'0'},
     'zero_current_selector':'FAIL: zero current at u=0 empty and u=pi/2 full',
     'null_release_latch_at_pi':'target stock 0,0,1 respectively',
     'conservation':'target+source=1 for all empty-target fixture times',
     'fixed_skew_attraction':'NO-GO: joint isometry preserves distinct full-state distances',
     'selection_status':'OPEN: timed shutoff is an additional controller',
     'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
