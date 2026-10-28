#!/usr/bin/env python3
"""Support-overlap lower bounds for a local odd graphite bond readout.

The target Q is from a previously exposed conventional registered stiffness.
The support theorem is exact for the declared isotropic site-velocity covariance.
"""
import json
from pathlib import Path
import sys

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"graphite-registry-defect-source"))
from audit_registry_defect import carrier, permutations  # noqa: E402


def graph_distance(b):
    n=b.shape[0]
    adjacency=((abs(b)@abs(b).T)>0)
    d=np.full((n,n),n,dtype=int)
    np.fill_diagonal(d,0)
    d[adjacency & ~np.eye(n,dtype=bool)]=1
    for k in range(n):
        d=np.minimum(d,d[:,k,None]+d[k,None,:])
    return d


def supports(b,d,r):
    return np.array([(d[:,np.nonzero(b[:,e])[0]].min(axis=1)<=r)
                     for e in range(b.shape[1])],dtype=bool)


def bound(q,support):
    disjoint=(support.astype(int)@support.T.astype(int)==0)
    np.fill_diagonal(disjoint,False)
    upper=np.triu(disjoint,1)
    vals=q[upper]
    return dict(unordered_disjoint_pairs=int(np.count_nonzero(upper)),
                nonzero_disjoint_pairs=int(np.count_nonzero(abs(vals)>1e-12*np.max(abs(q)))),
                disjoint_entry_abs_max=float(np.max(abs(vals))) if vals.size else 0.0,
                disjoint_entry_abs_min=float(np.min(abs(vals))) if vals.size else None,
                covariance_relative_frobenius_lower_bound=float(np.linalg.norm(q*disjoint)/np.linalg.norm(q)))


def main():
    data=json.loads((HERE.parent/"graphite-matched-hessian-reconstruction"/
                     "MATCHED_HESSIAN_RESULTS.json").read_text())
    k=np.array(data["K"])
    pairs,b,m=carrier()
    b=np.array(b,dtype=int)
    m=np.array(m,dtype=float)
    d=graph_distance(b)
    q=b.T@np.linalg.solve(k,b)
    support={str(r):supports(b,d,r) for r in (0,1,2)}
    result={r:bound(q,s) for r,s in support.items()}
    assert result["0"]["unordered_disjoint_pairs"]>0
    assert result["0"]["covariance_relative_frobenius_lower_bound"]>0

    # A deliberately fitted diagonal-weight match has 21 edge scales and
    # reproduces the rank-two variance port without reproducing Q.
    w=np.diag(q)
    scales=np.sqrt(w/2)
    d_fitted=scales[:,None]*b.T
    q_fitted=d_fitted@d_fitted.T
    assert np.max(abs(np.diag(q_fitted)-w))<1e-12
    port=m.T@(w[:,None]*b.T)
    # Uniform endpoint map D=B^T has zero source after common scaling.
    assert np.linalg.norm(m.T@b.T)<1e-12
    group=permutations(pairs,b)
    kbar=sum(p@k@p.T for p,_,_,_ in group)/len(group)
    qbar=b.T@np.linalg.solve(kbar,b)
    assert np.ptp(np.diag(qbar))<1e-11
    alternatives=[]
    for row in data["pressure_rows"]:
        for label,kk in (("nominal",row["K"]),("alternate_step",row["K_alt_step"])):
            qq=b.T@np.linalg.solve(np.array(kk),b)
            alternatives.append(dict(pressure_delta_MPa=row["delta_pressure_MPa"],
                                     hessian_step=label,
                                     radius_zero_relative_bound=bound(qq,support["0"])["covariance_relative_frobenius_lower_bound"]))
    return dict(evidence="EXACT/CONDITIONAL support-overlap zero; NUMERICAL conventional model Q",
        normalization="Q=Cov(B^T h)/Theta_bar=B^T K^-1 B, Theta_bar=kBT/14; odd site velocity Cov(x_prime)=a Theta_bar I",
        n_vertices=b.shape[0],n_edges=b.shape[1],site_graph_diameter=int(d.max()),
        neighborhood_bounds=result,
        target_Q_frobenius=float(np.linalg.norm(q)),
        uniform_odd_endpoint_variance=float(np.diag(b.T@b).mean()),
        uniform_endpoint_source_norm=float(np.linalg.norm(m.T@b.T)),
        fitted_edge_scale_count=len(scales),
        fitted_diagonal_match_max_abs=float(np.max(abs(np.diag(q_fitted)-w))),
        fitted_endpoint_full_covariance_relative_error=float(np.linalg.norm(q_fitted-q)/np.linalg.norm(q)),
        fitted_endpoint_port_norm=float(np.linalg.norm(port)),
        group_averaged_Q_radius_zero_bound=bound(qbar,support["0"]),
        alternative_pressure_step_bounds=alternatives,
        caveat="The bound applies to a linear odd readout D x_prime with isotropic site-velocity covariance and declared support. It does not constrain even q=B^T x, correlated velocities, extra hidden sites, or a nonlocal native metric. Matching diagonal weights with 21 exposed scales is a fit, not a physical residual.")


if __name__=="__main__":
    out=main()
    (HERE/"LOCAL_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
