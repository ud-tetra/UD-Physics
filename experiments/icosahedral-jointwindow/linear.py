"""Energy-metric ringdown and analytic-in-phase/strength sufficient inequalities."""
from pathlib import Path
import importlib.util,sys
import numpy as np
from scipy.linalg import eigh,expm,null_space,solve_continuous_lyapunov
from bounds import MountLoss,ROOT,COMPLIANCE
spec=importlib.util.spec_from_file_location('jointwindow_parent',ROOT/'experiments/icosahedral-mountloss/analyze.py')
parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
T=100.

def model(case,nu):return parent.model(case,nu)

def mean_row(m):
    l=np.zeros(280);l[4:40]=(m.ref[1:]/(4*m.R2)).ravel();return l

def baseline_rms(m):
    lam,V=eigh(m.H0);keep=lam>1e-9;assert sum(keep)==34
    w=np.sqrt(lam[keep]);V=V[:,keep]
    l=mean_row(m)[:40]/m.rootmass;initial=np.zeros(40);initial[0]=.1
    a=(l@V)*(V.T@initial)
    integral=(np.sinc((w[:,None]-w[None,:])*T/np.pi)+np.sinc((w[:,None]+w[None,:])*T/np.pi))/2
    return float(np.sqrt(a@integral@a))

def system(m):
    M,K,C=m.linear_matrices();Q,_=parent.reduced_basis(m,M)
    k=Q.T@K@Q;c=Q.T@C@Q;n=len(k)
    Braw=m.loss_rows()/np.sqrt(M)[None,:]
    factor=.4*m.beta/m.R2
    D=factor*(Braw@Q).T@(Braw@Q)
    A=np.block([[np.zeros_like(k),np.eye(n)],[-k,-c]])
    N=np.zeros((12,30))
    for j,(i,h) in enumerate(m.edges):N[i-1,j]=N[h-1,j]=1
    S=np.kron(null_space(N*np.sqrt(m.hm)[None,:]),np.eye(3));U=np.zeros((280,54));U[190:]=S
    raw=np.block([[U/m.omega_h,np.zeros_like(U)],[np.zeros_like(U),U]])
    B=np.vstack([Q.T@raw[:280],Q.T@raw[280:]])
    G=np.block([[k,np.zeros_like(k)],[np.zeros_like(k),np.eye(n)]])
    assert np.max(abs(B.T@G@B-np.eye(108)))<3e-12
    return M,Q,k,D,A,B,raw,G

def integral(A,P,x,final):
    W=solve_continuous_lyapunov(A.T,-P);W=(W+W.T)/2
    residual=float(np.linalg.norm(A.T@W+W@A+P,'fro')/(1+np.linalg.norm(P,'fro')))
    value=float(x@W@x-final@W@final)
    assert residual<2e-7 and value>-1e-8
    return max(0.,value),residual

def evaluate(case,nu,vector=False):
    m=model(case,nu);M,Q,k,D,A,B,raw,G=system(m);n=len(k)
    F=expm(T*A);FB=F@B;gram=FB.T@G@FB;val,vec=eigh((gram+gram.T)/2)
    ratio=float(val[-1]);assert ratio<=1+2e-9
    l=np.r_[mean_row(m)/np.sqrt(M)@Q,np.zeros(n)]
    xp=np.zeros(2*n);q=np.zeros(280);q[0]=.1;xp[:n]=Q.T@(np.sqrt(M)*q)
    final=F@xp
    I,res=integral(A,np.outer(l,l),xp,final)
    Pd=np.zeros_like(A);Pd[n:,n:]=D@D
    Id,resD=integral(A,Pd,xp,final)
    rms=float(np.sqrt(I/T));base=baseline_rms(m);Ep=(1+m.g.sum())*.01/2;Eh=Ep/40000
    phase_bound=float(np.sqrt(2*Eh*float(COMPLIANCE)))
    ld=float(eigh(D,eigvals_only=True)[-1])*(1+1e-9)
    # Explicit numerical cushions; not a verified interval-arithmetic error proof.
    r=np.sqrt(max(0,ratio))+1e-6
    L=float(np.sqrt(float(COMPLIANCE)*T*(Id+1e-6)/2))
    lower=rms-phase_bound-1e-6
    rh=(np.sqrt(.5)-r)/(T*ld)
    rb=(lower-.8*base)/L
    radius=float(min(rh,rb))
    result={'id':case['id'],'nu':float(nu),'beta':case['beta'],'cf':case['cf'],
            'worst_housing_energy_fraction':ratio,'linear_pulse_rms':rms,'original_linear_rms':base,
            'all_phase_readout_rms_bound':phase_bound,'all_phase_linear_retention_lower':lower/base,
            'strength_generator_norm':ld,'trajectory_sensitivity_integral':Id,'breathing_rms_lipschitz_bound':L,
            'ringdown_radius':float(rh),'breathing_radius':float(rb),'joint_radius':radius,
            'lyapunov_relative_residual':res,'sensitivity_lyapunov_relative_residual':resD,
            'passes_node':bool(ratio<=.5 and lower/base>=.8),'initial_pulse_energy':float(Ep),'housing_energy':float(Eh)}
    physical=None
    if vector:
        physical=raw@vec[:,-1]/np.r_[np.sqrt(M),np.sqrt(M)]
        assert max(abs(physical[:190]))==0 and max(abs(physical[280:470]))==0
        physical=np.r_[physical[190:280],physical[470:560]]
    return result,physical
