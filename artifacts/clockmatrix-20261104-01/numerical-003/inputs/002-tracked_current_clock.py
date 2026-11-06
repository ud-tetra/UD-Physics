"""Integrate site-clock residuals and read them in moving stock windows."""
from itertools import product
import json
import numpy as np

from directional_packet import DIRECTIONS, dispersion
from isospectral_clock import replay


D = np.array(DIRECTIONS)
HORIZON = 12


def site_rule(u, potential, sites, head, tail):
    # The potential has Fourier multiplier -i/omega.
    vertex = u[sites]
    edge_out = potential[head] - potential[sites, None]
    edge_in = potential[sites, None] - potential[tail]
    others = abs(u[head])**2 + abs(u[tail])**2
    stock = ((2 * abs(vertex[:, None])**2 + others) / 14
             + abs(edge_out)**2 + abs(edge_in)**2).sum(axis=1) / 2
    outgoing = np.real((vertex[:, None] + u[head]).conj() * edge_out)
    incoming = np.real((u[tail] + vertex[:, None]).conj() * edge_in)
    current = ((outgoing + incoming) / 2) @ D
    norm_sq = (current**2).sum(axis=1) / 2 - current.sum(axis=1)**2 / 8
    normalized = np.divide(norm_sq, stock**2, out=np.zeros_like(stock), where=stock > 0)
    return stock, normalized / 128


def integrate(field, sites, head, tail, windows, step, total_stock):
    phase = np.zeros(len(sites))
    samples = []
    previous = None
    for index in range(round(HORIZON / step) + 1):
        time = index * step
        stock, rate = site_rule(*field(time), sites, head, tail)
        if previous is not None:
            phase += step * (previous + rate) / 2
        previous = rate
        if time % 4 == 0:
            sample = []
            for window in windows(time):
                weights = stock * window
                contrast = np.dot(weights, np.exp(1j * phase)) / weights.sum()
                sample.append({"phase_rad": float(np.angle(contrast)),
                               "contrast": float(abs(contrast)),
                               "stock_fraction": float(weights.sum() / total_stock)})
            samples.append({"native_time": time, "ports": sample})
    return samples


def matched_probe(order, step, radii=(3,)):
    _, weights = np.polynomial.legendre.leggauss(order)
    outer_radius = max(radii)
    gauss = weights[:, None, None] * weights[None, :, None] * weights[None, None, :]

    def probe(k, probability):
        omega, velocity = dispersion(k)
        center_velocity = np.array([np.sum(probability * v) for v in velocity])
        diagonal = bool(np.mean(k[1]) > 0.5)
        jacobian = 2 * omega * (sum(velocity) if diagonal else velocity[0])
        assert np.all(jacobian > 0)
        amplitude = np.sqrt(probability * gauss / jacobian).ravel()
        omega = omega.ravel()
        wavevectors = np.array([axis.ravel() for axis in k])
        points = np.array(list(product(*(range(-outer_radius, int(v * HORIZON) + outer_radius + 2)
                                         for v in center_velocity))))
        if outer_radius > 3:
            covered = np.zeros(len(points), dtype=bool)
            for time in range(0, HORIZON + 1, 4):
                covered |= np.sum((points - time * center_velocity)**2, axis=1) <= outer_radius**2
            points = points[covered]
        offsets = np.vstack((points, (points[:, None, :] + D).reshape(-1, 3),
                             (points[:, None, :] - D).reshape(-1, 3)))
        positions, inverse = np.unique(offsets, axis=0, return_inverse=True)
        n = len(points)
        sites, head, tail = np.split(inverse, [n, 8 * n])
        basis = np.exp(1j * (positions @ wavevectors))
        def field(time):
            wave = amplitude * np.exp(-1j * omega * time)
            return basis @ wave, basis @ (-1j * wave / omega)

        def windows(time):
            distance_sq = np.sum((points - time * center_velocity)**2, axis=1)
            return [distance_sq <= radius**2 for radius in radii]

        total_stock = 2 * (2 * np.pi)**3 * 20 * 100**2
        return integrate(field, sites, head.reshape(n, 7), tail.reshape(n, 7),
                         windows, step, total_stock)

    result = replay(order, probe)
    return {key: result[key]["probe"] for key in ("axis", "diagonal")}


def counterflow(step, offset):
    size = 256
    sites = np.arange(size)
    k = 2 * np.pi * np.fft.fftfreq(size)
    omega, velocity = dispersion((k, 0, 0))
    distance = abs(k - np.pi / 3)
    f = np.exp(-distance**2 / (2 * 0.18**2)) * (distance < 0.65)
    speed = np.sum(f**2 * velocity[0]) / np.sum(f**2)
    forward = f * np.exp(1j * offset * k)
    spectrum = forward + forward[(-sites) % size]
    omega = np.where(omega > 0, omega, 1)
    head = (sites[:, None] + D[:, 0]) % size
    tail = (sites[:, None] - D[:, 0]) % size

    def field(time):
        wave = spectrum * np.exp(-1j * omega * time)
        return np.fft.ifft(wave), np.fft.ifft(-1j * wave / omega)

    def windows(time):
        center = speed * time - offset
        r = (sites + size // 2) % size - size // 2
        return [np.exp(-(r - sign * center)**2 / 72) for sign in (-1, 1)]

    total_stock = 2 * np.sum(abs(spectrum)**2) / size
    return integrate(field, sites, head, tail, windows, step, total_stock)


def run():
    records = []
    for order, step in ((8, 1 / 4), (12, 1 / 8)):
        matched = matched_probe(order, step)
        records.append({"order": order, "time_step": step, "matched": matched,
                        "overlapped_at_launch": counterflow(step, 0),
                        "separated_at_launch": counterflow(step, 12)})
    for record in records:
        a, d = (record["matched"][key][-1]["ports"][0] for key in ("axis", "diagonal"))
        assert d["phase_rad"] - a["phase_rad"] > 0.01
        assert min(a["contrast"], d["contrast"]) > 0.99
    return records


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
