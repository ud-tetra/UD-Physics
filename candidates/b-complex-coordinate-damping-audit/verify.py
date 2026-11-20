from itertools import combinations
from sympy import Matrix, eye, zeros, factor, symbols, sqrt, Rational, cos, sin, pi

def carrier(cells):
    simplices = [s for k in range(1, 5) for s in
                 sorted({s for cell in cells for s in combinations(cell, k)})]
    index = {s: i for i, s in enumerate(simplices)}
    boundary = zeros(len(simplices))
    for simplex, j in index.items():
        if len(simplex) > 1:
            for k in range(len(simplex)):
                boundary[index[simplex[:k] + simplex[k + 1:]], j] = (-1)**k
    assert boundary**2 == zeros(len(simplices))
    return index, boundary - boundary.T

def ring(size):
    return carrier([tuple(sorted((i, (i + 1) % size, size, size + 1)))
                    for i in range(size)])

def dark(generator, observer):
    rows, ranks = observer, []
    while True:
        rank = rows.rank()
        if ranks and rank == ranks[-1]:
            break
        ranks.append(rank)
        rows = rows.col_join(rows * generator)
        rows = rows.T[:, rows.T.rref()[1]].T
    return Matrix.hstack(*rows.nullspace()), ranks

def restricted(generator, basis):
    restriction = (basis.T*basis).inv()*basis.T*generator*basis
    assert generator*basis == basis*restriction
    return restriction

z = symbols('z')
b_index, B = ring(3)
mask = [(3, 4), (0, 3, 4), (1, 3, 4), (0, 1, 3, 4)]
O_B = eye(27)[[b_index[s] for s in mask], :]
dark_B, b_ranks = dark(B, O_B)
P_B = restricted(B, dark_B)
assert dark_B.cols == 17
assert factor(P_B.charpoly(z).as_expr()) == z*(z**2+2)*(z**2+5)**7
assert O_B*dark_B == zeros(4, 17)
print('B observer ranks:', b_ranks, 'lossless:', dark_B.cols)
print('B lossless characteristic polynomial:', factor(P_B.charpoly(z).as_expr()))

p_index, A = ring(5)
eq = [tuple(sorted((i, (i + 1) % 5))) for i in range(5)]
radial_edges = sorted({e for i in range(5) for e in combinations((i, 5, 6), 2)})
S = eye(43)[[p_index[e] for e in radial_edges], :]
dark_PB5, pb_ranks = dark(A, S)
P5 = restricted(A, dark_PB5)
assert dark_PB5.cols == 21
P = dark_PB5*(dark_PB5.T*dark_PB5).inv()*dark_PB5.T
for edge, i in p_index.items():
    if len(edge) == 2:
        assert P[:, i] == (eye(43)[:, i] if edge in eq else zeros(43, 1))
assert (P5**2+5*eye(21)).det() != 0
assert (A**2+5*eye(43)).det() != 0
print('PB5 observer ranks:', pb_ranks, 'lossless:', dark_PB5.cols)
print('PB5 grade-one projection: five equatorial edge coefficients')

angles = [2*pi*i/5 for i in range(5)]
circulations = [1, 1, 1, 1, -1]  # last cyclic edge reverses ascending orientation
point_rows = Matrix([[cos(2*t)/sqrt(2), sin(2*t)/sqrt(2)] for t in angles])
difference = Matrix([[(1 if j == (i+1)%5 else 0)-(1 if j == i else 0)
                      for j in range(5)] for i in range(5)])
signed = difference*point_rows
gain = 5*(5+sqrt(5))/8
assert all(value.equals(0) for value in signed.T*signed-gain*eye(2))
# An equatorial chord has tangent direction at the midpoint angle.
mid = [t+pi/5 for t in angles]
directional = Matrix([[1/sqrt(6), -cos(2*t)/sqrt(2), -sin(2*t)/sqrt(2)] for t in mid])
expected_gain = Matrix.diag(Rational(5,6), Rational(5,4), Rational(5,4))
assert all(value.equals(0) for value in directional.T*directional-expected_gain)
assert Matrix.diag(*circulations).T*Matrix.diag(*circulations) == eye(5)
print('Signed quadratic-potential preparation: rank 2, Gram gain', gain)
print('Cyclically oriented directional measurement: rank 3, Gram gains 5/6, 5/4, 5/4')
print('Same-clock nonzero sqrt(5) transfer: obstructed by PB5 spectrum')
