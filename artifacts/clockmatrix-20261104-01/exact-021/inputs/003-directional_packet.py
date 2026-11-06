"""Numerical vertex-lane packet transport and moving phase readout."""
from itertools import product
import json
import numpy as np


DIRECTIONS = [d for d in product((0, 1), repeat=3) if any(d)]
WIDTH = 0.18
CUTOFF = 0.65
TIMES = (0, 4, 8, 12)


def dispersion(k):
    squared = sum(2 * (1 - np.cos(sum(a * b for a, b in zip(k, d))))
                  for d in DIRECTIONS)
    omega = np.sqrt(squared)
    velocity = [sum(d[j] * np.sin(sum(a * b for a, b in zip(k, d)))
                    for d in DIRECTIONS) / np.where(omega > 0, omega, 1)
                for j in range(3)]
    return omega, velocity


def phase_difference(a, b):
    return float(np.angle(np.exp(1j * (a - b))))


def packet(size, sign, width=WIDTH):
    carrier = (sign * np.pi / 3, 0, 0)
    k = np.meshgrid(*(np.fft.fftfreq(size) * (2 * np.pi),) * 3,
                    indexing="ij", sparse=True)
    r = np.meshgrid(*(np.arange(size) - size // 2,) * 3,
                    indexing="ij", sparse=True)
    offset_sq = sum((axis - center)**2 for axis, center in zip(k, carrier))
    taper_coordinate = np.clip((np.sqrt(offset_sq) - 0.45) / (CUTOFF - 0.45), 0, 1)
    taper = (1 + np.cos(np.pi * taper_coordinate)) / 2
    spectrum = np.exp(-offset_sq / (2 * width**2)) * taper
    weights = spectrum**2
    omega, velocity = dispersion(k)
    spectral_velocity = [float(np.sum(weights * component) / np.sum(weights))
                         for component in velocity]
    carrier_omega, _ = dispersion(carrier)
    demodulator = np.exp(-1j * sum(a * b for a, b in zip(carrier, r)))
    observations = []
    for time in TIMES:
        field = np.fft.fftshift(np.fft.ifftn(spectrum * np.exp(-1j * omega * time)))
        stock = np.abs(field)**2
        total = np.sum(stock)
        center = [float(np.sum(stock * axis) / total) for axis in r]
        radius_sq = sum((axis - mean)**2 for axis, mean in zip(r, center))
        window = np.exp(-radius_sq / (2 * 6**2))
        port = np.sum(window * field * demodulator)
        local_phase = np.angle(port) + sum(a * b for a, b in zip(carrier, center))
        observations.append({
            "s": time,
            "centroid": center,
            "fraction_in_radius_12": float(np.sum(stock[radius_sq <= 12**2]) / total),
            "phase_coherence": float(abs(port) / np.sum(window * np.abs(field))),
            "phase_residual_rad": phase_difference(
                local_phase, -carrier_omega * time + sum(a * b for a, b in zip(carrier, center))),
            "centroid_residual_norm": float(np.linalg.norm(
                np.array(center) - np.array(spectral_velocity) * time)),
        })
    return {"grid": size, "carrier_sign": sign, "width": width, "spectral_velocity": spectral_velocity,
            "observations": observations}


def run():
    forward, enlarged, reverse = packet(65, 1), packet(97, 1), packet(65, -1)
    for direct, mirrored in zip(forward["observations"], reverse["observations"]):
        assert np.linalg.norm(np.array(direct["centroid"]) + mirrored["centroid"]) < 1e-8
        assert abs(direct["phase_residual_rad"] - mirrored["phase_residual_rad"]) < 1e-8
    return [forward, enlarged, reverse, packet(97, 1, 0.12)]


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
