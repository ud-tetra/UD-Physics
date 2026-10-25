#!/usr/bin/env python3
"""Exact carrier automorphisms and numerical registry-defect decomposition.

The material interpretation q_e=h_B-h_A remains a declared hypothesis.
"""
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "graphite-matched-hessian-reconstruction" / "MATCHED_HESSIAN_RESULTS.json"
OUTPUT = HERE / "REGISTRY_DEFECT_RESULTS.json"


def carrier():
    pairs = [(i, k) for i in range(7) for k in range(7) if (i-k) % 7 in (0, 1, 5)]
    assert len(pairs) == 21
    b = np.zeros((14, 21), dtype=int)
    m = np.zeros((21, 2), dtype=float)
    vectors = {0: (0.5, 0.5), 1: (-0.5, 0.0), 5: (0.0, -0.5)}
    # Gram basis convention of the previous bond-proxy replay.
    for e, (i, k) in enumerate(pairs):
        b[i, e], b[7+k, e] = -1, 1
        m[e] = vectors[(i-k) % 7]
    assert np.array_equal(b @ m, np.zeros((14, 2)))
    assert set(pairs) == {(i, k) for i, k in json.loads(DATA.read_text())["aligned_bond_edges"]}
    return pairs, b, m


def permutations(pairs, b):
    edge_ids = {pair: e for e, pair in enumerate(pairs)}
    # T^t R^r: R(A_i)=A_(4i), R(B_k)=B_(4k-1), T shifts both by one.
    group = []
    for r in range(3):
        for t in range(7):
            def vertex(v):
                if v < 7:
                    return (pow(4, r, 7)*v+t) % 7
                k = v-7
                return 7+(pow(4, r, 7)*k-(pow(4, r, 7)-1)*pow(3, -1, 7)+t) % 7
            vp = [vertex(v) for v in range(14)]
            ep = [edge_ids[(vp[i], vp[7+k]-7)] for i, k in pairs]
            p = np.eye(14, dtype=int)[vp].T
            q = np.eye(21, dtype=int)[ep].T
            assert np.array_equal(p @ b, b @ q)
            group.append((p, q, vp, ep))
    assert len({tuple(g[2]) for g in group}) == 21
    assert len({g[3][0] for g in group}) == 21
    # Check the generators and the semidirect relation with exact integers.
    t, r = group[1][0], group[7][0]
    eye = np.eye(14, dtype=int)
    assert np.array_equal(np.linalg.matrix_power(t, 7), eye)
    assert np.array_equal(np.linalg.matrix_power(r, 3), eye)
    assert np.array_equal(r @ t @ r.T, np.linalg.matrix_power(t, 4))
    return group


def source(k, b, m):
    inv = np.linalg.inv(k)
    w = np.diag(b.T @ inv @ b)
    return w, m.T @ (w[:, None]*b.T)


def audit():
    data = json.loads(DATA.read_text())
    k = np.array(data["K"], dtype=float)
    assert k.shape == (14, 14) and np.min(np.linalg.eigvalsh(k)) > 0
    pairs, b, m = carrier()
    group = permutations(pairs, b)
    kb = sum(p @ k @ p.T for p, _, _, _ in group)/len(group)
    delta = k-kb
    w, s = source(k, b, m)
    wb, sb = source(kb, b, m)
    assert np.max(np.abs(kb-kb.T)) < 1e-10
    assert min(np.linalg.eigvalsh(kb)) > 0
    assert max(np.linalg.norm(p @ kb @ p.T-kb) for p, _, _, _ in group) < 1e-8
    assert np.ptp(wb) < 1e-12 and np.linalg.norm(sb) < 1e-12
    # Exact resolvent identity, with no small-defect assumption.
    inv, invb = np.linalg.inv(k), np.linalg.inv(kb)
    difference = -invb @ delta @ inv
    assert np.linalg.norm(inv-invb-difference) < 1e-12
    wr = np.diag(b.T @ difference @ b)
    sr = m.T @ (wr[:, None]*b.T)
    assert np.linalg.norm(s-sr) < 1e-12
    first = -invb @ delta @ invb
    sf = m.T @ (np.diag(b.T @ first @ b)[:, None]*b.T)
    lap = b @ b.T
    polynomial = np.stack([np.eye(14).ravel(), lap.ravel(), (lap @ lap).ravel()], axis=1)
    coeff = np.linalg.lstsq(polynomial, kb.ravel(), rcond=None)[0]
    discrepancy = np.linalg.norm(kb-(coeff[0]*np.eye(14)+coeff[1]*lap+coeff[2]*lap@lap))/np.linalg.norm(kb)
    original = json.loads((HERE.parent/"graphite-matched-hessian-reconstruction"/"BOND_PROXY_RESULTS.json").read_text())
    assert abs(np.linalg.norm(s)-np.linalg.norm(original["source_native"])) < 1e-12
    assert abs(w.mean()-original["edge_weight_mean"]) < 1e-12
    out = {
        "evidence": "EXACT carrier group; NUMERICAL conventional KC Hessian; CONDITIONAL assumed bond-height proxy",
        "group": "21 distinct T^t R^r; T^7=R^3=I, R T R^-1=T^4; one 21-edge orbit",
        "matched_input": str(DATA.relative_to(HERE.parent.parent)),
        "units": {"K": "meV/Angstrom^2 per upper atom", "w": "Angstrom^2/meV per Theta_bar", "S_native": "Angstrom^2/meV per Theta_bar"},
        "norm_delta_over_K": float(np.linalg.norm(delta)/np.linalg.norm(k)),
        "generator_defect_relative_F": {"T": float(np.linalg.norm(group[1][0]@k@group[1][0].T-k)/np.linalg.norm(k)), "R": float(np.linalg.norm(group[7][0]@k@group[7][0].T-k)/np.linalg.norm(k))},
        "minimum_eigenvalues": {"K": float(np.min(np.linalg.eigvalsh(k))), "group_mean_K": float(np.min(np.linalg.eigvalsh(kb)))},
        "bond_weight": {"original_mean": float(w.mean()), "original_cv": float(w.std()/w.mean()), "group_mean": float(wb.mean()), "group_range": float(np.ptp(wb))},
        "native_source": {"original_norm": float(np.linalg.norm(s)), "group_mean_norm": float(np.linalg.norm(sb)), "resolvent_recovery_error": float(np.linalg.norm(s-sr)), "first_order_relative_error": float(np.linalg.norm(s-sf)/np.linalg.norm(s)), "inverse_defect_operator_norm": float(np.linalg.norm(invb@delta, ord=2))},
        "numerical_polynomial_fit_only": {"coefficients_I_L_L2": coeff.tolist(), "relative_residual": float(discrepancy), "laplacian_eigenvalues": np.linalg.eigvalsh(lap).tolist()},
        "scope": "S=0 under full graph-symmetric group mean, and exact S is driven by K minus group mean within the assumed q_e proxy; no native map or measured friction inference"
    }
    return out


if __name__ == "__main__":
    result = audit()
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
