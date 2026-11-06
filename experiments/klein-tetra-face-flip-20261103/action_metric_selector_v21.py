#!/usr/bin/env python3
"""Exact K4 intercomplex metric selector audit v2.1.
Depends on same-folder metric_completion_v20.py and cross_complex_native_v17.py.
H_t is a CANDIDATE changed metric, not source Q165/Q169.
"""
import contextlib,io,json,runpy
from itertools import permutations
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 v=runpy.run_path(str(Path(__file__).resolve().parent/'metric_completion_v20.py'))
P,F,D1,D0,A0,A1,Q=v['P'],v['F'],v['D1'],v['D0'],v['A0'],v['A1'],v['Q']
assert P*F==s.eye(15) and P*D1==D0*P and D1*F==F*D0
assert Q==s.eye(29)-F*P and Q**2==Q and D1*Q==Q*D1
assert F.T*F==s.diag(*([1]*14+[4]))
p=P.T*P;q=Q.T*Q;generators=[];records=[]
for t in (s.Rational(1,4),s.Integer(1),s.Integer(2)):
 H=p+t*q
 AH=D1-H.inv()*D1.T*H
 assert H.T==H and H.rank()==29 and H!=s.eye(29)
 assert F.T*H*F==s.eye(15)
 assert F.T*H*Q==s.zeros(15,29)
 assert AH.T*H+H*AH==s.zeros(29)
 assert AH*F==F*A0 and AH!=A1
 generators.append(AH)
 records.append({'t':str(t),'rank':29,'isometric':True,
   'offdiag_pairs':sum(bool(H[i,j]) for i in range(29) for j in range(i+1,29))})
assert generators[0]==generators[1]==generators[2]
# New-only mode demonstrates unconstrained normalization.
cent=s.zeros(29,1);cent[4]=1;y=Q*cent
assert P*y==s.zeros(15,1) and y.dot(y)==s.Rational(5,4)
for t,z in [(s.Rational(1,4),s.Rational(5,16)),(s.Integer(1),s.Rational(5,4)),(s.Integer(2),s.Rational(5,2))]:
 assert (y.T*(p+t*q)*y)[0]==z
# Two individual newborn Q165 unit basis requirements contradict each other.
e=s.zeros(29,1);e[v['o1'][1]+v['b1'][1].index((0,4))]=1
assert (cent.T*p*cent)[0]==s.Rational(1,4)
assert (cent.T*q*cent)[0]==s.Rational(5,4)
assert (e.T*p*e)[0]==s.Rational(3,16)
assert (e.T*q*e)[0]==s.Rational(19,16)
assert s.Rational(3,5)!=s.Rational(13,19)
# All source S4 relabelings preserve BOTH quadratic forms separately.
for perm in permutations(range(4)):
 U=s.zeros(29);p5=(*perm,4)
 for k,level in enumerate(v['b1']):
  idx={c:i for i,c in enumerate(level)}
  for j,c in enumerate(level):
   w=tuple(p5[u] for u in c)
   sign=(-1)**sum(w[i]>w[h] for i in range(len(w)) for h in range(i+1,len(w)))
   U[v['o1'][k]+idx[tuple(sorted(w))],v['o1'][k]+j]=sign
 assert U.T*p*U==p and U.T*q*U==q
 assert U*generators[1]==generators[1]*U
out={'status':'PASS_EXACT_CONDITIONAL_SOURCE_BLOCKED',
 'H_family':'H_t=P.T*P+t Q.T*Q, t>0',
 'valid_t':'all strictly positive real t (direct-sum algebra proof)',
 'tested_t':records,'same_full_generator_all_t':True,'S4_signed_cases':24,
 'P_F':'I15','P_D1':'D0P','Q_rank':14,
 'F_T_H_t_F':'I15 for all positive t',
 'A_t_F':'F A0 for all positive t',
 'new_centroid_complement_H_t_norm':'5t/4',
 'centroid_basis_unit_requires_t':'3/5',
 'new_edge_04_basis_unit_requires_t':'13/19',
 'source_unit_metric_and_F_isometry_compatible':False,
 'independent_action_source_selects_t':False,
 'Q171_issue_338':'OPEN, NO ACCEPTED DECISION','physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
