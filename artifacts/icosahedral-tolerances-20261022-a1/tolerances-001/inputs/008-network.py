"""Passive reciprocal difference transmissions with finite auxiliary dynamics."""
from pathlib import Path
from itertools import combinations
import sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'icosahedral-free3d'))
from model import Model,ico

class Network(Model):
    def __init__(self,mu=.02,kappa=.5,gamma=.1,ratio_error=None,**kwargs):
        super().__init__(**kwargs)
        assert mu>0 and kappa>0 and gamma>0
        self.mu=float(mu);self.kappa=float(kappa);self.gamma=float(gamma);self.weight=.1
        self.radial_pairs=np.array([(i-1,j-1) for i,j in self.edge])
        self.edge_pairs=np.array([(i,j) for i,j in combinations(range(30),2) if set(self.edges[i])&set(self.edges[j])])
        self.pairs=np.vstack([self.radial_pairs,self.edge_pairs+12]);self.naux=len(self.pairs);assert self.naux==150
        self.gain=np.ones(self.naux) if ratio_error is None else 1+np.asarray(ratio_error)
        assert self.gain.shape==(self.naux,)
        self.G=np.zeros((self.naux,42));self.G[np.arange(self.naux),self.pairs[:,0]]=1
        self.G[np.arange(self.naux),self.pairs[:,1]]=-self.gain
        self.n=40+self.naux

    def strain_geometry(self,x):
        p=x[1:].reshape(13,3);rad=p[1:]-p[0];rho=np.linalg.norm(rad,axis=1)
        delta=p[self.edge[:,0]]-p[self.edge[:,1]];ell=np.linalg.norm(delta,axis=1)
        assert min(rho)>1e-10 and min(ell)>1e-10
        return np.r_[rho/self.R-1,ell-1],rad/rho[:,None],delta/ell[:,None]

    def rows(self,x):
        _,rn,en=self.strain_geometry(x);J=np.zeros((42,40))
        for i,n in enumerate(rn):J[i,4+3*i:7+3*i]=n/self.R;J[i,1:4]=-n/self.R
        for z,((i,j),n) in enumerate(zip(self.edge,en)):
            J[12+z,1+3*i:4+3*i]=n;J[12+z,1+3*j:4+3*j]=-n
        return self.G@J

    def port_force(self,x,z):
        y,rn,en=self.strain_geometry(x)
        d=y[self.pairs[:,0]]-self.gain*y[self.pairs[:,1]]
        error=d-z;f=self.weight*self.kappa*error
        tension=np.zeros(42)
        np.add.at(tension,self.pairs[:,0],f);np.add.at(tension,self.pairs[:,1],-self.gain*f)
        pgrad=np.zeros((13,3));rf=(tension[:12]/self.R)[:,None]*rn
        pgrad[1:]+=rf;pgrad[0]-=rf.sum(axis=0)
        ef=tension[12:,None]*en
        np.add.at(pgrad,self.edge[:,0],ef);np.add.at(pgrad,self.edge[:,1],-ef)
        return np.r_[0.,pgrad.ravel()],error,float(self.weight*self.kappa*(error@error)/2)

    def initial_augmented(self,A0=.1):
        y=np.zeros(2*self.n+1);y[:40]=self.initial[:40];y[0]=A0;return y

    def ode(self,t,y):
        x=y[:40];z=y[40:self.n];v=y[self.n:self.n+40];w=y[self.n+40:2*self.n]
        _,grad=self.energy_force(x);force,error,_=self.port_force(x,z)
        return np.r_[v,w,-(grad+force)/self.mass,(self.kappa*error-self.gamma*w)/self.mu,self.weight*self.gamma*(w@w)]

    def energy(self,y):
        x=y[:40];z=y[40:self.n];v=y[self.n:self.n+40];w=y[self.n+40:2*self.n]
        return self.energy_force(x)[0]+self.port_force(x,z)[2]+np.sum(self.mass*v*v)/2+self.weight*self.mu*(w@w)/2

    def normal_matrices(self):
        Q,_=self.transverse_basis();J=self.rows(self.initial[:40])/self.rootmass[None,:];D=J@Q
        h=Q.T@self.H0@Q;aux=self.naux
        K=np.block([[h+self.weight*self.kappa*D.T@D,-self.kappa*np.sqrt(self.weight/self.mu)*D.T],
                    [-self.kappa*np.sqrt(self.weight/self.mu)*D,(self.kappa/self.mu)*np.eye(aux)]])
        C=np.diag(np.r_[np.zeros(32),np.full(aux,self.gamma/self.mu)])
        return K,C,D
