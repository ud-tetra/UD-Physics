#!/usr/bin/env python3
"""Inverse-designed covariance metric and a rank-minimal open contact.

The imported K is conventional; neither construction derives a UD material law.
"""
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "graphite-registry-defect-source"))
from audit_registry_defect import carrier  # noqa: E402


def rel(a, b):
    return float(np.linalg.norm(a-b)/np.linalg.norm(b))


def main():
    k = np.array(json.loads((HERE.parent / "graphite-matched-hessian-reconstruction" /
                             "MATCHED_HESSIAN_RESULTS.json").read_text())["K"])
    _, b, m = carrier()
    b = np.asarray(b, float)
    m = np.asarray(m, float)
    n, e = b.shape
    one = np.ones(n)/np.sqrt(n)
    p = np.eye(n)-np.outer(one, one)
    l = b@b.T
    lp = np.linalg.pinv(l, hermitian=True)
    pg = b.T@lp@b
    pc = np.eye(e)-pg
    assert (n, e) == (14, 21) and np.linalg.matrix_rank(b) == 13
    assert np.linalg.norm(b.T@one) < 1e-13
    assert rel(pg@pg, pg) < 1e-12
    assert np.linalg.eigvalsh(k).min() > 0

    # Target covariance is Cov(B^T h)/Theta_bar, Theta_bar=kBT/14.
    q = b.T@np.linalg.solve(k, b)
    qplus = np.linalg.pinv(q, hermitian=True)
    keff = p@k@p-(p@k@one)[:, None]@(one@k@p)[None, :]/float(one@k@one)
    schur_metric = b.T@lp@keff@lp@b
    assert rel(qplus, schur_metric) < 1e-10
    positive_q = np.linalg.eigvalsh(q)[-13:]
    eta = float(np.linalg.eigvalsh(qplus)[-13])  # positive free cycle stiffness
    he_cov = qplus+eta*pc
    cov_native = pg@np.linalg.inv(he_cov)@pg
    assert np.linalg.eigvalsh(he_cov).min() > 0
    assert rel(cov_native, q) < 1e-10
    w_unit = np.diag(pg)
    w_cov = np.diag(cov_native)
    source_unit = m.T@(w_unit[:, None]*b.T)
    source_cov = m.T@(w_cov[:, None]*b.T)
    assert np.linalg.norm(source_unit) < 1e-12

    # A closed incidence matrix cannot address the uniform site coordinate.
    # One explicit grounded edge at A0 completes row rank, while importing an
    # external reference. The right-inverse metric is generally dense.
    a = np.column_stack([b, np.eye(n)[:, 0]])
    la = a@a.T
    la_inv = np.linalg.inv(la)
    p_row = a.T@la_inv@a
    eta_contact = 1.0
    he_contact = a.T@la_inv@la_inv@a+eta_contact*(np.eye(e+1)-p_row)
    assert np.linalg.matrix_rank(a) == n
    assert np.linalg.eigvalsh(he_contact).min() > 0
    effective_mass = a@he_contact@a.T
    assert rel(effective_mass, np.eye(n)) < 1e-10
    # E=(x^T H_v x+y^T H_e y)/2; x'=A H_e y, y'=-A^T H_v x.
    # With s=t/tau, H_v=(14 tau^2/m_phys) K makes x'' the physical h equation.
    hv = k.copy()  # illustrative 14 tau^2/m_phys = 1 in compatible units
    generator = np.block([[np.zeros((n,n)), a@he_contact],
                          [-a.T@hv, np.zeros((e+1,e+1))]])
    energy = np.block([[hv, np.zeros((n,e+1))],
                       [np.zeros((e+1,n)), he_contact]])
    assert np.linalg.norm(generator.T@energy+energy@generator)/np.linalg.norm(energy) < 1e-10
    assert rel(a@he_contact@a.T@hv, k) < 1e-10
    global_a = np.column_stack([b, one])
    global_l = global_a@global_a.T

    # This is a necessary, not sufficient, locality diagnostic. At edge
    # distance >1, a nonzero entry rules out a diagonal/one-hop edge metric.
    adjacency = ((abs(b).T@abs(b)) > 0)
    far = ~adjacency
    np.fill_diagonal(far, False)
    significant = abs(qplus) > 1e-10*np.max(abs(qplus))
    return dict(evidence="EXACT/CONDITIONAL algebra; NUMERICAL conventional-K inverse design",
                base_K="registered KC plus plate Hessian, energy per upper atom",
                n_sites=n, n_bonds=e, rank_closed=int(np.linalg.matrix_rank(b)),
                rank_with_grounded_contact=int(np.linalg.matrix_rank(a)),
                static_gradient_metric=dict(covariance_definition="Q=B^T K^-1 B, units A^2/meV",
                    q_rank=int(np.linalg.matrix_rank(q)), q_eigen_nonzero_min=float(positive_q[0]),
                    q_eigen_nonzero_max=float(positive_q[-1]),
                    metric_definition="H_e=Q^+ + eta P_cycle; eta is arbitrary positive",
                    eta_cycle=eta, min_metric_eigenvalue=float(np.linalg.eigvalsh(he_cov).min()),
                    schur_identity_relative_error=rel(qplus, schur_metric),
                    covariance_match_relative_error=rel(cov_native, q),
                    unit_source_norm=float(np.linalg.norm(source_unit)),
                    model_imported_source_norm=float(np.linalg.norm(source_cov)),
                    source_rank=int(np.linalg.matrix_rank(source_cov)),
                    source_weight_cv=float(w_cov.std()/w_cov.mean()),
                    far_edge_metric_nonzeros=int(np.count_nonzero(significant & far & np.triu(np.ones((e,e),bool),1))),
                    far_edge_metric_max_abs=float(np.max(abs(qplus[far])))),
                grounded_contact=dict(contact="one signed external reference at site A0, not an internal incidence edge",
                    rank_minimal_extra_columns=1,
                    grounded_l_min_eigenvalue=float(np.linalg.eigvalsh(la).min()),
                    grounded_l_condition=float(np.linalg.cond(la)),
                    global_uniform_contact_l_condition=float(np.linalg.cond(global_l)),
                    metric_min_eigenvalue=float(np.linalg.eigvalsh(he_contact).min()),
                    effective_mass_identity_relative_error=rel(effective_mass,np.eye(n)),
                    skew_adjoint_metric_relative_error=float(np.linalg.norm(generator.T@energy+energy@generator)/np.linalg.norm(energy)),
                    oscillator_match_relative_error=rel(a@he_contact@a.T@hv,k)),
                caveat="The covariance metric and contact dynamical metric are different inverse designs. No single sourced native constitutive law, physical clock, damping, measured friction, or angle selection follows.")


if __name__ == "__main__":
    result = main()
    (HERE/"EDGE_RESULTS.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
