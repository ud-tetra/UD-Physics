"""Analytic full mechanical Jacobian of the unchanged MountLoss ODE.

Heat is excluded from the mechanical560-state Jacobian. All43 spatial points
and all reactions are retained; no rigid quotient is used.
"""
from pathlib import Path
import sys
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,diags,bmat,eye
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/icosahedral-mountloss'))
from mountloss import MountLoss

class Linearization:
    def __init__(self,m):
        self.m=m;self.n=m.n
        self.M=np.r_[m.mass,np.full(150,m.weight*m.mu),np.repeat(m.hm,3)]
        self.invM=diags(1/self.M)
        self.spatial=np.r_[np.arange(1,40),np.arange(190,280)].reshape(43,3)
        self.pairs=np.array([(i,0) for i in range(1,13)]+list(m.edges)+[(13+h,a) for h,a in zip(m.housing_index,m.anchor_index)])
        self.i=self.pairs[:,0];self.j=self.pairs[:,1]
        self.G=csr_matrix(m.G)
        self.scale=np.r_[np.full(12,1/m.R),np.ones(30)]
        self.damping=np.r_[np.full(12,m.cs/m.R2),np.full(30,m.ce),np.full(120,m.eta)]
        self.longitudinal=np.r_[1+m.g,m.k]
        # Fixed triplets for sums of pair-local3x3 blocks.
        rows=[];cols=[];sign=[]
        for si,sj,sgn in [(self.i,self.i,1),(self.j,self.j,1),(self.i,self.j,-1),(self.j,self.i,-1)]:
            rows.append(np.repeat(self.spatial[si],3,axis=1).ravel())
            cols.append(np.tile(self.spatial[sj],(1,3)).ravel());sign.append(sgn)
        self.block_rows=np.concatenate(rows);self.block_cols=np.concatenate(cols);self.block_sign=sign
        # Constant mount Hessian: H_e-(X_i+X_j)/2, repeated over3 axes.
        rr=[];cc=[];vv=[]
        for h,(i,j) in enumerate(m.edges):
            for a in range(3):
                rr.extend([3*h+a]*3);cc.extend([190+3*h+a,1+3*i+a,1+3*j+a]);vv.extend([1.,-.5,-.5])
        A=coo_matrix((vv,(rr,cc)),shape=(90,self.n)).tocsr()
        self.Kmount=A.T@diags(np.repeat(m.kh,3))@A
        self.Caux=diags(np.r_[np.zeros(40),np.full(150,m.weight*m.gamma),np.zeros(90)])
        self.Kaux=diags(np.r_[np.zeros(40),np.full(150,m.weight*m.kappa),np.zeros(90)])
        self.identity=eye(self.n,format='csr');self.zero=csr_matrix((self.n,self.n))

    def pair_matrix(self,blocks):
        v=blocks.reshape(-1)
        values=np.concatenate([s*v for s in self.block_sign])
        return coo_matrix((values,(self.block_rows,self.block_cols)),shape=(self.n,self.n)).tocsr()

    def matrices(self,y):
        """Returns K=U_qq+partial_q(D(q)v), C=D(q), physical coordinates."""
        m=self.m;q=y[:self.n];v=y[self.n:2*self.n]
        P=q[self.spatial];V=v[self.spatial]
        d=P[self.i]-P[self.j];ell=np.linalg.norm(d,axis=1);assert ell.min()>1e-10
        n=d/ell[:,None];w=V[self.i]-V[self.j];rate=np.einsum('ij,ij->i',n,w)
        nn=n[:,:,None]*n[:,None,:];trans=np.eye(3)[None,:,:]-nn
        # Exact derivative of c*n*(n.v): c/ell[rate I+n v^T-2rate nn^T].
        dampq=(self.damping/ell)[:,None,None]*(rate[:,None,None]*np.eye(3)+n[:,:,None]*w[:,None,:]-2*rate[:,None,None]*nn)
        C=self.pair_matrix(self.damping[:,None,None]*nn)+self.Caux
        # 42 strain rows in the entire280-coordinate space.
        si=self.spatial[self.i[:42]];sj=self.spatial[self.j[:42]]
        r=np.repeat(np.arange(42),3)
        J=coo_matrix((np.r_[(self.scale[:,None]*n[:42]).ravel(),(-self.scale[:,None]*n[:42]).ravel()],
                      (np.r_[r,r],np.r_[si.ravel(),sj.ravel()])),shape=(42,self.n)).tocsr()
        strain=ell[:42]*self.scale-1
        error=m.G@strain-q[40:190]
        tension=np.r_[strain[:12]+m.g*(strain[:12]-q[0]),m.k*strain[12:]]+m.G.T@(m.weight*m.kappa*error)
        geom=np.zeros_like(dampq);geom[:42]=(tension*self.scale/ell[:42])[:,None,None]*trans[:42]
        JP=self.G@J
        K=J.T@diags(self.longitudinal)@J+m.weight*m.kappa*(JP.T@JP)
        # Device/primary reciprocal cross blocks and alpha/spoke cross terms.
        ar=[];ac=[];av=[]
        for h in range(12):
            f=-m.g[h]*self.scale[h]*n[h]
            for k in range(3):
                for point,sgn in [(h+1,1),(0,-1)]:
                    ix=1+3*point+k;ar.extend([0,ix]);ac.extend([ix,0]);av.extend([sgn*f[k]]*2)
        ar.append(0);ac.append(0);av.append(1+m.g.sum())
        cross=JP.tocoo();ar.extend((40+cross.row).tolist());ac.extend(cross.col.tolist());av.extend((-m.weight*m.kappa*cross.data).tolist())
        ar.extend(cross.col.tolist());ac.extend((40+cross.row).tolist());av.extend((-m.weight*m.kappa*cross.data).tolist())
        K=K+coo_matrix((av,(ar,ac)),shape=(self.n,self.n)).tocsr()+self.Kaux+self.Kmount+self.pair_matrix(geom+dampq)
        return K.tocsr(),C.tocsr()

    def jacobian(self,y):
        K,C=self.matrices(y)
        return bmat([[self.zero,self.identity],[-self.invM@K,-self.invM@C]],format='csr')

    def apply(self,y,W):
        K,C=self.matrices(y)
        return np.vstack([W[self.n:],-(K@W[:self.n]+C@W[self.n:])/self.M[:,None]])

    def injection(self):
        B=np.zeros((2*self.n,180));k=np.arange(90)
        B[190+k,k]=1/(self.m.omega_h*np.sqrt(np.repeat(self.m.hm,3)))
        B[self.n+190+k,90+k]=1/np.sqrt(np.repeat(self.m.hm,3))
        return B

def model(case,nu):
    return MountLoss(nu=nu,beta=case['beta'],omega_h=case['omega_h'],cf=case['cf'],
                     housing_weights=case['housing_weights'],ratio_error=case['ratio_error'],**case['primary'])
