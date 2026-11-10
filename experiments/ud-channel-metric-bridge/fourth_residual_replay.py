"""Exact box support and fourth-port planning budget."""
from fractions import Fraction as Q
from itertools import product
import json


def budget(eta):
    b = 6*eta + 16*eta**2 + Q(1,32)
    bd = 8*eta + 16*eta**2 + Q(1,32)
    coeffs = (Q(-1,2), -2, 1, 1)  # x,y,c,d
    radii = (b,b,b,bd)
    corners = [sum(k*e for k,e in zip(coeffs,p))
               for p in product(*[(-r,r) for r in radii])]
    radius = bd + Q(7,2)*b
    assert (min(corners),max(corners)) == (-radius,radius)
    assert radius == 29*eta+72*eta**2+Q(9,64)
    return b,bd,radius


def run():
    b,bd,E = budget(Q(1,100))
    assert (b,bd,E) == (Q(1857,20000),Q(2257,20000),Q(17513,40000))
    assert Q(1,2)-E <= E < Q(1,2)
    improved = budget(Q(1,300))[2]
    assert improved == Q(28571,120000) < Q(1,4)
    for x,y,c,d in [(1,Q(5,4),Q(3,2),Q(3,2)),(1,Q(5,4),1,2)]:
        assert d+c-2*y-Q(x,2)==0
    return {k:str(v) for k,v in dict(original_radius=b,fourth_radius=bd,
           residual_radius=E,residual_radius_nJ=500*E,
           strict_gap_floor=2*E,improved_radius=improved).items()}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
