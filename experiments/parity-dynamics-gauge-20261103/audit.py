#!/usr/bin/env python3
"""Exact K4 parity / S4 / illustrative dynamical quotient verification."""
import itertools,collections,json
V=range(4); E=list(itertools.combinations(V,2)); I={e:k for k,e in enumerate(E)}
pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
def pop(x):return x.bit_count()&1
def parts(s):return s&15,s>>4
def P(s):
 b,e=parts(s)
 return sum(((((e>>I[a])&1)^((e>>I[c])&1))<<k) for k,(a,c) in enumerate(pairs))
def q(s):return pop(s&15)
def delta(b):return sum(((((b>>i)&1)^((b>>j)&1))<<k) for k,(i,j) in enumerate(E))
def T(s):
 b,e=parts(s);return b|((e^delta(b))<<4)
def perm(s,p):
 b,e=parts(s);bb=sum(((b>>i)&1)<<p[i] for i in V);ee=0
 for k,(i,j) in enumerate(E):
  ee|=((e>>k)&1)<<I[tuple(sorted((p[i],p[j])))]
 return bb|(ee<<4)
S=range(1024);G=list(itertools.permutations(V))
fib=collections.Counter(P(s) for s in S)
assert set(fib)==set(range(8)) and set(fib.values())=={128}
assert all(T(T(s))==s for s in S)
assert all(T(perm(s,p))==perm(T(s),p) for s in S for p in G)
assert all(P(T(s))==(P(s)^(7 if q(s) else 0)) for s in S)
assert all(q(T(s))==q(s) for s in S)
assert P(0)==P(1)==0 and P(T(0))==0 and P(T(1))==7
unused=set(S); hist=collections.Counter()
while unused:
 s=min(unused);o={perm(s,p) for p in G};assert o<=unused
 hist[len(o)]+=1;unused-=o
assert hist=={1:4,3:4,4:12,6:12,12:42,24:16}
K=[h for h in S if P(h)==0]
H=[h for h in K if q(h)==0]
C=[h for h in K if delta(h&15)==0]
assert (len(K),len(H),len(C))==(128,64,16)
assert all(sum(1 for s in S if (P(s),q(s))==(a,b))==64 for a in range(8) for b in range(2))
print(json.dumps({"raw":1024,"fiber_each":128,"orbit_count":sum(hist.values()),"orbit_histogram":dict(sorted(hist.items())),"P_kernel":128,"P_history_invisible":64,"P_commuting_translations":16,"closed_four_bit_states":16,"checks":"PASS","scope":"conditional illustrative update; canonical UD OPEN","physical_promotion":0},indent=2,sort_keys=True))
