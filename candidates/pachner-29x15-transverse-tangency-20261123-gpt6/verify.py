#!/usr/bin/env python3
"""Exact unit-chain 15-to-29 split and transverse rank; requires SymPy."""
from itertools import combinations
import sympy as S
def make(tops):
    C=[sorted({tuple(z) for t in tops for z in combinations(t,k+1)}) for k in range(4)]
    off=[0]
    for a in C:off.append(off[-1]+len(a))
    D=S.zeros(off[-1]);B={}
    for k in range(1,4):
        b=S.zeros(len(C[k-1]),len(C[k]))
        for j,t in enumerate(C[k]):
            for i in range(k+1):b[C[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
        B[k]=b;D[off[k-1]:off[k],off[k]:off[k+1]]=b
    assert B[1]*B[2]==S.zeros(len(C[0]),len(C[2]))
    assert B[2]*B[3]==S.zeros(len(C[1]),len(C[3]))
    return C,off,D
O,oo,Do=make([(0,1,2,3)])
N,no,D=make([(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)])
assert [len(v) for v in O]==[4,6,4,1]
assert [len(v) for v in N]==[5,10,10,4]
T=S.zeros(29,15)
for k in range(3):
    for j,t in enumerate(O[k]):T[no[k]+N[k].index(t),oo[k]+j]=1
for i in range(4):
    q=list(range(4));q[i]=4
    parity=(-1)**sum(q[a]>q[b] for a in range(4) for b in range(a+1,4))
    T[no[3]+N[3].index(tuple(sorted(q))),14]=S.Rational(parity,2)
assert T.T*T==S.eye(15)
A=D-D.T;P=T*T.T;L=(S.eye(29)-P)*A*T
assert L.rank()==13
lam=S.Symbol('lambda')
assert S.factor((L.T*L).charpoly(lam).as_expr())==lam**2*(lam-1)**13
assert S.trace((A*P-P*A).T*(A*P-P*A))==26
f=S.zeros(15,1)
for j,v in enumerate([-1,1,-1,1]):f[10+j]=S.Rational(v,2)
t=S.zeros(15,1);t[14]=1
assert L*f==S.zeros(29,1) and L*t==S.zeros(29,1)
assert A*T*t==T*f and A*T*f==-T*t
assert L.T*L==S.eye(15)-f*f.T-t*t.T
print('PASS: exact signed 1-to-4 incidence, 15-to-29 isometry, rank 13, invariant 2D oscillator')
