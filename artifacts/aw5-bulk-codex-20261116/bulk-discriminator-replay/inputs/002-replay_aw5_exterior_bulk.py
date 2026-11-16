"""Exact AW5 bulk readout spectra and damped Taylor coefficients."""
from itertools import combinations
from math import factorial
from sympy import Matrix, Rational, eye, symbols, zeros


def boundary(rows, columns):
    matrix = zeros(len(rows), len(columns))
    positions = {face: index for index, face in enumerate(rows)}
    for col, simplex in enumerate(columns):
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k + 1:]
            matrix[positions[face], col] = (-1) ** k
    return matrix


def derivatives(eigenvalue, gamma):
    values = [1, 0]
    for _ in range(6):
        values.append((-gamma * values[-1] - eigenvalue * values[-2]).expand())
    return values


def main():
    hub = (0, 1, 2, 3)
    tops = [hub] + [tuple(j for j in hub if j != i) + (4 + i,) for i in hub]
    faces = sorted({f for t in tops for f in combinations(t, 3)})
    edges = sorted({e for f in faces for e in combinations(f, 2)})
    b2 = boundary(edges, faces)
    b3 = boundary(faces, tops)
    c = b3[:, 0]
    leaves = Matrix.hstack(*[-(c.T * b3[:, i])[0] * b3[:, i] for i in range(1, 5)])
    d = leaves * Matrix([1] * 4)
    e = c + d
    assert leaves.T * leaves == 4 * eye(4)
    assert c.T * leaves == Matrix([[-1] * 4])
    assert b2 * e == zeros(18, 1)
    assert all(e[i] == 0 if max(f) < 4 else abs(e[i]) == 1 for i, f in enumerate(faces))
    assert e.dot(e) == 12

    hollow = leaves * leaves.T
    filled = hollow + c * c.T
    hollow_mode = hollow * e / 4
    hollow_static = e - hollow_mode
    assert hollow * hollow_static == zeros(16, 1)
    assert hollow * hollow_mode == 4 * hollow_mode
    assert [v.dot(v) for v in (hollow_static, hollow_mode)] == [3, 9]

    filled_low = (6 * e - filled * e) / 4
    filled_high = e - filled_low
    assert filled * filled_low == 2 * filled_low
    assert filled * filled_high == 6 * filled_high
    assert [v.dot(v) for v in (filled_low, filled_high)] == [9, 3]

    gamma = symbols("gamma")
    leaf, low, high = (derivatives(lam, gamma) for lam in (4, 2, 6))
    gap = [Rational(1, 4) * (int(k == 0) + 3 * leaf[k] - 3 * low[k] - high[k])
           for k in range(8)]
    assert [v.expand() for v in gap[:7]] == [0] * 6 + [12]
    residual_bound = (3 * 4**4 + 3 * 2**4 + 6**4) * Rational(1, 4 * factorial(8))
    assert residual_bound == Rational(11, 840)
    assert Rational(1, 60) - residual_bound == Rational(1, 280)
    print("PASS exterior shell support and closed-cycle incidence.")
    print("PASS exact spectral weights hollow (0:1/4, 4:3/4) and filled (2:3/4, 6:1/4).")
    print("PASS common damping leaves the first separating derivative at order six, value 12.")
    print("PASS undamped lower bound s^6/280 on 0 < s <= 1.")


if __name__ == "__main__":
    main()
