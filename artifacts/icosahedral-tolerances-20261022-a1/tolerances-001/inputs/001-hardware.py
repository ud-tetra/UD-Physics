"""Finite midpoint-mounted housing model; all primary/housing reactions retained."""
from pathlib import Path
import importlib.util,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-multiport'))
from network import Network
spec=importlib.util.spec_from_file_location('tolerance_readouts',ROOT/'experiments/icosahedral-damping/analyze.py')
sys.path.insert(0,str(ROOT/'experiments/icosahedral-damping'))
readouts=importlib.util.module_from_spec(spec);spec.loader.exec_module(readouts)
from damping import Damped

class Hardware(Network):
    def __init__(self,beta=.05,omega_h=10.,cf=.001,housing_weights=None,**kwargs):
        super().__init__(mu=2.,kappa=50.,gamma=5.,**kwargs)
        assert beta>0 and omega_h>0 and cf>=0
        self.beta=float(beta);self.omega_h=float(omega_h);self.cf=float(cf)
        self.hw=np.ones(30) if housing_weights is None else np.asarray(housing_weights)
        assert self.hw.shape==(30,) and min(self.hw)>0 and abs(self.hw.mean()-1)<1e-12
        self.hm=.4*self.beta*self.hw/self.R2;self.kh=self.hm*self.omega_h**2
        self.cs=self.cf/2;self.ce=4*self.cf/5
        self.n=280;self.nhousing=30

    def initial_augmented(self,A0=.1):
        y=np.zeros(2*self.n+1);y[:40]=self.initial[:40];y[0]=A0
        y[190:self.n]=self.midpoints(self.ref).ravel();return y

    def midpoints(self,points):return (points[self.edge[:,0]]+points[self.edge[:,1]])/2

    def mount_force(self,x,H):
        points=x[1:].reshape(13,3);delta=H-self.midpoints(points);gh=self.kh[:,None]*delta
        gp=np.zeros((13,3));np.add.at(gp,self.edge[:,0],-gh/2);np.add.at(gp,self.edge[:,1],-gh/2)
        U=float(np.sum(self.kh[:,None]*delta*delta)/2)
        return np.r_[0.,gp.ravel()],gh,U

    def ode(self,t,y):
        x=y[:40];z=y[40:190];H=y[190:self.n].reshape(30,3)
        v=y[self.n:self.n+40];w=y[self.n+40:self.n+190];V=y[self.n+190:2*self.n].reshape(30,3)
        _,g0=self.energy_force(x);gp,error,_=self.port_force(x,z);gm,gh,_=self.mount_force(x,H)
        friction,power=Damped.damping_force(self,x,v)
        return np.r_[v,w,V.ravel(),-(g0+gp+gm+friction)/self.mass,
                     (self.kappa*error-self.gamma*w)/self.mu,(-gh/self.hm[:,None]).ravel(),
                     self.weight*self.gamma*(w@w)+power]

    def energy(self,y):
        x=y[:40];z=y[40:190];H=y[190:self.n].reshape(30,3)
        v=y[self.n:self.n+40];w=y[self.n+40:self.n+190];V=y[self.n+190:2*self.n].reshape(30,3)
        return self.energy_force(x)[0]+self.port_force(x,z)[2]+self.mount_force(x,H)[2]+np.sum(self.mass*v*v)/2+self.weight*self.mu*(w@w)/2+np.sum(self.hm[:,None]*V*V)/2

    def collective_matrices(self):
        rho=float(np.sum(self.midpoints(self.ref)**2)/(30*self.R2));m=12*self.beta*rho;k=m*self.omega_h**2
        M=np.diag([1.,12.,m]);K=np.array([[13.,-12.,0.],[-12.,36.+k,-k],[0.,-k,k]])
        C=np.diag([0.,30*self.cf,0.]);return M,K,C,rho
