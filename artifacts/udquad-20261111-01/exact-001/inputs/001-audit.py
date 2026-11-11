"""Exact S4 parity/edge-to-tracefree-quadrupole intertwiner source gates."""
import itertools
import json
from fractions import Fraction as Q

V = range(4)
EDGES = tuple(itertools.combinations(V, 2))
PERMS = tuple(itertools.permutations(V))
MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
THETA7 = tuple(t for t in itertools.product((0, 1), repeat=3) if any(t))


def zeros(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


P = [[Q(int(i == j)) - Q(1, 4) for j in V] for i in V]


def dyad(edge):
    i, j = edge
    v = [Q(int(k == i) - int(k == j)) for k in V]
    return [[v[k] * v[l] - Q(2, 3) * P[k][l] for l in V] for k in V]


M = [dyad(e) for e in EDGES]


def dot(a, b):
    return sum(a[i][j] * b[i][j] for i in V for j in V)


def rank(a):
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    pivot = 0
    for col in range(w):
        pos = next((i for i in range(pivot, h) if a[i][col]), None)
        if pos is None:
            continue
        a[pivot], a[pos] = a[pos], a[pivot]
        z = a[pivot][col]
        a[pivot] = [v / z for v in a[pivot]]
        for i in range(h):
            if i != pivot:
                z = a[i][col]
                a[i] = [v - z * b for v, b in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == h:
            break
    return pivot


def parity(g):
    return (-1) ** sum(g[i] > g[j] for i in V for j in range(i + 1, 4))


def match_perm(g):
    return tuple(MATCHINGS.index(tuple(sorted(tuple(sorted((g[i], g[j]))) for i, j in pair)))
                 for pair in MATCHINGS)


def perm_theta(t, g):
    dest = [0, 0, 0]
    for p, gp in enumerate(match_perm(g)):
        dest[gp] = t[p]
    return tuple(dest)


def main():
    gram = [[dot(a, b) for b in M] for a in M]
    assert rank(gram) == 5
    assert all(sum(gram[i]) == 0 for i in range(6))
    assert all(sum(m[i][j] for m in M) == 0 for i in V for j in V)
    assert all(sum(m[i][i] for i in V) == 0 for m in M)
    assert all(sum(m[i][j] for j in V) == 0 for m in M for i in V)

    # Pair-constant zero-sum plane (dimension 2), and pair-antisymmetric
    # subspace (dimension 3). Their exact Gram eigenvalues are 2 and 4.
    opposite = {0: 5, 5: 0, 1: 4, 4: 1, 2: 3, 3: 2}
    pair_plane = [[Q(1), Q(-1), Q(0), Q(0), Q(-1), Q(1)],
                  [Q(1), Q(0), Q(-1), Q(-1), Q(0), Q(1)]]
    antisym = [[Q(int(i == k) - int(i == opposite[k])) for i in range(6)]
               for k in (0, 1, 2)]
    for eigen, vectors in ((2, pair_plane), (4, antisym)):
        for x in vectors:
            assert [sum(gram[i][j] * x[j] for j in range(6)) for i in range(6)] == [eigen * z for z in x]
    assert rank(pair_plane + antisym + [[Q(1)] * 6]) == 6

    # Correct P06 source: Delta_theta = |Theta \ {000}| = 7, not 6+1.
    # The optional edge-plus-top source below is a different carrier.
    pair_m = [[[sum(M[EDGES.index(e)][i][j] for e in pair) for j in V] for i in V]
              for pair in MATCHINGS]
    assert all(sum(pair_m[p][i][j] for p in range(3)) == 0 for i in V for j in V)
    parity_m = [[[sum(t[p] * pair_m[p][i][j] for p in range(3)) for j in V] for i in V]
                for t in THETA7]
    parity_gram = [[dot(a, b) for b in parity_m] for a in parity_m]
    assert rank(parity_gram) == 2
    assert all(sum(m[i][j] for m in parity_m) == 0 for i in V for j in V)

    edge_char, parity_char, quad_char, sign_char = [], [], [], []
    for g in PERMS:
        edge_char.append(sum(set((g[i], g[j])) == set((i, j)) for i, j in EDGES))
        parity_char.append(sum(perm_theta(t, g) == t for t in THETA7))
        fixed = sum(g[i] == i for i in V)
        std = fixed - 1
        g2 = tuple(g[g[i]] for i in V)
        std2 = sum(g2[i] == i for i in V) - 1
        quad_char.append((std * std + std2) // 2 - 1)
        sign_char.append(parity(g))
        # Covariance of the explicit map under vertex relabeling.
        for e, m in zip(EDGES, M):
            ge = tuple(sorted((g[e[0]], g[e[1]])))
            transformed = [[m[g.index(i)][g.index(j)] for j in V] for i in V]
            assert transformed == M[EDGES.index(ge)]
        for t, m in zip(THETA7, parity_m):
            transformed = [[m[g.index(i)][g.index(j)] for j in V] for i in V]
            assert transformed == parity_m[THETA7.index(perm_theta(t, g))]
    def inner(a, b):
        numerator = sum(x * y for x, y in zip(a, b))
        assert numerator % 24 == 0
        return numerator // 24
    assert inner(edge_char, quad_char) == 2
    assert inner(parity_char, quad_char) == 2
    assert inner(parity_char, parity_char) == 13  # 3 trivial + 2 copies of the two-dimensional irrep
    assert inner([1] * 24, quad_char) == 0
    assert inner(sign_char, quad_char) == 0
    assert inner(quad_char, quad_char) == 2
    assert inner(edge_char, edge_char) == 3
    print(json.dumps({
        "status": "EXACT_CONDITIONAL",
        "p06_source": "seven nonreference parity states Theta minus {000}; S4 action factors through S3",
        "p06_source_decomposition": "3 trivial + 2 copies of dimension-2 irrep; no dimension-3 response irrep",
        "p06_hom_s4_to_response_dimension": inner(parity_char, quad_char),
        "p06_maximum_intertwiner_rank": 2,
        "p06_example_map": "Psi(c)=sum_nonzero_theta c_theta sum_p theta_p Q_p; Q_p=sum_edges_in_matching_p M_edge",
        "p06_example_rank": rank(parity_gram),
        "p06_example_kernel_dimension": 7 - rank(parity_gram),
        "p06_uniform_seven_state_source_image": "0",
        "p06_s4_covariance_checks": len(PERMS) * len(THETA7),
        "alternate_carrier": "six unoriented edges plus one trivial or sign top-cell source, NOT ledger P06",
        "response": "trace-free symmetric operators on H={x in Q^4:sum x=0}",
        "intertwiner": "Phi(x)=sum_edges x_ij[(e_i-e_j)(e_i-e_j)^T-(2/3)P_H]",
        "gram": [[str(v) for v in row] for row in gram],
        "rank": rank(gram), "kernel": "span{(1,1,1,1,1,1)}",
        "gram_eigenspaces": {"pair_constant_zero_sum": {"dimension": 2, "eigenvalue": 2},
                             "pair_antisymmetric": {"dimension": 3, "eigenvalue": 4}},
        "hom_s4_edge_to_response_dimension": inner(edge_char, quad_char),
        "hom_s4_trivial_top_to_response_dimension": 0,
        "hom_s4_sign_top_to_response_dimension": 0,
        "uniform_six_edge_source_image": "0",
        "alternate_uniform_six_edge_plus_top_source_image": "0",
        "s4_covariance_checks": len(PERMS) * len(EDGES),
        "physical_promotion": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
