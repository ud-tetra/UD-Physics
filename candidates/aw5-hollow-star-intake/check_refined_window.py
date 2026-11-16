"""Exact one-leaf AW5 certificate for the sampled contrast budget."""
from itertools import combinations

from sympy import Poly, Rational as Q, symbols, zeros

from residue import af, ff, filled_basis, hub, leaves, model

EXTERIOR = ((0,1,6),(0,1,7),(0,2,5),(0,2,7),(0,3,5),(0,3,6),
            (1,2,4),(1,2,7),(1,3,4),(1,3,6),(2,3,4),(2,3,5))
SIGNS = (1,-1,-1,1,1,-1,1,-1,-1,1,1,-1)
T, N, JITTER, GAMMA = 32, 256, Q(1,1024), Q(1,512)


def drive(A, face_slice, faces, coordinates):
    q = zeros(A.rows, 1)
    for face, value in zip(EXTERIOR, coordinates):
        q[face_slice.start+faces.index(face)] = value
    return q


def spectral_check(A, expected_nullity):
    x = symbols("x")
    p = Poly((-A**2).charpoly(x).as_expr(), x)
    assert p.nth(expected_nullity) != 0
    p = p.exquo(Poly(x**expected_nullity, x))
    while p.eval(1) == 0:
        p = p.exquo(Poly(x-1,x))
    assert p.count_roots(0,1) == 0
    degree = max(sum(abs(v) for v in A.row(j)) for j in range(A.rows))
    assert degree <= 8
    print(f"PASS: nullity {expected_nullity}; positive frequencies in [1, {degree}]")


cells = leaves[1:]+[face+(8,) for face in combinations(leaves[0],3)]
basis,D,ar,fr = model(cells)
q_ref = drive(ar, fr, basis[2], SIGNS)
q_filled = drive(af, ff, filled_basis[2], SIGNS)
q_null = drive(ar, fr, basis[2], (1,1)+(0,)*10)
shell = zeros(D.rows,1)
for j in range(4):
    shell[basis[2].index(hub[:j]+hub[j+1:])] = (-1)**j
h = shell-D*(D.T*D).inv(method="DM")*D.T*shell
assert ar[:,fr]*h == zeros(ar.rows,1)
assert q_ref[fr,0].dot(h)**2/(q_ref.dot(q_ref)*h.dot(h)) == Q(19,80)
assert q_null[fr,0].dot(h) == 0
spectral_check(af, 1)
spectral_check(ar, 2)
for label,A,q in (("refined",ar,q_ref),("filled",af,q_filled),("orthogonal",ar,q_null)):
    derivative_sq = (A*q).dot(A*q)/q.dot(q)+GAMMA**2
    assert derivative_sq <= Q(9,4)**2
    print(f"PASS: {label} derivative bound 9/4")

sin_floor = Q(1,16)-Q(1,16)**3/6
oscillation_loss = (2-Q(19,80))/(2*N*sin_floor)
damping_loss = GAMMA*T
timing_loss = Q(9,2)*JITTER
epsilon, eta, beta = Q(1,512), Q(1,4096), Q(1,256)
mismatch_loss = 2*(2*epsilon+epsilon**2+beta)+eta*(T+2*JITTER)
noise_loss = Q(1,32)
lower = Q(19,80)-oscillation_loss-damping_loss-timing_loss-mismatch_loss-noise_loss
assert lower >= Q(3,64)
print(f"PASS: contrast lower bound {lower} = {float(lower):.9f}")
print(f"PASS: headroom above frozen 3/64 = {lower-Q(3,64)}")
