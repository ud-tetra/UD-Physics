"""Reproduce AW5 face-only pole residues with exact rational arithmetic."""
from itertools import combinations
from sympy import Matrix, eye, zeros

hub = (0, 1, 2, 3)
leaves = [tuple(j for j in hub if j != i) + (4+i,) for i in hub]

def model(cells):
    basis = [sorted({s for t in cells for s in combinations(t,k)}) for k in range(1,5)]
    n = [len(layer) for layer in basis]
    offsets = [0, n[0], sum(n[:2]), sum(n[:3]), sum(n)]
    B = zeros(sum(n))
    for k in range(3):
        lookup = {s: i for i,s in enumerate(basis[k])}
        for j,s in enumerate(basis[k+1]):
            for r in range(len(s)):
                i = lookup[s[:r]+s[r+1:]]
                B[offsets[k]+i,offsets[k+1]+j] = (-1)**r
    faces = slice(offsets[2], offsets[3])
    return basis, B[faces, offsets[3]:], B.T-B, faces

filled_basis, df, af, ff = model([hub]+leaves)
hollow_basis, dh, ah, hf = model(leaves)
assert filled_basis[2] == hollow_basis[2]
z = df[:,filled_basis[3].index(hub)]
h = z-dh*(dh.T*z)/4
ext = [i for i in range(len(z)) if sum(v != 0 for v in df.row(i)) == 1]
mask = eye(len(z))[:,ext]
p = mask*mask.T
matched = p*h
orthogonal = h[ext[1]]*mask[:,0]-h[ext[0]]*mask[:,1]

def embed(v, A, faces):
    result = zeros(A.rows,1)
    result[faces,0] = v
    return result

def check(A, faces, name, expected):
    def residues(G):
        K = Matrix.hstack(*G.nullspace())
        assert all(G.T*v == zeros(A.rows,1) for v in K.columnspace())
        H = K*(K.T*K).inv()*K.T
        return [(x.T*H*x)[0]/(x.T*x)[0] for x in
                (embed(v,A,faces) for v in (mask[:,0], matched, orthogonal))]
    M = zeros(A.rows)
    M[faces,faces] = p
    undamped = residues(A)
    damped = residues(A-M)
    assert undamped == expected and damped == [0,0,0]
    print(name, undamped, damped)

from sympy import Rational
check(af, ff, "filled", [0,0,0])
check(ah, hf, "hollow", [Rational(1,48),Rational(1,4),0])
