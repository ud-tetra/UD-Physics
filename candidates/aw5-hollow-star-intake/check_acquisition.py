"""Replay the exact error budget for the AW5 sampled acquisition."""
from fractions import Fraction as Q
from sympy import sqrt

T, N = 32, 256
j, gamma = Q(1, 1024), Q(1, 512)
epsilon, eta, beta = Q(1, 512), Q(1, 4096), Q(1, 256)
sigma, adverse_noise = Q(1, 16), Q(1, 32)
assert 5 + sqrt(5) + gamma**2 < Q(29, 4) < Q(27, 10)**2
sampling = Q(29, 48)*Q(T, N)**2 + Q(27, 5)*j
mismatch = 2*(2*epsilon + epsilon**2 + beta) + eta*(T+2*j)
exponent = N*adverse_noise**2/(4*sigma**2)
assert sampling < Q(1, 64) and mismatch < Q(1, 32)
assert exponent == 16
assert Q(1, 8)-Q(1, 64)-Q(1, 32)-adverse_noise == Q(3, 64)
print(f"PASS: sampling={sampling}, mismatch={mismatch}, exponent={exponent}, margin>=3/64")
