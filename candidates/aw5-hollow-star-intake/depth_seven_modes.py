"""Separate the fixed AW5 contrast into spectral grades and terminal sectors."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import pi

from mpmath import iv
import numpy as np

from adaptive_dtn_enclosure import blocks
from check_recursive_leaf_residue import cells_at_depth
from recursive_dtn import ALPHA, EXTERIOR_INDICES, PERIOD, midpoint_weights, response
from residue import ah, hf, matched

DEPTH = 7
CUTOFF = 16384
HARMONIC = Q(64,2315)


def dual_terminal(z, depth):
    """Inverse terminal eigenvalues of zI+B3.T B3, constant and differential."""
    a, lam_const = z+5, z+1
    for _ in range(1,depth):
        b = (lam_const-a)/4
        constant = a+b*(a-1)/(a-1+3*b)
        differential = a+b*(a*a-1)/(a*a-1+b*(3*a-1))
        lam_const, a = constant, differential
    return lam_const, a


def terminal_derivative(z):
    """Interval enclosures of terminal Schur eigenvalues and z derivatives."""
    a, c = z+5, z+1
    da, dc = iv.mpf(1), iv.mpf(1)
    for _ in range(1,DEPTH):
        b, db = (c-a)/4, (dc-da)/4
        u, v = a-1, a*a-1
        du, dv = da, 2*a*da
        d0 = u+3*b
        d1 = v+b*(3*a-1)
        assert d0 > 0 or d0 < 0
        assert d1 > 0 or d1 < 0
        dc = da+((db*u+b*du)*d0-b*u*(du+3*db))/(d0*d0)
        da_new = da+((db*v+b*dv)*d1-b*v*(dv+db*(3*a-1)+3*b*da))/(d1*d1)
        c, a, da = a+b*u/d0, a+b*v/d1, da_new
    return (c,a), (dc,da)


def x_fraction(x):
    return iv.mpf(x.numerator)/x.denominator


def pole_bracket(sector, left, right):
    """Certify a simple scalar pole and its midpoint-mean contribution."""
    a,b = Q(left),Q(right)
    def evaluate(x):
        return terminal_derivative(-x_fraction(x)**2)[0][sector]

    assert evaluate(a)>0 and evaluate(b)<0
    for _ in range(28):
        mid = (a+b)/2
        value = evaluate(mid)
        if value > 0:
            a = mid
        else:
            assert value < 0
            b = mid
    omega = iv.mpf([x_fraction(a).a,x_fraction(b).b])
    _, deriv = terminal_derivative(-omega**2)
    assert deriv[sector] > 0
    mass = 1/(omega**2*deriv[sector])
    contribution = mass*iv.sin(32*omega)/(512*iv.sin(omega/16))/2
    assert omega.delta < iv.mpf("1e-11")
    assert mass.delta < iv.mpf("1e-7") and contribution.delta < iv.mpf("1e-7")
    return omega,mass,contribution


def window_mean(s, weights, residual, initial):
    return initial + np.sum(np.real(weights*residual))/PERIOD


def total_undamped(s):
    M, probes, err = blocks(s,DEPTH)
    return response(s,M,probes,err,EXTERIOR_INDICES,0,95)


def crosscheck_dual():
    """Compare scalar recurrence to the full dual terminal inverse at shallow depth."""
    z = 1/3+2j/5
    constant_projection = np.ones((4,4))/4
    for depth in range(1,4):
        cells = cells_at_depth(depth)
        owners = defaultdict(list)
        for k,cell in enumerate(cells):
            for face in combinations(cell,3):
                owners[face].append(k)
        matrix = (z+4)*np.eye(len(cells),dtype=complex)
        for indices in owners.values():
            if len(indices)==2:
                i,j = indices
                matrix[i,j] = matrix[j,i] = -1
        ports = [owners[face][0] for face in combinations((0,1,2,3),3)]
        columns = np.eye(len(cells))[:,ports]
        direct = columns.T@np.linalg.solve(matrix,columns)
        a,b = dual_terminal(z,depth)
        expected = constant_projection/a+(np.eye(4)-constant_projection)/b
        assert np.max(abs(direct-expected)) < 1e-12
    print("PASS: constant/differential recurrence vs full dual at depths 1–3")


def main():
    iv.dps = 45
    crosscheck_dual()
    # The original signed outer surface is a closed 2-chain.
    assert all(value == 0 for value in ah[:hf.start,hf]*matched)
    for label,sector,a,b in (("constant A",0,"0.00648","0.00652"),
                             ("constant B",0,"0.02996","0.03001"),
                             ("differential A",1,"0.01282","0.01287")):
        omega,mass,part = pole_bracket(sector,a,b)
        print(f"{label}: omega={float(omega.mid):.11f}, mass={float(mass.mid):.9f}, "
              f"signed contrast={(-1 if sector else 1)*float(part.mid):.9f}")
    indices = np.arange(CUTOFF+1)
    s = ALPHA+1j*2*pi*indices/PERIOD
    w = midpoint_weights(indices)
    b0 = dual_terminal(0,DEPTH)
    spectrum = np.array([1/x for x in dual_terminal(s*s,DEPTH)])
    constant, differential = [window_mean(s,w,-g/s,1/b)
                            for b,g in zip(b0,spectrum)]
    total = np.zeros(2)
    total_error = np.zeros(2)
    for first in range(0,len(s),128):
        sl = slice(first,min(first+128,len(s)))
        f,err = total_undamped(s[sl])
        total += np.sum((w[sl,None]*(f-1/s[sl,None])).real,axis=0)/PERIOD
        total_error += np.sum(abs(w[sl,None])*err,axis=0)/PERIOD
    total += 1
    top_drive = (3*constant+differential)/4
    top_reference = (constant+3*differential)/4
    edge = total-[float(HARMONIC),0]-[top_drive,top_reference]
    print(f"terminal means: constant={constant:.12f}; differential={differential:.12f}")
    print(f"whole means {total}, numerical radii {total_error}")
    print(f"top-component means {top_drive:.12f}, {top_reference:.12f}; edge means {edge}")
    print(f"decomposition: harmonic {float(HARMONIC):.12f}; "
          f"constant {constant/2:.12f}; differential {-differential/2:.12f}; "
          f"edge difference {edge[0]-edge[1]:.12f}")
    assert abs(edge[0]) < 1e-10

if __name__ == "__main__":
    main()
