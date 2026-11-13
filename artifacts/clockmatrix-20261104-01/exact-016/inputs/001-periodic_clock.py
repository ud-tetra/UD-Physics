"""Exact initial-time diagnostics on the periodic scalar incidence lane."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json


DIRECTIONS = tuple(d for d in product((0, 1), repeat=3) if any(d))
TETRAHEDRON = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))


def edges_at(vertex):
    for direction in DIRECTIONS:
        yield vertex, tuple(a + b for a, b in zip(vertex, direction))
        yield tuple(a - b for a, b in zip(vertex, direction)), vertex


def vertex_to_edge(state, local=False):
    result = defaultdict(F)
    for vertex, value in state.items():
        for edge in edges_at(vertex):
            if not local or all(endpoint in TETRAHEDRON for endpoint in edge):
                result[edge] += value if vertex == edge[0] else -value
    return result


def edge_to_vertex(state):
    result = defaultdict(F)
    for (tail, head), value in state.items():
        result[tail] -= value
        result[head] += value
    return result


def dot(a, b):
    return sum(value * b.get(cell, 0) for cell, value in a.items())


def run():
    a, b = TETRAHEDRON[1:3]
    v = {a: F(1), b: F(-1)}
    initial_edge_rate = vertex_to_edge(v)
    h = {cell: value / 2 for cell, value in vertex_to_edge(v, local=True).items()}
    outside = {cell: value for cell, value in initial_edge_rate.items() if cell not in h}
    acceleration = edge_to_vertex(initial_edge_rate)
    residual = {cell: value + 15 * v.get(cell, 0) for cell, value in acceleration.items()}
    assert dot(v, v) == dot(h, h) == 2
    assert dot(initial_edge_rate, h) / 2 == 2
    assert dot(outside, outside) == 22
    assert dot(v, acceleration) / 2 == -15
    assert residual and dot(residual, residual) > 0

    # Reflection exchanges the two seed vertices and preserves the squared readout.
    center = tuple(F(i + j, 2) for i, j in zip(a, b))

    def radius_squared(point):
        delta = [i - j for i, j in zip(point, center)]
        return dot_vector(delta) / 2 - sum(delta) ** 2 / 8

    vertex_term = sum(v[cell] * acceleration[cell] * radius_squared(cell) for cell in v)
    edge_term = sum(value**2 * radius_squared(tuple(F(i + j, 2) for i, j in zip(*edge)))
                    for edge, value in initial_edge_rate.items())
    assert vertex_term + edge_term > 0
    return {
        "outside_stock_quadratic_coefficient": str(dot(outside, outside) / 2),
        "local_q_second_derivative": str(dot(v, acceleration) / 2),
        "local_p_first_derivative": str(dot(initial_edge_rate, h) / 2),
        "global_scalar_closure_residual_norm_squared": str(dot(residual, residual)),
        "mean_squared_radius_initial": str(radius_squared(a)),
        "mean_squared_radius_quadratic_coefficient": str((vertex_term + edge_term) / 2),
    }


def dot_vector(values):
    return sum(value**2 for value in values)


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
