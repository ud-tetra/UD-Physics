#!/usr/bin/env python3
"""Independent spectral check from factor CW and filled-simplex Laplacians."""
import json
from itertools import combinations
from sympy import Matrix,zeros,eye,trace

def cw(twist):
 b1=Matrix([[-2,0]]) if twist else zeros(1,2)
 b2=zeros(2,1) if twist else Matrix([[0],[2]])
 levels=[b1*b1.T,b1.T*b1+b2*b2.T,b2.T*b2]
 counts={0:0,4:0}
 for m in levels:
  for val,mul in m.eigenvals().items():counts[int(val)]+=mul
 return counts

simp=[list(combinations(range(4),k)) for k in (1,2,3,4)]
D=zeros(15)
off=(0,4,10,14)
for q in (1,2,3):
 for j,t in enumerate(simp[q]):
  for a in range(q+1):
   sub=t[:a]+t[a+1:]
   D[off[q-1]+simp[q-1].index(sub),off[q]+j]=(-1)**a
assert D*D==zeros(15)
A=D-D.T
L=-A*A
assert L*(L-4*eye(15))==zeros(15)
assert L.rank()==14 and trace(L)==56
packet={0:1,4:14}
out={}
for label,t in (('twisted',True),('untwisted',False)):
 base=cw(t)
 spectrum={}
 for b,mb in base.items():
  for k,mk in packet.items():spectrum[b+k]=spectrum.get(b+k,0)+mb*mk
 assert spectrum=={0:2,4:30,8:28}
 out[label]={'base_spectrum':base,'packet_spectrum':packet,'product_spectrum':spectrum}
print(json.dumps({'method':'independent factor Hodge Laplacians and eigenvalue-sum multiplicities','results':out,'status':'PASS_EXACT','physical_promotion':0},sort_keys=True,indent=2))
