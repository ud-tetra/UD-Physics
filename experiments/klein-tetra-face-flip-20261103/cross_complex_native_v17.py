#!/usr/bin/env python3
"""Exact source-native K4 1->4 transfer and face-mask gate v1.7 (SymPy).
Q173 masked readout is NOT a change of source Q169 boundary dynamics.
"""
import itertools,json
import sympy as s
def complex_(tops):
 B=[sorted({t for T in tops for t in itertools.combinations(T,k)}) for k in range(1,5)]
 m=[]
 for k in range(1,4):
  X=s.zeros(len(B[k-1]),len(B[k]));idx={t:i for i,t in enumerate(B[k-1])}
  for j,T in enumerate(B[k]):
   for i in range(k+1):X[idx[T[:i]+T[i+1:]],j]=(-1)**i
  m.append(X)
 offsets=[0]
 for g in B:offsets.append(offsets[-1]+len(g))
 D=s.zeros(offsets[-1])
 for k in range(1,4):D[offsets[k-1]:offsets[k],offsets[k]:offsets[k+1]]=m[k-1]
 assert D*D==s.zeros(D.rows)
 return B,m,D,D-D.T,offsets
old=[(0,1,2,3)]
new=[tuple(sorted(old[0][:i]+old[0][i+1:]+(4,))) for i in range(4)]
b0,m0,D0,A0,o0=complex_(old)
b1,m1,D1,A1,o1=complex_(new)
F=[]
for grade in range(4):
 X=s.zeros(len(b1[grade]),len(b0[grade]));idx={z:i for i,z in enumerate(b1[grade])}
 for j,T in enumerate(b0[grade]):
  if grade!=3:X[idx[T],j]=1
  else:
   for i in range(4):X[idx[tuple(sorted(T[:i]+T[i+1:]+(4,)))],j]=(-1)**(i+1)
 F.append(X)
Q=s.diag(*F)
assert D1*Q==Q*D0
assert Q.T*Q-s.eye(15)==s.diag(*([0]*14+[3]))
assert m1[2].rank()==4
assert (F[3]/2).T*(F[3]/2)==s.ones(1)
assert m1[2]*(F[3]/2)!=m0[2]
v=s.zeros(29,1)
for j,face in enumerate(b0[2]):
 v[o1[2]+b1[2].index(face)]=m0[2][j,0]/2
w=A1*v
assert v.dot(v)==w.dot(w)==1 and v.dot(w)==0 and A1*w==-v
oldv=s.zeros(15,1)
oldv[o0[2]:o0[3],:]=m0[2][:,0]/2
assert A0**2*oldv==-4*oldv
faces=b1[2];outer=[i for i,f in enumerate(faces) if 4 not in f]
inner=[i for i,f in enumerate(faces) if 4 in f]
assert len(outer)==4 and len(inner)==6
s4mask=[];chainmasks=[]
for h in itertools.product((0,1),repeat=10):
 if all(h[j]==h[outer[0]] for j in outer) and all(h[j]==h[inner[0]] for j in inner):s4mask.append(h)
 if m1[1]*s.diag(*h)*m1[2]==s.zeros(10,4):chainmasks.append(h)
assert len(s4mask)==4 and chainmasks==[(0,)*10,(1,)*10]
assert A1[o1[3]+b1[3].index((0,1,2,4)),o1[2]+b1[2].index((0,1,2))]==1
assert m1[2][b1[2].index((0,1,2)),b1[3].index((0,1,2,4))]==-1
out={'status':'PASS_EXACT_CONDITIONAL','old_f':[len(x) for x in b0],'new_f':[len(x) for x in b1],
 'full_Q165_stock_defect':'3*c_oldtop^2','unique_boundary_top_lift':True,
 'isometric_shared_shell_rank':14,'new_top_unit_derivative':True,
 'exact_new_shell_stock':'cos(u)^2','exact_new_top_stock':'sin(u)^2',
 'postevent_formal_frequency':1,'old_formal_frequency':2,
 'face_mask_count':1024,'S4_invariant_masks':4,'d_squared_zero_masks':2,
 'Q173_mask_readout_is_not_generator':True,
 'Q171_literal_plus_B3_sign_vs_A_d_minus_dT':'OPEN_CONVENTION_GATE',
 'source_selected_refinement_trigger':False,'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
