"""Free 3D centre and shell, plus one passive internal preferred-radius coordinate."""
from pathlib import Path
import importlib.util
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('free3d_ico',ROOT/'experiments/icosahedral-cone/analyze.py')
ico=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ico;spec.loader.exec_module(ico)


class Model:
    def __init__(self,g=None,m=None,k=None):
        self.vertices,self.edges,self.faces,self.cells,self.simplices,self.B=ico.construction()
        self.ref=np.array([[float(v) for v in x] for x in self.vertices])
        self.R2=float(ico.dot(self.vertices[1],self.vertices[1]));self.R=np.sqrt(self.R2)
        self.edge=np.array(self.edges);self.face=np.array(self.faces)
        self.sign=np.array([ico.det(*[self.vertices[i] for i in f]).sign() for f in self.faces])
        self.vcell=(3+np.sqrt(5))/48
        self.g=np.ones(12) if g is None else np.array(g)
        self.m=np.ones(13) if m is None else np.array(m)
        self.k=np.full(30,.4) if k is None else np.array(k)
        assert min(self.g)>0 and min(self.m)>0 and min(self.k)>0
        self.mass=np.r_[1.,np.repeat(self.m/self.R2,3)]
        self.rootmass=np.sqrt(self.mass)
        self.initial=np.r_[.1,self.ref.ravel(),np.zeros(40)]
        self.H0,self.Tr,self.Te=self.hessian_parts()

    def energy_force(self,x):
        alpha=x[0];points=x[1:].reshape(13,3)
        radial=points[1:]-points[0];rho=np.linalg.norm(radial,axis=1)
        n=radial/rho[:,None];s=rho/self.R-1
        delta=points[self.edge[:,0]]-points[self.edge[:,1]]
        ell=np.linalg.norm(delta,axis=1);edge_n=delta/ell[:,None];e=ell-1
        if min(rho)<1e-10 or min(ell)<1e-10:raise ValueError('length-domain singularity')
        potential=(alpha*alpha+np.sum(s*s)+np.sum(self.g*(s-alpha)**2)+np.sum(self.k*e*e))/2
        grad=np.zeros((13,3))
        radial_grad=((s+self.g*(s-alpha))/self.R)[:,None]*n
        grad[1:]+=radial_grad;grad[0]-=radial_grad.sum(axis=0)
        edge_grad=(self.k*e)[:,None]*edge_n
        np.add.at(grad,self.edge[:,0],edge_grad);np.add.at(grad,self.edge[:,1],-edge_grad)
        return potential,np.r_[alpha+np.sum(self.g*(alpha-s)),grad.ravel()]

    def ode(self,time,state):
        _,force=self.energy_force(state[:40])
        return np.r_[state[40:],-force/self.mass]

    def hessian_parts(self):
        K=np.zeros((40,40));Tr=np.zeros_like(K);Te=np.zeros_like(K)
        K[0,0]=1+self.g.sum()
        def add_pair(matrix,i,j,block):
            ix=np.arange(1+3*i,4+3*i);jx=np.arange(1+3*j,4+3*j)
            matrix[np.ix_(ix,ix)]+=block;matrix[np.ix_(jx,jx)]+=block
            matrix[np.ix_(ix,jx)]-=block;matrix[np.ix_(jx,ix)]-=block
        for i in range(1,13):
            n=self.ref[i]/self.R;nn=np.outer(n,n);ix=np.arange(1+3*i,4+3*i);cx=np.arange(1,4)
            add_pair(K,i,0,(1+self.g[i-1])*nn/self.R2)
            K[0,ix]-=self.g[i-1]*n/self.R;K[ix,0]-=self.g[i-1]*n/self.R
            K[0,cx]+=self.g[i-1]*n/self.R;K[cx,0]+=self.g[i-1]*n/self.R
            add_pair(Tr,i,0,(np.eye(3)-nn)/self.R2)
        for (i,j),k in zip(self.edge,self.k):
            n=self.ref[i]-self.ref[j];nn=np.outer(n,n)
            add_pair(K,i,j,k*nn)
            add_pair(Te,i,j,k*(np.eye(3)-nn))
        return tuple(matrix/self.rootmass[:,None]/self.rootmass[None,:] for matrix in [K,Tr,Te])

    def collective(self,t,A0=.1):
        t=np.asarray(t);root=np.sqrt(37);lo=8-root;hi=8+root
        b=A0*(np.cos(np.sqrt(lo)*t)-np.cos(np.sqrt(hi)*t))/(2*root)
        alpha=A0*((3-lo)*np.cos(np.sqrt(lo)*t)+(hi-3)*np.cos(np.sqrt(hi)*t))/(2*root)
        return alpha,b

    def transverse_basis(self):
        # Remove actuator/uniform radial coordinates and all six rigid displacements.
        columns=[np.eye(40)[:,0]]
        radial=np.r_[0.,self.ref.ravel()];columns.append(radial)
        for axis in np.eye(3):columns.append(np.r_[0.,np.tile(axis,13)])
        for axis in np.eye(3):columns.append(np.r_[0.,np.cross(np.tile(axis,(13,1)),self.ref).ravel()])
        D=np.column_stack(columns)*self.rootmass[:,None]
        q,_=np.linalg.qr(D,mode='complete');return q[:,8:],q[:,:8]

    def volumes(self,states):
        points=states[:,1:40].reshape(-1,13,3);relative=points[:,self.face]-points[:,None,0,None,:]
        determinants=np.einsum('tfi,tfi->tf',relative[:,:,0],np.cross(relative[:,:,1],relative[:,:,2]))
        return determinants*self.sign[None,:]/(6*self.vcell)

    def geometry_checks(self,states):
        points=states[::10,1:40].reshape(-1,13,3)
        fa=points[:,self.face[:,0]];fb=points[:,self.face[:,1]];fc=points[:,self.face[:,2]]
        normal=np.cross(fb-fa,fc-fa)*self.sign[None,:,None]
        separation=points[:,None,1:,:]-fa[:,:,None,:]
        violation=float(np.max(np.einsum('tfi,tfji->tfj',normal,separation)))
        return {'minimum_oriented_cell_volume_ratio':float(self.volumes(states).min()),
                'maximum_support_halfspace_violation_sampled':violation}


def exact_rigidity(model):
    Q=ico.Q5;zero=Q(0);one=Q(1)
    def row():return [zero]*40
    rows=[];r=row();r[0]=one;rows.append(r)
    for i in range(1,13):
        r=row()
        for j in range(3):r[1+3*i+j]=model.vertices[i][j];r[1+j]=-model.vertices[i][j]
        rows.append(r)
    edge_rows=[]
    for i,j in model.edges:
        r=row();delta=ico.sub(model.vertices[i],model.vertices[j])
        for k in range(3):r[1+3*i+k]=delta[k];r[1+3*j+k]=-delta[k]
        edge_rows.append(r)
    def rank(matrix):
        a=[r.copy() for r in matrix];pivot=0
        for j in range(len(a[0])):
            available=next((i for i in range(pivot,len(a)) if a[i][j]!=zero),None)
            if available is None:continue
            a[pivot],a[available]=a[available],a[pivot]
            v=a[pivot][j];a[pivot]=[x/v for x in a[pivot]]
            for i in range(pivot+1,len(a)):
                v=a[i][j]
                if v!=zero:a[i]=[x-v*y for x,y in zip(a[i],a[pivot])]
            pivot+=1
            if pivot==len(a):break
        return pivot
    edge_rank=rank(edge_rows);full_rank=rank(rows+edge_rows)
    null=[]
    for axis in range(3):
        r=row()
        for i in range(13):r[1+3*i+axis]=one
        null.append(r)
    for axis in range(3):
        unit=[Q(int(i==axis)) for i in range(3)];r=row()
        for i,v in enumerate(model.vertices):
            rotation=ico.cross(unit,v)
            for j in range(3):r[1+3*i+j]=rotation[j]
        null.append(r)
    for a in rows+edge_rows:
        assert all(sum(x*y for x,y in zip(a,z))==zero for z in null)
    assert edge_rank==30 and full_rank==34 and rank(null)==6
    return {'coefficient_field':'Q(sqrt(5))','edge_rigidity_rank':edge_rank,
            'full_constraint_rank':full_rank,'configuration_dimension':40,
            'exact_kernel_dimension':6,'kernel':'three global translations plus three global rotations'}
