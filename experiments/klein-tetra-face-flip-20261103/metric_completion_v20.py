#!/usr/bin/env python3
"""UD Discovery v2.0: exact barycentric chain-retraction metric completion.
Requires same-folder cross_complex_native_v17.py.
Changed metric and Hodge adjoint are CANDIDATE, not source Q165/Q169.
"""
import contextlib,io,runpy,json
from pathlib import Path
from itertools import permutations
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(Path(__file__).resolve().parent/'cross_complex_native_v17.py'))
A0,A1,D0,D1=z['A0'],z['A1'],z['D0'],z['D1']
F=z['Q'] if 'Q' in z else z['F']
b0,b1,o0,o1=z['b0'],z['b1'],z['o0'],z['o1']
P=s.zeros(15,29)
for k in range(4):
 idx={t:i for i,t in enumerate(b0[k])}
 for j,t in enumerate(b1[k]):
  if 4 not in t: P[o0[k]+idx[t],o1[k]+j]=1
  else:
   for a in range(4):
    w=tuple(a if v==4 else v for v in t)
    if len(set(w))<len(w): continue
    sg=(-1)**sum(w[i]>w[h] for i in range(len(w)) for h in range(i+1,len(w)))
    P[o0[k]+idx[tuple(sorted(w))],o1[k]+j]+=s.Rational(sg,4)
assert P*F==s.eye(15) and P*D1==D0*P
Q=s.eye(29)-F*P
H=P.T*P+Q.T*Q
assert F.T*H*F==s.eye(15) and H.det()!=0
AH=D1-H.inv()*D1.T*H
assert AH.T*H+H*AH==s.zeros(29)
assert AH*F==F*A0 and D1**2==s.zeros(29)
assert AH!=A1 and H!=s.eye(29)
for p in permutations(range(4)):
 p5=(*p,4)
 def signed(Ubasis,off):
  U=s.zeros(off[-1])
  for k,level in enumerate(Ubasis):
   idx={t:i for i,t in enumerate(level)}
   for j,t in enumerate(level):
    w=tuple(p5[i] for i in t)
    sg=(-1)**sum(w[i]>w[h] for i in range(len(w)) for h in range(i+1,len(w)))
    U[off[k]+idx[tuple(sorted(w))],off[k]+j]=sg
  return U
 U0,U1=signed(b0,o0),signed(b1,o1)
 assert U0*P==P*U1 and U1*F==F*U0
 assert U1.T*H*U1==H and U1*AH==AH*U1
result={
 'status':'PASS_EXACT_CONDITIONAL',
 'P_F':'I15','P_D1':'D0_P','F_transpose_H_F':'I15',
 'H':'P.T*P+(I29-F*P).T*(I29-F*P)',
 'H_positive':'||P*x||²+||Q*x||² and x=F*P*x+Q*x',
 'A_H':'D1-H^-1*D1.T*H',
 'H_skew':True,'A_H_F':'F_A0','S4_cases':24,
 'H_off_diagonal_unordered_pairs':sum(bool(H[i,j]) for i in range(29) for j in range(i+1,29)),
 'AH_changed_directed_entries':sum(AH[i,j]!=A1[i,j] for i in range(29) for j in range(29)),
 'AH_new_nonhasse_entries':sum(A1[i,j]==0 and AH[i,j]!=0 for i in range(29) for j in range(29)),
 'chi_AH':str(s.factor(AH.charpoly().as_expr())),
 'chi_A1':str(s.factor(A1.charpoly().as_expr())),
 'changed_metric_source_selected':False,'physical_promotion':0}
assert result['H_off_diagonal_unordered_pairs']==52
assert result['AH_changed_directed_entries']==50
assert result['AH_new_nonhasse_entries']==12
print(json.dumps(result,sort_keys=True,indent=2))
