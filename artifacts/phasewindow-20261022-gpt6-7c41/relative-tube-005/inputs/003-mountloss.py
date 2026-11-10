"""Four central, massless viscous struts per finite housing; all reactions kept."""
from pathlib import Path
import sys
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-tolerances'))
from hardware import Hardware,Damped,readouts


class MountLoss(Hardware):
    def __init__(self,nu=.02,**kwargs):
        super().__init__(**kwargs)
        assert nu>=0
        self.nu=float(nu)
        # Fixed per-trajectory coefficient, based on nominal mean housing inertia.
        self.eta=self.nu*.4*self.beta/self.R2
        anchors=[]
        for i,j in self.edges:
            opposite=[next(k for k in f if k not in (i,j)) for f in self.faces if i in f and j in f]
            assert len(opposite)==2
            anchors.append([i,j]+sorted(opposite))
        self.anchors=np.array(anchors)
        self.housing_index=np.repeat(np.arange(30),4)
        self.anchor_index=self.anchors.ravel()

    def loss_geometry(self,x,H):
        points=x[1:].reshape(13,3)
        d=H[self.housing_index]-points[self.anchor_index]
        ell=np.linalg.norm(d,axis=1)
        if min(ell)<1e-10:raise ValueError('housing strut length-domain singularity')
        return d/ell[:,None],ell

    def housing_loss(self,x,H,v,V):
        n,_=self.loss_geometry(x,H)
        pv=v[1:].reshape(13,3)
        rate=np.einsum('ij,ij->i',n,V[self.housing_index]-pv[self.anchor_index])
        f=(self.eta*rate)[:,None]*n
        gp=np.zeros((13,3));gh=np.zeros((30,3))
        np.add.at(gp,self.anchor_index,-f);np.add.at(gh,self.housing_index,f)
        return np.r_[0.,gp.ravel()],gh,float(self.eta*(rate@rate))

    def ode(self,t,y):
        dy=super().ode(t,y)
        gp,gh,power=self.housing_loss(y[:40],y[190:self.n].reshape(30,3),y[self.n:self.n+40],y[self.n+190:2*self.n].reshape(30,3))
        dy[self.n:self.n+40]-=gp/self.mass
        dy[self.n+190:2*self.n]-=(gh/self.hm[:,None]).ravel()
        dy[-1]+=power
        return dy

    def loss_rows(self):
        x=self.initial[:40];H=self.midpoints(self.ref);n,_=self.loss_geometry(x,H)
        B=np.zeros((120,self.n))
        for row,(h,a,d) in enumerate(zip(self.housing_index,self.anchor_index,n)):
            B[row,1+3*a:4+3*a]=-d;B[row,190+3*h:193+3*h]=d
        return B

    def linear_matrices(self):
        """Mass-normalized equilibrium stiffness and loss, including all coordinates."""
        M=np.r_[self.mass,np.full(150,self.weight*self.mu),np.repeat(self.hm,3)]
        S=np.sqrt(M);J=self.rows(self.initial[:40]);B=self.loss_rows()
        K=np.zeros((self.n,self.n));C=np.zeros_like(K)
        K[:40,:40]=self.rootmass[:,None]*self.H0*self.rootmass[None,:]+self.weight*self.kappa*J.T@J
        K[:40,40:190]=-self.weight*self.kappa*J.T;K[40:190,:40]=K[:40,40:190].T
        K[40:190,40:190]=self.weight*self.kappa*np.eye(150)
        A=np.zeros((90,40))
        for e,(i,j) in enumerate(self.edges):
            A[3*e:3*e+3,1+3*i:4+3*i]=np.eye(3)/2
            A[3*e:3*e+3,1+3*j:4+3*j]=np.eye(3)/2
        kh=np.repeat(self.kh,3)
        K[:40,:40]+=A.T@(kh[:,None]*A)
        K[:40,190:]=-A.T*kh[None,:];K[190:,:40]=K[:40,190:].T;K[190:,190:]=np.diag(kh)
        Br,Be=Damped.strain_rows(self,self.initial[:40])
        C[:40,:40]=self.cs*Br.T@Br+self.ce*Be.T@Be
        C[40:190,40:190]=self.weight*self.gamma*np.eye(150)
        C+=self.eta*B.T@B
        return M,K/S[:,None]/S[None,:],C/S[:,None]/S[None,:]

    def collective_loss(self,b,c):
        """Exact reduced nonlinear Rayleigh matrix for uniform primary/housing scales."""
        A=self.midpoints(self.ref);points=self.ref.copy();points[1:]*=1+b
        x=np.r_[0.,points.ravel()];n,_=self.loss_geometry(x,(1+c)*A)
        rate_map=np.column_stack([-np.einsum('ij,ij->i',n,self.ref[self.anchor_index]),
                                  np.einsum('ij,ij->i',n,A[self.housing_index])])
        C=super().collective_matrices()[2].copy();C[1:,1:]+=self.eta*rate_map.T@rate_map
        return C
