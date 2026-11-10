#!/usr/bin/env python3
"""A5 multiplicity-space reduction of the complete 560-phase moving adjoint.
Local exploratory numerical verification; no interval claim.
"""
import sys, numpy as np, time, argparse, json
from pathlib import Path
from scipy.linalg import eigh
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from six_moving_adjoint import six_seeds, baseline, Mechanical, SparseJacobian, injection, solve_target, group_matrix
from verify_group import build_actions


def transform_q_matrix(a):
    T=np.zeros((280,280));T[0,0]=1
    rt=a['rt'];block=rt.T
    for old,new in enumerate(a['node']):
        T[1+3*int(new):1+3*int(new)+3,1+3*old:1+3*old+3]=block
    for old,new in enumerate(a['auxidx']):T[40+int(new),40+old]=int(a['auxsign'][old])
    for old,new in enumerate(a['edge']):
        T[190+3*int(new):190+3*int(new)+3,190+3*old:190+3*old+3]=block
    return T

def construct():
    actions=build_actions();seeds=six_seeds()
    groups=[('3',3,0,[0]),('3prime',3,1,[1]),('4',4,2,[2,3]),('5',5,4,[4,5])]
    base=[]
    for key,d,seedidx,ind in groups:
        s=seeds[:,seedidx];P=np.zeros((280,280)); Pout=np.zeros((36,36))
        for a in actions:
            U=group_matrix(a);t=transform_q_matrix(a)
            coeff=s@(U@s)
            P+=(d/60)*coeff*t
            Pout+=(d/60)*coeff*U
        herm=np.max(abs(P-P.T));projection=np.max(abs(P@P-P));eigs,Q=np.linalg.eigh((P+P.T)/2)
        k=np.sum(eigs>.5);basis=Q[:,eigs>.5]
        exact_seeds=[]
        for n in ind:
            z=np.zeros(280);z[4:40]=seeds[:,n]
            exact_seeds.append(float(np.linalg.norm(z-basis@(basis.T@z))))
        base.append(dict(key=key,d=d,basis=basis,seed_indices=ind,herm=herm,projection=projection,rank=int(k),eigen_mid=float(np.sort(eigs)[-k]),seed_errors=exact_seeds))
        print('SECTOR',key,'d',d,'rank',k,'idempotence',projection,'seederrors',exact_seeds,flush=True)
    return base,seeds

def checks(m,sp,ref,base):
    rng=np.random.default_rng(24)
    errors={}
    for u in [0.,1.,4.,30.,100.]:
        K,C=sp.matrices(ref(u))
        for v in base:
            Q=v['basis'];P=Q@Q.T
            q=rng.normal(size=(280,2))
            rK=(np.eye(280)-P)@(K@Q)
            rC=(np.eye(280)-P)@(C@Q)
            errors[v['key']+f'_{u}']=max(np.linalg.norm(rK,ord=np.inf),np.linalg.norm(rC,ord=np.inf))
    print('MAXINVARIANCE',max(errors.values()),flush=True)
    return errors

def solve_reduced(sp,ref,B,basis,seed_columns,tstar,rtol=1e-9,atol=1e-11):
    Q=basis; r=Q.shape[1];nseed=seed_columns.shape[1]
    qi=np.zeros((280,nseed));qi[4:40]=seed_columns
    init=np.zeros((2*r,nseed));init[:r]=Q.T@qi
    mu=sp.M; invM=1/mu
    start=time.perf_counter();calls=[0]
    def rhs(t,arr):
        L=arr.reshape(2*r,nseed)
        K,C=sp.matrices(ref(t))
        # Unbalanced mass: system A=-M^-1K; project after applying
        Aq=Q.T@(K.T@(invM[:,None]*Q));Ac=Q.T@(C.T@(invM[:,None]*Q))
        calls[0]+=1
        return np.vstack([Aq@L[r:],-L[:r]+Ac@L[r:]]).ravel()
    sol=solve_ivp(rhs,(tstar,0),init.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not sol.success:raise RuntimeError(sol.message)
    L=sol.y[:,-1].reshape(2*r,nseed)
    G=np.vstack([Q@L[:r],Q@L[r:]]).T@B
    return G,dict(nfev=sol.nfev,elapsed_s=round(time.perf_counter()-start,2),nvar=2*r*nseed,rtol=rtol,atol=atol,calls=calls[0])

def all_six(sp,ref,B,base,seeds,tstar,rtol=1e-9):
    G=np.zeros((6,180));info=[]
    for item in base:
        ind=item['seed_indices'];g,one=solve_reduced(sp,ref,B,item['basis'],seeds[:,ind],tstar,rtol=rtol,atol=rtol*.01)
        G[ind]=g;one['sector']=item['key'];info.append(one)
        print('SOLVED',item['key'],one,flush=True)
    eigs=[];blocks={}
    for item in base:
        ind=item['seed_indices'];g=G[ind];ev=np.linalg.eigvalsh(g@g.T);eigs+=list(np.repeat(ev,item['d']));blocks[item['key']]=ev.tolist()
    gain=np.sqrt(max(eigs))*np.sqrt(102/20000000)
    return gain,blocks,G,info

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--time',type=float,default=4);ap.add_argument('--rtol',type=float,default=1e-8);ap.add_argument('--check',action='store_true');ap.add_argument('--out',type=Path,default=Path('/mnt/data/ud_024_reduced_validation/result.json'))
    args=ap.parse_args()
    t=time.perf_counter();m=Mechanical(nu=.05,beta=.005,cf=0,primary_pattern='uniform');sp=SparseJacobian(m)
    base,S=construct();baseline_sol,ref=baseline(m,max(args.time,100 if args.check else args.time));B=injection(m)
    e=checks(m,sp,ref,base) if args.check else {}
    gain,blocks,G,info=all_six(sp,ref,B,base,S,args.time,args.rtol)
    result={'time':args.time,'gain':gain,'sectors':[{k:v for k,v in x.items() if k!='basis'} for x in base],'blocks':blocks,'info':info,'invariance_errors':e,'elapsed_total_s':time.perf_counter()-t}
    args.out.parent.mkdir(exist_ok=True,parents=True);args.out.write_text(json.dumps(result,indent=2,default=lambda o:o.item() if hasattr(o,'item') else str(o))+'\n')
    np.savez_compressed(args.out.with_suffix('.npz'),G=G)
    print('GAIN',gain,'total',result['elapsed_total_s'],flush=True)
