"""Local-current rate controls on a periodic axial lattice reduction."""
from fractions import Fraction as F
import json
import numpy as np

from directional_packet import DIRECTIONS, dispersion
from incidence_current import bond_stock_flow
from isospectral_clock import center_speeds_squared


def rates(u, edges):
    density = np.zeros_like(u.real)
    current = np.zeros((3, u.size))
    for d, edge in zip(DIRECTIONS, edges):
        head = np.roll(u, -d[0])
        tail_flow, head_flow = bond_stock_flow(u, head, edge)
        mass = (abs(u)**2 + abs(head)**2) / 14 + abs(edge)**2
        flow = (tail_flow - head_flow) / 2
        density += (mass + np.roll(mass, d[0])) / 2
        for index, step in enumerate(d):
            current[index] += step * (flow + np.roll(flow, d[0])) / 2
    stock = density.sum()
    assert np.isclose(stock, np.sum(abs(u)**2) + np.sum(abs(edges)**2))

    def metric_squared(vector):
        return (vector**2).sum(axis=0) / 2 - vector.sum(axis=0)**2 / 8

    local = np.divide(metric_squared(current), density, out=np.zeros_like(density),
                      where=density > 0).sum() / stock
    net = metric_squared(current.sum(axis=1) / stock)
    assert local + 1e-14 >= net
    return {"local_rate_increment": float(local / 128), "net_rate_increment": float(net / 128)}


def run():
    matched = [str(F(speed) / 128) for speed in center_speeds_squared()]
    stationary = []
    for parity in ((1, 0, 0), (1, 1, 1)):
        for d in DIRECTIONS:
            head = (-1)**sum(a * b for a, b in zip(parity, d))
            assert bond_stock_flow(1, head, -1j * (head - 1) / 4) == (0, 0)
        stationary.append("0")

    size = 256
    k = 2 * np.pi * np.fft.fftfreq(size)
    distance = abs(k - np.pi / 3)
    f = np.exp(-distance**2 / (2 * 0.18**2)) * (distance < 0.65)
    omega, _ = dispersion((k, 0, 0))
    omega = np.where(omega > 0, omega, 1)
    reflected = (-np.arange(size)) % size

    def measure(spectrum):
        u = np.fft.ifft(spectrum)
        edges = np.array([np.fft.ifft(-1j * (np.exp(1j * k * d[0]) - 1)
                                        * spectrum / omega) for d in DIRECTIONS])
        return rates(u, edges)

    shifted = f * np.exp(40j * k)
    single = measure(f)
    overlap = measure(f + f[reflected])
    separated = measure(shifted + shifted[reflected])
    assert overlap["local_rate_increment"] < 1e-20
    assert separated["net_rate_increment"] < 1e-20
    assert separated["local_rate_increment"] > 0.99 * single["local_rate_increment"]
    return {"stationary_rate_increments": stationary, "matched_center_rate_increments": matched,
            "single": single, "overlapped": overlap, "separated": separated}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
