"""Target-blind finite-order Q169 phase and integer-lattice audit.

All calculations use the filled K4 ascending simplex basis and exact integers.
"""

import json
from native_compare import CELLS, INDEX, N, matmul, mv
from native_integral_event import matrix, step


def image_mod(matrix_entries, modulus):
    """Enumerate the additive image of an integer matrix modulo modulus."""
    image = {tuple(0 for _ in range(N))}
    for j in range(N):
        column = tuple(matrix_entries[i][j] % modulus for i in range(N))
        image = {
            tuple((v[i] + k * column[i]) % modulus for i in range(N))
            for v in image for k in range(modulus)
        }
    return image


def main():
    a, aa, m = matrix()  # U_quarter=M/4
    h = [[2 * (i == j) + aa[i][j] for j in range(N)] for i in range(N)]
    assert matmul(m, m) == [[8 * h[i][j] for j in range(N)] for i in range(N)]
    assert matmul(h, h) == [[4 * (i == j) for j in range(N)] for i in range(N)]

    # A² modulo 2 is the all-ones 4x4 vertex block and zero elsewhere.
    assert all(
        aa[i][j] % 2 == int(i < 4 and j < 4)
        for i in range(N) for j in range(N)
    )
    half_image = image_mod(h, 2)
    quarter_image = image_mod(m, 4)
    assert len(half_image) == 2
    assert len(quarter_image) == 256
    doubles = {tuple((2 * q) % 4 for q in v) for v in quarter_image}
    assert len(doubles) == 2
    # Finite abelian group of exponent four: |image|=4^a 2^b,
    # |2 image|=2^a; hence a=1, b=6.
    assert len(quarter_image) == 4 * 2**6

    two_v0 = [0] * N
    two_v0[INDEX[(0,)]] = 2
    assert step(two_v0, m)[1] == "HOLD_NONINTEGRAL"
    half_next = [q // 2 for q in mv(h, two_v0)]
    assert half_next == [-1, 1, 1, 1] + [0] * (N - 4)
    assert [q // 2 for q in mv(h, half_next)] == two_v0
    assert sum(q * q for q in half_next) == 4
    assert sum(half_next[:4]) == 2

    # The ordinary simplex basis is outside the quarter admitted lattice.
    assert step([1] + [0] * (N - 1), m)[1] == "HOLD_NONINTEGRAL"
    assert len(CELLS) == N == 15

    result = {
        "source": "UD-Physics Q169/Q170 ledger v0.85; full filled K4, unit Euclidean, ascending orientations",
        "target_use": "none in construction, enumeration, or phase classification; historical alpha exposure disclosed",
        "continuous_family": "E(s)=I+sin(2s)A/2+(1-cos(2s))A^2/4",
        "finite_order_full_rank_integer_lattice_phases": [
            "2s=0 mod 2pi: identity",
            "2s=pi/2 mod 2pi: quarter orientation U, order 4",
            "2s=pi mod 2pi: half H, order 2",
            "2s=3pi/2 mod 2pi: inverse quarter U^-1, order 4",
        ],
        "phase_selection": "not unique; Q169/Q170 do not prescribe integer amplitude unit, admission criterion or event interval",
        "half": {
            "operator": "H=I+A^2/2=U^2",
            "gate": "sum of four vertex amplitudes even",
            "maximal_admitted_lattice_index_in_Z15": len(half_image),
            "quotient": "Z/2",
            "witness": "2v0 -> -v0+v1+v2+v3 -> 2v0",
        },
        "quarter": {
            "operator": "U=(4I+2A+A^2)/4",
            "gate": "(2A+A^2)x=0 mod4",
            "maximal_admitted_lattice_index_in_Z15": len(quarter_image),
            "quotient": "(Z/4) x (Z/2)^6",
            "witness": "4v0 four-step orbit; 2v0 fails quarter gate but passes half gate",
        },
        "relation": "L_quarter proper subset L_half; index [L_half:L_quarter]=128",
        "physical_promotion": 0,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
