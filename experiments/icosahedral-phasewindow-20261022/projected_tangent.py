#!/usr/bin/env python3
"""UD Discovery: full 560-state nonlinear pulse variational projection.

Source: standalone reimplementation originally audited in checkpoint nonaffine-011;
original model imported from ud-tetra/UD-Physics at SHA 41ebf960d90d8147f2ebb8c8b9ecb0700516e9bb.
The moving-state tangent J is differentiated directly from reciprocal physical forces.
Finite computations are development tests, NOT a nonlinear all-phase certificate.
"""
import argparse, json, time, hashlib, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import svd
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonaffine_audit import Mechanical, X, V, EDGES, I, J, R, R2, PROJ, HIDX, AIDX

class MovingTangent:
    def __init__(self,m):
        self.m=m
        self.n=280
        self.pairs=m.G
    def apply(self,q,v,DQ,DV):
        """For arbitrary real columns DQ,DV compute derivative of generalized force.

        DQ,DV arrays (280,b), output same; exact first derivative at positive lengths.
        """
        m=self.m
        b=DQ.shape[1]
        alpha,xp,z,H,rho,rn,s,d,ell,en,e,err,mid,mount,sn,ls=m.geometry(q)
        primal_v=v[1:40].reshape(13,3)
        hv=v[190:280].reshape(30,3)
        dqprim=DQ[1:40].reshape(13,3,b)
        dvprim=DV[1:40].reshape(13,3,b)
        dqH=DQ[190:280].reshape(30,3,b)
        dvH=DV[190:280].reshape(30,3,b)
        dr=dqprim[1:]-dqprim[0]
        dr_l=np.einsum('ij,ijb->ib',rn,dr)
        dr_n=(dr-rn[:,:,None]*dr_l[:,None,:])/rho[:,None,None]
        de=dqprim[I]-dqprim[J]
        de_l=np.einsum('ij,ijb->ib',en,de)
        de_n=(de-en[:,:,None]*de_l[:,None,:])/ell[:,None,None]
        dstrain=np.vstack([dr_l/R,de_l]); derr=m.G@dstrain-DQ[40:190]
        tensions=m.G.T@(5.*err)
        dtension=m.G.T@(5.*derr)
        gt=np.zeros((13,3,b));gh=np.zeros((30,3,b))
        drt=(1+m.g[:,None])*dstrain[:12]-m.g[:,None]*DQ[0]+dtension[:12]
        dgt=drt[:,None,:]/R*rn[:,:,None]+((s+m.g*(s-alpha)+tensions[:12])/R)[:,None,None]*dr_n
        gt[1:]+=dgt;gt[0]-=dgt.sum(axis=0)
        det=m.k[:,None]*dstrain[12:]+dtension[12:]
        dg_edge=det[:,None,:]*en[:,:,None]+(m.k*e+tensions[12:])[:,None,None]*de_n
        np.add.at(gt,I,dg_edge);np.add.at(gt,J,-dg_edge)
        dhmount=dqH-(dqprim[I]+dqprim[J])*.5
        gh+=m.kh[:,None,None]*dhmount
        np.add.at(gt,I,-m.kh[:,None,None]*dhmount*.5)
        np.add.at(gt,J,-m.kh[:,None,None]*dhmount*.5)
        # Source ordinary current-axis spring dashpots
        spoke_vel=primal_v[1:]-primal_v[0]
        ds_rate=np.einsum('ij,ij->i',rn,spoke_vel)/R
        dds_rate=(np.einsum('ijb,ij->ib',dr_n,spoke_vel)+np.einsum('ij,ijb->ib',rn,dvprim[1:]-dvprim[0]))/R
        drd=m.cs/R*(dds_rate[:,None,:]*rn[:,:,None]+ds_rate[:,None,None]*dr_n)
        gt[1:]+=drd;gt[0]-=drd.sum(axis=0)
        edge_vel=primal_v[I]-primal_v[J]
        ed_rate=np.einsum('ij,ij->i',en,edge_vel)
        ded_rate=np.einsum('ijb,ij->ib',de_n,edge_vel)+np.einsum('ij,ijb->ib',en,dvprim[I]-dvprim[J])
        dedamp=m.ce*(ded_rate[:,None,:]*en[:,:,None]+ed_rate[:,None,None]*de_n)
        np.add.at(gt,I,dedamp);np.add.at(gt,J,-dedamp)
        # Four-anchor central moving-axis loss
        strut_vel=hv[HIDX]-primal_v[AIDX]
        diff=dqH[HIDX]-dqprim[AIDX]
        dl=np.einsum('ij,ijb->ib',sn,diff)
        dn=(diff-sn[:,:,None]*dl[:,None,:])/ls[:,None,None]
        rate=np.einsum('ij,ij->i',sn,strut_vel)
        drate=np.einsum('ijb,ij->ib',dn,strut_vel)+np.einsum('ij,ijb->ib',sn,dvH[HIDX]-dvprim[AIDX])
        drag=m.eta*(drate[:,None,:]*sn[:,:,None]+rate[:,None,None]*dn)
        np.add.at(gt,AIDX,-drag);np.add.at(gh,HIDX,drag)
        dalpha=(1+m.g.sum())*DQ[0]-np.sum(m.g[:,None]*dstrain[:12],axis=0)
        result=np.vstack([dalpha[None,:],gt.reshape(39,b),-5*derr+.5*DV[40:190],gh.reshape(90,b)])
        return result

    def rhs(self,t,state,b):
        m=self.m
        Q=state[:280];Vel=state[280:560]
        DQ=state[560:560+280*b].reshape(280,b)
        DV=state[560+280*b:].reshape(280,b)
        grad,_=m.forces(Q,Vel)
        dg=self.apply(Q,Vel,DQ,DV)
        return np.r_[Vel,-grad/m.M,DV.ravel(),(-dg/m.M[:,None]).ravel()]

    def verify_jvp(self, y, b=4, eps=1e-6,seed=11):
        rng=np.random.default_rng(seed)
        Q=y[:280];vv=y[280:560]
        DQ=rng.normal(size=(280,b));DV=rng.normal(size=(280,b))
        dg=self.apply(Q,vv,DQ,DV)
        errs=[]
        for col in range(b):
            fplus,_=self.m.forces(Q+eps*DQ[:,col],vv+eps*DV[:,col])
            fminus,_=self.m.forces(Q-eps*DQ[:,col],vv-eps*DV[:,col])
            errs.append(np.max(np.abs((fplus-fminus)/(2*eps)-dg[:,col])))
        return max(errs)

def injection(m):
    # 560 x 180 canonical housing energy-orthonormal injection
    B=np.zeros((560,180));scale=np.repeat(np.sqrt(m.mh),3)
    j=np.arange(90)
    B[190+j,j]=1/(10*scale)
    B[280+190+j,90+j]=1/scale
    return B

def projected_output(W):
    # shell only -> fixed reference nonaffine projector; this is linear readout
    b=W.shape[1]
    dq=W[4:40].reshape(12,3,b)
    dZ=np.einsum('ij,jkb->ikb',PROJ,dq).reshape(36,b)
    return dZ

def run_case(m, T, samples,rtol,atol,summary_only=False):
    t0=time.perf_counter()
    y0,_=m.initial(phase='none')
    L=MovingTangent(m)
    direction_error=L.verify_jvp(y0[:560],b=3)
    assert direction_error<3e-6,direction_error
    B=injection(m)
    # mechanical 560 reference trajectory + full 560x180 tangent (no heat)
    initial=np.r_[y0[:560],B.ravel()]
    grid=np.linspace(0,T,samples)
    def rhs(t,state):return L.rhs(t,state,180)
    sol=solve_ivp(rhs,(0,T),initial,t_eval=grid,method='DOP853',rtol=rtol,atol=atol)
    assert sol.success,sol.message
    Eh=(1+m.g.sum())*.01/2/40000*1.5
    eps=np.sqrt(2*Eh)
    snapshots=[];max_amp=(-1,None,None,None)
    for i,t in enumerate(sol.t):
        Q=sol.y[:280,i]
        ybase=sol.y[:560,i]
        Z0=PROJ@Q[4:40].reshape(12,3)
        W=sol.y[560:,i].reshape(560,180)
        A=projected_output(W)
        # Frobenius induced gain from canonical unit-2norm phase
        # computed through top 36x36 eigenvalue of AA^T
        S=np.linalg.svd(A,full_matrices=False,compute_uv=False)
        gain=eps*S[0]
        bound=np.linalg.norm(Z0)+gain
        if bound>max_amp[0]:max_amp=(bound,float(t),float(np.linalg.norm(Z0)),float(gain))
        snapshots.append((float(t),float(np.linalg.norm(Z0)),float(gain),float(bound),float(S[0])))
    ipeak=np.argmax([k[3] for k in snapshots]);tpeak=grid[ipeak]
    W=sol.y[560:,ipeak].reshape(560,180)
    A=projected_output(W)
    u,s,vh=svd(A,full_matrices=False)
    phase=vh[0,:]
    phase_norm=np.linalg.norm(phase)
    assert abs(phase_norm-1)<1e-11
    # directional finite perturbation follow-up, naturally distinct from a full ball theorem
    elapsed=time.perf_counter()-t0
    result={'T':float(T),'sample_count':samples,'nu':m.nu,'beta':m.beta,'cf':m.cf,'pattern':m.pattern,'Eh':float(Eh),'eps_sqrt_2Eh':float(eps),
            'global_sampled_linearized_amplitude_bound':float(max_amp[0]),'at_u':max_amp[1],
            'reference_nonaffine_at_peak':max_amp[2],'housing_first_order_allowance_at_peak':max_amp[3],
            'ratio_to_1_over_40':40*max_amp[0],'JVP_directional_FD_max_error':float(direction_error),
            'solver_nfev':sol.nfev,'solver_rtol':rtol,'solver_atol':atol,'wall_seconds':elapsed,
            'scope':'NUMERICAL sampled t, full 560-state moving pulse, all180 housing tangent phase directions at each sampled time. First derivative only; NOT nonlinear all-phase certification.'}
    return result,np.array(snapshots),phase,sol.y[:560],sol.t

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);parser.add_argument('--T',type=float,default=10);parser.add_argument('--samples',type=int,default=101);
    parser.add_argument('--nu',type=float,default=.05);parser.add_argument('--beta',type=float,default=.005);parser.add_argument('--pattern',default='uniform');parser.add_argument('--cf',type=float,default=0);
    parser.add_argument('--rtol',type=float,default=5e-8);parser.add_argument('--atol',type=float,default=1e-10);
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    m=Mechanical(nu=args.nu,beta=args.beta,cf=args.cf,primary_pattern=args.pattern)
    result,rows,phase,reference,ts=run_case(m,args.T,args.samples,args.rtol,args.atol)
    (args.out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savetxt(args.out/'tangent_gain.csv',rows,delimiter=',',header='u,baseline_Znorm,worst_phase_linear_amplitude,triangle_bound,unscaled_gain',comments='')
    np.save(args.out/'worst_phase_at_peak.npy',phase,allow_pickle=False)
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
