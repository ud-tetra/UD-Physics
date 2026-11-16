"""Exploratory NumPy screen; exact finalist claims use seventh_probe_replay."""
import numpy as np
from itertools import combinations
from fractions import Fraction as F
from mixed_taylor_replay import coeffs
from mixture_probe_replay import P,J,points,value
sites=points+((F(-1,2),1),)
eta=F(1,100)
full=[[(-1,t) for t in np.linspace(0,1,51)],[ (t,1) for t in np.linspace(-1,1,101)],[(1,t) for t in np.linspace(0,1,51)]]
D=np.unique(np.array(sum(full,[])),axis=0)
ix=np.array(list(combinations(range(7),4)))
subs=np.array([[k for k in range(4) if k!=j] for j in range(4)])
def row(q):
 p,j=coeffs(P,q),coeffs(J,q)
 for k in p.keys()|j.keys():
  yield [float(p.get(k,0)),float(j.get(k,0))]
def data(q):
 vec=np.array(list(row(q))).reshape((-1,2))
 return np.abs(vec@D.T).sum(0),np.array([q[0]**2,q[0]*q[1],q[1]**2],float),np.array([value(p,q) for p in (P,J)],float),float(4*eta*sum(map(abs,q))+16*eta**2+F(1,32))
zero=data((0,0))[0]*3
old=[data(q) for q in sites]
res=[]
for i in range(-40,41):
 for j in range(41):
  q=(F(i,40),F(j,40))
  if q in sites or tuple(-v for v in q) in sites or q==(0,0): continue
  d,v,signal,B=map(np.array,zip(*old,data(q)))
  cs=v[ix]
  w=np.linalg.det(cs[:,subs,:])*np.array([1,-1,1,-1])
  sel=np.max(abs(w),axis=1)>1e-11
  w=w[sel]
  idx=ix[sel]
  aw=abs(w)
  c=np.einsum('ij,ijk->ik',w,signal[idx])
  h=2*np.einsum('ij,ij->i',aw,B[idx])
  e=np.einsum('ij,ijk->ik',aw,d[idx]+zero)
  s=((abs(c@D.T)-e)/h[:,None]).max(0).min()
  res.append((1/s,q))
print(len(res))
for x in sorted(res)[:20]:print(x)
