#!/usr/bin/env python3
"""Parity-compatible Gaussian surrogate and unit-clock obstruction.

All numerical matrices are the prior registered conventional KC model. No
native packet/material identification or experimentally calibrated damping.
"""
import json
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT / "graphite-registry-defect-source"))
from audit_registry_defect import carrier, permutations  # noqa: E402

MATCHED = PARENT / "graphite-matched-hessian-reconstruction" / "MATCHED_HESSIAN_RESULTS.json"
PROXY = PARENT / "graphite-matched-hessian-reconstruction" / "BOND_PROXY_RESULTS.json"


def matrices():
    matched = json.loads(MATCHED.read_text())
    k = np.asarray(matched["K"], dtype=float)
    pairs, b, m = carrier()
    assert k.shape == (14, 14) and b.shape == (14, 21)
    assert np.linalg.eigvalsh(k).min() > 0
    assert np.linalg.matrix_rank(b) == 13
    assert np.array_equal(np.diag(b.T @ b), 2*np.ones(21, dtype=int))
    assert np.array_equal(b @ m, np.zeros((14,2)))
    l = b @ b.T
    eye = np.eye(14, dtype=int)
    assert np.array_equal(l @ (l-6*eye) @ ((l-3*eye)@(l-3*eye)-2*eye), np.zeros((14,14), dtype=int))
    group = permutations(pairs, b)
    kb = sum(p @ k @ p.T for p, _, _, _ in group) / len(group)
    return matched, k, kb, b, m


def best_scalar_clock(k, b):
    """Necessary B^T K=c B^T L condition for scalar-clock native y dynamics."""
    l = b @ b.T
    x, z = b.T @ k, b.T @ l
    c = float(np.vdot(x, z) / np.vdot(z, z))
    return dict(best_c=float(c), relative_operator_defect=float(np.linalg.norm(x-c*z)/np.linalg.norm(x)),
                c_units="meV/Angstrom^2 per upper atom; equals m/(14 tau^2) in consistently calibrated physical units")


def covariance_replay(k, b):
    # Numerical convention m=1, Theta_bar=1, hence kBT=14, with arbitrary
    # consistent mass/time units. This fixes no physical mass or time.
    eig, u = np.linalg.eigh(k)
    root_inv = (u / np.sqrt(eig)) @ u.T
    inv = (u / eig) @ u.T
    c0 = b.T @ inv @ b
    ymap = b.T @ root_inv / np.sqrt(14.0)
    assert np.linalg.norm(ymap @ (14*np.eye(14)) @ ymap.T-c0) < 1e-12
    times = [0.0, 0.001, 0.005, 0.01]
    errors = []
    cross_norms = []
    for t in times:
        cos = (u * np.cos(np.sqrt(14*eig)*t)) @ u.T
        sin = (u * np.sin(np.sqrt(14*eig)*t)) @ u.T
        # Exact harmonic Gibbs correlations for q=B^T h and odd y=B^T K^-1/2 p/sqrt(14m).
        qq = b.T @ inv @ cos @ b
        yy = b.T @ root_inv @ cos @ root_inv @ b
        qy = b.T @ inv @ sin @ b
        errors.append(float(np.linalg.norm(qq-yy)))
        cross_norms.append(float(np.linalg.norm(qy)))
    # Equilibrium Langevin extension: dp=-14Kh dt-(d/m)p dt+sqrt(2 kBT d)dW.
    # For isotropic dI, the y autocovariance initial right derivative is
    # -(d/m) C0, while the q autocovariance derivative is exactly zero.
    d_over_m = 1.0  # a unit coefficient check, not a physical loss calibration
    yy_derivative = ymap @ (-d_over_m*14*np.eye(14)) @ ymap.T
    qq_derivative = np.zeros_like(c0)
    assert np.linalg.norm(yy_derivative+c0) < 1e-12
    # Independently finite-difference the full 28-state damped drift propagator.
    drift = np.block([[np.zeros_like(k), np.eye(14)], [-14*k, -np.eye(14)]])
    thermal_cov = np.block([[inv, np.zeros_like(k)], [np.zeros_like(k), 14*np.eye(14)]])
    dt = 1e-8  # arbitrary normalized time, not a physical linewidth
    cross = expm(drift*dt) @ thermal_cov
    cq_t = b.T @ cross[:14, :14] @ b
    cy_t = ymap @ cross[14:, 14:] @ ymap.T
    q_slope_error = float(np.linalg.norm((cq_t-c0)/dt)/np.linalg.norm(c0))
    y_slope_error = float(np.linalg.norm((cy_t-c0)/dt+c0)/np.linalg.norm(c0))
    assert q_slope_error < 1e-3 and y_slope_error < 1e-3
    return dict(bond_covariance_trace_per_Theta_bar=float(np.trace(c0)),
                bond_variance_minmax_per_Theta_bar=[float(c0.diagonal().min()), float(c0.diagonal().max())],
                normalized_time_points=times, harmonic_qq_yy_max_frobenius_difference=float(max(errors)),
                harmonic_qy_cross_norms=cross_norms,
                isotropic_damping_right_derivative=dict(C_qq_norm_per_d_over_m=float(np.linalg.norm(qq_derivative)),
                    C_yy_plus_C0_norm_per_d_over_m=float(np.linalg.norm(yy_derivative+c0)),
                    negative_C_yy_trace_per_d_over_m=float(-np.trace(yy_derivative)),
                    full_drift_finite_difference_relative_errors=dict(q_zero_slope=q_slope_error,
                                                                        y_negative_C0_slope=y_slope_error)))


def main():
    matched, k, kb, b, m = matrices()
    prior = json.loads(PROXY.read_text())
    out = dict(evidence="EXACT conditional harmonic/Gibbs and parity identities; NUMERICAL conventional model replay; no physical loss calibration",
               definitions="E_total=7 h^T K h+p^T p/(2m); q=B1^T h even; y*=B1^T K^-1/2 p/sqrt(14m) odd; Theta_bar=kBT/14",
               physical_map_status="HYPOTHESIS y_native=y*/ell with free length ell; this is a Gaussian surrogate, not the native packet dynamics",
               uniform_local_momentum_null="For y_local=a B1^T p with identical site mass, diagonal covariance is 2 a^2 m kBT on all 21 edges; S=0 by B1 M=0",
               carrier=dict(vertices=14,edges=21,rank_B1=13,dimension_gradient_edge_subspace=13,edge_cycle_kernel_dimension=8),
               actual_clock=best_scalar_clock(k,b),group_mean_clock=best_scalar_clock(kb,b),
               group_mean_laplacian_eigenvalues=np.linalg.eigvalsh(b@b.T).tolist(),
               group_mean_K_eigenvalues=np.linalg.eigvalsh(kb).tolist(),
               gaussian_replay=covariance_replay(k,b),
               pressure_clock_rows=[dict(delta_pressure_MPa=row["delta_pressure_MPa"],**best_scalar_clock(np.asarray(row["K"]),b)) for row in matched["pressure_rows"]],
               physical_loss_gate="The d/m derivative is symbolic per unit assumed isotropic Rayleigh loss. Native H=I one-clock dynamics cannot reproduce matched material K on gradient edges. Measured D, FDT bath, ell, force/contact and packet action remain open.")
    assert abs(out["gaussian_replay"]["bond_variance_minmax_per_Theta_bar"][0]-prior["edge_weight_minmax"][0]) < 1e-12
    assert abs(out["gaussian_replay"]["bond_variance_minmax_per_Theta_bar"][1]-prior["edge_weight_minmax"][1]) < 1e-12
    return out


if __name__ == "__main__":
    result = main()
    (HERE / "QUADRATURE_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
