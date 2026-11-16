"""Check the sufficient observation window with exact rational arithmetic."""
from sympy import Rational as Q, sqrt

# Positive squared frequencies from the filled and hollow characteristic polynomials.
squared = (2, 3, 4, 5, 6, (9-sqrt(17))/2, (9+sqrt(17))/2,
           5-sqrt(5), 5+sqrt(5))
assert all(q > 1 for q in squared)

time = 32
damping = Q(1, 512)
stationary_weight = Q(1, 4)
assert stationary_weight - Q(2, time) - damping*time == Q(1, 8)
print("PASS: positive frequency floor > 1; guaranteed contrast >= 1/8")
