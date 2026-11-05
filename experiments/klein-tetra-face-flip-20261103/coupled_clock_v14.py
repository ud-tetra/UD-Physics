#!/usr/bin/env python3
"""Exact G=S3 coupled parity eight-cycle and affine-update obstruction (stdlib)."""
import itertools,math,json
from collections import Counter
THETA=list(itertools.product((0,1),repeat=3))
S3=list(itertools.permutations(range(3)))
S4=list(itertools.permutations(range(4)))
PAIR=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
PAIRSET=tuple(frozenset(frozenset(e) for e in pp) for pp in PAIR)
def pair_frame(p):
 return tuple(PAIRSET.index(frozenset(frozenset(p[v] for v in edge) for edge in pp)) for pp in PAIR)
def comp(g,m):return tuple(g[m[i]] for i in range(3))
def inv(m):return tuple(m.index(i) for i in range(3))
def act(p,x):
 y=[0]*3
 for i,v in enumerate(x):y[p[i]]=v
 return tuple(y)
def num(x):return sum(v<<i for i,v in enumerate(x))
def bits(n):return tuple((n>>i)&1 for i in range(3))
def f5(x):return bits((num(x)+5)%8)
assert all(f5((a,b,c))==(a^1,b^a,c^1^(a&b)) for a,b,c in THETA)
assert len(S4)==24 and Counter(pair_frame(p) for p in S4)=={x:4 for x in S3}
def t48(s):
 m,x=s
 return m,act(m,f5(act(inv(m),x)))
P48=list(itertools.product(S3,THETA))
assert len(P48)==48
for s in P48:
 x=s;seen=[]
 for i in range(8):seen.append(x);x=t48(x)
 assert x==s and len({v[1] for v in seen})==8
 for g in S3:
  gf=(comp(g,s[0]),act(g,s[1]))
  y=t48(s)
  assert t48(gf)==(comp(g,y[0]),act(g,y[1]))
def t192(s):
 p,x=s;m=pair_frame(p)
 return p,act(m,f5(act(inv(m),x)))
P192=list(itertools.product(S4,THETA))
for p,x in P192:
 y=(p,x)
 for i in range(8):y=t192(y)
 assert y==(p,x)
 for g in S4:
  gp=tuple(g[p[j]] for j in range(4));r=pair_frame(g)
  s=t192((p,x))
  assert t192((gp,act(r,x)))==(gp,act(r,s[1]))
# Necessity: three distinct weight-one stabilizers intersect in the identity.
stabs=[{g for g in S3 if act(g,bits(1<<i))==bits(1<<i)} for i in range(3)]
assert set.intersection(*stabs)=={(0,1,2)}
# Affine bijections over F2 on the parity three-cube never have an eight-cycle.
def affine_mat(rows,x):return tuple(sum(rows[i][j]*x[j] for j in range(3))%2 for i in range(3))
mats=[a for a in itertools.product(THETA,repeat=3) if len({affine_mat(a,x) for x in THETA})==8]
assert len(mats)==168
cycles=Counter()
for a in mats:
 for v in THETA:
  f={x:tuple(y^z for y,z in zip(affine_mat(a,x),v)) for x in THETA}
  visited=set();ls=[]
  for x in THETA:
   if x in visited:continue
   y=x;k=0
   while y not in visited:
    visited.add(y);y=f[y];k+=1
   assert y==x
   ls.append(k)
  cycles[max(ls)]+=1
assert sum(cycles.values())==1344 and cycles[8]==0
# Transfer current on finite address graph; not physical simplicial burden.
stocks={s:1+((7*i+3)%11) for i,s in enumerate(P48)}
new={t48(s):v for s,v in stocks.items()}
U=set(P48[::3])
incoming=sum(stocks[s] for s in P48 if s not in U and t48(s) in U)
outgoing=sum(stocks[s] for s in P48 if s in U and t48(s) not in U)
delta=sum(new[s]-stocks[s] for s in U)
assert (delta,incoming,outgoing)==(14,59,45)
assert sum(stocks.values())==sum(new.values())
assert sum(v*v for v in stocks.values())==sum(v*v for v in new.values())
print(json.dumps({
 "effective_frame_states":6,"effective_total_states":48,"existing_full_frame_states":192,
 "S4_to_S3_kernel_cardinality":4,
 "S4_covariance_checks":len(P192)*len(S4),
 "period":8,"eight_cycles_effective":6,"eight_cycles_full":24,
 "affine_invertible_F2_3_count":1344,"affine_cycle_histogram":dict(cycles),
 "affine_eight_cycles":0,"minimal_extra_frame_states_proved":6,
 "discrete_stock_flux_example":{"delta":delta,"in":incoming,"out":outgoing},
 "source_selected_successor":False,"physical_promotion":0,
 "status":"PASS_EXACT_CONDITIONAL"
},indent=2,sort_keys=True))
