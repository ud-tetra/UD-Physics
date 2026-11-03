#!/usr/bin/env python3
"""Outward-rounded binary64 scalar bounds for all 4000 frozen A5 sector4 slabs.
WARNING: proof concerns the float-defined cubic spline, not the original ODE.
Requires frozen npz input from the separate local checkpoint 026 ZIP.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

UP = np.inf
def add_up(a, b): return np.nextafter(a + b, UP)
def mul_up(a, b): return np.nextafter(a * b, UP)

def verify(A, D, nodes, degree=20, radius=8):
    assert A.shape == D.shape and A.shape[0] == 4 and A.shape[2:] == (18,18)
    n = A.shape[1]
    assert nodes.shape == (n+1,) and n == 4000
    assert np.isfinite(A).all() and np.isfinite(D).all()
    assert np.isfinite(nodes).all() and np.all(np.diff(nodes)>0)
    hu = np.nextafter(np.diff(nodes), UP)
    assert np.all(hu < 0.1)
    powers = np.ones(n)
    norms = []
    for k in range(4):
        powers = mul_up(powers, hu)
        ka = np.abs(A[3-k]).transpose(0,2,1)
        ca = np.abs(D[3-k]).transpose(0,2,1)
        pk = np.nextafter(mul_up(ka, powers[:,None,None]) / 16, UP)
        pc = mul_up(ca, powers[:,None,None])
        rows = np.zeros((n,18))
        for column in range(18):
            rows = add_up(rows, pk[:,:,column])
            rows = add_up(rows, pc[:,:,column])
        m = rows.max(axis=1)
        if k == 0: m = np.maximum(m, mul_up(hu,16))
        norms.append(m)
    upper = np.zeros(n)
    for m in norms: upper = add_up(upper,m)
    index = int(upper.argmax())
    M = F.from_float(float(upper[index]))
    assert M < F(401,1000)
    Q = []
    for j in range(n):
        q = sum((F.from_float(float(norms[k][j])) * F(radius**(k+1),k+1)
                 for k in range(4)), F(0))
        Q.append(q)
    qmax = max(Q)
    assert qmax < F(321,100)
    tail = (1-qmax/F(64))**(-64)/F(radius**degree*(radius-1))
    assert tail < F(4,10**18)
    return {'status':'EXACT_UNIFORM_SPLINE_TAYLOR_TAIL_IEEE754_OUTWARD_ROUNDING',
            'intervals':n,'taylor_degree':degree,'cauchy_radius':radius,
            'M_max_rational':str(M),'M_max_float_display':float(M),
            'M_max_slab_index':index,'complex_exponent_Qmax_rational':str(qmax),
            'complex_exponent_Qmax_display':float(qmax),
            'complex_exponent_max_slab_index':Q.index(qmax),
            'global_degree20_Taylor_tail_bound_rational':str(tail),
            'global_degree20_Taylor_tail_bound_display':float(tail),
            'scope':'Exact dyadic polynomial coefficients plus outward IEEE754 operations only; original source interpolation and global 4000-product error not enclosed.'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--coeff',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    with np.load(a.coeff) as z:
        result=verify(z['A'],z['D'],z['nodes'])
    result['binary64_array_checksum_sha256']=hashlib.sha256(a.coeff.read_bytes()).hexdigest()
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],result['global_degree20_Taylor_tail_bound_display'])

if __name__=='__main__': main()
