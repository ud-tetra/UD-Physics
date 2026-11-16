"""Numerical synthetic replay of the two-state certificate."""
from fractions import Fraction
import numpy as np
from scipy.linalg import expm, logm

H = 1/8
RADIUS = 1/4
GAMMA = 1/1024
TARGET = np.array([[-GAMMA, -1], [1, 0]])
GUARD = 1/32768
norm = lambda matrix: np.linalg.norm(matrix, ord=2)

assert Fraction(1, 8192)*Fraction(1, 8)*Fraction(3, 4) == Fraction(3, 262144)


def certify(generator):
    transition = expm(H*generator)
    initial = np.array([[1, 1/128], [1/256, 1]])
    # Offset cancellation in + and - preparations with an identical affine term.
    offset = np.array([[1/100], [-1/100]])
    endpoint = ((transition@initial + offset) - (-transition@initial + offset))/2
    estimate = np.linalg.solve(initial.T, endpoint.T).T
    d_x = d_y = 1/2**23
    epsilon = (d_y+norm(estimate)*d_x)/(np.linalg.svd(initial, compute_uv=False).min()-d_x)
    assert norm(estimate-np.eye(2))+epsilon <= RADIUS
    rho = epsilon/(H*(1-RADIUS))
    fitted = logm(estimate).real/H
    coupling_error = max(abs(fitted[0, 1]+1), abs(fitted[1, 0]-1))
    sym_max = np.linalg.eigvalsh((fitted+fitted.T)/2).max()
    gamma = fitted[1, 1]-fitted[0, 0]
    return (norm(fitted-TARGET)+rho <= 1/4096
            and coupling_error+rho <= 1/49152 and sym_max+rho <= 0
            and gamma-2*rho >= 0 and gamma+2*rho <= 1/512), rho


guarded = TARGET-GUARD*np.eye(2)
polarity_error = guarded.copy()
polarity_error[0, 1] = 1
gain_error = guarded.copy()
gain_error[0, 1] -= 1/16384
for name, operator, expected in (("guarded nominal", guarded, True),
                                 ("wrong polarity", polarity_error, False),
                                 ("excess coupling error", gain_error, False)):
    accepted, rho = certify(operator)
    assert accepted == expected
    print(f"{name}: {'PASS' if accepted else 'FAIL'} synthetic certificate; rho={rho:.3e}")
