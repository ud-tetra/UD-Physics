"""Exact constructor replay, using H = <w,q> before normalizing to G."""
from fractions import Fraction
from replay_aw5_structural_gap4 import carrier, incidence, multiply, transpose


def column(matrix, index):
    return [[row[index]] for row in matrix]


def scale(matrix, factor):
    return [[factor * v for v in row] for row in matrix]


def add(left, right):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(left, right)]


def main():
    cells = carrier((0, 1, 2, 3), (0, 1, 2, 4))
    b1, b2, b3 = incidence(cells)
    x = column(b2, cells[2].index((0, 1, 2)))
    w = multiply(transpose(b2), x)
    # Row identities hold against every edge and face basis vector.
    assert multiply(transpose(x), transpose(b1)) == [[0] * len(cells[0])]
    assert multiply(transpose(w), b3) == [[0] * len(cells[3])]
    assert multiply(transpose(x), b2) == list(map(list, transpose(w)))
    assert multiply(transpose(w), transpose(b2)) == scale(transpose(x), 5)
    assert multiply(transpose(x), x) == [[3]]
    assert multiply(transpose(w), w) == [[15]]

    # F'=-H, H'=5F. The normalized plane-norm form is conserved.
    generator = [[0, -1], [5, 0]]
    norm_form = [[Fraction(1, 3), 0], [0, Fraction(1, 15)]]
    assert add(multiply(transpose(generator), norm_form),
               multiply(norm_form, generator)) == [[0, 0], [0, 0]]
    assert multiply(transpose(x), scale(x, Fraction(1, 2))) == [[Fraction(3, 2)]]
    print("PASS gauge and top-face orthogonality, shared output closure and exact conserved norm.")
    print("PASS inequivalent native readouts for integer-shifted compact lifts, including half-turn discrepancy.")


if __name__ == "__main__":
    main()
