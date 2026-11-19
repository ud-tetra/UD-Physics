#!/usr/bin/env python3
"""Exact v1.9 interface: all Q170 shell cuts match at top-zero instant,
but native old/new shared accelerations differ by 4bb^T-I14.
Run adjacent to sign_admission_v18.py (and cross_complex_native_v17.py).
"""
import runpy,contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 z=runpy.run_path(str(Path(__file__).resolve().parent/'sign_admission_v18.py'))
A0,A1,F,b=z['A0'],z['A1'],z['F'],z['b']
T=F[:,:14]                          # exact shared 14 original simplices
N=s.eye(29)-T*T.T                   # 15 new simplices
Lnew=N*A1*T
Lold=z['e'].T*A0*T                 # old single removed top row
bb=b[:14,:]
assert T.T*T==s.eye(14) and N.rank()==15
assert T.T*A1*T==A0[:14,:14]
assert Lnew.T*Lnew==s.eye(14)
assert Lold==-2*bb.T and Lold.T*Lold==4*bb*bb.T
M=T.T*(A1*A1)*T-(A0*A0)[:14,:14]
assert M==4*bb*bb.T-s.eye(14)
assert M.eigenvals()=={s.Integer(-1):13,s.Integer(3):1}
assert M.rank()==14
# Exact all-cuts first-jet match follows from the shared A block identity.
# One independently fixed rational fixture checks all 2^14 cut sums.
x=s.Matrix([s.Rational(i-3,7) for i in range(14)])
old=s.Matrix.vstack(x,s.zeros(1,1));new=T*x
fo=A0*old;fn=T.T*A1*new
assert fn==fo[:14,:]
out_old=[2*x[i]*fo[i] for i in range(14)]
out_new=[2*x[i]*fn[i] for i in range(14)]
assert out_old==out_new
for mask in range(1<<14):
 ids=[i for i in range(14) if mask>>i&1]
 assert sum(out_old[i] for i in ids)==sum(out_new[i] for i in ids)
# For normalized boundary mode b, removed/created stock slopes differ 8 vs2.
assert (Lnew*bb).dot(Lnew*bb)==1 and (Lold*bb).dot(Lold*bb)==4
print(json.dumps({'status':'PASS_EXACT_CONDITIONAL',
 'instantaneous_shared_cut_Q170':'ALL 2^14 PASS',
 'old_shell_dim':14,'new_complement_dim':15,
 'new_cone_derivative_gram':'I14',
 'old_removed_top_derivative_gram':'4bbT',
 'shared_acceleration_difference':'4bbT-I14',
 'eigenvalues':{'3':1,'-1':13},'rank':14,
 'boundary_mode_old_vs_new_cut_slopes':[8,2],
 'source_selected_refinement_event':False,'physical_promotion':0},indent=2))
