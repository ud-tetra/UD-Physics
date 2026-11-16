"""Replay the originally declared acquisition window on uniform AW5 depths two and three."""
from itertools import combinations

from check_refinement_sweep import (
    ARM_ERROR, BIAS, EPSILON, ETA, GAMMA, JITTER, THRESHOLD, Q, af, ff,
    filled_basis, leaves, matched, mean, model, orthogonal, vector,
)


def main():
    filled = mean(af, vector(af, filled_basis[2], ff, matched))
    loss = (2*ARM_ERROR+GAMMA*32+Q(9,2)*JITTER
            +2*(2*EPSILON+EPSILON**2+BIAS)+ETA*(32+2*JITTER)+Q(1,32))
    cells = list(leaves)
    vertex = 8
    for depth in range(1,4):
        refined = []
        for cell in cells:
            refined.extend(face+(vertex,) for face in combinations(cell,3))
            vertex += 1
        cells = refined
        if depth == 1:
            continue
        basis, _, A, faces = model(cells)
        target = mean(A, vector(A,basis[2],faces,matched), order=48)
        reference = mean(A, vector(A,basis[2],faces,orthogonal), order=48)
        floor = min(target-filled,target-reference)-loss
        if depth == 2:
            assert floor > THRESHOLD
        if depth == 3:
            assert floor < THRESHOLD
        print(f"depth {depth}, states {A.rows}: "
              f"undamped gaps {float(target-filled):.10f}, {float(target-reference):.10f}; "
              f"budgeted minimum {float(floor):.10f}")


if __name__ == "__main__":
    main()
