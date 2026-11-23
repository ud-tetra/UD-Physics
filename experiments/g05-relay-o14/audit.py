"""Replay the note 11231155 controls using exact integer and fraction arithmetic."""

from fractions import Fraction
from itertools import combinations, product


def main():
    windings = list(product(range(3), repeat=2))
    action_weights = (Fraction(1, 3), Fraction(2, 3))
    collisions = []
    for left, right in combinations(windings, 2):
        if sum(left) != sum(right):
            continue
        delta_a, delta_b = (i - j for i, j in zip(left, right))
        delta_action_over_pi = action_weights[0] * delta_a + action_weights[1] * delta_b
        # Zero elapsed difference would imply the following squared equality.
        assert 5 * delta_a**2 != 3 * delta_b**2
        assert delta_action_over_pi != 0
        collisions.append((left, right))
        print(f"{left} vs {right}: dq=0, dI/pi={delta_action_over_pi}, dT!=0")

    assert len(windings) == 9 and len(collisions) == 5
    energy_row = (1, 2, -2)
    period_row = (0, 0, 1)
    action_row = tuple(e + t for e, t in zip(energy_row, period_row))
    assert action_row == (1, 2, -1)
    print(f"histories={len(windings)}, collisions={len(collisions)}, equal-time collisions=0")
    print(f"O14 energy + period rows: {action_row}")


if __name__ == "__main__":
    main()
