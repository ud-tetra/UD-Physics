"""Exact native path-graph controls for G0 weak-field candidate v0.1."""
from fractions import Fraction as F


def solve(w01: int, w12: int):
    assert w01 > 0 and w12 > 0
    phi2 = F(0)
    phi1 = F(1, w12)
    phi0 = F(1, w01) + phi1
    assert w01 * (phi0 - phi1) == 1
    assert w12 * (phi1 - phi2) == 1
    return (phi0, phi1, phi2), (phi0 - phi1, phi1 - phi2)


if __name__ == "__main__":
    assert solve(1, 1) == ((F(2), F(1), F(0)), (F(1), F(1)))
    assert solve(2, 2) == ((F(1), F(1, 2), F(0)), (F(1, 2), F(1, 2)))
    assert solve(1, 2) == ((F(3, 2), F(1, 2), F(0)), (F(1), F(1, 2)))
    print("PASS: exact source, flux, and three distinct metric-gradient controls")
