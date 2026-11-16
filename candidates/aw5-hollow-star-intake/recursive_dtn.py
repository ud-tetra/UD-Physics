"""Boundary Schur reduction and certified Fourier inversion for uniform AW5."""
from itertools import combinations
from fractions import Fraction as Q
from math import factorial, floor, pi

import numpy as np

from residue import af, ext, ff, filled_basis, hub, leaves, matched, model, orthogonal

PERIOD = 256
ALPHA = 1/16
COUNT = 256
K = 8192
GAMMA = 1/512
U = 2.0**-53
TET = (0,1,2,3)


def boundary_data(cells):
    return [sorted({q for tet in cells for q in combinations(tet,k)}) for k in range(1,4)]


def flat(layers):
    return [q for layer in layers for q in layer]


def skeleton(layers):
    faces = flat(layers)
    index = {q:i for i,q in enumerate(faces)}
    A = np.zeros((len(faces),len(faces)))
    for q,i in index.items():
        if len(q)>1:
            for k in range(len(q)):
                j=index[q[:k]+q[k+1:]]
                A[i,j]=(-1)**k
                A[j,i]=-A[i,j]
    return A


def shifted(s, A):
    return s[:,None,None]*np.eye(len(A))-A


def absolute_entries(M):
    return np.max(np.abs(M),axis=(-1,-2))


def schur(K, kept):
    removed = [i for i in range(K.shape[-1]) if i not in kept]
    A = K[:,kept][:,:,kept]
    if not removed:
        return A, np.zeros(len(A))
    B = K[:,kept][:,:,removed]
    C = K[:,removed][:,:,kept]
    D = K[:,removed][:,:,removed]
    Z = np.linalg.solve(D,C)
    S = A-B@Z
    residual = D@Z-C
    # The first correction makes the computed Z an exact solution. The
    # second is the roundoff in forming A-BZ. Both act on this skeleton.
    n = len(removed)
    m = len(kept)
    correction = (n+m)*(absolute_entries(residual) +
        128*(n+1)*U*(n*(absolute_entries(D)+absolute_entries(B))*absolute_entries(Z)
                     +absolute_entries(A)+absolute_entries(C)+absolute_entries(S)+1))
    return S, correction


PARENT = boundary_data([TET])
CHILDREN = [face+(4,) for face in combinations(TET,3)]
CHILD_SKELETON = boundary_data(CHILDREN)
PORT_INDEX = [flat(CHILD_SKELETON).index(q) for q in flat(PARENT)]
CHILD_INDEX = [[flat(CHILD_SKELETON).index(q) for q in flat(boundary_data([cell]))]
               for cell in CHILDREN]
AW5 = boundary_data(leaves)
AW5_INDEX = [[flat(AW5).index(q) for q in flat(boundary_data([cell]))] for cell in leaves]
LEAF_A = skeleton(PARENT)
CONE_A = skeleton(CHILD_SKELETON)
AW5_A = skeleton(AW5)
EXTERIOR = [filled_basis[2][i] for i in ext]
AW5_FACES = [flat(AW5).index(q) for q in AW5[2]]
EXTERIOR_INDICES = [AW5[2].index(q) for q in EXTERIOR]


def assemble(s, base, delta, children, baseline_size):
    M = shifted(s,base)
    for index in children:
        M[:,np.ix_(index,index)[0],np.ix_(index,index)[1]] += delta
    # Includes shifted matrix and subtracting the standalone boundary block.
    return M, len(base)*128*U*(absolute_entries(M)+4*absolute_entries(delta)+baseline_size+1)


def leaf_schur_components(s, depth):
    baseline = shifted(s,LEAF_A)
    # Last simplex is the oriented tetrahedron. A[v3,v2] is its signed boundary.
    v = np.array([(-1)**(TET.index(next(i for i in TET if i not in face))) for face in PARENT[2]])
    w = np.r_[np.zeros(10),v]
    H = baseline+np.outer(w,w)/s[:,None,None]
    errors = [14*128*U*(absolute_entries(H)+absolute_entries(baseline)+1)]
    for _ in range(depth):
        M, assembly_error = assemble(s,CONE_A,H-baseline,CHILD_INDEX,absolute_entries(baseline))
        H, correction = schur(M,PORT_INDEX)
        errors.append(assembly_error+correction)
    return H-baseline, errors


def leaf_schur(s, depth):
    delta, errors = leaf_schur_components(s,depth)
    return delta, sum(4**(depth-i)*err for i,err in enumerate(errors))


def probe_vector(indices, count, coefficients):
    q = np.zeros(count)
    q[indices] = np.asarray(coefficients,dtype=float)
    return q


TARGET = [matched[i] for i in ext]
REFERENCE = [orthogonal[i] for i in ext]
HOLLOW_PROBES = np.column_stack([probe_vector(EXTERIOR_INDICES,len(AW5_FACES),weights)
                                for weights in (TARGET,REFERENCE)])
FILLED_PROBE = HOLLOW_PROBES[:,:1]
assert AW5[2] == filled_basis[2]


def response(s, matrix, probes, error, exterior, gamma, operator_norm=None):
    M = matrix.copy()
    M[:,exterior,exterior] += gamma
    rhs = np.broadcast_to(probes,(len(s),*probes.shape))
    X = np.linalg.solve(M,rhs)
    norms = (probes**2).sum(axis=0)
    values = np.einsum("ij,kij->kj",probes,X)/norms
    residual = np.max(abs(M@X-rhs),axis=1)
    m = M.shape[-1]
    # The diagonal shift, frequency representation and local Schur perturbations
    # are included in the lifted full-operator error. The solve residual
    # has support only on retained coordinates.
    error = error+128*m*U*(abs(s)+absolute_entries(M)+1)
    assert np.all(error<ALPHA)
    minimum = ALPHA if operator_norm is None else np.maximum(
        ALPHA, abs(s.imag)*(1-8*U)-operator_norm
    )[:,None]
    resid = residual + 128*(m+1)*U*(
        m*absolute_entries(M)[:,None]*np.max(abs(X),axis=1)+1)
    radius = (error[:,None]/(minimum*(minimum-error[:,None]))+
              np.sqrt(m)*resid/(np.sqrt(norms)*(minimum-error[:,None]))+
              128*m*U*(abs(values)+1))
    return values,radius


def phase_exponential(indices, period, real):
    # Arguments have magnitude < 4. The order-40 Taylor tail and
    # roundoff in this elementary recurrence are bounded in the receipt.
    reduced = (indices+period//2)%period-period//2
    x = real+1j*(2*pi/period)*reduced
    term = np.ones_like(x)
    value = term.copy()
    for k in range(1,41):
        term = term*x/k
        value += term
    return value


def midpoint_weights(indices):
    start = phase_exponential(indices,4096,ALPHA/16)
    step = phase_exponential(indices,2048,ALPHA/8)
    last = phase_exponential(indices,8,32*ALPHA)
    weights = start*(1-last)/(COUNT*(1-step))
    weights[1:] *= 2
    return weights


def invert_frequency():
    frequency = 2*pi*np.arange(K+1)/PERIOD
    weights = midpoint_weights(np.arange(K+1))
    averages = np.zeros((7,2,2))
    errors = np.zeros_like(averages)
    for start in range(0,K+1,128):
        sl = slice(start,min(start+128,K+1))
        s = ALPHA+1j*frequency[sl]
        for depth in (0,4,5,6):
            if depth:
                delta,err=leaf_schur(s,depth)
                M,rounding=assemble(s,AW5_A,delta,AW5_INDEX,absolute_entries(shifted(s,LEAF_A)))
                M,correction=schur(M,AW5_FACES)
                pr,err=HOLLOW_PROBES,4*err+rounding+correction
            else:
                M,err=schur(shifted(s,np.asarray(af,dtype=float)),list(range(ff.start,ff.stop)))
                pr=FILLED_PROBE
            for i,gamma in enumerate((0,GAMMA)):
                values,radius=response(s,M,pr,err,EXTERIOR_INDICES,gamma)
                smooth=values-1/s[:,None]+gamma/s[:,None]**2
                averages[depth,i,:pr.shape[1]] += (weights[sl,None]*smooth).real.sum(axis=0)/PERIOD
                errors[depth,i,:pr.shape[1]] += (abs(weights[sl,None])*radius).sum(axis=0)/PERIOD
    averages += np.array([1,1-16*GAMMA])[None,:,None]
    return averages,errors


def crosscheck():
    s = np.array([ALPHA, ALPHA+0.8j, 0.5+3.1j, 1+17j])
    cells, vertex = list(leaves), 8
    for depth in range(3):
        basis, _, A, faces = model(cells)
        exterior = [faces.start+basis[2].index(q) for q in EXTERIOR]
        probes = np.column_stack([probe_vector(exterior,A.rows,load)
                                 for load in (TARGET,REFERENCE)])
        delta, error = leaf_schur(s,depth)
        coarse, rounding = assemble(s,AW5_A,delta,AW5_INDEX,absolute_entries(shifted(s,LEAF_A)))
        reduced, correction = schur(coarse,AW5_FACES)
        direct = shifted(s,np.asarray(A,dtype=float))
        for gamma in (0,GAMMA):
            exact_structure, _ = response(s,direct,probes,np.zeros(len(s)),exterior,gamma)
            nested, radius = response(s,reduced,HOLLOW_PROBES,
                                      4*error+rounding+correction,EXTERIOR_INDICES,gamma)
            assert np.max(abs(nested-exact_structure)) < 1e-10
            assert np.all(abs(nested-exact_structure) <= radius)
        refined = []
        for cell in cells:
            refined.extend(face+(vertex,) for face in combinations(cell,3))
            vertex += 1
        cells = refined
    print("PASS: reduced transfer vs full matrices at depths 0–2, 4 frequencies and 2 damping values")


def common_radius():
    p = Q(157,50)
    # Alternating arctan bounds applied to Machin's formula.
    def atan_partial(x,n):
        return sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n))

    lower_pi = 16*atan_partial(Q(1,5),16)-4*atan_partial(Q(1,239),15)
    upper_pi = 16*atan_partial(Q(1,5),15)-4*atan_partial(Q(1,239),16)
    assert lower_pi > p
    assert max(abs(Q(pi)-lower_pi),abs(Q(pi)-upper_pi)) < Q(1,2**52)
    # The bound on A follows from B^2=0 and the maximum incidence degrees.
    assert max(2*(6+2*(3**6-1)),3*(6+4*(2**6-1)),8) < 55**2
    exp2 = sum(Q(2**n,factorial(n)) for n in range(16))+Q(2**16,factorial(16))/(1-Q(2,17))
    assert exp2 < Q(37,5)
    exp4 = sum(Q(4**n,factorial(n)) for n in range(20))+Q(4**20,factorial(20))/(1-Q(4,21))
    assert exp4 < 55
    alias_ratio = Q(1,8_000_000)
    assert sum(Q(16**n,factorial(n)) for n in range(33)) > 1/alias_ratio
    tail = Q(37,5)*Q(81,16)*PERIOD**2/((2*p)**3*K*K*(1-Q(56*PERIOD,2*K)/p))
    alias = ((2+Q(32,512))*alias_ratio/(1-alias_ratio)
             +Q(PERIOD,512)*alias_ratio/(1-alias_ratio)**2)
    # Rounded elementary weights and scalar summation use an additional
    # 1e-5 per arm, with the arithmetic assumptions stated in the receipt.
    assert tail+alias+Q(1,100000) < Q(1,4000)
    return Q(1,4000)


def main():
    crosscheck()
    smooth_radius = common_radius()
    means,errors=invert_frequency()
    errors += float(smooth_radius)
    numerical_interpolation = Q(1,3072)
    acquisition_loss = Q(9,2048)+Q(49169,2097152)+Q(1,32)
    combined_loss = float(numerical_interpolation+acquisition_loss)
    print("depth | lower gap vs filled | lower gap vs fixed reference | headroom vs 3/64")
    for depth in (4,5,6):
        target = min(means[depth,:,0]-errors[depth,:,0])
        filled = max(means[0,:,0]+errors[0,:,0])
        reference = max(means[depth,:,1]+errors[depth,:,1])
        bounds = [Q(floor((target-control-combined_loss)*10**6),10**6)
                  for control in (filled,reference)]
        assert min(bounds) > Q(3,64)
        print(f"{depth} | {float(bounds[0]):.6f} | {float(bounds[1]):.6f} | "
              f"{float(min(bounds)-Q(3,64)):.6f}")
    print(f"fourier tail, alias and scalar arithmetic allowance per arm: {smooth_radius}")
    print("PASS: independently bounded arm damping in [0, 1/512], fixed 3/64 gate")


if __name__ == "__main__":
    main()
