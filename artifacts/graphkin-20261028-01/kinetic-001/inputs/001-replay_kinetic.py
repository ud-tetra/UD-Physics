#!/usr/bin/env python3
"""Reciprocal kinetic-metric tradeoff for the registered graphite oscillator."""
import json
from pathlib import Path
import sys

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"graphite-registry-defect-source"))
from audit_registry_defect import carrier  # noqa: E402


def relative(a,b):
    return float(np.linalg.norm(a-b)/np.linalg.norm(b))


def curvature_fit(k,b):
    q=b.T@np.linalg.solve(k,b)
    s=b.T@b
    # The scalar kappa has stiffness units; a=1 in this numerical unit replay.
    kappa=float(np.sum(q*s)/np.sum(q*q))
    defect=relative(kappa*q,s)
    eig=np.linalg.eigvalsh(k)
    lags=[]
    ew,u=np.linalg.eigh(k)
    for t in (0.0,0.01,0.1,0.5,1.0):
        physical=b.T@(u*(np.cos(np.sqrt(ew)*t)/ew))@u.T@b
        flat=q*np.cos(np.sqrt(kappa)*t)
        lags.append(dict(dimensionless_lag=t,relative_full_covariance_error=relative(flat,physical)))
    return dict(kappa_best_frobenius_curvature=float(kappa),
                best_second_derivative_relative_defect=defect,
                k_eigen_min=float(eig[0]),k_eigen_max=float(eig[-1]),
                conservative_lag_comparison=lags)


def main():
    data=json.loads((HERE.parent/"graphite-matched-hessian-reconstruction"/
                     "MATCHED_HESSIAN_RESULTS.json").read_text())
    _,b,m=carrier()
    b=np.asarray(b,float);m=np.asarray(m,float)
    k=np.asarray(data["K"],float)
    u=np.ones(14)/np.sqrt(14)
    p=np.eye(14)-np.outer(u,u)
    q=b.T@np.linalg.solve(k,b)
    assert np.linalg.eigvalsh(k).min()>0
    assert np.linalg.matrix_rank(b)==13
    # Energy En=(x^T V x + pi^T G pi)/2, x'=G pi, pi'=-V x.
    # Set V=aK and a=1 in numeric units. A matching site/bond acceleration
    # for every initial x forces P(G-I)=0, leaving only uniform-mode freedom.
    alpha=.6
    g_dyn=np.eye(14)+alpha*np.outer(u,u)
    assert np.linalg.eigvalsh(g_dyn).min()>0
    assert np.linalg.norm(b.T@(g_dyn-np.eye(14))@k)<1e-12
    cov_local_dyn=b.T@g_dyn@b
    assert np.ptp(np.diag(cov_local_dyn))<1e-12
    source_dyn=m.T@(np.diag(cov_local_dyn)[:,None]*b.T)
    assert np.linalg.norm(source_dyn)<1e-12

    trade=curvature_fit(k,b)
    kappa=trade["kappa_best_frobenius_curvature"]
    g_cov=kappa*np.linalg.inv(k)
    assert np.linalg.eigvalsh(g_cov).min()>0
    assert relative(b.T@g_cov@b/kappa,q)<1e-12
    # r=B^T x'/sqrt(a*kappa), a=1. Cov(x')=a Theta_bar G.
    source_cov=m.T@(np.diag(b.T@g_cov@b/kappa)[:,None]*b.T)
    assert np.linalg.matrix_rank(source_cov)==2
    flat_operator=g_cov@k
    assert relative(flat_operator,kappa*np.eye(14))<1e-12
    # Check the projected covariance is not a scalar graph projector.
    lsq_alpha=float(np.sum(q*(b.T@b))/np.sum((b.T@b)**2))
    q_scalar_defect=relative(lsq_alpha*(b.T@b),q)
    alternatives=[]
    for row in data["pressure_rows"]:
        for step,kk in (("nominal",row["K"]),("alternate",row["K_alt_step"])):
            fit=curvature_fit(np.asarray(kk,float),b)
            alternatives.append(dict(pressure_delta_MPa=row["delta_pressure_MPa"],hessian_step=step,
                                     curvature_defect=fit["best_second_derivative_relative_defect"],
                                     fitted_kappa=fit["kappa_best_frobenius_curvature"]))
    return dict(evidence="EXACT/CONDITIONAL reciprocal identity; NUMERICAL target-exposed KC model",
      normalization="a=14 tau^2/m=1 in compatible material units for numerical replay; kappa has K units, theta_n=a Theta_bar",
      site_dimension=14,bond_dimension=21,
      exact_theorem="V=aK and B^T G V=B^T aK for all x imply G=I+gamma uu^T; hence B^T G B=B^T B and all internal local-gradient variances equal 2",
      exact_site_dynamic_example=dict(uniform_gamma=alpha,source_norm=float(np.linalg.norm(source_dyn)),
                                     bond_acceleration_relative_error=float(np.linalg.norm(b.T@(g_dyn-np.eye(14))@k)/np.linalg.norm(b.T@k))),
      static_local_covariance_fit=dict(G_definition="G=kappa K^-1; local r=B^T x_prime/sqrt(a kappa)",
                                     positive_min_eigenvalue=float(np.linalg.eigvalsh(g_cov).min()),
                                     target_Q_match_relative_error=relative(b.T@g_cov@b/kappa,q),
                                     model_imported_source_norm=float(np.linalg.norm(source_cov)),
                                     source_rank=int(np.linalg.matrix_rank(source_cov)),
                                     flat_site_operator_relative_error=relative(flat_operator,kappa*np.eye(14)),
                                     fit=trade),
      projected_Q_best_scalar_graph_relative_defect=q_scalar_defect,
      archive_pressure_step_sensitivity=alternatives,
      caveat="G=kappa K^-1 is target-selected and changes physical mass and the full spectrum; theorem assumes fixed V=aK, reciprocal finite oscillator, exact bond acceleration for every initial site x and local B^T velocity readout. No loss or measured friction follows.")


if __name__=="__main__":
    out=main()
    (HERE/"KINETIC_RESULTS.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
