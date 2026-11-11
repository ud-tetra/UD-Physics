"""Exact native Q169 quarter-cycle map with pre-event integer admission."""
import itertools
import json
from native_compare import CELLS, INDEX, N, boundary, matmul, mv


def matrix():
    d = boundary()
    a = [[d[i][j] - d[j][i] for j in range(N)] for i in range(N)]
    aa = matmul(a, a)
    m = [[4 * (i == j) + 2 * a[i][j] + aa[i][j]
          for j in range(N)] for i in range(N)]
    return a, aa, m


def step(x, m):
    numerator = mv(m, x)
    if any(q % 4 for q in numerator):
        return x, 'HOLD_NONINTEGRAL'
    return [q // 4 for q in numerator], 'EVENT'


def transform(x, p):
    """Signed ascending-simplex action of a vertex permutation."""
    y = [0] * N
    for sigma, q in zip(CELLS, x):
        labels = tuple(p[i] for i in sigma)
        inversions = sum(labels[i] > labels[j]
                         for i in range(len(labels)) for j in range(i+1,len(labels)))
        y[INDEX[tuple(sorted(labels))]] = (-1)**inversions * q
    return y


def main():
    a, aa, m = matrix()
    assert all(matmul(aa, a)[i][j] == -4*a[i][j]
               for i in range(N) for j in range(N))
    # U=M/4; U^2=I+A^2/2, U^3=U-A, U^4=I.
    mm = matmul(m, m)
    assert all(mm[i][j] == 16*(i==j)+8*aa[i][j]
               for i in range(N) for j in range(N))
    m3 = matmul(mm, m)
    assert all(m3[i][j] == 16*(m[i][j]-4*a[i][j])
               for i in range(N) for j in range(N))
    m4 = matmul(m3, m)
    assert all(m4[i][j] == 256*(i==j)
               for i in range(N) for j in range(N))

    prepared = [0]*N
    prepared[INDEX[(0,)]]=1
    prepared[INDEX[(0,1)]]=2
    assert step(prepared,m)[1] == 'HOLD_NONINTEGRAL'
    x = [0]*N
    x[INDEX[(0,)]]=4
    path=[x]
    for _ in range(4):
        y, verdict=step(path[-1],m)
        assert verdict=='EVENT'
        path.append(y)
    assert path[4]==x and path[1]!=x
    assert all(sum(q*q for q in y)==16 and sum(y[:4])==4 for y in path)

    cases=[]
    for cell in range(N):
        for scale in (1,2,3,4,-4):
            initial=[0]*N
            initial[cell]=scale
            y, verdict=step(initial,m)
            if verdict=='EVENT':
                z=y
                for _ in range(3):
                    z, later=step(z,m)
                    assert later=='EVENT'
                assert z==initial
                assert sum(q*q for q in y)==sum(q*q for q in initial)
                assert sum(y[:4])==sum(initial[:4])
            else:
                assert y==initial
            for p in itertools.permutations(range(4)):
                yy,vv=step(transform(initial,p),m)
                assert (yy,vv)==(transform(y,p),verdict)
            cases.append(verdict)
    assert 'EVENT' in cases and 'HOLD_NONINTEGRAL' in cases

    # No nontrivial all-Z^15 U(s): an adjacent-grade matrix entry has
    # A_ij=±1 and (A²)_ij=0, so integrality forces sin(2s)/2 integer,
    # hence sin(2s)=0. cos(2s)=-1 gives vertex diagonal -1/2.
    assert a[INDEX[(0,)]][INDEX[(0,1)]]==-1
    assert aa[INDEX[(0,)]][INDEX[(0,1)]]==0
    assert aa[INDEX[(0,)]][INDEX[(0,)]]==-3

    labels=[('v' if len(c)==1 else 'e' if len(c)==2 else 'f' if len(c)==3 else 't')+
            ''.join(map(str,c)) for c in CELLS]
    print(json.dumps({
        'source':'Q169 native filled K4, A=d-d^T, A^3=-4A',
        'chosen_phase':'s=pi/4, active angle 2s=pi/2; not source-selected event time',
        'finite_map':'U=(4I+2A+A^2)/4, U^4=I',
        'pre_event_gate':'(2A+A^2)x == 0 mod 4 in every coordinate',
        'admitted_lattice':'L={x in Z^15: Ux in Z^15}; U(L)=L, contains 4Z^15',
        'hold_rule':'identity when gate fails',
        'no_go':'exp(sA) preserves all Z^15 only when exp(sA)=I on this carrier',
        'prepared_v0_plus_2e01_verdict':step(prepared,m)[1],
        'four_v0_orbit':[{labels[i]:q for i,q in enumerate(y) if q} for y in path],
        'unit_basis_cases':len(cases),
        'unit_basis_events':cases.count('EVENT'),
        'unit_basis_holds':cases.count('HOLD_NONINTEGRAL'),
        'signed_S4_singleton_checks':len(cases)*24,
        'invariants':'unit Euclidean norm squared and total vertex amplitude',
        'physical_promotion':0
    },indent=2))


if __name__=='__main__':
    main()
