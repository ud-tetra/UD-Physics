"""Exact all-pass Hodge and face-to-cell current control."""

from itertools import combinations

from sympy import Matrix, Rational, cos, integrate, pi, simplify, sin, sqrt, symbols, zeros


def main():
    simplices = [simplex for size in range(1, 5) for simplex in combinations(range(4), size)]
    index = {simplex: i for i, simplex in enumerate(simplices)}
    boundary = zeros(len(simplices))
    for j, simplex in enumerate(simplices):
        if len(simplex) > 1:
            for k in range(len(simplex)):
                boundary[index[simplex[:k] + simplex[k + 1:]], j] = (-1) ** k

    assert boundary**2 == zeros(len(simplices))
    generator = boundary - boundary.T
    cell = Matrix([0] * (len(simplices) - 1) + [1])
    face = boundary * cell / 2
    assert face.dot(face) == 1 and face.dot(cell) == 0
    assert generator * cell == 2 * face and generator * face == -2 * cell

    s = symbols("s", real=True)
    a = symbols("a", positive=True)
    x = sqrt(a) * (cos(2 * s) * cell + sin(2 * s) * face)
    assert all(simplify(z) == 0 for z in x.diff(s) - generator * x)
    hodge = simplify((generator * x).dot(x.diff(s)) / 4)
    assert hodge == a

    currents = [-2 * boundary[i, -1] * x[i] * x[-1] for i in range(len(x))
                if boundary[i, -1] != 0]
    total = sum(currents)
    assert len(currents) == 4 and all(simplify(4 * j - total) == 0 for j in currents)
    assert simplify(total - (x[-1]**2).diff(s)) == 0

    for turns in (1, 2):
        end = turns * pi
        assert x.subs(s, end) == x.subs(s, 0)
        assert all(integrate(j, (s, 0, end)) == 0 for j in currents)
        assert integrate(hodge, (s, 0, end)) == pi * a * turns
        # The current sign only changes at the quarter-turns.
        gross = sum(abs(integrate(total, (s, k*pi/4, (k + 1)*pi/4)))
                    for k in range(4 * turns))
        assert gross == 4 * a * turns
        reversed_path = x.subs(s, end - s)
        reversed_hodge = simplify((generator * reversed_path).dot(reversed_path.diff(s)) / 4)
        assert integrate(reversed_hodge, (s, 0, end)) == -pi * a * turns
        for support in (1, Rational(3, 2)):
            print(f"stock={support}, turns={turns}: Hodge/pi={support * turns}, "
                  f"net=0, gross={gross.subs(a, support)}")


if __name__ == "__main__":
    main()
