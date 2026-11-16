"""Certify the depth-three sampled contrast for all independently varying arm damping."""
from itertools import combinations

from check_refinement_sweep import (
    ARM_ERROR, BIAS, EPSILON, ETA, EXTERIOR, GAMMA, JITTER, THRESHOLD, Q, af, ff,
    filled_basis, leaves, matched, mean, model, orthogonal, vector,
)


def endpoints(A, faces, face_slice, load):
    q = vector(A,faces,face_slice,load)
    exterior = [face_slice.start+faces.index(face) for face in EXTERIOR]
    return (mean(A,q,order=48), mean(A,q,order=48,exterior_indices=exterior))


def main():
    cells, vertex = list(leaves), 8
    for _ in range(3):
        refined = []
        for cell in cells:
            refined.extend(face+(vertex,) for face in combinations(cell,3))
            vertex += 1
        cells = refined
    basis, _, A, faces = model(cells)
    target = endpoints(A,basis[2],faces,matched)
    filled = endpoints(af,filled_basis[2],ff,matched)
    reference = endpoints(A,basis[2],faces,orthogonal)
    # Each arm's mean second derivative in gamma is bounded by the
    # mean squared sample time, at most 32**2/3 on the midpoint grid.
    interpolation_loss = GAMMA**2*32**2/12
    assert interpolation_loss == Q(1,3072)
    loss = (2*ARM_ERROR+interpolation_loss+Q(9,2)*JITTER
            +2*(2*EPSILON+EPSILON**2+BIAS)+ETA*(32+2*JITTER)+Q(1,32))
    floors = [min(target)-max(control)-loss for control in (filled,reference)]
    assert min(floors) > THRESHOLD
    for name, floor in zip(("filled","fixed reference"),floors):
        print(f"depth 3 damped floor vs. {name}: {float(floor):.10f}")
    print("PASS: original threshold, independently varying arm damping in [0, 1/512]")


if __name__ == "__main__":
    main()
