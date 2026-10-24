#!/usr/bin/env python3
"""Replay archived graphite mode weights as conditional linewidth-to-drag coefficients."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAP = ROOT / "artifacts/graphpub-20261023-gpt6-4f9a/graphite-history-001/files/captures"
SPEC = CAP / "2026-10-23T023854Z-codex-graphite-finite-spectrum-4c8b18e3-68bdd1a3-441a-4a35-ac05-a26af9803d0c"
SWEEP = CAP / "2026-10-23T024735Z-codex-graphite-loss-load-60d8705c-babb19e4-d2fd-435f-abd7-86602cecf7fc"
out = []
for cutoff in (14, 16, 18):
    spec = json.loads((SPEC/f"FINITE_HEIGHT_SPECTRUM_{cutoff}A.json").read_text())
    sweep = json.loads((SWEEP/f"PRESSURE_LOSS_{cutoff}A_RESULTS.json").read_text())
    rows = {int(v["mode"]):v for v in spec["mode_rows"]}
    # Units: kappa [meV / A^2 per upper atom], f [cycles / ps],
    # m_eff [meV ps^2 / A^2 per upper atom]. Infer from archived f and kappa.
    inferred_masses = [r["height_stiffness_mev_per_a2_per_mean_atom"]/
                       (2*math.pi*r["illustrative_12C_frequency_THz"])**2
                       for r in rows.values()]
    mass = sum(inferred_masses)/len(inferred_masses)
    assert max(abs(m-mass) for m in inferred_masses)/mass < 1e-10
    a = {j:rows[j]["scalar_rayleigh_coefficient_per_unit_d"] for j in rows}
    assert math.isclose(sum(a.values()),spec["scalar_rayleigh_coefficient_per_unit_d"],rel_tol=1e-11)
    assert all(math.isclose(a[j],rows[j]["lateral_coupling_squared"]/
                            (2*rows[j]["height_stiffness_mev_per_a2_per_mean_atom"]**2),rel_tol=1e-11)
               for j in rows)
    low = a[5]+a[6]
    high = a[8]+a[9]
    omitted = sum(a.values())-low-high
    assert omitted >= -1e-15 and abs(omitted) < 1e-15
    assert math.isclose(sum(r["isotropic_static_softening_mev_per_a2_per_mean_atom"] for r in rows.values()),
                        spec["static_softening_scalar"],rel_tol=1e-11)
    pressure = {r["delta_pressure_MPa"]:r for r in sweep["rows"]}
    def weights(p):
        mode = {int(n):q for n,_,q in pressure[p]["active_modes"]}
        return mode[5]+mode[6],mode[8]+mode[9]
    p0 = weights(0.0)
    slopes = [(y-x)/5.0 for x,y in zip(weights(-2.5),weights(2.5))]
    assert all(math.isclose(x,y,rel_tol=1e-9) for x,y in zip(p0,(low,high)))
    assert math.isclose(sum(slopes),sweep["centered_slopes"][0]["scalar_slope_per_MPa"],rel_tol=1e-9)
    transfer = [2*math.pi*mass*v for v in p0]
    derivative = [2*math.pi*mass*v for v in slopes]
    out.append({
        "cutoff_angstrom":cutoff,
        "mass_eff_meV_ps2_per_A2_per_upper_atom":mass,
        "mode_pair_frequencies_THz":[(rows[5]["illustrative_12C_frequency_THz"]+rows[6]["illustrative_12C_frequency_THz"])/2,
                                     (rows[8]["illustrative_12C_frequency_THz"]+rows[9]["illustrative_12C_frequency_THz"])/2],
        "per_unit_d_pair_weights":[low,high],
        "inactive_weight_absolute_upper_bound":abs(omitted),
        "low_pair_fraction_for_uniform_d":low/(low+high),
        "high_to_low_linewidth_ratio_for_equal_drag":transfer[0]/transfer[1],
        "drag_coefficients_meV_ps_per_A2_per_upper_atom_per_THz_FWHM":transfer,
        "drag_pressure_coefficients_per_MPa_per_THz_FWHM":derivative,
        "pair_log_weight_slopes_per_MPa":[slopes[i]/p0[i] for i in (0,1)],
        "uniform_width_log_drag_slope_per_MPa":sum(slopes)/sum(p0),
        "uniform_width_fractional_slope_needed_for_zero_drag_slope_per_MPa":-sum(slopes)/sum(p0),
        "static_softening_meV_per_A2_per_upper_atom":spec["static_softening_scalar"],
        "closed_finite_Ohmic_drag":spec["low_frequency_ohmic_coefficient_closed_finite_harmonic"]
    })
print(json.dumps({"status":"PASS_CONDITIONAL_ARCHIVED_SPECTRAL_REPLAY",
                  "linewidth_definition":"resolved dissipative power-spectrum FWHM in cycles/ps (THz), weak damping, D diagonal in conservative normal-mode basis",
                  "drag_formula":"gamma_scalar = sum_j a_j d_j; d_j = 2*pi*m_eff*Delta_f_j; gamma is per mean upper atom",
                  "pressure_formula":"gamma_prime = sum_j (a_j_prime*d_j + a_j*d_j_prime)",
                  "cutoff_results":out},indent=2))
