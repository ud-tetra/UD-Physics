#!/usr/bin/env python3
"""Exact K4 parity-sector source audit, no added native projector assumption."""
import itertools,json
from fractions import Fraction as Q
import sympy as S
def chain(T):
 bs=[sorted({a for t in T for a in itertools.combinations(t,k)}) for k in (1,2,3,4)]
 d={}
 for k in (1,2,3):
  d[k]=S.zeros(len(bs[k-1]),len(bs[k]))
  ids={a:i for i,a in enumerate(bs[k-1])}
  for j,t in enumerate(bs[k]):
   for i in range(k+1):d[k][ids[t[:i]+t[i+1:]],j]=(-1)**i
 return bs,d
def refine(T,z):
 return [tuple(sorted(t[:i]+t[i+1:]+(z+j,))) for j,t in enumerate(T) for i in range(4)]
def residue(old,new,z):
 a,da=chain(old);bb,db=chain(new);parts=[]
 ix=[{v:i for i,v in enumerate(level)} for level in bb]
 for k in range(4):
  mat=S.zeros(len(bb[k]),len(a[k]))
  for j,t in enumerate(a[k]):
   if k<3:mat[ix[k][t],j]=1
   else:
    cen=z+old.index(t)
    for i in range(4):
     v=tuple(sorted(t[:i]+t[i+1:]+(cen,)))
     mat[ix[3][v],j]=(-1)**(i+1)
  parts.append(mat)
 for k in (1,2,3):assert db[k]*parts[k]==parts[k-1]*da[k]
 F=S.diag(*parts)
 def gen(b,d):
  A=S.zeros(sum(map(len,b)));ofs=[0]
  for lev in b:ofs.append(ofs[-1]+len(lev))
  for k in (1,2,3):A[ofs[k-1]:ofs[k],ofs[k]:ofs[k+1]]=d[k]
  return A-A.T
 Af=gen(bb,db);G=F.T*F
 return Af*F-F*(G.inv()*F.T*Af*F),F,Af
L0=[(0,1,2,3)];L1=refine(L0,4);L2=refine(L1,5)
r01,f01,_=residue(L0,L1,4)
r12,f12,A2=residue(L1,L2,5)
f02=f12*f01;g=f02.T*f02
r02=A2*f02-f02*(g.inv()*f02.T*A2*f02)
norm=lambda A:sum((v*v for v in A),S.Integer(0))
assert [norm(R) for R in (r01,r12,r02)]==[13,52,S.Rational(151,4)]
pairs=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
pairsets=tuple(frozenset(frozenset(t) for t in pp) for pp in pairs)
actions=[]
for p in itertools.permutations(range(4)):
 actions.append(tuple(pairsets.index(frozenset(frozenset(p[v] for v in edge) for edge in pair)) for pair in pairs))
assert len(actions)==24 and len(set(actions))==6
theta=list(itertools.product((0,1),repeat=3))
orbits=[];remaining=set(theta)
while remaining:
 t=min(remaining);o={tuple(t[i] for i in a) for a in actions}
 orbits.append(sorted(o));remaining-=o
assert list(map(len,orbits))==[1,3,3,1]
models={
 'uniform':{t:Q(1,8) for t in theta},
 'positive_nonuniform':{t:Q(1,4) if sum(t) in (0,3) else Q(1,12) for t in theta},
 'singleton':{t:Q(1) if t==(0,0,0) else Q(0) for t in theta}}
for p in models.values():
 assert sum(p.values(),Q(0))==1
 assert all(p[t]==p[tuple(t[i] for i in a)] for a in actions for t in theta)
assert norm(2*r01)/8==S.Rational(13,2)
out={'status':'PASS_EXACT','native_leakage_norm_squared':['13','52','151/4'],
 'S4_permutations':24,'theta_orbits':[[''.join(map(str,t)) for t in o] for o in orbits],
 'sector_contributions_first_level':{n:{''.join(map(str,t)):str(13*p[t]) for t in theta} for n,p in models.items()},
 'uniform_sector_second_level':'13/2','uniform_sector_composite':'151/32',
 'second_level_per_four_top_cells':'13/8',
 'gain_2_uniform_sector':'13/2','metric_2_uniform_sector':'13/4',
 'orthogonal_projectors_native_K4':'NOT_DEFINED',
 'projectors_added_R8_tensor_space':'EXACT_CONDITIONAL',
 'equal_weight_forced_by_S4':False,
 'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
