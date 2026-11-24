#!/usr/bin/env python3
"""Exact Whitney cochain 15→29 rank-zero tangency; SymPy required."""
import sympy as s
from itertools import combinations as co
from math import factorial as fact
xyz={0:(1,1,1),1:(1,-1,-1),2:(-1,1,-1),3:(-1,-1,1),4:(0,0,0)}
K0=[(0,1,2,3)]
K1=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
def all_s(tets): return [sorted({x for t in tets for x in co(t,k+1)}) for k in range(4)]
def bd(ss,k):
 b=s.zeros(len(ss[k-1]),len(ss[k]))
 for j,t in enumerate(ss[k]):
  for i in range(k+1): b[ss[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
 return b
def wedge(gs):
 k=len(gs)
 return s.Matrix([s.det(s.Matrix([[g[i] for i in axes] for g in gs])) for axes in co(range(3),k)]) if k else s.Matrix([1])
def mass(tets,k):
 ss=all_s(tets)[k];ix={a:i for i,a in enumerate(ss)};out=s.zeros(len(ss))
 for t in tets:
  V=s.Matrix([[1]+list(xyz[v]) for v in t]); I=V.inv();volume=abs(V.det())/6
  grads={t[i]:tuple(I[j,i] for j in range(1,4)) for i in range(4)}
  forms={}
  for face in co(t,k+1):
   vals=[]
   for v in t:
    if k==0: vals.append(s.Matrix([int(v==face[0])]))
    else:
     w=s.zeros(len(list(co(range(3),k))),1)
     for j,z in enumerate(face):
      if v==z:w+=fact(k)*(-1)**j*wedge([grads[b] for b in face if b!=z])
     vals.append(w)
   forms[face]=vals
  for aa,x in forms.items():
   for bb,y in forms.items():
    out[ix[aa],ix[bb]]+=volume*sum((1+int(i==j))*x[i].dot(y[j]) for i in range(4) for j in range(4))/20
 return out
S0=all_s(K0);S1=all_s(K1);ls={i:s.eye(4)[i,:] for i in range(4)};ls[4]=s.ones(1,4)/4
P=[]
for k in range(4):
 a=s.zeros(len(S1[k]),len(S0[k]))
 for i,t in enumerate(S1[k]):
  for j,b in enumerate(S0[k]):
   a[i,j]=s.det(s.Matrix([[ls[v][z] for z in b] for v in t])) if k else ls[t[0]][b[0]]
 P.append(a)
M0=s.diag(*(mass(K0,k) for k in range(4)));M1=s.diag(*(mass(K1,k) for k in range(4)));Q=s.diag(*P)
assert Q.T*M1*Q==M0
def diff(ss):
 dims=[len(x) for x in ss];offset=[0]
 for n in dims:offset.append(offset[-1]+n)
 d=s.zeros(offset[-1])
 for k in range(3):d[offset[k+1]:offset[k+2],offset[k]:offset[k+1]]=bd(ss,k+1).T
 return d
d0=diff(S0);d1=diff(S1)
assert d1*Q==Q*d0
A0=d0-M0.inv()*d0.T*M0;A1=d1-M1.inv()*d1.T*M1
assert A1*Q==Q*A0
Pi=Q*M0.inv()*Q.T*M1
assert Pi*Pi==Pi and Pi*Q==Q and Pi.rank()==15
assert A1*Pi==Pi*A1
L=(s.eye(29)-Pi)*A1*Q
assert L==s.zeros(29,15)
assert P[3].T*P[3]==s.Matrix([[s.Rational(1,4)]])
assert P[3].T*mass(K1,3)*P[3]==mass(K0,3)==s.Matrix([[s.Rational(3,8)]])
print("PASS exact all-grade mass and d commute, A intertwine, Pi commute, Whitney L rank 0")
