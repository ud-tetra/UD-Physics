"""Exact first derivative of the frozen UD 3D mechanical surrogate, sparse assembled.
Adapted from integrated experiments/icosahedral-pulsetube/jacobian.py in
ud-tetra/UD-Physics, with index conventions of checkpoint-014 standalone model.
Compared against independent column JVP and finite differences before use.
"""
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, diags, bmat, eye
from nonaffine_audit import R, R2, I as EDGE_I, J as EDGE_J, HIDX, AIDX, pairs

class SparseJacobian:
    def __init__(self,m):
        self.m=m; self.n=m.n; self.M=m.M
        self.invM=diags(1/self.M)
        # 13 primary and 30 housing point masses; index 0 means primary centre
        self.spatial=np.r_[np.arange(1,40),np.arange(190,280)].reshape(43,3)
        self.pairs=np.asarray([(i,0) for i in range(1,13)] + list(zip(EDGE_I,EDGE_J)) + [(13+h,a) for h,a in zip(HIDX,AIDX)])
        self.i=self.pairs[:,0];self.j=self.pairs[:,1]
        self.G=csr_matrix(m.G)
        self.scale=np.r_[np.full(12,1/R),np.ones(30)]
        self.damping=np.r_[np.full(12,m.cs/R2),np.full(30,m.ce),np.full(120,m.eta)]
        self.longitudinal=np.r_[1+m.g,m.k]
        row=[];col=[];sign=[]
        for si,sj,sgn in [(self.i,self.i,1),(self.j,self.j,1),(self.i,self.j,-1),(self.j,self.i,-1)]:
            row.append(np.repeat(self.spatial[si],3,axis=1).ravel())
            col.append(np.tile(self.spatial[sj],(1,3)).ravel())
            sign.append(sgn)
        self.block_rows=np.concatenate(row);self.block_cols=np.concatenate(col);self.block_sign=sign
        rr=[];cc=[];vv=[]
        for h,(i,j) in enumerate(zip(EDGE_I,EDGE_J)):
            for a in range(3):
                rr.extend([3*h+a]*3); cc.extend([190+3*h+a,1+3*i+a,1+3*j+a]);vv.extend([1.,-.5,-.5])
        A=coo_matrix((vv,(rr,cc)),shape=(90,self.n)).tocsr()
        self.Kmount=A.T@diags(np.repeat(m.kh,3))@A
        self.Caux=diags(np.r_[np.zeros(40),np.full(150,.1*5),np.zeros(90)])
        self.Kaux=diags(np.r_[np.zeros(40),np.full(150,.1*50),np.zeros(90)])
        self.identity=eye(self.n,format='csr');self.zero=csr_matrix((self.n,self.n))
    def pair_matrix(self,blocks):
        values=np.concatenate([s*blocks.reshape(-1) for s in self.block_sign]);return coo_matrix((values,(self.block_rows,self.block_cols)),shape=(self.n,self.n)).tocsr()
    def matrices(self,y):
        """Return K=Uqq+∂q[D(q)v], C=D(q)."""
        m=self.m;q=y[:self.n];v=y[self.n:2*self.n]
        P=q[self.spatial];V=v[self.spatial]
        d=P[self.i]-P[self.j];ell=np.linalg.norm(d,axis=1)
        if np.min(ell)<1.e-9:raise ValueError('collapsed strut or primary')
        n=d/ell[:,None];w=V[self.i]-V[self.j]
        rate=np.einsum('ij,ij->i',n,w)
        nn=n[:,:,None]*n[:,None,:];trans=np.eye(3)[None,:,:]-nn
        dampq=(self.damping/ell)[:,None,None]*(rate[:,None,None]*np.eye(3)+n[:,:,None]*w[:,None,:]-2*rate[:,None,None]*nn)
        C=self.pair_matrix(self.damping[:,None,None]*nn)+self.Caux
        si=self.spatial[self.i[:42]];sj=self.spatial[self.j[:42]]
        rr=np.repeat(np.arange(42),3)
        J=coo_matrix((np.r_[(self.scale[:,None]*n[:42]).ravel(),(-self.scale[:,None]*n[:42]).ravel()],(np.r_[rr,rr],np.r_[si.ravel(),sj.ravel()])),shape=(42,self.n)).tocsr()
        strain=ell[:42]*self.scale-1
        error=m.G@strain-q[40:190]
        tension=np.r_[strain[:12]+m.g*(strain[:12]-q[0]),m.k*strain[12:]]+m.G.T@(5.*error)
        geom=np.zeros_like(dampq);geom[:42]=(tension*self.scale/ell[:42])[:,None,None]*trans[:42]
        JP=self.G@J
        K=J.T@diags(self.longitudinal)@J+5.*(JP.T@JP)
        ar=[];ac=[];av=[]
        for h in range(12):
            f=-m.g[h]*self.scale[h]*n[h]
            for k in range(3):
                for point,sgn in [(h+1,1),(0,-1)]:
                    ix=1+3*point+k;ar.extend([0,ix]);ac.extend([ix,0]);av.extend([sgn*f[k]]*2)
        ar.append(0);ac.append(0);av.append(1+m.g.sum())
        cross=JP.tocoo()
        ar.extend((40+cross.row).tolist());ac.extend(cross.col.tolist());av.extend((-5.*cross.data).tolist())
        ar.extend(cross.col.tolist());ac.extend((40+cross.row).tolist());av.extend((-5.*cross.data).tolist())
        K=(K+coo_matrix((av,(ar,ac)),shape=(self.n,self.n)).tocsr()+self.Kaux+self.Kmount+self.pair_matrix(geom+dampq)).tocsr()
        return K,C.tocsr()
    def apply(self,y,W):
        K,C=self.matrices(y);n=self.n
        return np.vstack([W[n:],-(K@W[:n]+C@W[n:])/self.M[:,None]])
    def adjoint(self,y,Lambda):
        K,C=self.matrices(y);n=self.n
        # ∂_t Lambda=-Jac(y)^T Lambda
        top=K.T@(Lambda[n:]/self.M[:,None]); bot=-Lambda[:n]+C.T@(Lambda[n:]/self.M[:,None])
        return np.vstack([top,bot])
