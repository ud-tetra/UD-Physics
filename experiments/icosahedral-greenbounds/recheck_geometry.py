"""Recovery reconstruction, NOT_RUN after authoring; exact retained curve check."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
import numpy as np

def centered(a):
    x=[[F.from_float(float(v)) for v in row] for row in a]
    mean=[sum((row[j] for row in x),F(0))/13 for j in range(3)]
    return [[row[j]-mean[j] for j in range(3)] for row in x]
def diff(a,b):return [[v-w for v,w in zip(r,s)] for r,s in zip(a,b)]
def scale(a,s):return [[s*v for v in row] for row in a]
def norm2(a):return sum((v*v for row in a for v in row),F(0))

def check(path):
    z=np.load(path);X=[centered(a) for a in z['positions']];V=[centered(a) for a in z['velocities']]
    assert len(X)==len(V) and len(X) in (2001,4001)
    h=F(100,len(X)-1);lo=None;hi=None;rho=F(0)
    for x in X:
        G=[[sum((row[i]*row[j] for row in x),F(0)) for j in range(3)] for i in range(3)]
        lower=min(G[i][i]-sum(abs(G[i][j]) for j in range(3) if i!=j) for i in range(3))
        upper=max(G[i][i]+sum(abs(G[i][j]) for j in range(3) if i!=j) for i in range(3))
        lo=lower if lo is None else min(lo,lower);hi=upper if hi is None else max(hi,upper)
    for x,y,v,w in zip(X,X[1:],V,V[1:]):
        d=diff(y,x)
        rho=max(rho,norm2(scale(v,h/3)),norm2(diff(d,scale(w,h/3))),norm2(d))
    assert lo>F(187,100)**2 and hi<F(97,50)**2 and rho<F(1,100)**2
    s=F(37,20);a=F(39,20);r=F(4,125)
    assert F(187,100)-F(1,100)>s and F(97,50)+F(1,100)==a and a*r<s*s
    q=2*a*r/(2*s*s-a*r);R=a*q*q/2+r*q
    assert q==F(624,33913) and R==F(132102048,143761446125)
    assert R*R<2*F(13,20000)**2
    assert F(13,20000)+F(7,20000)==F(1,1000)
    return dict(status='EXACT_DEFINED_REFERENCE_CURVE_AND_CONDITIONAL_CHART_PASS',
        sha256=hashlib.sha256(path.read_bytes()).hexdigest(),nodes=len(X),time_step=str(h),
        Gram_lower=str(lo),Gram_upper=str(hi),control_difference_norm_squared=str(rho),
        radius='4/125',chart_bound='<13/20000',projected_flow_target='<=7/20000',
        scope='Defined dyadic Hermite curve only; actual-flow conditions OPEN.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('files',nargs='+',type=Path);a=p.parse_args()
    for path in a.files:print(json.dumps(check(path),indent=2))
