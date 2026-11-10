"""Exact onsite J-invariance obstruction and phase-compatible star quartic."""
import argparse,json
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
cs=[s for k in range(1,5) for s in combinations(range(4),k)]; idx={s:i for i,s in enumerate(cs)};n=15
z=lambda:[[F(0) for j in range(n)] for i in range(n)]
t=lambda a:[list(r) for r in zip(*a)]
add=lambda a,b:[[u+v for u,v in zip(x,y)] for x,y in zip(a,b)]
sc=lambda a,q:[[q*v for v in x] for x in a]
mm=lambda a,b:[[sum((u*v for u,v in zip(x,y)),F(0)) for y in t(b)] for x in a]
mv=lambda a,x:[sum((u*v for u,v in zip(r,x)),F(0)) for r in a]
dot=lambda x,y:sum((u*v for u,v in zip(x,y)),F(0))
D=[z() for k in range(3)]
for s in cs:
 if len(s)>1:
  for k in range(len(s)):D[len(s)-2][idx[s[:k]+s[k+1:]]][idx[s]]=F((-1)**k)
K=[add(a,sc(t(a),-1)) for a in D];A=add(add(K[0],K[1]),K[2]);J=sc(A,F(1,2))
P=[sc(mm(a,a),F(-1,4)) for a in K];H=P[2]
assert mm(A,mm(A,A))==sc(A,-4) and sum(H[i][i] for i in range(n))==2
assert all(mm(K[i],K[j])==z() for i in range(3) for j in range(3) if i!=j)
adj=[set() for i in range(n)]
for d in D:
 for i in range(n):
  for j in range(n):
   if d[i][j]:adj[i].add(j);adj[j].add(i)
seen={0};queue=[0]
while queue:
 for j in adj[queue.pop()]:
  if j not in seen:seen.add(j);queue.append(j)
assert len(seen)==15 and all(adj)
# Formal two-site proof: J_ij*(h_i'(u)*v-h_j'(v)*u)=0 for an
# incidence pair with other coordinates zero, h_k'(0)=0. Connectedness
# forces all onsite h_i'(u)=c*u; integration yields only common quadratic.
I=z()
for i in range(n):I[i][i]=F(1)
star=0
for p in permutations(range(4)):
 R=z()
 for s in cs:
  w=[p[v] for v in s];sgn=(-1)**sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
  R[idx[tuple(sorted(w))]][idx[s]]=F(sgn)
 assert mm(t(R),R)==I and mm(R,H)==mm(H,R) and mm(R,A)==mm(A,R)
 star+=1
c=idx[(0,1,2,3)];e=[F(i==c) for i in range(n)];f=mv(J,e)
assert dot(f,f)==1 and dot(e,f)==0
rot=[add(add(I,sc(J,sn)),sc(mm(J,J),1-co)) for co,sn in [(1,0),(0,1),(-1,0),(0,-1)]]
def vec(x,lam):
 p=mv(H,x);r=dot(p,p);return mv(A,[v+lam*r*u for v,u in zip(x,p)])
def energy(x,lam):r=dot(x,mv(H,x));return dot(x,x)/2+lam*r*r/4
fix=0; phase=0
edge=[F(i==idx[(0,1)]) for i in range(n)]
for lam,q,p,w in product([F(0),F(1,4),F(1),F(2)],[F(0),F(1,2),F(1)],[F(-1,2),F(0),F(1,2)],[F(0),F(1,3)]):
 x=[q*e[i]+p*f[i]+w*edge[i] for i in range(n)]
 v=vec(x,lam);r=dot(x,mv(H,x))
 assert v==[a+lam*r*b for a,b in zip(mv(A,x),mv(K[2],x))]
 assert dot(x,v)==dot([a+lam*r*b for a,b in zip(x,mv(H,x))],v)==0
 assert all(dot(mv(P[k],x),mv(P[k],v))==0 for k in range(3))
 fix+=1
 for U in rot:
  assert vec(mv(U,x),lam)==mv(U,v) and energy(mv(U,x),lam)==energy(x,lam)
  phase+=1
assert F(1)+(F(1)*F(1,2))==F(3,2)
offdiag=sum(bool(H[i][j]) for i in range(n) for j in range(i+1,n))
assert offdiag==6 and star==24 and fix==72 and phase==288
result={'status':'PASS','method':'Q exact incidence, analytic two-site proof and rational constructor','onsite_theorem':'Differentiable H=sum h_i(x_i) with h_i_prime(0)=0 and exp(theta J) invariance forces H=c||x||^2/2+constant on connected Hasse graph','connected_registers':len(seen),'signed_S4_actions':star,'quartic_fixture_states':fix,'phase_rotation_checks':phase,'hidden_projector_rank':2,'hidden_face_pair_couplings':offdiag,'model':'H=||x||^2/2+lambda*(||P3x||^2)^2/4; xprime=A x+lambda*r3*K3 x','frequencies':'omega1=omega2=2; omega3=2*(1+lambda*r3); r3 invariant','inverse_design':'g3=3/2 at r3=1/2 requires lambda=1 (FIT, exposed target)','onsite_locality':'FAILED: phase-compatible hidden quartic mixes all four faces via P3','classical_null':'Matched classical Hamiltonian using Poisson A and same H is exactly equivalent','source_coefficient':'OPEN: no source selection for lambda','review':'Same-context constructor; external and empirical NOT_RUN'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'PASS','S4':star,'phase':phase,'fixtures':fix},sort_keys=True))
