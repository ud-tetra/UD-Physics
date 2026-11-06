#!/usr/bin/env python3
"""Full exact pulled-back orientation local system on the 72-tetrahedron K x I quotient."""
import runpy, json
from pathlib import Path
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ, QQ
from sympy.polys.matrices import DomainMatrix
P=Path(__file__).resolve().parent
base=runpy.run_path(str(P/'bulk_prism_v04.py'))
simp, objects, PAIRS, key, UF=tuple(base[k] for k in ('simp','objects','PAIRS','key','UF'))
# The Klein orientation character on seam pairs h,v,x is (1,0,1).
w=(1,0,1)
uf=[UF() for _ in range(4)]
for d in range(4):
 for cell in simp[d]:
  for sh in (0,1): uf[d].root((sh,cell))
for i,((a,bb),(c,dd),qa,qb) in enumerate(PAIRS):
 side=frozenset(((a,0),(a,1),(bb,0),(bb,1)))
 mp={(a,h):(c,h) for h in (0,1)}
 mp.update({(bb,h):(dd,h) for h in (0,1)})
 for n in range(3):
  for flag in simp[n]:
   if not all(q==qa and objects[(q,j,cell)].issubset(side) for q,j,cell in flag):
    continue
   image=tuple(key(qb,j,frozenset(mp[z] for z in objects[(q,j,cell)])) for q,j,cell in flag)
   assert image in simp[n]
   for sh in (0,1):uf[n].union((sh,flag),(sh^w[i],image))
rep=[]; lookup=[]
for d in range(4):
 orbits=[];seen=set();index={}
 for flag in sorted(simp[d]):
  a=uf[d].root((0,flag)); bb=uf[d].root((1,flag))
  assert a!=bb
  pair=frozenset((a,bb))
  if pair not in seen:
   seen.add(pair);index[a]=(len(orbits),1);index[bb]=(len(orbits),-1)
   orbits.append((a,bb))
 assert len(orbits)==[18,102,156,72][d]
 rep.append(orbits);lookup.append(index)
boundary={}
for d in (1,2,3):
 mat=S.zeros(len(rep[d-1]),len(rep[d]))
 by_class={uf[d].root((sh,cell)):(sh,cell) for sh in (0,1) for cell in simp[d]}
 for j,(a,_) in enumerate(rep[d]):
  sh,flag=by_class[a]
  for z in range(d+1):
   lower=uf[d-1].root((sh,flag[:z]+flag[z+1:]))
   row,sign=lookup[d-1][lower]
   mat[row,j]+=(-1)**z*sign
 boundary[d]=mat
assert boundary[1]*boundary[2]==S.zeros(18,156)
assert boundary[2]*boundary[3]==S.zeros(102,72)
ranks=[int(DomainMatrix.from_Matrix(boundary[k]).convert_to(QQ).rank()) for k in (1,2,3)]
assert ranks==[18,83,72]
smith=smith_normal_form(boundary[1],domain=ZZ)
diag=[abs(int(smith[i,i])) for i in range(18)]
assert diag==[1]*17+[2],diag
out={'complex':'twisted 72-tetrahedron Klein x I via orientation double cover anti-invariants',
 'orientation_seam_labels_hvx':[1,0,1], 'cover_counts':[36,204,312,144],
 'twisted_counts':[18,102,156,72], 'rank_d1_d2_d3':ranks,
 'twisted_Betti_over_Q':[0,1,1,0], 'Smith_d1':diag,
 'H0_over_Z':'Z/2Z','boundary_squared_zero':True,
 'full_integral_H1_H2_Smith':'not computed; source cellular equivalence predicts H1=Z,H2=Z',
 'physical_promotion':0,'status':'PASS_EXACT_CONDITIONAL'}
print(json.dumps(out,indent=2,sort_keys=True))
