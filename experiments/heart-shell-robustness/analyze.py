"""Exact mismatch identities plus numerical finite-window heart-shell scan."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse
import csv
import json
import math
import numpy as np


def qsolve(a,b):
    a=[list(map(Q,row))+[Q(v)] for row,v in zip(a,b)];n=len(a)
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
        c=a[j][j];a[j]=[v/c for v in a[j]]
        for k in range(n):
            if k!=j:
                c=a[k][j];a[k]=[v-c*w for v,w in zip(a[k],a[j])]
    return [row[-1] for row in a]

def qshape(g,m,lam):
    # Unit prescribed heart amplitude, Ks=1, Kt=1/2; exact shell dynamic stiffness.
    h=[[((1+g[i]+2-lam*m[i]) if i==j else Q(0))-Q(1,2) for j in range(4)] for i in range(4)]
    q=qsolve(h,g);b=sum(q)/4;return q,b

def exact_checks():
    # Balanced two-group pattern s=(+,+,-,-).
    p=[1,1,-1,-1];rows=[]
    for eps,eta,label in [(Q(1,20),Q(0),'stiffness_only'),(Q(0),Q(1,20),'inertia_only'),(Q(1,20),Q(1,20),'aligned'),(Q(1,20),Q(-1,20),'opposed')]:
        g=[1+eps*s for s in p];m=[1+eta*s for s in p]
        for lam in [Q(0),Q(1),Q(6),Q(39,10),Q(41,10)]:
            q,b=qshape(g,m,lam);r=((eps*(1-lam)+lam*eta)/(4-lam-eps*eps+eps*lam*eta))
            assert all(q[i]==b*(1+p[i]*r) for i in range(4))
            if lam in (1,6):rows.append({'pattern':label,'squared_frequency':str(lam),'d_over_b':str(r),'linear_volume_differential_over_collective':str(abs(r)/3)})
    # General projected differential equation, checked with exact nonsymmetric parameters.
    g=[Q(9,10),Q(11,10),Q(21,20),Q(19,20)];m=[Q(26,25),Q(24,25),Q(101,100),Q(99,100)]
    gb=sum(g)/4;mb=sum(m)/4;dg=[x-gb for x in g];dm=[x-mb for x in m]
    for lam in [Q(0),Q(1),Q(6),Q(39,10)]:
        q,b=qshape(g,m,lam);d=[x-b for x in q]
        unprojected=[(3+g[i]-lam*m[i])*d[i] for i in range(4)]
        lhs=[x-sum(unprojected)/4 for x in unprojected]
        rhs=[dg[i]*(1-b)+lam*dm[i]*b for i in range(4)]
        assert lhs==rhs
        gap=abs(3+gb-lam*mb);rho=max(abs(dg[i]-lam*dm[i]) for i in range(4))
        if gap>rho:
            bound=(2*max(map(abs,dg))*abs(1-b)+2*abs(lam)*max(map(abs,dm))*abs(b))/(gap-rho)
            assert sum(x*x for x in d)<=bound*bound
    # A protected in-phase mode under arbitrary spoke disorder when onsite K/M ratios match.
    for g in [[Q(7,10),Q(9,10),Q(6,5),Q(3,2)],[Q(1,100),Q(2),Q(3),Q(5)]]:
        q,b=qshape(g,[Q(1)]*4,Q(1));assert q==[Q(1)]*4 and b==1
    # Engineered compensation at the exposed reference upper mode lambda=6.
    eps=Q(1,10);eta=Q(5,6)*eps
    q,b=qshape([1+eps*s for s in p],[1+eta*s for s in p],Q(6));assert len(set(q))==1
    # Exact anti-coherence counterexample at the former dark frequency lambda=4.
    eps=Q(1,20);q,b=qshape([1+eps*s for s in p],[Q(1)]*4,Q(4));r=(q[0]-b)/b
    assert r==3/eps and abs(r)/3==20
    return {'status':'PASS','projected_differential_identity_checks':4,'balanced_reference_shapes':rows,'near_dark_counterexample':{'epsilon':'1/20','lambda':'4','d_over_b':str(r),'linear_volume_differential_over_collective':str(abs(r)/3)},'compensation':'eta=5*epsilon/6 preserves uniform lambda6 mode for balanced pattern; target-informed design, not independent prediction'}


def matrices(g,m,matched_pinning=False):
    g=np.asarray(g,dtype=np.float64);m=np.asarray(m,dtype=np.float64)
    mass=np.r_[1.,m];k=np.diag(mass if matched_pinning else np.ones(5))
    for i,v in enumerate(g,1):k[0,0]+=v;k[i,i]+=v;k[0,i]-=v;k[i,0]-=v
    for i in range(1,5):
        for j in range(i+1,5):k[i,i]+=.5;k[j,j]+=.5;k[i,j]-=.5;k[j,i]-=.5
    return k,mass

def trajectory(g,m,t,matched_pinning=False):
    k,mass=matrices(g,m,matched_pinning);root=np.sqrt(mass)
    h=k/root[:,None]/root[None,:];lam,v=np.linalg.eigh(h)
    assert min(lam)>0
    initial=np.array([.1,0,0,0,0]);coeff=v.T@(root*initial);omega=np.sqrt(lam)
    x=((np.cos(t[:,None]*omega)*coeff)@v.T)/root
    vel=((-np.sin(t[:,None]*omega)*omega*coeff)@v.T)/root
    energy=(np.sum(mass*vel*vel,axis=1)+np.einsum('ti,ij,tj->t',x,k,x))/2
    e0=float(initial@k@initial/2)
    residual=float(np.max(abs(energy-e0))/e0)
    assert residual<2e-12
    assert np.min(x[:,1:])>-1 and e0<.5
    eigres=float(np.linalg.norm(h@v-v*lam,ord=np.inf));assert eigres<1e-12
    return x,vel,{'energy_relative_residual':residual,'eigen_residual_inf':eigres,'minimum_squared_frequency':float(min(lam)),'initial_energy':e0}

def integrate(y,t):return float(np.sum((y[:-1]+y[1:])*np.diff(t)/2))

def signal_leakage(x,t):
    q=x[:,1:];s=1+q
    # Exact fractional volume changes: reference child volume V0/4 cancels.
    y=np.column_stack([np.prod(s[:,[j for j in range(4) if j!=i]],axis=1)-1 for i in range(4)])
    pd=y-y.mean(axis=1,keepdims=True)
    numerator=integrate(np.sum(pd*pd,axis=1),t);denominator=integrate(np.sum(y*y,axis=1),t)
    assert denominator>0
    return math.sqrt(numerator/denominator)

def short_series_check(g,m):
    k,mass=matrices(g,m);a=np.zeros((10,10));a[:5,5:]=np.eye(5);a[5:,:5]=-k/mass[:,None]
    t=.25;ex=np.eye(10);term=np.eye(10)
    for j in range(1,61):term=term@(a*t)/j;ex+=term
    initial=np.r_[.1,np.zeros(9)];direct=ex@initial
    x,v,_=trajectory(g,m,np.array([0.,t]));spectral=np.r_[x[-1],v[-1]]
    error=float(max(abs(spectral-direct)));assert error<3e-13
    return error

def main(out):
    out.mkdir(parents=True,exist_ok=True);exact=exact_checks()
    t=np.linspace(0,100,4001);short=t<=20
    signs=list(product((-1,1),repeat=4));records=[];summaries=[];worst_cases=[];maxenergy=0.;mineig=1e9
    for epsilon in [.01,.05,.1,.2]:
        worst=None
        for gs in signs:
            for ms in signs:
                g=1+epsilon*np.array(gs);m=1+epsilon*np.array(ms)
                x,_,checks=trajectory(g,m,t)
                l=signal_leakage(x,t);l20=signal_leakage(x[short],t[short])
                row={'epsilon':epsilon,'stiffness_pattern':','.join(map(str,gs)),'inertia_pattern':','.join(map(str,ms)),'leakage_0_20':l20,'leakage_0_100':l,'max_abs_shell_strain':float(np.max(abs(x[:,1:])))}
                records.append(row);maxenergy=max(maxenergy,checks['energy_relative_residual']);mineig=min(mineig,checks['minimum_squared_frequency'])
                if worst is None or l>worst['leakage_0_100']:worst=row.copy()
        worst_cases.append(worst)
        summaries.append({'epsilon':epsilon,'tested_corner_patterns':256,'maximum_leakage_0_100':worst['leakage_0_100'],'maximum_leakage_0_20':max(r['leakage_0_20'] for r in records if r['epsilon']==epsilon),'worst_pattern':worst})
    # Recheck each observed worst corner with finer quadrature; no global optimization claim.
    convergence=[]
    for w in worst_cases:
        eps=w['epsilon'];gs=np.fromstring(w['stiffness_pattern'],sep=',');ms=np.fromstring(w['inertia_pattern'],sep=',');values=[]
        for n in [8001,16001]:
            fine=np.linspace(0,100,n);x,_,_=trajectory(1+eps*gs,1+eps*ms,fine);values.append(signal_leakage(x,fine))
        err=abs(values[1]-values[0]);assert err<5e-6
        convergence.append({'epsilon':eps,'coarse_4001':w['leakage_0_100'],'fine_8001':values[0],'fine_16001':values[1],'fine_difference':err})
    # Deterministic seeded interior points complement the corners; not a confidence interval.
    rng=np.random.default_rng(4307);interior=[]
    for _ in range(256):
        g=1+.05*rng.uniform(-1,1,4);m=1+.05*rng.uniform(-1,1,4);x,_,_=trajectory(g,m,t);interior.append(signal_leakage(x,t))
    sampleg=[1.05,1.05,.95,.95];samplem=[.95,.95,1.05,1.05]
    series=short_series_check(sampleg,samplem)
    # Check the general matched-onsite-ratio eigenvector condition in a numerical unequal-mass case.
    km,mm=matrices(sampleg,samplem,matched_pinning=True);assert max(abs(km@np.ones(5)-mm))<1e-14
    baseline,_,_=trajectory(np.ones(4),np.ones(4),t);baseline_leak=signal_leakage(baseline,t);assert baseline_leak<1e-12
    result={'evidence':['EXACT_CONDITIONAL','NUMERICAL'],'exact':exact,'preparation':'a0=1/10, all shell strains and all velocities0; Kh=Ks=Ih=1,Kt=1/2; spokes g_i and shell inertias m_i varied','numerics':{'dtype':'float64','numpy_version':np.__version__,'time_window':[0,100],'coarse_samples':4001,'fine_samples':[8001,16001],'leakage_definition':'sqrt(integral ||P y||^2 / integral ||y||^2), y_i=V_i/(V0/4)-1; signal amplitude fraction, not energy/information','baseline_leakage':baseline_leak,'maximum_relative_energy_residual':maxenergy,'minimum_observed_squared_frequency':mineig,'second_implementation_short_time_error':series},'corner_scan':summaries,'quadrature_convergence':convergence,'five_percent_seeded_interiors':{'seed':4307,'count':256,'maximum_leakage':max(interior),'median_leakage':float(np.median(interior))},'scope_limits':['Finite tested corners/interiors and declared windows only; no proof these are worst cases over the continuous parameter box or all time.','Positive-energy stability holds generally with positive inertias/spokes and positive pinning, but coherent response need not hold at every drive frequency.','No physical parameters or calibration; same chosen radial ansatz as preceding model.']}
    with (out/'corner-scan.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
