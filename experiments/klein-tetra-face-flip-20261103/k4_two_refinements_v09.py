#!/usr/bin/env python3
"""Exact K4 1->4->16 centroid subdivision and native-metric closure audit (SymPy)."""
import itertools,json
import sympy as S

def get_bases(tets):
 return [sorted({t for cell in tets for t in itertools.combinations(cell,k)})
         for k in (1,2,3,4)]
def incidence(b):
 mats=[]
 for k in range(1,4):
  a=S.zeros(len(b[k-1]),len(b[k]));ids={t:i for i,t in enumerate(b[k-1])}
  for j,t in enumerate(b[k]):
   for i in range(k+1):a[ids[t[:i]+t[i+1:]],j]=(-1)**i
  mats.append(a)
 assert mats[0]*mats[1]==S.zeros(len(b[0]),len(b[2]))
 assert mats[1]*mats[2]==S.zeros(len(b[1]),len(b[3]))
 return mats
def refine(cells,z):
 out=[]
 for t in cells:
  for i in range(4):out.append(tuple(sorted(t[:i]+t[i+1:]+(z,))))
  z+=1
 return out
def embed(cells,bc,bf,start):
 m=[]
 ids=[{t:i for i,t in enumerate(a)} for a in bf]
 for k in range(4):
  x=S.zeros(len(bf[k]),len(bc[k]))
  for j,t in enumerate(bc[k]):
   if k<3:x[ids[k][t],j]=1
   else:
    z=start+cells.index(t)
    for i in range(4):
     child=tuple(sorted(t[:i]+t[i+1:]+(z,)))
     x[ids[3][child],j]=(-1)**(i+1)
  m.append(x)
 return S.diag(*m),m
def generator(m):
 ns=[m[0].rows]+[p.cols for p in m]
 off=[0]
 for n in ns:off.append(off[-1]+n)
 a=S.zeros(off[-1])
 for k,D in enumerate(m,1):a[off[k-1]:off[k],off[k]:off[k+1]]=D
 return a-a.T
def test(coarse,fine,z):
 bc,bf=get_bases(coarse),get_bases(fine)
 dc,df=incidence(bc),incidence(bf)
 F,parts=embed(coarse,bc,bf,z)
 for k in (1,2,3):assert df[k-1]*parts[k]==parts[k-1]*dc[k-1]
 G=F.T*F
 assert G==S.diag(*([1]*(F.cols-len(coarse))+[4]*len(coarse)))
 Ac,Af=generator(dc),generator(df)
 Ag=G.inv()*F.T*Af*F
 assert Ag.T*G+G*Ag==S.zeros(G.rows)
 residual=Af*F-F*Ag
 assert F.T*residual==S.zeros(F.cols)
 return {"coarse_f":[len(a) for a in bc],"fine_f":[len(a) for a in bf],
         "G_diag":[int(G[i,i]) for i in range(G.rows)],
         "residual_norm_sq":str(sum((a*a for a in residual),S.Integer(0))),
         "residual_weighted_sq":str(S.trace(residual*G.inv()*residual.T)),
         "native_charpoly":str(S.factor(Ac.charpoly().as_expr())),
         "induced_charpoly":str(S.factor(Ag.charpoly().as_expr()))},(F,Ac,Af,Ag,G)
def group(b,perm):
 n=sum(map(len,b));P=S.zeros(n);off=0
 for sub in b:
  idx={t:i for i,t in enumerate(sub)}
  for j,t in enumerate(sub):
   y=[perm[z] for z in t]
   sg=(-1)**sum(y[i]>y[h] for i in range(len(y)) for h in range(i+1,len(y)))
   P[off+idx[tuple(sorted(y))],off+j]=sg
  off+=len(sub)
 return P
def extend(per,cells,z):
 p=dict(per);idx={frozenset(t):i for i,t in enumerate(cells)}
 for i,t in enumerate(cells):
  p[z+i]=z+idx[frozenset(p[v] for v in t)]
 return p
v0=[(0,1,2,3)]
v1=refine(v0,4);v2=refine(v1,5)
r01,x01=test(v0,v1,4)
r12,x12=test(v1,v2,5)
F02=x12[0]*x01[0];G02=F02.T*F02
assert G02==S.diag(*([1]*14+[16]))
Ag02=G02.inv()*F02.T*x12[2]*F02
E02=x12[2]*F02-F02*Ag02
r02={"G_diag":[int(G02[i,i]) for i in range(G02.rows)],
     "residual_norm_sq":str(sum((a*a for a in E02),S.Integer(0))),
     "induced_charpoly":str(S.factor(Ag02.charpoly().as_expr()))}
assert [r01["residual_norm_sq"],r12["residual_norm_sq"],r02["residual_norm_sq"]]==["13","52","151/4"]
assert r01["native_charpoly"]=="lambda*(lambda**2 + 4)**7"
assert r12["native_charpoly"]=="lambda*(lambda**2 + 1)*(lambda**2 + 5)**13"
B=[get_bases(v) for v in (v0,v1,v2)]
for p0 in itertools.permutations(range(4)):
 p=dict(zip(range(4),p0));p1=extend(p,v0,4);p2=extend(p1,v1,5)
 R0=group(B[0],p);R1=group(B[1],p1);R2=group(B[2],p2)
 assert R1*x01[0]==x01[0]*R0 and R2*x12[0]==x12[0]*R1
 assert R0*x01[3]==x01[3]*R0 and R1*x12[3]==x12[3]*R1
 assert R1*x01[2]==x01[2]*R1 and R2*x12[2]==x12[2]*R2
out={"status":"PASS_EXACT_CONDITIONAL","levels":[[len(a) for a in t] for t in B],
     "level0_to1":r01,"level1_to2":r12,"level0_to2":r02,
     "signed_S4_permutations":24,
     "native_twist_sign":"rho(h)=-1 optional and source-unselected; commutes with each integral map",
     "physical_promotion":0}
print(json.dumps(out,indent=2,sort_keys=True))
