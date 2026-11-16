"""Enclose AW5 midpoint means with signed integer propagation and rational error bounds."""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, isqrt

from sympy import zeros

from residue import af, ext, ff, filled_basis, hub, leaves, matched, model, orthogonal

COUNT = 256
SCALE = 2**80
ORDER = 24
JITTER = Q(1, 1024)
GAMMA = Q(1, 512)
ETA, EPSILON, BIAS = Q(1, 4096), Q(1, 512), Q(1, 256)
ARM_ERROR = Q(1, 10**12)
THRESHOLD = Q(3, 64)
EXTERIOR = [filled_basis[2][i] for i in ext]


def sparse_rows(A):
    rows = [[] for _ in range(A.rows)]
    for (i, j), value in A.todok().items():
        rows[i].append((j, int(value)))
    # The generator is real skew, so the maximum absolute row and column sums agree.
    assert A.T == -A
    return rows


def vector(A, faces, sl, boundary_load):
    out = [0]*A.rows
    for i, face in zip(ext, EXTERIOR):
        value = 4*boundary_load[i]
        assert value in (-1, 0, 1)
        out[sl.start+faces.index(face)] = int(value)
    return out


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def apply(rows, vector):
    return [sum(weight*vector[j] for j,weight in row) for row in rows]


def step(rows, initial, denominator, order):
    term = list(initial)
    result = list(term)
    for k in range(1, order+1):
        term = [value//(denominator*k) for value in apply(rows, term)]
        result = [total+value for total,value in zip(result,term)]
    return result


def certify_error(a, dimension, order):
    assert 0 <= a < order+2
    tail = a**(order+1)/factorial(order+1)/(1-a/(order+2))
    # Each later polynomial term amplifies a rounding error by at most a term of exp(a).
    exp_upper = sum(a**k/factorial(k) for k in range(order+1))+tail
    # Norm of any grid state is at most 5 by induction if cumulative error <= 1.
    step_error = 5*tail+order*exp_upper*Q(isqrt(dimension)+1, SCALE)
    assert COUNT*step_error < ARM_ERROR


def mean(A, q, order=ORDER, exterior_indices=()):
    rows = sparse_rows(A)
    row_bound = max(sum(abs(weight) for _, weight in row) for row in rows)
    damping_denominator = GAMMA.denominator if exterior_indices else 1
    certify_error((row_bound+(GAMMA if exterior_indices else 0))/Q(8), A.rows, order)
    sq_norm = dot(q,q)
    assert 1 <= sq_norm <= 16
    # For face q, Aq is in neighboring degrees and is orthogonal to Pq=q.
    assert Q(dot(apply(rows,q),apply(rows,q)),sq_norm)+GAMMA**2 <= Q(9,4)**2
    if exterior_indices:
        rows = [[(j,weight*damping_denominator) for j,weight in row] for row in rows]
        for i in exterior_indices:
            rows[i].append((i,-GAMMA.numerator))
    current = step(rows, [coefficient*SCALE for coefficient in q], 16*damping_denominator, order)
    total = dot(q,current)
    for _ in range(COUNT-1):
        current = step(rows, current, 8*damping_denominator, order)
        total += dot(q,current)
    return Q(total, COUNT*SCALE*sq_norm)


def refine(indices):
    return [tet for i,tet in enumerate(leaves) if i not in indices]+[
        face+(8+i,) for i in indices for face in combinations(leaves[i],3)
    ]


def harmonic_check(basis, D, A, face_slice, q_target, q_reference, indices):
    faces = basis[2]
    shell = zeros(len(faces), 1)
    for k in range(4):
        shell[faces.index(hub[:k]+hub[k+1:])] = (-1)**k
    h = shell-D*(D.T*D).inv(method="DM")*D.T*shell
    assert A[:,face_slice]*h == zeros(A.rows, 1)
    assert A.rows-A.to_DM().rank() == 2

    def residue(q):
        return dot(q[face_slice], h)**2/(dot(q,q)*h.dot(h))

    count = len(indices)
    assert residue(q_target) == Q(20-count,80)
    leakage = Q(1,120*(20-count)) if len({2,3}.intersection(indices)) == 1 else 0
    assert residue(q_reference) == leakage
    return leakage


def main():
    certify_error(Q(3,2),102,ORDER)
    filled_mean = mean(af, vector(af, filled_basis[2], ff, matched))
    loss = (2*ARM_ERROR+GAMMA*32+Q(9,2)*JITTER
            +2*(2*EPSILON+EPSILON**2+BIAS)+ETA*(32+2*JITTER)+Q(1,32))
    print(f"enclosure per midpoint mean: +/-{ARM_ERROR}; combined comparison loss: {loss}")
    minima = []
    max_leakage = 0
    for count in range(5):
        by_subset = []
        for indices in combinations(range(4),count):
            basis, D, A, face_slice = model(refine(indices))
            assert A.rows == 46+14*count
            q_target = vector(A,basis[2],face_slice,matched)
            q_reference = vector(A,basis[2],face_slice,orthogonal)
            max_leakage = max(max_leakage, harmonic_check(
                basis,D,A,face_slice,q_target,q_reference,indices))
            target = mean(A,q_target)
            reference = mean(A,q_reference)
            gap_filled, gap_reference = target-filled_mean-loss, target-reference-loss
            by_subset.append((min(gap_filled,gap_reference),indices,gap_filled,gap_reference))
        floor, indices, _, _ = min(by_subset)
        minima.append(floor)
        print(f"refined={count}; subsets={len(by_subset)}; "
              f"filled floor={float(min(row[2] for row in by_subset)):.10f}; "
              f"fixed-reference floor={float(min(row[3] for row in by_subset)):.10f}; "
              f"worst subset={indices}")
    bound = min(minima)
    assert bound >= THRESHOLD
    assert max_leakage == Q(1,2040)
    print(f"maximum fixed-reference harmonic leakage {max_leakage}")
    shortened = Q(7,100)
    print(f"uniform lower bound {bound} = {float(bound):.10f}")
    print(f"headroom above 3/64 = {float(bound-THRESHOLD):.10f}")
    if bound >= shortened:
        print(f"uniform outward-rounded lower bound {shortened}")
    correlated_allowance = Q(19,320)
    correlated_bound = bound+Q(1,32)-correlated_allowance
    assert correlated_bound >= THRESHOLD
    print(f"conditional floor at joint noise proxy factor 361/100: {float(correlated_bound):.10f}")


if __name__ == "__main__":
    main()
