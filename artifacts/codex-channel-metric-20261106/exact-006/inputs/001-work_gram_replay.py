"""Exact work-plane reconstruction and corner certificates."""
from fractions import Fraction as Q
from itertools import product
import json


def run():
    out={}
    for name,C in [('candidate',Q(3,2)),('uniform',Q(1))]:
        A,D=Q(1),Q(5,4)
        B=C-D-A/4
        assert B==(0 if name=='candidate' else Q(-1,2))
        W=lambda a,b:A*a*a+2*B*a*b+D*b*b
        assert (W(1,0),W(0,1),W(Q(1,2),1))==(A,D,C)
        assert W(Q(-1,2),1)==2*D+A/2-C
        # The bench radius per corrected work, in reference work units.
        e=Q(1857,20000)
        box=[(v-e,v+e) for v in (A,D,C)]
        det=lambda a,d,c:a*d-(c-d-a/4)**2
        floor=min(det(*z) for z in product(*box))
        assert box[0][0]>0 and floor>0
        for z in product(*(tuple(lo+(hi-lo)*Q(i,4) for i in range(5)) for lo,hi in box)):
            assert det(*z)>=floor
        out[name]={'cross':str(B),'fourth':str(W(Q(-1,2),1)),
                   'box_det_floor':str(floor)}
    extra=lambda a,b:a*a*b*b*(2*a-b)**2
    assert [extra(*v) for v in [(1,0),(0,1),(Q(1,2),1),(Q(-1,2),1)]]==[0,0,0,1]
    return out


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
