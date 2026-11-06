#!/usr/bin/env python3
"""Exact K4 Q169/Q171 signed-current and conditional zero-top admission gate."""
import contextlib,io,runpy,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(Path(__file__).resolve().parent/'cross_complex_native_v17.py'))
A0,A1,F,D0,D1=z['A0'],z['A1'],z['Q'],z['D0'],z['D1']
e=s.zeros(15,1);e[14]=1
b=z['oldv']
assert e.dot(e)==b.dot(b)==1 and e.dot(b)==0
assert A0*e==2*b and A0*b==-2*e
Qt=e*e.T+b*b.T;P=s.eye(15)-Qt
assert P.rank()==13 and A0*P==P*A0
assert F.T*F-s.eye(15)==3*e*e.T and (F.T*F-s.eye(15))*P==s.zeros(15)
assert e.T*A0==-2*b.T
G=F.T*F;Pi=F*G.inv()*F.T
Rleak=(s.eye(29)-Pi)*A1*F
assert Rleak.T*Rleak==P
Err=A1*F-F*A0
assert (Err*P).rank()==13
assert (Err*P).T*(Err*P)-P==(Pi*Err*P).T*(Pi*Err*P)
assert (Err*b).dot(Err*b)==9
# Shared ascending orientation with source Q169 A=D-D.T.
B3=z['m1'][2];fo=z['b1'][2].index((0,1,2));to=z['b1'][3].index((0,1,2,4))
sigma=B3[fo,to];assert sigma==-1
assert A1[z['o1'][3]+to,z['o1'][2]+fo]==-sigma
# Source Q171 prints +2B3 for top derivative; that is face gain with same B3.
assert (2*sigma,-2*sigma)==(-2,2)
u,a,beta=s.symbols('u a beta',real=True)
at=a*s.cos(2*u)-beta*s.sin(2*u); S=at**2
assert s.simplify(s.diff(S,u,2).subs({a:0,u:0})-8*beta**2)==0
assert s.simplify(at.subs({a:1,beta:0,u:s.pi/4}))==0
assert s.simplify(at.subs({a:1,beta:1,u:s.pi/8}))==0
assert s.simplify(at.subs({a:1,beta:-1,u:3*s.pi/8}))==0
# Old invariant no-top-pair shell sector can nevertheless excite new top modes.
y=s.zeros(15,1);y[10]=1;y[11]=1
assert P*y==y and (e.T*A0*y)[0]==0
assert (A1*F*y)[25:29,:]!=s.zeros(4,1)
# Check all signed S4 permutations on the top plane.
from itertools import permutations
old_basis=z['b0']
for perm in permutations(range(4)):
 U=s.zeros(15);offset=0
 for lev in old_basis:
  ix={t:i for i,t in enumerate(lev)}
  for j,t in enumerate(lev):
   word=tuple(perm[v] for v in t)
   sign=(-1)**sum(word[i]>word[k] for i in range(len(word)) for k in range(i+1,len(word)))
   U[offset+ix[tuple(sorted(word))],offset+j]=sign
  offset+=len(lev)
 parity=(-1)**sum(perm[i]>perm[k] for i in range(4) for k in range(i+1,4))
 assert U*e==parity*e and U*b==parity*b and U*P*U.T==P
out={'status':'PASS_EXACT_CONDITIONAL','Q169_face_gain':'2 B3 cface ctop',
     'Q169_top_gain':'-2 B3 cface ctop',
     'Q171_literal_plus_B3_top_gain':'CONVENTION_COLLISION_IF_SAME_B3',
     'F_stock_defect':'3*a^2','instantaneous_eligible_iff':'a=0',
     'old_top':'a(u)=a*cos(2u)-beta*sin(2u)',
     'candidate_isolated_crossing_gate':'S_top=0, S_top_ddot>0',
     'isolated_crossing_spacing':'pi/2 native u',
     'equal_modal_norm2_timings':['pi/8','3pi/8'],
     'max_old_A0_invariant_isometric_subspace_rank':13,
     'first_leakage_gram':'R.T R=P13',
     'derivative_intertwining_no_go_on_P13':True,
     'prepared_first_switch_derivative_jump_squared':'9',
     'S4_signed_checks':24,'source_event_selected':False,'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
