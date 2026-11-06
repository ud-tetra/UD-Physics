"""Prepared-clock transverse variational calculation; own RK4, numpy linear algebra."""
from itertools import combinations
from pathlib import Path
import json, math
import numpy as np

def setup():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)];ix={s:i for i,s in enumerate(cells)};n=15
    d=np.zeros((n,n))
    for s in cells:
        if len(s)>1:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]],ix[s]]=(-1)**k
    J=(d-d.T)/2;v=np.zeros(n);v[1]=1;v[2]=-1;h=J@v
    harmonic=np.zeros(n);harmonic[:4]=.5
    PN=np.eye(n)-np.outer(harmonic,harmonic)-(np.outer(v,v)+np.outer(h,h))/2
    vals,vecs=np.linalg.eigh(PN);N=vecs[:,vals>.5]
    terms=[({1:4},.25),({2:4},.25)]
    for edge in ((0,1),(0,2),(1,3),(2,3)):terms.append(({ix[edge]:4},1.))
    terms.append(({ix[(1,2)]:4},.25))
    for vertex,edge in ((1,(0,1)),(1,(1,3)),(2,(0,2)),(2,(2,3))):terms.append(({vertex:2,ix[edge]:2},.5))
    for vertex in (1,2):terms.append(({vertex:2,ix[(1,2)]:2},.25))
    def hessian(x):
        M=np.zeros((n,n))
        for powers,c in terms:
            for i,pi in powers.items():
                for j,pj in powers.items():
                    mult=pi*(pj-int(i==j))
                    if not mult:continue
                    z=c*mult
                    for k,pk in powers.items():z*=x[k]**(pk-int(k==i)-int(k==j))
                    M[i,j]+=z
        return M
    Bc,Bs=hessian(v),hessian(h);Bcross=hessian(v+h)-Bc-Bs
    W=np.column_stack((v,h))/math.sqrt(2)
    assert N.shape==(15,12)
    assert np.linalg.norm(N.T@W)<1e-14
    assert max(np.linalg.norm(N.T@B@W) for B in (Bc,Bs,Bcross))<1e-13
    jn=N.T@J@N
    return jn,[N.T@B@N for B in (Bc,Bs,Bcross)],N,J,hessian

def monodromy(rho,steps,jn,bb):
    bc,bs,bx=bb
    a0=(1-rho)*jn;ac=rho*jn@bc;ass=rho*jn@bs;ax=rho*jn@bx
    def m(t):
        c,s=math.cos(t),math.sin(t)
        return a0+ac*c*c+ass*s*s+ax*c*s
    dt=math.pi/steps;U=np.eye(12)
    for k in range(steps):
        t=k*dt;m0=m(t);mh=m(t+dt/2);m1=m(t+dt)
        k1=m0@U;k2=mh@(U+dt*k1/2);k3=mh@(U+dt*k2/2);k4=m1@(U+dt*k3)
        U+=dt*(k1+2*k2+2*k3+k4)/6
    return U

def run():
    jn,bb,N,J,hess=setup();reports=[]
    for mu in (0.,1/64,1/16,1/4,1.,2.,4.,8.,16.,64.):
        rho=mu/(2+mu)
        U=monodromy(rho,2048,jn,bb);Uf=monodromy(rho,4096,jn,bb)
        eig,V=np.linalg.eig(Uf)
        reports.append({'mu':mu,'rho':rho,'max_multiplier_modulus':float(np.max(np.abs(eig))),
                        'min_multiplier_modulus':float(np.min(np.abs(eig))),
                        'step_doubling_matrix_error':float(np.linalg.norm(U-Uf,ord=2)),
                        'symplectic_residual':float(np.linalg.norm(Uf.T@jn@Uf-jn,ord=2)),
                        'eigenvector_condition':float(np.linalg.cond(V)),
                        'multipliers':[[float(z.real),float(z.imag)] for z in sorted(eig,key=lambda z:(z.real,z.imag))]})
    return {'evidence':'NUMERICAL','parameter':'mu=lambda I>=0;rho=mu/(2+mu)',
            'equation':'d eta/dtheta=J_N[(1-rho)Id+rho B_N(theta)]eta',
            'coefficient_period':'pi in theta; half of the clock orbit',
            'integrator':'own classical RK4,2048/4096 uniform steps per half orbit;float64',
            'transverse_dimension':12,'numpy_version':np.__version__,'grid':reports,'physical_promotion':0}
if __name__=='__main__':
    r=run();Path(__file__).with_name('transverse_stability_results.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    for x in r['grid']:print(x['mu'],x['max_multiplier_modulus'],x['step_doubling_matrix_error'],x['eigenvector_condition'])
