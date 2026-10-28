"""Numerical cross-check of the exact geometry identities in README.md."""

import json
import math


def main():
    ga = 3 ** 0.25 / 2
    gs = math.sqrt(math.sqrt(3) / 6)
    gv = (math.sqrt(2) / 12) ** (1 / 3)
    rho = 6 * gv**2 / math.sqrt(3)
    assert math.isclose(ga**2, math.sqrt(3) / 4, rel_tol=1e-14)
    assert math.isclose(6 * gs**2, math.sqrt(3), rel_tol=1e-14)
    assert math.isclose(gv**3, math.sqrt(2) / 12, rel_tol=1e-14)
    assert math.isclose(rho, 3 ** (-1 / 6), rel_tol=1e-14)
    assert math.isclose(gs / gv, 3 ** (1 / 12), rel_tol=1e-14)
    assert math.isclose((math.sqrt(3) ** 3 / (math.sqrt(2) / 12) ** 2) / 216, math.sqrt(3), rel_tol=1e-14)
    assert math.isclose(6 * ga**2 / math.sqrt(3), 1.5, rel_tol=1e-14)
    result = dict(face_edge_ratio=ga, surface_edge_ratio=gs, volume_edge_ratio=gv,
                  equal_volume_surface_ratio=rho, boundary_shortfall=1-rho,
                  surface_to_volume_edge_ratio=gs/gv,
                  equal_face_area_total_surface_ratio=1.5,
                  exact_forms=['3^(1/4)/2', 'sqrt(sqrt(3)/6)',
                               '(sqrt(2)/12)^(1/3)', '3^(-1/6)', '3^(1/12)'])
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
