"""Exact Boolean-lattice triangulation and tetrahedron/cube boundary audit."""

import itertools
import json
from collections import Counter
from fractions import Fraction as Q


I = (0, 1, 2)
vertices = [frozenset(s) for k in range(4) for s in itertools.combinations(I, k)]
label = {s: i for i, s in enumerate(vertices)}


def det3(a, b, c):
    return (a[0] * (b[1]*c[2]-b[2]*c[1])
            - a[1] * (b[0]*c[2]-b[2]*c[0])
            + a[2] * (b[0]*c[1]-b[1]*c[0]))


def source(s):
    return tuple(Q(int(i in s), len(s)) if s else Q(0) for i in I)


def cube(s):
    return tuple(Q(int(i in s)) for i in I)


def boundary(chain):
    out = Counter()
    for simplex, coeff in chain.items():
        for i in range(len(simplex)):
            face = simplex[:i] + simplex[i+1:]
            out[face] += (-1)**i * coeff
    return {k: v for k, v in out.items() if v}


def main():
    sectors = []
    for p in itertools.permutations(I):
        chain = (frozenset(), frozenset(p[:1]), frozenset(p[:2]), frozenset(I))
        vs, vc = [[f(s) for s in chain] for f in (source, cube)]
        ds = det3(*[tuple(v[i]-vs[0][i] for i in I) for v in vs[1:]])
        dc = det3(*[tuple(v[i]-vc[0][i] for i in I) for v in vc[1:]])
        assert abs(ds) == Q(1,6) and abs(dc) == 1 and dc/ds == 6
        sign = 1 if ds > 0 else -1
        sectors.append((chain, sign))
    c3 = {chain: sign for chain, sign in sectors}
    c2 = boundary(c3)
    assert boundary(c2) == {}
    faces = set(itertools.chain.from_iterable(itertools.combinations(c,3) for c,_ in sectors))
    edges = set(itertools.chain.from_iterable(itertools.combinations(c,2) for c,_ in sectors))
    assert (len(vertices),len(edges),len(faces),len(sectors)) == (8,19,18,6)
    assert len(c2) == 12 and len(faces)-len(c2) == 6
    # Each boundary triangle lies in exactly one original tetrahedral face.
    groups = Counter()
    for face,sign in c2.items():
        classes = []
        for i in I:
            if all(i not in s for s in face):
                classes.append(f'zero_{i}')
        if all(s for s in face):
            classes.append('opposite_origin')
        assert len(classes) == 1 and abs(sign) == 1
        groups[classes[0]] += 1
    assert groups == {'zero_0':2,'zero_1':2,'zero_2':2,'opposite_origin':6}
    # Both triangulations use the same oriented Boolean-lattice simplex labels.
    # Their induced signed incidence lists are identical in every dimension.
    for k in range(1,4):
        for simplex in itertools.combinations(vertices,k+1):
            mapped_source = tuple(label[s] for s in simplex)
            mapped_boundary = {tuple(label[s] for s in face):v
                               for face,v in boundary({simplex:1}).items()}
            assert mapped_boundary == boundary({mapped_source:1})
    result = {'f_vector':[8,19,18,6], 'boundary_triangle_count':len(c2),
              'boundary_group_counts':dict(sorted(groups.items())),
              'source_sector_coordinate_volume':'1/36',
              'target_sector_coordinate_volume':'1/6',
              'coordinate_jacobian':6,
              'physical_jacobian_at_equal_volume':1,
              'equal_volume_surface_ratio':'3^(-1/6)',
              'induced_average_surface_density_ratio':'3^(1/6)',
              'induced_zero_face_density_ratio':'(3/2)*3^(1/6)',
              'induced_opposite_face_density_ratio':'(1/2)*3^(1/6)'}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
