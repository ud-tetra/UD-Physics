"""Ordinary axial dashpots; all point forces are internal and central."""
from pathlib import Path
import sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'icosahedral-free3d'))
from model import Model,ico

class Damped(Model):
    def __init__(self,cs=0.,ce=0.,**kwargs):
        super().__init__(**kwargs)
        assert cs>=0 and ce>=0
        self.cs=float(cs);self.ce=float(ce)

    def strain_rows(self,x):
        p=x[1:].reshape(13,3);rad=p[1:]-p[0];rho=np.linalg.norm(rad,axis=1)
        B=np.zeros((12,40));D=np.zeros((30,40))
        for z,n in enumerate(rad/rho[:,None]/self.R):
            B[z,4+3*z:7+3*z]=n;B[z,1:4]=-n
        delta=p[self.edge[:,0]]-p[self.edge[:,1]];ell=np.linalg.norm(delta,axis=1)
        for z,((i,j),n) in enumerate(zip(self.edge,delta/ell[:,None])):
            D[z,1+3*i:4+3*i]=n;D[z,1+3*j:4+3*j]=-n
        return B,D

    def damping_force(self,x,v):
        p=x[1:].reshape(13,3);pv=v[1:].reshape(13,3)
        r=p[1:]-p[0];n=r/np.linalg.norm(r,axis=1)[:,None]
        sd=np.einsum('ij,ij->i',n,pv[1:]-pv[0])/self.R
        delta=p[self.edge[:,0]]-p[self.edge[:,1]];en=delta/np.linalg.norm(delta,axis=1)[:,None]
        ed=np.einsum('ij,ij->i',en,pv[self.edge[:,0]]-pv[self.edge[:,1]])
        f=np.zeros((13,3));rf=(self.cs*sd/self.R)[:,None]*n
        f[1:]+=rf;f[0]-=rf.sum(axis=0)
        ef=(self.ce*ed)[:,None]*en
        np.add.at(f,self.edge[:,0],ef);np.add.at(f,self.edge[:,1],-ef)
        return np.r_[0.,f.ravel()],float(self.cs*(sd@sd)+self.ce*(ed@ed))

    def ode_loss(self,t,y):
        v=y[40:80];_,grad=self.energy_force(y[:40]);f,power=self.damping_force(y[:40],v)
        return np.r_[v,-(grad+f)/self.mass,power]

    def collective_matrix(self):
        d=self.cs+2.5*self.ce
        return np.array([[0,0,1,0],[0,0,0,1],[-13,12,0,0],[1,-3,0,-d]],float)

    def damped_collective(self,t,A0=.1):
        A=self.collective_matrix();w,V=np.linalg.eig(A);z=np.linalg.solve(V,np.array([A0,0,0,0.]))
        answer=(V@((np.exp(w[:,None]*np.asarray(t)[None,:]))*z[:,None])).real
        return answer
