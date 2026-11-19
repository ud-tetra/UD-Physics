#!/usr/bin/env python3
"""Independent exhaustive Θ=F2^3 S4-equivariant deterministic map audit."""
import itertools,json
T=list(itertools.product((0,1),repeat=3))
G=list(itertools.permutations(range(3)))
def a(g,t):
 out=[0,0,0]
 for i in range(3):out[g[i]]=t[i]
 return tuple(out)
remaining=set(T);reps=[]
while remaining:
 r=min(remaining);orb={a(g,r) for g in G}
 reps.append((r,sorted(orb)));remaining-=orb
assert [len(o) for r,o in reps]==[1,3,3,1]
choices=[]
for r,_ in reps:
 stab=[g for g in G if a(g,r)==r]
 choices.append([t for t in T if all(a(g,t)==t for g in stab)])
assert list(map(len,choices))==[2,4,4,2]
maps=[]
for vals in itertools.product(*choices):
 f={}
 for (r,orb),v in zip(reps,vals):
  for g in G:
   x,y=a(g,r),a(g,v)
   if x in f:assert f[x]==y
   f[x]=y
 assert len(f)==8
 assert all(f[a(g,x)]==a(g,f[x]) for g in G for x in T)
 maps.append(f)
bij=[f for f in maps if len(set(f.values()))==8]
assert len(maps)==64 and len(bij)==4
assert all(f[f[t]]==t for f in bij for t in T)
assert all(f[(0,0,0)] in [(0,0,0),(1,1,1)] for f in maps)
assert all(f[(1,1,1)] in [(0,0,0),(1,1,1)] for f in maps)
out={'status':'PASS_EXACT_NO_GO_SCOPED','orbit_sizes':[1,3,3,1],
 'stabilizer_target_choices':[2,4,4,2],
 'equivariant_deterministic_map_count':64,'equivariant_bijection_count':4,
 'max_cycle_length_in_equivariant_bijections':2,
 'no_equivariant_full_eight_address_cycle':True,
 'changed_hypotheses':['extra state memory','broken S4 symmetry','different state-carrier rule'],
 'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
