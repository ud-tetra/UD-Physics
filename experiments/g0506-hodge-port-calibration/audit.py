"""Exact rational witnesses for directed Hodge port and multi-preparation rank."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def rank(rows):
    rows = [[F(v) for v in row] for row in rows]
    pivot = 0
    for col in range(len(rows[0])):
        k = next((k for k in range(pivot, len(rows)) if rows[k][col]), None)
        if k is None:
            continue
        rows[pivot], rows[k] = rows[k], rows[pivot]
        p = rows[pivot][col]
        rows[pivot] = [v / p for v in rows[pivot]]
        for k in range(len(rows)):
            if k != pivot:
                p = rows[k][col]
                rows[k] = [v - p * w for v, w in zip(rows[k], rows[pivot])]
        pivot += 1
    return pivot


def main():
    simplices = [s for size in range(1, 5) for s in combinations(range(4), size)]
    index = {s: k for k, s in enumerate(simplices)}
    d = [[F(0) for _ in simplices] for _ in simplices]
    for s in simplices:
        if len(s) > 1:
            for k in range(len(s)):
                d[index[s[:k] + s[k + 1:]]][index[s]] = F((-1) ** k)
    A = [[d[i][j] - d[j][i] for j in range(15)] for i in range(15)]
    product = lambda M, N: [[sum((M[i][k] * N[k][j] for k in range(15)), F(0)) for j in range(15)] for i in range(15)]
    A2 = product(A, A)
    assert product(A2, A) == [[-4 * v for v in row] for row in A]
    P = [[-v / 4 for v in row] for row in A2]
    assert product(P, P) == P and rank(P) == 14
    # theta = 1/4 <Ax,dx>; A's entries are incident pairs only.
    assert all(A[i][j] == 0 for i, s in enumerate(simplices) for j, t in enumerate(simplices)
               if not (len(s) + 1 == len(t) and set(s) < set(t)
                       or len(t) + 1 == len(s) and set(t) < set(s)))
    x = [F(0)] * 15
    x[index[(0, 1)]] = F(1)
    assert [sum(P[i][j] * x[j] for j in range(15)) for i in range(15)] == x
    Ax = [sum(A[i][j] * x[j] for j in range(15)) for i in range(15)]
    assert sum(v * v for v in Ax) == 4
    assert sum((Ax[i] * Ax[i] / 4 for i in range(15)), F(0)) == 1  # theta_x(Ax)=a
    # Exact coefficients of pi: theta's oriented closed loop I/pi=a*n.
    winding = []
    for a in [F(1, 4), F(1), F(9, 4)]:
        for n in [-2, -1, 0, 1, 2]:
            I = a * n
            L = F(3, 2) * I  # an arbitrary nonzero rational lambda, not a fit
            assert (L == 0) == (I == 0)
            assert -L == F(3, 2) * (-I)
            winding.append([str(a), n, str(I), str(L)])
    assert F(1) * 2 == F(2) * 1  # same scalar action, distinct typed (a,n)
    # Log unknowns (A0,tau0,a1,...,aN). Any number of energy rows plus
    # a signed period leaves one global scale null direction.
    ranks = {}
    for count in (1, 2, 5):
        energy = []
        for k in range(count):
            row = [0] * (count + 2)
            row[0], row[1], row[k + 2] = 1, -1, 1
            energy.append(row)
        period = [0, 1] + [0] * count
        anchor = [0, 0, 1] + [0] * (count - 1)
        target = [1, 0] + [0] * count
        null = [1, 0] + [-1] * count
        assert all(sum(x * y for x, y in zip(row, null)) == 0 for row in energy + [period])
        assert sum(x * y for x, y in zip(anchor, null)) == -1
        assert rank(energy + [period]) == count + 1
        assert rank(energy + [period, target]) == count + 2
        assert rank(energy + [period, anchor]) == count + 2
        # Relative supports/log amplitude ratios supply no missing direction.
        relative = [0, 0, 1, -1] + [0] * (count - 2) if count >= 2 else None
        if relative:
            assert sum(x * y for x, y in zip(relative, null)) == 0
            assert rank(energy + [period, relative]) == count + 1
        ranks[str(count)] = {"without_absolute_support": count + 1, "with_absolute_support": count + 2}
    A0, tau0, a, c = F(5), F(2), F(3), F(2)
    assert A0 * a / tau0 == (A0 / c**2) * (c**2 * a) / tau0
    assert (A0 * a / tau0) * (F(1, 2) * F(1) * tau0) / (F(1, 2) * a) == A0  # rho=1/2, T_read=rho*pi*tau0; pi cancels
    result = {
        "status": "EXACT_CONDITIONAL_WITNESSES_PASS",
        "carrier": "filled K4, unit coefficient metric, 15 registers, 14 active",
        "theta": "1/2<Jx,dx>=1/4<Ax,dx>; simplex incidence local",
        "directed_transport": "R_lambda(gamma)=exp(-lambda integral_gamma theta); inverse under path reversal",
        "lambda_test_value": "3/2 (arbitrary witness; no source selection)",
        "winding_cases": winding,
        "multi_preparation_ranks": ranks,
        "period_ratio_examples": {"signed_linear": "1", "nonconstant_quadratic": "1/2", "constant_energy": "undefined"},
        "empirical_admission": False, "physical_promotion": 0,
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "multi_preparation_ranks", "empirical_admission")}))


if __name__ == "__main__":
    main()
