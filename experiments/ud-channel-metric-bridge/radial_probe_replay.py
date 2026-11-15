"""Exact box certificate for the bounded pure-J radial probe."""
import json
from collections import defaultdict
from fractions import Fraction as F
from math import comb

ETA = F(1, 100)
P = {(4, 2): 4, (3, 3): 4, (2, 4): 1}
J = {(i, j): F(4*c, 9) for (i, j), c in P.items()} | {
    (i+1, j+1): F(-5*c, 9) for (i, j), c in P.items()
}


def local_bound(r):
    terms = defaultdict(F)
    for (i,j),c in J.items():
        for k in range(i+1):
            for l in range(j+1):
                terms[k,l] += c*comb(i,k)*comb(j,l)*r**(i+j-k-l)
    return sum(abs(c)*ETA**(k+l) for (k,l),c in terms.items() if k+l)


def design(r):
    assert 0 < r < 1
    def qbound(t):
        return 8*ETA*t+16*ETA**2+F(1,32)
    j = lambda t: sum(c*t**(i+k) for (i,k),c in J.items())
    assert j(r) == r**6*(4-5*r*r) and j(F(1)) == -1
    signal = abs(j(F(1))-j(r)/r**2)/2
    null = qbound(F(1))+qbound(r)/r**2
    extra = (local_bound(F(1))+local_bound(r)/r**2+
             3*local_bound(F(0))*(1+1/r**2))/2
    return signal, null, extra, signal-2*null-extra


def run():
    rows = {F(k,100): design(F(k,100)) for k in range(1,100)}
    best = max(rows, key=lambda r: rows[r][-1])
    r = F(4,5)
    signal, null, extra, margin = rows[r]
    assert signal == F(4149,6250) and margin > F(46,1000)
    return {'grid_count': len(rows), 'grid_best': str(best),
            'grid_best_margin': str(rows[best][-1]),
            'selected_r': str(r), 'signal': str(signal), 'null_radius': str(null),
            'extra_alt_radius': str(extra), 'guaranteed_margin': str(margin)}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
