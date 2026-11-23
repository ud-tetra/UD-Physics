#!/usr/bin/env python3
"""One opposite-edge bit per tick: Gray clock and exploratory raw edge lift."""
import itertools,collections,json
THETA=list(itertools.product((0,1),repeat=3))
S4=list(itertools.permutations(range(4)))
S3=list(itertools.permutations(range(3)))
PAIRS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
PAIRSETS=tuple(frozenset(frozenset(e) for e in p) for p in PAIRS)
EDGES=list(itertools.combinations(range(4),2))
REFERENCES=((0,1),(0,2),(0,3))
def bits(n):return tuple((n>>i)&1 for i in range(3))
def act(p,x):
 y=[0]*3
 for i,v in enumerate(x):y[p[i]]=v
 return tuple(y)
def inverse(p):return tuple(p.index(i) for i in range(3))
def induced(p):
 return tuple(PAIRSETS.index(frozenset(frozenset(p[v] for v in e) for e in pair)) for pair in PAIRS)
GRAY=[bits(n^(n>>1)) for n in range(8)]
NEXT={GRAY[k]:GRAY[(k+1)%8] for k in range(8)}
assert all(sum(x!=y for x,y in zip(k,NEXT[k]))==1 for k in THETA)
flips=[next(j for j in range(3) if x[j]!=NEXT[x][j]) for x in GRAY]
assert flips==[0,1,0,2,0,1,0,2]
hood={x:[y for y in THETA if sum(a!=b for a,b in zip(x,y))==1] for x in THETA}
cycles=[]
def walk(path):
 if len(path)==8:
  if path[0] in hood[path[-1]]:cycles.append(tuple(path))
  return
 for nxt in hood[path[-1]]:
  if nxt not in path:walk(path+[nxt])
walk([(0,0,0)])
assert len(cycles)==12
unoriented={min(c,(c[0],)+tuple(reversed(c[1:]))) for c in cycles}
assert len(unoriented)==6
# Gray f is non-affine: check its output Boolean ANF degree.
def anf_degree(k):
 vals=[NEXT[bits(n)][k] for n in range(8)]
 for i in range(3):
  for mask in range(8):
   if mask>>i&1:vals[mask]^=vals[mask^(1<<i)]
 return max((mask.bit_count() for mask,z in enumerate(vals) if z),default=0)
assert max(anf_degree(k) for k in range(3))==2
RAW=list(itertools.product((0,1),repeat=6))
def parity(e):
 return tuple(e[EDGES.index(a)]^e[EDGES.index(b)] for a,b in PAIRS)
def relabel(p,e):
 y=[0]*6
 for edge in EDGES:
  moved=tuple(sorted(p[v] for v in edge))
  y[EDGES.index(moved)]=e[EDGES.index(edge)]
 return tuple(y)
def update(p,e):
 m=induced(p);eta=act(inverse(m),parity(e));following=NEXT[eta]
 k=next(j for j in range(3) if eta[j]!=following[j])
 moved=tuple(sorted(p[v] for v in REFERENCES[k]))
 z=list(e);z[EDGES.index(moved)]^=1
 return p,tuple(z)
for p in S4:
 for e in RAW:
  q=update(p,e)
  assert sum(a!=b for a,b in zip(e,q[1]))==1
  assert sum(a!=b for a,b in zip(parity(e),parity(q[1])))==1
  x=(p,e);seen=[]
  for _ in range(8):seen.append(x);x=update(*x)
  assert x==(p,e) and len(set(seen))==8
  for g in S4:
   gp=tuple(g[p[i]] for i in range(4))
   lhs=update(gp,relabel(g,e))
   rhs=(gp,relabel(g,q[1]))
   assert lhs==rhs
# Rank obstruction: native real projectors of prior v1.1 have
# ranks 1+7*2. Invertible linear conjugation preserves ranks.
native_ranks=(1,2,2,2,2,2,2,2)
assert len(set(native_ranks))==2
print(json.dumps({
 "Gray_cycle":[''.join(map(str,x)) for x in GRAY],
 "pair_flip_schedule":flips,
 "directed_Hamiltonian_cube_cycles":len(cycles),
 "undirected_Hamiltonian_cube_cycles":len(unoriented),
 "Boolean_degree_of_successor":max(anf_degree(k) for k in range(3)),
 "exploratory_raw_edge_carrier":True,
 "edge_micro_states_with_full_frame":24*64,
 "S4_covariance_checks":24*64*24,
 "eight_step_raw_return":True,"one_edge_bit_per_step":True,
 "native_real_projector_ranks":native_ranks,
 "native_whole_projector_eight_cycle_possible_under_invertible_linear_map":False,
 "source_selected_update":False,"physical_promotion":0,
 "status":"PASS_EXACT_CONDITIONAL"
},indent=2))
