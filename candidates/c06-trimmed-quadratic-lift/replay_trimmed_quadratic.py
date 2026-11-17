"""Exact regular tetrahedron P^-_2 Lambda^1 trace and Dirichlet tests."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import factorial
import json

from sympy import Matrix, Rational as R, eye, zeros

EDGES = list(combinations(range(4), 2))
FACES = list(combinations(range(4), 3))
CANDIDATES = [(i, j, k) for i, j in EDGES for k in range(4)]


def dot(i, j):
    return 2 * (int(i == j) - R(1, 4))


@lru_cache(None)
def moment(indices):
    numerator = 6
    for count in Counter(indices).values():
        numerator *= factorial(count)
    return R(numerator, factorial(3 + len(indices)))


def basis_terms(i, j, k):
    return [(1, (i, k), j), (-1, (j, k), i)]


def derivative(terms):
    return [(sign, bary[:p] + bary[p+1:], covector, index)
            for sign, bary, covector in terms for p, index in enumerate(bary)]


def mass_gram(left, right):
    return sum(a * b * moment(tuple(sorted(x + y))) * dot(i, j)
               for a, x, i in left for b, y, j in right)


def derivative_gram(left, right, curl):
    return sum(a * b * moment(tuple(sorted(x + y))) *
               (dot(i, j) * dot(k, l) - (dot(i, l) * dot(k, j) if curl else 0))
               for a, x, i, k in left for b, y, j, l in right)


def trace_matrix(indices):
    # On each face use tangents v_b-v_a, v_c-v_a and the coefficients of
    # the six homogeneous degree-two barycentric monomials of that face.
    rows = []
    for a, b, c in FACES:
        f = (a, b, c)
        for v in (b, c):
            for monomial in [(i, j) for i in f for j in f if i <= j]:
                rows.append([sum(sign * (int(g == v) - int(g == a))
                                 for sign, bary, g in basis_terms(*CANDIDATES[k])
                                 if tuple(sorted(bary)) == monomial)
                             for k in indices])
    return Matrix(rows)


def effective(gram, restriction):
    # Choose a right inverse of the edge-integral map, then eliminate its
    # kernel. Rank-deficient derivative forms admit multiple minimizers.
    _, pivots = restriction.rref()
    right = zeros(restriction.cols, restriction.rows)
    for i, row in enumerate(restriction[:, list(pivots)].inv().tolist()):
        right[pivots[i], :] = Matrix([row])
    kernel = Matrix.hstack(*restriction.nullspace())
    h = kernel.T * gram * kernel
    rhs = kernel.T * gram * right
    solution, parameters = h.gauss_jordan_solve(rhs)
    solution = solution.subs({p: 0 for p in parameters})
    lift = right - kernel * solution
    assert restriction * lift == eye(6)
    assert kernel.T * gram * lift == zeros(kernel.cols, 6)
    return lift.T * gram * lift


def main():
    terms = [basis_terms(*item) for item in CANDIDATES]
    full = Matrix(24, 24, lambda i, j: mass_gram(terms[i], terms[j]))
    _, indices = full.rref()
    assert len(indices) == 20
    assert trace_matrix(indices).rank() == 20
    terms = [terms[k] for k in indices]
    dterms = [derivative(t) for t in terms]
    restriction = Matrix(6, 20, lambda e, k: R(1, 2) if (
        CANDIDATES[indices[k]][:2] == EDGES[e]
        and CANDIDATES[indices[k]][2] in EDGES[e]) else 0)
    assert restriction.rank() == 6
    mass = full.extract(indices, indices)
    curl = Matrix(20, 20, lambda i, j: derivative_gram(dterms[i], dterms[j], True))
    grad = Matrix(20, 20, lambda i, j: derivative_gram(dterms[i], dterms[j], False))
    v = Matrix(4, 6, lambda a, e: int(a == EDGES[e][1]) - int(a == EDGES[e][0]))
    cuts = v.T * v / 4
    cycles = eye(6) - cuts
    output = {"space_rank": 20, "full_trace_rank": 20, "edge_mean_rank": 6,
              "free_with_edge_mean": 14, "energy_sectors": {}}
    tests = (
        ("mass", mass, (R(31, 560), R(1, 12))),
        ("curl", curl, (0, R(144, 19))),
        ("gradient", grad, (0, R(48, 11))),
        ("mass_plus_curl", mass + curl, (R(5701, 40250), R(92399, 12030))),
    )
    for name, energy, expected in tests:
        g = effective(energy, restriction)
        cut, cycle = (g * cuts).trace() / 3, (g * cycles).trace() / 3
        assert (cut, cycle) == expected
        assert g == cut * cuts + cycle * cycles
        output["energy_sectors"][name] = {"cut": str(cut), "cycle": str(cycle)}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
