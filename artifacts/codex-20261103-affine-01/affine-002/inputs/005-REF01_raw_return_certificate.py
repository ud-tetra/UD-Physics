from REF01_four_norm_probes import *
def inv(a):
 a=[r+[F(i==j) for j in range(n)] for i,r in enumerate(a)]
 for j in range(n):
  i=next(i for i in range(j,n) if a[i][j])
  a[j],a[i]=a[i],a[j];a[j]=[v/a[j][j] for v in a[j]]
  for i in range(n):
   if i!=j and a[i][j]:a[i]=[v-a[i][j]*w for v,w in zip(a[i],a[j])]
 return [r[n:] for r in a]
Hi=inv(H); ks=[mat([sum(a*c for a,c in zip(row,u)) for row in V]) for u in N]
def mm(a,b):
 out=[]
 for r in a:
  v=[0]*len(b[0])
  for i,c in enumerate(r):
   if c:
    for j,d in enumerate(b[i]):
     if d:v[j]+=c*d
  out.append(v)
 return out
def ni(M):return max(sum(map(abs,r)) for r in M)
import numpy as np
from scipy.linalg import expm_frechet
from scipy.optimize import least_squares
cases=[]
for face,port in [((0,1,3),(0,1,3)),((0,1,5),(0,1,2,3)),((0,3,5),(0,1,3)),((0,3),(0,))]:
 i=b.index(face);c=coarse.index(port)
 E=[[(-B[l][j] if (l==i and len(b[j])==4 if len(face)==3 else j==i) else F(0)) for j in range(n)] for l in range(n)]
 W=mm(Hi,mm(tr(E),H)); G=add(A,add(W,neg(E)))
 Ds=[mm(Hi,add(mm(tr(E),k),neg(mm(k,W)))) for k in ks]
 cases.append((G,Ds,[R[c]],[[r[c]] for r in S],add(B,E)))
def arr(x):return np.array(x,float)
def jac(t):
 return np.array([[float((arr(r)@expm_frechet(t*arr(g),t*arr(d),compute_expm=False)@arr(s))[0,0]) for d in ds] for g,ds,r,s,_ in cases])
from math import factorial
from scipy.linalg import expm
def ni(a):return max(sum(map(abs,r)) for r in a)
def inv4(a):
 global n
 old=n;n=4
 try:return inv(a)
 finally:n=old
t=F(3,2); rho=F(1,10**10)
T=[]
for g,ds,r,s,_ in cases:
 assert ni(g)<F(77,10) and sum(map(ni,ds))<57
 d=[[[F(0)] for _ in s] for _ in ds]; p=s
 j=[F(0)]*4
 for m in range(1,81):
  d=[[[t/m*a[0]] for a in add(mm(g,v),mm(D,p))] for v,D in zip(d,ds)]
  p=[[t/m*a[0]] for a in mm(g,p)]
  j=[u+mm(r,v)[0][0] for u,v in zip(j,d)]
 T.append(j)
tail=2*57*t*F(12)**80/factorial(80)/(1-F(12,81))
assert ni(inv4(T))<206 and tail<F(1,10**30)
assert ni(Hi)*sum(map(ni,ks))<153
assert 153*rho< F(1,100) and 57+53000*rho<58
assert ni(H)*ni(Hi)==8
# H-theta condition number <16. D^2 G infinity norm <36000.
assert 8*(1+153*rho)/(1-153*rho)<16
assert 2*153/(1-153*rho)*58<36000
L=t*4*7*36000+t*t*(4*7*58)**2
assert 206*(tail+L*rho)<F(1,2)
print('CERT',float(ni(inv4(T))),float(tail),L, 'inverse <=412',flush=True)
def model(theta):
 h=arr(H)+sum((v*arr(k) for v,k in zip(theta,ks)),np.zeros((41,41)))
 return np.array([(arr(r)@expm(float(t)*(np.linalg.solve(h,arr(bg).T@h)-arr(bg)))@arr(s))[0,0] for _,_,r,s,bg in cases])
truth=np.array([.5,-.4,.3,-.2]); noise=np.array([1,-1,1,-1])*1e-14
target=model(float(rho)*truth)+noise
fit=least_squares(lambda u:(model(float(rho)*u)-target)/float(rho),np.zeros(4),jac=lambda u:jac(float(t)),bounds=(-1,1),gtol=1e-12)
print('FIT',fit.x,'theta err',float(rho)*max(abs(fit.x-truth)),'res',max(abs(model(float(rho)*fit.x)-target)))
