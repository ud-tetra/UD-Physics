#!/usr/bin/env python3
"""Joint conservative covariance/spectrum construction from exposed KC stiffness.

All material maps, the grounded contact, and the odd readout are assumed/FIT.
"""
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "graphite-registry-defect-source"))
from audit_registry_defect import carrier  # noqa: E402


def rel(x, y):
    return float(np.linalg.norm(x-y)/np.linalg.norm(y))


def main():
    source = json.loads((HERE.parent/"graphite-matched-hessian-reconstruction"/
                         "MATCHED_HESSIAN_RESULTS.json").read_text())
    k = np.asarray(source["K"], float)
    _, b, m = carrier()
    b, m = np.asarray(b,float), np.asarray(m,float)
    n, e = b.shape
    a = np.column_stack((b, np.eye(n)[:,0]))
    la = a@a.T
    la_inv = np.linalg.inv(la)
    prow = a.T@la_inv@a
    he = a.T@la_inv@la_inv@a + (np.eye(e+1)-prow)
    hv = k.copy()  # normalized 14 tau^2/m_phys = 1, Theta_native = Theta_bar = 1
    assert np.linalg.matrix_rank(a) == n and np.linalg.eigvalsh(k).min()>0
    assert np.linalg.eigvalsh(he).min()>0
    assert rel(a@he@a.T, np.eye(n))<1e-11
    generator=np.block([[np.zeros((n,n)),a@he],[-a.T@hv,np.zeros((e+1,e+1))]])
    h=np.block([[hv,np.zeros((n,e+1))],[np.zeros((e+1,n)),he]])
    assert np.linalg.norm(generator.T@h+h@generator)/np.linalg.norm(h)<1e-11

    eig, u = np.linalg.eigh(k)
    invroot = (u/np.sqrt(eig))@u.T
    target = b.T@np.linalg.solve(k,b)
    # Row-sector y=A^T x' is invariant, because y'=-A^T H_v x.
    # E|row=(x^T K x+|x'|^2)/2, hence Cov(x)=K^-1 and Cov(x')=I.
    cov_y=a.T@a
    odd = b.T@invroot  # r=odd x'; a=14 tau^2/m_phys set to 1 here
    cov_r=odd@odd.T
    cov_q=b.T@np.linalg.inv(k)@b
    raw_internal_var=np.diag(cov_y)[:e]
    q_var=np.diag(cov_q)
    raw_port=m.T@(raw_internal_var[:,None]*b.T)
    r_port=m.T@(np.diag(cov_r)[:,None]*b.T)
    assert rel(cov_q,target)<1e-11 and rel(cov_r,target)<1e-11
    assert np.ptp(raw_internal_var)<1e-12 and np.linalg.norm(raw_port)<1e-12
    assert np.linalg.matrix_rank(r_port)==2
    # Another equal-mass local odd gradient r_loc=B^T x' has equal diagonal.
    assert np.ptp(np.diag(b.T@b))<1e-12

    lag_errors=[]
    for s in (0.0,0.01,0.1,0.5,1.0):
        cos=(u*np.cos(np.sqrt(eig)*s))@u.T
        qq=b.T@(u*(np.cos(np.sqrt(eig)*s)/eig))@u.T@b
        rr=odd@cos@odd.T
        lag_errors.append(dict(dimensionless_lag=s,relative_covariance_error=rel(rr,qq)))

    # A single incoming contact is essential to retain the uniform coordinate.
    # For the full K all 14 eigenvectors have nonzero B^T projection, as in
    # the preceding metric audit. Rank/source matches do not select a law.
    soft_visibility=float(np.linalg.norm(b.T@u[:,0]))
    kbar=json.loads((HERE.parent/"graphite-metric-locality"/"METRIC_RESULTS.json").read_text())
    return dict(evidence="EXACT/CONDITIONAL finite positive construction; NUMERICAL/FIT conventional K replay",
        normalization="a=14 tau^2/m_phys=1 and Theta_native=Theta_bar=1 for replay; general formulas retain scales",
        n_sites=n,n_internal_edges=e,n_augmented_edges=e+1,augmented_rank=int(np.linalg.matrix_rank(a)),
        generator_skew_adjoint_relative_error=float(np.linalg.norm(generator.T@h+h@generator)/np.linalg.norm(h)),
        effective_site_inverse_mass_relative_error=rel(a@he@a.T,np.eye(n)),
        even_bond_covariance_relative_error=rel(cov_q,target),
        odd_bond_covariance_relative_error=rel(cov_r,target),
        conservative_stationary_two_time_covariance=lag_errors,
        raw_internal_edge_variance_range=[float(raw_internal_var.min()),float(raw_internal_var.max())],
        raw_internal_edge_port_norm=float(np.linalg.norm(raw_port)),
        odd_readout_port_norm=float(np.linalg.norm(r_port)),
        odd_readout_port_rank=int(np.linalg.matrix_rank(r_port)),
        odd_readout_weight_cv=float(q_var.std()/q_var.mean()),
        inverse_sqrt_K_offdiagonal_relative_frobenius=float(np.linalg.norm(invroot-np.diag(np.diag(invroot)))/np.linalg.norm(invroot)),
        soft_mode_bond_visibility=soft_visibility,
        preceding_closed_gradient_mode_budget=kbar["observed_material_mode_rank_sum"],
        exposure="Readout r=B^T K^-1/2 x'/sqrt(a) imports conventional K; grounded contact and H_v=aK are assumed; no new force data",
        limitation="Conservative equilibrium two-time law only; local raw y source zero, damping/contact physics and signed friction open")


if __name__=="__main__":
    result=main()
    (HERE/"JOINT_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
