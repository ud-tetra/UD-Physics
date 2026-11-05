#!/usr/bin/env python3
"""Exact Hasse-cut and interior-stock audit for the snapped 2->3 bipyramid."""
import json
from fractions import Fraction as Q
from pathlib import Path

OLD = [(0, 1, 2, 3), (0, 1, 2, 4)]
NEW = [(0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4)]


def simplices(tops):
    from itertools import combinations
    return sorted({(k, s) for t in tops for k in range(4)
                   for s in combinations(t, k + 1)})


def incidence(lower, upper):
    if len(upper) != len(lower) + 1:
        return 0
    return sum((-1)**j for j in range(len(upper))
               if upper[:j] + upper[j + 1:] == lower)


def generator(labels):
    A = [[Q(0) for _ in labels] for _ in labels]
    for i, (di, si) in enumerate(labels):
        for j, (dj, sj) in enumerate(labels):
            if di == dj + 1:
                A[i][j] = Q(incidence(sj, si))
            elif dj == di + 1:
                A[i][j] = -Q(incidence(si, sj))
    assert all(A[i][j] == -A[j][i] for i in range(len(labels)) for j in range(len(labels)))
    return A


def components(labels, A):
    unseen = set(range(len(labels)))
    out = []
    while unseen:
        todo = [min(unseen)]
        comp = set(todo)
        unseen -= comp
        while todo:
            i = todo.pop()
            for j in list(unseen):
                if A[i][j] or A[j][i]:
                    unseen.remove(j); comp.add(j); todo.append(j)
        out.append(sorted(comp))
    return out


def mv(A, x):
    return [sum(a*b for a, b in zip(row, x)) for row in A]


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def main():
    O, N = simplices(OLD), simplices(NEW)
    shell, oi, ni = sorted(set(O) & set(N)), sorted(set(O) - set(N)), sorted(set(N) - set(O))
    assert len(shell) == 20 and len(oi) == 3 and len(ni) == 7
    assert oi == [(2, (0, 1, 2)), (3, (0, 1, 2, 3)), (3, (0, 1, 2, 4))]
    labels = sorted(set(O) | set(N))
    Ao, An = generator(O), generator(N)
    # The only native cross-incidences of the abstract union use common-shell
    # simplices; freezing them pointwise restricts the active graph to I_o+I_n.
    Aunion = generator(labels)
    interior = oi + ni
    indexes = [labels.index(s) for s in interior]
    B = [[Aunion[i][j] for j in indexes] for i in indexes]
    comps = components(interior, B)
    assert len(comps) == 2 and sorted(map(len, comps)) == [3, 7]
    assert {interior[j] for j in comps[0]} in (set(oi), set(ni))
    assert all(B[i][j] == 0 for i in range(3) for j in range(3, 10))
    old_edges = sum(bool(B[i][j]) for i in range(3) for j in range(i + 1, 3))
    new_edges = sum(bool(B[i][j]) for i in range(3, 10) for j in range(i + 1, 10))
    assert (old_edges, new_edges) == (2, 9)

    # Guard witness under the actual fixed OLD Q169 generator.
    f = O.index((2, (0, 1, 2)))
    x = [Q(i == f) for i in range(len(O))]
    Ax = mv(Ao, x); A2x = mv(Ao, Ax)
    old_indices = [O.index(s) for s in oi]
    shell_indices = [O.index(s) for s in shell]
    stock0 = sum(x[i]**2 for i in old_indices)
    first = 2*sum(x[i]*Ax[i] for i in old_indices)
    second = 2*sum(Ax[i]**2 + x[i]*A2x[i] for i in old_indices)
    shell_leak = sum(Ax[i]**2 for i in shell_indices)
    assert (stock0, first, second, shell_leak) == (1, 0, -6, 3)
    assert dot(Ax, Ax) + dot(x, A2x) == 0
    # Independently count the three face->shell-edge cut incidences.
    assert sum(abs(Ao[i][f]) for i in shell_indices) == 3
    assert sum(abs(Ao[i][f]) for i in old_indices) == 2
    # Interior stock is invariant under base/apex signed permutations.
    permutations = [(1,0,2,3,4),(1,2,0,3,4),(0,1,2,4,3)]
    for perm in permutations:
        mapped = []
        for _,s in oi:
            word = tuple(perm[v] for v in s)
            sign = (-1)**sum(word[i] > word[j] for i in range(len(word)) for j in range(i+1,len(word)))
            mapped.append((oi.index((len(s)-1,tuple(sorted(word)))),sign))
        assert sorted(i for i,_ in mapped) == [0,1,2]
        assert sum(x[O.index(oi[j])]**2 for j,_ in mapped) == stock0

    result = {
        "base_carrier": "abstract union; ascending oriented simplices; Q, unit Q165 stock",
        "counts": {"old":len(O),"new":len(N),"shell":len(shell),"old_only":len(oi),"new_only":len(ni)},
        "interior_hasse_components": [len(c) for c in comps],
        "interior_hasse_edges": {"old_only":old_edges,"new_only":new_edges,"cross":0},
        "guard_witness": {"initial_state":"unit old face 012; all others zero", "old_interior_stock_at_zero":str(stock0),
                          "stock_first_derivative":str(first),"stock_second_derivative":str(second),
                          "shell_stock_leading_coefficient":str(shell_leak),
                          "shell_cut_incidence_count":3},
        "scope":"pointwise shell-amplitude fixation for every state; Q169/Hasse-only skew support; no added contact or memory incidence",
        "physical_promotion":0
    }
    out=Path(__file__).with_name('results.json')
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
