#!/usr/bin/env python3
"""UD Discovery 4D apex/3D shell coupling; standalone exact + finite pulse audit.
Dependencies: sympy, numpy, scipy. Run python3 audit.py; prints findings and checks.
Provenance: source main 92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa.
This is an assumed Euclidean spring model, not a physical identification.
"""
import math
import numpy as np
import sympy as S
from scipy.integrate import solve_ivp

phi=(1+S.sqrt(5))/2
rho2=(5+S.sqrt(5))/8
eta2=(3-S.sqrt(5))/8
eta=S.sqrt(eta2)
s,z,kr,ke=S.symbols('s z k_r k_e',real=True,positive=True)
ell=S.sqrt(rho2*s*s+z*z)
U=6*kr*(ell-1)**2+15*ke*(s-1)**2
K=S.simplify(S.hessian(U,(s,z)).subs({s:1,z:eta}))
Kh=S.Matrix([[12*kr*rho2**2+30*ke,12*kr*rho2*eta],
             [12*kr*rho2*eta,12*kr*eta2]])
assert S.simplify(K-Kh)==S.zeros(2)
assert S.simplify(K.det()-360*kr*ke*eta2)==0
gain=S.simplify(-rho2/(10*ke*eta))
assert S.simplify(3*(K.inv()*S.Matrix([0,1]))[0]-gain)==0

raw=[]
for a in (-1,1):
    for b in (-1,1):
        raw.extend([(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)])
X=[S.Matrix(x)/2 for x in dict.fromkeys(raw)]
assert len(X)==12
assert all(S.simplify(v.dot(v)-rho2)==0 for v in X)
assert S.simplify(sum((v*v.T for v in X),S.zeros(3,3))-4*rho2*S.eye(3))==S.zeros(3)
edges=[(i,j) for i in range(12) for j in range(i+1,12)
       if S.simplify((X[i]-X[j]).dot(X[i]-X[j])-1)==0]
faces=[(i,j,k) for i in range(12) for j in range(i+1,12)
       for k in range(j+1,12) if (i,j) in edges and (i,k) in edges and (j,k) in edges]
assert (len(edges),len(faces))==(30,20)

x=np.array([[float(t) for t in v] for v in X]);r2=float(rho2);h=float(eta)
# 42 springs, 40 coordinates: 36 shell xyz, three apex xyz, one apex w
J=np.zeros((42,40))
for row,(i,j) in enumerate(edges):
    dv=x[i]-x[j]
    J[row,3*i:3*i+3]=dv
    J[row,3*j:3*j+3]=-dv
for i in range(12):
    J[30+i,3*i:3*i+3]=x[i]
    J[30+i,36:39]=-x[i]
    J[30+i,39]=h
sing=np.linalg.svd(J,compute_uv=False)
assert np.count_nonzero(sing>1e-10)==34
for axis in range(3):
    v=np.zeros(40)
    v[axis:36:3]=1;v[36+axis]=1
    assert np.linalg.norm(J@v)<1e-12
    v=np.zeros(40)
    for i in range(12):v[3*i:3*i+3]=np.cross(np.eye(3)[axis],x[i])
    assert np.linalg.norm(J@v)<1e-12
T=np.zeros((40,2));T[:36,0]=x.ravel();T[39,1]=1
Kn=np.array(K.subs({kr:1,ke:1}).evalf(),dtype=float)
M=np.diag([12*r2,1.])
assert np.max(np.abs(T.T@J.T@J@T-Kn))<1e-12
assert np.max(np.abs(T.T@T-M))<1e-12
assert np.max(np.abs(J.T@J@T-T@np.linalg.solve(M,Kn)))<1e-12
D=np.diag(np.diag(M)**-.5)
wn=np.sqrt(np.linalg.eigvalsh(D@Kn@D))

# Comparison baseline: conventional 3D axial centre motion, own relaxed shell.
R=math.sqrt(r2)
s0=(12*R+30)/(12*r2+30)
assert 12-8/(s0*R)>0
assert s0>1
# Mixed Hessian K_su=0 exactly by sum_i x_i=0.
assert np.linalg.norm(np.sum(x,axis=0))<1e-12

damping=.06*M
def grad4(q):
    ss,zz=q
    L=math.sqrt(r2*ss*ss+zz*zz)
    return np.array([12*(L-1)*r2*ss/L+30*(ss-1),12*(L-1)*zz/L])
def grad3(q):
    ss,u=q
    L=np.sqrt(r2*ss*ss+u*u-2*ss*u*x[:,2])
    return np.array([np.sum((L-1)*(ss*r2-u*x[:,2])/L)+30*(ss-1),
                     np.sum((L-1)*(u-ss*x[:,2])/L)])
def pulse(t,A):
    return A*math.exp(-.5*((t-8)/1.5)**2)
def integrate(kind,A):
    base=np.array([1.,h]) if kind=="4d" else np.array([s0,0.])
    grad=grad4 if kind=="4d" else grad3
    def rhs(t,y):
        v=y[2:]
        acc=np.linalg.solve(M,np.array([0.,pulse(t,A)])-grad(y[:2])-damping@v)
        return np.r_[v,acc]
    sol=solve_ivp(rhs,(0,70),np.r_[base,0.,0.],t_eval=np.linspace(0,70,1401),
                  method="DOP853",rtol=1e-11,atol=1e-13)
    assert sol.success
    return float(np.max(np.abs((sol.y[0]/base[0])**3-1)))
peaks={(kind,A):integrate(kind,A) for kind in ["4d","3d"] for A in [.01,.02,.08]}
assert 1.7<peaks["4d",.02]/peaks["4d",.01]<2.3
assert 3.1<peaks["3d",.02]/peaks["3d",.01]<5.
# Positive 3D two-coordinate lever energy has precisely the same Hessian.
q,t=S.symbols('q t',real=True)
U3lever=15*ke*q*q+6*kr*(rho2*q+eta*t)**2
assert S.simplify(S.hessian(U3lever,(q,t))-K)==S.zeros(2)
print("PASS: Hessian, static transfer, icosahedron, full40 rank, symmetry sector, 3D analogue, pulses")
print("K=",Kn.tolist()," M=",M.tolist()," angular_frequencies=",wn.tolist())
print("static fractional volume gain=",float(gain.subs(ke,1)))
print("full40 rank=34 nullity=6; 3D axial s0=",s0)
for k,v in peaks.items():print(k,"peak fractional-volume amplitude:",v)
