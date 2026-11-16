"""Reduce signed AW5 bench shots under supplied uncertainty certificates."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm, logm

H = 1/8
RADIUS = 1/4
TARGET = np.array([[-1/1024, -1], [1, 0]])
SHOT_IDS = ("+e1", "-e1", "+e2", "-e2")


def finite(value, shape):
    array = np.asarray(value, dtype=float)
    if array.shape != shape or not np.isfinite(array).all():
        raise ValueError(f"Expected finite values of shape {shape}")
    return array


def bound(value):
    result = float(finite(value, ()))
    if result < 0:
        raise ValueError("Uncertainty bounds must be nonnegative")
    return result


def norm(matrix):
    return float(np.linalg.norm(matrix, ord=2))


def assess(packet):
    try:
        evidence = packet["evidence"]
        if packet["protocol"] != "AW5-PAIR-v1" or evidence not in ("SYNTHETIC", "MEASURED"):
            raise ValueError("Unsupported protocol or evidence label")
        cert = packet["certificate"]
        for key in ("clock_reference", "endpoint_uncertainty", "lti_scope", "loss_model"):
            if not isinstance(cert[key], str) or not cert[key].strip():
                raise ValueError(f"Missing certificate reference: {key}")
        g_limit = bound(cert["generator_norm_upper"])
        if g_limit > 3/2:
            raise ValueError("Generator prior exceeds the declared logarithm scope")
        timing = packet["timing"]
        axis = finite(timing["midpoint_times_ms"], (256,))
        nominal = (np.arange(256)+0.5)/8
        timing_error = float(np.max(np.abs(axis-nominal)))+bound(timing["uncertainty_ms"])

        shots = packet["shots"]
        if set(shots) != set(SHOT_IDS):
            raise ValueError("Exactly four signed basis shots required")
        arrays = [finite(shots[key], (2, 2)) for key in SHOT_IDS]
        pair1, pair2 = (arrays[0]-arrays[1])/2, (arrays[2]-arrays[3])/2
        X = np.column_stack((pair1[0], pair2[0]))
        Y = np.column_stack((pair1[1], pair2[1]))
        dx, dy = bound(cert["delta_x"]), bound(cert["delta_y"])
        numerical_map = bound(cert["map_numerical_allowance"])
        numerical_generator = bound(cert["generator_numerical_allowance"])
        denominator = float(np.linalg.svd(X, compute_uv=False)[-1])-dx
        if denominator <= 0:
            raise ValueError("Initial-state conditioning is uncertifiable")
        M = np.linalg.solve(X.T, Y.T).T
        epsilon = (dy+norm(M)*dx)/denominator+numerical_map
        if norm(M-np.eye(2))+epsilon > RADIUS:
            raise ValueError("Transition is outside the certified logarithm radius")
        logarithm = logm(M)/H
        if not np.isfinite(logarithm).all() or np.iscomplexobj(logarithm):
            raise ValueError("Computed logarithm failed the real finite model check")
        G = logarithm
        rho = epsilon/(H*(1-RADIUS))+numerical_generator
        off = float(max(abs(G[0, 1]+1), abs(G[1, 0]-1)))+rho
        upper_sym = float(np.linalg.eigvalsh((G+G.T)/2)[-1])+rho
        gamma = float(G[1, 1]-G[0, 0])
        gates = {"timing_loopback": timing_error <= 1/1024,
                 "generator": norm(G-TARGET)+rho <= 1/4096,
                 "signed_coefficients": off <= 1/49152,
                 "dissipativity": upper_sym <= 0,
                 "selective_loss": gamma-2*rho >= 0 and gamma+2*rho <= 1/512}

        heldout = packet["heldout"]
        if not isinstance(heldout, list) or len(heldout) < 2:
            raise ValueError("At least two held-out state comparisons are required")
        residuals = []
        for shot in heldout:
            t = float(finite(shot["time_native"], ()))
            if not 0 < t <= 32:
                raise ValueError("Held-out time outside the observation window")
            start = finite(shot["start"], (2,))
            end = finite(shot["end"], (2,))
            residual = norm(expm(t*G)@start-end)
            # A contractive fitted generator and a certified contractive true
            # generator permit the linear Duhamel bound.
            limit = (bound(shot["start_error"])+bound(shot["end_error"])
                     +t*rho*norm(start)+bound(shot["numerical_allowance"]))
            residuals.append({"time_native": t, "residual": residual, "bound": limit,
                              "pass": residual <= limit})
        gates["heldout"] = bool(gates["dissipativity"] and all(item["pass"] for item in residuals))
        return {"status": "PASS_CONDITIONAL" if all(gates.values()) else "FAIL_GATES",
                "scope": evidence, "generator_estimate": G.tolist(), "transition_error_upper": epsilon,
                "generator_error_upper": rho, "loopback_error_ms": timing_error,
                "selective_loss_interval": [gamma-2*rho, gamma+2*rho],
                "gates": gates, "heldout": residuals, "physical_promotion": 0}
    except (KeyError, TypeError, ValueError, OverflowError, np.linalg.LinAlgError) as exc:
        return {"status": "INADMISSIBLE", "reason": str(exc), "physical_promotion": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    path = parser.parse_args().packet
    raw = path.read_bytes()
    try:
        result = assess(json.loads(raw))
    except (UnicodeError, json.JSONDecodeError) as exc:
        result = {"status": "INADMISSIBLE", "reason": str(exc), "physical_promotion": 0}
    result["packet_sha256"] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
