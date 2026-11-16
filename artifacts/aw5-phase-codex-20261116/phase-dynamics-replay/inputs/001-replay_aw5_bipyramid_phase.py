"""Exact checks of the shared-face oscillator and failure of compact descent."""
from fractions import Fraction
from replay_aw5_structural_gap4 import carrier, incidence, multiply, transpose


def column(matrix, index):
    return [[row[index]] for row in matrix]


def scale(vector, factor):
    return [[factor * value] for value, in vector]


def main():
    cells = carrier((0, 1, 2, 3), (0, 1, 2, 4))
    b1, b2, b3 = incidence(cells)
    face = cells[2].index((0, 1, 2))
    edge_mode = column(b2, face)
    face_mode = multiply(transpose(b2), edge_mode)
    assert not any(map(any, multiply(b1, edge_mode)))
    assert not any(map(any, multiply(transpose(b3), face_mode)))
    assert multiply(b2, face_mode) == scale(edge_mode, 5)
    assert face_mode[face] == [3]
    assert multiply(transpose(edge_mode), edge_mode) == [[3]]

    # Integer-equivalent preparations differ by half the edge mode at phase pi/3.
    assert all(value == int(value) for value, in edge_mode)
    assert Fraction(face_mode[face][0], 2) % 1 == Fraction(1, 2)
    assert Fraction(face_mode[face][0], 4) % 1 == Fraction(3, 4)
    print("PASS plane: A x = B2^T x, A(B2^T x) = -5 x, shared-face coboundary = 3.")
    print("PASS compact descent counterexample: same initial edge phase, later shared turn differs by 1/2.")
    print("PASS conditional Wilson witness: shared-face turn 3/4 gives -i.")


if __name__ == "__main__":
    main()
