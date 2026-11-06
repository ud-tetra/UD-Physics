"""Exact topology controls for a proposed native-to-image readout; no sky data."""
from collections import deque
from fractions import Fraction


def components(cells, neighbors):
    remaining = set(cells)
    count = 0
    while remaining:
        count += 1
        seed = remaining.pop()
        queue = deque([seed])
        while queue:
            x, y = queue.popleft()
            for dx, dy in neighbors:
                v = (x + dx, y + dy)
                if v in remaining:
                    remaining.remove(v)
                    queue.append(v)
    return count


FOUR = ((1, 0), (-1, 0), (0, 1), (0, -1))
EIGHT = tuple((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)


def betti(mask):
    """Foreground 4-connectivity; background 8-connectivity; zero exterior."""
    h, w = len(mask), len(mask[0])
    assert h and w and all(len(row) == w for row in mask)
    fg = {(x, y) for y in range(h) for x in range(w) if mask[y][x]}
    bg = {(x, y) for y in range(-1, h + 1) for x in range(-1, w + 1)
          if not (0 <= x < w and 0 <= y < h and mask[y][x])}
    # Border padding forms the exterior background component.
    return components(fg, FOUR), components(bg, EIGHT) - 1


def threshold(a, cut):
    return [[int(v >= cut) for v in row] for row in a]


def block_mean(a):
    return [[sum((Fraction(v) for row in a for v in row), Fraction(0)) /
             (len(a) * len(a[0]))]]


if __name__ == "__main__":
    # Same K4 vertex amplitudes, two unselected vertex-to-pixel assignments.
    vertex = (1, 1, 0, 0)
    adjacent = [[vertex[0], vertex[1]], [vertex[2], vertex[3]]]
    diagonal = [[vertex[0], vertex[2]], [vertex[3], vertex[1]]]
    assert betti(threshold(adjacent, Fraction(1, 2))) == (1, 0)
    assert betti(threshold(diagonal, Fraction(1, 2))) == (2, 0)

    ring = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert betti(threshold(ring, Fraction(1, 2))) == (1, 1)
    coarse = block_mean(ring)
    assert coarse == [[Fraction(8, 9)]]
    assert betti(threshold(coarse, Fraction(1, 2))) == (1, 0)
    assert betti(threshold(coarse, Fraction(9, 10))) == (0, 0)
    print("PASS: exact layout, hole-loss, and threshold controls")
