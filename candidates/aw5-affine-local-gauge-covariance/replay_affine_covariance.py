"""Replay the gauge basis identities using signed integer simplex boundaries."""

from itertools import combinations
import json


def boundary_columns(lower, upper, lower_offset):
    index = {simplex: lower_offset + row for row, simplex in enumerate(lower)}
    return [
        {index[simplex[:i] + simplex[i + 1:]]: (-1) ** i for i in range(len(simplex))}
        for simplex in upper
    ]


def verify(cells):
    strata = [sorted({s for cell in cells for s in combinations(cell, k)}) for k in range(1, 5)]
    sizes = [len(grade) for grade in strata]
    offsets = [sum(sizes[:k]) for k in range(4)]
    dimension = sum(sizes)
    boundary = [{} for _ in strata[0]]
    for k in range(1, 4):
        boundary.extend(boundary_columns(strata[k-1], strata[k], offsets[k-1]))

    def apply_a(vector):
        down = [0] * dimension
        up = [0] * dimension
        for col, entries in enumerate(boundary):
            for row, sign in entries.items():
                down[row] += sign * vector[col]
                up[col] += sign * vector[row]
        return [u - d for u, d in zip(up, down)]

    def affine(state, connection, rate):
        return [
            v + w for v, w in zip(apply_a([x - y for x, y in zip(state, connection)]), rate)
        ]

    for entries in boundary:
        twice = [0] * dimension
        for col, weight in entries.items():
            for row, sign in boundary[col].items():
                twice[row] += weight * sign
        assert not any(twice)

    state = list(range(dimension))
    connection = [i if offsets[1] <= i < offsets[2] else 0 for i in range(dimension)]
    rate = [-x for x in connection]
    baseline = affine(state, connection, rate)
    zero = [0] * dimension
    for vertex in range(sizes[0]):
        gauge = [entries.get(vertex, 0) if offsets[1] <= i < offsets[2] else 0
                 for i, entries in enumerate(boundary)]
        shifted_state = [x + y for x, y in zip(state, gauge)]
        shifted_connection = [x + y for x, y in zip(connection, gauge)]
        shifted_rate = [x + y for x, y in zip(rate, gauge)]
        assert affine(shifted_state, shifted_connection, rate) == baseline
        assert affine(state, connection, shifted_rate) == [x + y for x, y in zip(baseline, gauge)]
        assert affine(zero, zero, gauge) == gauge and any(gauge)  # homogeneous no-go at zero
        assert any(apply_a(gauge))  # the unmodified generator also fails the static shift
        assert all(sum(sign * gauge[row] for row, sign in face.items()) == 0
                   for face in boundary[offsets[2]:offsets[3]])
    return {"dimension": dimension, "vertex_basis_shifts": sizes[0], "result": "PASS_EXACT"}


def main():
    hub = (0, 1, 2, 3)
    leaves = [tuple(sorted((set(hub) - {i}) | {4 + i})) for i in hub]
    complexes = {
        "tetrahedron": [hub],
        "bipyramid": [hub, (0, 1, 2, 4)],
        "aw5_filled": [hub, *leaves],
        "aw5_hollow": leaves,
    }
    print(json.dumps({name: verify(cells) for name, cells in complexes.items()}, indent=2))


if __name__ == "__main__":
    main()
