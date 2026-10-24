#!/usr/bin/env python3
"""Bound passive cross-mode loss using archived graphite modal pair weights."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAP = ROOT / "artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures"
SPEC = CAP / "2026-10-23T023854Z-codex-graphite-finite-spectrum-4c8b18e3-68bdd1a3-441a-4a35-ac05-a26af9803d0c"
SWEEP = CAP / "2026-10-23T024735Z-codex-graphite-loss-load-60d8705c-babb19e4-d2fd-435f-abd7-86602cecf7fc"

rows_out = []
for cutoff in (14, 16, 18):
    spectrum = json.loads((SPEC / f"FINITE_HEIGHT_SPECTRUM_{cutoff}A.json").read_text())
    sweep = json.loads((SWEEP / f"PRESSURE_LOSS_{cutoff}A_RESULTS.json").read_text())
    modes = {int(r["mode"]): r for r in spectrum["mode_rows"]}
    mass = sum(r["height_stiffness_mev_per_a2_per_mean_atom"] /
               (2 * math.pi * r["illustrative_12C_frequency_THz"]) ** 2
               for r in modes.values()) / len(modes)
    assert all(math.isclose(r["height_stiffness_mev_per_a2_per_mean_atom"] /
                            (2 * math.pi * r["illustrative_12C_frequency_THz"]) ** 2,
                            mass, rel_tol=1e-10) for r in modes.values())
    pair = [sum(modes[j]["scalar_rayleigh_coefficient_per_unit_d"] for j in indices)
            for indices in ((5, 6), (8, 9))]
    assert math.isclose(sum(pair), spectrum["scalar_rayleigh_coefficient_per_unit_d"], rel_tol=1e-10)
    # Each normalized dissipative FWHM is one THz; this is a transfer coefficient,
    # not an asserted physical linewidth or a measured kinetic friction.
    coeff = [2 * math.pi * mass * a for a in pair]
    diag = sum(coeff)
    cross = 2 * math.sqrt(math.prod(coeff))
    # Analytic extremizers: pair maps B_i=sqrt(a_i) I_2 and the 4x4 Rayleigh
    # block [[d_L I, rho sqrt(d_L d_H) I], [rho sqrt(d_L d_H) I, d_H I]].
    # With d_L=d_H=2*pi*m_eff, eigenvalues are d*(1 +/- rho), each twice.
    extremizers = []
    for rho in (-1., 0., 1.):
        eigenvalues = [2 * math.pi * mass * (1-rho)]*2 + [2 * math.pi * mass * (1+rho)]*2
        drag = diag + rho*cross
        assert min(eigenvalues) >= -1e-14 and drag >= 0
        extremizers.append({"rho": rho, "rayleigh_eigenvalues": eigenvalues,
                            "drag_per_normalized_THz_width": drag})
    ps = {}
    for row in sweep["rows"]:
        p = row["delta_pressure_MPa"]
        if p not in (-2.5, 0., 2.5):
            continue
        a = [sum(mode[2] for mode in row["active_modes"] if mode[0] in ids)
             for ids in ((5, 6), (8, 9))]
        c = [2*math.pi*mass*v for v in a]
        center = sum(c)
        half_range = 2*math.sqrt(math.prod(c))
        ps[p] = {"diagonal": center, "passive_min": center-half_range,
                 "passive_max": center+half_range, "cross_half_range": half_range}
    assert math.isclose(ps[0.]["diagonal"], diag, rel_tol=1e-9)
    rows_out.append({"cutoff_angstrom":cutoff, "pair_coefficients_per_THz":coeff,
                     "diagonal_equal_width_coefficient":diag,
                     "cross_half_range_per_THz":cross,
                     "cross_fraction_of_diagonal":cross/diag,
                     "bounds_per_THz_equal_width":[diag-cross, diag+cross],
                     "extremizers":extremizers,
                     "pressure_pointwise_envelopes_equal_constant_width":ps})

print(json.dumps({"evidence":"EXACT conditional PSD bound; NUMERICAL archived coefficients",
                  "units":"meV ps Angstrom^-2 per upper atom per THz of dissipative FWHM",
                  "law":"(sqrt(c_L Delta_f_L)-sqrt(c_H Delta_f_H))^2 <= gamma <= (sqrt(c_L Delta_f_L)+sqrt(c_H Delta_f_H))^2",
                  "interpretation":"Envelope only: a pressure-varying cross loss has no derivative bound from diagonal linewidths alone",
                  "results": rows_out}, indent=2))
