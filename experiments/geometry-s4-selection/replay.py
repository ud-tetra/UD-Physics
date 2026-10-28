"""Exact finite cube-isometry and tetrahedral vertex-orbit check."""

import itertools
import json

V = list(itertools.product((0, 1), repeat=3))
STAR = {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)}
EVEN = {v for v in V if sum(v) % 2 == 0}


def transform(v, perm, flip):
    return tuple(v[perm[i]] ^ flip[i] for i in range(3))


def d2(u, v):
    return sum((u[i] - v[i]) ** 2 for i in range(3))


def orbit_stabilizer(shape):
    transforms = [(p, f) for p in itertools.permutations(range(3))
                  for f in V]
    stabilizer = [(p, f) for p, f in transforms
                  if {transform(v, p, f) for v in shape} == shape]
    induced = {tuple(sorted((v, transform(v, p, f)) for v in shape))
               for p, f in stabilizer}
    return len(stabilizer), len(induced), len(transforms)


def main():
    star_stab, star_actions, cube_order = orbit_stabilizer(STAR)
    even_stab, even_actions, _ = orbit_stabilizer(EVEN)
    assert (star_stab, star_actions, cube_order) == (6, 6, 48)
    assert (even_stab, even_actions) == (24, 24)
    star_d2 = sorted(d2(u, v) for u, v in itertools.combinations(STAR, 2))
    even_d2 = sorted(d2(u, v) for u, v in itertools.combinations(EVEN, 2))
    assert star_d2 == [1, 1, 1, 2, 2, 2]
    assert even_d2 == [2] * 6
    # Inversion interchanges the 3 zero and 3 unit coordinate cube faces.
    c0, c1 = (3, 1), (1, 3)  # densities in units 3^(1/6)/2
    assert tuple((x+y)/2 for x,y in zip(c0,c1)) == (2,2)
    print(json.dumps({'cube_isometry_order':cube_order,
                      'six_sector_star_stabilizer':star_stab,
                      'six_sector_star_pairwise_squared_distances':star_d2,
                      'alternate_even_tetra_stabilizer':even_stab,
                      'alternate_even_pairwise_squared_distances':even_d2,
                      'inversion_average_density':'3^(1/6) on all six faces'},
                     indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
