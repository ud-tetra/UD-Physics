"""Exact signed-incidence replay for the 46D and 47D AW5 readouts."""
from sympy import Matrix, eye, symbols, zeros
from replay_aw5_structural_gap4 import carrier, incidence


def verify(cells, counts):
    assert tuple(map(len, cells)) == counts
    b1, b2, b3 = map(Matrix, incidence(cells))
    n0, n1, n2, n3 = counts
    assert b1 * b2 == zeros(n0, n2)
    assert b2 * b3 == zeros(n1, n3)
    assert b1.rank() == 7 and b2.rank() == 11
    k = b2.T * b2
    a = Matrix.vstack(
        Matrix.hstack(zeros(n0), -b1, zeros(n0, n2), zeros(n0, n3)),
        Matrix.hstack(b1.T, zeros(n1), -b2, zeros(n1, n3)),
        Matrix.hstack(zeros(n2, n0), b2.T, zeros(n2), -b3),
        Matrix.hstack(zeros(n3, n0), zeros(n3, n1), b3.T, zeros(n3)),
    )
    output = Matrix.vstack(
        Matrix.hstack(zeros(n2, n0), b2.T, zeros(n2), zeros(n2, n3)),
        Matrix.hstack(zeros(n2, n0), zeros(n2, n1), k, zeros(n2, n3)),
    )
    law = Matrix.vstack(Matrix.hstack(zeros(n2), -eye(n2)),
                        Matrix.hstack(k, zeros(n2)))
    assert output * a == law * output
    exterior = [index for index, face in enumerate(cells[2]) if max(face) >= 4]
    assert len(exterior) == 12
    assert b2[:, exterior].rank() == 11
    assert output[exterior + [n2 + i for i in exterior], :].rank() == 22
    u = symbols("u")
    expected = u**5 * (u - 3)**2 * (u - 5)**3 * (u**2 - 9*u + 16)**3
    assert (k.charpoly(u).as_expr() - expected).expand() == 0
    return b1, b2, k, exterior


def main():
    hub = (0, 1, 2, 3)
    leaves = [tuple(j for j in hub if j != i) + (4 + i,) for i in hub]
    hollow = carrier(*leaves)
    filled = carrier(hub, *leaves)
    assert hollow[:3] == filled[:3]
    assert verify(hollow, (8, 18, 16, 4)) == verify(filled, (8, 18, 16, 5))
    print("PASS full generators intertwine with the same exact real face-output law.")
    print("PASS exterior readout rank 22 in both carriers; positive spectral multiplicities 2,3,3,3.")
    print("PASS common boundary incidence and exterior face rows imply identical matched traces.")


if __name__ == "__main__":
    main()
