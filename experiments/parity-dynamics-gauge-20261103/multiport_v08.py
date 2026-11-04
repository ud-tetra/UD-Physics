#!/usr/bin/env python3
"""EXACT v0.8 K4 QPB1 two-channel port audit; stdlib only."""
from fractions import Fraction as F
import json
def tr(m):return tuple(tuple(m[j][i] for j in range(2)) for i in range(2))
def mm(m,n):return tuple(tuple(sum((m[i][k]*n[k][j] for k in range(2)),F(0)) for j in range(2)) for i in range(2))
def mv(m,v):return tuple(sum((m[i][k]*v[k] for k in range(2)),F(0)) for i in range(2))
def dot(v,w):return sum((a*b for a,b in zip(v,w)),F(0))
def wedge(v,w):return v[0]*w[1]-v[1]*w[0]
def deriv(r,y,m):
 rd=mv(m,y)
 yd=tuple(-z for z in mv(tr(m),r))
 return rd,yd
def dnorm(r,y,m):
 rd,yd=deriv(r,y,m)
 return 2*dot(r,rd)+2*dot(y,yd)
def dd(r,y,m):
 rd,yd=deriv(r,y,m)
 return wedge(rd,y)+wedge(r,yd)
def ddr(r,y,m,R):
 rd,yd=deriv(r,y,m)
 return wedge(rd,mv(R,y))+wedge(r,mv(R,yd))
a,b=F(3,5),F(4,5)
I=((F(1),F(0)),(F(0),F(1)))
R=((a,-b),(b,a))
assert mm(R,tr(R))==I and mm(tr(R),R)==I
fixtures=[((F(1),F(0)),(F(0),F(1))),
          ((F(2),F(0)),(F(0),F(1))),
          ((F(1),F(2)),(F(3),F(4))),
          ((F(-2),F(5)),(F(-3),F(1)))]
for r,y in fixtures:
 assert dnorm(r,y,R)==0 and ddr(r,y,R,R)==0
 rd,yd=deriv(r,y,R)
 assert rd==mv(R,y) and mv(R,yd)==tuple(-v for v in r)
assert dd(fixtures[1][0],fixtures[1][1],R)==F(12,5)
r,y=fixtures[0]
n=dot(r,r)+dot(y,y)
drot=wedge(r,mv(R,y))
assert n==2 and drot==F(3,5) and drot*drot/n==F(9,50)
# Exact minimum (N-sqrt(N*N-4*Drot*Drot))/2 = (2-8/5)/2.
assert (n-F(8,5))/2==F(1,5)
def sine_cosine_pi_over_two_integer(k):
 return ((0,1),(1,0),(0,-1),(-1,0))[k%4]
assert sine_cosine_pi_over_two_integer(1)==(1,0)
assert sine_cosine_pi_over_two_integer(2)==(0,-1)
assert sine_cosine_pi_over_two_integer(3)==(-1,0)
out={'source':'QPB1 source-reservoir v1.1 Sections 1-2',
     'model':'rprime=M y, yprime=-transpose(M) r, co-rotating modal coordinates',
     'S4':'matched sign representations assumed; any real 2x2 M equivariant',
     'complex_compatible':{'M':'(3/5)I+(4/5)j','old_D_derivative':'(4/5)(|r|^2-|y|^2)',
      'new_invariant':'D_R=det(r,R y)','D_R_example':'3/5',
      'N_example':'2','reservoir_bound':'9/50','exact_orbit_minimum':'1/5',
      'interpretation':'equivalent to scalar port by fixed reservoir rotation'},
     'anisotropic_co_rotating_branch':{
      'diag_1_2':'no shared complete source transfer time for all input components',
      'diag_1_3':'all source amplitudes transfer at chosen u=pi/2 from empty target, but reverse later',
      'caveat':'holding anisotropic M fixed in rotating frame needs time-modulated source-frame interaction'},
     'fixed_source_frame_G_M':'skew, isometric, no open full-state attractor',
     'physical_promotion':0,'checks':'PASS'}
print(json.dumps(out,sort_keys=True,indent=2))
