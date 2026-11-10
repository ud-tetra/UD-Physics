#!/usr/bin/env python3
"""Finite-window, endpoint-corrected UD phase: exact bounds + constructor probes.

Mathematical toy: three orthogonal J-complex sectors, fixed weights
(1/4,1/4,1/2), local generators with gains (1,1,3/2)+delta.
The unit-normalized overlap is sum(r_j exp(i*2*g_j*T)).
No physical clock, apparatus, or independent measurement is assumed.
"""
import argparse
from fractions import Fraction as F
from itertools import product
from math import atan2, cos, hypot, pi, sin
from pathlib import Path
import json

R = (F(1, 4), F(1, 4), F(1, 2))
G0 = (F(1), F(1), F(3, 2))
EPS = F(1, 100)


def check():
    assert sum(R) == 1
    assert sum(a*b for a, b in zip(R, G0)) == F(5, 4)
    # T=2*pi gives baseline phase -1 and common endpoint rotation +1.
    assert tuple(4*g for g in G0) == (F(4), F(4), F(6))
    # The rational pi upper bound is deliberately one-sided.
    B = F(44, 175)  # 8*pi*EPS < 8*(22/7)*EPS
    v_lower = F(1) - F(22, 175)**2/F(2)
    phase_upper = B**3/(6*(1 - B**2/F(2)))
    assert v_lower > F(99, 100)
    assert phase_upper < F(1, 100)
    samples = []
    largest_phase = 0.0
    smallest_visibility = 1.0
    errors = (-EPS, -EPS/2, F(0), EPS/2, EPS)
    for delta in product(errors, repeat=3):
        angles = [4*pi*float(d) for d in delta]
        mean = sum(float(r)*a for r, a in zip(R, angles))
        # Removing the mean implements dynamical-phase/endpoint correction.
        z_re = sum(float(r)*cos(a-mean) for r, a in zip(R, angles))
        z_im = sum(float(r)*sin(a-mean) for r, a in zip(R, angles))
        visibility = hypot(z_re, z_im)
        shift = atan2(z_im, z_re)
        assert visibility >= float(v_lower) - 3e-15
        assert abs(shift) <= float(phase_upper) + 3e-15
        smallest_visibility = min(smallest_visibility, visibility)
        largest_phase = max(largest_phase, abs(shift))
        if delta in ((F(0), EPS, F(0)), (-EPS, -EPS, EPS)):
            samples.append({
                "gain_errors": [str(d) for d in delta],
                "visibility": visibility,
                "corrected_phase_change_radians": shift,
                "first_order_uncorrected_shift_radians": -mean,
            })
    # Former exact-return discontinuity is not a finite-window discontinuity.
    challenges = []
    for n in (101, 1001, 10001):
        theta = 4*pi/n
        re, im = 3/4 + cos(theta)/4, sin(theta)/4
        phase_shift = atan2(im, re) - theta/4
        visibility = hypot(re, im)
        assert visibility > float(v_lower) and abs(phase_shift) < float(phase_upper)
        challenges.append({
            "odd_N": n, "gain2_error": f"1/{n}",
            "visibility_at_T_2pi": visibility,
            "open_path_phase_shift_radians": phase_shift,
            "minimal_exact_ray_period_over_pi": 2*n,
            "exact_recurrence_phase": "+1",
            "reference_phase": "-1",
        })
    return {
        "status": "PASS",
        "evidence": ["EXACT", "CONDITIONAL", "NUMERICAL"],
        "reference_weights": [str(x) for x in R],
        "reference_gains": [str(x) for x in G0],
        "window": "T=2*pi, dimensionless",
        "uncertainty": "|delta_gj|<=1/100 independently, including g1 != g2",
        "visibility_lower_rational": str(v_lower),
        "visibility_lower_decimal": float(v_lower),
        "phase_error_upper_rational": str(phase_upper),
        "phase_error_upper_radians": float(phase_upper),
        "target_visibility_floor": "99/100",
        "target_phase_error_ceiling_radians": "1/100",
        "sampled_gain_triples": len(errors)**3,
        "sample_min_visibility": smallest_visibility,
        "sample_max_abs_phase_shift_radians": largest_phase,
        "sample_detail": samples,
        "odd_N_challenges": challenges,
        "conventions": "J multiplication by +i; Euclidean sector metric; zero physical calibration",
        "claim_scope": "All independent errors in the closed box, analytic bounds; fixed state weights",
        "limits": "No device, no noise model, no measured time, no rate-selection mechanism",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = check()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "sampled_gain_triples": result["sampled_gain_triples"],
        "visibility_lower_rational": result["visibility_lower_rational"],
        "phase_error_upper_rational": result["phase_error_upper_rational"],
    }, sort_keys=True))
