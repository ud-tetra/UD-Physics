"""Exact finite carrier controls for the uniform filtration bound."""

from fractions import Fraction
from cell_support_invariants import complex_matrices
from filtration_dynamics import second_order_cell_support


def run():
    cells = ((0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 4, 5))
    simplices, a, _ = complex_matrices(cells)
    d = max(sum(v != 0 for v in row) for row in a)
    assert all(sum(a[i][j] != 0 for i in range(len(a))) <= d
               for j in range(len(a)))
    amplitudes = (1, 3, 2)
    stock = sum(x*x for x in amplitudes)
    margin = min(abs(x*x - 5) for x in amplitudes)
    cells_frozen = tuple(map(frozenset, cells))
    coeff = second_order_cell_support(cells_frozen,
                                      dict(zip(cells_frozen, amplitudes)))
    assert tuple(coeff[x] for x in cells_frozen) == (4, Fraction(-13, 2), Fraction(5, 2))
    assert margin == 1 and stock == 14
    print(f"registers={len(simplices)} d={d} S={stock} margin={margin}; "
          f"strict safe |t|<{Fraction(margin, 2*d*stock)}")
    print("threshold 4 has zero margin and positive third-cell t² coefficient")


if __name__ == "__main__":
    run()
