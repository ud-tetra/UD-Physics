#!/usr/bin/env python3
"""Exact Whitney k-form mass isometry for K4 -> centroid 1-to-4 (SymPy)."""
import sympy as S
from itertools import combinations
from math import factorial
pts={0:(1,1,1),1:(1,-1,-1),2:(-1,1,-1),3:(-1,-1,1),4:(0,0,0)}
old=[(0,1,2,3)]
new=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
def simplices(tets,k):
 return sorted({z for t in tets for z in combinations(t,k+1)})
def wedge(grad):
 k=len(grad)
 return S.Matrix([S.det(S.Matrix([[g[i] for i in c] for g in grad]))
                  for c in combinations(range(3),k)]) if k else S.Matrix([1])
def mass(tets,k):
 ss=simplices(tets,k); ids={a:i for i,a in enumerate(ss)}; out=S.zeros(len(ss))
 for t in tets:
  V=S.Matrix([[1]+list(pts[v]) for v in t])
  inverse=V.inv();vol=abs(V.det())/6
  grads={t[i]:tuple(inverse[j,i] for j in range(1,4)) for i in range(4)}
  forms={}
  for a in combinations(t,k+1):
   vectors=[]
   for v in t:
    if not k:vectors.append(S.Matrix([int(v==a[0])]))
    else:
     W=S.zeros(len(list(combinations(range(3),k))),1)
     for j,z in enumerate(a):
      if v==z: W+=factorial(k)*(-1)**j*wedge([grads[b] for b in a if b!=z])
     vectors.append(W)
   forms[a]=vectors
  for a,aa in forms.items():
   for b,bb in forms.items():
    out[ids[a],ids[b]]+=vol*sum((1+int(i==j))*aa[i].dot(bb[j])
                         for i in range(4) for j in range(4))/20
 return out
so=[simplices(old,k) for k in range(4)]
sn=[simplices(new,k) for k in range(4)]
lam={i:S.eye(4)[i,:] for i in range(4)}
lam[4]=S.ones(1,4)/4
P=[]
for k in range(4):
 mat=S.zeros(len(sn[k]),len(so[k]))
 for i,a in enumerate(sn[k]):
  for j,b in enumerate(so[k]):
   mat[i,j]=S.det(S.Matrix([[lam[v][z] for z in b] for v in a])) if k else lam[a[0]][b[0]]
 P.append(mat)
for k in range(4):
 mo=mass(old,k);mn=mass(new,k)
 assert P[k].T*mn*P[k]==mo,(k,'mass defect')
 assert mo.det()!=0 and mn.det()!=0
 if k<3:
  def boundary(ss,kk):
   out=S.zeros(len(ss[kk-1]),len(ss[kk]))
   for j,t in enumerate(ss[kk]):
    for i in range(kk+1):out[ss[kk-1].index(t[:i]+t[i+1:]),j]=(-1)**i
   return out
  assert boundary(sn,k+1).T*P[k]==P[k+1]*boundary(so,k+1).T
print("PASS: all grades 0,1,2,3 Whitney mass isometry and cochain commutation")
