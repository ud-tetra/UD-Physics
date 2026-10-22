"""Exact instructional calculations; no empirical or native-UD identification."""
import json
from fractions import Fraction
from math import gcd, lcm


def orbit(modulus, stride):
    value, seen = 0, set()
    while value not in seen:
        seen.add(value)
        value = (value + stride) % modulus
    return len(seen)


omega = {(label, mask) for label in range(1, 25) for mask in range(8)}
event = {(1, mask) for mask in range(1, 8)}
assert event <= omega
assert len(omega) == 24 * 8 == 192 == 2**6 * 3
assert len(event) == 8 - 1 == 7
assert Fraction(len(event), len(omega)) == Fraction(7, 192)
assert orbit(8, 3) == 8 // gcd(8, 3) == 8
assert orbit(12, 8) == 12 // gcd(12, 8) == 3
state, ticks = (0, 0), 0
while True:
    ticks += 1
    state = ((state[0] + 3) % 8, (state[1] + 8) % 12)
    if state == (0, 0):
        break
assert ticks == lcm(8, 3) == 24
try:
    pow(8, -1, 12)
except ValueError:
    inverse_exists = False
else:
    inverse_exists = True
assert not inverse_exists
print(json.dumps({"count_ratio": str(Fraction(len(event), len(omega))),
                  "factorization_192": {"2": 6, "3": 1},
                  "orbit_lengths": [orbit(8, 3), orbit(12, 8)],
                  "joint_period_in_common_ticks": ticks,
                  "inverse_8_mod_12_exists": inverse_exists,
                  "scope": "Illustrative target-exposed construction; no physical identification",
                  "status": "PASS"}, indent=2))
