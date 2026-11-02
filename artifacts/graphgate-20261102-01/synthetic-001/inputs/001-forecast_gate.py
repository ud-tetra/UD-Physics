"""Conditional simple-vs-simple signed-force gate. Rational input; Gaussian tail."""
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path
from statistics import NormalDist


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def solve_spd(matrix, rhs):
    """Exact LDL^T solve with a strict positive-definiteness check."""
    n = len(rhs)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError("covariance shape differs from forecast vector")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise ValueError("covariance is not symmetric")
    lower = [[F(i == j) for j in range(n)] for i in range(n)]
    diag = [F(0) for _ in range(n)]
    for i in range(n):
        diag[i] = matrix[i][i] - sum(lower[i][k] ** 2 * diag[k] for k in range(i))
        if diag[i] <= 0:
            raise ValueError("covariance is not positive definite")
        for j in range(i + 1, n):
            lower[j][i] = (matrix[j][i] - sum(lower[j][k] * lower[i][k] * diag[k] for k in range(i))) / diag[i]
    forward = [F(0)] * n
    for i in range(n):
        forward[i] = rhs[i] - sum(lower[i][j] * forward[j] for j in range(i))
    scaled = [forward[i] / diag[i] for i in range(n)]
    answer = [F(0)] * n
    for i in reversed(range(n)):
        answer[i] = scaled[i] - sum(lower[j][i] * answer[j] for j in range(i + 1, n))
    return answer


def evaluate(record):
    if record.get("mode") not in ("design", "evaluation"):
        raise ValueError("mode must be design or evaluation")
    if not record.get("force_unit") or not record.get("freeze_reference"):
        raise ValueError("force_unit and external freeze_reference are required")
    rows = record["rows"]
    n = len(rows)
    if n == 0 or len(set(rows)) != n:
        raise ValueError("rows must be nonempty unique labels in frozen order")
    mu0, mu1 = ([F(v) for v in record[k]] for k in ("mu0", "mu1"))
    if len(mu0) != n or len(mu1) != n:
        raise ValueError("forecast length differs from rows")
    covariance = [[F(v) for v in row] for row in record["covariance"]]
    delta = [a-b for a, b in zip(mu1, mu0)]
    weighted = solve_spd(covariance, delta)
    d2 = dot(delta, weighted)
    alpha, power_target = F(record["alpha"]), F(record["target_power"])
    if not (0 < alpha < 1 and 0 < power_target < 1):
        raise ValueError("alpha and target_power must lie strictly between 0 and 1")
    normal = NormalDist()
    z = normal.inv_cdf(1-float(alpha))
    required_d = z + normal.inv_cdf(float(power_target))
    out = {"status": "CONDITIONAL_GAUSSIAN_GATE", "force_unit": record["force_unit"],
           "dimension": n, "d_squared_exact": str(d2), "d": math.sqrt(float(d2)),
           "alpha": str(alpha), "target_power": str(power_target),
           "required_d_for_target_power": required_d,
           "nominal_power": normal.cdf(math.sqrt(float(d2))-z) if d2 else None,
           "identifiable": bool(d2), "freeze_reference": record["freeze_reference"]}
    if record["mode"] == "evaluation":
        observed = [F(v) for v in record["observed"]]
        if len(observed) != n:
            raise ValueError("observation length differs from rows")
        residual = [a-b for a, b in zip(observed, mu0)]
        improvement = 2*dot(weighted, residual)-d2
        out["delta_chi_squared_exact"] = str(improvement)
        if d2:
            threshold = -float(d2) + 2*math.sqrt(float(d2))*z
            z_observed = (float(improvement)+float(d2))/(2*math.sqrt(float(d2)))
            out.update(threshold_delta_chi_squared=threshold,
                       one_sided_null_p=normal.cdf(-z_observed),
                       favors_frozen_H1_at_alpha=float(improvement)>threshold)
        else:
            out["favors_frozen_H1_at_alpha"] = False
    return out


def self_check():
    cov = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
    delta = [F(1), F(1)]
    weighted = solve_spd(cov, delta)
    assert weighted == [F(2, 3), F(2, 3)]
    assert dot(delta, weighted) == F(4, 3)
    fixture = json.loads((Path(__file__).parent / "SYNTHETIC_EXAMPLE.json").read_text())
    assert evaluate(fixture)["delta_chi_squared_exact"] == "0"
    for observation, expected in [(["0", "0"], "-4/3"), (["1", "1"], "4/3")]:
        fixture["observed"] = observation
        assert evaluate(fixture)["delta_chi_squared_exact"] == expected
    for invalid in ([[F(1), F(2)], [F(2), F(1)]], [[F(1), F(0)], [F(2), F(1)]]):
        try:
            solve_spd(invalid, delta)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid covariance accepted")
    print("PASS: exact LDL solve, d²=4/3, null/alternative/midpoint improvement and invalid covariances")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
    if args.input:
        print(json.dumps(evaluate(json.loads(args.input.read_text())), indent=2))
    if not args.self_check and not args.input:
        parser.error("provide an input file or --self-check")
