#!/usr/bin/env python3
"""EXACT conditional K4 native W phase to 12 top daughter cochains; SymPy constructor replay."""
import itertools,json
import sympy as S
V=range(4)
sim=[list(itertools.combinations(V,k+1)) for k in range(4)]
off=[0,4,10,14,15]; D=S.zeros(15)
for k in (1,2,3):
    for j,t in enumerate(sim[k]):
        for i in range(k+1):
            D[off[k-1]+sim[k-1].index(t[:i]+t[i+1:]),off[k]+j]=(-1)**i
assert D*D==S.zeros(15)
A=D.T-D; J=A/2
Z=S.zeros(15,4)
for i in V:
    f=tuple(v for v in V if v!=i)
    e=S.zeros(15,1);e[off[2]+sim[2].index(f)]=(-1)**i
    Z[:,i]=D*e
Y=J*Z; I=S.eye(4);Q=I-S.ones(4)/4
assert Z.T*Z==4*Q and Y.T*Y==4*Q and Z.T*Y==S.zeros(4)
assert J*Z==Y and J*Y==-Z
W=(Z*Z.T+Y*Y.T)/4
assert W.rank()==6 and W*W==W and J*W==W*J
H=S.diag(*([6]*8+[3]*4))
alpha=S.sqrt(S.Rational(2,3))
Phi=S.zeros(12,15)
Phi[:4,:]=alpha*Z.T/4;Phi[4:8,:]=alpha*Y.T/4
Jlocal=S.zeros(12);Jlocal[:4,4:8]=-I;Jlocal[4:8,:4]=I
Jw=S.zeros(12);Jw[:4,4:8]=-Q;Jw[4:8,:4]=Q
assert S.simplify(Phi.T*H*Phi-W)==S.zeros(15)
assert Phi*J==Jlocal*Phi==Jw*Phi
assert Jlocal.T*H+H*Jlocal==S.zeros(12)
assert Jw.T*H+H*Jw==S.zeros(12)
assert Jlocal.rank()==8 and Jw.rank()==6 and (Jlocal-Jw).rank()==2
assert Jw*Jw==-S.diag(Q,Q,S.zeros(4))
for g in itertools.permutations(V):
    sign=(-1)**sum(g[i]>g[j] for i in V for j in V if i<j)
    R=S.zeros(15)
    for k in range(4):
        for j,t in enumerate(sim[k]):
            dest=[g[v] for v in t]
            osign=(-1)**sum(dest[i]>dest[j] for i in range(len(dest)) for j in range(i+1,len(dest)))
            R[off[k]+sim[k].index(tuple(sorted(dest))),off[k]+j]=osign
    perm=S.zeros(4)
    for i in V:perm[g[i],i]=1
    Rd=S.diag(sign*perm,sign*perm,sign*perm)
    assert R.T*R==S.eye(15) and R*J==J*R
    assert R*Z==Z*(sign*perm) and R*Y==Y*(sign*perm)
    assert Rd*Phi==Phi*R and Rd*Jw==Jw*Rd
B=S.zeros(24);B[:12,12:]=Jw;B[12:,:12]=Jw
H2=S.diag(H,H);Swap=S.zeros(24);Swap[:12,12:]=S.eye(12);Swap[12:,:12]=S.eye(12)
assert B.T*H2+H2*B==S.zeros(24) and Swap*B*Swap==B and B.rank()==12
e_top=S.zeros(15,1);e_top[14]=1
assert Phi*e_top==S.zeros(12,1)
u=S.Matrix([1]*4+[0]*8)
assert Jlocal*u!=S.zeros(12,1) and Jw*u==S.zeros(12,1)
print(json.dumps({"pass":True,"native_phase_rank":6,"daughter_dim":12,
 "signed_S4_checks":24,"Phi_metric_isometry":True,
 "Phi_native_intertwining":True,"Jlocal_rank":8,"Jnative_supported_rank":6,
 "extra_cell_local_modes":2,"two_sheet_swap_and_stock":True,
 "two_sheet_exchange_rank":12,"uniform_top_state_image_zero":True,
 "physical_promotion":0},indent=2))
