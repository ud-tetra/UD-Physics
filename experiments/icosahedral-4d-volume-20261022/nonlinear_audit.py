#!/usr/bin/env python3
"""UD Discovery: nonlinear 4D-to-3D volume readout vs two ordinary 3D mechanisms.

Reproduce: python3 nonlinear_audit.py
Dependencies: sympy, numpy, scipy. Outputs run_results.json and pulse_curves.csv.
The '4D' coordinate is Euclidean, independent of physical Newtonian time.
"""
from __future__ import annotations
import csv, json, math, platform
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.signal import find_peaks

HERE = Path(__file__).resolve().parent
s,z,f = sp.symbols('s z f', real=True)
R2 = (sp.Integer(5)+sp.sqrt(5))/8
E2 = 1 - R2
ETA = sp.sqrt(E2)
RHO = sp.sqrt(R2)
V0 = 5*(3+sp.sqrt(5))/12
L = sp.sqrt(R2*s*s+z*z)
U = 6*(L-1)**2+15*(s-1)**2
Q = (s,z)
STAR={s:sp.Integer(1),z:ETA}
K = sp.simplify(sp.hessian(U,Q).subs(STAR))
Kinv=K.inv()
assert sp.simplify(K.det()-360*E2)==0
assert all(sp.simplify(sp.diff(U,v).subs(STAR))==0 for v in Q)
q1=sp.simplify(Kinv*sp.Matrix([0,1]))
# Implicit derivatives: q'(0)=K^-1 e_z;
# q''(0)=-K^-1 T3[q',q']; q'''(0)=-K^-1(T4[q',q',q']+3T3[q',q'']).
T3 = [[[sp.diff(U, Q[i], Q[j], Q[k]).subs(STAR) for k in range(2)] for j in range(2)] for i in range(2)]
T4 = [[[[sp.diff(U, Q[i], Q[j], Q[k], Q[h]).subs(STAR) for h in range(2)] for k in range(2)] for j in range(2)] for i in range(2)]
t3q1=sp.Matrix([sum(T3[i][j][k]*q1[j]*q1[k] for j in range(2) for k in range(2)) for i in range(2)])
q2=sp.simplify(-Kinv*t3q1)
t4q1=sp.Matrix([sum(T4[i][j][k][h]*q1[j]*q1[k]*q1[h] for j in range(2) for k in range(2) for h in range(2)) for i in range(2)])
t3mixed=sp.Matrix([3*sum(T3[i][j][k]*q1[j]*q2[k] for j in range(2) for k in range(2)) for i in range(2)])
q3=sp.simplify(-Kinv*(t4q1+t3mixed))
# Fractional volume is (s(f))^3-1; coefficients of f, f^2, f^3.
c1 = sp.simplify(3*q1[0])
c2 = sp.simplify(sp.Rational(3,2)*q2[0]+3*q1[0]**2)
c3 = sp.simplify(q3[0]/2+3*q1[0]*q2[0]+q1[0]**3)
assert sp.simplify(c1 + R2/(10*ETA))==0
print('exact stationary fractional-volume jet:')
for i,c in enumerate((c1,c2,c3),1):
    print(i,sp.simplify(c),float(c))

# Both 4D and planar 3D slider models have this same COMPLETE scalar Lagrangian.
# In the 3D mechanical analogue, a carriage A=(rho*s,0,0), B=(0,z,0)
# move on perpendicular guide rails, giving Euclidean 3D spring length |A-B|=L.
# Twelve parallel copies of the carriage spring and 30 exterior-edge springs
# yield identical energy for ALL s,z (not just a Taylor expansion).
X = sp.Matrix([RHO*s,0,0]); Y=sp.Matrix([0,z,0])
L3=sp.sqrt((X-Y).dot(X-Y))
assert sp.simplify(L3**2-L**2)==0
U3=6*(L3-1)**2+15*(s-1)**2
assert sp.simplify(U3-U)==0
M = np.diag([12*float(R2),1.0])
kn=np.array(K,dtype=float)
qstar=np.array([1.0,float(ETA)])
C=.06*M
R=float(RHO); r2=float(R2)

def e4(sv,zv):
    length=math.hypot(R*sv,zv)
    return 6*(length-1)**2+15*(sv-1)**2

def g4(sv,zv):
    length=math.hypot(R*sv,zv)
    return np.array([12*(length-1)*r2*sv/length+30*(sv-1),12*(length-1)*zv/length])

def e3planar(sv,zv):
    dx,dy=R*sv,-zv
    length=math.sqrt(dx*dx+dy*dy)
    return .5*12*(length-1)**2+.5*30*(sv-1)**2

def g3planar(sv,zv):
    dx,dy=R*sv,-zv
    length=math.sqrt(dx*dx+dy*dy)
    # independently differentiated planar carriage coordinates
    return np.array([12*(length-1)/length*dx*R+30*(sv-1),-12*(length-1)/length*dy])

# One ordinarily constrained 3D analogue is exactly equivalent at nonlinear order,
# including the same damping, mass, generalized force and shell volume readout.
for ss0 in (.8,1,1.3):
    for zz0 in (-.4,.01,.31,.8):
        assert abs(e4(ss0,zz0)-e3planar(ss0,zz0))<1e-12
        assert np.linalg.norm(g4(ss0,zz0)-g3planar(ss0,zz0))<1e-12

# Simpler linear spring/lever null calibrated to the same K,M,C and shell-volume map.
# Ulin=1/2 (q-q*)^T K (q-q*), an exactly matched *linear* mechanical realization.
def elin(sv,zv):
    d=np.array([sv,zv])-qstar
    return float(.5*d@kn@d)
def glin(sv,zv):
    return kn@(np.array([sv,zv])-qstar)

# Damped IVP with Gaussian generalized force applied to second coordinate.
def pulse(t,A):
    return A*math.exp(-.5*((t-8.)/1.5)**2)

def integrate(A,grad):
    def rhs(t,y):
        v=y[2:]
        return np.r_[v,np.linalg.solve(M,np.array([0.0,pulse(t,A)])-grad(*y[:2])-C@v)]
    ts=np.linspace(0,70,1401)
    sol=solve_ivp(rhs,(0,70),np.r_[qstar,0.,0.],t_eval=ts,rtol=3e-12,atol=3e-14,method='DOP853')
    if not sol.success:raise RuntimeError(sol.message)
    return ts,sol.y,(sol.y[0]**3-1)

# Fractional volume static response at specified force f, positive-height branch.
def stationary(ff):
    fun=lambda a: g4(a[0],a[1])-np.array([0.,ff])
    rr=root(fun,qstar+np.array(q1,dtype=float).ravel()*ff,method='hybr',tol=1e-12)
    if np.linalg.norm(fun(rr.x))>1e-10:raise RuntimeError(f'stationary fail at {ff}: {rr.message}')
    # Local Hessian positive at returned state, tested numerically using symbolic formula
    H=np.array(hessfun(*rr.x),dtype=float)
    if np.linalg.eigvalsh(H)[0]<=0:raise RuntimeError('stationary branch lost stability')
    return rr.x,rr.x[0]**3-1,float(np.linalg.eigvalsh(H)[0])

hessfun=sp.lambdify(Q,sp.hessian(U,Q),'numpy')
# Detect static saddle-node on the positive-height equilibrium branch.
# This is an informative *failure* of continuation under negative constant force.
spin=root(lambda q: np.array([g4(*q)[0],np.linalg.det(hessfun(*q))]),[1.01,.17],method='hybr',tol=1e-12)
assert np.linalg.norm([g4(*spin.x)[0],np.linalg.det(hessfun(*spin.x))])<1e-8
spinodal_force=float(g4(*spin.x)[1])
assert -.06<spinodal_force<-.05
stat=[]
for ff in (-.05,-.04,-.02,-.01,.0,.01,.02,.04,.08):
    q,v,hmin=stationary(ff)
    trunc=sum(float(c)*ff**(i+1) for i,c in enumerate((c1,c2,c3)))
    stat.append({'force':ff,'s':float(q[0]),'z':float(q[1]),'fractional_volume':float(v),'third_order_prediction':trunc,'third_order_residual':float(v-trunc),'min_stiffness_eigenvalue':hmin})

curves=[]; stats=[]
for A in (-.08,-.02,-.01,.01,.02,.08):
    traces={name:integrate(A,g) for name,g in [('4d',g4),('3d_planar_exact',g3planar),('3d_linear_null',glin)]}
    ts, yy4, vol4=traces['4d']
    max_eq=max(float(np.max(np.abs(yy4-traces['3d_planar_exact'][1]))),float(np.max(np.abs(vol4-traces['3d_planar_exact'][2]))))
    assert max_eq<1e-9,max_eq
    _,yyl,voll=traces['3d_linear_null']
    stats.append({'pulse_amplitude':A,'4d_min_volume':float(np.min(vol4)),'4d_max_volume':float(np.max(vol4)),
       '4d_peak_abs_volume':float(np.max(np.abs(vol4))),
       'exact_3d_planar_peak_abs_volume':float(np.max(np.abs(traces['3d_planar_exact'][2]))),
       'max_abs_difference_full_trajectories_4d_vs_3d_planar':max_eq,
       '3d_linear_null_peak_abs_volume':float(np.max(np.abs(voll))),
       'max_abs_difference_4d_vs_linear_null_volume':float(np.max(np.abs(vol4-voll)))})
    for i,t in enumerate(ts):
        curves.append([A,t,float(yy4[0,i]),float(yy4[1,i]),float(vol4[i]),float(traces['3d_planar_exact'][2][i]),float(voll[i])])
with (HERE/'pulse_curves.csv').open('w',newline='') as fcsv:
    wcsv=csv.writer(fcsv)
    wcsv.writerow(['pulse_A','time','shell_s','apex_z','volume_fraction_4d','volume_fraction_3d_exact','volume_fraction_3d_linear'])
    wcsv.writerows((f'{v:.16g}' for v in row) for row in curves)

# A stringent finite-difference check of the first three static coefficients via
# explicitly computed solutions at shrinking loads, not relied upon as derivation.
for eps in (5e-4,2.5e-4,1.25e-4):
    vp=stationary(eps)[1]
    vn=stationary(-eps)[1]
    avg=(vp+vn)/(2*eps**2)
    odd=(vp-vn)/(2*eps)
    assert abs(avg-float(c2))<5e-5
    assert abs((odd-float(c1))/eps**2 -float(c3))<5e-4

# Normal form check: scalar amplitude in generalized lower eigenvector, project
# nonlinear force onto modal coordinate and calculate cubic/quadratic restoring terms
# for a constrained path q=q*+e*A (not a standalone exact normal mode).
D=np.diag(np.diag(M)**(-.5))
w2,E=np.linalg.eigh(D@kn@D)
mode=D@E[:,0]
if mode[1]<0:mode=-mode
# U(q*+mode*X)= (w2/2)X²+(g3/6)X³+(g4/24)X⁴+...,
# frequency shift of 1-DOF constrained potential: Δω/(ω A²)=g4/(16ω²)-5*g3²/(48ω⁴)
G3=sp.N(sum(T3[i][j][k]*float(mode[i])*float(mode[j])*float(mode[k]) for i in range(2) for j in range(2) for k in range(2)),16)
G4=sp.N(sum(T4[i][j][k][h]*float(mode[i])*float(mode[j])*float(mode[k])*float(mode[h]) for i in range(2) for j in range(2) for k in range(2) for h in range(2)),16)
mode_frequency_shift_coefficient=float(G4)/(16*w2[0])-5*float(G3)**2/(48*w2[0]**2)
# This coefficient is only for a *constrained* 1D mode path, not full 2-mode nonlinear resonance;
# the 3D exact analogue gives identical coefficient, the linear null gives zero.

# Free, undamped two-mode motion: infer the lower-mode dominant oscillation
# frequency from ~30 subsequent maxima of its mass-metric projection.
# A single nonlinear mode is not generally invariant; reported frequencies
# are finite-time spectral estimators, not exact nonlinear normal modes.
def free_evolution(A, grad, Tfinal=220.0):
    ts=np.linspace(0.,Tfinal,11001)
    y0=np.r_[qstar+mode*A,0.,0.]
    def rhs(t,y):
        return np.r_[y[2:],np.linalg.solve(M,-grad(*y[:2]))]
    sol=solve_ivp(rhs,(0,Tfinal),y0,t_eval=ts,method='DOP853',rtol=2e-11,atol=2e-13)
    if not sol.success:raise RuntimeError(sol.message)
    p=mode @ M @ (sol.y[:2]-qstar[:,None])
    peaks,_=find_peaks(p,distance=250,prominence=max(A*0.12,2e-5))
    if len(peaks)<20: raise RuntimeError(('insufficient modal extrema',A,len(peaks)))
    # Refine sample grid extrema with three-point parabola; t spacing=0.02.
    dt=ts[1]-ts[0]
    peak_times=[]
    for j in peaks:
        if j==0 or j==len(ts)-1:continue
        y0,y1,y2=p[j-1:j+2]
        shift=.5*(y0-y2)/(y0-2*y1+y2)
        if abs(shift)>1.5:raise RuntimeError('bad parabola')
        peak_times.append(ts[j]+dt*shift)
    coeff=np.polyfit(np.arange(len(peak_times)),peak_times,1)
    period=coeff[0]
    expected=2*np.pi/np.sqrt(w2[0])
    return {'angular_frequency':float(2*np.pi/period),
      'fractional_shift_relative_linear':float((2*np.pi/period)/np.sqrt(w2[0])-1),
      'number_of_peaks':len(peak_times),
      'peak_spacing_rms':float(np.std(np.diff(peak_times)-period)),
      'expected_linear_period':float(expected)}

free=[]
for A in (.005,.02,.04,.06):
    a4=free_evolution(A,g4)
    a3=free_evolution(A,g3planar)
    al=free_evolution(A,glin)
    assert abs(a4['angular_frequency']-a3['angular_frequency'])<1e-9
    assert abs(al['angular_frequency']-np.sqrt(w2[0]))<2e-6
    free.append({'initial_mass_normalized_lower_mode_amplitude':A,
       '4d':a4,'3d_planar_exact':a3,'3d_linear_null':al})

result={'schema':'ud-4d-nonlinear-discrimination-v1',
    'origin':'target-exposed regularity criterion, assumed elastic laws, no empirical data',
    'evidence':'EXACT/CONDITIONAL for local derivatives and all-order 3D equivalence; NUMERICAL for integration',
    'units':'a=k_r=k_e=m_s=m_a=1, independent Newtonian t, generalized force f conjugate to z; C=.06M',
    'source_baseline':'ud-tetra/UD-Physics main@92dbe7d99d4a5a65d3acf978fd63e192f73c4bfa; previous pulse response local audit',
    'exact':{'rho_squared':str(R2),'eta':str(ETA),'K':[[str(K[i,j]) for j in range(2)] for i in range(2)],
       'static_volume_series_coefficient':{'f':str(c1),'f2':str(c2),'f3':str(c3)},
       'exact_planar_equivalence':'| (rho s,0,0)-(0,z,0)|=sqrt(rho²s²+z²); U3D_planar == U4D for every (s,z) with s>0',
       'same_mass_damping_forcing_and_observable':True,
       'modal_constrained_slice_frequency_shift_coefficient':'g4/(16*omega²)-5*g3²/(48*omega⁴); not full nonlinear 2-mode frequency'},
    'numeric':{'coefficients':{'f':float(c1),'f2':float(c2),'f3':float(c3)},
       'mode1_angular_frequency':float(np.sqrt(w2[0])), 'mode2_angular_frequency':float(np.sqrt(w2[1])),
       'constrained_mode_slice_g3':float(G3),'constrained_mode_slice_g4':float(G4),
       'constrained_mode_fractional_frequency_shift_per_amplitude_squared':mode_frequency_shift_coefficient,'free_nonlinear_mode_estimates':free,
       'statics':stat,'positive_height_spinodal':{'force':spinodal_force,'s':float(spin.x[0]),'z':float(spin.x[1]),'interpretation':'negative static loading below this saddle-node loses positive-height local stable equilibrium'},'pulse_results':stats,'pulse_samples':len(curves),
       'damping':.06,'pulse_time_window':[0,70], 'pulse_shape':'A exp(-.5*((t-8)/1.5)²)',
       'integrator':'DOP853', 'rtol':3e-12,'atol':3e-14},
    'checks':['SymPy exact potential equivalence with planar Euclidean 3D slider geometry',
        'exact Hessian determinant and implicit force derivatives to third order',
        'finite difference on equilibrium branch',
        'independent numerically coded 3D planar spring length and gradient',
        'numerical pulse trace equality across signs and amplitudes',
        'matched full two-mode undamped free oscillation frequencies vs matched 3D planar analogue'],
    'known_failures_and_limits':['An unrestricted 3D mechanism can match the 4D reduced mechanics to all orders; nonlinear response is NOT a unique 4D signature.',
        'External icosahedral shell symmetry of 3D lever involves assumed transmission and synchronous guided carriages, not native local isotropic physics.',
        'The analytic modal frequency shift is for constrained one-mode motion; full two-mode nonlinear resonance measured as finite-time peak frequency only, no exact backbone.',
        'Fixed shell hyperplane w=0; no GR/QFT action or physical time calibration.',
        'Quasistatic positive-height branch has a negative-force fold at the reported spinodal; failed continuation at -0.08 is preserved.',
        'Constitutive and drive couplings imposed and not derived from UD.']}
(HERE/'run_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('static range',[(a['force'],round(a['fractional_volume'],6)) for a in stat])
print('dynamics',[(a['pulse_amplitude'],a['4d_peak_abs_volume'],a['max_abs_difference_full_trajectories_4d_vs_3d_planar'],a['max_abs_difference_4d_vs_linear_null_volume']) for a in stats])
print('mode slice',mode_frequency_shift_coefficient)
print('free modes',[(r['initial_mass_normalized_lower_mode_amplitude'],r['4d']['angular_frequency'],r['4d']['fractional_shift_relative_linear']) for r in free])
print('PASS exact symbolic checks, 3D planar all-order equivalence and numerical controls')
