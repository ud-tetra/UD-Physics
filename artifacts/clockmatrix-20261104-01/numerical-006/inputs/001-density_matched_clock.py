"""Match local stock histories by a single preparation amplitude adjustment."""
from itertools import product
import json
import numpy as np

from isospectral_clock import replay
from tracked_current_clock import D, HORIZON, dispersion, site_rule


def histories(order, step):
    _, weights = np.polynomial.legendre.leggauss(order)
    gauss = weights[:, None, None] * weights[None, :, None] * weights[None, None, :]
    offsets = np.array([r for r in product(range(-12, 13), repeat=3)
                        if sum(x*x for x in r) <= 144])
    unit_stock = 10**8 / (2 * (2 * np.pi)**3 * 20 * 100**2)

    def probe(k, probability):
        omega, velocity = dispersion(k)
        v = np.array([np.sum(probability * component) for component in velocity])
        center = np.rint(HORIZON * v).astype(int)
        points = offsets + center
        neighbors = np.vstack((points, (points[:, None, :] + D).reshape(-1, 3),
                               (points[:, None, :] - D).reshape(-1, 3)))
        positions, index = np.unique(neighbors, axis=0, return_inverse=True)
        n = len(points)
        sites, head, tail = np.split(index, [n, 8*n])
        head, tail = head.reshape(n, 7), tail.reshape(n, 7)
        jacobian = 2 * omega * (sum(velocity) if np.mean(k[1]) > 0.5 else velocity[0])
        amplitude = np.sqrt(probability * gauss / jacobian).ravel()
        basis = np.exp(1j * (positions @ np.array([axis.ravel() for axis in k])))
        omega = omega.ravel()
        stocks, normalized_rates, phases = [], [], np.zeros(n)
        previous = None
        for time in np.linspace(0, HORIZON, round(HORIZON / step) + 1):
            wave = amplitude * np.exp(-1j * omega * time)
            stock, normalized_rate = site_rule(basis @ wave, basis @ (-1j * wave / omega),
                                               sites, head, tail)
            stock *= unit_stock
            stocks.append(stock)
            normalized_rates.append(normalized_rate)
            rate = normalized_rate * stock**2
            if previous is not None:
                phases += step * (previous + rate) / 2
            previous = rate
        return np.array(stocks), np.array(normalized_rates), phases, center.tolist()

    result = replay(order, probe)
    return result["axis"]["probe"], result["diagonal"]["probe"]


def run():
    rows = []
    for order, step in ((8, 1/4), (12, 1/8)):
        (axis, _, phase_a, center_a), (diagonal, rate_d, phase_d, center_d) = histories(order, step)
        # Fit only densities. Linear propagation makes this equivalent to
        # rescaling the diagonal launch amplitude by sqrt(stock_scale).
        stock_scale = np.sum(axis * diagonal) / np.sum(diagonal**2)
        residual = stock_scale * diagonal - axis

        def phase(stock, angles):
            return float(np.angle(np.dot(stock[-1], np.exp(1j * angles))))

        raw = phase(diagonal, phase_d) - phase(axis, phase_a)
        adjusted = phase(diagonal, phase_d * stock_scale**2) - phase(axis, phase_a)
        common_density_rate = rate_d * axis**2
        common_density_phase = step * (common_density_rate[1:] + common_density_rate[:-1]).sum(axis=0) / 2
        counterfactual = phase(axis, common_density_phase) - phase(axis, phase_a)
        rows.append({"order": order, "time_step": step, "centers": [center_a, center_d],
                     "diagonal_stock_scale": float(stock_scale),
                     "max_relative_stock_mismatch": float(np.max(abs(residual) / axis)),
                     "relative_l2_stock_mismatch": float(np.linalg.norm(residual)
                                                        / np.linalg.norm(axis)),
                     "unmatched_split_rad": raw, "density_matched_split_rad": adjusted,
                     "common_density_counterfactual_split_rad": counterfactual})
        assert raw < 0 < adjusted
    return rows


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
