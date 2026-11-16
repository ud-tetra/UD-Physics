"""Check native-to-bench scales and a sufficient AW5 entry-error bound."""
from fractions import Fraction

from residue import af, ah


def max_degree(operator):
    return max(sum(entry != 0 for entry in operator.row(i))
               for i in range(operator.rows))


for name, operator in (("filled", af), ("hollow", ah)):
    degree = max_degree(operator)
    assert degree == max_degree(operator.T) == 6
    print(f"{name}: {operator.rows} states, maximum row and column degree {degree}")

tau = Fraction(1, 1000)
assert 32*tau == Fraction(4, 125)
assert 1/(tau/8) == 8000
assert tau/1024 == Fraction(1, 1024000)
assert 1/(4096*tau) == Fraction(125, 512)
assert 1/(512*tau) == Fraction(125, 64)
entry_bound = Fraction(1, 2*6*4096)
assert 6*entry_bound == Fraction(1, 8192)
print("PASS: 1 ms/native, 32 ms window, 8 ksample/s, 1/1024 ms timing bound")
print(f"Half-budget per supported entry: {entry_bound}")
