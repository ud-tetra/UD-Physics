"""Exact tetrahedral source closure and a local quartic constitutive alternative."""
import argparse,itertools,json
from fractions import Fraction as Q
from pathlib import Path
cells=[c for k in range(1,5) for c in itertools.combinations(range(4),k)]; ix={c:i for i,c in enumerate(cells)}; n=15
zero=lambda:[[Q(0) for _ in range(n)] for _ in range(n)]
tr=lambda a:[list(r) for r in zip(*a)]
add=lambda a,b:[[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
scale=lambda a,t:[[t*x for x in r] for r in a]
mm=lambda a,b:[[sum((x*y for x,y in zip(r,c)),Q(0)) for c in zip(*b)] for r in a]
mv=lambda a,v:[sum((x*y for x,y in zip(r,v)),Q(0)) for r in a]
dot=lambda x,y:sum((a*b for a,b in zip(x,y)),Q(0))
D=[zero() for _ in range(3)]
for c in cells:
 if len(c)>1:
  for j in range(len(c)):D[len(c)-2][ix[c[:j]+c[j+1:]]][ix[c]]=Q((-1)**j)
K=[add(d,scale(tr(d),-1)) for d in D];A=add(add(K[0],K[1]),K[2]);A2=mm(A,A)
assert mm(A2,A)==scale(A,-4)
assert all(mm(K[i],K[j])==zero() for i in range(3) for j in range(3) if i!=j)
lam=Q(1,4)
def vfield(x):return mv(A,[a+lam*a**3 for a in x])
def energy(x):return sum((a*a/2+lam*a**4/4 for a in x),Q(0))
C=ix[(0,1,2,3)]; e=[Q(i==C) for i in range(n)];j=mv(scale(A,Q(1,2)),e)
assert dot(j,j)==1 and dot(j,e)==0
plane=lambda q,p:[q*e[i]+p*j[i] for i in range(n)]
checks=0
for q,p in itertools.product([Q(-1),Q(0),Q(1,2),Q(1)],repeat=2):
 assert vfield(plane(q,p))==plane(-2*(p+lam*p**3/4),2*(q+lam*q**3))
 checks+=1
x=[Q(((7*i+3)%13)-6,7) for i in range(n)]; w=[u+lam*u**3 for u in x]
assert dot(w,vfield(x))==0 and dot(x,vfield(x))!=0
for m in [1,2,4,7,11,15]:
 assert sum((w[i]*vfield(x)[i] for i in range(m)),Q(0))==sum((A[i][k]*w[i]*w[k] for i in range(m) for k in range(m,n)),Q(0))
for p in itertools.permutations(range(4)):
 R=zero()
 for c in cells:
  z=[p[i] for i in c];sign=(-1)**sum(u>v for i,u in enumerate(z) for v in z[i+1:]);R[ix[tuple(sorted(z))]][ix[c]]=Q(sign)
 assert mm(R,A)==mm(A,R) and vfield(mv(R,x))==mv(R,vfield(x)) and energy(mv(R,x))==energy(x)
J=scale(A,Q(1,2)); defect=[a-b for a,b in zip(vfield(mv(J,e)),mv(J,vfield(e)))]
assert defect==plane(Q(3,8),Q(0))
rate1=dot(j,vfield(plane(Q(1),Q(0))));ratehalf=2*dot(j,vfield(plane(Q(1,2),Q(0))))
assert rate1==Q(5,2) and ratehalf==Q(17,8) and rate1-ratehalf==Q(3,8)
result={'status':'PASS','evidence':['EXACT','CONDITIONAL','HYPOTHESIS','FAILED'],'signed_permutations':24,'plane_fixtures':checks,'energy_current_cuts':6,'native_identity':'A^3=-4A','native_only_skew_function':'Any real analytic skew-adjoint f(A)=c*A; no native detuning','constitutive_hypothesis':'xprime=A(x+lambda*x**3 componentwise), H=sum(x_i²/2+lambda*x_i⁴/4)','lambda':'1/4 (target-informed free choice)','signed_face_pattern':'+,-,+,-','two_preparation_normalized_face_rates':[str(rate1),str(ratehalf)],'rate_difference':str(rate1-ratehalf),'J_equivariance_defect':str(dot(e,defect)),'original_norm_conserved':False,'energy_conserved':True,'classical_matched_quartic':'exactly identical Poisson A, Hamiltonian H and evolution; UD physical attribution FAILED','source_selection':'OPEN','physical_port_clock':'OPEN','independent_review':'NOT_RUN'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True,type=Path);z=ap.parse_args();z.out.parent.mkdir(parents=True,exist_ok=True);z.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps(result,sort_keys=True))
