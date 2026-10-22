"""Passive K4 difference damping: exact certificates and finite pulse campaign.

Run with OPENBLAS_NUM_THREADS=1 for predictable small-matrix performance.
The frequency-band certificate uses rational inequalities, not a frequency grid.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt, sqrt
from pathlib import Path
import argparse
import csv
import importlib.util
import json
import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('previous', ROOT/'experiments/heart-shell-robustness/analyze.py')
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)
P = np.eye(4)-np.ones((4,4))/4


def certificate():
    """Exact all-box guarantees; sqrt lower bounds rounded DOWN as rationals."""
    e, gamma = F(1,20), F(1,2)
    results=[]
    for lo,hi in [(F(4,5),F(6,5)),(F(11,2),F(13,2))]:
        bounds=[]
        for j in range(100):
            l=lo+(hi-lo)*j/100; h=lo+(hi-lo)*(j+1)/100
            assert not l <= 2 <= h
            sl=F(isqrt(l.numerator*10**12//l.denominator),10**6)
            assert sl*sl <= l
            s=4*gamma*sl; G=2*e; V=2*e*(1+h)
            dmin=min(abs(2-l),abs(2-h)); dmax=max(abs(2-l),abs(2-h))
            perturb=V*V/(4*s); z=V*G/(4*s)
            assert dmin-e*(1+h)>perturb  # invertibility of full shell block
            bmin=(1-e-z)/(dmax+e*(1+h)+perturb)
            assert bmin>0
            B=(G/bmin+V)/s  # ||d||/|b| upper bound
            assert B*B <= F(12,133)  # L_h <= 1/20 exactly
            assert bmin*dmin >= F(4,5)  # coherent gain retention >= 80%
            bounds.append((B*B,bmin*dmin))
        B2=max(x[0] for x in bounds); gain=min(x[1] for x in bounds)
        results.append({'lambda_interval':[str(lo),str(hi)],'omega_interval':[sqrt(float(lo)),sqrt(float(hi))],
                        'subintervals':100,'B_squared_bound_exact':str(B2),'gain_lower_exact':str(gain),
                        'linear_volume_leakage_upper_rounded_display':sqrt(float(B2/(36+B2))),
                        'coherent_gain_lower_rounded_display':float(gain)})
    # Projection/combinatorial facts: 6 distinct edges, degree 3, Laplacian 4P.
    L=[[F(3 if i==j else -1) for j in range(4)] for i in range(4)]
    assert len(list(__import__('itertools').combinations(range(4),2)))==6
    assert all(sum(row)==0 for row in L)
    assert all(sum(L[i][k]*L[k][j] for k in range(4))==4*L[i][j] for i in range(4) for j in range(4))
    # The chosen scalar difference law is NOT ordinary axial damping on tetrahedron edges.
    # For reference rays at L=1, axial extension rate = sqrt(2)*(q_i'+q_j').
    rays=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    for i in range(4):
        for j in range(i+1,4):
            edge=[rays[i][k]-rays[j][k] for k in range(3)]
            assert sum(v*v for v in edge)==8
            assert sum(edge[k]*rays[i][k] for k in range(3))==4
            assert sum(edge[k]*rays[j][k] for k in range(3))==-4
    # Symbolic polynomial identity behind balanced harmonic ratio.
    # D*r = eps*(1-lambda)+lambda*eta; q=b*1+s*d.
    # Rational samples check derivation independently against full complex solve below.
    errors=[]
    signs=np.array([1,1,-1,-1])
    for eps,eta in [(F(1,20),F(0)),(F(0),F(1,20)),(F(1,20),F(-1,20))]:
        for lam in [F(1),F(4),F(6)]:
            g=1+float(eps)*signs;m=1+float(eta)*signs; w=sqrt(float(lam))
            H=np.diag(3+g-float(lam)*m)-.5*np.ones((4,4))-4j*float(gamma)*w*P
            q=np.linalg.solve(H,g);b=q.mean();r=(q[0]-b)/b
            predicted=complex(eps*(1-lam)+lam*eta)/(complex(4-lam-eps*eps+eps*lam*eta)-4j*float(gamma)*w)
            errors.append(abs(r-predicted))
    assert max(errors)<1e-13
    return {'status':'PASS','epsilon':'1/20','gamma':'1/2','design_criteria':{'linear_volume_Lh_max':'1/20','coherent_gain_retention_min':'4/5'},
            'all_box_certificate':results,'balanced_formula_full_solve_max_error':max(errors),
            'ordinary_axial_edge_warning':'edge extension rate=sqrt(2)*L*(qi_prime+qj_prime); common breathing dissipates 48*c*L^2*b_prime^2 for six equal axial dashpots',
            'former_dark_example':{'lambda':'4','epsilon':'1/20','eta':'0','gamma':'1/2',
                                   'd_over_b_abs_exact':'60/sqrt(2560001)',
                                   'volume_differential_over_collective_exact':'20/sqrt(2560001)'}}


def trajectory(g,m,gamma,t):
    K,mass=previous.matrices(g,m)
    C=np.zeros((5,5));C[1:,1:]=4*gamma*P
    A=np.zeros((10,10));A[:5,5:]=np.eye(5);A[5:,:5]=-K/mass[:,None];A[5:,5:]=-C/mass[:,None]
    eig,V=np.linalg.eig(A);cond=float(np.linalg.cond(V))
    # Chosen sweep avoids critical gamma=1. Repeated modes need not be defective.
    assert cond<1e5
    z0=np.r_[.1,np.zeros(9)];coeff=np.linalg.solve(V,z0)
    z=(np.exp(t[:,None]*eig)*coeff)@V.T
    imag=float(np.max(abs(z.imag)));assert imag<2e-11
    z=z.real;x=z[:,:5];v=z[:,5:]
    E=(np.sum(v*v*mass,axis=1)+np.einsum('ti,ij,tj->t',x,K,x))/2
    e0=float(z0[:5]@K@z0[:5]/2)
    pd=v[:,1:]@P
    power=4*gamma*np.sum(pd*pd,axis=1)
    loss=previous.integrate(power,t)
    balance=abs(E[-1]-e0+loss)/e0
    assert max(np.diff(E))/e0<2e-11 and balance<2e-4
    assert np.min(x[:,1:])>-1 and e0<.5
    direct=expm(A*.25)@z0
    via_eig=((np.exp(.25*eig)*coeff)@V.T).real
    check=float(np.max(abs(direct-via_eig)));assert check<3e-12
    return x,{'relative_energy_remaining':float(E[-1]/e0),'energy_balance_relative_error':balance,
              'maximum_energy_increase_step_relative':float(max(np.diff(E))/e0),
              'eigenvector_condition':cond,'imaginary_residual':imag,'expm_check_error':check}


def metrics(x,t):
    q=x[:,1:];s=1+q
    y=np.column_stack([np.prod(s[:,[j for j in range(4) if j!=i]],axis=1)-1 for i in range(4)])
    mean=y.mean(axis=1);d=y-mean[:,None]
    numerator=previous.integrate(np.sum(d*d,axis=1),t)
    denominator=previous.integrate(np.sum(y*y,axis=1),t)
    rms=sqrt(previous.integrate(mean*mean,t)/(t[-1]-t[0]))
    return sqrt(numerator/denominator),rms


def main(out):
    out.mkdir(parents=True,exist_ok=True)
    cert=certificate();t=np.linspace(0,100,4001)
    signs=list(product((-1,1),repeat=4));rows=[];worsts={};checks=[]
    for eps in [.01,.05,.1,.2]:
        for gs in signs:
            for ms in signs:
                g=1+eps*np.array(gs);m=1+eps*np.array(ms)
                x,_,_=previous.trajectory(g,m,t);L0,rms0=metrics(x,t)
                for gamma in [.1,.25,.5]:
                    x,ch=trajectory(g,m,gamma,t);checks.append(ch)
                    L,rms=metrics(x,t)
                    row={'epsilon':eps,'gamma':gamma,'stiffness_pattern':','.join(map(str,gs)),
                         'inertia_pattern':','.join(map(str,ms)),
                         'volume_leakage':L,'undamped_volume_leakage':L0,
                         'mean_volume_rms':rms,'undamped_mean_volume_rms':rms0,
                         'mean_volume_rms_retention':rms/rms0,**ch}
                    rows.append(row);key=(eps,gamma)
                    if key not in worsts or L>worsts[key]['volume_leakage']:worsts[key]=row
    summaries=[];convergence=[]
    for eps in [.01,.05,.1,.2]:
        for gamma in [.1,.25,.5]:
            selected=[r for r in rows if r['epsilon']==eps and r['gamma']==gamma]
            w=worsts[(eps,gamma)]
            summaries.append({'epsilon':eps,'gamma':gamma,'corner_count':256,
                'max_volume_leakage':w['volume_leakage'],
                'min_mean_rms_retention':min(r['mean_volume_rms_retention'] for r in selected),
                'max_mean_rms_retention':max(r['mean_volume_rms_retention'] for r in selected),
                'min_energy_remaining':min(r['relative_energy_remaining'] for r in selected),
                'worst_leakage_pattern':{k:w[k] for k in ['stiffness_pattern','inertia_pattern']}})
            if gamma==.5:
                gs=np.fromstring(w['stiffness_pattern'],sep=',');ms=np.fromstring(w['inertia_pattern'],sep=',')
                vals=[]
                for n in [8001,16001]:
                    tf=np.linspace(0,100,n);x,_=trajectory(1+eps*gs,1+eps*ms,gamma,tf);vals.append(metrics(x,tf)[0])
                assert abs(vals[0]-vals[1])<2e-6
                convergence.append({'epsilon':eps,'coarse':w['volume_leakage'],'fine_8001':vals[0],
                                    'fine_16001':vals[1],'fine_difference':abs(vals[0]-vals[1])})
    # Exact symmetric pulse is unmodified, checked against the undamped implementation.
    x,ch=trajectory(np.ones(4),np.ones(4),.5,t);base,_,_=previous.trajectory(np.ones(4),np.ones(4),t)
    symmetry_error=float(np.max(abs(x-base)));assert symmetry_error<1e-11
    # An interior sample remains an exploratory comparison, not a probabilistic bound.
    rng=np.random.default_rng(4307);interior=[]
    for _ in range(256):
        g=1+.05*rng.uniform(-1,1,4);m=1+.05*rng.uniform(-1,1,4)
        x,_=trajectory(g,m,.5,t);und,_,_=previous.trajectory(g,m,t)
        L,r=metrics(x,t);_,r0=metrics(und,t);interior.append((L,r/r0))
    # Distinct full linear solves sample the exact all-box harmonic certificate.
    harmonic=[]
    for lo,hi in [(.8,1.2),(5.5,6.5)]:
        maxL=0.;minGain=1e9
        for lam in np.linspace(lo,hi,31):
            for gs in signs:
                for ms in signs:
                    g=1+.05*np.array(gs);m=1+.05*np.array(ms)
                    H=np.diag(3+g-lam*m)-.5*np.ones((4,4))-2j*sqrt(lam)*P
                    q=np.linalg.solve(H,g);b=q.mean();d=q-b
                    L=float(np.linalg.norm(d)/sqrt(36*abs(b)**2+np.linalg.norm(d)**2))
                    gain=abs(b)*abs(2-lam);maxL=max(maxL,L);minGain=min(minGain,gain)
        assert maxL<.05 and minGain>.8
        harmonic.append({'lambda_interval':[lo,hi],'frequency_points':31,'corner_patterns':256,
                         'max_linear_volume_leakage':maxL,'min_coherent_gain_retention':minGain})
    summary={'evidence':['EXACT_CONDITIONAL','NUMERICAL','FIT_DESIGN'],'certificate':cert,
        'configuration':{'gamma_sweep':[.1,.25,.5],'epsilon_sweep':[.01,.05,.1,.2],
                         'time_window':[0,100],'samples':4001,'a0':.1,'dtype':'float64',
                         'numpy':np.__version__,'scipy':scipy.__version__,
                         'gamma_selection':'1/2 selected for exact 5% all-box harmonic band certificate before pulse results; not optimized for pulse outcomes'},
        'pulse_scan':summaries,'pulse_rows':len(rows),'quadrature_convergence':convergence,
        'checks':{'maximum_energy_balance_error':max(c['energy_balance_relative_error'] for c in checks),
                  'maximum_eigenvector_condition':max(c['eigenvector_condition'] for c in checks),
                  'maximum_expm_crosscheck_error':max(c['expm_check_error'] for c in checks),
                  'symmetry_trajectory_error':symmetry_error},
        'interior_5percent':{'seed':4307,'count':256,'max_leakage':max(x[0] for x in interior),
                            'min_rms_retention':min(x[1] for x in interior)},
        'harmonic_full_solve_check':harmonic,
        'limits':['Pulse scan is finite and exploratory; harmonic certificate concerns linear volume phasors and prescribed heart amplitude, not a fixed external force.',
                  'Damping is assumed and target-informed. Under disorder it can dissipate collective pulse energy.',
                  'No native UD damping derivation, material, physical clock or physical promotion.']}
    with (out/'pulse-scan.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    main(parser.parse_args().out)
