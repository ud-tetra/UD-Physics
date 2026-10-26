#!/usr/bin/env python3
"""Positive vertex-metric inverse design against a matched graphite K.

This fits a conventional model. It does not derive UD material stiffness,
the edge Gibbs law, a physical clock, or loss.
"""
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "graphite-registry-defect-source"))
from audit_registry_defect import carrier, permutations  # noqa: E402

DATA = HERE.parent / "graphite-matched-hessian-reconstruction" / "MATCHED_HESSIAN_RESULTS.json"


def symmetric_optimal(k, b, l, h_zero):
    """Minimum of ||B^T(H L-K)||_F over symmetric H, with fixed positive null mode."""
    eig, u = np.linalg.eigh(l)
    kp = u.T @ k @ u
    hh = np.zeros_like(kp)
    zero = np.argmin(np.abs(eig))
    assert abs(eig[zero]) < 1e-12
    for i in range(14):
        for j in range(14):
            if i != zero and j != zero:
                hh[i, j] = 2*kp[i, j]/(eig[i]+eig[j])
    hh[zero, zero] = h_zero
    h = u @ hh @ u.T
    assert np.linalg.eigvalsh(h).min() > 0
    return h


def local_least_squares(k, b, l, radius):
    dist = np.full((14, 14), 100, dtype=int)
    np.fill_diagonal(dist, 0)
    dist[l < 0] = 1
    for via in range(14):
        dist = np.minimum(dist, dist[:, via, None]+dist[via, None, :])
    basis = []
    for i in range(14):
        for j in range(i, 14):
            if dist[i, j] <= radius:
                a = np.zeros((14, 14))
                a[i, j] = a[j, i] = 1
                basis.append(a)
    design = np.stack([(b.T @ a @ l).ravel() for a in basis], axis=1)
    target = (b.T @ k).ravel()
    coef = np.linalg.lstsq(design, target, rcond=None)[0]
    h = sum(v*a for v, a in zip(coef, basis))
    return h, len(basis), dist


def relative_defect(h, k, b, l):
    return float(np.linalg.norm(b.T @ (h @ l-k))/np.linalg.norm(b.T @ k))


def spectral_weights(k, b):
    eig, u = np.linalg.eigh(k)
    groups = []
    i = 0
    while i < len(eig):
        j = i+1
        while j < len(eig) and abs(eig[j]-eig[i]) < 1e-4:
            j += 1
        projected = b.T @ u[:, i:j]
        sv = np.linalg.svd(projected, compute_uv=False)
        rank = int(np.count_nonzero(sv > sv.max()*1e-8))
        assert rank == j-i
        groups.append(dict(model_eigenvalue_mean=float(eig[i:j].mean()), multiplicity=j-i,
                           edge_weight_rank=rank, minimum_projection_singular=float(sv.min())))
        i = j
    assert sum(g["edge_weight_rank"] for g in groups) == 14
    return groups


def main():
    raw = json.loads(DATA.read_text())
    k = np.array(raw["K"])
    pairs, b, m = carrier()
    l = b @ b.T
    eye = np.eye(14)
    ie = np.eye(14, dtype=int)
    assert np.array_equal(l @ (l-6*ie) @ ((l-3*ie)@(l-3*ie)-2*ie), np.zeros((14,14), dtype=int))
    group = permutations(pairs, b)
    kb = sum(p @ k @ p.T for p, _, _, _ in group)/21
    polynomial = np.stack([eye.ravel(), l.ravel(), (l@l).ravel()], axis=1)
    a, bb, cc = np.linalg.lstsq(polynomial, kb.ravel(), rcond=None)[0]
    # On the positive spectrum (lambda-6)((lambda-3)^2-2)=0,
    # so lambda^-1=(lambda^2-12lambda+43)/42.
    coefficients = [bb+43*a/42, cc-2*a/7, a/42]
    hbar = coefficients[0]*eye+coefficients[1]*l+coefficients[2]*l@l
    c_ref = float(np.vdot(b.T@k, b.T@l)/np.vdot(b.T@l,b.T@l))
    hopt = symmetric_optimal(k, b, l, coefficients[0])
    h1, count, dist = local_least_squares(k,b,l,1)
    assert count == 35 and dist.max() == 3
    assert np.linalg.eigvalsh(hbar).min() > 0 and np.linalg.eigvalsh(h1).min() > 0
    p0 = np.ones((14,14))/14
    p = eye-p0
    uniform_injection = float(np.linalg.norm(b.T@k@p0)/np.linalg.norm(b.T@k))
    full = relative_defect(hopt,k,b,l)
    noncomm_remainder = float(np.sqrt(max(0, full*full-uniform_injection*uniform_injection)))
    projector = b.T @ np.linalg.pinv(l) @ b
    assert np.linalg.norm(projector@projector-projector) < 1e-12
    assert np.ptp(np.diag(projector)) < 1e-12
    assert np.linalg.norm(m.T @ (np.diag(projector)[:,None]*b.T)) < 1e-12
    bands = spectral_weights(k,b)
    alt = np.array(raw["pressure_rows"][1]["K_alt_step"])
    soft = float(np.linalg.norm(b.T@np.linalg.eigh(k)[1][:,0]))
    soft_alt = float(np.linalg.norm(b.T@np.linalg.eigh(alt)[1][:,0]))
    return dict(evidence="EXACT finite-carrier identities and conditional positive metric formula; NUMERICAL conventional K inverse design; physical source/loss OPEN",
                input="registered conventional K per upper atom; 14 sites, 21 edges; unit native edge metric, vertex H_v symmetric positive",
                exact_spectrum="L: 0 (1), 3-sqrt(2) (6), 3+sqrt(2) (6), 6 (1); positive spectrum obeys lambda^3-12lambda^2+43lambda-42=0",
                clock_normalization="For s=t/tau and physical mass m, H_v is g(L)/c with c=m/(14tau^2). c_ref below is a fitted model scale only.",
                conventional_K_fit=dict(group_mean_K_I_L_L2=[float(a),float(bb),float(cc)],
                    group_polynomial_relative_error=float(np.linalg.norm(kb-(a*eye+bb*l+cc*l@l))/np.linalg.norm(kb)),
                    positive_two_hop_g_coeff_I_L_L2=[float(v) for v in coefficients],
                    group_mean_intertwining_relative_error=relative_defect(hbar,kb,b,l),
                    group_mean_metric_min_eigenvalue=float(np.linalg.eigvalsh(hbar).min())),
                actual_K=dict(best_scalar_c=float(c_ref),
                    scalar_metric_relative_defect=relative_defect(c_ref*eye,k,b,l),
                    group_mean_metric_relative_defect=relative_defect(hbar,k,b,l),
                    optimized_symmetric_positive_relative_defect=full,
                    optimized_symmetric_min_eigenvalue=float(np.linalg.eigvalsh(hopt).min()),
                    one_hop_symmetric_fit_parameters=count,
                    one_hop_positive_relative_defect=relative_defect(h1,k,b,l),
                    one_hop_min_eigenvalue=float(np.linalg.eigvalsh(h1).min()),
                    uniform_input_lower_bound=uniform_injection,
                    irreducible_noncommuting_component=noncomm_remainder,
                    normalized_commutator=float(np.linalg.norm(k@l-l@k)/(np.linalg.norm(k)*np.linalg.norm(l))),
                    normalized_projected_commutator=float(np.linalg.norm((p@k@p)@l-l@(p@k@p))/(np.linalg.norm(k)*np.linalg.norm(l))),
                    uniform_height_output_range=float(np.ptp(k@np.ones(14))),
                    soft_edge_projection_norm=soft,soft_alt_step_projection_norm=soft_alt),
                gradient_Gibbs_unit_edge=dict(rank=13,edge_projector_diagonal=float(projector.diagonal().mean()),
                                              source_norm=float(np.linalg.norm(m.T@(projector.diagonal()[:,None]*b.T)))),
                actual_material_spectral_weights=bands,
                observed_material_mode_rank_sum=sum(g["edge_weight_rank"] for g in bands),
                native_gradient_oscillator_dimension=13,
                caveat="The positive two-hop metric exactly matches only the group-averaged conventional K, which has zero proxy source. Actual K fits remain target-exposed and cannot match exactly with symmetric vertex H_v and H_e=I. Full native edge/cycle dynamics or new constitutive laws are not excluded.")


if __name__ == "__main__":
    result = main()
    (HERE/"METRIC_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
