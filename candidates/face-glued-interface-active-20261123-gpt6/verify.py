#!/usr/bin/env python3
"""EXACT: face-glued two K4s, invariant active interface, signed symmetry."""
from itertools import combinations,permutations
import sympy as S
simp=[sorted({q for t in [(0,1,2,3),(0,1,2,4)] for q in combinations(t,k+1)}) for k in range(4)]
off=[0]
for arr in simp:off.append(off[-1]+len(arr))
D=S.zeros(23)
B=[None]
for k in (1,2,3):
 b=S.zeros(len(simp[k-1]),len(simp[k]))
 for j,t in enumerate(simp[k]):
  for i in range(k+1):b[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
 B.append(b);D[off[k-1]:off[k],off[k]:off[k+1]]=b
assert B[1]*B[2]==S.zeros(5,7) and B[2]*B[3]==S.zeros(9,2)
A=D.T-D;z=S.symbols('z')
assert S.factor(A.charpoly(z).as_expr())==z*(z*z+3)**4*(z*z+5)**7
assert B[3].T*B[3]==S.Matrix([[4,1],[1,4]])
v=S.zeros(23,1);v[off[2]+simp[2].index((0,1,2))]=1
u=A*v;P=v*v.T+u*u.T/5
assert (u.T*u)[0]==5 and u.T*v==S.zeros(1) and A*u==-5*v
assert P*P==P and P*A==A*P and P.rank()==2
assert [(simp[1][i],u[off[1]+i]) for i in range(9) if u[off[1]+i]]==[((0,1),-1),((0,2),1),((1,2),-1)]
assert u[off[2]:off[3],:]==S.zeros(7,1) and u[off[3]:off[4],:]==S.Matrix([-1,-1])
for p in permutations((0,1,2)):
 for swap in (False,True):
  g={0:p[0],1:p[1],2:p[2],3:4 if swap else 3,4:3 if swap else 4}
  R=S.zeros(23)
  for k,arr in enumerate(simp):
   for j,t in enumerate(arr):
    q=[g[a] for a in t]
    sign=(-1)**sum(q[i]>q[h] for i in range(len(q)) for h in range(i+1,len(q)))
    R[off[k]+arr.index(tuple(sorted(q))),off[k]+j]=sign
  assert R.T*R==S.eye(23) and R*A==A*R and R*P==P*R
s=S.symbols('s',real=True)
x=S.cos(S.sqrt(5)*s)*v+S.sin(S.sqrt(5)*s)*u/S.sqrt(5)
assert S.simplify(x.dot(x)-1)==0
assert S.simplify(x[off[3]:off[4],:].dot(x[off[3]:off[4],:])-2*S.sin(S.sqrt(5)*s)**2/5)==0
print('PASS: f=(5,9,7,2), rank P=2, omega^2=5, 12 signed automorphisms')
