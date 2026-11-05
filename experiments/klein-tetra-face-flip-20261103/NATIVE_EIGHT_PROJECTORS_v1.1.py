#!/usr/bin/env python3
"""Exact native K4 eight-projector resolution and first/second refinement audit.

Source inputs: K4 signed oriented simplicial boundary, H=I, J=(d-d.T)/2,
opposite-edge pairs (01,23),(02,13),(03,12). The correspondence of these
real subspaces with the eight F2^3 labels is a proposed, non-unique bridge.
No new Hilbert fiber, empirical Planck unit or physical clock is introduced.
"""
import sympy as s
import json
from itertools import combinations,permutations

pairs=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
def basis(cells):
 return [sorted({t for T in cells for t in combinations(T,k)}) for k in (1,2,3,4)]
def boundaries(b):
 D=[]
 for k in range(1,4):
  m=s.zeros(len(b[k-1]),len(b[k])); idx={z:i for i,z in enumerate(b[k-1])}
  for j,t in enumerate(b[k]):
   for i in range(k+1):m[idx[t[:i]+t[i+1:]],j]=(-1)**i
  D.append(m)
 assert D[0]*D[1]==s.zeros(D[0].rows,D[1].cols)
 assert D[1]*D[2]==s.zeros(D[1].rows,D[2].cols)
 return D
def generator(b,D):
 off=[0]
 for z in b:off.append(off[-1]+len(z))
 d=s.zeros(off[-1])
 for k,m in enumerate(D,1):d[off[k-1]:off[k],off[k]:off[k+1]]=m
 return d-d.T
def refinement(parent,child,z):
 bp,bc=basis(parent),basis(child);Dparent=boundaries(bp);Dchild=boundaries(bc)
 offp=[0];offc=[0]
 for a in bp:offp.append(offp[-1]+len(a))
 for a in bc:offc.append(offc[-1]+len(a))
 F=s.zeros(offc[-1],offp[-1]);blocks=[]
 for k in range(4):
  ids={t:i for i,t in enumerate(bc[k])}
  M=s.zeros(len(bc[k]),len(bp[k]))
  for j,T in enumerate(bp[k]):
   if k<3:M[ids[T],j]=1
   else:
    for i in range(4):
     ch=tuple(sorted(T[:i]+T[i+1:]+(z+j,)))
     M[ids[ch],j]=(-1)**(i+1)
  blocks.append(M)
  F[offc[k]:offc[k+1],offp[k]:offp[k+1]]=M
 for k in (1,2,3):assert Dchild[k-1]*blocks[k]==blocks[k-1]*Dparent[k-1]
 Af=generator(bc,Dchild);G=F.T*F
 R=Af*F-F*G.inv()*F.T*Af*F
 return R,F,Af,G
parent=[(0,1,2,3)];bp=basis(parent)
A=generator(bp,boundaries(bp));J=A/2
assert J**3==-J and (J.T*J).rank()==14
Q={};h=s.zeros(15,1)
for i in range(4):h[i]=s.Rational(1,2)
Q['000']=h*h.T
ids={t:4+i for i,t in enumerate(bp[1])}
for k,opp in enumerate(pairs):
 W=s.zeros(15,2)
 for i,t in enumerate(opp):W[ids[t],i]=1
 assert W.T*W==s.eye(2) and (J*W).T*(J*W)==s.eye(2)
 Q[('100','010','001')[k]]=W*W.T
 Q[('011','101','110')[k]]=J*W*W.T*J.T
v=s.zeros(15,1);v[14]=1
assert (J*v).dot(J*v)==1
Q['111']=v*v.T+(J*v)*(J*v).T
assert sum(Q.values(),s.zeros(15))==s.eye(15)
for theta,P in Q.items():
 assert P.T==P and P*P==P
 for phi,N in Q.items():
  if theta!=phi:assert P*N==s.zeros(15)
assert [int(Q[t].rank()) for t in sorted(Q)]==[1,2,2,2,2,2,2,2]
for perm in permutations(range(4)):
 U=s.zeros(15);off=0
 for lev in bp:
  idx={t:i for i,t in enumerate(lev)}
  for j,t in enumerate(lev):
   w=tuple(perm[z] for z in t)
   sign=(-1)**sum(w[i]>w[k] for i in range(len(w)) for k in range(i+1,len(w)))
   U[off+idx[tuple(sorted(w))],off+j]=sign
  off+=len(lev)
 assert U*J==J*U and U.T*U==s.eye(15)
 for k,opp in enumerate(pairs):
  moved=frozenset(frozenset(perm[z] for z in edge) for edge in opp)
  target=next(j for j,pp in enumerate(pairs) if moved==frozenset(map(frozenset,pp)))
  for labels in (('100','010','001'),('011','101','110')):
   assert U*Q[labels[k]]*U.T==Q[labels[target]]
 for t in ('000','111'):assert U*Q[t]*U.T==Q[t]
for a,b in zip(('100','010','001'),('011','101','110')):
 assert J*Q[a]*J.T==Q[b] and J*Q[b]*J.T==Q[a]
 assert A*(Q[a]+Q[b])==(Q[a]+Q[b])*A and A*Q[a]!=Q[a]*A
assert A*Q['000']==Q['000']*A and A*Q['111']==Q['111']*A
children=[tuple(sorted(parent[0][:i]+parent[0][i+1:]+(4,))) for i in range(4)]
R01,F01,A1,G01=refinement(parent,children,4)
gram=R01.T*R01
assert gram==s.eye(15)-Q['111'] and gram.rank()==13 and gram**2==gram
score={t:s.trace(P*gram) for t,P in sorted(Q.items())}
assert {t:str(x) for t,x in score.items()}=={'000':'1','001':'2','010':'2','011':'2','100':'2','101':'2','110':'2','111':'0'}
assert sum(score.values())==13
assert all(gram*P==P*gram for P in Q.values())
assert (gram*A-A*gram)==s.zeros(15)
children2=[tuple(sorted(T[:i]+T[i+1:]+(5+j,))) for j,T in enumerate(children) for i in range(4)]
R12,F12,A2,G12=refinement(children,children2,5)
F02=F12*F01;G02=F02.T*F02
R02=A2*F02-F02*G02.inv()*F02.T*A2*F02
norm=lambda M:sum((z*z for z in M),s.Integer(0))
assert (norm(R01),norm(R12),norm(R02))==(13,52,s.Rational(151,4))
score02={t:s.trace(P*R02.T*R02) for t,P in sorted(Q.items())}
assert sum(score02.values())==s.Rational(151,4)
B02=R02.T*R02
rank_commute02={t:(B02*P-P*B02).rank() for t,P in sorted(Q.items())}
assert (B02*A-A*B02).rank()==14
T=F01*s.diag(*([1]*14+[s.Rational(1,2)]))
assert T.T*T==s.eye(15)
Qup={t:T*P*T.T for t,P in Q.items()}
assert sum(Qup.values(),s.zeros(29))==T*T.T
rest=s.eye(29)-T*T.T
assert rest.rank()==14
score12={t:s.trace(P*R12.T*R12) for t,P in sorted(Qup.items())}
remainder=s.trace(rest*R12.T*R12)
assert sum(score12.values())==27 and remainder==25
assert norm(R12)==sum(score12.values())+remainder
out={'status':'PASS_EXACT_CONDITIONAL','source_native_real_C15':True,
 'added_Hilbert_fiber':False,
 'Theta_assignment':'CANDIDATE: 000 harmonic, weight1 edge pairs, weight2 J(edge pairs), 111 top/Jtop',
 'projector_ranks':{t:int(P.rank()) for t,P in sorted(Q.items())},
 'projectors_sum_I15':True,'projectors_orthogonal':True,'S4_signed_actions_checked':24,
 'A0_sector_dynamics':'three paired rank4 sectors invariant; weight1 and 2 individually exchange under J; 000 static, 111 top-plane invariant',
 'first_leakage_gram_identity':'R01.T*R01=I15-Q111',
 'first_leakage_singular_values':'1 multiplicity13, 0 multiplicity2',
 'first_leakage_sector_scores':{t:str(x) for t,x in score.items()},
 'arithmetic_mean_eight_labels':'13/8',
 'equal_sectors':False,
 'first_leakage_gram_commutes_all_projectors':True,
 'first_leakage_gram_commutes_A0':True,
 'direct_second_composite_scores':{t:str(x) for t,x in score02.items()},
 'direct_second_composite_total':'151/4',
 'direct_second_composite_commutator_ranks':rank_commute02,
 'direct_second_composite_gram_commutes_A0':False,
 'second_step_inherited_scores':{t:str(x) for t,x in score12.items()},
 'second_step_inherited_sum':'27','new_14D_complement_leakage':'25',
 'second_step_total':'52','full_eight_resolution_at_level1':False,
 'metric_or_gain_scale2_average':'13/4 or 13/2, respectively',
 'physical_Planck_bridge':False,'physical_promotion':0}
print(json.dumps(out,indent=2,sort_keys=True))
