#!/usr/bin/env python3
"""UD Discovery v2.0: exact local cone, masks, clock and nonnative contact witness.
Requires same-folder cross_complex_native_v17.py; all arithmetic exact.
"""
import contextlib,io,runpy,json
from itertools import product,permutations
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(Path(__file__).resolve().parent/'cross_complex_native_v17.py'))
A0,A1,D0,D1=z['A0'],z['A1'],z['D0'],z['D1']
F=z['Q'] if 'Q' in z else z['F'];T=F[:,:14]
N=s.eye(29)-T*T.T;C=N*A1*T
b=z['oldv'][:14,:] if 'oldv' in z else s.Matrix([0]*10+[-s.Rational(1,2),s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2)])
e=s.zeros(15,1);e[14]=1;Lo=e.T*A0[:,:14]
assert Lo==-2*b.T
old=Lo.T*Lo
assert C.T*C==s.eye(14) and old==4*b*b.T and old.rank()==1
M=old-s.eye(14)
assert M.eigenvals()=={s.Integer(3):1,s.Integer(-1):13}
assert s.trace(M.T*M)==22
off=sum(old[i,j]**2 for i in range(14) for j in range(14) if i!=j)
assert off==12
mask_scores=[]
for h in product((0,1),repeat=4):
 W=s.diag(*([1]*10+list(h)))
 mask_scores.append(int(s.trace((old-W.T*W)**2)))
assert min(mask_scores)==22 and max(mask_scores)==26
As=T.T*A1*T
assert As!=s.zeros(14) and As.T==-As and M.T==M
h=C*b
assert h.dot(h)==1 and N*A1*h==s.zeros(29,1)
Cs=h*Lo
assert Cs.T*Cs==old and Cs.rank()==1
B=Cs-C;Ast=A1+B*T.T-T*B.T
assert Ast.T==-Ast
S=s.zeros(29,15);S[:,:14]=T;S[:,14]=h
assert S.T*S==s.eye(15) and Ast*S==S*A0
Dst=s.zeros(29)
for lo,mid,hi in ((0,5,15),(5,15,25),(15,25,29)):
 Dst[lo:mid,mid:hi]=Ast[lo:mid,mid:hi]
assert Dst*Dst==s.zeros(29) and Dst*S==S*D0
assert D1*S!=S*D0
nonhasse=sum(A1[i,j]==0 and Ast[i,j]!=0 for i in range(29) for j in range(i+1,29))
changed=sum(A1[i,j]!=Ast[i,j] for i in range(29) for j in range(i+1,29))
assert nonhasse==12 and changed==26
for p in permutations(range(4)):
 p5=(*p,4); U=s.zeros(29)
 for k,level in enumerate(z['b1']):
  idx={t:i for i,t in enumerate(level)}
  for j,t in enumerate(level):
   w=tuple(p5[v] for v in t)
   sg=(-1)**sum(w[i]>w[h] for i in range(len(w)) for h in range(i+1,len(w)))
   U[z['o1'][k]+idx[tuple(sorted(w))],z['o1'][k]+j]=sg
 assert U*Ast==Ast*U
out={'status':'PASS_EXACT_CONDITIONAL','native_cone_rank':14,
 'old_top_contact_rank':1,'native_mismatch_squared_Frobenius':22,
 'best_diagonal_local_weight_residual_squared':12,
 'Q173_like_four_outer_face_binary_mask_mismatch_range':[min(mask_scores),max(mask_scores)],
 'clock_scalar_no_universal_repair':True,
 'coherent_alternative_rank':1,'coherent_Astar_S_equals_S_A0':True,
 'coherent_Dstar_squared_zero':True,'coherent_Dstar_chainmap':True,
 'coherent_S_is_original_integral_F':False,
 'coherent_added_nonHasse_couplings':nonhasse,
 'coherent_changed_undirected_pairs':changed,
 'S4_actions':24,'source_selected_coherent_contact':False,'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
