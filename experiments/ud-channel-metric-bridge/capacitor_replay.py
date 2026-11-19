"""Exact two-port capacitor and bounded-error audit."""
from fractions import Fraction as Q
from itertools import product
import json


def run():
    def inv(K):
        a,b=K[0]
        c,d=K[1]
        s=a*d-b*c
        return ((d/s,-b/s),(-c/s,a/s))

    eta=Q(1,100)
    other=Q(1,32)
    U=6*eta+16*eta**2+other
    assert U==Q(1857,20000) < Q(1,8)
    x,y,c=(1,0),(Q(-1,2),1),(0,1)
    networks={}
    for name,K in [('candidate',((Q(1),Q(1,2)),(Q(1,2),Q(3,2)))),
                   ('uniform',((Q(1),Q(0)),(Q(0),Q(1))))]:
        C=inv(K)
        assert inv(C)==K
        mutual=-C[0][1]
        ground=[sum(row) for row in C]
        assert min(mutual,*ground)>=0
        assert max(sum(map(abs,row)) for row in K)<=2
        def E(v):
            return sum(v[i]*K[i][j]*v[j] for i,j in product(range(2),repeat=2))
        w=list(map(E,(x,y,c)))
        s=w[2]-w[1]
        assert s==(Q(1,4) if name=='candidate' else Q(-1,4))
        for a,b in product((-U,U),repeat=2):
            assert (s+a-b>0)==(name=='candidate')
        networks[name]={'mutual':str(mutual),'ground':list(map(str,ground)),
                        'work_over_reference':list(map(str,w)),
                        'signed_discriminant':str(s)}
    return {'networks':networks,'endpoint_charge_fraction':str(eta),
            'other_per_receipt_budget':str(other),'total_per_receipt_budget':str(U),
            'decision_margin_over_reference':str(Q(1,4)-2*U)}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
