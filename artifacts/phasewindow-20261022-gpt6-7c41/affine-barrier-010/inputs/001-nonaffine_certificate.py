#!/usr/bin/env python3
"""UD full-12-vertex rank-three non-affinity certificate.
EXACT/CONDITIONAL: a flat centre-face cell at U<=E requires ||Z||_F>1/40.
The full nonlinear u100 theorem remains OPEN.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import argparse
import json
import sympy as S

phi=(1+S.sqrt(5))/2
V=[]
for a in (-1,1):
 for b in (-1,1):
  V.extend((S.Matrix([0,a,b*phi])/2,S.Matrix([a,b*phi,0])/2,
            S.Matrix([b*phi,0,a])/2))
V.sort(key=lambda v:tuple(float(x) for x in v))
R2=(5+S.sqrt(5))/8
edges=[(i,j) for i,j in combinations(range(12),2)
       if S.simplify((V[i]-V[j]).dot(V[i]-V[j])-1)==0]
faces=[(i,j,k) for i,j,k in combinations(range(12),3)
       if all((x,y) in edges for x,y in combinations((i,j,k),2))]
assert len(edges)==30 and len(faces)==20
assert S.simplify(sum((v*v.T for v in V),S.zeros(3))-4*R2*S.eye(3))==S.zeros(3)
assert R2>S.Rational(9,10) and R2<1
assert (5+2*S.sqrt(5))/15>S.Rational(79,100)**2
assert 5+S.sqrt(5)<S.Rational(27,10)**2
# Thirty edge directions form an exact isotropic fourth-moment frame.
T=[]
for i in range(3):
 t=S.zeros(3);t[i,i]=1;T.append(t)
for i,j in ((0,1),(0,2),(1,2)):
 t=S.zeros(3);t[i,j]=t[j,i]=1;T.append(t)
for A in T:
 for B in T:
  lhs=sum((V[i]-V[j]).dot(A*(V[i]-V[j]))*
          (V[i]-V[j]).dot(B*(V[i]-V[j])) for i,j in edges)
  rhs=2*(S.trace(A)*S.trace(B)+2*S.trace(A*B))
  assert S.simplify(lhs-rhs)==0
# Every face has the same centroid and tangent covariance structure.
for f in faces:
 pts=[V[i] for i in f];cen=sum(pts,S.zeros(3,1))/3
 n=cen/S.sqrt(cen.dot(cen))
 cov=sum(((v-cen)*(v-cen).T for v in pts),S.zeros(3))
 assert S.simplify(cov-(S.eye(3)-n*n.T)/2)==S.zeros(3)
 assert S.simplify(cen.dot(cen)-(7+3*S.sqrt(5))/24)==0
# Original material coefficient minima and pulse mechanical energy budget.
E=Q(1360051,20000000);g=Q(19,20);k=Q(19,50)
delta=Q(1,40);L=Q(137,100)
assert 2*E<k*Q(3,5)**2
# Odd and even spoke modes split energy with weights (1+g) and 1.
# Bins in the exterior edge strain norm exhaust a<3/5.
bins=[('0..1/2',Q(0),Q(1,2),Q(53,200),Q(37,100)),
      ('1/2..11/20',Q(1,2),Q(11,20),Q(3,20),Q(21,100)),
      ('11/20..3/5',Q(11,20),Q(3,5),Q(21,200),Q(3,20))]
checks=[]
for label,a0,a1,o,b in bins:
 rem=2*E-k*a0*a0
 assert rem<(1+g)*o*o and rem<b*b
 af=a1+Q(27,10)*delta
 lam=1-af-af*af/2
 assert lam>0 and 3*Q(9,10)*lam>Q(1,4)
 # Quantitative necessary flat-face inequality derived in NONAFFINE_THRESHOLD.md.
 low=Q(79,50)*(lam-2*delta*delta)-4*lam*delta
 high=o*(1+Q(5,7)*b)+Q(5,9)*(2*L+delta)*delta
 assert low>high
 checks.append(dict(bin=label,gram_lambda_lower=str(lam),
                    strict_margin=str(low-high)))
result={'status':'EXACT_CONDITIONAL',
        'question':'Flattened original cell at U<=pulse requires nonaffine Z?',
        'pulse_energy':str(E),'nonaffine_threshold':'1/40',
        'necessary':'flat at U<=E implies ||(I-P0-PV)Y||_F>1/40',
        'edge_fourth_moment_checks':36,'face_covariance_checks':20,
        'energy_bins':checks,
        'stress_corollary':'flat at U<=E implies tr(Y^T Omega Y)>(1+sqrt5)/1600',
        'limitations':'Does not exclude nonaffine collapse or certify u=100 dynamics.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('PASS',result['status'],[x['strict_margin'] for x in checks])
