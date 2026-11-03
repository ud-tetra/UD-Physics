#!/usr/bin/env python3
"""Exact mass-CM block identity and numerical internal stiffness diagnostic.

Frozen original 560-dimensional source mechanics. This is NOT an interval
Green/error certificate, and does not modify the source constitutive law.
"""
import argparse
import json
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/"experiments/icosahedral-pulsetube"))
from jacobian import Linearization, model
from variational import SOURCE

TIMES=[0.,1.,9.2,12.5,64.5,100.]
CASES=["seed10422-0-boundary2","uniform-b0.05-cf0.0"]

def run(case_id):
    case=next(c for c in json.loads((SOURCE/"cases.json").read_text()) if c["id"]==case_id)
    m=model(case,.05)
    L=Linearization(m)
    y0=m.initial_augmented(.1)
    sol=solve_ivp(m.ode,(0,100),y0,method="DOP853",
                  rtol=5e-12,atol=5e-15,dense_output=True)
    assert sol.success
    n=m.n
    sqrtm=np.sqrt(L.M)
    T=np.zeros((n,3))
    spatial=L.spatial
    for k in range(3):
        T[spatial[:,k],k]=1.
    # Q has 3 orthonormal mass-weighted translational columns.
    Q=sqrtm[:,None]*T
    totalmass=Q[:,0]@Q[:,0]
    assert np.allclose(Q.T@Q,totalmass*np.eye(3),atol=1e-12)
    Q/=np.sqrt(totalmass)
    P=np.eye(n)-Q@Q.T
    assert np.linalg.norm(P@Q)<1e-12
    report=[]
    for time in TIMES:
        y=sol.sol(time)
        K,C=L.matrices(y)
        K=K.toarray()
        C=C.toarray()
        Kmass=(K/sqrtm[:,None])/sqrtm[None,:]
        Cmass=(C/sqrtm[:,None])/sqrtm[None,:]
        symK=(Kmass+Kmass.T)/2
        symC=(Cmass+Cmass.T)/2
        klam=eigh(symK,eigvals_only=True,subset_by_index=[0,7])
        clam=eigh(symC,eigvals_only=True,subset_by_index=[0,7])
        KQ=float(np.linalg.norm(Kmass@Q))
        CQ=float(np.linalg.norm(Cmass@Q))
        QK=float(np.linalg.norm(Q.T@Kmass))
        QC=float(np.linalg.norm(Q.T@Cmass))
        antisymK=float(np.linalg.norm(Kmass-Kmass.T))
        antisymC=float(np.linalg.norm(Cmass-Cmass.T))
        # Exact source invariant: CM-free complement is invariant under
        # J(q,v)=[v,-M^-1(Kq+Cv)]; test mass-orthogonal projection.
        qnorm=max(KQ,QK,CQ,QC)
        assert qnorm<1e-8, (case_id,time,qnorm)
        # K includes d/dq(D(q)*v), generally NON-SYMMETRIC even though
        # the conservative potential Hessian is symmetric.
        assert antisymC<1e-8
        # Eigenvalues of K on the mass-relative internal sector; translational
        # exact zero modes are omitted by a tiny positive rank-3 shift.
        eiginternal=eigh(symK + Q@Q.T,eigvals_only=True,subset_by_index=[0,7])
        report.append({
           "u":float(time),
           "internal_mass_normalized_stiffness_eigmin":float(eiginternal[0]),
           "smallest_eight_K_mass_eigenvalues":[float(x) for x in klam],
           "smallest_eight_C_mass_eigenvalues":[float(x) for x in clam],
           "source_internal_K_C_CM_leakage_norm":qnorm,
           "K_mass_skew_error":antisymK,
           "C_mass_skew_error":antisymC,
           "K_mass_negative":bool(eiginternal[0]<-1e-8),
           "K_is_nonconservative_tangent":bool(antisymK>1e-8),
           "C_mass_negative":bool(clam[0]<-1e-8),
        })
    return {
       "case":case_id,
       "status":"NUMERICAL_FINITE_TIME_STIFFNESS_SPECTRUM_PLUS_EXACT_CM_THEOREM",
       "full_mechanical_dimension":2*n,
       "translation_dimension":6,
       "CM_mass":float(totalmass),
       "strict_dop853_nfev":int(sol.nfev),
       "observations":report,
       "certification":"NO interval eigenspectra, residual enclosure, full forced Green, nonlinear tube, or validated reference numerical error",
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",required=True,type=Path)
    args=p.parse_args()
    data={"status":"PASS","labels":["EXACT","CONDITIONAL","NUMERICAL","OPEN"],
          "source_base":"unmodified integrated icosahedral MountLoss with full 560 mechanical phase variables",
          "CM_projector":"Q=M^(1/2)T/sqrt(Mtot), P=I-QQ^T; exact KQ=Q^T K=CQ=Q^T C=0 for reciprocal internal forces; physical 6D Galilean CM block",
          "rigid_Green":"S(t,s)=[[I,(t-s)I],[0,I]] on CM and CM velocity, all times",
          "internal_projection_warning":"Source K includes non-symmetric d/dq(D(q)*velocity). Symmetric K spectrum is a diagnostic, NOT a conservative Hessian eigen-certification; positivity may fail despite nonnegative nonlinear energy.",
          "cases":{case:run(case) for case in CASES}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    print("ICO_PROJECTED_STABILITY_SUMMARY:"+json.dumps(data,sort_keys=True),flush=True)
