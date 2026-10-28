"""Exact Fraction check of the K4 gate obstruction and least-norm port."""
from fractions import Fraction as F
from itertools import combinations, product

edges = list(combinations(range(4), 2))
B = [[F((i == v) - (j == v)) for i, j in edges] for v in range(4)]
u = [F(1, 4)] * 4
r = [F(i == 0) for i in range(4)]
Bt = list(map(list, zip(*B)))
matvec = lambda A, v: [sum(a * b for a, b in zip(row, v)) for row in A]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
assert matvec(Bt, u) == [0] * 6
Lr = matvec(B, matvec(Bt, r))
assert Lr == [4 * (a - b) for a, b in zip(r, u)]
b = [-z for z in matvec(Bt, r)]
assert dot(b, b) == 3
assert matvec(B, b) == [-4 * (a - c) for a, c in zip(r, u)]
for mask in product((0, 1), repeat=6):
    assert matvec(B, [h * z for h, z in zip(mask, [F(0)] * 6)]) == [0] * 4
    assert [h * z for h, z in zip(mask, matvec(Bt, u))] == [0] * 6
assert dot(u, u) == F(1, 4) and dot(r, r) == 1
print("PASS: 64 binary masks fixed; norm obstruction; L=4I-J; least-norm port squared=3")
