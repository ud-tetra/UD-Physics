#!/usr/bin/env python3
"""Exact K4 1->4 control; source-defined event selector NOT assumed."""
from itertools import combinations, permutations
import sympy as S,json
T0=[(0,1,2,3)]
T1=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
def make(tets):
 c=[sorted({z for t in tets for z in combinations(t,k+1)}) for k in range(4)]
 B=[None]
 for k in (1,2,3):
  b=S.zeros(len(c[k-1]),len(c[k]))
  for j,t in enumerate(c[k]):
   for i in range(k+1):b[c[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
  B.append(b)
 off=[0]
 for x in c:off.append(off[-1]+len(x))
 D=S.zeros(off[-1])
 for k in (1,2,3):D[off[k-1]:off[k],off[k]:off[k+1]]=B[k]
 assert D*D==S.zeros(off[-1])
 return c,B,D,D.T-D,off
old,bo,do,ao,oo=make(T0);new,bn,dn,an,on=make(T1)
T=[]
for k in range(4):
 t=S.zeros(len(new[k]),len(old[k]))
 if k<3:
  for j,x in enumerate(old[k]):t[new[k].index(x),j]=1
 else:
  for i in range(4):
   x=tuple(z for z in range(4) if z!=i)+(4,)
   t[new[3].index(x),0]=(-1)**(i+1)
 T.append(t)
for k in (1,2,3):assert bn[k]*T[k]==T[k-1]*bo[k]
F=S.diag(*T)
assert F.T*F==S.diag(*([1]*14+[4]))
P=T[3]/4;M=S.diag(*([S.Rational(3,2)]*4))
assert P.T*M*P==S.Matrix([[S.Rational(3,8)]])
assert ao.charpoly().as_expr().factor()==S.Symbol('lambda')*(S.Symbol('lambda')**2+4)**7
assert an.charpoly().as_expr().factor()==S.Symbol('lambda')*(S.Symbol('lambda')**2+1)*(S.Symbol('lambda')**2+5)**13
Lold=bo[1]*bo[1].T;Lnew=bn[1]*bn[1].T
Lam=Lnew[:4,:4]-Lnew[:4,4:5]*Lnew[4:5,4:5].inv()*Lnew[4:5,:4]
assert Lam==S.Rational(5,4)*Lold
x=S.zeros(29,1);x[0]=1
assert (an*x)[4]==0 and (an**2*x)[4]==1
def rep(basis,p):
 off=[0]
 for a in basis:off.append(off[-1]+len(a))
 R=S.zeros(off[-1]);pi={**{i:p[i] for i in range(4)},4:4}
 for k,simp in enumerate(basis):
  for j,t in enumerate(simp):
   v=[pi[i] for i in t]
   sign=(-1)**sum(v[i]>v[h] for i in range(len(v)) for h in range(i+1,len(v)))
   R[off[k]+simp.index(tuple(sorted(v))),off[k]+j]=sign
 return R
for p in permutations(range(4)):
 assert rep(new,p)*F==F*rep(old,p)
print(json.dumps({"pass":True,"f_pre":[4,6,4,1],"f_post":[5,10,10,4],"S4_tests":24,"chain_gram_top":4,"Whitney_top_pullback":"3/8","boundary_mode":"4->5","event_selector":"OPEN","physical_promotion":0},indent=2))
