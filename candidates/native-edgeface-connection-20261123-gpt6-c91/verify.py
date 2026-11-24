#!/usr/bin/env python3
"""Exact constructor replay: conditional state-dependent cross-grade junction coupling."""
import itertools, sympy as s, json
V=tuple(range(4))
simp=[list(itertools.combinations(V,k+1)) for k in range(4)]
offset=[0,4,10,14,15]
D=s.zeros(15)
for k in (1,2,3):
    b=s.zeros(len(simp[k-1]),len(simp[k]))
    for j,t in enumerate(simp[k]):
        for i in range(k+1):
            b[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
    D[offset[k-1]:offset[k],offset[k]:offset[k+1]]=b
A=D.T-D
assert A.T==-A and D*D==s.zeros(15)
P=[s.diag(*([0]*offset[k]+[1]*(offset[k+1]-offset[k])+[0]*(15-offset[k+1]))) for k in range(4)]
R={}
for perm in itertools.permutations(V):
    S=s.zeros(15)
    for k in range(4):
        for j,t in enumerate(simp[k]):
            q=[perm[i] for i in t]
            sign=(-1)**sum(q[i]>q[h] for i in range(len(q)) for h in range(i+1,len(q)))
            S[offset[k]+simp[k].index(tuple(sorted(q))),offset[k]+j]=sign
    assert S.T*S==s.eye(15) and S*A==A*S
    R[perm]=S
a=s.Matrix([1,0,-1,0, 1,2,-1,0,1,-2, 1,0,0,-1, 0])
b=s.Matrix([2,-1,0,1, -1,1,0,2,-1,0, 0,1,-2,1, 0])
K=(P[1]*a)*(P[2]*b).T+(P[2]*a)*(P[1]*b).T
rho=(a.T*a)[0]-(b.T*b)[0]
J=s.zeros(30)
J[:15,15:]=rho*K
J[15:,:15]=-rho*K.T
assert J.T==-J and rho==-4 and J.rank()==4
assert sum(int(v!=0) for v in K)==23
for Sa,Sb in itertools.product(R.values(),repeat=2):
    aa,bb=Sa*a,Sb*b
    KK=(P[1]*aa)*(P[2]*bb).T+(P[2]*aa)*(P[1]*bb).T
    assert KK==Sa*K*Sb.T
    assert (aa.T*aa)[0]-(bb.T*bb)[0]==rho
assert J*a.col_join(b)!=s.zeros(30)
flip=s.zeros(30);flip[:15,15:]=s.eye(15);flip[15:,:15]=s.eye(15)
Jswap=s.zeros(30)
Jswap[:15,15:]=-rho*K.T;Jswap[15:,:15]=rho*K
assert flip*J*flip==Jswap
assert (a.T*a)[0]-(a.T*a)[0]==0
faces=simp[2]
matchings=[(fa,tuple(p)) for fa in faces for fb in faces for p in itertools.permutations(fb)]
def act(m,ga,gb):
    fa,fb=m
    mp={ga[v]:gb[w] for v,w in zip(fa,fb)}
    ff=tuple(sorted(mp))
    return ff,tuple(mp[i] for i in ff)
orbit={act(matchings[0],ga,gb) for ga,gb in itertools.product(R,repeat=2)}
assert len(matchings)==len(orbit)==96
print(json.dumps({"pass":True,"relabelings":576,"matching_orbit":96,
  "cross_rank":4,"rho":"-4","cross_nonzero_entries":23,
  "quadratic_stock_conserved":True,"source_derived":False,
  "physical_promotion":0},indent=2))
