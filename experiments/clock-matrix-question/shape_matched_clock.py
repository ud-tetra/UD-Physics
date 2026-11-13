"""Same-spectrum chirp controls for the density-matched polynomial clock."""
import json
import numpy as np

from density_matched_clock import histories


def run():
    reports = []
    for order, step in ((8, 1/4), (12, 1/8)):
        (base, rate_base, phase_base, _), _ = histories(order, step)
        rows = []
        for chirp in (-2, 2):
            (stock, rate, site_phase, _), _ = histories(order, step, chirp)
            scale = np.sum(base * stock) / np.sum(stock**2)
            residual = scale * stock - base

            def phase(weights, angles):
                return float(np.angle(np.dot(weights, np.exp(1j * angles))))

            def integrate(local_rate):
                return step * (local_rate[1:] + local_rate[:-1]).sum(axis=0) / 2

            nominal = phase(base[-1], phase_base)
            fitted = phase(stock[-1], site_phase * scale**2)
            common = phase(base[-1], integrate(rate * base**2))
            assert abs(nominal - phase(base[-1], integrate(rate_base * base**2))) < 1e-14
            rows.append({"chirp": chirp, "stock_scale": float(scale),
                         "relative_l2_mismatch": float(np.linalg.norm(residual) / np.linalg.norm(base)),
                         "maximum_relative_mismatch": float(np.max(abs(residual) / base)),
                         "matched_phase_delta_rad": fitted - nominal,
                         "common_density_counterfactual_delta_rad": common - nominal})
        reports.append({"order": order, "step": step, "rows": rows})
    for first, second in zip(reports[0]["rows"], reports[1]["rows"], strict=True):
        key = "common_density_counterfactual_delta_rad"
        assert abs(first[key] - second[key]) < 0.1 * abs(second[key])
    return reports


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
