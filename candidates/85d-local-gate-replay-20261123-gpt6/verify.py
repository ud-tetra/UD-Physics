#!/usr/bin/env python3
"""85D Pachner normalized-gate screen; NumPy/SciPy. Formal time, unit metric."""
import itertools as it
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
par=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
tops=sorted(tuple(sorted((set(p)-{v})|{n})) for p,n in zip(par,range(5,9)) for v in p)
simp=[sorted({s for t in tops for s in it.combinations(t,k+1)}) for k in range(4)]
assert list(map(len,simp))==[9,26,34,16]
o=np.cumsum([0]+list(map(len,simp)))
B=[]
for k in (1,2,3):
 b=np.zeros((len(simp[k-1]),len(simp[k])),int)
 for j,t in enumerate(simp[k]):
  for i in range(k+1):b[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
 B.append(b)
assert not (B[0]@B[1]).any() and not (B[1]@B[2]).any()
assert [np.linalg.matrix_rank(b) for b in B]==[8,18,16]
A=np.zeros((85,85))
for k,b in enumerate(B,1):
 A[o[k-1]:o[k],o[k]:o[k+1]]=b;A[o[k]:o[k+1],o[k-1]:o[k]]=-b.T
assert np.array_equal(A,-A.T)
coords={0:(1,1,1),1:(1,-1,-1),2:(-1,1,-1),3:(-1,-1,1),4:(0,0,0)}
for n,p in enumerate(par,5):coords[n]=np.mean([coords[i] for i in p],axis=0)
sigs=[]
for t in tops:
 pts=[np.array(coords[v],float) for v in t]
 sigs.append(int(np.sign(np.linalg.det(np.array([pts[i]-pts[0] for i in (1,2,3)])))))
outer=[j for j,t in enumerate(tops) if 4 not in t]
assert len(outer)==4
c=np.zeros(85);c[o[3]+np.array(outer)]=np.array(sigs)[outer]
assert c@c==4
r,j=np.nonzero(B[2]);b=B[2][r,j]
def rhs(mode):
 def fn(s,x):
  y=A@x
  if mode!='null':
   f=x[o[2]:o[3]];q=x[o[3]:o[4]]
   u=f[r]**2;v=q[j]**2;den=u+v
   if mode=='lower':g=np.divide(2*u,den,out=np.ones_like(u),where=den>0)
   elif mode=='higher':g=np.divide(2*v,den,out=np.ones_like(u),where=den>0)
   else:g=np.divide(4*u*v,den**2,out=np.ones_like(u),where=den>0)
   delta=b*(g-1)
   np.add.at(y,o[2]+r,delta*q[j]);np.add.at(y,o[3]+j,-delta*f[r])
  return y
 return fn
inter=[j for j in range(16) if j not in outer]
for mode in ['null','lower','higher','balance']:
 sol=solve_ivp(rhs(mode),(0,2),c,rtol=2e-11,atol=1e-12,dense_output=True,method='DOP853')
 assert sol.success
 for s in (0,.5,1,2):
  x=sol.sol(s);f=x[o[2]:o[3]];q=x[o[3]:o[4]]
  interior=q[inter]@q[inter];face=f@f
  Eg=np.linalg.norm(B[2]@q)**2+np.linalg.norm(B[2].T@f)**2
  assert abs(x@x-4)<2e-8
  print(mode,s,'inside',round(interior,6),'face',round(face,6),'Eg',round(Eg,6),'stockerr',abs(x@x-4))
 if mode=='null':assert np.linalg.norm(expm(2*A)@c-sol.y[:,-1])<1e-8
print('PASS, fixed post-event 85D unit metric; no native event admission')
