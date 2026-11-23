"""Verify the LC schema and exact K-minus redistribution controls."""

import json
from itertools import combinations
from pathlib import Path

from jsonschema import Draft202012Validator
from sympy import eye, integrate, pi, simplify, sin, sqrt, symbols, zeros


def main():
    schema = Path(__file__).with_name("LC_CALIBRATION_BUNDLE_SCHEMA_v0.1.json")
    Draft202012Validator.check_schema(json.loads(schema.read_text()))
    print("O14 schema: Draft 2020-12 metaschema PASS")

    cells = ((0, 1, 2, 3), (0, 1, 2, 4))
    simplices = sorted(
        {face for cell in cells for size in range(1, 5) for face in combinations(cell, size)},
        key=lambda face: (len(face), face),
    )
    index = {face: i for i, face in enumerate(simplices)}
    boundary = zeros(len(simplices))
    for j, face in enumerate(simplices):
        if len(face) > 1:
            for k in range(len(face)):
                boundary[index[face[:k] + face[k + 1:]], j] = (-1)**k
    assert boundary**2 == zeros(len(simplices))
    generator = boundary - boundary.T
    laplacian = -generator**2
    assert laplacian.eigenvals() == {0: 1, 3: 8, 5: 14}
    ident = eye(len(simplices))
    for value, other in ((3, 5), (5, 3)):
        projector = laplacian * (laplacian - other * ident) / (value * (value - other))
        assert projector**2 == projector
        assert projector * generator == generator * projector
        assert generator.T * projector + projector * generator == zeros(len(simplices))
    print("K-minus: squared frequencies 0 (1), 3 (8), 5 (14); fixed-flow sector stocks conserved")

    s, duration, eps = symbols("s T eps", positive=True)
    shift = eps * sin(pi * s / duration)**2
    assert shift.subs(s, 0) == shift.subs(s, duration) == 0
    canonical = integrate((sqrt(3) - sqrt(5)) * shift, (s, 0, duration))
    generator_form = integrate((3 - 5) * shift / 2, (s, 0, duration))
    assert simplify(canonical - eps * duration * (sqrt(3) - sqrt(5)) / 2) == 0
    assert generator_form == -eps * duration / 2
    print("Driven control: canonical difference eps*T*(sqrt(3)-sqrt(5))/2; generator-form difference -eps*T/2")


if __name__ == "__main__":
    main()
