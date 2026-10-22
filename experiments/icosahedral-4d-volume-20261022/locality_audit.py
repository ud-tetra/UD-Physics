#!/usr/bin/env python3
"""UD Discovery local reciprocal SO(3)-equivariant 3D null against 4D apex.

Pure central-force, pairwise Hookean springs on two concentric icosahedral shells:
outer shell edges (30), inner shell edges (30), matching radial spokes (12),
and nearest-neighbour outer-inner cross braces (60). Every spring is an
ordinary Euclidean 3D distance, energy k/2 (ell-ell0)^2. The full network
has 24 free 3D point masses. It uses no guided carriages or multi-body angles.

Two-DOF restricted homothety is fitted to the earlier 4D Hessian and mass,
not claimed to be a new physical prediction. Exact prior 3D guided nonlinear
analogue remains a separate baseline, untouched.
"""
from __future__ import annotations
import json, math, hashlib, csv, sys
from pathlib import Path
import numpy as np
import sympy as S
from scipy.linalg import eigh
from scipy.optimize import root
from scipy.integrate import solve_ivp

OUT=Path(__file__).resolve().parent
phi=(1+S.sqrt(5))/2
r2=(5+S.sqrt(5))/8
eta=S.sqrt((3-S.sqrt(5))/8)
gamma=S.Rational(1,5)
b0=S.Rational(1,4)
kcross=S.Rational(1,20)
Lcross=S.sqrt(r2*(1-b0)**2+b0)
As=(r2*(1-b0)+b0/2)/Lcross
Bz=gamma*(r2*(1-b0)-S.Rational(1,2))/Lcross
A=12*r2**2+30
B=12*r2*eta
D=12*eta**2
ks=S.simplify((B-60*kcross*As*Bz)/(12*r2*gamma))
ke=S.simplify((A-12*ks*r2-60*kcross*As**2)/30)
ki=S.simplify((D-12*ks*r2*gamma**2-60*kcross*Bz**2)/(30*gamma**2))
mi=S.simplify(1/(12*r2*gamma**2))
assert all(float(v)>0 for v in (ks,ke,ki,kcross,mi))
K4=S.Matrix([[A,B],[B,D]])
Kr=S.simplify(12*ks*r2*S.Matrix([[1,gamma],[gamma,gamma**2]])
    +30*ke*S.diag(1,0)+30*ki*gamma**2*S.diag(0,1)
    +60*kcross*S.Matrix([[As**2,As*Bz],[As*Bz,Bz**2]]))
assert S.simplify(Kr-K4)==S.zeros(2)
M4=S.diag(12*r2,1)
M3=S.diag(12*r2,12*mi*r2*gamma**2)
assert S.simplify(M3-M4)==S.zeros(2)
assert S.simplify(K4.det()-360*eta**2)==0

raw=[]
for a in [-1,1]:
 for b in [-1,1]:
  raw.extend([(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)])
X=[S.Matrix(v)/2 for v in dict.fromkeys(raw)]
assert len(X)==12
edges=[]
for i in range(12):
 for j in range(i+1,12):
  if S.simplify((X[i]-X[j]).dot(X[i]-X[j])-1)==0:
   edges.append((i,j))
assert len(edges)==30
# Exact 3D rotational rigidity certificate: three adjacent cross-products
# span R^3; after each shell is rigid, spokes remove relative translations
# and neighbor cross-links remove relative rotations.
witness=S.simplify(S.det(S.Matrix.hstack(X[0].cross(X[1]),X[0].cross(X[2]),X[1].cross(X[2]))))
assert S.simplify(witness-(7+3*S.sqrt(5))/32)==0
xx=np.asarray([[float(v) for v in q] for q in X])
rho=math.sqrt(float(r2));h=float(eta);g=float(gamma);b00=float(b0)
P=np.vstack([xx,b00*xx])  # 24x3
names=[];pairs=[];stiff=[];rests=[]
def append(a,b,k):
 names.append('out' if a<12 and b<12 else 'inner' if a>=12 and b>=12 else 'spoke' if (a%12)==(b%12) else 'cross')
 pairs.append((a,b));stiff.append(float(k));rests.append(float(np.linalg.norm(P[a]-P[b])))
for i,j in edges:append(i,j,ke)
for i,j in edges:append(i+12,j+12,ki)
for i in range(12):append(i,i+12,ks)
for i,j in edges:
 append(i,j+12,kcross)
 append(j,i+12,kcross)
assert len(pairs)==132
pairs=np.asarray(pairs,dtype=int);stiff=np.asarray(stiff);rests=np.asarray(rests)
assert (names.count('out'),names.count('inner'),names.count('spoke'),names.count('cross'))==(30,30,12,60)

J=np.zeros((len(pairs),72))
for idx,(i,j) in enumerate(pairs):
 d=(P[i]-P[j])/rests[idx]
 J[idx,i*3:i*3+3]=d
 J[idx,j*3:j*3+3]=-d
JW=np.sqrt(stiff)[:,None]*J
sing=np.linalg.svd(JW,compute_uv=False)
rank=int(np.count_nonzero(sing>1e-9))
assert rank==66,(rank,sing[-12:])
Kfull=JW.T@JW
trans=np.zeros((72,3));rots=np.zeros((72,3))
for j in range(3):
 trans[j::3,j]=1
 rots[:,j]=np.asarray([np.cross(np.eye(3)[j],q) for q in P]).ravel()
assert np.max(np.abs(J@trans))<1e-12
assert np.max(np.abs(J@rots))<1e-12
T=np.zeros((72,2))
T[:36,0]=xx.ravel()
T[36:,1]=-g*xx.ravel()
Mdiag=np.repeat(np.asarray([1.]*12+[float(mi)]*12),3)
Mn=T.T@(Mdiag[:,None]*T)
Kn=T.T@Kfull@T
assert np.max(np.abs(Mn-np.array(M4.evalf(),dtype=float)))<1e-12
assert np.max(np.abs(Kn-np.array(K4.evalf(),dtype=float)))<1e-12
invred=np.linalg.inv(Mn)@Kn
invariance=np.max(np.abs(Kfull@T-(Mdiag[:,None]*T)@invred))
assert invariance<1e-10,invariance
spectrum=eigh(Kfull,np.diag(Mdiag),eigvals_only=True,check_finite=True)
assert np.count_nonzero(spectrum>1e-8)==66
freq=np.sqrt(np.maximum(spectrum,0))
w4=np.sqrt(eigh(np.array(K4.evalf(),dtype=float),np.array(M4.evalf(),dtype=float),eigvals_only=True))
assert all(np.min(abs(freq-w))<1e-8 for w in w4)

ss,zz,force=S.symbols('s z f',real=True)
b=b0-gamma*(zz-eta)
L4=S.sqrt(r2*ss**2+zz**2)
Uc=S.simplify(6*(L4-1)**2+15*(ss-1)**2)
L3=S.sqrt(r2*(ss-b)**2+ss*b)
U3=S.simplify(15*ke*(ss-1)**2+15*ki*(b-b0)**2
    +6*ks*r2*((ss-b)-(1-b0))**2+30*kcross*(L3-Lcross)**2)
assert S.simplify(S.hessian(Uc,(ss,zz)).subs({ss:1,zz:eta})-K4)==S.zeros(2)
assert S.simplify(S.hessian(U3,(ss,zz)).subs({ss:1,zz:eta})-K4)==S.zeros(2)
assert S.simplify(S.Matrix([S.diff(U3,p) for p in [ss,zz]]).subs({ss:1,zz:eta}))==S.zeros(2,1)
# Distinguishing nonlinear Taylor data along the internal z direction at equilibrium.
third4=S.simplify(S.diff(Uc,zz,3).subs({ss:1,zz:eta}))
third3=S.simplify(S.diff(U3,zz,3).subs({ss:1,zz:eta}))
assert abs(float(third4-third3))>1e-3

# Quasistatic force response. High precision evaluation with exact symbolic
# potential, numerical roots at f=±0.01 around the positive stable branch.
G4=S.lambdify((ss,zz),S.Matrix([S.diff(Uc,p) for p in (ss,zz)]),'numpy',cse=True)
G3=S.lambdify((ss,zz),S.Matrix([S.diff(U3,p) for p in (ss,zz)]),'numpy',cse=True)
H4=S.lambdify((ss,zz),S.hessian(Uc,(ss,zz)),'numpy',cse=True)
H3=S.lambdify((ss,zz),S.hessian(U3,(ss,zz)),'numpy',cse=True)
def stat(G,H,f):
 def F(q):return G(*q).reshape(2)-np.array([0,f])
 out=root(F,np.array([1.,h]),jac=lambda q:H(*q),tol=1e-12)
 assert np.linalg.norm(F(out.x))<1e-10,(f,out.message,F(out.x))
 return np.asarray(out.x),float(out.x[0]**3-1),float(np.linalg.eigvalsh(H(*out.x))[0])
static=[]
for f in [-.02,-.01,-.005,0,.005,.01,.02]:
 q4,v4,d4=stat(G4,H4,f);q3,v3,d3=stat(G3,H3,f)
 static.append(dict(force=f,volume_4d=v4,volume_3d_local=v3,difference=v3-v4,smallest_stiffness_4d=d4,smallest_stiffness_3d=d3))

# Local source, reciprocal force, and symmetry assertions. Rotation acts on
# all coordinates, and pairwise distances are exactly SO(3) invariant.
def grad_energy_positions(y):
 p=y.reshape(24,3);d=p[pairs[:,0]]-p[pairs[:,1]]
 lens=np.linalg.norm(d,axis=1)
 dE=stiff*(lens-rests)/lens
 fvec=dE[:,None]*d
 grad=np.zeros((24,3))
 np.add.at(grad,pairs[:,0],fvec)
 np.add.at(grad,pairs[:,1],-fvec)
 return grad
rng=np.random.default_rng(20261022)
Arot=rng.standard_normal((3,3)); Q,_=np.linalg.qr(Arot)
if np.linalg.det(Q)<0:Q[:,0]*=-1
Ptest=P+0.03*rng.standard_normal((24,3))
def energy(p):
 lens=np.linalg.norm(p[pairs[:,0]]-p[pairs[:,1]],axis=1)
 return .5*np.sum(stiff*(lens-rests)**2)
Eres=abs(energy(Ptest@Q.T)-energy(Ptest))
Fres=np.max(abs(grad_energy_positions(Ptest@Q.T)-grad_energy_positions(Ptest)@Q.T))
force_sum=np.max(np.abs(grad_energy_positions(Ptest).sum(axis=0)))
torque_sum=np.max(np.abs(np.sum(np.cross(Ptest,grad_energy_positions(Ptest)),axis=0)))
assert Eres<1e-12 and Fres<1e-12 and force_sum<1e-12 and torque_sum<1e-12

# Finite nonlinear pulse probes for q=(s,z). Models share the same M and
# linear damping but not the cubic constitutive terms.
Mred=np.array(M4.evalf(),dtype=float)
Minv=np.linalg.inv(Mred)
def pulse(t,amp):return amp*math.exp(-.5*((t-8)/1.5)**2)
def integrate(G,amp):
 def rhs(t,y):
  pos=y[:2];vel=y[2:]
  accel=Minv@(np.array([0,pulse(t,amp)])-G(*pos).reshape(2)-.06*Mred@vel)
  return np.concatenate([vel,accel])
 sol=solve_ivp(rhs,(0,70),[1,h,0,0],t_eval=np.linspace(0,70,1401),method='DOP853',rtol=1e-10,atol=1e-12)
 assert sol.success
 return sol.t,sol.y.T
pulse_rows=[];pulse_summary=[]
for amp in [.01,.02,.08]:
 tt,y4=integrate(G4,amp);_,y3=integrate(G3,amp)
 vol4=y4[:,0]**3-1;vol3=y3[:,0]**3-1
 pulse_summary.append(dict(amplitude=amp,peak_4d=float(np.max(abs(vol4))),peak_3d_local=float(np.max(abs(vol3))),maximum_fractional_volume_difference=float(np.max(abs(vol4-vol3)))))
 if amp==.08:
  for t,v4,v3 in zip(tt,vol4,vol3):pulse_rows.append((t,v4,v3,v3-v4))

# Matched shell-facing, force/torque-balanced one-site perturbation tests.
# Unlike total volume, this readout can couple to nontrivial irreducible modes.
J4=np.zeros((42,40))
for row,(i,j) in enumerate(edges):
    dv=xx[i]-xx[j]
    J4[row,3*i:3*i+3]=dv
    J4[row,3*j:3*j+3]=-dv
for i in range(12):
    J4[30+i,3*i:3*i+3]=xx[i]
    J4[30+i,36:39]=-xx[i]
    J4[30+i,39]=h
Kfull4=J4.T@J4
Mfull4=np.eye(40)
spec4=eigh(Kfull4,Mfull4,eigvals_only=True)
assert np.count_nonzero(spec4>1e-8)==34
f4=np.zeros(40);f3=np.zeros(72)
unit=xx[0]/rho
f4[:36]=np.tile(-unit/12,12)
f4[:3]+=unit
f3[:36]=f4[:36]
# Applied forces have vanishing net linear and angular momentum injection.
assert np.max(abs(f4[:36].reshape(12,3).sum(axis=0)))<1e-12
assert np.max(abs(np.sum(np.cross(xx,f4[:36].reshape(12,3)),axis=0)))<1e-12
# shell volume differential via least-squares s channel is 3*delta s.
volume_readout4=np.zeros(40);volume_readout3=np.zeros(72)
volume_readout4[:36]=3*xx.ravel()/(12*float(r2))
volume_readout3[:36]=volume_readout4[:36]
lin_spectrum=[]
for omega in [0.,.15,.24,.3,.5,.886725,1.25,2.007002,2.5]:
 z4=np.linalg.solve(Kfull4-(omega**2)*Mfull4+1j*.06*omega*Mfull4+1.e-12*np.eye(40),f4)
 z3=np.linalg.solve(Kfull-(omega**2)*np.diag(Mdiag)+1j*.06*omega*np.diag(Mdiag)+1.e-12*np.eye(72),f3)
 lin_spectrum.append(dict(omega=omega,shell_site_compliance_4d=float(abs(f4@z4)),shell_site_compliance_3d=float(abs(f3@z3)),volume_amplitude_4d=float(abs(volume_readout4@z4)),volume_amplitude_3d=float(abs(volume_readout3@z3))))
# Volume readout matches because its invariant sector and shell forcing match.
assert max(abs(x['volume_amplitude_3d']-x['volume_amplitude_4d']) for x in lin_spectrum)<1e-8

results={
 'session':'icosa4dvol-20261022-gpt6-c7d2',
 'task':'icosahedral-4d-volume-20261022',
 'prior_branch_revision':'1bc9f2d450bde6deb85f0b05dd31109795ef2b76',
 'evidence':'EXACT / CONDITIONAL / NUMERICAL / FAILED unique dimensional discriminator',
 'model':'two concentric icosahedral shells; local pairwise central Hooke springs, zero prestress; 132 edge springs, 24 free 3D point masses; icosahedral symmetry and SO(3) covariance',
 'spring_counts':{name:names.count(name) for name in ['out','inner','spoke','cross']},
 'target_exposure':'K and M of prior 4D model explicitly selected; 3 spring constants and 1 mass parameter exactly fitted with gamma=1/5,b0=1/4,kcross=1/20 chosen; no measured targets',
 'fitted_values':{'gamma':float(gamma),'b0':float(b0),'cross_spring_k':float(kcross),'outer_edge_k':float(ke),'inner_edge_k':float(ki),'spoke_k':float(ks),'inner_vertex_mass':float(mi)},
 'exact_fitted_expressions':{'k_spoke':str(ks),'k_outer':str(ke),'k_inner':str(ki),'inner_mass':str(mi)},
 'K_target':np.array(K4.evalf(),dtype=float).tolist(),
 'K_reduced_3d':Kn.tolist(),'M_reduced':Mn.tolist(),
 'mass_normalized_frequencies_4d':w4.tolist(),
 'exact_cross_rotation_determinant':str(witness),'full3d_rank':rank,'full3d_nullity':72-rank,'full3d_singular_values_smallest_positive':float(sing[65]),
 'full3d_lowest_positive_angular_frequencies':freq[6:20].tolist(),
 'full3d_spectral_extra_mode_count':64,
 'full4d_lowest_positive_angular_frequencies':np.sqrt(np.maximum(spec4[6:12],0)).tolist(),
 'local_shell_force_nonuniform_frequency_response':lin_spectrum,
 'reduced_subspace_invariance_residual':float(invariance),
 'rotational_energy_residual':float(Eres),'rotational_force_covariance_residual':float(Fres),
 'total_force_residual':float(force_sum),'total_torque_residual':float(torque_sum),
 'cubic_derivative_pure_z':{'4d':float(third4),'3d_local':float(third3),'difference':float(third3-third4)},
 'static_force_vs_volume':static,'nonlinear_pulse_summary':pulse_summary,
 'prior_nonlinear_3d_guided_analogue':'EXACT at all orders in the previously constructed 2-DOF guided analogue; unmodified, not part of this local pairwise construction',
 'scope':'The fully free 3D countermodel has six rigid zero modes and positive all other quadratic spring modes; linear uniform shell volume response is exactly target matched. The nonlinear dynamics differ under fixed Hookean constitutive family. No general theorem excluding all 3D alternatives.',
 'limitations':['132 pairwise springs and 24 nodes vs 42 and 13 in 4D; no physical complexity budget set','3D inner shell is a fitted added scalar carrier with 11 other internal displacement modes','all reference springs are individually stress free but geometry is engineered','4D model suppresses shell fourth displacements and takes an Euclidean apex w','no native UD selection, physical calibration, or material realization','local tests and deterministic code are constructor self checks, not independent replication'],
 'next_discriminant':'Impose matched locality/degree-of-freedom/component-budget constraints and test nonuniform shell-drive spectra on unused preparations; 4D signature remains OPEN.'
}
(OUT/'results.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
with (OUT/'pulse_curves.csv').open('w',newline='') as stream:
 wr=csv.writer(stream);wr.writerow(['dimensionless_time','volume4d_fraction','volume3d_pairwise_fraction','difference_3d_minus_4d'])
 wr.writerows(pulse_rows)
print('PASS: exact reduced Hessian and mass; full 3D rigidity; SO(3)/reciprocity; nonlinear countercheck')
print('3D network counts',len(pairs),'rank',rank,'nullity',72-rank,'positive frequencies',freq[6:12])
print('target freqs',w4,'invariance',invariance,'cubic difference',float(third3-third4))
print('local shell response',lin_spectrum)
print('static',static)
print('pulse summaries',pulse_summary)
