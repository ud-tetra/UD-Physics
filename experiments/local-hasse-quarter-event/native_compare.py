"""Exact comparison of the candidate event to native Q169 on filled K4."""
import itertools
import json

SIMPLEX = [list(itertools.combinations(range(4), k)) for k in range(1, 5)]
CELLS = [s for grade in SIMPLEX for s in grade]
INDEX = {s: i for i, s in enumerate(CELLS)}
N = len(CELLS)


def boundary():
    d = [[0 for _ in range(N)] for _ in range(N)]
    for sigma in CELLS:
        if len(sigma) == 1:
            continue
        for j in range(len(sigma)):
            face = sigma[:j] + sigma[j + 1:]
            d[INDEX[face]][INDEX[sigma]] = (-1) ** j
    return d


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def mv(a, x):
    return [sum(a[i][j] * x[j] for j in range(N)) for i in range(N)]


def main():
    d = boundary()
    a = [[d[i][j] - d[j][i] for j in range(N)] for i in range(N)]
    assert all(y == 0 for row in matmul(d, d) for y in row)
    assert all(a[i][j] == -a[j][i] for i in range(N) for j in range(N))

    x = [0] * N
    x[INDEX[(0,)]] = 1
    x[INDEX[(0, 1)]] = 2
    dx = mv(a, x)
    endpoint = x.copy()
    endpoint[INDEX[(0,)]] = 2
    endpoint[INDEX[(0, 1)]] = -1
    vertex_sum = lambda y: sum(y[:4])
    stock = lambda y: sum(t * t for t in y)
    assert vertex_sum(x) == 1 and vertex_sum(endpoint) == 2
    assert stock(x) == stock(endpoint) == 5
    assert sum(xi * di for xi, di in zip(x, dx)) == 0
    assert sum(dx[:4]) == 0
    assert all(sum(a[i][j] for i in range(4)) == 0 for j in range(N))

    expected = {"v0": -2, "v1": 2, "e01": 1, "e02": 1,
                "e03": 1, "f012": -2, "f013": -2}
    labels = ["v" + "".join(map(str, c)) if len(c) == 1 else
              {2: "e", 3: "f", 4: "t"}[len(c)] + "".join(map(str, c))
              for c in CELLS]
    nonzero = {labels[i]: q for i, q in enumerate(dx) if q}
    assert nonzero == expected, nonzero

    # Independent scalar incidence proof: every edge has one -1 and one +1.
    assert all(sum(d[i][j] for i in range(4)) == 0 for j in range(4, 10))
    # Exact carrier spectral identity; only the active subspace rotates.
    aa = matmul(a, a)
    aaa = matmul(aa, a)
    assert all(aaa[i][j] == -4 * a[i][j]
               for i in range(N) for j in range(N))

    # Phase 2s=pi/2 (s=pi/4) gives x+Ax/2+A^2x/4, exactly.
    # Multiply every coefficient by four for an integer numerator.
    aax = mv(aa, x)
    quarter_phase_times_four = [4 * x[i] + 2 * dx[i] + aax[i] for i in range(N)]
    assert vertex_sum(quarter_phase_times_four) == 4
    assert quarter_phase_times_four != [4 * q for q in endpoint]

    print(json.dumps({
        "source": "recovered ledger v0.85 Q169, unit filled K4, A=d-d^T",
        "basis": labels,
        "initial_nonzero": {labels[i]: q for i, q in enumerate(x) if q},
        "candidate_endpoint_nonzero": {labels[i]: q for i, q in enumerate(endpoint) if q},
        "native_initial_derivative_nonzero": nonzero,
        "native_quarter_phase_numerator_denominator_4": {labels[i]: q for i, q in enumerate(quarter_phase_times_four) if q},
        "vertex_sum_initial": vertex_sum(x),
        "vertex_sum_candidate_endpoint": vertex_sum(endpoint),
        "stock_both": stock(x),
        "native_dot_stock_derivative_half": sum(xi * di for xi, di in zip(x, dx)),
        "d_squared_zero": True,
        "A_cubed_equals_minus_4A": True,
        "native_full_state_can_equal_candidate_endpoint_at_any_real_s": False,
        "reason": "vertex sum conserved by 1^T B1=0, but event changes 1 to 2",
        "physical_promotion": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
