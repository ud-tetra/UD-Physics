"""Exact rational toy controls; no UD-derived lapse and no physical data."""
from fractions import Fraction as F
import json
from pathlib import Path

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def scale(a,s): return [[s*x for x in row] for row in a]
def generator(w1,w2):
    return [[F(0),-w1,F(0),F(0)],[w1,F(0),F(0),F(0)],
            [F(0),F(0),F(0),-w2],[F(0),F(0),w2,F(0)]]
def run():
    A=generator(F(1),F(2)); alpha=F(1,2)
    H=[[F(i==j) for j in range(4)] for i in range(4)]
    assert all(A[i][j]==-A[j][i] for i in range(4) for j in range(4))
    checks=[]
    for s in (F(1,3),F(1,2),F(2),F(3)):
        B=scale(A,s)
        assert B[3][2]/B[1][0]==2
        checks.append({'common_scale':str(s),'mode_ratio':'2'})
    detuned=generator(F(1),F(3))
    assert detuned[3][2]/detuned[1][0]==3
    assert detuned != scale(A,detuned[1][0]/A[1][0])
    # Nonorthogonal coordinate change preserves spectrum but changes the norm matrix.
    S=[[F(2 if i==0 else 1) if i==j else F(0) for j in range(4)] for i in range(4)]
    Si=[[F(1,2) if i==j==0 else F(i==j) for j in range(4)] for i in range(4)]
    B=mul(mul(S,A),Si)
    metric=mul(Si,Si)  # S is real diagonal; H'=S^-T H S^-1
    Bt=list(map(list,zip(*B)))
    left=mul(Bt,metric); right=mul(metric,B)
    assert all(left[i][j]+right[i][j]==0 for i in range(4) for j in range(4))
    assert B!=A and mul(mul(Si,B),S)==A
    # A single phase channel cannot distinguish assigned lapse from retuned oscillator.
    for t in (F(0),F(1,3),F(2),F(7)):
        assert F(2)*(F(1,2)*t)==F(1)*t
    return {'evidence':'EXACT_CONDITIONAL_TOY','uniform_scaling':checks,
            'detuned_ratio':'3','uniform_ratio':'2','similarity_metric':'diag(1/4,1,1,1)',
            'single_phase_alias':'omega0=2,lapse=1/2 versus omega=1,lapse=1',
            'physical_dilation':'NOT_ESTABLISHED','physical_promotion':0}

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PASS: exact uniform/detuned scaling, similarity metric, and single-phase alias controls')
