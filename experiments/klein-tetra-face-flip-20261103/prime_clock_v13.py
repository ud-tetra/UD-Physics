#!/usr/bin/env python3
"""Exact source-type K4 13/8 number theory and parity-clock no-go (v1.3)."""
import itertools,json
from collections import Counter
from fractions import Fraction
from math import gcd,lcm
import sympy as S
assert S.factorint(13)=={13:1}
assert S.factorint(8)=={2:3}
assert S.factorint(192)=={2:6,3:1}
assert gcd(312,192)==24 and Fraction(312,192)==Fraction(13,8)
assert [13*k%8 for k in range(9)]==[0,5,2,7,4,1,6,3,0]
assert [int(S.n_order(13,n)) for n in (8,24,192)]==[2,2,16]
assert pow(13,16,192)==1
bits=list(itertools.product((0,1),repeat=3))
s3=list(itertools.permutations(range(3)))
def act(p,t):
 out=[0]*3
 for i in range(3):out[p[i]]=t[i]
 return tuple(out)
def orbit(t):return {act(p,t) for p in s3}
rem=set(bits);os=[]
while rem:
 t=min(rem);o=orbit(t);os.append((t,sorted(o)));rem-=o
assert [len(o) for t,o in os]==[1,3,3,1]
choices=[]
for t,o in os:
 stabilizer=[g for g in s3 if act(g,t)==t]
 choices.append([v for v in bits if all(act(g,v)==v for g in stabilizer)])
assert [len(c) for c in choices]==[2,4,4,2]
maps=[]
for pick in itertools.product(*choices):
 m={}
 for (t,o),v in zip(os,pick):
  for g in s3:
   a,bb=act(g,t),act(g,v)
   if a in m:assert m[a]==bb
   m[a]=bb
 assert len(m)==8 and all(m[act(g,t)]==act(g,m[t]) for g in s3 for t in bits)
 maps.append(m)
bijections=[m for m in maps if len(set(m.values()))==8]
assert len(maps)==64 and len(bijections)==4
for m in bijections:
 assert all(m[m[t]]==t for t in bits)
assert all(m[(0,0,0)] in [(0,0,0),(1,1,1)] for m in maps)
perms=list(itertools.permutations(range(4)))
def compose(p,q):return tuple(p[q[i]] for i in range(4))
def order(p):
 x=tuple(range(4))
 for n in range(1,25):
  x=compose(p,x)
  if x==tuple(range(4)):return n
 raise ValueError
grouporder=Counter(lcm(order(p),1 if t==(0,0,0) else 2) for p in perms for t in bits)
assert sum(grouporder.values())==192 and max(grouporder)==6
simp=[list(itertools.combinations(range(4),k)) for k in range(1,5)]
ofs=(0,4,10,14)
d=S.zeros(15)
for k in (1,2,3):
 for j,t in enumerate(simp[k]):
  for i in range(k+1):
   d[ofs[k-1]+simp[k-1].index(t[:i]+t[i+1:]),ofs[k]+j]=(-1)**i
A=d-d.T;J=A/2
h=S.Matrix([S.Rational(1,2)]*4+[0]*11)
Q0=h*h.T
assert A**3==-4*A and J**2==-(S.eye(15)-Q0)
U=Q0+J
assert U.T*U==S.eye(15) and U**2==2*Q0-S.eye(15) and U**4==S.eye(15)
pairs=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
for pp in pairs:
 W=S.zeros(15,2)
 for j,e in enumerate(pp):W[4+simp[1].index(e),j]=1
 Qe=W*W.T;Qj=J*Qe*J.T
 assert U*Qe*U.T==Qj and U*Qj*U.T==Qe
top=S.zeros(15,1);top[14]=1
Qtop=top*top.T+(J*top)*(J*top).T
K=S.eye(15)-Qtop
assert K.rank()==13 and K*A==A*K and U.T*K*U==K
assert S.trace(K)/8==S.Rational(13,8)
out={'status':'PASS_EXACT_CONDITIONAL','prime_factors':{'13':'13','8':'2^3','192':'2^6*3'},
 'capacity_average':'(24*13)/(24*8)=312/192=13/8',
 'Z8_plus13':[13*k%8 for k in range(9)],
 'Z192_plus13_period':192,'Z192_plus312_period':8,'Z192_multiply13_order':16,
 'Theta_F2cube_additive_exponent':2,'Theta_equivariant_deterministic_maps':64,
 'Theta_equivariant_bijections':4,'maximum_equivariant_cycle_length':2,
 'S4_x_Theta_product_group_max_element_order':6,
 'native_15D_amplitude_strobe_order':4,'native_middle_projector_strobe_order':2,
 'K4_leakage_gram_rank':13,'mean_over_8':'13/8',
 'source_selected_eight_step_clock':False,'physical_promotion':0}
print(json.dumps(out,sort_keys=True,indent=2))
