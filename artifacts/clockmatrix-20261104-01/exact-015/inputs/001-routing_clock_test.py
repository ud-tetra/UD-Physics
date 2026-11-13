"""Exact counterchecks of the prepared-plane clock substitution."""
from fractions import Fraction


def readouts(q, p, mu):
    action = q * q + p * p
    omega = 2 + mu * action
    dq, dp = -omega * p, omega * q
    assert 2 * (q * dq + p * dp) == 0
    return (q * dp - p * dq) / action, p * p / action


if __name__ == "__main__":
    for mu in (Fraction(0), Fraction(1, 3), Fraction(31, 5)):
        rate_a, stock_a = readouts(Fraction(1), Fraction(0), mu)
        rate_b, stock_b = readouts(Fraction(0), Fraction(1), mu)
        assert rate_a == rate_b == 2 + mu
        assert stock_a == 0 and stock_b == 1
        if mu:
            squared_rates = [(2 + mu * action) ** 2 for action in (1, 2, 3)]
            assert squared_rates[2] - 2 * squared_rates[1] + squared_rates[0] == 2 * mu**2
    print("PASS: fixed-action phase pair and squared-rate curvature")
