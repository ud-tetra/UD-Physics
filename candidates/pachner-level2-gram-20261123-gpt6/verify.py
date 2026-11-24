#!/usr/bin/env python3
"""Exact 16-cell level-two Pachner Gram, S4 symmetry and collective ODE audit."""
import itertools
import sympy as S
pairs=[(i,i) for i in range(4)]+[(i,j) for i in range(4) for j in range(4) if j!=i]
A=S.zeros(16)
for a,(i,j) in enumerate(pairs):
 for b,(k,l) in enumerate(pairs):
  if a!=b and (i==k or (i==l and j==k and i!=j)): A[a,b]=1
assert A==A.T
G=4*S.eye(16)-A
assert G*S.ones(16,1)==S.Matrix([1]*4+[0]*12)
z=S.symbols('z')
cp=S.factor(G.charpoly(z).as_expr())
target=(z-6)**3*(z-4)**2*(z**2-5*z+1)*(z**3-11*z*z+35*z-26)**3
assert S.expand(cp-target)==0 and G.det()!=0
for p in itertools.permutations(range(4)):
 R=S.zeros(16)
 for a,(i,j) in enumerate(pairs):R[pairs.index((p[i],p[j])),a]=1
 assert R.T*R==S.eye(16) and R*G==G*R
# S4 character multiplicities of 16D ordered pair module.
types={(1,1,1,1):(1,4,[1,3,2,3,1]),(2,1,1):(6,2,[1,1,0,-1,-1]),
       (2,2):(3,0,[1,-1,2,-1,1]),(3,1):(8,1,[1,0,-1,0,1]),
       (4,):(6,0,[1,-1,0,1,-1])}
multiplicities=[sum(n*f*f*chars[a] for n,f,chars in types.values())//24 for a in range(5)]
assert multiplicities==[2,3,1,1,0]
Gs=S.Matrix([[4,-3],[-1,1]])
lam_m=(5-S.sqrt(21))/2;lam_p=(5+S.sqrt(21))/2
assert Gs.eigenvals()=={lam_m:1,lam_p:1}
s=S.symbols('s',real=True)
y=(S.cos(S.sqrt(lam_m)*s)-S.cos(S.sqrt(lam_p)*s))/S.sqrt(21)
x=S.diff(y,s,2)+y
assert S.simplify(x.subs(s,0)-1)==0 and y.subs(s,0)==0
assert S.simplify(S.diff(x,s,2)+4*x-3*y)==0
assert S.simplify(S.diff(y,s,2)-x+y)==0
assert S.diff(y,s,2).subs(s,0)==1
assert S.diff(y,s,4).subs(s,0)==-5
print('PASS exact Gram, spectral factorization, 24 S4 covariance, irreducible multiplicities and ODE')
print('characteristic polynomial:',cp)
print('S4 multiplicities:',multiplicities)
print('squared symmetric frequencies:',lam_m,lam_p)
print('interior top stock bound: 16/7; fraction bound: 4/7')
